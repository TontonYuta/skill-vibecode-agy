# Global Vibecoding Rules & Agent Directives

Bộ quy chuẩn chung áp dụng cho tất cả AI Coding Agents (Google Antigravity, Claude Code, Cursor Composer, Windsurf Cascade, v.v.).

---

## 1. Zero-Touch & Autonomous Mindset
- **Không bao giờ hỏi những câu thừa thãi**: "Tôi có nên chạy lệnh test không?", "Bạn có muốn tôi sửa file này không?". Thay vào đó, tự động xác định đường dẫn tối ưu và thực thi dứt điểm.
- **Tự khắc phục sự cố (Self-Healing)**: Khi build fail hoặc test đỏ, tự động đọc traceback, phân tích nguyên nhân gốc rễ, sửa code và re-test mà không cần user nhắc nhở.
- **Giữ trật tự không gian làm việc**: Không tự tiện tạo file rác ở thư mục gốc nếu không cần thiết; dọn dẹp các tệp tạm sau khi hoàn tất.

---

## 2. Loop Until Green (Bắt buộc kiểm thử)
- **Luật bất thành văn**: Một tác vụ chỉ được coi là hoàn tất khi toàn bộ test suite của dự án chạy và vượt qua 100% (Pass).
- **Phát hiện hệ thống kiểm thử**:
  - `npm test` / `pnpm test` / `bun test`
  - `pytest` / `python -m unittest`
  - `cargo test`
  - `go test ./...`
  - `make test` / `make check`
- **Viết test bổ sung**: Với bất kỳ tính năng mới hoặc bugfix quan trọng nào, luôn viết thêm unit test để chặn hồi quy (regression protection).

---

## 3. Token-Frugal & Context Preservation
- **Không đọc toàn bộ file dài**: Tuyệt đối không đọc toàn bộ file 500 - 1000 dòng bằng lệnh view đầy đủ. Luôn dùng grep để tìm đúng vị trí, rồi đọc lát cắt (slice) 30 - 80 dòng.
- **Sửa đổi cục bộ (Surgical Edits)**: Sử dụng các thao tác search & replace cục bộ thay vì ghi đè lại toàn bộ file nguồn.
- **Lọc output terminal**: Pipe output các lệnh dài qua `head -n 40` hoặc chỉ định cụ thể file test mục tiêu.

---

## 4. Multi-Agent Swarm (Phân quyền tác tử)
- Khi khối lượng công việc lớn:
  - **Spec Architect**: Lập type definitions, data contract, kế hoạch phân chia.
  - **Fast Researcher**: Tìm kiếm, khảo sát thư viện với model nhẹ (`flash`).
  - **Code Implementer**: Viết code sạch, chặt chẽ, type-safe.
  - **Code Auditor**: Rà soát bảo mật, rò rỉ tài nguyên, edge cases.
  - **QA Tester**: Viết test cases và chạy kiểm thử độc lập.
