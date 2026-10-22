# ✍️ Ngôn Ngữ Vi Mô UX & Giảm Thiểu Tải Nhận Thức (UX Writing & Cognitive Load)

> *"Giao diện tốt nhất là giao diện không đòi hỏi người dùng phải suy nghĩ về giao diện. Từ ngữ trên màn hình không phải là tác phẩm văn học để khoe khoang vốn từ, mà là những biển báo giao thông dẫn dắt người dùng đến đích nhanh nhất."*

---

## 1. Giảm Tải Nhận Thức (Cognitive Load Reduction)

### A. Định Luật Hick (Hick's Law) & Giảm Thiểu Lựa Chọn
- Càng nhiều lựa chọn được bày ra cùng một lúc, thời gian người dùng quyết định càng lâu và tỷ lệ bỏ ngang càng lớn.
- **Quy tắc 3 Hành Động Tối Đa**: Trên một màn hình hoặc một thanh công cụ, chỉ để tối đa **1 hành động chính (Primary CTA)**, **1 - 2 hành động phụ (Secondary Actions)**. Toàn bộ các tùy chọn nâng cao khác phải được nhóm vào menu thả xuống `...` (More options).

### B. Tiết Lộ Thông Tin Từng Bước (Progressive Disclosure)
- Chỉ hiển thị những thông tin tối thiểu cần thiết để người dùng hoàn thành bước hiện tại.
- Ví dụ:
  - Trong biểu mẫu đăng ký, không phơi bày 20 trường thông tin cùng lúc. Hãy chia nhỏ thành các bước logic có chỉ số tiến trình rõ ràng (Step 1 -> Step 2 -> Step 3).
  - Tận dụng `Accordion` hoặc `Details/Summary` cho các thiết lập kỹ thuật sâu ít khi dùng.

---

## 2. Tiêu Chuẩn Ngôn Ngữ Vi Mô (Microcopy Standards)

### A. Nút Bấm Hành Động Phải Cụ Thể (Action-Oriented Verb + Noun)
Tuyệt đối tránh các nhãn nút mơ hồ, chung chung do AI hay gán:

| AI Slop / Bad Copy | Chuẩn UX Hiện Đại | Lý Do Cải Tiến |
| :--- | :--- | :--- |
| `Submit` / `OK` | `Lưu thay đổi` / `Tạo tài khoản` | Mô tả chính xác việc gì sẽ xảy ra sau khi bấm |
| `Cancel` / `Delete` | `Hủy bỏ` / `Xóa vĩnh viễn dự án` | Tránh nhầm lẫn nguy hiểm giữa 2 nút đứng cạnh nhau |
| `Click here` / `Read more` | `Xem bảng so sánh gói giá` | Thân thiện với độc giả và công nghệ đọc màn hình (Screen Readers) |
| `Learn more` | `Tìm hiểu cách bảo mật API key` | Giảm cảm giác mơ hồ về điểm đến của liên kết |

### B. Tiêu Diệt Các Thuật Ngữ Tiếp Thị Sáo Rỗng (Eliminate AI Buzzwords)
Loại bỏ hoàn toàn các khẩu hiệu vô nghĩa mà các mô hình AI thường chèn vào:
- ❌ *"Supercharge your daily workflow with cutting-edge intelligence"*
- ❌ *"Unleash the full power of your team's synergy"*
- ❌ *"Next-generation seamless automated platform"*
- ✅ Thay bằng ngôn ngữ thực tế, nêu rõ **giá trị cụ thể và kết quả đo lường được**:
  - *"Tự động đồng bộ hóa dữ liệu tồn kho sau mỗi 5 phút giữa cửa hàng và kho vận."*
  - *"Tìm kiếm nhanh tài liệu nội bộ trong vòng 0.2 giây bằng phím tắt Cmd+K."*

### C. Công Thức Thông Báo Lỗi 3 Thành Phần (The 3-Part Error Formula)
Một thông báo lỗi đạt chuẩn bắt buộc phải trả lời đủ 3 câu hỏi:
1. **Chuyện gì đã xảy ra?** (Bằng ngôn ngữ đơn giản, không đổ lỗi cho người dùng).
2. **Tại sao lại xảy ra?** (Nguyên nhân cốt lõi).
3. **Cách khắc phục ngay bây giờ là gì?** (Hành động tiếp theo).

*Ví dụ:*
- ❌ **Kém**: *"Lỗi tải tệp. Dung lượng không hợp lệ."*
- ✅ **Chuẩn**: *"Không thể tải lên ảnh 'avatar.png' vì dung lượng vượt quá giới hạn 5MB. Vui lòng chọn ảnh có dung lượng nhỏ hơn hoặc nén ảnh trước khi tải lại."*
