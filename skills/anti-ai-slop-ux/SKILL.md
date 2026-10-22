---
name: modern-app-ux-ui-standards
description: >-
  Bộ quy chuẩn toàn diện về kiến trúc UX/UI hiện đại và cẩm nang tiêu diệt "AI Slop"
  cho các ứng dụng web và di động. Tích hợp triết lý thiết kế thủ công Linear, Apple HIG,
  Nielsen Norman Group (NN/g 2026) và Google Labs DESIGN.md. Áp dụng khi tạo mới hoặc
  refactor giao diện frontend, xây dựng design system, kiểm tra tương phản WCAG 2.2,
  tối ưu công thái học bàn phím (Cmd+K) và loại bỏ các anti-pattern giao diện AI sáo rỗng.
---

# 🎨 Modern App UX/UI Standards & Anti-AI-Slop Governance

> *"Khi AI tạo code giao diện nhanh gấp 100 lần con người, giá trị của một sản phẩm không còn nằm ở việc có bao nhiêu dòng code CSS hay bao nhiêu card bóng bẩy, mà nằm ở việc loại bỏ những thứ thừa thãi, tôn trọng sự tập trung của người dùng và mang lại cảm giác mượt mà, chân thực."*

---

## 🎯 Mục Đích & Phạm Vi Áp Dụng

Skill này quy định các tiêu chuẩn tối thượng bắt buộc cho mọi ứng dụng khi thiết kế giao diện (UI) và trải nghiệm người dùng (UX):
1. **Tiêu diệt 100% "AI Slop"**: Ngăn chặn AI tự động đẻ ra các giao diện trung bình cộng, sáo rỗng, lạm dụng gradient tím xanh, bento grid rập khuôn và icon đóng hộp.
2. **Thiết lập chuẩn mực phần mềm chất lượng cao (Artisan Craft)**: Lấy cảm hứng từ Linear, Raycast, Vercel và Apple Human Interface Guidelines.
3. **Cung cấp ngữ cảnh máy đọc (Machine-Readable Context)**: Dùng `DESIGN.md` và `UX.md` làm kim chỉ nam để AI Agent lập trình đúng chuẩn mà không đoán mò.
4. **Kiểm tra tự động bằng Playwright**: Tích hợp kịch bản kiểm thẩm giao diện `audit-ui-slop.mjs` để phát hiện lỗi ngay trong chu trình CI/CD và Vibe Coding.

---

## 🧭 Cấu Trúc Bộ Tài Liệu Quy Chuẩn

Thư mục quy chuẩn UX/UI được phân bổ mạch lạc thành các chuyên đề chuyên sâu:

| Thứ tự | Tài liệu thành phần | Nội dung trọng tâm |
| :-: | :--- | :--- |
| **01** | [`01-ANTI-AI-SLOP-MANIFESTO.md`](./01-ANTI-AI-SLOP-MANIFESTO.md) | Giải phẫu hiện tượng AI Slop, 7 nhóm dấu hiệu nhận diện, 67+ anti-patterns theo nghiên cứu NN/g & Impeccable. |
| **02** | [`02-APP-UX-UI-DESIGN-SYSTEM.md`](./02-APP-UX-UI-DESIGN-SYSTEM.md) | Kiến trúc Design Tokens, Dark Mode tầng bậc (Elevation), Typography chống vỡ chữ tiếng Việt, Spacing lưới 4px/8px. |
| **03** | [`03-INTERACTION-MOTION-ERGONOMICS.md`](./03-INTERACTION-MOTION-ERGONOMICS.md) | Công thái học bàn phím `Cmd+K`, chuẩn chuyển động 150-200ms ease-out, triệt tiêu animation rung lắc/bouncing. |
| **04** | [`04-RESILIENT-STATE-ENGINEERING.md`](./04-RESILIENT-STATE-ENGINEERING.md) | 5 trạng thái sống còn (Loading Skeleton, Ideal, Empty, Error, Partial), Zero CLS, Undo Toast thay thế Modal xác nhận. |
| **05** | [`05-UX-WRITING-AND-COGNITIVE-LOAD.md`](./05-UX-WRITING-AND-COGNITIVE-LOAD.md) | Ngôn ngữ vi mô UX, công thức thông báo lỗi 3 phần, định luật Hick và xóa sổ thuật ngữ tiếp thị sáo rỗng. |
| **06** | [`DESIGN.md`](./DESIGN.md) | Đặc tả token thị giác máy đọc theo chuẩn Google Labs Stitch (Colors, Typography, Radii, Shadows). |
| **07** | [`UX.md`](./UX.md) | Đặc tả ràng buộc trải nghiệm máy đọc theo chuẩn Nielsen Norman Group (Glossary, Interaction constraints). |
| **08** | [`scripts/audit-ui-slop.mjs`](./scripts/audit-ui-slop.mjs) | Kịch bản kiểm thẩm giao diện tự động chạy ngầm bằng Playwright + Chromium headless. |

