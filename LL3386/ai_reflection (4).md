# บันทึก Reflection การใช้ AI

ใช้ไฟล์นี้เฉพาะเมื่อมีการใช้ AI กับโจทย์ OJ ที่เป็น learning-log-required เท่านั้น

ให้ copy template นี้ แล้วเปลี่ยนชื่อไฟล์เป็น:

```text
ai_reflection.md
```

เขียน reflection นี้ด้วยคำพูดของตนเอง

ห้ามวาง AI conversation ทั้งหมด

ห้ามให้ AI เขียน reflection นี้แทนคุณ

AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียน reflection ของตนเองแล้ว

---

## 1. ข้อมูล OJ

| Item | Answer |
|---|---|
| OJ problem number/title | OJ3386 - [LEARNING LOGS] Duplicate I |
| OJ submission ID, if submitted |  |
| OJ status | Pass |

---

## 2. เครื่องมือ AI ที่ใช้

เขียนชื่อเครื่องมือ AI ที่ใช้

ตัวอย่าง:

```text
ChatGPT
Claude
Gemini
ChatGPT Codex / OpenAI Codex / Codex CLI
Claude Code
Other: ...
```

My answer:

```text
Gemini
```

---

## 3. การตรวจสอบนโยบายการใช้ AI ของรายวิชา

ตอบหัวข้อนี้อย่างซื่อสัตย์

หัวข้อนี้ยืนยันว่าคุณได้ทำตาม AI workflow ของรายวิชาก่อนและระหว่างใช้ AI

| Statement | Yes / No / Not Applicable | Short note |
|---|---|---|
| I read the relevant workflow before using AI. | Yes | อ่านแนวทางของวิชาก่อนเริ่มใช้งาน |
| I used `instructions/COURSE_AI_INSTRUCTIONS.md`, `instructions/AGENTS.md`, or manually followed the course AI instructions if the tool did not support custom instructions. | Yes | ทำตามกรอบ ไม่ได้ให้ AI ทำแทน |
| I wrote my own problem understanding before asking AI for help. | Yes | สรุปเรื่องหาตัวซ้ำและเรียงลำดับเองก่อน |
| I wrote my own first plan before asking AI for help. | Yes | คิดวิธีใช้ Set และ Intersection เองก่อน |
| I used AI as a coach, reviewer, debugger, or test-case helper, not as a full-answer generator. | Yes | ใช้ช่วยตรวจตรรกะความเร็วในการค้นหา |

ถ้าตอบ "No" ในข้อใด ให้อธิบายเหตุผล:

```text

```

---

## 4. ฉันถาม AI ให้ช่วยอะไร

อธิบายสั้น ๆ ว่าถาม AI ให้ช่วยเรื่องอะไร

ห้ามวาง chat log ทั้งหมด

ตัวอย่าง:

- ฉันถาม AI ให้ช่วยอธิบายโจทย์ด้วยภาษาที่เข้าใจง่ายขึ้น
- ฉันถาม AI ให้ช่วย review แผนแรกของฉัน
- ฉันถาม AI ให้ช่วยหา bug ใน code
- ฉันถาม AI ให้ช่วยเสนอ test cases
- ฉันถาม AI ให้อธิบายว่าทำไม output ของฉันต่างจาก expected output

My answer:

```text
ถาม AI ให้ช่วยรีวิวโค้ดว่าการใช้ Set Intersection (&) และการเรียงจากมากไปน้อยด้วย reversed(sorted()) ทำงานถูกต้องและมีประสิทธิภาพดีที่สุดตามเงื่อนไขโจทย์ไหม
```

---

## 5. AI ช่วยให้ฉันสังเกตอะไร

เขียนว่า AI ช่วยให้คุณสังเกตอะไร

ตัวอย่าง:

- ความเข้าใจผิดเกี่ยวกับโจทย์
- condition ที่ขาดไป
- bug ในการอ่าน input
- edge case
- ปัญหา syntax ของ Python
- ปัญหา output formatting

My answer:

```text
AI ช่วยให้สังเกตว่าการใช้ Set ในการหา Intersection มีความเร็วสูงมาก O(min(m, n)) เมื่อเทียบกับการใช้ List วนลูปเทียบทีละตัว ซึ่งจะช่วยป้องกันปัญหา Time Limit Exceeded เมื่อข้อมูลมีขนาดใหญ่
```

---

## 6. ฉันตรวจสอบหรือแก้อะไรด้วยตนเอง

เขียนว่าหลังจากได้รับความช่วยเหลือจาก AI คุณตรวจสอบ ทดสอบ หรือแก้อะไรด้วยตนเอง

ตัวอย่าง:

- ฉันตรวจ input format ใน OJ problem อีกครั้ง
- ฉันทดสอบ code ใน VS Code
- ฉันเปรียบเทียบ expected output กับ actual output
- ฉันแก้ loop condition ด้วยตนเอง
- ฉันไม่ใช้บางคำแนะนำของ AI เพราะไม่ตรงกับ constraints ของโจทย์
- ฉันปรับคำแนะนำของ AI ให้เป็น code ที่ฉันเข้าใจเอง

My answer:

```text
เอารหัสนักศึกษาทดสอบรันใน VS Code เช็กเคสไม่มีตัวซ้ำว่าพิมพ์ "Nope" จริงไหม และเช็กเคสมีตัวซ้ำว่าเรียงรหัสจากมากไปน้อยถูกต้องตามโจทย์สั่ง
```

---

## 7. ฉันได้เรียนรู้อะไร

เขียน 2-4 ประโยคเกี่ยวกับสิ่งที่ได้เรียนรู้จากโจทย์นี้และจากกระบวนการใช้ AI ช่วย

ให้เน้นการเรียนรู้ของตนเอง

ห้ามเขียนแค่ว่า "I learned coding" หรือ "AI helped me."

My answer:

```text
ได้เรียนรู้ประสิทธิภาพของ Set Data Structure ใน Python ในการหาจุดตัดข้อมูล (Intersection) ได้อย่างรวดเร็ว และได้ฝึกใช้ flag ตัวแปรในการเช็กสถานะเพื่อพิมพ์ข้อความแจ้งเตือนเมื่อไม่พบข้อมูล
```

---

## 8. คำรับรองของนักศึกษา

ตอบอย่างซื่อสัตย์

| Statement | Yes / No |
|---|---|
| I wrote this reflection in my own words. | Yes |
| This reflection describes my real AI use. | Yes |
| I checked AI's suggestions before using them. | Yes |
| I can explain my final code. | Yes |
| I did not ask AI to write this reflection for me. | Yes |
