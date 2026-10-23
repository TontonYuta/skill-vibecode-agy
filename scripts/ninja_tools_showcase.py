#!/usr/bin/env python3
"""
scripts/ninja_tools_showcase.py
Trình diễn các vũ khí ninja nguồn mở cho Vibecoder:
1. Jina Reader (r.jina.ai): Bóc tách Markdown từ bất kỳ URL nào trong 1 giây mà KHÔNG cần mở trình duyệt.
2. SQLite FTS5 (Full-Text Search): Tạo bộ tìm kiếm toàn văn siêu tốc cục bộ chỉ bằng Python thuần.
3. Cloudflared Tunnel: Mở cổng localhost ra Internet công khai (HTTPS) không cần cấu hình Router.
"""

import sys
import os
import sqlite3
import httpx
import argparse

def fetch_markdown_via_jina(url):
    """
    Kỹ thuật Jina Reader Ninja: Thêm tiền tố 'https://r.jina.ai/' vào trước bất kỳ URL nào.
    Tiết kiệm 100% tài nguyên so với việc khởi chạy Chromium/Playwright.
    """
    jina_url = f"https://r.jina.ai/{url}"
    print(f"[*] [Jina Reader Ninja] Đang bóc tách Markdown từ: {url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "X-No-Cache": "true"
    }
    try:
        resp = httpx.get(jina_url, headers=headers, timeout=15.0)
        resp.raise_for_status()
        print(f"✅ Bóc tách thành công! Độ dài văn bản: {len(resp.text)} ký tự.")
        print("="*60)
        print(resp.text[:500] + "\n...[Nội dung còn tiếp]...")
        print("="*60)
        return resp.text
    except Exception as e:
        print(f"❌ Lỗi Jina Reader: {e}")
        return None

def demo_sqlite_fts5(db_path="/tmp/vibecoding_fts5.db"):
    """
    Kỹ thuật SQLite FTS5: Xây dựng cơ sở dữ liệu tìm kiếm toàn văn cục bộ trong 15 dòng code.
    Không cần cài đặt Elasticsearch hay Meilisearch cồng kềnh.
    """
    print(f"[*] [SQLite FTS5 Ninja] Khởi tạo cơ sở dữ liệu tìm kiếm toàn văn tại: {db_path}...")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Tạo bảng ảo FTS5 hỗ trợ tìm kiếm toàn văn
    cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS documents USING fts5(title, content, tags);")
    cur.execute("DELETE FROM documents;") # Reset dữ liệu mẫu
    
    # Nạp dữ liệu mẫu
    sample_docs = [
        ("Kỹ nghệ Playwright", "Playwright điều khiển Chromium không đầu, bắt console.error và chụp ảnh screenshot.", "automation,browser"),
        ("Bản đồ yt-dlp & FFmpeg", "yt-dlp bóc tách phụ đề VTT, FFmpeg nén video H.264 và chuẩn hóa audio 16kHz cho Whisper.", "media,video,audio"),
        ("Tự động hóa Android ADB", "scrcpy stream video qua Unix socket, ADB bắn lệnh input tap và trích xuất UIAutomator XML.", "mobile,android,scrcpy"),
        ("PocketBase Siêu Nhẹ", "PocketBase là file binary Go duy nhất chứa SQLite, Auth, Realtime thay thế hoàn toàn Supabase cho MVP.", "backend,sqlite,database")
    ]
    cur.executemany("INSERT INTO documents(title, content, tags) VALUES (?, ?, ?);", sample_docs)
    conn.commit()
    
    # Thực hiện truy vấn tìm kiếm toàn văn (Full-Text Search Query)
    search_query = "FFmpeg OR ADB OR PocketBase"
    print(f"[*] Thực hiện tìm kiếm FTS5 với từ khóa: '{search_query}'...")
    cur.execute("SELECT title, snippet(documents, 1, '<b>', '</b>', '...', 10) FROM documents WHERE documents MATCH ? ORDER BY rank;", (search_query,))
    results = cur.fetchall()
    
    print(f"🎯 Tìm thấy {len(results)} kết quả khớp chính xác:")
    for r in results:
        print(f"   📌 {r[0]}: {r[1]}")
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ninja Tools Showcase for Vibecoders")
    parser.add_argument("--jina", help="URL cần chuyển đổi sang Markdown sạch (ví dụ: https://example.com)")
    parser.add_argument("--fts5", action="store_true", help="Chạy thử nghiệm SQLite FTS5 Full-Text Search cục bộ")
    
    args = parser.parse_args()
    if args.jina:
        fetch_markdown_via_jina(args.jina)
    elif args.fts5:
        demo_sqlite_fts5()
    else:
        # Mặc định chạy cả 2
        demo_sqlite_fts5()
        print("\n")
        fetch_markdown_via_jina("https://example.com")
