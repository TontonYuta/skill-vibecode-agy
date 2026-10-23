#!/bin/bash
# compile_latex.sh - Biên dịch LaTeX sang PDF theo chuẩn học thuật cho Vibecoding Hub
set -e

if [ -z "$1" ]; then
    echo "Cách dùng: $0 <duong_dan_tep.tex>"
    exit 1
fi

TEX_FILE="$1"
DIR=$(dirname "$TEX_FILE")
BASENAME=$(basename "$TEX_FILE" .tex)

if [ ! -f "$TEX_FILE" ]; then
    echo "❌ Lỗi: Không tìm thấy tệp $TEX_FILE"
    exit 1
fi

cd "$DIR"

echo "Đang biên dịch $BASENAME.tex với pdflatex (Pass 1)..."
pdflatex -interaction=nonstopmode "$BASENAME.tex" > /dev/null 2>&1 || {
    echo "❌ Lỗi biên dịch Pass 1. Kiểm tra log tại $DIR/$BASENAME.log"
    exit 1
}

echo "Đang biên dịch $BASENAME.tex với pdflatex (Pass 2 cho mục lục và liên kết)..."
pdflatex -interaction=nonstopmode "$BASENAME.tex" > /dev/null 2>&1 || {
    echo "❌ Lỗi biên dịch Pass 2. Kiểm tra log tại $DIR/$BASENAME.log"
    exit 1
}

if [ -f "$BASENAME.pdf" ]; then
    echo "✅ Biên dịch thành công: $DIR/$BASENAME.pdf"
else
    echo "❌ Không tìm thấy tệp $BASENAME.pdf được tạo ra."
    exit 1
fi
