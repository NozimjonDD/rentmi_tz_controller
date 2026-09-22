# R5-AD-02 — SLA monitoring

**Rollar:** 🛡 Administrator    **Holat:** spec (web kod yo'q)    **Manba:** Release 5 (R5-AD-02)

## User Story
Administrator sifatida men muddati o'tgan so'rovlar va uy egalarining javob berish intizomini kuzatishni xohlayman, shunda platforma xizmat sifatini nazorat qila olaman.

## Tavsif
So'rovlar monitoring bo'limiga SLA ko'rinishi qo'shiladi (R3 moduli kengaytmasi):
- **"Ko'rib chiqilmagan" (muddati o'tgan) so'rovlar ro'yxati** — ijarachi, uy egasi, e'lon, o'tgan vaqt
- **Uy egasi kesimida o'rtacha/mediana javob vaqti** hisoboti
- Davr bo'yicha filtrlash va eksport

> **Bog'liqlik:** bu monitoring **mobil** tarafdagi so'rovlar SLA'sini (R5-UE-02 countdown, first_response_time) kuzatadi.

## Qabul mezonlari (BDD)
- **GIVEN** muddati o'tgan so'rovlar mavjud **WHEN** SLA monitoring ochilsa **THEN** ro'yxat sana bo'yicha (eng eskisi birinchi) ko'rinadi
- **GIVEN** davr filtri qo'llandi **WHEN** hisobot yuklansa **THEN** faqat tanlangan davr so'rovlari va statistikasi ko'rinadi
- **GIVEN** uy egasi kesimi ochildi **WHEN** hisobot yuklansa **THEN** har uy egasi bo'yicha so'rovlar soni, javob berilganlar ulushi va mediana javob vaqti ko'rinadi
- **GIVEN** ro'yxat ko'rsatilgan **WHEN** so'rov satri bosilsa **THEN** so'rov tafsilotlari sahifasi (readonly) ochiladi

## Backend / API (kutilayotgan)
Web kodbaza yo'q → taxminiy: `GET /admin/monitoring/sla/` (filtr: davr, uy egasi). Aniq yo'l web repo berilganda tasdiqlanadi (W-K1).

## Konflikt / farqlar
- Farq aniqlanmadi.
