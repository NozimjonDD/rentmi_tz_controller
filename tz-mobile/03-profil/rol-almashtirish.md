# Rol almashtirish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan (kodda) · ⚠ TZ U4 da yo'q

## TZ manbai
U4 · §4.1.1.4 — rol almashtirish **qamralmagan**. U4 bajarish tartibi shaxsiy ma'lumot tahriri, Rentmi bali, hisobot, faol qurilmalar va telefon o'zgartirish bilan cheklanadi; rolni almashtirish harakati sanab o'tilmagan. §4.1.3.2 da rollar (ijarachi/uy egasi) belgilangan, lekin ular o'rtasida almashish oqimi ta'riflanmagan.

## Reliz / R5
- **RELIZ:** rol almashtirish uchun alohida US aniqlanmagan.
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Profil sozlamalari → `role_switch_page`.
2. Foydalanuvchi mavjud rollar orasidan tanlaydi.
3. Rol o'zgargach tegishli dashboard (landlord / tenant shell) ochiladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi **WHEN** rol almashtirishni tanlaydi **THEN** rol o'zgaradi va mos dashboard ochiladi.
- **GIVEN** rol o'zgardi **WHEN** navbar yuklanadi **THEN** tanlangan rolga mos shell ko'rsatiladi — [`navigatsiya`](../00-umumiy/navigatsiya.md).

## Kod joylashuvi
- **Modul:** `lib/features/settings`
- **Sahifa / Cubit:** `role_switch_page` / — (`SettingsDataCubit` konteksti)
- **Endpoint:** aniqlanmagan.

## Konflikt / farqlar
- ⚠ **B4** — Rol almashtirish kodda mavjud (`role_switch_page`), lekin **TZ U4 da yo'q**; modul bu funksiyani va'da qilgan, TZ qamrovidan tashqarida. → [`_konfliktlar.md`](../_konfliktlar.md)
