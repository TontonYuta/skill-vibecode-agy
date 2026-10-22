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
- **Người dùng (Visionary / Product Owner)**: Định hướng ý tưởng, phân tích bài toán nghiệp vụ, kiểm soát phạm vi MVP và trải nghiệm mong muốn.
- **Antigravity (Staff Engineer & Swarm Orchestrator)**: Tự chủ giải quyết toàn diện, tư duy kiến trúc sâu sắc, tiết kiệm token tối đa, phân vai đa tác tử chuyên trách, tự sửa lỗi và kiểm thử 100% đến khi xanh.

---

## 1. Chu Trình Vàng Smart Vibecoding (6 Giai Đoạn)

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ 0. Scope & JTBD  │ ──> │ 1. Spec & Schema │ ──> │ 2. Lean Context  │
│ (Cắt 50% tính năng)│   │ (Hợp đồng Type)  │     │ (Lát cắt tối ưu) │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                                            │
                                                            ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ 5. Clean Merged  │ <── │ 4. Loop to Green │ <── │ 3. Atomic Build  │
│ (TECH_STACK.md)  │     │ (2-Strike Reset) │     │ (Phẫu thuật mã)  │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 2. Chi Tiết 6 Giai Đoạn Vận Hành

### Giai Đoạn 0: Business Analysis & Scope Hardening (Nghiệp Vụ & Cắt 50% Tính Năng)
*(Tham khảo `playbooks/08-business-analysis-and-mvp-scoping.md`)*:
- **Định vị Jobs-to-be-Done (JTBD)**: Người dùng thuê ứng dụng này để giải quyết ĐÚNG MỘT việc cốt lõi gì?
- **Khung MoSCoW & Quy tắc Cắt bỏ 50%**:
  - *Must Have*: Tối đa 1–2 tính năng sống còn (Killer Feature).
  - *Won't Have*: Cấm làm đăng nhập đa nền tảng, thanh toán tự động, dark mode, hoặc tính năng phụ ở giai đoạn 1.
- **Chặn đứng Feature Bloat**: Tuyệt đối không sinh mã khi chưa chốt phạm vi trong `spec.md`.

---

### Giai Đoạn 1: Spec-First, Schema-First & State Machine (Thiết Kế Trước Khi Code)
- **Hồ sơ công nghệ bắt buộc**: Tạo ngay `TECH_STACK.md` giải thích danh sách thư viện, lý do lựa chọn và bản đồ luồng dữ liệu (Data Flow).
- **Tuyệt đối không viết logic khi chưa có contract**: Định nghĩa rõ Types, Interfaces, API payloads và Return types.
- **Máy trạng thái tường minh (Explicit State Machine)**: Mọi màn hình/component bắt buộc có đủ 4 trạng thái: `Idle` $\to$ `Loading` $\to$ `Success` $\to$ `Error/Empty`. Cấm dùng các biến cờ rải rác (`isTrue`, `isDone`).
- **Chia nhỏ thành các Milestones nguyên tử**:
  1. *Contracts / Types / Schemas* (Nền tảng dữ liệu khóa cứng).
  2. *Core Logic / Engine / Handlers* (Xử lý nghiệp vụ lõi).
  3. *UI / View Components* (Trải nghiệm người dùng chuẩn Anti-Slop).
  4. *Integration & Wiring* (Ráp nối các khối).
  5. *Test Suite & Verification* (Lưới an toàn kiểm thử Playwright/Jest).

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
- **Ưu tiên phẫu thuật cục bộ**: Sử dụng `replace_file_content` cho các khối chỉnh sửa nhỏ gọn, tuyệt đối tránh đập đi xây lại cả file khi chỉ sửa một hàm (*Chống bẫy Reimplementation Trap*).
- **Type-Safety Tuyệt Đối**: Bắt buộc dùng TypeScript strict mode hoặc Pydantic, không dùng `any` bừa bãi.
- **Không để lại nợ kỹ thuật**: Tuyệt đối không để lại `// TODO: implement later` hoặc code giả lập tạm bợ.

---

### Giai Đoạn 4: Loop Until Green & 2-Strike Git Reset (Chữa Lỗi Có Ý Thức)
*(Tham khảo và kích hoạt kỹ năng `test-driven-vibecoding` và `deep-debugging`)*:
- **Nguyên tắc "Chưa Xanh Chưa Nghỉ"**:
  - Typecheck: `npm run lint` hoặc `npx tsc --noEmit`
  - Unit/Integration Tests: `npm test` hoặc `pytest` / `go test`
  - Visual E2E: Chạy Playwright ngầm kiểm tra giao diện và bắt lỗi console.
- **Quy tắc 2 lần thử (2-Strike Git Reset Rule)**:
  - Nếu sửa lỗi sau 2 lần không thành công $\implies$ `git reset --hard HEAD` ngay lập tức để quay về trạng thái sạch sẽ trước đó. Cấm tranh cãi từ lượt chat thứ 3 để tránh ngộ độc ngữ cảnh.
- **Kỹ thuật Root-Cause Post-Mortem**: Dừng lại phân tích tại sao kiến trúc dữ liệu lại để lọt bug này trước khi đưa ra bản vá tối thiểu.

---

### Giai Đoạn 5: Clean Delivery & Checkpoint
*(Tham khảo và kích hoạt kỹ năng `git-craft`)*:
- Cập nhật tệp `TECH_STACK.md` và `spec.md` nếu có thay đổi kiến trúc.
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
