---
name: react-dialogue-shorts-pro
description: >-
  Chuẩn Biên Soạn Kịch Bản Viral TikTok/Shorts, Bố Cục Safe-Zone 9:16 & 16:9, Hoạt Họa 2D Vector Puppetry và Phụ Đề Kinetic Cho Video Đối Thoại React.
---

# Quy Chuẩn Hoạt Họa Đối Thoại 2D Vector Shorts (React & Remotion Architecture)

Kỹ năng này cung cấp toàn bộ công thức biên kịch viral, ngân sách bố cục an toàn chống đè chữ (Zero-Overlap), phân bổ thời lượng theo nhịp nói tự nhiên, và quy chuẩn sinh dữ liệu hoạt họa 2D Vector Puppetry chuyên nghiệp cho video ngắn (TikTok, YouTube Shorts, Reels).

---

## 1. Công Thức Biên Kịch Viral Shorts (The 3-Second Hook & Punchline Formula)

### A. Cấu trúc thời lượng vàng 45s - 60s
1. **HOOK 3 GIÂY ĐẦU (00:00 - 00:03)**:
   - Đặt thẳng vào mâu thuẫn, nghịch lý oái oăm hoặc câu hỏi kích thích tò mò cực độ.
   - **TUYỆT ĐỐI CẤM** các câu chào hỏi rườm rà: *"Xin chào các bạn"*, *"Chào mừng quay trở lại"*, *"Hôm nay chúng ta sẽ tìm hiểu về..."*.
   - Ví dụ Hook đỉnh cao:
     * *"Ủa, nếu 1 chia 0 bằng vô cùng thì 0 nhân vô cùng phải bằng 1 chứ anh?"*
     * *"Sếp ơi, em xin nghỉ phép 3 ngày đi tìm lại cảm hứng sống!"*
     * *"Đi chợ mua mớ rau có bao giờ dùng đến Tích phân đâu mà bắt học?"*

2. **XUNG ĐỘT TĂNG TIẾN & TRANH LUẬN (00:03 - 00:45)**:
   - Nhịp đối đáp nhanh gọn: Mỗi câu thoại chỉ từ **8 đến 16 từ**. Tuyệt đối không để một nhân vật độc thoại quá 5 giây liên tục.
   - Tung hứng đối đáp qua lại: Nhân vật hỏi ngây ngô $\leftrightarrow$ Nhân vật đáp thông thái/cà khịa $\leftrightarrow$ Phản biện bất ngờ.
   - Tốc độ phát âm chuẩn Shorts: **2.6 - 3.0 từ/giây**.

3. **CÚ TWIST & PUNCHLINE (00:45 - 00:60)**:
   - Kết thúc bằng một cú bẻ lái bất ngờ (Plot Twist), câu nói châm biếm sâu cay hoặc đúc kết hài hước.
   - Câu kết (Call-to-Action) ngắn gọn, tự nhiên, không gượng ép.

### B. Triệt tiêu AI Clichés & Văn phong sách vở
- Cấm hoàn toàn giọng điệu AI thuyết giáo: *"Đó quả là một câu hỏi thú vị"*, *"Toán học thật kỳ diệu"*, *"Chúng ta hãy cùng nhớ rằng"*.
- Dùng ngôn ngữ đời sống, tự nhiên, hóm hỉnh của người Việt: *"Ủa alo?"*, *"Á đù"*, *"Ảo ma thật đấy"*, *"Cạn lời luôn"*, *"Tỉnh táo lên bạn ơi"*.

---

## 2. Ngân Sách Bố Cục An Toàn 9:16 (Safe Zone & Anti-Overlap)

Màn hình dọc 9:16 (1080x1920) được chia thành 4 phân vùng tọa độ nghiêm ngặt:

| Phân Vùng | Tọa độ Y (% chiều cao) | Nhiệm Vụ & Quy Định Chống Đè Chữ |
| :--- | :--- | :--- |
| **Top Zone** | `0% - 14%` | Tiêu đề chủ đề ngắn gọn hoặc khoảng trống an toàn để không bị che bởi avatar/thanh tìm kiếm của TikTok. |
| **Dialogue Bubble** | `14% - 46%` | Khu vực hiển thị bong bóng thoại Comic. Đuôi thoại trỏ xuống người nói. **CẤM đè lên mắt/mặt nhân vật**. Tự động co chữ nếu > 50 ký tự. |
| **Kinetic Subtitles** | `46% - 62%` | Phụ đề nảy chữ trung tâm. Font chữ to đậm, viền tương phản, highlight từ đang nói màu vàng neon `#FEF08A`. |
| **Character Stage** | `62% - 100%` | Sàn diễn của các nhân vật 2D Vector Puppets. Chiều cao nhân vật chiếm ~35-40% khung hình. Chân chạm sàn vững chãi. |

