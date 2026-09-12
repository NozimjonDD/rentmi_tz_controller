> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-R3 — Ijarachi ma'lumotlarini ko'rish**

| **Sseneriy nomi** | Ijarachi ma'lumotlarini ko'rish (Rentmi skore + ijara tarixi) |
| --- | --- |
| **Guruh** | So'rov boshqaruvi |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi ijarachi tafsilot sahifasida shaxsiy ma'lumotlar, Rentmi skore, to'lov intizomi va ijara tarixini ko'radi. Ijarachi toggle'ni yoqmagan bo'lsa — daromadlar va ijara tarixi bo'limlari xiralashtirilgan (disabled) ko'rinishda ko'rsatiladi; Rentmi skore bali har doim ko'rinadi. Sahifada chat ikona va sticky bottom'da qaror tugmalari mavjud. |
| **Kirish sharti** | UE-R2 da 'Batafsil' bosilgan |
| **Chiqish natijasi** | Uy egasi ijarachi to'liq yoki cheklangan profilini ko'radi; qaror qabul qiladi yoki chat ochadi |
| **Sseneriy ID** | UE-R3 |

**Asosiy oqim — Toggle yoqilgan (to'liq profil)**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Sahifa ochiladi: sarlavha 'Ijarachi ma'lumotlari'; qaytish (←) va chat ikona header'da |
| 2 | **Tizim** | Shaxsiy ma'lumotlar bloki: avatar, ism, MyID badge (identifikatsiyadan o'tgan), telefon raqami, oilaviy holat |
| 3 | **Tizim** | So'rov jo'natilgan uy mini-kartasi: e'lon rasmi, nomi, manzili, maydoni, narxi |
| 4 | **Tizim** | Daromadlar bloki: 'Tasdiqlanga' yoki 'Tasdiqlanmagan ' badge; umumiy ish faoliyati (yil), joriy ish joyi (oy), norasmiy daromad holati |
| 5 | **Tizim** | Rentmi skore gauge: N/100, rang (yashil/sariq/qizil), label (Ishonchli/O'rtacha/Ishonchsiz ijarachi) |
| 6 | **Tizim** | To'lov intizomi bloki: Kredit byuro skori (raqam + holat), MIB qarzdorligi, Soliq qarzdorligi |
| 7 | **Tizim** | Ijara tarixi bloki: Tavsiyanomalar (N ta), Ijara to'lovi intizomi, Kommunal to'lovlar, Mulkka yetkazilgan zarar, Qo'shnilardan shikoyat, Shartnoma shartlari buzilganmi — har biri yashil/qizil holat bilan |
| 8 | **Tizim** | Sticky bottom: 'So'rovni qabul qilish' (ko'k, to'liq) \| 'So'rovni rad qilish' (pushti, outline) \| chat ikona |

**Muqobil oqim — Toggle yoqilmagan (cheklangan profil)**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Shaxsiy ma'lumotlar va Rentmi skore gauge — to'liq ko'rsatiladi (o'zgarmaydi) |
| 2 | **Tizim** | Daromadlar bloki — xiralashtirilgan (overlay) ko'rinishda: ma'lumotlar ko'rinadi lekin o'qib bo'lmaydi; 'Ma'lumotlarni ko'rish uchun ijarachi ruxsat berishi kerak' tushuntirish matni |
| 3 | **Tizim** | To'lov intizomi bloki — xiralashtirilgan ko'rinishda |
| 4 | **Tizim** | Ijara tarixi bloki — xiralashtirilgan ko'rinishda |
| 5 | **Tizim** | Sticky bottom tugmalari va chat ikona — o'zgarmaydi, qaror qabul qilish mumkin |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Chat ikonasi bosiladi** | UE-C1 chat ekrani ochiladi (qarordan oldin ham mumkin) |
| **'So'rovni qabul qilish' bosiladi** | UE-R4 qabul oqimi → 'So'rovni qabul qildingiz' modal |
| **'So'rovni rad qilish' bosiladi** | UE-R4 rad oqimi → sabab kiritish (ixtiyoriy) → modal |
| **Tasdiqlangan so'rov tafsiloti** | Sticky bottom'da faqat chat ikona; qaror tugmalari yo'q |
| **Tavsiyanomalar bo'limi bosiladi** | Tavsiyanomalar to'liq ko'rsatilgan sahifaga o'tiladi (toggle yoqilgan holatda) |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh ma'lumotlar ko'rsatiladi; banner; qaror tugmalari disabled |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Rentmi skore bali toggle holati qanday bo'lishidan qat'iy nazar doim ko'rsatiladi |
| **BQ-2** | Toggle yoqilmagan holda daromadlar, to'lov intizomi va ijara tarixi bo'limlari xiralashtirilgan overlay bilan ko'rsatiladi — ma'lumotlar ko'rinadi lekin o'qib bo'lmaydi |
| **BQ-3** | Toggle yoqilmagan holatda ham uy egasi qaror qabul qilishi mumkin — to'liq profilsiz ham tasdiqlash yoki rad etish imkoni bor |
| **BQ-4** | Chat ikona toggle holatidan qat'iy nazar mavjud; rad etilgan so'rovda chat disabled |
| **BQ-5** | Sticky bottom doim ekran pastida fiksirlangan ko'rinadi (scroll qilganda ham) |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Sahifa ≤3 s ichida yuklanadi |
| **AC-2** | Toggle yoqilmagan holatda daromadlar, to'lov intizomi va ijara tarixi bo'limlari ustida xiralashtirilgan overlay ko'rinadi va ma'lumotlar o'qilmaydi |
| **AC-3** | Rentmi skore gauge toggle holatidan qat'iy nazar to'g'ri qiymat bilan ko'rsatiladi |
| **AC-4** | Chat ikona bosilganda UE-C1 ga o'tiladi; qaror qabul qilinmaganida ham ishlaydi |
| **AC-5** | Sticky bottom 'So'rovni qabul qilish' va 'So'rovni rad qilish' tugmalari sahifani scroll qilganda ham ko'rinib turadi |
