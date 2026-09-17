> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)
>
> ⚠ CTA nomi R5 da o'zgargan ([3-6 E'lon detail sahifasi](<../../3-6 E'lon detail sahifasi/about.md>)); ❓ ruxsat toggle bo'yicha ichki nomuvofiqlik — [3-8 So'rovlar](<../about.md>).

**IJ-R1 — Ijara so'rovini yuborish**

| **Sseneriy nomi** | Ijara so'rovini yuborish |
| --- | --- |
| **Guruh** | So'rov |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan va identifikatsiyadan o'tgan) |
| **Tavsif** | Ijarachi e'lon detail sahifasidan so'rov yuboradi. Bottom sheet'da xabar maydoni va ma'lumotlarni berishga ruxsat knopkasi ko'rinadi. Yuborilgandan so'ng 'So'rov jo'natildi' modali ochiladi. Rentmi bali mavjud bo'lmasa S1 ssenariysi (hisobot xarid qilish) taklif qilinadi. |
| **Kirish sharti** | Ijarachi IJ-08 sahifasida; tanlangan e'lon faol holatda; ijarachi identifikatsiyadan o'tgan |
| **Chiqish natijasi** | So'rov 'ko'rib chiqish kutmoqda' holatida saqlanadi; uy egasiga push bildirishnoma yuboriladi; ijarachiga tasdiq modali ko'rsatiladi |
| **Sseneriy ID** | IJ-R1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | E'lon detail sahifasida 'So'rov jo'natish' (ko'k CTA) tugmasini bosadi |
| 2 | **Tizim** | Rentmi bali tekshiriladi: mavjud va muddati o'tmagan bo'lsa — davom etadi; yo'q yoki muddati o'tgan bo'lsa — S1 ssenariysi (Rentmi hisobotini xarid qilish) taklif qilinadi |
| 3 | **Tizim** | Bottom sheet ochiladi: 'Xabar maydoni' (ixtiyoriy) + 'Ma'lumotlarimni uy egasiga berishga roziman' toggle (majburiy, default — o'chirilgan) |
| 4 | **Ijarachi** | Xabar yozadi (ixtiyoriy) va ruxsat toggleni yoqadi |
| 5 | **Ijarachi** | 'So'rov yuborish' tugmasini bosadi |
| 6 | **Tizim** | Validatsiya: toggle yoqilganligini tekshiradi; ayni shu e'lon bo'yicha faol so'rov mavjudligini tekshiradi; ijarachi blacklist'da emasligini tekshiradi |
| 7 | **Tizim** | So'rov 'ko'rib chiqish kutmoqda' holatida saqlanadi; uy egasiga push va tizim ichidagi bildirishnoma yuboriladi |
| 8 | **Tizim** | 'So'rov jo'natildi' modal ochiladi (ko'k checkmark ikona, tasdiqlash matni) |
| 9 | **Ijarachi** | Modalni yopadi → IJ-08 ga qaytadi; CTA endilikda 'So'rov jo'natildi ✓' ko'rinishida (disabled) |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Rentmi bali yo'q yoki muddati o'tgan** | S1 ssenariysi taklif qilinadi: 'Rentmi hisobotini xarid qiling' bottom sheet; ijarachi rad etsa — so'rov formasiga qaytiladi |
| **Takroriy so'rov (faol so'rov mavjud)** | Yangi so'rov bloklanadi; 'Bu e'lon bo'yicha so'rovingiz allaqachon mavjud' xabari; IJ-R2 ga o'tish taklif qilinadi |
| **Ijarachi blacklist'da** | So'rov bloklanadi; 'So'rov yuborish imkoni yo'q' xabari ko'rsatiladi |
| **E'lon so'rov paytida nofaol bo'lib qolsa** | So'rov bekor qilinadi; ijarachiga xabar ko'rsatiladi |
| **Toggle yoqilmagan holda yuborish urinishi** | 'So'rov yuborish' tugmasi disabled qoladi; toggle belgilash taklif qilinadi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | So'rov saqlanmaydi; 'Internet aloqasi yo'q' xabari; kiritilgan matn saqlanib qoladi |
| **Server xatosi** | Xabar va Retry; matn yo'qolmaydi |
| **FCM push yuborib bo'lmadi** | So'rov saqlanadi; push fon rejimda qayta uriniladi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Faqat identifikatsiyadan o'tgan va ro'yxatdan o'tgan ijarachi so'rov yuborishi mumkin |
| **BQ-2** | Bir e'lon bo'yicha bir vaqtda faqat bitta faol so'rov bo'lishi mumkin |
| **BQ-3** | Ruxsat toggle majburiy — yoqilmasdan 'So'rov yuborish' mumkin, so’rov yuborilganida ijarachining rentmi skori bali uy egasiga ko’rsatilinadi, lekin uy egasi ijarachining batafsil malumotlarini ko’ra olmaydi |
| **BQ-4** | Xabar maydoni ixtiyoriy — bo'sh bo'lishi mumkin |
| **BQ-5** | S1 rad etilsa ijarachi so'rov formasiga qaytadi lekin so'rovni yubora olmaydi |
| **BQ-6** | Blacklist'dagi ijarachi so'rov yuborolmaydi — CTA disabled ko'rsatiladi |
| **BQ-7** | Yuborilgandan so'ng CTA 'So'rov jo'natildi ✓' holatiga o'tadi va disabled bo'ladi, va chat qilish va telefon qilish ikonkalari ko’rsatilinadi, uy egasiga ijarachi chat orqali murojaat qilishi mumkin, lekin uy egasi ijarachi so’rovini qabul qilmaguniga qadar ijarachi uy egasi telefon kontakt malumotini ololmaydi |
| **BQ-8** | Uy egasiga push bildirishnoma ≤10 s ichida yuborilishi kerak |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Bottom sheet ≤2 s ichida ochiladi |
| **AC-2** | Toggle yoqilmagan holda 'So'rov yuborish' bosilsa, ijarachining to’liq xisoboti uy egasiga ko’rsatilinmaydi, disabled xolatda bo’ladi, uy egasi ijarachi malumotlarini ochishi mumkin lekin to’liq ko’ra olmaydi |
| **AC-3** | Ayni shu e'lon bo'yicha faol so'rov mavjud bo'lsa — yangi so'rov yuborib bo'lmaydi va IJ-R2 ga o'tish taklif qilinadi |
| **AC-4** | Blacklist'dagi ijarachi uchun 'So'rov jo'natish' CTA disabled holatda ko'rinadi |
| **AC-5** | 'So'rov jo'natildi' modal yuborilgandan ≤3 s ichida ko'rsatiladi |
| **AC-6** | CTA yuborilgandan so'ng 'So'rov jo'natildi ✓' holatiga o'tadi va qayta bosilmaydi |
| **AC-7** | Rentmi bali yo'q holatda S1 taklifi ko'rsatiladi; rad etilsa so'rov formasiga qaytiladi |
