# UX.md - Tiêu Chuẩn Ngữ Cảnh Trải Nghiệm Máy Đọc (Machine-Readable UX Spec)

> Chuẩn đặc tả ngữ cảnh UX cho AI Coding Agents theo đề xuất của **Nielsen Norman Group (2026)**. Tệp này cung cấp tri thức sản phẩm, mô hình người dùng, và các ràng buộc tương tác để AI không sinh ra mã theo lối mòn giả định vô căn cứ.

---

## 1. Ràng Buộc Tương Tác Cốt Lõi (Interaction Constraints)

```yaml
interaction_standards:
  primary_navigation:
    type: "sidebar_and_command_palette"
    command_shortcut: "Cmd+K / Ctrl+K"
    mobile_pattern: "bottom_nav_bar"
  destructive_actions:
    confirmation_policy: "undo_toast_first"
    undo_window_seconds: 7
    modal_confirmation_only_for:
      - "permanent_account_deletion"
      - "database_drop"
  data_entry:
    auto_save: true
    debounce_ms: 500
    save_indicator: "discrete_status_badge"
  loading_feedback:
    skeleton_shimmer: true
    full_screen_spinner_allowed: false
    min_skeleton_display_ms: 200
  animation_timing:
    micro_interactions_ms: 150
    modal_transitions_ms: 200
    easing: "cubic-bezier(0.16, 1, 0.3, 1)"
    reduced_motion_respected: true
```

---

## 2. Mô Hình Người Dùng & Bối Cảnh (User Models)

- **Đối Tượng Chính**: Người làm việc chuyên nghiệp (Knowledge workers, kỹ sư, quản trị viên dự án).
- **Mức Độ Thành Thạo**: Trung bình đến nâng cao. Cần tốc độ cao, khả năng thao tác bằng bàn phím, mật độ thông tin vừa phải (Medium to High Density), không thích các bước hướng dẫn rườm rà (no onboarding popover tours).
- **Thiết Bị Chủ Yếu**: Laptop màn hình 13-16 inch và Desktop màn hình rộng (24-32 inch); truy cập di động để tra cứu nhanh và duyệt phê duyệt.

---

## 3. Thuật Ngữ Chuẩn Hóa Của Sản Phẩm (Domain Glossary)

Tránh việc AI dùng lẫn lộn các từ ngữ không đồng nhất:

| Khái Niệm Trong Hệ Thống | Từ Được Phép Dùng | Từ Bị Cấm Tuyệt Đối (AI Slop) |
| :--- | :--- | :--- |
| Đơn vị công việc | **Nhiệm vụ (Task)** | Issue, Ticket, Item, Thing |
| Không gian làm việc | **Dự án (Project)** | Workspace, Hub, Realm |
| Thành viên nhóm | **Cộng sự (Collaborator)** | User, Subordinate, Resource |
| Trạng thái hoàn thành | **Đã xử lý (Resolved)** | Finished, Dead, Closed |
