# A4 — To'lovlarni nazorat qilish

**Rollar:** 🛡 Administrator    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
A4 · §4.1.1.4 · Administrator to'lov tranzaksiyalarini ko'radi va filtrlaydi, muammoli tranzaksiyalarni aniqlaydi, reconciliation/refund amalga oshiradi va billing hisobotini shakllantiradi.
> «Tizim barcha tranzaksiyalar ro'yxatini ko'rsatadi (sana, foydalanuvchi, tur, summa, holat, to'lov tizimi) filtr va qidiruv bilan; … zaruratga ko'ra qo'lda holatni moslashtirish yoki to'lov tizimi bilan solishtirish (reconciliation) amalga oshiriladi.»

## Reliz / R5
- **RELIZ / R5:** admin panel VueJS'da (R5 — algoritm parametrlari, SLA monitoring). Billing nazorati oqimiga o'zgarish yo'q.

## Ishga tushirish shartlari
Administrator web qismi quyi tizimiga kirgan; tizimda kamida bitta to'lov tranzaksiyasi mavjud.

## Bajarish tartibi
1. Administrator 'To'lovlar nazorati' bo'limini ochadi.
2. Tizim barcha tranzaksiyalar ro'yxatini ko'rsatadi (sana, foydalanuvchi, tur, summa, holat, to'lov tizimi) — filtr va qidiruv bilan.
3. Administrator tranzaksiyani tanlaydi va batafsil ma'lumotlarni ko'radi (to'lov tizimi javobi, webhook holati).
4. Muammoli tranzaksiyani aniqlaydi (muvaffaqiyatsiz, kutilmoqda, qaytarilishi kerak).
5. Zaruratga ko'ra **qo'lda holatni moslashtirish** yoki to'lov tizimi bilan solishtirish (**reconciliation**) amalga oshiriladi.
6. Statistik **hisobot** shakllantiriladi (kunlik/oylik tushum, muvaffaqiyat darajasi).
7. Harakatlar audit jurnaliga yoziladi.

## Vaqt reglamenti
Ro'yxatni yuklash — ≤5 s; tranzaksiya tafsilotlari — ≤3 s; hisobot shakllantirish — ≤30 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** kamida bitta tranzaksiya bor **WHEN** administrator 'To'lovlar nazorati'ni ochadi **THEN** ro'yxat filtr/qidiruv bilan ko'rsatiladi (sana, foydalanuvchi, tur, summa, holat, to'lov tizimi).
- **GIVEN** muammoli tranzaksiya **WHEN** administrator uni tanlaydi **THEN** to'lov tizimi javobi va webhook holati ko'rinadi.
- **GIVEN** to'lov tizimi bilan nomuvofiqlik **WHEN** administrator solishtiradi **THEN** reconciliation jarayoni ishga tushadi.
- **GIVEN** qaytarish (refund) talab qilinadi **WHEN** administrator buni boshlaydi **THEN** qaytarish tegishli to'lov tizimi orqali amalga oshiriladi.
- **GIVEN** kunlik/oylik davr **WHEN** hisobot so'raladi **THEN** tushum va muvaffaqiyat darajasi ≤30 s da shakllantiriladi.

## Backend / API (kutilayotgan)
- Kutiladi: `GET /admin/billing/transactions/` (filtr/qidiruv), `GET /admin/billing/transactions/{id}/` (tafsilot + webhook holati), `POST /admin/billing/transactions/{id}/reconcile/`, `POST /admin/billing/transactions/{id}/refund/`, `GET /admin/billing/reports/?period=daily|monthly`. Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Hisobot vaqti:** A4 da hisobot ≤30 s, §2.2/§4.1.4.1 da ≤10 s. → [`_konfliktlar.md`](../_konfliktlar.md) W-A1.
- ⚠ **Ssenariylar tartibi:** ro'yxatda A4 A3 dan oldin kelgan. → [`_konfliktlar.md`](../_konfliktlar.md) W-B3.
