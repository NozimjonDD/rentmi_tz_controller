# 3-8 So'rovlar (ijarachi)

**Manba:** [R4 · 4. Bajariladi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665) · [R5 · 4. Bajariladi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) · muddat (SLA): [4-5 SLA va javob vaqti](<../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>)

## Joriy talablar

- So'rov formasini ko'rsatish: qo'shimcha xabar maydoni `R4`
- So'rov formasi yangi maydonlar: kirish sanasi, byudjet (max), ijara muddati, to'lov kuni `R5`
- Rentmi bali tekshiruvi — ball mavjud bo'lmasa S1 ssenariysi taklifi `R4`
- 'So'rov jo'natildi' tasdiqlash modal ekrani (blue checkmark) `R4`
- 'So'rovingiz qabul qilindi' modal — 'Uy egasi bilan bog'lanish' + 'Uy haqida' tugmalari `R4`
- 'So'rovingiz qabul qilinmadi' modal — 'Boshqa uy qidirish' tugmasi `R4`
- Alohida 'So'rovlar' tab (bottom navigation) `R4`
- Filter tabs: Barchasi | Yangi so'rovlar | Rad etilganlar | Tasdiqlanganlar `R4`
- Sort tugmasi: 'Eng oxirgi so'rovlar' `R4`
- Filter bottom sheet: Sana bo'yicha (Dan/Gacha), Lokatsiya, Narx (So'm/Dollar, range slider) `R4`
- Statuslar nomlanishi: "ko'rilmoqda" / "kutilmoqda" / "qabul qilindi" / "rad etildi" / "bekor qilingan" `R5`
  > ⚠ Konflikt: R4 da — Holat badge'lari: qabul qilindi / qabul qilinmadi / tekshirish jarayonida
- So'rovni bekor qilish tugmasi (faqat hali ko'rib chiqilmagan so'rovlar uchun); bekor qilingan so'rov ro'yxatda tegishli badge bilan `R5`
- Tasdiqlangan kartada: 'Uy egasi bilan bog'lanish' blue button `R4`
- Bog'lanish modal: Telefon qilish \[raqam ko'rsatiladi\] | Chat orqali yozish `R4`
- So'rov tasdiqlanganidan so'ng uy egasining telefon raqami ochiladi `R4`
- Xabarnoma so'rovlar tabida ham mavjud: bir xil modal `R4`
- Faqat identifikatsiyadan o'tgan va ro'yxatdan o'tgan ijarachi so'rov yuborishi mumkin `R4 · IJ-R1 BQ-1`
- Bir e'lon bo'yicha bir vaqtda faqat bitta faol so'rov bo'lishi mumkin `R4 · IJ-R1 BQ-2`
- Ruxsat toggle majburiy — yoqilmasdan 'So'rov yuborish' mumkin, so’rov yuborilganida ijarachining rentmi skori bali uy egasiga ko’rsatilinadi, lekin uy egasi ijarachining batafsil malumotlarini ko’ra olmaydi `R4 · IJ-R1 BQ-3`
  > ❓ Ichki nomuvofiqlik: R4 · IJ-R1 da — 'Ma'lumotlarimni uy egasiga berishga roziman' toggle (majburiy, default — o'chirilgan)
  >
  > ❓ Ichki nomuvofiqlik: R4 · IJ-R1 da — 'So'rov yuborish' tugmasi disabled qoladi; toggle belgilash taklif qilinadi
  >
  > Izoh: toggle majburiymi yoki ixtiyoriymi — bitta sahifa ichida zid; hal qilinmagan (N5).

## Use case'lar

| ID | Nomi | Reliz | Holati |
| --- | --- | --- | --- |
| [IJ-R1](<IJ-R1 Ijara so'rovini yuborish/about.md>) | Ijara so'rovini yuborish | R4 | ⚠ CTA nomi R5 da o'zgargan; ❓ toggle |
| [IJ-R2](<IJ-R2 Mening so'rovlarim — holat ro'yxati va filter/about.md>) | Mening so'rovlarim | R4 | ⚠ Statuslar va muddat R5 da o'zgargan |
| [IJ-R3](<IJ-R3 Uy egasi bilan bog'lanish/about.md>) | Uy egasi bilan bog'lanish | R4 | Joriy |
| [R5-IJ-09](<R5-IJ-09 So'rov formasi yangi maydonlar/about.md>) | So'rov formasi yangi maydonlar | R5 | Joriy |
| [R5-IJ-10](<R5-IJ-10 So'rov statuslari va bekor qilish/about.md>) | So'rov statuslari va bekor qilish | R5 | Joriy |
