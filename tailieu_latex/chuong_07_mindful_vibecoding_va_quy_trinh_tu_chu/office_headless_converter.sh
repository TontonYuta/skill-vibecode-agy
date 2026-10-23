#!/bin/bash
# scripts/office_headless_converter.sh
# Kịch bản tự động hóa chuyển đổi tài liệu Office sang PDF và ảnh minh họa không cần mở GUI:
# 1. Sử dụng LibreOffice Headless mode để chuyển DOCX/XLSX/PPTX sang PDF chuẩn in ấn.
# 2. Sử dụng pdftoppm để trích xuất các trang PDF thành ảnh PNG phân giải cao (150 DPI) cho AI OCR/Vision.

set -euo pipefail

if [ -z "${1:-}" ]; then
    echo "Cách dùng: $0 <duong_dan_tep_office> [thu_muc_dau_ra]"
    echo "Hỗ trợ định dạng: .docx, .doc, .xlsx, .xls, .pptx, .ppt, .odt, .ods"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_DIR="${2:-converted_docs}"

if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ Lỗi: Không tìm thấy tệp $INPUT_FILE"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"
BASENAME=$(basename "$INPUT_FILE")
FILENAME="${BASENAME%.*}"

echo "=========================================================="
echo "📄 [Office Headless Pipeline] Bắt đầu xử lý: $BASENAME"
echo "📂 Thư mục xuất bản: $OUTPUT_DIR"
echo "=========================================================="

echo "[*] Đang chuyển đổi sang PDF bằng LibreOffice Headless Engine..."
libreoffice --headless --convert-to pdf "$INPUT_FILE" --outdir "$OUTPUT_DIR" > /dev/null 2>&1

PDF_OUTPUT="$OUTPUT_DIR/$FILENAME.pdf"

if [ -f "$PDF_OUTPUT" ]; then
    PDF_SIZE_KB=$(du -k "$PDF_OUTPUT" | cut -f1)
    echo "✅ [1/2] Đã tạo thành công tệp PDF: $PDF_OUTPUT ($PDF_SIZE_KB KB)"
    
    echo "[*] [2/2] Đang trích xuất ảnh PNG từng trang qua pdftoppm (150 DPI)..."
    IMAGE_PREFIX="$OUTPUT_DIR/${FILENAME}_page"
    pdftoppm -png -r 150 "$PDF_OUTPUT" "$IMAGE_PREFIX"
    
    TOTAL_PAGES=$(ls -1 "${IMAGE_PREFIX}"-*.png 2>/dev/null | wc -l)
    echo "✅ Đã trích xuất $TOTAL_PAGES trang ảnh làm tài nguyên cho Vision/OCR!"
    echo "🎉 Quy trình chuyển đổi hoàn tất không cần mở giao diện Office!"
else
    echo "❌ Lỗi: Chuyển đổi PDF thất bại."
    exit 1
fi
