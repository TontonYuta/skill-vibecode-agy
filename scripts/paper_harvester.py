#!/usr/bin/env python3
"""
scripts/paper_harvester.py
Công cụ tự động hóa nghiên cứu & thu thập bài báo khoa học cho Vibecoding:
1. Chế độ Siêu Nhẹ (Fast API/HTTPX): Dùng arXiv API để lấy metadata, abstract và tải PDF cực nhanh (tiết kiệm 95% RAM).
2. Chế độ Playwright Headless: Khi cần vượt qua trang web JavaScript động hoặc chụp ảnh minh chứng nghiên cứu.
"""

import sys
import os
import json
import argparse
import xml.etree.ElementTree as ET
import httpx
from playwright.sync_api import sync_playwright

def harvest_via_api(query_or_id, max_results=3, download_pdf=False, output_dir="harvested_papers"):
    """
    Sử dụng HTTPX gọi arXiv API thuần túy.
    Tốc độ: < 1 giây, Tiêu thụ RAM: ~15MB (Thay vì 500MB của Chrome).
    """
    os.makedirs(output_dir, exist_ok=True)
    is_id = all(c.isdigit() or c == '.' for c in query_or_id)
    
    if is_id:
        url = f"https://export.arxiv.org/api/query?id_list={query_or_id}"
    else:
        url = f"https://export.arxiv.org/api/query?search_query=all:{query_or_id}&start=0&max_results={max_results}"
        
    print(f"[*] Đang tra cứu arXiv API (Fast HTTPX): {query_or_id}...")
    headers = {"User-Agent": "Antigravity-Vibecoding-Researcher/2.0"}
    
    try:
        response = httpx.get(url, headers=headers, follow_redirects=True, timeout=15.0)
        response.raise_for_status()
        
        root = ET.fromstring(response.text)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = root.findall('atom:entry', ns)
        if not entries:
            print(f"[-] Không tìm thấy bài báo nào cho: {query_or_id}")
            return []
            
        results = []
        for entry in entries:
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            published = entry.find('atom:published', ns).text.strip()
            id_url = entry.find('atom:id', ns).text.strip()
            paper_id = id_url.split('/abs/')[-1]
            authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
            
            pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
            
            paper_data = {
                "id": paper_id,
                "title": title,
                "authors": authors,
                "published": published,
                "abstract": summary,
                "pdf_url": pdf_url,
                "abs_url": id_url
            }
            results.append(paper_data)
            
            print(f"\n📄 [arXiv:{paper_id}] {title}")
            print(f"   👥 Tác giả: {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''}")
            print(f"   📝 Abstract: {summary[:180]}...")
            
            if download_pdf:
                pdf_path = os.path.join(output_dir, f"{paper_id}.pdf")
                if not os.path.exists(pdf_path):
                    print(f"   ⬇️ Đang tải PDF về: {pdf_path}...")
                    pdf_resp = httpx.get(pdf_url, headers=headers, follow_redirects=True, timeout=30.0)
                    with open(pdf_path, "wb") as f:
                        f.write(pdf_resp.content)
                    print(f"   ✅ Đã tải xong: {pdf_path}")
                else:
                    print(f"   ℹ️ Tệp PDF đã tồn tại cục bộ: {pdf_path}")
                    
        # Lưu kết quả ra JSON có cấu trúc cho AI Agent đọc
        json_path = os.path.join(output_dir, "research_summary.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Đã lưu cấu trúc nghiên cứu ra: {json_path}")
        return results
        
    except Exception as e:
        print(f"❌ Lỗi khi tra cứu API: {e}")
        return []

def harvest_via_playwright(paper_id, output_dir="harvested_papers"):
    """
    Sử dụng Playwright Headless khi cần tương tác DOM, chụp ảnh chụp trang hoặc cào các trang web có JS động.
    """
    os.makedirs(output_dir, exist_ok=True)
    url = f"https://arxiv.org/abs/{paper_id}"
    screenshot_path = os.path.join(output_dir, f"{paper_id}_evidence.png")
    
    print(f"[*] Đang khởi chạy Playwright Chromium để thẩm định: {url}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=20000)
            title = page.locator("h1.title").inner_text().replace("Title:", "").strip()
            abstract = page.locator("blockquote.abstract").inner_text().replace("Abstract:", "").strip()
            page.screenshot(path=screenshot_path)
            
            print(f"✅ [Playwright Success]")
            print(f"   - Tiêu đề: {title}")
            print(f"   - Abstract: {abstract[:180]}...")
            print(f"   - Ảnh minh chứng: {screenshot_path}")
            
            return {"id": paper_id, "title": title, "abstract": abstract, "screenshot": screenshot_path}
        except Exception as e:
            print(f"❌ Lỗi Playwright: {e}")
            return None
        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paper Harvester & Researcher for Vibecoding")
    parser.add_argument("query", help="Mã bài báo arXiv (ví dụ: 2610.14766) hoặc từ khóa tìm kiếm (ví dụ: 'agentic software engineering')")
    parser.add_argument("--mode", choices=["fast", "playwright"], default="fast", help="Chế độ cào: 'fast' (HTTPX API siêu nhẹ) hoặc 'playwright' (Browser automation)")
    parser.add_argument("--download-pdf", action="store_true", help="Tải trực tiếp tệp PDF về máy")
    parser.add_argument("--limit", type=int, default=3, help="Số lượng kết quả tối đa khi tìm kiếm")
    parser.add_argument("--output-dir", default="harvested_papers", help="Thư mục lưu trữ kết quả")
    
    args = parser.parse_args()
    if args.mode == "fast":
        harvest_via_api(args.query, max_results=args.limit, download_pdf=args.download_pdf, output_dir=args.output_dir)
    else:
        harvest_via_playwright(args.query, output_dir=args.output_dir)
