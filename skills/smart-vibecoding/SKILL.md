---
name: smart-vibecoding
description: >-
  Core methodology and master playbook for autonomous 'smart vibecoding'. Use when tackling large features,
  end-to-end prototyping, converting ideas/PRDs into production code, optimizing tokens,
  orchestrating multi-agent workflows, or managing complex coding projects with zero regressions.
---

# Smart Vibecoding Pro: Triết Lý & Quy Trình Lập Trình Tự Chủ Thông Minh 2.0

"Vibe Coding" không phải là tạo code ngẫu nhiên hay nhắm mắt chấp nhận output của AI.
**Smart Vibecoding (Vibe Coding Thông Minh)** là sự kết hợp tối thượng giữa:
- **Người dùng (Visionary / Product Owner)**: Định hướng ý tưởng, yêu cầu nghiệp vụ, trải nghiệm mong muốn.
- **Antigravity (Staff Engineer & Swarm Orchestrator)**: Tự chủ giải quyết toàn diện, tư duy kiến trúc sâu sắc, tiết kiệm token tối đa, phân vai đa tác tử chuyên trách, tự sửa lỗi và kiểm thử 100% đến khi xanh.

---

## 1. Chu Trình Vàng Smart Vibecoding (5 Giai Đoạn)

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ 1. Spec-First   │ ──> │ 2. Lean Context  │ ──> │ 3. Atomic Build │
│ (Hợp đồng Type) │     │ (Lát cắt tối ưu) │     │ (Phẫu thuật mã) │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ 5. Clean Merged │ <── │ 4. Loop to Green │ <───┘                 │
│ (Bàn giao sạch) │     │ (Test & Audit)   │                       │
└─────────────────┘     └──────────────────┘
```

---

## 2. Chi Tiết 5 Giai Đoạn Vận Hành

### Giai Đoạn 1: Spec-First & Task Decomposition (Thiết Kế Trước Khi Code)
- **Tuyệt đối không viết logic khi chưa có contract**: Định nghĩa rõ Types, Interfaces, API payloads và Return types.
- **Chia nhỏ thành các Milestones nguyên tử**:
  1. *Contracts / Types / Schemas* (Nền tảng dữ liệu).
  2. *Core Logic / Engine / Handlers* (Xử lý nghiệp vụ lõi).
  3. *UI / View Components* (Trải nghiệm người dùng).
  4. *Integration & Wiring* (Ráp nối các khối).
  5. *Test Suite & Verification* (Lưới an toàn kiểm thử).

---

### Giai Đoạn 2: Lean Context Retrieval (Khảo Sát Tinh Gọn - Zero Token Waste)
*(Tham khảo và kích hoạt kỹ năng `token-optimizer-pro`)*:
- **Không đọc full file**: Dùng `find_by_name` và `grep_search` để định vị đúng dòng, sau đó chỉ dùng `view_file` với `StartLine`/`EndLine` (30-80 dòng).
- **Hấp thụ Pattern của dự án**:
  - Quản lý trạng thái: Zustand, Redux, React Context, hay Signal?
  - Styling: Tailwind, CSS Modules, hay inline styles?
  - Xử lý lỗi: Try/Catch, Result pattern, hay Global Error Boundary?
- **Bảo tồn mã nguồn hiện hữu**: Giữ nguyên comments, logic không liên quan và kiến trúc chung của người dùng.

---

### Giai Đoạn 3: Atomic Implementation (Triển Khai Phẫu Thuật Cục Bộ)
- **Ưu tiên phẫu thuật cục bộ**: Sử dụng `replace_file_content` cho các khối chỉnh sửa nhỏ gọn, tuyệt đối tránh đập đi xây lại cả file khi chỉ sửa một hàm.
- **Type-Safety Tuyệt Đối**: Không dùng `any` bừa bãi, mọi props/parameters phải được định kiểu rõ ràng.
- **Không để lại nợ kỹ thuật**: Tuyệt đối không để lại `// TODO: implement later` hoặc code giả lập tạm bợ.

---

### Giai Đoạn 4: Loop Until Green & Tự Chẩn Đoán Sửa Lỗi (Self-Healing)
*(Tham khảo và kích hoạt kỹ năng `test-driven-vibecoding` và `deep-debugging`)*:
- **Nguyên tắc "Chưa Xanh Chưa Nghỉ"**:
  - Typecheck: `npm run lint` hoặc `npx tsc --noEmit`
  - Unit/Integration Tests: `npm test` hoặc `pytest` / `go test`
  - Build Check: `npm run build`
- **Quy trình gỡ lỗi 4 bước (Root-Cause Troubleshooting)**:
  1. *Reproduce*: Tái hiện lỗi qua test runner hoặc lệnh curl/script.
  2. *Isolate*: Đọc kỹ stacktrace, khoanh vùng chính xác module gây lỗi.
  3. *Hypothesize*: Đặt giả thuyết kỹ thuật về nguyên nhân gốc rễ (không đoán mò).
  4. *Fix & Verify*: Sửa dứt điểm nguyên nhân gốc và chạy lại test ngay lập tức.

---

### Giai Đoạn 5: Clean Delivery & Checkpoint
*(Tham khảo và kích hoạt kỹ năng `git-craft`)*:
- Trình bày kết quả súc tích, chuyên nghiệp bằng tiếng Việt.
- Tạo liên kết dẫn trực tiếp đến các file đã sửa: `[Component](file:///abs/path#Lxx-Lyy)`.
- Trích dẫn định lượng kết quả: Số lượng test passed (`x/x passed`), kết quả build (`0 errors`).

---

## 3. Tích Hợp Multi-Agent Swarm Khi Gặp Nhiệm Vụ Lớn
*(Tham khảo và kích hoạt kỹ năng `multi-agent-orchestrator-pro`)*:
Khi gặp tác vụ phức tạp (nhiều hơn 3 files hoặc tính năng full-stack):
- **Spec Architect**: Khảo sát kiến trúc và xuất bản spec.
- **Fast Researcher** (`flash`): Tra cứu tài liệu, regex tìm file nhanh mà không hao token.
- **Code Implementer**: Nhận spec và thi công code nguyên tử.
- **Code Reviewer & Auditor**: Thẩm định độc lập về bảo mật, hiệu năng và chống bug ngầm.
- **QA Tester**: Viết test và chạy loop-until-green.
