# Skoringni hisoblash (jarayon)

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 6–9 qadam). Tizim ichki ma'lumotlarni yig'adi, tashqi manbalardan ma'lumot oladi (S2) va skoring algoritmi asosida Rentmi balini (0–100) hisoblaydi. §4.2.1/§4.3.1 — skoring moduli va matematik ta'minot.
> «Tizim foydalanuvchi bo'yicha ichki ma'lumotlarni yig'adi …; Tashqi manbalardan foydalanuvchining ma'lumotlari olinadi (S2); Tizim skoring algoritmi asosida Rentmi skoring balini (0–100) hisoblaydi.»
> Vaqt reglamenti: «hisobotni shakllantirish — ≤2 daqiqa.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6, Scenario 4` — «scoring calculation ishlayotganda foydalanuvchi ilovani yopsa yoki boshqa sahifaga o'tsa jarayon **background** rejimida davom etadi; **status widget** orqali ko'rsatiladi».
- **R5 o'zgarishi:** «R5 dagi barcha algoritmik funksionallar **qoidalarga asoslangan (rule-based) v1**; ML modellari keyingi bosqichda. Muhim biznes qarorlarga to'liq avtomatik algoritm qo'llanilmaydi (TZ §4.3.1) — faqat ko'maklashuvchi ma'lumot» `R5 · §5`.

## Bajarish tartibi
1. To'lovdan so'ng `POST /mobile/scoring/check/` `{rent_amount}` async hisoblashni boshlaydi (`rent_amount` — affordability uchun, ixtiyoriy).
2. `ScoringProcessCubit` `GET /mobile/scoring/status/` ni `Timer.periodic(1 s)` bilan polling qiladi; holatlar: `initiating → polling → completed / failed`.
3. Progress asimptotik ko'rsatiladi (`scoring_process_page`); foydalanuvchi ilovadan chiqsa jarayon backend'da davom etadi.
4. `completed` bo'lgach natija sahifasiga o'tiladi ([`04-natija-band-faktor.md`](04-natija-band-faktor.md)); push notification yuboriladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** to'lov muvaffaqiyatli **WHEN** `/scoring/check/` chaqiriladi **THEN** hisoblash async boshlanadi va status polling ishga tushadi.
- **GIVEN** hisoblash davom etyapti **WHEN** foydalanuvchi ilovani yopadi/boshqa sahifaga o'tadi **THEN** jarayon background'da davom etadi, status widget orqali kuzatiladi.
- **GIVEN** status `completed` **WHEN** natija tayyor **THEN** natija sahifasiga o'tiladi va push notification yuboriladi.

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/scoring` (oqim) + `lib/features/scoring` (data source)
- **Sahifa / BLoC:** `ScoringProcessPage` / `ScoringProcessCubit` (`Timer.periodic(1 s)` polling, asimptotik progress)
- **Endpoint:** `POST /mobile/scoring/check/` `{rent_amount}` (async); `GET /mobile/scoring/status/` (polling)

## Konflikt / farqlar
- Vaqt reglamenti (TZ ≤2 daqiqa) kodda qat'iy timeout bilan cheklanmagan — polling `completed`/`failed` gacha davom etadi. Boshqa farq aniqlanmadi.
