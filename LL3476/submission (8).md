# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3476 - [LEARNING LOGS] CuteCat CuteFox
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text

```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
3-6 hours
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
- Input: บรรทัดแรก n / อีก n บรรทัดเป็น String รูปแบบ Dictionary `{"Name": "TypeNo"}`
- Output: จำนวนแมว / จำนวนจิ้งจอก / รายชื่อเรียงตามประเภท (Cat ก่อน Fox) และเรียงลำดับตามตัวเลขรหัส
- Constraints: ห้ามมีชื่อหรือรหัสซ้ำกัน และต้องใช้ Dictionary ช่วยจัดการข้อมูล
```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
1. รับจำนวน n แล้ววนลูปอ่าน String Dictionary โดยแปลงเป็น Dict ด้วย `ast.literal_eval`
2. เก็บข้อมูลลง Dict โดยสลับใช้รหัส (เช่น Cat06) เป็น Key และใช้ชื่อเป็น Value เพื่อความง่ายในการค้นหา
3. ตรวจสอบว่ามี Cat01 และ Fox01 หรือยัง ถ้ายังไม่มีให้ใส่ Garfield (Cat01) และ Fubuki (Fox01) เพิ่มเข้าไป
4. แยก Key ออกเป็นกลุ่ม Cat และ Fox แล้วเรียงลำดับโดยตัดเอาเฉพาะตัวเลขด้านหลังมาเทียบ
5. พิมพ์จำนวนรวม และวนลูปแสดงผล `[ชื่อ] : [รหัส]`
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
- เช็กว่า Garfield/Cat01 และ Fubuki/Fox01 มีอยู่หรือยังด้วย `.values()` และ `in animal`
- สร้างฟังก์ชัน `kk(x)` เพื่อแปลงส่วนตัวเลข `int(x[3:])` มาใช้เป็น Key ในการ `.sort()`
- พิมพ์สรุปจำนวน `Cat : X` และ `Fox : Y` แล้ววนลูปพิมพ์ผลลัพธ์ Cat ก่อนแล้วตามด้วย Fox
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
เคสปกติที่ไม่มี Cat01 และ Fox01 มาให้
```

Input:

```text
5
  {"Chi" : "Cat06"}
  {"Tom" : "Cat05"}
  {"Shiro" : "Fox02"}
  {"Senko" : "Fox10"}
  {"Chocola" : "Cat03"}
```

Expected output:

```text
Cat : 4
  Fox : 3
  Garfield : Cat01
  Chocola : Cat03
  Tom : Cat05
  Chi : Cat06
  Fubuki : Fox01
  Shiro : Fox02
  Senko : Fox10
```

Actual output:

```text
Cat : 4
  Fox : 3
  Garfield : Cat01
  Chocola : Cat03
  Tom : Cat05
  Chi : Cat06
  Fubuki : Fox01
  Shiro : Fox02
  Senko : Fox10
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
มี Cat01 และ Fox01 ระบุมาใน Input
```

Input:

```text
2
  {"Neko" : "Cat01"}
  {"Kitsune" : "Fox01"}
```

Expected output:

```text
Cat : 1
  Fox : 1
  Neko : Cat01
  Kitsune : Fox01
```

Actual output:

```text
Cat : 1
  Fox : 1
  Neko : Cat01
  Kitsune : Fox01
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ตัวเลขรหัสหลักสิบ
```

Input:

```text
- Input:
  2
  {"A" : "Cat10"}
  {"B" : "Cat02"}
```

Expected output:

```text
Fox : 1
  Garfield : Cat01
  B : Cat02
  A : Cat10
  Fubuki : Fox01
```

Actual output:

```text
Fox : 1
  Garfield : Cat01
  B : Cat02
  A : Cat10
  Fubuki : Fox01
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
Yes
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
