---
name: healthcare-ui-ergonomics
description: >-
  Bộ quy chuẩn công thái học giao diện y tế lâm sàng (Clinical UI & Human Factors Ergonomics)
  theo chuẩn FDA Medical Software Human Factors, IEC 62366-1, Apple Health Records và WHO Digital Health.
  Áp dụng khi thiết kế, xây dựng hoặc refactor giao diện EMR, HIS, LIS, tủ trực cấp cứu, kho dược FEFO,
  và trang thiết bị y tế với quy chuẩn kích thước chữ dễ đọc từ xa, chống nhầm lẫn liều/giường bệnh,
  và kiểm thử tự động bằng Playwright.
---

# 🏥 Healthcare UI Ergonomics & Clinical Human Factors Standard

> *"Trong môi trường y tế lâm sàng (phòng cấp cứu, buồng bệnh ICU, xe tiêm di động), một giao diện khó đọc hoặc một con số mờ nhạt không đơn thuần là lỗi thẩm mỹ — đó là nguy cơ đe dọa trực tiếp đến an toàn tính mạng người bệnh."*

---

## 🎯 6 Nguyên Tắc Vàng Trong Thiết Kế UI Y Tế

### 1. Typography & Khả Năng Đọc Từ Khoảng Cách Xa (Distance Legibility)
- **Cỡ chữ cơ sở (Base Reading Font)**: Dữ liệu lâm sàng chính (Tên bệnh nhân, Tên thuốc & hàm lượng, Số lượng, Chỉ số sinh tồn) phải đạt từ **15px - 16px (`text-base` / `text-[15px]`)**, in đậm (`font-bold text-slate-900`).
- **Thông tin thứ cấp (Secondary Metadata)**: Vị trí giường bệnh, phân loại thuốc, hạn kiểm định phải đạt **13px - 14px (`text-sm text-slate-700`)**.
- **Ngưỡng tối thiểu tuyệt đối (Absolute Floor)**: Không bao giờ dùng font dưới **12px (`text-xs`)**. Tuyệt đối cấm các kích thước chữ li ti `10px` hay `11px`.
- **Tương phản cao chống lóa (Fluorescent Glare Contrast)**: Tỷ lệ tương phản tối thiểu 4.5:1 (WCAG AA), khuyến khích 7:1 (WCAG AAA). Cấm sử dụng màu xám mờ nhạt (`text-slate-400`) cho dữ liệu chuyên môn.

### 2. Phòng Ngừa Sai Sót Y Khoa (Medical Error Prevention)
- **Tên thuốc & Hàm lượng**: Phải hiển thị trọn vẹn (vd: *"Morphin sulfat 10mg/1ml"*), không được dùng `truncate` làm mất nồng độ hàm lượng.
- **Tên bệnh nhân & Buồng giường**: Phải luôn đi kèm với nhau, làm nổi bật số giường bằng màu sắc và biểu tượng trực quan để điều dưỡng không trao nhầm thuốc.
- **Chữ số đo lường (Tabular Monospace Digits)**: Số lượng, nhiệt độ, mã phiếu phải dùng `font-mono font-bold` để các con số thẳng hàng khi so sánh dọc.

### 3. Phân Bổ Không Gian & Khoảng Thở Hàng (Space Ergonomics)
- **Chiều cao hàng bảng**: Tối thiểu 56px - 64px (`py-3.5` hoặc `py-4`) để mắt dễ quét theo chiều ngang và tay dễ chạm bấm trên màn hình cảm ứng hoặc xe tiêm COW (Computer on Wheels).
- **Tránh khoảng trắng vô nghĩa (Balanced Density)**: Phân bổ tỷ lệ cột theo dạng `table-fixed` để dữ liệu dàn đều toàn màn hình, không để cột này quá co cụm trong khi cột khác trống hoác.

### 4. Triệt Tiêu Lỗi Lặp Thừa Thãi (De-Duplication)
- Không lặp lại 2 nút điều khiển cùng một chức năng trên một màn hình (ví dụ: 2 nút đóng/mở sidebar cạnh nhau, hoặc 2 hộp chọn vai trò).
- Không lặp lại trạng thái và hành động cùng một lúc (ví dụ: đã có cột `Trạng thái: Đã hoàn bù` thì cột thao tác không cần ghi thêm chữ `Đã chốt sổ`).

### 5. Vùng Đệm An Toàn Tuyệt Đối (Zero-Overlap Floating Elements)
- Bất kỳ nút nổi nào (Chatbot AI, Call button, Floating Actions) đều phải có vùng đệm an toàn (`pb-24` hoặc `pb-28`) ở container bên dưới để khi người dùng cuộn đến cuối trang, dữ liệu và các nút bấm hàng cuối cùng không bao giờ bị che phủ.

### 6. Kiểm Thử Tự Động Bằng Playwright (Automated Playwright Auditing)
- Trước khi release bất kỳ thay đổi UI nào, bắt buộc chạy kịch bản Playwright để đo lường phân bố kích thước font chữ và kiểm tra không có phần tử bị che khuất.
