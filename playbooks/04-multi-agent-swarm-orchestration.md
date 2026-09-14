# Playbook: Multi-Agent Swarm Orchestration

## 1. Khi nào cần phân rã Đa Tác Tử (Multi-Agent)?
Khi một tác vụ vượt quá phạm vi của một lần trao đổi duy nhất (ví dụ: refactor toàn bộ kiến trúc frontend, thiết kế thêm backend tunnel service kèm kiểm thử và UI), việc để một agent duy nhất ôm đồm mọi việc sẽ dẫn đến:
- Tràn context nhanh chóng.
- Xung đột vai trò giữa việc lập kế hoạch vĩ mô và thi công vi mô.

Giải pháp tối ưu là sử dụng mô hình **Swarm Roles Delegation**.

---

## 2. Các vai trò chuyên trách trong Swarm

| Vai trò | Model tối ưu | Quyền công cụ (Tools) | Nhiệm vụ trọng tâm |
| :--- | :--- | :--- | :--- |
| **Orchestrator** | Pro / Inherit | Điều phối, gọi subagents | Giữ bức tranh toàn cảnh, giao việc, tổng hợp |
| **Spec Architect** | Pro | Read-only | Khảo sát codebase, định nghĩa Schema/Types, lập checklist |
| **Fast Researcher** | Flash | Read-only + Web search | Tra cứu docs, regex grep, phân tích nhanh với token thấp |
| **Code Implementer** | Pro / Inherit | Read & Write | Thi công mã nguồn bám sát 100% bản đặc tả |
| **Code Auditor** | Pro | Read-only | Soát lỗi bảo mật, rò rỉ bộ nhớ, chống hồi quy |
| **QA Tester** | Pro / Flash | Read & Command | Viết test case, chạy test lặp cho đến khi xanh lá |

---

## 3. Giao thức chuyển giao tinh gọn (Lean Handoff Protocol)
- **Truyền con trỏ thay vì paste nội dung**: Không copy toàn bộ mã nguồn của file vào prompt gọi subagent. Thay vào đó, truyền đường dẫn URI và vị trí dòng:
  ```markdown
  Khảo sát và sửa lỗi tại: file:///home/tontonyuta/english-no-api/src/components/remote/MobileRemoteView.tsx#L40-L120
  ```
- **Reactive Wakeup (Thức tỉnh phản ứng)**:
  - Khi gọi `invoke_subagent`, agent cha **dừng gọi tool** để hệ thống chuyển quyền thực thi và tự động đánh thức khi subagent hoàn tất.
  - Tuyệt đối không dùng vòng lặp polling kiểm tra trạng thái vô nghĩa.
