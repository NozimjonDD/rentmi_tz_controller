# A2 — Tizim hisobotlarini shakllantirish

**Rollar:** 🛡 Administrator / 🛠 Support    **Holat:** 🟡 (qisman — ziddiyatli talablar: W-A1, W-A4)

## TZ manbai
A2 · §4.1.1.4 · Administrator yoki texnik qo'llab-quvvatlash xodimi turli **hisobot turlarini** shakllantiradi va **PDF/XLSX/CSV** ko'rinishida yuklab oladi; integratsiya monitoringi real vaqtda.
> «Tizim hisobot turlarini ko'rsatadi: foydalanuvchilar, e'lonlar, so'rovlar, to'lovlar, skoring, moderatsiya faoliyati, tizim monitoring, tashqi integratsiyalar holati.»

## Reliz / R5
- **RELIZ / R5:** R5 da **SLA monitoring** (R5-AD-02) qo'shildi — muddati o'tgan (ko'rib chiqilmagan) so'rovlar ro'yxati/statistikasi va uy egasi kesimida o'rtacha javob vaqti hisoboti; A2 hisobot turlariga yaqin. reliz admin bo'limi to'liq emas → W-K2.

## Ishga tushirish shartlari
Foydalanuvchi tizimga kirgan va **administrator yoki texnik qo'llab-quvvatlash** roliga ega; hisobot uchun yetarli ma'lumotlar mavjud.

## Bajarish tartibi
1. Foydalanuvchi 'Hisobotlar va analitika' bo'limini ochadi.
2. Tizim hisobot turlarini ko'rsatadi: **foydalanuvchilar, e'lonlar, so'rovlar, to'lovlar, skoring, moderatsiya faoliyati, tizim monitoring, tashqi integratsiyalar holati**.
3. Foydalanuvchi hisobot turi va parametrlarni (davr, filtrlar) tanlaydi.
4. Tizim hisobotni ma'lumotlar bazasidan yig'adi va **jadval/grafik** ko'rinishida ko'rsatadi.
5. **Integratsiya monitoringi** rejimida: tashqi xizmatlar holati **real vaqtda** ko'rsatiladi.
6. **PDF, XLSX yoki CSV** formatida yuklab olish mumkin.
7. Audit jurnaliga yozuv kiritiladi.

## Vaqt reglamenti
Hisobot sahifasini yuklash — ≤5 s; **hisobot shakllantirish — ≤30 s** (⚠ §2.2/§4.1.4.1 da ≤10 s — W-A1); eksport faylini tayyorlash — ≤15 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** administrator/support 'Hisobotlar va analitika'da **WHEN** hisobot turi va davrni tanlaydi **THEN** tizim jadval/grafik shakllantiradi, audit yozuvi kiritiladi.
- **GIVEN** shakllantirilgan hisobot **WHEN** foydalanuvchi eksport qiladi **THEN** PDF/XLSX/CSV fayli tayyorlanadi (≤15 s).
- **GIVEN** integratsiya monitoringi rejimi **WHEN** ochiladi **THEN** tashqi xizmatlar holati real vaqtda ko'rsatiladi.
- **GIVEN** hisobot vaqti chegaradan oshadi **WHEN** shakllantirish davom etadi **THEN** ogohlantirish va davrni kamaytirish taklifi.
- **GIVEN** tanlangan davrda ma'lumot yo'q **WHEN** hisobot so'raladi **THEN** 'ma'lumot topilmadi' xabari.

## Backend / API (kutilayotgan)
Web kodbaza yo'q → TZ asosida taxminiy (`/admin/...`):
- `GET /admin/reports/` — hisobot turlari ro'yxati.
- `POST /admin/reports/generate/` — `{type, period, filters}` → jadval/grafik.
- `GET /admin/reports/{id}/export/?format=pdf|xlsx|csv` — eksport.
- `GET /admin/monitoring/integrations/` — tashqi xizmatlar holati (real vaqtda).
- Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Hisobot vaqti:** A2 da **≤30 s**, biroq §2.2 va §4.1.4.1 da **≤10 s** — qaysi biri birlamchi ekani noaniq. → [`_konfliktlar.md`](../_konfliktlar.md) W-A1.
- ⚠ **Support doirasi:** A2 support'ga «foydalanuvchilar, to'lovlar, skoring» (shaxsiy/moliyaviy) hisobotlarini ochadi, §4.1.3.2 esa support'ni **«anonimlashtirilgan analitikaga cheklangan kirish»** bilan chegaralaydi. → [`_konfliktlar.md`](../_konfliktlar.md) W-A4.
