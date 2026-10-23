#!/bin/bash
# scripts/hacker_linux_daemon.sh
# Kịch bản mẫu Hacker Scripting trên Linux:
# 1. Quản lý File Descriptors (FD) và chuyển hướng luồng (Redirection).
# 2. Cơ chế Named Pipe (FIFO) giao tiếp liên tiến trình (IPC).
# 3. Bắt tín hiệu hệ thống (Signals: SIGINT, SIGTERM, SIGHUP) bằng lệnh 'trap'.
# 4. Tự động dọn dẹp tiến trình con và tệp tạm khi thoát.

set -euo pipefail

PIPE_DIR="/tmp/vibecoding_ipc"
PIPE_NAME="$PIPE_DIR/agent_event.pipe"
LOG_FILE="/tmp/vibecoding_daemon.log"

# Hàm dọn dẹp tài nguyên khi nhận tín hiệu dừng (Graceful Shutdown)
cleanup() {
    echo -e "\n[*] [Hacker Daemon] Đang nhận tín hiệu dừng. Bắt đầu dọn dẹp tài nguyên..."
    rm -rf "$PIPE_DIR"
    echo "[*] Đã xóa đường ống FIFO: $PIPE_NAME"
    echo "[*] Daemon kết thúc an toàn lúc $(date '+%Y-%m-%d %H:%M:%S')"
    exit 0
}

# Đăng ký bẫy tín hiệu (Signal Trapping)
trap cleanup SIGINT SIGTERM SIGHUP EXIT

# Khởi tạo thư mục và Named Pipe (FIFO)
mkdir -p "$PIPE_DIR"
if [[ ! -p "$PIPE_NAME" ]]; then
    mkfifo "$PIPE_NAME"
    echo "[*] Đã tạo Named Pipe (FIFO) thành công tại: $PIPE_NAME"
fi

echo "=========================================================="
echo "🚀 [Hacker Linux Daemon] Khởi động tiến trình ngầm (PID: $$)"
echo "📡 Đang lắng nghe sự kiện trên FIFO: $PIPE_NAME"
echo "📝 Ghi nhật ký tiến trình vào: $LOG_FILE"
echo "=========================================================="

# Mở File Descriptor 3 gắn vào FIFO để tránh tình trạng EOF khi không có writer
exec 3<>"$PIPE_NAME"

# Vòng lặp sự kiện bất đồng bộ (Event-driven loop)
echo "[*] Daemon sẵn sàng nhận lệnh. (Gửi dữ liệu thử bằng: echo 'TEST_EVENT' > $PIPE_NAME)"

# Chạy thử nghiệm phát sự kiện trong nền để chứng minh luồng hoạt động
(
    sleep 1
    echo "HELLO_VIBECODER: Khởi động tác vụ xử lý nền" > "$PIPE_NAME"
    sleep 1
    echo "TRIGGER_BACKUP: Sao lưu cơ sở dữ liệu hoàn tất" > "$PIPE_NAME"
    sleep 1
    echo "SHUTDOWN_SIGNAL: Hoàn thành kịch bản thử nghiệm" > "$PIPE_NAME"
) &

# Lắng nghe dữ liệu từ FD 3
while read -r event <&3; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$TIMESTAMP] 🔔 Sự kiện nhận được: $event" | tee -a "$LOG_FILE"
    
    case "$event" in
        HELLO_VIBECODER*)
            echo "   👉 [Action] Khởi tạo môi trường làm việc tác tử..."
            ;;
        TRIGGER_BACKUP*)
            echo "   👉 [Action] Đang đồng bộ hóa kho dữ liệu..."
            ;;
        SHUTDOWN_SIGNAL*)
            echo "   👉 [Action] Nhận lệnh tự ngắt từ luồng sự kiện."
            break
            ;;
        *)
            echo "   👉 [Action] Lệnh không xác định: $event"
            ;;
    esac
done

echo "[*] Vòng lặp sự kiện hoàn thành thành công."