---

## ⚡ Bảng Kiểm 10 Điểm Vàng Trước Khi Giao Diện Lên Sóng (Golden Checklist)

Trước khi xác nhận hoàn thành bất kỳ tính năng UI nào, AI Agent và lập trình viên phải tự kiểm tra danh sách sau:

- [ ] **1. Không Gradient Tím - Xanh ngọc**: Nền và text có đang dùng gradient tím-sang-xanh sáo rỗng không? Đã chuyển sang nền Slate/Zinc trung tính chưa?
- [ ] **2. Không Cardocalypse**: Có card nào bị lồng quá 2 tầng không? Các nhóm thông tin nhỏ đã được phân tách bằng khoảng trắng và divider mỏng thay vì bọc thêm card chưa?
- [ ] **3. Typography Có Phân Cấp Rõ Ràng**: Tiêu đề có dùng `text-wrap: balance` không? Đoạn văn đọc có `text-wrap: pretty` và chiều rộng từ 60-75 ký tự không? Font chữ có hỗ trợ đầy đủ tiếng Việt không?
- [ ] **4. Đạt Chuẩn Tương Phản WCAG 2.2 AA**: Chữ thường có tỷ lệ tương phản tối thiểu 4.5:1 so với nền không? Đã loại bỏ hoàn toàn chữ xám mờ trên nền xám chưa?
- [ ] **5. Tốc Độ & Phản Hồi Dưới 100ms**: Nút bấm có hiệu ứng Tactile Feedback lún nhẹ khi click không? Chuyển động có kết thúc trong vòng 150-200ms không?
- [ ] **6. Hoạt Họa Tinh Tế, Không Gây Say Xe**: Đã tắt toàn bộ hiệu ứng nảy tưng tưng (bouncing), rung rinh (wiggling) và chấm nhấp nháy liên tục vô căn cứ chưa?
- [ ] **7. Đủ 5 Trạng Thái Giao Diện**: Đã thiết kế Loading Skeleton (không dùng spinner che màn hình), Empty State (có CTA hành động) và Error State (có nút Thử lại) chưa?
- [ ] **8. Chống Trôi Layout (Zero CLS)**: Hình ảnh và video đã được gán sẵn `aspect-ratio` hoặc kích thước khung cố định chưa?
- [ ] **9. Nút Toast Undo Thay Vì Modal Xác Nhận**: Các thao tác xóa thường ngày đã chuyển sang mô thức Optimistic Delete + Toast Hoàn tác trong 7 giây chưa?
- [ ] **10. Từ Ngữ Hành Động Cụ Thể**: Nút bấm có dùng công thức "Động từ + Danh từ" cụ thể (vd: "Xuất file PDF") thay vì từ chung chung như "OK", "Submit" không? Đã xóa sạch các từ tiếp thị rỗng tuếch như "supercharge", "next-gen" chưa?

---

## 🚀 Cách Chạy Kịch Bản Kiểm Thẩm Tự Động Playwright

Quét trực tiếp một trang web hoặc tệp HTML tĩnh để nhận báo cáo vi phạm AI Slop:

```bash
# Quét ứng dụng đang chạy ở môi trường phát triển (Dev server):
node UX/UI/scripts/audit-ui-slop.mjs http://localhost:3000

# Quét trang web thực tế:
node UX/UI/scripts/audit-ui-slop.mjs https://example.com

# Quét tệp HTML bản build:
node UX/UI/scripts/audit-ui-slop.mjs ./dist/index.html
```
