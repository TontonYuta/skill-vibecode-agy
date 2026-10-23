#!/usr/bin/env python3
"""
tailieu_latex/chuong_02_phan_tich_nghiep_vu_va_mvp_scoping/socratic_spec_builder.py
Công cụ hỗ trợ phân tích nghiệp vụ & sinh tệp đặc tả kỹ thuật spec.md:
1. Áp dụng quy tắc Jobs-to-be-Done (JTBD) 3 vế chuẩn mực.
2. Sàng lọc MoSCoW và tự động kích hoạt "Quy tắc Cắt 50% tính năng râu ria".
3. Xuất tệp 'spec.md' chuẩn máy đọc được cho AI Agent.
"""

import sys
import os
import json
import argparse

def build_spec(project_name, persona, problem, core_action, outcome, must_haves, non_goals, out_file="spec.md"):
    print(f"[*] [Socratic Spec Builder] Đang phân tích nghiệp vụ cho: {project_name}...")
    
    # Kiểm tra quy tắc Cắt 50%
    must_list = [m.strip() for m in must_haves.split(",") if m.strip()]
    non_goal_list = [ng.strip() for ng in non_goals.split(",") if ng.strip()]
    
    spec_content = f"""# SPECIFICATION: {project_name.upper()} (MVP v1.0)
> Generated via Socratic JTBD Framework - Vibecoding Hub

## 1. JOBS-TO-BE-DONE (JTBD) & CORE VALUE PROPOSITION
- **Chân dung người dùng (Persona)**: {persona}
- **Bối cảnh & Nỗi đau**: {problem}
- **Hành động chuyển đổi cốt lõi**: {core_action}
- **Kết quả mong đợi (North Star Metric)**: {outcome}

## 2. MUST-HAVE SCOPE (KILLER FEATURES)
"""
    for idx, feature in enumerate(must_list, 1):
        spec_content += f"- **Feature {idx}**: {feature}\n"

    spec_content += """
## 3. NON-GOALS (TUYỆT ĐỐI KHÔNG LÀM TRONG V1)
> Quy tắc Cắt 50%: Mọi tính năng dưới đây bị cấm triển khai để bảo vệ sự tập trung của sản phẩm và ngữ cảnh của AI.
"""
    for idx, non_goal in enumerate(non_goal_list, 1):
        spec_content += f"- [CẤM] {non_goal}\n"

    spec_content += """
## 4. BẢN HỢP ĐỒNG TRẠNG THÁI (4-STATE MACHINE)
- Mọi tương tác mạng phải tuân thủ 4 trạng thái: `IDLE` -> `LOADING` -> `SUCCESS` -> `ERROR`.
- Xử lý riêng biệt Empty State khi mảng dữ liệu có 0 phần tử.

## 5. THIẾT KẾ GIAO DIỆN ANTI-SLOP (CHƯƠNG 6)
- Tỷ lệ màu: 60% Nền trung tính (#09090b hoặc #ffffff), 30% Thẻ phẳng xám, 10% Nhấn Cobalt (#2563eb).
- Lưới khoảng trắng: Bội số của 8px (p-4, gap-4, py-6).
- Loại bỏ toàn bộ gradient tím và hiệu ứng nhảy giật.
"""
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(spec_content)
        
    print(f"✅ Đã tạo thành công bản đặc tả kỹ thuật: {out_file}")
    print(f"📊 Thống kê phạm vi: {len(must_list)} Must-Haves, {len(non_goal_list)} Non-Goals bị cắt bỏ.")
    return spec_content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socratic Spec Builder for Vibecoders")
    parser.add_argument("--name", default="TOEIC Deconstructor", help="Tên dự án")
    parser.add_argument("--persona", default="Học sinh gặp khó khăn với từ vựng lạ trong đề Reading", help="Chân dung người dùng")
    parser.add_argument("--problem", default="Bị hoảng loạn khi đọc đoạn văn có nhiều từ mới lẫn ngữ pháp phức tạp", help="Nỗi đau cụ thể")
    parser.add_argument("--action", default="Bóc tách câu hỏi thành 2 tầng: Ngữ pháp đơn giản hóa & Từ vựng cô lập", help="Hành động cốt lõi")
    parser.add_argument("--outcome", default="Làm chủ ngữ pháp trước rồi ghép từ vựng, tự tin suy luận đáp án đúng", help="Kết quả chuyển đổi")
    parser.add_argument("--must", default="Bóc tách 2 tầng, Hiển thị đáp án step-by-step, Đánh dấu từ khóa", help="Các tính năng bắt buộc (ngăn cách bằng dấu phẩy)")
    parser.add_argument("--non-goals", default="Đăng nhập tài khoản, Lưu Cloud Database, Dark mode, Diễn đàn chat, Bảng xếp hạng", help="Các tính năng cắt bỏ (Non-goals)")
    parser.add_argument("--out", default="spec_demo.md", help="Tệp đầu ra")
    
    args = parser.parse_args()
    build_spec(args.name, args.persona, args.problem, args.action, args.outcome, args.must, args.non_goals, args.out)
