> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)
>
> ⚠ 7 kunlik muddat va push qoidasi R5 da o'zgargan — [4-5 SLA va javob vaqti](<../../4-5 SLA va javob vaqti/about.md>).

**UE-R4 — So'rovni qabul qilish yoki rad etish**

| **Sseneriy nomi** | So'rovni qabul qilish yoki rad etish |
| --- | --- |
| **Guruh** | So'rov boshqaruvi |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi ijarachi so'rovini qabul qiladi yoki rad etadi. Qabul qilishda ijarachiga uy egasining kontakt ma'lumotlari ochiladi va tasdiq modali ko'rsatiladi. Rad etishda sabab kiritish ixtiyoriy; ijarachiga xabarnoma yuboriladi va u e'lon sahifasiga kirganida modal ko'rsatiladi. Bir e'lon bo'yicha bir vaqtda bir nechta so'rovni tasdiqlash mumkin. |
| **Kirish sharti** | UE-R2 yoki UE-R3 da yangi so'rov mavjud |
| **Chiqish natijasi** | So'rov holati yangilanadi; ijarachiga bildirishnoma yuboriladi; uy egasiga tasdiq modali ko'rsatiladi |
| **Sseneriy ID** | UE-R4 |

**Asosiy oqim — Qabul qilish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | 'So'rovni qabul qilish' tugmasini bosadi (UE-R2 kartasida yoki UE-R3 sticky bottom'da) |
| 2 | **Tizim** | So'rov 'tasdiqlangan' holatiga o'tadi; ijarachiga uy egasining telefon raqami ochiladi |
| 3 | **Tizim** | Ijarachiga push bildirishnoma yuboriladi: 'Uy egasi so'rovingizni qabul qildi' |
| 4 | **Tizim** | 'So'rovni qabul qildingiz' modal ochiladi: ko'k checkmark ikona, 'Ma'lumotlaringiz ijarachiga jo'natildi. Ijarachi siz bilan bog'lanadi' matni |
| 5 | **Tizim** | Modal tugmalari: 'Ijarachi bilan bog'lanish' (ko'k) \| 'So'rovlar ro'yhati' (kulrang) |
| 6 | **Uy egasi** | 'Ijarachi bilan bog'lanish' → UE-C1 chat ekrani; 'So'rovlar ro'yhati' → UE-R2 ga qaytiladi |

**Asosiy oqim — Rad etish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | 'So'rovni rad qilish' tugmasini bosadi |
| 2 | **Tizim** | Rad etish bottom sheet ochiladi: 'Rad etish sababi' matn maydoni (ixtiyoriy) + 'Rad etish' (qizil) + 'Bekor qilish' tugmalari |
| 3 | **Uy egasi** | Sabab yozadi yoki bo'sh qoldiradi → 'Rad etish' tugmasini bosadi |
| 4 | **Tizim** | So'rov 'rad etildi' holatiga o'tadi; ijarachiga push bildirishnoma yuboriladi |
| 5 | **Tizim** | 'So'rovni qabul qilimadingiz' modal ochiladi: qizil X ikona, 'Uy egasiga ma'lumotlaringiz berilmaydi' matni |
| 6 | **Tizim** | Modal tugmasi: 'So'rovlar ro'yhati' → UE-R2 ga qaytiladi |
| 7 | **Tizim** | Ijarachi keyingi safar o'sha e'lon sahifasiga (IJ-08) kirganida 'So'rovingiz qabul qilinmadi' modal ko'rsatiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **7 kun ko'rib chiqilmagan so'rov** | Scheduler avtomatik 'ko'rib chiqilmagan' holatga o'tkazadi; faqat uy egasiga push yuboriladi: 'N ta so'rovingiz ko'rib chiqilmadi' |
| **Bir e'lon bo'yicha bir nechta tasdiqlash** | Tizim bloklashmaydi va ogohlantirish ko'rsatmaydi; ikkinchi ijarachini ham tasdiqlash mumkin |
| **UE-R2 kartasidan tezkor qaror** | UE-R3 ga o'tmasdan to'g'ridan-to'g'ri UE-R4 oqimi ishga tushadi |
| **'Bekor qilish' (rad etish oqimida)** | Bottom sheet yopiladi; so'rov holati o'zgarmaydi; UE-R3 ga qaytiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Qaror saqlanmaydi; 'Internet aloqasi yo'q' xabari; bottom sheet ochiq qoladi |
| **Server xatosi** | Xabar va Retry; holat o'zgarmaydi |
| **FCM push yuborib bo'lmadi** | Qaror saqlanadi; push fon rejimda qayta uriniladi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Qabul qilishda ijarachiga uy egasining telefon raqami ochiladi |
| **BQ-2** | Rad etishda sabab kiritish ixtiyoriy — bo'sh holda ham rad etish mumkin |
| **BQ-3** | 7 kun ko'rib chiqilmagan so'rov avtomatik 'ko'rib chiqilmagan' holatga o'tadi; faqat uy egasiga push yuboriladi (ijarachiga emas) |
| **BQ-4** | Bir e'lon bo'yicha bir vaqtda bir nechta so'rovni tasdiqlash mumkin — tizim bloklashmaydi |
| **BQ-5** | Rad etilgan so'rovda ijarachiga darhol modal ko'rsatilmaydi — u keyingi safar o'sha e'lon sahifasiga kirganida modal avtomatik ochiladi |
| **BQ-6** | Qaror audit jurnaliga yoziladi (kim, qachon, nima) |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Qabul qilishda ≤3 s ichida tasdiq modal ko'rsatiladi |
| **AC-2** | Qabul qilishda ijarachiga ≤10 s ichida push bildirishnoma yuboriladi |
| **AC-3** | Rad etishda sabab maydoni bo'sh bo'lsa ham 'Rad etish' tugmasi faol ko'rsatiladi |
| **AC-4** | 7 kun o'tgach ko'rib chiqilmagan so'rov UE-R2 da 'Ko'rib chiqilmadi' badge bilan ko'rsatiladi |
| **AC-5** | Bir e'lon bo'yicha ikkinchi so'rov tasdiqlanganida ogohlantirish modal ko'rsatilmaydi |
