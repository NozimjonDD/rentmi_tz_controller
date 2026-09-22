# Rol tanlash

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** 🟡 Qisman

## TZ manbai
TZ da alohida use-case yo'q — rol U1 (ro'yxatdan o'tkazish) ning **kiruvchi ma'lumoti** sifatida keladi (`rol`). §4.1.3.2 da rollar ta'riflangan: Ijarachi, Uy egasi, Mehmon (guest) va boshqalar. §4.2.1 (Foydalanuvchi moduli) "Rol (ijarachi/uy egasi) tanlash va o'zgartirish" ni funksiya deb sanaydi.

## Reliz / R5
- **RELIZ:** `2-4 Ro'yxatdan o'tish / US 4 LA` — «Role: uy egasi / ijarachi / guest», «Role change settings orqali mumkin».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Foydalanuvchi rol tanlash ekranini ochadi.
2. Rolni tanlaydi: **uy egasi / ijarachi / mehmon**.
3. Rol ilova xotirasida vaqtinchalik saqlanadi (`selectedRole`).
4. Agar access token allaqachon bo'lsa → PIN tekshirishga; aks holda → login (telefon) ga o'tadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi rol ekranida **WHEN** rolni tanlaydi **THEN** rol lokal saqlanadi.
- **GIVEN** mehmon tanlanadi **WHEN** davom etsa **THEN** cheklangan ijarachi rejimida asosiy sahifaga o'tadi (so'rov yuborib bo'lmaydi).

## Kod joylashuvi
- **Modul:** `lib/features/role_selection`
- **Sahifa / BLoC:** `RoleSelectionPage` / `RoleSelectionBloc` (`RoleSelectedEvent`, `ContinueButtonPressedEvent`)
- **Endpoint:** yo'q — rol faqat lokal (`SharedPreferences: selectedRole`, `homeowner`↔`landlord` normalizatsiya).

## Konflikt / farqlar
- ⚠ **"Mehmon" — rol emas.** Kodda `enum UserRole { landlord('homeowner'), tenant('tenant') }` — guest qiymati yo'q; "mehmon rejimi" = `AuthGuardService.markPincodeUnlocked()` + tenant dashboard'ga o'tish (backend roli emas). TZ da esa Mehmon alohida rol sifatida ta'riflangan.
- ⚠ **Rol o'zgartirish** §4.2.1 da va'da qilingan, lekin U4 use-case'da qamralmagan (foydalanuvchi o'zi orqali). Kodda `settings/role-switch` bor. → [`_konfliktlar.md`](../../_konfliktlar.md) B4.
