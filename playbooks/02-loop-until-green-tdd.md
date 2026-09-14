# Playbook: Loop-Until-Green & Test-Driven Vibecoding

## 1. Triết lý "Loop-Until-Green"
Trong môi trường phát triển tự động hóa, **Test Suite chính là la bàn và rào chắn an toàn duy nhất của AI Agent**.
Nếu không có test:
- AI rất dễ rơi vào ảo giác (hallucination), khẳng định tính năng hoạt động trong khi code thực tế bị crash ngầm ở runtime.
- Gây ra lỗi thụt lùi (regression bugs) vào các tính năng cũ đã hoàn thiện.

**Quy tắc bất biến**: Agent **KHÔNG BAO GIỜ** được thông báo hoàn thành nhiệm vụ nếu chưa chạy test suite và nhận kết quả **100% Pass**.

---

## 2. Chu trình Loop-Until-Green chuẩn 4 bước

```mermaid
flowchart TD
    A[Nhận Yêu Cầu Tính Năng / Bugfix] --> B[Viết Unit / Integration Test Kiểm Chứng]
    B --> C[Chạy Test: Đỏ (Fail / Expected)]
    C --> D[Thực hiện Code / Sửa lỗi]
    D --> E[Chạy lại Test Suite]
    E -->|Vẫn còn lỗi (Fail)| F[Phân tích Traceback & Tự sửa]
    F --> E
    E -->|Toàn bộ Xanh (Green)| G[Chạy Linter & Production Build]
    G -->|Build Fail| F
    G -->|Build Pass| H[Commit & Hoàn Thành]
```

---

## 3. Cách tổ chức Test nhanh không phụ thuộc framework cồng kềnh

Với các dự án TypeScript/JavaScript nhẹ (như `english-no-api`), sử dụng Node.js Test Runner kết hợp với `tsx` mang lại tốc độ thực thi siêu tốc (dưới 100ms cho 30+ test cases):

```json
{
  "scripts": {
    "test": "tsx tests/memoryAndLessons.test.ts"
  }
}
```

### Mẫu Test chuẩn hóa (Node.js native `node:test` + `node:assert`):
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';

test('feature: safe array boundary handling', () => {
  const emptyList = undefined;
  const safeResult = Array.isArray(emptyList) ? [...emptyList] : [];
  assert.equal(safeResult.length, 0);
});
```

---

## 4. Kinh nghiệm thực chiến khi sửa lỗi
1. **Cô lập lỗi bằng test mục tiêu**: Không chạy toàn bộ hệ sinh thái test nếu chỉ sửa 1 component nhỏ; hãy chạy test file liên quan trước để tiết kiệm thời gian, sau đó mới chạy full test suite trước khi commit.
2. **Bắt các lỗi biên (Edge Cases)**:
   - Dữ liệu `null` hoặc `undefined` từ `localStorage` hoặc network.
   - Chuỗi rỗng `""`, số âm, mảng rỗng `[]`.
   - Lỗi bất đồng bộ (`Promise` unhandled rejection).
