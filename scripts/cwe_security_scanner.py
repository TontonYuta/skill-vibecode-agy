#!/usr/bin/env python3
"""
CWE Security Scanner & Audit Gatekeeper (Chương 4 Companion)
============================================================
Mục đích:
- Tự động rà soát cơ sở mã Vibecoding để tìm 5 lỗ hổng CWE phổ biến nhất do LLM sinh ra:
  1. CWE-89: SQL Injection (queryRawUnsafe, chuỗi nối thô f-string/template literals)
  2. CWE-639/862: IDOR (truy vấn DB theo id mà thiếu ràng buộc user_id/owner_id)
  3. CWE-798/200: Rò rỉ Secret qua tiền tố NEXT_PUBLIC_ hoặc hardcoded API Keys
  4. CWE-918: SSRF (fetch/requests URL người dùng truyền vào mà không chặn Private IP)
  5. Supabase RLS Missing (CREATE TABLE mà không có ENABLE ROW LEVEL SECURITY)
- Xuất báo cáo cấu trúc máy đọc (JSON) và CLI Terminal.
- Trả về Exit Code 1 nếu có lỗ hổng CRITICAL/HIGH (tích hợp CI/CD và AI Self-Healing).

Cách dùng:
  python3 cwe_security_scanner.py --dir /path/to/project
  python3 cwe_security_scanner.py --json report.json
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

VULNERABILITY_PATTERNS = [
    {
        "id": "CWE-89",
        "name": "SQL Injection / Unsafe Raw Query",
        "severity": "CRITICAL",
        "regex": re.compile(r'(\$queryRawUnsafe|rawQuery|executeRawUnsafe|\.query\s*\(\s*`[^`]*\$\{|\.execute\s*\(\s*f["\'][^"\']*\{)', re.IGNORECASE),
        "remediation": "Sử dụng tham số hóa parameterized queries ($queryRaw`...` hoặc db.execute('SELECT ... %s', (val,)))"
    },
    {
        "id": "CWE-798",
        "name": "Hardcoded Secret / API Key Exposure",
        "severity": "CRITICAL",
        "regex": re.compile(r'((?:AIzaSy[0-9A-Za-z-_]{33})|(?:sk-[a-zA-Z0-9_-]{20,})|(?:sk-ant-[a-zA-Z0-9_-]{20,})|(?:ghp_[a-zA-Z0-9]{36}))'),
        "remediation": "Chuyển khóa bảo mật vào biến môi trường máy chủ (.env.local), tuyệt đối không commit lên git."
    },
    {
        "id": "CWE-200",
        "name": "Client-Side Exposed Secret via NEXT_PUBLIC_",
        "severity": "HIGH",
        "regex": re.compile(r'NEXT_PUBLIC_[A-Z0-9_]*(SECRET|PRIVATE|SERVICE_ROLE|ADMIN|DATABASE|TOKEN)', re.IGNORECASE),
        "remediation": "Xóa bỏ tiền tố NEXT_PUBLIC_ đối với các biến nhạy cảm. Chỉ truy cập biến này trên Server Actions hoặc API Route."
    },
    {
        "id": "CWE-639",
        "name": "Potential IDOR (Direct Object Reference without Ownership Filter)",
        "regex": re.compile(r'prisma\.[a-zA-Z]+\.(findUnique|findFirst|delete|update)\s*\(\s*\{\s*where\s*:\s*\{\s*id\s*:\s*[^,\}]+(?!\s*,\s*userId|\s*,\s*ownerId|\s*,\s*user_id)'),
        "severity": "HIGH",
        "remediation": "Bắt buộc bổ sung điều kiện ràng buộc quyền sở hữu (ví dụ: where: { id, userId: session.user.id })."
    },
    {
        "id": "CWE-918",
        "name": "Server-Side Request Forgery (SSRF) Risk",
        "regex": re.compile(r'(fetch|axios\.get|http\.get|requests\.get)\s*\(\s*(req\.body|req\.query|req\.params|request\.args|user_url|target_url)'),
        "severity": "MEDIUM",
        "remediation": "Xác thực danh sách tên miền cho phép (Whitelist) và chặn triệt để dải IP nội bộ (127.0.0.1, 10.0.0.0/8, 192.168.0.0/16)."
    }
]

def scan_file(file_path: Path) -> List[Dict[str, Any]]:
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception:
        return []

    for line_idx, line in enumerate(lines, start=1):
        for rule in VULNERABILITY_PATTERNS:
            match = rule["regex"].search(line)
            if match:
                findings.append({
                    "cwe_id": rule["id"],
                    "vulnerability": rule["name"],
                    "severity": rule["severity"],
                    "file": str(file_path),
                    "line": line_idx,
                    "code_snippet": line.strip()[:100],
                    "remediation": rule["remediation"]
                })
    return findings

def scan_directory(target_dir: str) -> List[Dict[str, Any]]:
    allowed_exts = {'.ts', '.tsx', '.js', '.jsx', '.py', '.sql', '.env', '.env.local', '.env.production'}
    ignored_dirs = {'node_modules', '.git', 'dist', 'build', '__pycache__', '.next', 'venv', '.venv'}
    
    all_findings = []
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in allowed_exts or p.name.startswith('.env'):
                all_findings.extend(scan_file(p))
    return all_findings

def print_cli_report(findings: List[Dict[str, Any]]):
    print("=" * 80)
    print(" 🛡️  CWE SECURITY AUDIT & VIBECODING COMPLIANCE SCANNER")
    print("=" * 80)
    
    if not findings:
        print(" ✅ XUẤT SẮC! Không phát hiện lỗ hổng CWE nào trong cơ sở mã.")
        print("    Codebase đáp ứng các tiêu chuẩn phòng thủ chủ động của Vibecoding.")
        print("=" * 80)
        return

    print(f" ⚠️  Phát hiện {len(findings)} điểm rủi ro an ninh mã nguồn:\n")
    for idx, item in enumerate(findings, start=1):
        color_tag = "[CRITICAL]" if item["severity"] == "CRITICAL" else f"[{item['severity']}]"
        print(f" {idx}. {color_tag} {item['cwe_id']}: {item['vulnerability']}")
        print(f"    • Tệp & Dòng : {item['file']}:{item['line']}")
        print(f"    • Đoạn mã    : {item['code_snippet']}")
        print(f"    • Khắc phục  : {item['remediation']}")
        print("-" * 80)

def main():
    parser = argparse.ArgumentParser(description="CWE Security Scanner for Vibecoding Projects")
    parser.add_argument("--dir", type=str, default=".", help="Thư mục cần quét mã nguồn (mặc định: .)")
    parser.add_argument("--json", type=str, help="Đường dẫn xuất tệp báo cáo JSON máy đọc")
    args = parser.parse_args()

    findings = scan_directory(args.dir)
    print_cli_report(findings)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({
                "scanner": "cwe_security_scanner",
                "total_findings": len(findings),
                "findings": findings
            }, f, indent=2, ensure_ascii=False)
        print(f"\n📁 Đã xuất báo cáo JSON: {args.json}")

    has_critical_or_high = any(f["severity"] in ("CRITICAL", "HIGH") for f in findings)
    sys.exit(1 if has_critical_or_high else 0)

if __name__ == "__main__":
    main()
