# E4 — E'lonni moderatsiya qilish

**Rollar:** 🔍 Moderator    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
E4 · §4.1.1.4 · Moderator moderatsiya navbatidan e'lonni oladi va uni **tasdiqlaydi / rad etadi / tuzatishga qaytaradi**; soxta yoki qonunga zid e'lonni bloklaydi.
> «Moderator qaror qabul qiladi: tasdiqlash / rad etish / tuzatish talabi.»

## Reliz / R5
- **RELIZ / R5:** R5 da e'lonning yangi maydonlari (minimal ijara davri, minimal skoring talabi) uchun **moderatsiya ko'rinishi yangilanadi**. E4 dan muvaffaqiyatli o'tish — «Tekshirilgan» badge'ining uch shartidan biri (E4 + U5 identifikatsiya + tegishlilik). reliz admin bo'limi to'liq emas → W-K2.

## Ishga tushirish shartlari
Yangi yoki tahrirlangan e'lon **'moderatsiya kutmoqda'** holatida; moderator tizimga kirgan.

## Bajarish tartibi
1. Moderator moderatsiya navbati oynasini ochadi.
2. Tizim kutayotgan e'lonlar ro'yxatini ko'rsatadi (**eng eski avvalroq**).
3. Moderator e'lonni tanlaydi va tafsilotlarni ko'rib chiqadi (parametrlar, fotosuratlar, uy egasi ma'lumotlari).
4. Moderator qaror qabul qiladi: **tasdiqlash / rad etish / tuzatish talabi**.
5. **Tasdiqlash:** e'lon 'faol' holatga o'tadi, uy egasiga bildirishnoma yuboriladi.
6. **Rad etish:** moderator sabab kiritadi, e'lon 'rad etildi' holatga o'tadi, uy egasiga sabab bilan bildirishnoma.
7. **Tuzatish talabi:** moderator izoh kiritadi, e'lon 'tuzatish kutmoqda' holatga o'tadi.
8. Qaror audit jurnaliga yoziladi.

## Vaqt reglamenti
Navbatni yuklash — ≤3 s; qarorni saqlash — ≤2 s; uy egasiga bildirishnoma — ≤10 s; **navbatda kutishning maksimal muddati — 24 soatdan ko'p emas**.

## Qabul kriteriyalari (BDD)
- **GIVEN** 'moderatsiya kutmoqda' e'loni **WHEN** moderator tasdiqlaydi **THEN** e'lon 'faol' bo'ladi, uy egasiga bildirishnoma, qaror audit jurnalida.
- **GIVEN** qoidabuzar e'lon **WHEN** moderator rad etadi **THEN** sabab majburiy kiritiladi, e'lon 'rad etildi', uy egasiga sabab bilan xabar.
- **GIVEN** kamchiliklari bor e'lon **WHEN** moderator tuzatish talab qiladi **THEN** izoh bilan 'tuzatish kutmoqda' holatiga o'tadi.
- **GIVEN** soxta yoki qonunga zid e'lon **WHEN** moderator aniqlaydi **THEN** e'lon bloklanadi va uy egasi hisobi 'tekshiruv ostida' belgilanadi.
- **GIVEN** ayni obyekt uchun takroriy e'lon **WHEN** navbatga tushadi **THEN** avtomatik rad etiladi va sabab ko'rsatiladi.

## Backend / API (kutilayotgan)
Web kodbaza yo'q → TZ asosida taxminiy (`/admin/...`):
- `GET /admin/moderation/queue/` — kutayotgan e'lonlar (eng eski avvalroq).
- `POST /admin/moderation/listings/{id}/approve/` — tasdiqlash → 'faol'.
- `POST /admin/moderation/listings/{id}/reject/` — `{reason}` → 'rad etildi'.
- `POST /admin/moderation/listings/{id}/request-correction/` — `{comment}` → 'tuzatish kutmoqda'.
- `POST /admin/moderation/listings/{id}/block/` — soxta/qonunga zid → blok + uy egasi 'tekshiruv ostida'.
- Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- Farq aniqlanmadi — E4 ssenariysi §4.1.1.4 va modul talablari (§4.2.2) bilan izchil.
- Eslatma (modul talabi): **soxta e'lon ulushi 5% dan oshmasligi** nazorat qilinadi; rad etish/tuzatishda sabab/izoh **majburiy**.
