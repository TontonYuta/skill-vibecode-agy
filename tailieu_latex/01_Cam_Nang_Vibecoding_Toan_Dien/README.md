# Báo Cáo Chuyên Khảo: Cẩm Nang Vibecoding Toàn Diện (Từ Nghiệp Vụ, Logic, UX/UI Chống Nhựa Đến Tư Duy Làm Chủ)

Ấn phẩm chuyên khảo khoa học được biên soạn và xuất bản bằng mã nguồn LaTeX theo quy chuẩn của Trung tâm Nghiên cứu & Thực hành Vibecoding.

---

## 📄 Thông Tin Ấn Phẩm & Tệp PDF Đọc Ngay

* 📕 **Tệp PDF đọc ngay**: [**`cam_nang_vibecoding_toan_dien.pdf`**](./cam_nang_vibecoding_toan_dien.pdf) *(4 trang, 108 KB, A4)*
* 📄 **Mã nguồn LaTeX**: [`cam_nang_vibecoding_toan_dien.tex`](./cam_nang_vibecoding_toan_dien.tex)
* 📊 **Số liệu & Căn cứ**: 28 bài báo khoa học (arXiv 2025–2026), nghiên cứu về an ninh mã nguồn (*Last Secure Code Benchmark - arXiv:2610.14766*), nợ nhận thức (*Vibe-GUIDE - arXiv:2609.23859*), bẫy viết lại mã (*arXiv:2609.29410*), và khảo sát tệp luật Cursorrules trên GitHub (*arXiv:2608.10622*).

---

## 💡 Nội Dung Trọng Tâm

1. **Phẫu thuật 4 căn bệnh kinh niên**:
   * Nhồi nhét tính năng do thiếu phân tích nghiệp vụ.
   * Logic lỏng lẻo do để AI tự phỏng đoán.
   * Giao diện "Rất nhựa" (*AI Slop UI*) với gradient lòe loẹt, icon dày đặc.
   * Mất quyền làm chủ và không tiến bộ tư duy do sửa lỗi mù quáng.
2. **Khung phân tích nghiệp vụ thực chiến**:
   * Khung *Jobs-to-be-Done (JTBD)*: Xác định 1 công việc cốt lõi của người dùng.
   * Khung *MoSCoW* và Quy tắc cắt bỏ tối thiểu 50% tính năng trong MVP.
3. **Kiến trúc logic khóa cứng bằng Schema (Schema-First)**:
   * Định nghĩa máy trạng thái tường minh (Idle $\to$ Loading $\to$ Success $\to$ Error).
   * Khóa chặt các thực thể dữ liệu bằng TypeScript Interfaces / Pydantic Models.
4. **Bộ nguyên lý thiết kế UI/UX xóa sổ "Chất nhựa"**:
   * Tỷ lệ màu 60-30-10 (60% nền trung tính, 30% cấu trúc, 10% điểm nhấn nút chính).
   * Hệ thống lưới khoảng cách nhịp điệu 8px (Whitespace).
   * Phân cấp kiểu chữ (*Typography Hierarchy*) bằng độ đậm và kích thước, cấm dùng quá 2 font.
5. **Mindful Vibecoding — Phát triển tư duy sản phẩm**:
   * Tệp `TECH_STACK.md` bắt buộc để hiểu rõ kiến trúc và luồng dữ liệu.
   * Quy tắc 2 lần thử (2-Strike Rule) với `git reset --hard`.
   * Kỹ thuật truy cứu nguyên nhân gốc rễ (*Root-Cause Post-Mortem*) để học từ lỗi.
