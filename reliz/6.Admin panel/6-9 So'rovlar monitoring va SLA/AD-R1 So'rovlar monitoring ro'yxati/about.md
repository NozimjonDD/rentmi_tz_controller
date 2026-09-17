> Manba: [Release 4 14.06.2026 · Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360160)
>
> ⚠ Eksport R5 da SLA ko'rinishi uchun qo'shilgan — [6-9 So'rovlar monitoring va SLA](<../about.md>).

**AD-R1 — So'rovlar monitoring ro'yxati**

| **Sseneriy nomi** | So'rovlar monitoring ro'yxati |
| --- | --- |
| **Guruh** | So'rovlar monitoring |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator admin panel'da barcha so'rovlarni jadval ko'rinishida kuzatadi. Holat, sana va matn bo'yicha filtrlash va qidiruv imkoniyati mavjud. Eksport funksionali yo'q. |
| **Kirish sharti** | Administrator admin panel'ga kirgan; 'So'rovlar' bo'limini ochgan |
| **Chiqish natijasi** | Administrator so'rovlarni ko'radi, filtrlaydi va tafsilotga kiradi |
| **Sseneriy ID** | AD-R1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Administrator** | Admin panel'da 'So'rovlar' bo'limini ochadi |
| 2 | **Tizim** | Jadval ko'rsatiladi. Ustunlar: Ijarachi ismi \| Uy egasi ismi \| E'lon nomi \| So'rov sanasi \| So'rov xabari \| Ruxsat (Ha/Yo'q) \| Holat |
| 3 | **Tizim** | Default tartib: so'rov sanasi bo'yicha kamayish (eng yangi yuqorida) |
| 4 | **Tizim** | Filter paneli: Holat (Barchasi / Yangi / Tasdiqlangan / Rad etilgan / Ko'rib chiqilmagan); Sana oralig'i (dan/gacha) |
| 5 | **Administrator** | Qidiruv satriga ijarachi ismi, telefon raqami yoki e'lon nomini kiritadi → jadval real-time filtrlaydi |
| 6 | **Administrator** | Filter parametrlarini tanlaydi → jadval yangilanadi |
| 7 | **Administrator** | So'rov qatorini bosadi → AD-R2 tafsilot sahifasi ochiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Filterlar tozalanadi** | Barcha parametrlar bir vaqtda olib tashlanadi; to'liq ro'yxat qaytadi |
| **Qidiruv natijasi bo'sh** | 'Mos yozuv topilmadi' placeholder ko'rsatiladi |
| **Holat filtri o'zgartirilsa** | Jadval ≤2 s ichida yangilanadi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q / server xatosi** | Xabar va Retry; jadval bo'sh ko'rsatiladi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Jadval ustunlari: Ijarachi ismi, Uy egasi ismi, E'lon nomi, So'rov sanasi, So'rov xabari, Ruxsat (Ha/Yo'q), Holat |
| **BQ-2** | Ruxsat ustuni: ijarachi toggle yoqilgan bo'lsa 'Ha', o'chirilgan bo'lsa 'Yo'q' |
| **BQ-3** | Holat qiymatlari: Yangi \| Tasdiqlangan \| Rad etilgan \| Ko'rib chiqilmagan |
| **BQ-4** | Qidiruv ijarachi ismi, telefon raqami va e'lon nomi bo'yicha ishlaydi |
| **BQ-5** | Eksport funksionali yo'q |
| **BQ-6** | Default tartib: so'rov sanasi kamayish bo'yicha |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Jadval ≤3 s ichida yuklanadi |
| **AC-2** | Barcha 7 ta ustun to'g'ri ma'lumotlar bilan ko'rsatiladi |
| **AC-3** | Qidiruv satriga kiritishda jadval real-time filtrlaydi |
| **AC-4** | Holat filtri o'zgartirilganda jadval ≤2 s ichida yangilanadi |
| **AC-5** | So'rov qatori bosilganda AD-R2 ochiladi |
