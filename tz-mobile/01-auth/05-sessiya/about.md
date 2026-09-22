# 05 — Sessiya (JWT, refresh, multi-device, sessiya tugashi)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
- U2 — «sessiya va autentifikatsiya tokeni yaratiladi».
- §4.1.6.1 — «har bir foydalanuvchi sessiyasi… web qismida faoliyatsizlik davrida (15 daqiqa) avtomatik yakunlanadi» (mobil uchun PIN + JWT).
- §4.1.6.2 — «API so'rovlari autentifikatsiya tokenlari (JWT, OAuth 2.0) orqali himoyalanishi».
- U4 — «faol qurilmalarni ko'rish va boshqarish» (multi-device).

## Reliz / R5
- **RELIZ:** `2-4 / US 4 LA` — «JWT + refresh token», «Multi-device login mavjud», «Stable session management».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi (kod)
1. `login/confirm/` → `{access, refresh}` secure storage'ga saqlanadi.
2. Har so'rovga `Authorization: Bearer <access>` qo'shiladi (`AuthInterceptor`).
3. 401 → `TokenManager.refreshToken()` (`POST /auth/token/refresh/`) → so'rov qayta yuboriladi.
4. Refresh muvaffaqiyatsiz (refresh token muddati tugagan) → tokenlar tozalanadi → `SessionExpiredHandler.handle()` → login ekraniga.
5. Token refresh: splash'da bir marta + ilova >5 daqiqa fon'dan qaytganda + 401 da.
6. Multi-device: har login'da `device_id` + FCM ro'yxatdan o'tadi (`POST /mobile/device/register/`).

## Qabul kriteriyalari (BDD)
- **GIVEN** access token muddati tugagan **WHEN** so'rov 401 qaytaradi **THEN** avtomatik refresh + qayta urinish.
- **GIVEN** refresh token ham muddati tugagan **WHEN** 401 **THEN** sessiya tugaydi, login'ga.
- **GIVEN** bir nechta qurilma **WHEN** login qilinadi **THEN** har biri saqlanadi (U4 da boshqariladi).

## Kod joylashuvi
- **Modul:** `lib/core/services/token_manager.dart`, `token_storage_service.dart`, `session_expired_handler.dart`; `lib/core/network/interceptors/auth_interceptor.dart`
- **Endpoint:** `POST /auth/token/refresh/` `{refresh}` → `{access, refresh}`; `POST /mobile/device/register/`
- **Xususiyat:** refresh **Completer mutex** bilan (parallel refresh yo'q); token secure storage'da; splash eski SharedPreferences tokenlarni secure storage'ga migratsiya qiladi.

## Konflikt / farqlar
- ⚠ TZ §4.1.6.1 faoliyatsizlik timeout'ini **web** uchun 15 daqiqa deb belgilaydi; mobil uchun aniq timeout yo'q — kodda mobil PIN gate + JWT refresh bilan boshqariladi. Farq kritik emas.
- Faol qurilmalarni ko'rish/boshqarish U4 (profil) da — [`03-profil/`](../../03-profil/about.md).
