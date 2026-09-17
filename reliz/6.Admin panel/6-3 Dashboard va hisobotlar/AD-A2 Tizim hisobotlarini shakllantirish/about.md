> Manba: [Release 4 14.06.2026 · Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360160)

**AD-A2 — Tizim hisobotlarini shakllantirish**

| **Sseneriy nomi** | Tizim hisobotlarini shakllantirish |
| --- | --- |
| **Guruh** | Analitika va hisobotlar |
| **Aktorlar** | Administrator, Texnik qo'llab-quvvatlash xodimi |
| **Tavsif** | Administrator yoki texnik qo'llab-quvvatlash xodimi hisobotlar bo'limida turli statistik ma'lumotlarni sana va filtrlar bo'yicha shakllantiradi, jadval va grafik ko'rinishida ko'radi. Tashqi integratsiyalar holati real-time monitoriging qilinadi. |
| **Kirish sharti** | Foydalanuvchi admin panel'ga kirgan; 'Hisobotlar va analitika' bo'limini ochgan |
| **Chiqish natijasi** | Hisobot shakllantiriladi; PDF, XLSX yoki CSV formatida yuklab olinadi (ixtiyoriy) |
| **Sseneriy ID** | AD-A2 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Administrator** | 'Hisobotlar va analitika' bo'limini ochadi |
| 2 | **Tizim** | Mavjud hisobot turlari ko'rsatiladi (quyida ro'yxat) |
| 3 | **Administrator** | Hisobot turini tanlaydi; davr (sana oralig'i) va filtrlarni belgilaydi |
| 4 | **Tizim** | Hisobot shakllantiriladi va jadval/grafik ko'rinishida ko'rsatiladi (≤30 s) |
| 5 | **Administrator** | Hisobotni yuklab oladi: PDF, XLSX yoki CSV (ixtiyoriy) |
| 6 | **Tizim** | Audit jurnaliga hisobot shakllantirish yozuvi kiritiladi |

**Hisobot turlari**

| **Hisobot turi** | **Tarkibi** |
| --- | --- |
| **Foydalanuvchilar statistikasi** | Ro'yxatdan o'tganlar, identifikatsiyadan o'tganlar, rollar bo'yicha taqsimot, faollik ko'rsatkichlari |
| **E'lonlar statistikasi** | Yaratilgan, moderatsiyadan o'tgan, rad etilgan, faol e'lonlar soni; kategoriya va tuman bo'yicha |
| **So'rovlar statistikasi** | Yuborilgan, tasdiqlangan, rad etilgan, ko'rib chiqilmagan so'rovlar; konversiya darajasi |
| **To'lovlar** | Rentmi hisoboti xaridlari, summa, to'lov tizimlari bo'yicha taqsimot |
| **Skoring ko'rsatkichlari** | Hisoblangan skorlar taqsimoti (0–100), o'rtacha bal, ishonchlilik darajasi bo'yicha guruhlar |
| **Moderatsiya faoliyati** | Moderatorlar ishi: ko'rib chiqilgan e'lonlar soni, qaror vaqti, rad etish sabablari |
| **Tizim monitoring** | Uptime, xatoliklar soni, API javob vaqti, foydalanuvchilar soni dinamikasi |
| **Tashqi integratsiyalar holati** | MyID, skoring byurolari, SMS, to'lov tizimlari, FCM — real-time holat va so'rovlar statistikasi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Tashqi integratsiyalar monitoringi** | Real-time holat paneli: har bir tashqi xizmat uchun holat (Faol/Xato/Sekin), so'nggi so'rov vaqti, muvaffaqiyat darajasi |
| **Hisobot vaqti >30 s** | Foydalanuvchiga ogohlantirish; davr qisqartirilishi tavsiya qilinadi |
| **Tanlangan davr bo'yicha ma'lumot yo'q** | 'Ma'lumot topilmadi' xabari |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q / server xatosi** | Hisobot shakllantirilmaydi; xabar va Retry |
| **Eksport xatosi** | Yuklash amalga oshmaydi; xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Hisobotlar shakllantirishning maksimal davomiyligi — ≤30 s |
| **BQ-2** | Texnik qo'llab-quvvatlash xodimi faqat analitika ma'lumotlariga cheklangan (anonimlashtirilgan) kirish huquqiga ega |
| **BQ-3** | Eksport formatlari: PDF, XLSX, CSV; eksport ≤15 s ichida tayyorlanadi |
| **BQ-4** | Tashqi integratsiyalar monitoringi real-time yangilanadi |
| **BQ-5** | Har bir hisobot shakllantirish audit jurnaliga yoziladi: foydalanuvchi, hisobot turi, davr |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Hisobot sahifasi ≤5 s ichida yuklanadi |
| **AC-2** | Hisobot ≤30 s ichida shakllantiriladi va ko'rsatiladi |
| **AC-3** | Eksport fayli ≤15 s ichida yuklab olinadi |
| **AC-4** | Tashqi integratsiyalar real-time holati to'g'ri ko'rsatiladi |
| **AC-5** | Texnik qo'llab-quvvatlash xodimi shaxsiy ma'lumotlarga kira olmaydi — faqat anonimlashtirilgan statistika ko'rsatiladi |