### Quy tắc an toàn hình học:
1. **Khoảng cách giữa 2 nhân vật**: Nhân vật 1 đứng tại $X \approx 20\%$, Nhân vật 2 đứng tại $X \approx 80\%$. Hướng mặt vào nhau (`facing="right"` và `facing="left"`).
2. **Khi có 3 nhân vật**: Nhân vật 1 ($X \approx 15\%$), Nhân vật 2 ($X \approx 50\%$), Nhân vật 3 ($X \approx 85\%$).
3. **Bong bóng thoại tự co dãn (Responsive Sizing)**:
   - Dưới 30 ký tự: Cỡ chữ lớn `text-xl font-black`.
   - Từ 30 - 60 ký tự: Cỡ chữ vừa `text-base font-black`.
   - Trên 60 ký tự: Cỡ chữ an toàn `text-sm font-bold`, chủ động ngắt dòng cân đối.

---

---

## 3. Hệ Thống Biểu Cảm, Cử Chỉ & Hoạt Họa Tự Nhiên (Organic Puppetry Engine 2.0)

Để nhân vật sinh động, tự nhiên và **TUYỆT ĐỐI KHÔNG BỊ NHẢY TƯNG TƯNG (Chống Bobblehead)**:

1. **Cử động đầu tự nhiên (Neck Pivot Micro-Nodding)**:
   - Điểm tựa xoay tại khớp cổ $(X=100\text{px}, Y=125\text{px})$.
   - Khi nói (`isSpeaking`): Dao động góc nhẹ $\pm 0.8^\circ$ và tịnh tiến dọc rất nhỏ ($-1.5\text{px} \leftrightarrow +0.8\text{px}$) với chu kỳ $1.1\text{s}$ `ease-in-out`. Tạo cảm giác gật gù trao đổi tự nhiên của con người.
   - Khi lắng nghe (Idle): Dao động thở nhẹ nhàng $3.2\text{s}$ $\pm 0.4^\circ$.
   - **CẤM HOÀN TOÀN** dùng `animate-bounce` trên đầu khiến đầu bị rời khỏi cổ và nảy lên xuống quá đà.

2. **Chớp mắt tự nhiên (Eye Blinking)**:
   - Tự động chớp mắt sau mỗi $4\text{s}$ trong vòng $150\text{ms}$ (`scaleY(1) -> scaleY(0.08)` tại tâm mắt). Nhân vật luôn có hồn, tránh cảm giác đơ cứng như ma-nơ-canh.

3. **Khẩu hình môi nhịp nhàng (Organic Lip-Flap Visemes)**:
   - Khi nói: Chu kỳ co dãn môi $0.22\text{s}$ luân phiên giữa mở to và nửa mở với khoang miệng đỏ thẫm `#881337`, hàng răng trên trắng tinh `#FFFFFF` và lưỡi hồng `#F43F5E`.
   - **CẤM HOÀN TOÀN** dùng `animate-ping` làm miệng biến mất và nhấp nháy chói mắt.

4. **Bóng tiếp xúc mặt đất (Ground Shadow)**:
   - Đặt hình elip bóng mờ mềm mại dưới chân nhân vật (`fill="#000000"` độ mờ 16%) để nhân vật bám sàn chắc chắn.

5. **Cảm xúc khuôn mặt (`expression`)**:
   - `normal`: Mắt mở to tròn, tự động chớp mắt sau 4s.
   - `happy`: Mắt cười cong híp `^ ^`, miệng cười rạng rỡ.
   - `shocked`: Mắt mở tròn xoe `O_O`, con ngươi li ti, giọt mồ hôi toát ra bên thái dương `💧`.
   - `skeptical`: Mắt híp một bên, nhướn mày nghi ngờ `¬_¬`.
   - `angry`: Lông mày chéo gắt, tròng mắt đỏ rực.
   - `thinking`: Ngước mắt nhìn lên trên, một ngón tay chống cằm `◔_◔`.

6. **Cử chỉ tay (`gesture`)**:
   - `idle`: Thả lỏng tự nhiên bên hông.
   - `point`: Chỉ tay dứt khoát về phía đối phương hoặc lên bảng.
   - `explain`: Hai bàn tay mở rộng xòe ra diễn giải.
   - `think`: Tay gập chống cằm suy nghĩ.
   - `wave`: Giơ tay vẫy chào vui nhộn.
   - `facepalm`: Bàn tay ôm trán bất lực vì đối phương nói ngớ ngẩn.

