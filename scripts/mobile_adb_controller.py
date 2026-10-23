#!/usr/bin/env python3
"""
scripts/mobile_adb_controller.py
Bộ công cụ điều khiển và tự động hóa Android qua ADB & scrcpy:
1. Liệt kê các thiết bị Android kết nối qua USB hoặc Wi-Fi.
2. Chụp ảnh màn hình trực tiếp từ framebuffer thiết bị (không cần lưu tạm trên máy).
3. Gửi lệnh chạm (tap), vuốt (swipe), gõ chữ (input text), hoặc phím cứng (KeyEvent).
4. Bóc tách cây giao diện UI XML (UIAutomator) để AI Agent tự tìm tọa độ nút bấm mà không cần mã nguồn app.
"""

import subprocess
import sys
import os
import argparse
import xml.etree.ElementTree as ET

def run_adb(args):
    cmd = ["adb"] + args
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except FileNotFoundError:
        return "ERROR_NO_ADB: Không tìm thấy lệnh 'adb'. Cài đặt qua: sudo apt install adb (Linux) hoặc winget install Google.PlatformTools (Windows)."
    except subprocess.CalledProcessError as e:
        return f"ERROR_ADB_FAILED: {e.stderr.strip()}"

def list_devices():
    out = run_adb(["devices"])
    print("[*] Danh sách thiết bị Android kết nối:")
    print(out)
    return out

def capture_screenshot(output_path="android_screen.png"):
    print(f"[*] Đang chụp ảnh màn hình Android lưu vào: {output_path}...")
    try:
        # Kỹ thuật Hacker: Stream trực tiếp byte ảnh từ framebuffer qua stdout, bỏ qua ổ nhớ điện thoại
        with open(output_path, "wb") as f:
            proc = subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=f, stderr=subprocess.PIPE)
            if proc.returncode == 0:
                print(f"✅ Đã chụp màn hình thành công: {output_path}")
                return True
            else:
                print(f"❌ Lỗi chụp ảnh: {proc.stderr.decode('utf-8', errors='ignore')}")
                return False
    except Exception as e:
        print(f"❌ Ngoại lệ khi chụp ảnh: {e}")
        return False

def tap(x, y):
    print(f"[*] Chạm màn hình tại tọa độ ({x}, {y})...")
    res = run_adb(["shell", "input", "tap", str(x), str(y)])
    print(f"✅ Kết quả: {res if res else 'Thao tác hoàn tất'}")

def type_text(text):
    safe_text = text.replace(" ", "%s") # ADB quy ước khoảng trắng là %s
    print(f"[*] Nhập văn bản: '{text}'...")
    res = run_adb(["shell", "input", "text", safe_text])
    print(f"✅ Kết quả: {res if res else 'Thao tác hoàn tất'}")

def dump_ui_and_find_text(target_text):
    """
    Bóc tách cây DOM của Android qua UIAutomator, tìm tọa độ của phần tử chứa text.
    """
    print(f"[*] Đang bóc tách cây UI để tìm chuỗi: '{target_text}'...")
    run_adb(["shell", "uiautomator", "dump", "/sdcard/window_dump.xml"])
    xml_content = run_adb(["shell", "cat", "/sdcard/window_dump.xml"])
    
    if "ERROR" in xml_content or not xml_content.startswith("<?xml"):
        print("[-] Không trích xuất được UIAutomator XML hoặc chưa có thiết bị kết nối.")
        return None
        
    root = ET.fromstring(xml_content)
    found_bounds = None
    for node in root.iter('node'):
        text = node.attrib.get('text', '')
        desc = node.attrib.get('content-desc', '')
        if target_text.lower() in text.lower() or target_text.lower() in desc.lower():
            bounds = node.attrib.get('bounds') # Dạng [x1,y1][x2,y2]
            print(f"🎯 Tìm thấy phần tử khớp: text='{text}', bounds={bounds}")
            # Tính toán tâm nút bấm: [100,200][300,250] -> x=(100+300)/2=200, y=(200+250)/2=225
            raw = bounds.replace('][', ',').replace('[', '').replace(']', '').split(',')
            x1, y1, x2, y2 = map(int, raw)
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            found_bounds = (center_x, center_y)
            break
            
    if found_bounds:
        print(f"💡 Tọa độ tâm để click: X={found_bounds[0]}, Y={found_bounds[1]}")
    else:
        print(f"[-] Không tìm thấy phần tử nào chứa: '{target_text}'")
    return found_bounds

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hacker ADB & Android Automation Tool")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("devices", help="Liệt kê thiết bị kết nối")
    
    cap_parser = subparsers.add_parser("screenshot", help="Chụp màn hình")
    cap_parser.add_argument("--out", default="android_screen.png", help="Đường dẫn lưu ảnh")
    
    tap_parser = subparsers.add_parser("tap", help="Chạm tọa độ")
    tap_parser.add_argument("x", type=int, help="Tọa độ X")
    tap_parser.add_argument("y", type=int, help="Tọa độ Y")
    
    type_parser = subparsers.add_parser("type", help="Nhập văn bản")
    type_parser.add_argument("text", help="Chuỗi văn bản")
    
    find_parser = subparsers.add_parser("find-click", help="Tìm text trên màn hình và lấy tọa độ")
    find_parser.add_argument("text", help="Chữ cần tìm trên màn hình app")
    
    args = parser.parse_args()
    if args.command == "devices":
        list_devices()
    elif args.command == "screenshot":
        capture_screenshot(args.out)
    elif args.command == "tap":
        tap(args.x, args.y)
    elif args.command == "type":
        type_text(args.text)
    elif args.command == "find-click":
        dump_ui_and_find_text(args.text)
    else:
        parser.print_help()
