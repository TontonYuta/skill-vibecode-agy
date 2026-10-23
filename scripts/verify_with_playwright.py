#!/usr/bin/env python3
"""
verify_with_playwright.py
Công cụ tự động hóa Playwright cho Vibecoding Hub:
1. Chế độ 'verify-papers': Quét và kiểm định tính xác thực của các bài báo arXiv 2025-2026.
2. Chế độ 'test-app': Kiểm tra giao diện và bắt lỗi console/network của ứng dụng web được vibecode.
"""

import sys
import json
import argparse
from playwright.sync_api import sync_playwright

def verify_paper(paper_id):
    url = f"https://arxiv.org/abs/{paper_id}"
    print(f"[*] Đang kiểm tra bài báo: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=15000)
            title = page.locator("h1.title").inner_text().replace("Title:", "").strip()
            authors = page.locator("div.authors").inner_text().replace("Authors:", "").strip()
            print(f"✅ Xác minh thành công:")
            print(f"   - Tiêu đề: {title}")
            print(f"   - Tác giả: {authors}")
            browser.close()
            return True
        except Exception as e:
            print(f"❌ Lỗi xác minh {paper_id}: {e}")
            browser.close()
            return False

def test_web_app(url, output_screenshot="screenshot.png"):
    print(f"[*] Đang kiểm thử ứng dụng Vibecode tại: {url}")
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Bắt lỗi console
        page.on("console", lambda msg: errors.append(f"[Console {msg.type}] {msg.text}") if msg.type in ["error", "warning"] else None)
        # Bắt lỗi HTTP 4xx, 5xx
        page.on("response", lambda resp: errors.append(f"[HTTP {resp.status}] {resp.url}") if resp.status >= 400 else None)
        
        try:
            page.goto(url, timeout=15000, wait_until="networkidle")
            page.screenshot(path=output_screenshot, full_page=True)
            print(f"✅ Đã chụp ảnh màn hình lưu tại: {output_screenshot}")
            
            if errors:
                print(f"⚠️ Phát hiện {len(errors)} cảnh báo/lỗi trong ứng dụng:")
                for err in errors[:5]:
                    print(f"   - {err}")
            else:
                print("🎉 Ứng dụng sạch lỗi, không phát hiện lỗi console hoặc HTTP 4xx/5xx!")
        except Exception as e:
            print(f"❌ Lỗi khi tải trang {url}: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Playwright Verification Tool for Vibecoding")
    subparsers = parser.add_subparsers(dest="command")
    
    paper_parser = subparsers.add_parser("verify-paper")
    paper_parser.add_argument("paper_id", help="Mã bài báo arXiv (ví dụ: 2610.14766)")
    
    app_parser = subparsers.add_parser("test-app")
    app_parser.add_argument("url", help="URL ứng dụng (ví dụ: http://localhost:3000)")
    app_parser.add_argument("--screenshot", default="app_verification.png", help="Đường dẫn lưu ảnh chụp màn hình")
    
    args = parser.parse_args()
    if args.command == "verify-paper":
        verify_paper(args.paper_id)
    elif args.command == "test-app":
        test_web_app(args.url, args.screenshot)
    else:
        parser.print_help()
