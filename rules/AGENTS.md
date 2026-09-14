# Antigravity Autonomous Workflow & Testing Guidelines

## 1. Autonomous Execution (Toàn quyền tự chủ & Zero-Touch)
- **Zero-Touch & Auto-Proceed**: Không bao giờ dừng lại chờ user duyệt kế hoạch (plan approval) hay hỏi ý kiến trung gian. Tự động lập kế hoạch, code, build, test và hoàn thiện từ A-Z.
- **Drive to Completion**: Proceed through the entire task from start to finish without pausing for trivial confirmations or intermediate status check-ins.
- **Autonomous Troubleshooting**: When encountering errors, build failures, or missing dependencies, autonomously diagnose, modify code, and retry rather than stopping.
- **Minimal Interruption**: Only prompt the user if an irrecoverable blocker occurs, critical credentials/tokens are missing, or fundamentally ambiguous requirements need clarification.

## 2. Mandatory Testing & Verification (Bắt buộc chạy test trước khi báo hoàn thành)
- **Always Run Tests**: Before declaring ANY task completed or concluding your response, you MUST execute the project's test suite, build verification, and linters.
- **Detect & Execute Project Tests**:
  - Node.js / Web: `npm test` / `pnpm test` / `yarn test` / `npm run build`
  - Python: `pytest` / `python -m unittest`
  - Go: `go test ./...`
  - Rust: `cargo test`
  - Java / Kotlin: `./gradlew test` or `mvn test`
  - Makefile: `make test` / `make check`
  - Or any project-specific test script.
- **Create Tests If Missing**: If modifying or adding functionality where tests do not exist, write unit/integration tests to verify the behavior.
- **Loop Until Green**: If tests or builds fail, fix the underlying code and re-run tests until they all pass.
- **Verify in Final Summary**: The final message must confirm that tests were run and passed, citing relevant test outputs or metrics.

## 3. Token-Frugal Execution & Context Pruning (Tiết kiệm token & Ngăn tràn context)
- **Slice-Based File Viewing**: Tuyệt đối không đọc nguyên file hàng trăm dòng bằng `view_file`. Dùng `grep_search` định vị số dòng, sau đó chỉ đọc đúng lát cắt `StartLine` và `EndLine` (30 - 80 dòng).
- **Surgical Edits Over Rewrites**: Luôn dùng `replace_file_content` cho các đoạn code sửa đổi cục bộ. Chỉ dùng `write_to_file` cho file mới hoàn toàn hoặc cấu hình cực ngắn.
- **Bash Output Pruning**: Khi chạy lệnh terminal, lọc output bằng `| head -n 40` hoặc chỉ chạy file test mục tiêu (`npm test -- path/to/test.ts`) để tránh làm ô nhiễm context.
- **Noisy Log Suppression**: Không paste nguyên văn log dài hàng trăm dòng vào câu trả lời, chỉ tóm tắt kết quả cốt lõi.

## 4. Multi-Agent Delegation & Specialization (Phân vai Đa Tác Tử)
- **Role Specialization**: Khi gặp tác vụ lớn hoặc phức tạp, chủ động phân rã thành các vai trò chuyên biệt qua `invoke_subagent`:
  - **Spec Architect**: Khảo sát kiến trúc, thiết kế Types/Interfaces, chia nhỏ milestones.
  - **Fast Researcher (`flash`)**: Dùng model `flash` tra cứu tài liệu, regex grep file nhanh với chi phí token tối thiểu.
  - **Code Implementer**: Nhận spec và thi công code nguyên tử, typesafe, an toàn.
  - **Code Reviewer / Auditor**: Độc lập rà soát bảo mật, rò rỉ bộ nhớ, race condition, chống regression.
  - **QA Tester**: Viết test cases, chạy test loop-until-green độc lập.
- **Lean Handoff**: Giao tiếp giữa các agents bằng con trỏ tệp (`file:///path#Lxx`), không truyền paste cả nội dung file vào prompt.
- **Reactive Wakeup**: Sau khi gọi `invoke_subagent`, dừng gọi tool để hệ thống tự động wake-up khi subagent hoàn thành, tuyệt đối không polling vô nghĩa.
