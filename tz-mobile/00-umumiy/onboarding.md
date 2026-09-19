# Onboarding

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
— (TZ da onboarding alohida use-case sifatida yo'q). §4.1.7.4 qulaylik talabi: intuitiv interfeys, tizim ichida interaktiv yo'riqnoma. Kirish oqimi (rol tanlash → ro'yxatdan o'tish) U1 doirasida. Entry flow reliz US3 da ta'riflangan.

## Reliz / R5
- **RELIZ:** `2-3 Onboarding va mehmon rejimi / US 3 OF` — «Onboardingdan o'tish majburiy emas (skip qilish mumkin)», «3–5 slaydlardan iborat bo'lgan formatda», «Content: Rentmi platformasi va ijara tarixi nima, skoring nima, ijara so'rovi nima», «Tugagach ro'yxatdan o'tish yoki mexmon sifatida davom etish ekrani ochiladi».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Til tanlangach onboarding ochiladi (`/onboarding`), **3 slayd** (swipe qilinadigan karusel).
2. Foydalanuvchi 'O'tkazib yuborish' (skip) yoki oxirgi slaydda 'Davom etish' ni bosadi.
3. Kodda ikkala yo'l ham → `NavigateToGuestMode` (guest-first, `selectedRole='tenant'`).
4. `SharedPreferences` (`onboarding_completed=true`) — keyingi ochilishda onboarding o'tkazib yuboriladi.
5. Foydalanuvchi guest sifatida tenant dashboardga tushadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** oxirgi slayd **WHEN** foydalanuvchi 'Davom etish' ni bosadi **THEN** kodda guest rejimga o'tadi (reliz: ro'yxatdan o'tish/mehmon tanlovi).
- **GIVEN** onboarding **WHEN** foydalanuvchi skip qiladi **THEN** kodda guest rejimga o'tadi.
- **GIVEN** onboarding avval yakunlangan **WHEN** ilova qayta ochiladi **THEN** onboarding ko'rsatilmaydi (`onboarding_completed`).

## Kod joylashuvi
- **Modul:** `lib/features/onboarding`
- **Sahifa / BLoC:** onboarding page (3 slayd) / `OnboardingBloc` (`NavigateToGuestMode`)
- **Route:** `/onboarding`
- **Saqlash:** `SharedPreferences` kalit `onboarding_completed`
- **Endpoint:** yo'q (mahalliy).

## Konflikt / farqlar
- ⚠ **Guest-first oqim:** kodda onboarding skip/complete → to'g'ridan-to'g'ri **guest rejim** (`NavigateToGuestMode`, `selectedRole='tenant'`), **rol tanlashga o'tmaydi**. TZ U1 «rol tanlash birinchi» ni, reliz US3 «ro'yxatdan o'tish yoki mehmon» tanlov ekranini nazarda tutadi. → [`_konfliktlar.md`](../_konfliktlar.md)
- ⚠ Slaydlar soni: reliz «3–5», kodda **3**.
