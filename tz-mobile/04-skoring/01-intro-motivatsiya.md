# Skoring intro / motivatsiya

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 1–3 qadam). Foydalanuvchi "Rentmi hisobotini xarid qilish"ni tanlaydi, tizim mavjud hisobot ma'lumotlari va narxlarini ko'rsatadi.
> «Foydalanuvchi profil yoki ijarachi ma'lumotlari oynasida 'Rentmi hisobotini xarid qilish'ni tanlaydi; Tizim mavjud hisobot ma'lumotlarini va narxlarini ko'rsatadi.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6` — «MyID'dan so'ng avtomatik skoring bo'limiga yo'naltiriladi; motivatsion sahifada skoring narxi, "**Ishonchli ijarachiga aylaning**" qiymat taklifi va xizmat foydalari ko'rsatiladi», «Skoring narxi **fixed**», «Guest user scoring sotib ola olmaydi».
- **R5 o'zgarishi:** yo'q (skoring hisoblash logikasi R5 §5 da rule-based v1 sifatida belgilangan; intro sahifasiga o'zgarish kiritilmagan).

## Bajarish tartibi
1. MyID VERIFIED bo'lgach ijarachi skoring intro sahifasiga o'tadi (`scoring_intro_page`).
2. Sahifada "Ishonchli ijarachiga aylaning" mazmunidagi motivatsion kontent va xizmat foydalari ko'rsatiladi.
3. Narx `ReportServiceCubit` orqali `GET /mobile/report-service/` dan olinadi (yuklanmasa fallback 49000 so'm).
4. Ruxsat/rozilik sahifasi (`scoring_permission_page`) — shaxsiy ma'lumotni qayta ishlashga rozilik.
5. "Skoring sotib olish" → to'lov sahifasiga o'tadi ([`02-tolov.md`](02-tolov.md)).

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi MyID'dan o'tgan **WHEN** identifikatsiya yakunlanadi **THEN** skoring intro sahifasi avtomatik ochiladi va narx ko'rsatiladi.
- **GIVEN** intro sahifasi ochilgan **WHEN** ekran yuklanadi **THEN** "Ishonchli ijarachiga aylaning" motivatsion kontenti ko'rsatiladi.
- **GIVEN** foydalanuvchi guest **WHEN** skoringga urinadi **THEN** xarid taqiqlanadi (avval ro'yxatdan o'tish/identifikatsiya talab qilinadi).

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/scoring` + narx `lib/features/report_service`
- **Sahifa / BLoC:** `ScoringIntroPage`, `ScoringPermissionPage` / `ReportServiceCubit`
- **Endpoint:** `GET /mobile/report-service/` (tarif; fallback 49000 so'm)

## Konflikt / farqlar
- `‘Skoringdan o'ting'` bosilganda: MyID'dan o'tgan bo'lsa xaridga, o'tmagan bo'lsa avval identifikatsiyaga yo'naltiriladi (`R3 · IJ-01 BQ-6`). Farq aniqlanmadi.
