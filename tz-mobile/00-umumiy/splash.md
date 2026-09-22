# Splash screen + boshlang'ich initialization

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
— (TZ da splash alohida use-case sifatida yo'q). Umumiy grafik interfeys talabi §4.1.7.3: interfeys foydalanuvchiga joriy holat va keyingi harakatlar to'g'risida aniq ma'lumot berishi lozim. Boshlang'ich yuklash + routing reliz US1 da ta'riflangan.

## Reliz / R5
- **RELIZ:** `2-1 Splash screen / US 1 SS` — «Splash screen har doim ilova ochilganda ko'rsatiladi», «Routing faqat initialization tugagandan keyin amalga oshiriladi», «Foydalanuvchi splash screenni skip qila olmaydi», «Error holatida retry imkoniyati bo'lishi kerak». Routing: yangi user → onboarding; login bo'lgan user → Pincode → home; xatolik → kesh → error ekran.
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Ilova ochiladi → splash (logo) ko'rsatiladi (`AppConstants.splashDuration=2000ms`).
2. Fonda `SplashBloc` bootstrap: token refresh, foydalanuvchi sessiyasi holati, konfiguratsiya.
3. Routing qarori: token yo'q → onboarding/guest; aktiv token → PIN gate → asosiy sahifa.
4. FCM pending-nav replay: push orqali kutilayotgan navigatsiya qayta ijro etiladi.
5. Xatolik (tarmoq/server) → error ekran + retry, keshdagi ma'lumot ko'rsatiladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi autentifikatsiyadan o'tmagan **WHEN** initialization tugaydi **THEN** onboarding/guest oqimiga yo'naltiriladi.
- **GIVEN** aktiv token **WHEN** splash tugaydi **THEN** PIN so'raladi, to'g'ri PIN'dan keyin asosiy sahifa.
- **GIVEN** tarmoq yoki server xatosi **WHEN** initialization **THEN** error ekran + retry; keshdagi ma'lumot ko'rsatiladi.
- **GIVEN** splash ishlamoqda **WHEN** initialization davom etadi **THEN** foydalanuvchi splashni o'tkazib yubora olmaydi.

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/splash`
- **Sahifa / BLoC:** splash page / `SplashBloc` (bootstrap: token refresh, routing decision, FCM pending-nav replay)
- **Route:** `/`
- **Endpoint:** token refresh `POST /auth/token/refresh/` (sessiya) — [`01-auth/05-sessiya`](../01-auth/05-sessiya/about.md); splash uchun alohida endpoint yo'q.

## Konflikt / farqlar
- Farq aniqlanmadi. Reliz US1 va kod (`SplashBloc`) mos: initialization → routing → PIN/onboarding/error.
