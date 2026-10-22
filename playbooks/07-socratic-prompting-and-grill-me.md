# 📘 Playbook 07: Kỹ Thuật Phỏng Vấn Ngược (Socratic Prompting & "/grill-me")

> *"Lập trình viên thiếu kinh nghiệm bảo AI bắt đầu viết code ngay. Kỹ sư bậc thầy bắt AI phải chất vấn và phản biện lại ý tưởng của mình trước khi gõ bất kỳ dòng lệnh nào."*

---

## 1. Cạm Bẫy Của Việc "Code Ngay & Luôn" (The Rushing-to-Code Trap)

Khi bạn gửi cho Agent một prompt ngắn ngủi như:
> *"Hãy viết cho tôi một module thanh toán giỏ hàng cho app thương mại điện tử."*

Theo quán tính, mô hình AI sẽ tự động bịa ra hàng tá giả định ngầm (Assumptions):
- Giả định hệ thống chỉ có thanh toán thành công (Happy Path).
- Giả định người dùng thanh toán bằng USD thay vì VND.
- Giả định không có trường hợp hết hàng đột ngột giữa lúc giao dịch đang xử lý (Race Condition).
- Giả định mạng luôn ổn định và không cần Idempotency Key chống trừ tiền 2 lần.

Hậu quả: Bạn có được 500 dòng code chạy ngon trên môi trường demo, nhưng khi đưa vào thực tế thì sập liên tục và phát sinh vô số lỗi logic tinh vi.

---

## 2. Quy Trình "Grill-Me" (Phỏng Vấn Phản Biện Socratic)

Lấy cảm hứng từ phương pháp đối thoại của Socrates và quy trình `/grill-me` của Matt Pocock, quy trình chuẩn hóa gồm 3 chặng:

```
[ Ý TƯỞNG SƠ KHỞI ]
        │
        ▼
[ 1. GIAI ĐOẠN PHỎNG VẤN NGƯỢC (/grill-me) ]
     AI đưa ra 3 - 5 câu hỏi trắc nghiệm/ngắn về:
     - Giới hạn dữ liệu & Edge Cases
     - Xử lý lỗi & Phục hồi mạng
     - Phân quyền & Bảo mật
        │
        ▼
[ 2. ĐẶC TẢ TỰ ĐỘNG (Auto-Generated SPEC) ]
     Chốt API contracts, Database Schema, UI Mockup
        │
        ▼
[ 3. VÒNG LẶP TEST-DRIVEN VIBECODING ]
     Viết test trước -> Code -> Loop until 100% Green
```

---

## 3. Mẫu Kích Hoạt Chế Độ "Grill-Me" Thực Chiến

Bạn có thể kích hoạt tư duy này bằng prompt:

```markdown
Tôi muốn xây dựng tính năng: [Mô tả tính năng của bạn].
TRƯỚC KHI VIẾT BẤT KỲ DÒNG CODE NÀO:
Hãy đóng vai trò một Principal Software Architect và UX Director khó tính. 
Hãy chất vấn tôi (Grill me) với 3 đến 5 câu hỏi cốt lõi nhất về:
1. Trường hợp biên (Edge cases) và luồng xử lý lỗi nghiêm trọng.
2. Cấu trúc lưu trữ dữ liệu và tính nhất quán (Concurrency / Idempotency).
3. Quyết định thiết kế UX mà tôi có thể đã bỏ quên.
Đưa ra các phương án gợi ý dạng trắc nghiệm để tôi lựa chọn nhanh.
```

---

## 4. Lợi Ích Cốt Tử Cho Dự Án

1. **Tiết kiệm 80% thời gian gỡ lỗi**: Làm rõ yêu cầu trước giúp loại bỏ hoàn toàn việc phải đập đi xây lại cả hệ thống kiến trúc.
2. **Khóa chặt ảo giác của mô hình (Zero Hallucination)**: AI không còn phải đoán mò xem bạn muốn gì; mọi quyết định thiết kế đều đã được con người đồng thuận và lưu vào context.
3. **Mã nguồn đạt chuẩn Production ngay từ phiên bản đầu tiên (v1)**.
