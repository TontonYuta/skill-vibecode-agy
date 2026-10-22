# DESIGN.md - Tiêu Chuẩn Ngữ Cảnh Thị Giác Máy Đọc (Machine-Readable Visual Design Spec)

> Chuẩn đặc tả thiết kế cho AI Coding Agents (Google Labs Stitch & Modern Design Systems). Tệp này giúp AI hiểu chính xác mục đích sử dụng của từng màu sắc, kích thước và ngăn chặn việc sinh ra mã giao diện rác (AI Slop).

---

## 1. Design Tokens (Machine-Readable Values)

```json
{
  "$schema": "https://specs.designsystem.org/v1/tokens.json",
  "name": "Modern Artisan Design Tokens",
  "version": "2.0.0",
  "theme": {
    "colors": {
      "surface": {
        "canvas": "#090A0F",
        "subtle": "#12131A",
        "card": "#181924",
        "elevated": "#222334"
      },
      "border": {
        "subtle": "rgba(255, 255, 255, 0.05)",
        "default": "rgba(255, 255, 255, 0.10)",
        "hover": "rgba(255, 255, 255, 0.20)"
      },
      "accent": {
        "primary": "#4F46E5",
        "primaryHover": "#4338CA",
        "primaryMuted": "rgba(79, 70, 229, 0.15)"
      },
      "text": {
        "primary": "#F8FAFC",
        "secondary": "#94A3B8",
        "muted": "#64748B",
        "onAccent": "#FFFFFF"
      },
      "feedback": {
        "success": "#10B981",
        "warning": "#F59E0B",
        "danger": "#EF4444",
        "info": "#3B82F6"
      }
    },
    "typography": {
      "fontFamily": {
        "sans": "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Be Vietnam Pro', sans-serif",
        "mono": "'JetBrains Mono', 'SF Mono', monospace"
      },
      "fontSize": {
        "xs": "12px",
        "sm": "14px",
        "base": "16px",
        "lg": "18px",
        "xl": "20px",
        "2xl": "24px",
        "3xl": "30px",
        "4xl": "36px"
      },
      "lineHeight": {
        "tight": "1.2",
        "snug": "1.35",
        "normal": "1.6"
      }
    },
    "radii": {
      "none": "0px",
      "sm": "4px",
      "md": "8px",
      "lg": "12px",
      "full": "9999px"
    },
    "shadows": {
      "subtle": "0 1px 2px 0 rgba(0, 0, 0, 0.25)",
      "card": "0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -2px rgba(0, 0, 0, 0.3)",
      "elevated": "0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -4px rgba(0, 0, 0, 0.4)"
    }
  }
}
```

---

## 2. Quy Tắc Sử Dụng (Usage Guidelines & Rationale)

### Bảng Màu & Nền
- **DO**: Dùng `surface.card` cho các khối chức năng chính, viền `border.default`.
- **DON'T**: Không bao giờ tạo nền gradient tím-sang-xanh (`#8B5CF6 -> #06B6D4`) cho background hoặc text.
- **DON'T**: Không dùng nền kính mờ `backdrop-blur` trừ khi làm thanh Navigation cố định (Sticky Header).

### Kiểu Chữ & Phân Cấp
- **DO**: Dùng `text.primary` (#F8FAFC) cho mọi tiêu đề và nội dung chính.
- **DO**: Thêm `text-wrap: balance` cho các thẻ Heading (`h1, h2, h3`).
- **DO**: Thêm `text-wrap: pretty` cho các đoạn văn dài (`p`).
- **DON'T**: Không dùng `text.muted` (#64748B) cho các nhãn chỉ dẫn quan trọng hoặc input placeholder vì tương phản không đạt chuẩn WCAG.

### Bo Góc & Đổ Bóng
- **DO**: Dùng `radii.md` (8px) cho Button, Input field, Chip tags.
- **DO**: Dùng `radii.lg` (12px) cho Card hoặc Modal.
- **DON'T**: Không dùng bo góc quá đà (`rounded-3xl` hoặc `rounded-[32px]`) cho các thẻ nội dung có diện tích nhỏ hơn 300px.
