#!/usr/bin/env python3
"""
scripts/self_healing_test_runner.py
Công cụ kiểm thử webapp tự động & xuất phản hồi có cấu trúc cho AI Agent tự sửa lỗi:
1. Lắng nghe toàn bộ 4 kênh lỗi: Console Error, Page Error (Uncaught JS), Network 4xx/5xx, và Request Failed.
2. Tự động chụp ảnh màn hình minh chứng lỗi khi có sự cố.
3. Xuất tệp 'agent_feedback.json' chuẩn hóa để AI Agent (Antigravity/Cursor/Claude) đọc, khoanh vùng mã nguồn và sửa chữa.
4. Trả về Exit Code 1 khi có lỗi và Exit Code 0 khi hoàn toàn sạch bóng lỗi (Loop-until-green).
"""

import sys
import os
import json
import argparse
from datetime import datetime
from playwright.sync_api import sync_playwright

def run_self_healing_audit(url, output_dir="test_reports", timeout_ms=15000, interactive_click=False):
    os.makedirs(output_dir, exist_ok=True)
    feedback_file = os.path.join(output_dir, "agent_feedback.json")
    screenshot_file = os.path.join(output_dir, "failure_screenshot.png")
    
    console_errors = []
    console_warnings = []
    page_exceptions = []
    network_failures = []
    
    print(f"[*] [Self-Healing Test Runner] Khởi động kiểm thử: {url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        
        # 1. Bắt Console Logs
        def handle_console(msg):
            if msg.type == "error":
                console_errors.append({
                    "text": msg.text,
                    "location": msg.location
                })
            elif msg.type == "warning":
                console_warnings.append(msg.text)
                
        page.on("console", handle_console)
        
        # 2. Bắt ngoại lệ JavaScript chưa được xử lý (Uncaught Exceptions)
        def handle_pageerror(exc):
            page_exceptions.append({
                "message": str(exc),
                "type": type(exc).__name__
            })
        page.on("pageerror", handle_pageerror)
        
        # 3. Bắt lỗi phản hồi HTTP (4xx, 5xx)
        def handle_response(resp):
            if resp.status >= 400:
                network_failures.append({
                    "url": resp.url,
                    "status": resp.status,
                    "status_text": resp.status_text
                })
        page.on("response", handle_response)
        
        # 4. Bắt lỗi yêu cầu mạng bị ngắt (CORS, DNS, Connection Refused)
        def handle_requestfailed(req):
            failure = req.failure
            network_failures.append({
                "url": req.url,
                "status": "REQUEST_FAILED",
                "error_text": str(failure)
            })
        page.on("requestfailed", handle_requestfailed)
        
        try:
            # Điều hướng đến ứng dụng
            response = page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            
            # Thao tác tương tác thử nghiệm nếu được bật
            if interactive_click:
                buttons = page.locator("button:visible").all()
                print(f"[*] Phát hiện {len(buttons)} nút bấm, đang thử kích hoạt nút đầu tiên...")
                if buttons:
                    buttons[0].click(timeout=3000)
                    page.wait_for_timeout(1000) # Đợi phản ứng
                    
        except Exception as e:
            page_exceptions.append({
                "message": f"Navigation Fatal Error: {str(e)}",
                "type": "NavigationTimeoutOrCrash"
            })
            
        total_errors = len(console_errors) + len(page_exceptions) + len(network_failures)
        is_passed = (total_errors == 0)
        
        # Chụp ảnh màn hình làm bằng chứng
        page.screenshot(path=screenshot_file, full_page=True)
        browser.close()
        
    # Tạo chỉ dẫn hành động tự động cho Agent
    recommended_actions = []
    if page_exceptions:
        recommended_actions.append("Kiểm tra lại cú pháp JS/React Hydration mismatch hoặc thuộc tính null/undefined.")
    if network_failures:
        recommended_actions.append("Kiểm tra lại cấu hình CORS, endpoint API, biến môi trường (PORT, URL) hoặc backend server chưa chạy.")
    if console_errors:
        recommended_actions.append("Tra soát lại console.error để sửa chữa component liên quan.")
        
    feedback_data = {
        "timestamp": datetime.now().isoformat(),
        "target_url": url,
        "status": "PASSED" if is_passed else "FAILED",
        "summary": {
            "total_errors": total_errors,
            "console_errors_count": len(console_errors),
            "page_exceptions_count": len(page_exceptions),
            "network_failures_count": len(network_failures),
            "warnings_count": len(console_warnings)
        },
        "details": {
            "page_exceptions": page_exceptions,
            "console_errors": console_errors,
            "network_failures": network_failures,
            "warnings": console_warnings[:5]
        },
        "artifacts": {
            "screenshot": screenshot_file
        },
        "recommended_action_for_agent": recommended_actions if recommended_actions else ["Mọi thứ xanh hoàn hảo! Không cần sửa chữa mã nguồn."]
    }
    
    with open(feedback_file, "w", encoding="utf-8") as f:
        json.dump(feedback_data, f, ensure_ascii=False, indent=2)
        
    print("\n" + "="*60)
    if is_passed:
        print(f"🎉 [TEST PASSED] Ứng dụng tại {url} sạch bóng lỗi!")
        print(f"📊 Báo cáo lưu tại: {feedback_file}")
        print("="*60)
        return 0
    else:
        print(f"❌ [TEST FAILED] Phát hiện {total_errors} lỗi cần sửa:")
        print(f"   - Ngoại lệ trang: {len(page_exceptions)}")
        print(f"   - Lỗi console: {len(console_errors)}")
        print(f"   - Lỗi mạng/API: {len(network_failures)}")
        print(f"📸 Ảnh chụp hiện trạng: {screenshot_file}")
        print(f"💾 Báo cáo cho Agent: {feedback_file}")
        print("💡 Gợi ý sửa: " + "; ".join(recommended_actions))
        print("="*60)
        return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Self-Healing WebApp Test Runner for Vibecoding Agents")
    parser.add_argument("url", help="URL ứng dụng (ví dụ: http://localhost:3000 hoặc file HTML)")
    parser.add_argument("--output-dir", default="test_reports", help="Thư mục xuất báo cáo")
    parser.add_argument("--timeout", type=int, default=15000, help="Thời gian chờ tối đa (ms)")
    parser.add_argument("--interactive", action="store_true", help="Kích hoạt bấm thử các nút giao diện")
    
    args = parser.parse_args()
    exit_code = run_self_healing_audit(args.url, output_dir=args.output_dir, timeout_ms=args.timeout, interactive_click=args.interactive)
    sys.exit(exit_code)
