# Case Study: Xây Dựng Ứng Dụng Học Tiếng Anh Offline / Zero-API (`english-no-api`)

## 1. Bối cảnh & Thách thức
Dự án **`english-no-api`** là một ứng dụng web/PWA học tiếng Anh toàn diện (từ vựng TOEIC, ngữ pháp, đọc hiểu, nghe hội thoại, luyện phát âm, flashcard Spaced Repetition).
**Yêu cầu cốt lõi**:
1. Không phụ thuộc vào API key trả phí của bên thứ ba (OpenAI, Gemini, AWS).
2. Phát âm chuẩn bản xứ, có thể nghe song thoại giữa 2 nhân vật (David & Sarah).
3. Hỗ trợ học trên máy tính kết hợp điều khiển từ xa bằng điện thoại (Mobile Remote) qua quét mã QR cả trong mạng Wi-Fi LAN và mạng 4G/5G di động.

---

## 2. Kiến trúc giải pháp kỹ thuật

### 2.1 Âm thanh & Phát âm Zero-API
- **Web Speech API**: Sử dụng giọng đọc có sẵn của trình duyệt (`window.speechSynthesis`) làm kênh phát tức thì.
- **Edge TTS Streaming**: Tích hợp dịch vụ Microsoft Edge TTS qua websocket/HTTP backend (`en-US-JennyNeural`, `en-US-GuyNeural`) để phát âm chuẩn ngữ điệu tự nhiên mà không tốn phí bản quyền.
- **Chấm điểm phát âm cục bộ**: Tính toán độ tương đồng âm vị (Levenshtein distance + phonetic rules) trực tiếp trên client để đưa ra điểm số % và gợi ý cách uốn lưỡi/bật hơi.

### 2.2 Thuật toán Lặp lại ngắt quãng (Leitner Spaced Repetition)
- Phân loại từ vựng vào 5 hộp nhớ (Boxes 1–5).
- Mỗi lần ôn tập thành công, từ được thăng cấp lên hộp tiếp theo (khoảng cách ngày ôn tăng theo hàm mũ: 1 ngày, 3 ngày, 7 ngày, 14 ngày, 30 ngày).
- Khi trả lời sai, từ lập tức rơi về Hộp 1 để kích hoạt cơ chế Active Recall.

### 2.3 Mobile Remote qua QR Code & Cloudflare Quick Tunnel
- **Chế độ Mạng Cục Bộ (Wi-Fi LAN)**: Backend tự động phát hiện IP IPv4 nội bộ của máy chủ (ví dụ `192.168.0.103:3000`) và sinh mã QR để điện thoại cùng mạng quét truy cập ngay lập tức.
- **Chế độ Di Động (4G/5G)**: Tích hợp công cụ `cloudflared` (Cloudflare Quick Tunnel) để tạo đường hầm HTTPS ngẫu nhiên an toàn (`https://*.trycloudflare.com/remote`) mà không cần mở port modem hay cấu hình DDNS.

---

## 3. Bài học thực chiến & Post-Mortem lỗi

### 🐛 Lỗi 1: `TypeError: i is not iterable` trên Mobile Remote
- **Triệu chứng**: Khi chuyển sang tab Flashcard trên điện thoại, toàn bộ màn hình trắng xóa và console báo `i is not iterable`.
- **Nguyên nhân gốc**: Code component `FlashcardDeckView` thực hiện destruct mảng:
  ```typescript
  const [deck, setDeck] = useState([...initialItems]);
  ```
  Khi mở trên thiết bị mới chưa có lịch sử học, `initialItems` là `undefined`, khiến toán tử spread `[...]` bị crash trong bản build minified (`initialItems` bị đổi tên thành `i`).
- **Giải pháp dứt điểm**:
  1. Thêm giá trị mặc định cho prop: `items: initialItems = []`.
  2. Bọc kiểm tra phòng vệ: `Array.isArray(initialItems) ? [...initialItems] : []`.
  3. Cung cấp gói từ vựng khởi động (`STARTER_WORDS`) theo trình độ A1–B2 khi bộ nhớ trống để giao diện luôn có nội dung trực quan.

### 🐛 Lỗi 2: 403 Forbidden khi truy cập qua Cloudflare Tunnel
- **Triệu chứng**: Truy cập qua đường dẫn `trycloudflare.com` bị Vite chặn với thông báo `403 Forbidden: Invalid Host header`.
- **Giải pháp**: Trong `vite.config.ts` (Vite 6), bổ sung cấu hình máy chủ:
  ```typescript
  server: {
    host: true,
    allowedHosts: true,
  }
  ```
