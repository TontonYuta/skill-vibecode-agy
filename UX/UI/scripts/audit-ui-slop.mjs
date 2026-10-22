#!/usr/bin/env node

/**
 * 🕵️‍♂️ Anti-AI-Slop Playwright Inspector
 * Quét giao diện trang web để tự động phát hiện các dấu hiệu "AI Slop"
 * và vi phạm tiêu chuẩn UX/UI hiện đại.
 * 
 * Cách dùng:
 *   node UX/UI/scripts/audit-ui-slop.mjs https://your-app.com
 *   node UX/UI/scripts/audit-ui-slop.mjs http://localhost:3000
 *   node UX/UI/scripts/audit-ui-slop.mjs ./dist/index.html
 */

import { chromium } from '/home/tontonyuta/.gemini/antigravity-cli/brain/b8d2d63e-ace4-49d2-86f4-48cbb8f5023c/scratch/pw/node_modules/playwright-core/index.mjs';
import { pathToFileURL } from 'url';
import fs from 'fs';
import path from 'path';

const target = process.argv[2] || 'https://impeccable.style';

console.log(`\n======================================================`);
console.log(`🔍 KHỞI ĐỘNG ANTI-AI-SLOP AUDITOR: ${target}`);
console.log(`======================================================\n`);

async function runAudit() {
  const browser = await chromium.launch({
    executablePath: '/home/tontonyuta/.local/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  let targetUrl = target;
  if (!target.startsWith('http://') && !target.startsWith('https://')) {
    const fullPath = path.resolve(target);
    if (fs.existsSync(fullPath)) {
      targetUrl = pathToFileURL(fullPath).href;
    }
  }

  try {
    await page.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  } catch (err) {
    console.error(`❌ Không thể truy cập trang: ${err.message}`);
    await browser.close();
    process.exit(1);
  }

  const auditResults = await page.evaluate(() => {
    const issues = [];
    const elements = Array.from(document.querySelectorAll('*'));

    // 1. Kiểm tra lạm dụng Gradient Tím - Xanh
    elements.forEach(el => {
      const style = window.getComputedStyle(el);
      const bg = style.backgroundImage;
      if (bg && bg.includes('linear-gradient')) {
        const hasPurple = bg.includes('139, 92, 246') || bg.includes('168, 85, 247') || bg.toLowerCase().includes('purple');
        const hasCyan = bg.includes('6, 182, 212') || bg.includes('14, 165, 233') || bg.toLowerCase().includes('cyan');
        if (hasPurple && hasCyan) {
          issues.push({
            type: 'AI_SLOP_PURPLE_CYAN_GRADIENT',
            severity: 'HIGH',
            element: el.tagName.toLowerCase() + (el.className ? `.${el.className.split(' ').slice(0, 2).join('.')}` : ''),
            message: 'Phát hiện gradient tím - xanh sáo rỗng. Nên dùng nền trung tính với 1 màu Accent duy nhất.'
          });
        }
      }
    });

    // 2. Kiểm tra hiện tượng Card lồng Card (Nested Cards > 2 cấp)
    const cards = Array.from(document.querySelectorAll('[class*="card"], [class*="rounded-"], [class*="border"]'));
    cards.forEach(card => {
      let depth = 0;
      let parent = card.parentElement;
      while (parent) {
        if (parent.className && (parent.className.includes('card') || (parent.className.includes('border') && parent.className.includes('rounded')))) {
          depth++;
        }
        parent = parent.parentElement;
      }
      if (depth >= 2) {
        issues.push({
          type: 'AI_SLOP_CARDOCALYPSE_NESTED',
          severity: 'MEDIUM',
          element: card.tagName.toLowerCase() + (card.className ? `.${card.className.split(' ').slice(0, 2).join('.')}` : ''),
          message: `Lồng card quá sâu (Cấp độ ${depth + 1}). Nên làm phẳng giao diện bằng khoảng trắng hoặc divider.`
        });
      }
    });

    // 3. Kiểm tra Hoạt họa vô nghĩa (Bouncing, continuous ping/pulse)
    elements.forEach(el => {
      const style = window.getComputedStyle(el);
      const anim = style.animationName;
      if (anim && (anim.includes('bounce') || anim.includes('wiggle'))) {
        issues.push({
          type: 'AI_SLOP_BOUNCY_ANIMATION',
          severity: 'MEDIUM',
          element: el.tagName.toLowerCase(),
          message: 'Hoạt họa rung lắc/bouncing làm phân tâm và tạo cảm giác nghiệp dư.'
        });
      }
    });

    // 4. Phát hiện từ ngữ tiếp thị sáo rỗng (Vapid Buzzwords)
    const buzzwords = [
      'supercharge',
      'unleash the power',
      'next-generation',
      'empower your workflow',
      'not just a tool',
      'seamless experience',
      'world-class'
    ];
    const textContent = document.body.innerText.toLowerCase();
    buzzwords.forEach(bw => {
      if (textContent.includes(bw)) {
        issues.push({
          type: 'AI_SLOP_VAPID_COPYWRITING',
          severity: 'LOW',
          element: 'BODY',
          message: `Chứa từ ngữ tiếp thị rỗng: "${bw}". Hãy thay bằng giá trị cụ thể và đo lường được.`
        });
      }
    });

    // 5. Kiểm tra khả năng tiếp cận (Accessibility WCAG AA Contrast sơ bộ)
    const textNodes = Array.from(document.querySelectorAll('p, span, h1, h2, h3, h4, a, button'));
    textNodes.slice(0, 50).forEach(el => {
      const style = window.getComputedStyle(el);
      const color = style.color;
      // Phát hiện xám quá nhạt trên nền tối
      if (color.includes('rgba(255, 255, 255, 0.2') || color.includes('rgba(255, 255, 255, 0.3')) {
        issues.push({
          type: 'ACCESSIBILITY_LOW_CONTRAST',
          severity: 'HIGH',
          element: el.tagName.toLowerCase() + (el.id ? `#${el.id}` : ''),
          message: `Chữ quá mờ (${color}), nguy cơ không đạt tỷ lệ tương phản tối thiểu 4.5:1 của WCAG AA.`
        });
      }
    });

    return {
      totalEvaluated: elements.length,
      issues: issues.slice(0, 20) // lấy 20 mẫu tiêu biểu
    };
  });

  await browser.close();

  // Báo cáo kết quả
  console.log(`📊 TỔNG SỐ PHẦN TỬ ĐÃ QUÉT: ${auditResults.totalEvaluated}`);
  console.log(`⚠️  SỐ LƯỢNG VẤN ĐỀ PHÁT HIỆN: ${auditResults.issues.length}\n`);

  if (auditResults.issues.length === 0) {
    console.log(`🎉 CHÚC MỪNG! Không phát hiện dấu hiệu AI Slop nghiêm trọng nào trên giao diện.`);
  } else {
    auditResults.issues.forEach((iss, idx) => {
      const colorTag = iss.severity === 'HIGH' ? '🔴' : iss.severity === 'MEDIUM' ? '🟡' : '🔵';
      console.log(`${colorTag} [${iss.severity}] ${iss.type} tại <${iss.element}>`);
      console.log(`   └─ ${iss.message}`);
    });
  }

  console.log(`\n======================================================`);
  console.log(`✅ HOÀN TẤT KIỂM THẨM GIAO DIỆN.`);
  console.log(`======================================================\n`);
}

runAudit().catch(e => {
  console.error("Lỗi thực thi:", e);
  process.exit(1);
});