7. **Biểu tượng phản ứng bay (`reaction`)**:
   - `lightbulb`: Bóng đèn 💡 phát sáng khi vừa nảy ra ý tưởng hay.
   - `question`: Dấu chấm hỏi ❓ xoay tròn khi hoang mang.
   - `anger`: Dấu gân chữ thập 💢 bùng cháy khi cay cú.
   - `sweat`: Giọt mồ hôi rơi 💧 khi bị bắt bẻ trúng tim đen.
   - `coffee`: Cốc cafe bốc khói ☕ khi thư giãn, chill.
   - `laptop`: Chiếc laptop 💻 khi đang gõ phím làm việc.
   - `money`: Xấp tiền 💵 khi nói về tài chính, kinh doanh.
   - `mic`: Micro phỏng vấn 🎙️ khi làm talkshow/bản tin.
   - `phone`: Điện thoại 📱 khi nhắn tin, lướt mạng xã hội.
   - `book`: Sách giáo trình 📖 khi trích dẫn kiến thức.
   - `fire`: Ngọn lửa bùng cháy 🔥 khi tranh luận nảy lửa.

---

## 4. Kiến Trúc Phim Hoạt Họa Dài Đa Phân Cảnh (Multi-Act Storytelling 2m - 5m)

Khi sản xuất video dài (90s, 2 phút, 3 phút, 5 phút), kịch bản được tổ chức theo cấu trúc Đa Phân Cảnh (Multi-Scene):

| Phân Cảnh (Act) | Thời Lượng | Bối Cảnh Không Gian Đề Xuất | Nhiệm Vụ Kịch Bản |
| :--- | :--- | :--- | :--- |
| **Hồi 1: Hook & Nghịch Lý** | `0:00 - 0:45` | `classroom` hoặc `cozy_room` | Bật ra nghịch lý hoặc tranh luận bất ngờ, khơi gợi tò mò. |
| **Hồi 2: Thắt Nút & Tranh Biện** | `0:45 - 2:00` | `coffee_shop` hoặc `modern_office` | Chuyển cảnh, các nhân vật phản bác nhau, đưa ra dữ liệu thực tế. |
| **Hồi 3: Cao Trào & Thí Nghiệm** | `2:00 - 3:30` | `tech_lab` hoặc `park_street` | Thử nghiệm giả định, tình huống dở khóc dở cười hoặc chứng minh khoa học. |
| **Hồi 4: Twist & Đúc Kết** | `3:30 - 5:00` | `news_studio` hoặc `library` | Cú bẻ lái bất ngờ (Plot twist), đúc kết bài học giá trị và kêu gọi follow. |

### Đạo Diễn Máy Quay Điện Ảnh (Cinematic Camera Director Mode):
- **Tự động Focus theo người nói**: Khi Nhân vật 1 nói, khung hình zoom nhẹ $1.04\times$ và pan sang trái; khi Nhân vật 2 đáp, pan mượt sang phải.
- **Nhạc nền Lo-Fi Cartoon (Web Audio API Synthesizer)**: Tạo không khí ấm áp, thư giãn, 0% dính bản quyền âm nhạc.

---

## 5. Chuẩn Dữ Liệu Hoạt Họa JSON Đầy Đủ (React / TypeScript Scene Schema)

```json
{
  "title": "Ủa tại sao chia cho 0 lại không được?",
  "format": "vertical",
  "backgroundTheme": "classroom",
  "char1": {
    "name": "Tèo (Tò Mò)",
    "color": "#EAB308",
    "hairStyle": "messy",
    "outfit": "hoodie",
    "role": "curious"
  },
  "char2": {
    "name": "Giáo sư Tí",
    "color": "#06B6D4",
    "hairStyle": "curly",
    "accessory": "glasses",
    "outfit": "suit",
    "role": "expert"
  },
  "lines": [
    {
      "speakerId": "char1",
      "text": "Ủa anh Tí, tại sao 1 chia cho 0 lại không được vậy anh?",
      "duration": 3.5,
      "expression": "normal",
      "gesture": "point",
      "reaction": "question"
    },
    {
      "speakerId": "char2",
      "text": "Haha câu hỏi hay đó! Giả sử 1 chia 0 bằng số X nào đó đi.",
      "duration": 3.8,
      "expression": "happy",
      "gesture": "explain",
      "reaction": "lightbulb"
    },
    {
      "speakerId": "char1",
      "text": "Dạ thì sao anh? Em nghĩ nó phải bằng vô cùng chứ!",
      "duration": 3.2,
      "expression": "thinking",
      "gesture": "think",
      "reaction": "none"
    },
    {
      "speakerId": "char2",
      "text": "Nếu 1/0 = X thì suy ra 0 nhân X phải bằng 1, điều này là vô lý!",
      "duration": 4.2,
      "expression": "shocked",
      "gesture": "point",
      "reaction": "anger"
    },
    {
      "speakerId": "char1",
      "text": "Á đù... hóa ra nếu chia cho 0 thì toàn bộ toán học sụp đổ luôn!",
      "duration": 3.8,
      "expression": "shocked",
      "gesture": "facepalm",
      "reaction": "sweat"
    },
    {
      "speakerId": "char2",
      "text": "Chính xác! Nhớ bấm Follow kênh để không bị mất gốc kiến thức nhé!",
      "duration": 3.6,
      "expression": "happy",
      "gesture": "wave",
      "reaction": "none"
    }
  ]
}
```
