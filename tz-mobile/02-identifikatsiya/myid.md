# MyID SDK identifikatsiya

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U5 — Foydalanuvchini identifikatsiya qilish · §4.1.1.4 (U5). Tashqi davlat identifikatsiya xizmati (MyID yoki shunga o'xshash) orqali shaxs tasdiqlanadi; tizim ma'lumotlar to'g'riligi va to'liqligini tekshiradi, profil "identifikatsiyadan o'tgan" deb belgilanadi.
> «Tizim tashqi xizmat bilan integratsiyani ishga tushiradi; Foydalanuvchi tashqi xizmat interfeysiga yo'naltiriladi (OAuth 2.0); … Tashqi xizmat foydalanuvchi ma'lumotlarini (ism, JShShIR, pasport, tug'ilgan sana) qaytaradi.»
> «Shaxs bazada mavjud bo'lsa → mavjud hisob haqida xabar va kirish (U2) taklif qilinadi (yangi hisob yaratilmaydi).»

## Reliz / R5
- **RELIZ:** `2-5 MyID identifikatsiya / US 5 MyID: Identifikatsa` — «MyID jarayoni login dan keyin **avtomatik** boshlanadi», «SDK ilova ichida (**embedded**) ishlaydi», «PINFL, pasport va selfi ma'lumotlari olinadi», «Natija: **VERIFIED / REJECTED / ERROR**», «Qayta urinish cheklovi: **3 marta**», «Kamera ruxsati talab qilinadi», «Muvaffaqiyatli → ijarachi skoringga, uy egasi mulk import sahifasiga».
- **R5 o'zgarishi:** «Uy egasining davlat bazasidan mulklar ro'yxatini yuklash integratsiyasi ishlashi — "Tekshirilgan" va tegishlilik shunga tayanadi» `R5`. Batafsil: [`kadastr-import.md`](kadastr-import.md).

## Bajarish tartibi
1. `IdentificationCubit.getSessionId()` → `GET /mobile/identification/session/` sessiya identifikatorini qaytaradi.
2. `MyIdConfig(sessionId, clientHash, clientHashId, PRODUCTION, IDENTIFICATION, UZBEK, CIRCLE)` bilan `myid` SDK ilova ichida ishga tushadi (kamera ruxsati so'raladi).
3. Foydalanuvchi PINFL, pasport va selfi orqali identifikatsiyadan o'tadi; SDK `{code, base64}` qaytaradi.
4. `submitIdentification` → `POST /mobile/identification/` ma'lumotni backendga yuboradi; holat aniqlanadi: **VERIFIED / REJECTED / ERROR**.
5. VERIFIED → rolga qarab yo'naltirish: ijarachi → skoring intro (04); uy egasi → kadastr import.
6. REJECTED/ERROR → qayta urinish (jami ≤3 marta). Legacy oqim: `POST /mobile/identification/legacy/`.

## Qabul kriteriyalari (BDD)
- **GIVEN** login yakunlangan **WHEN** MyID ekrani ochiladi **THEN** kamera ruxsati so'raladi va SDK identifikatsiyani boshlaydi.
- **GIVEN** SDK `VERIFIED` qaytardi **WHEN** ma'lumot saqlanadi **THEN** foydalanuvchi rolga qarab skoring yoki mulk import sahifasiga o'tadi.
- **GIVEN** SDK `REJECTED`/`ERROR` qaytardi **WHEN** urinishlar soni ≤3 **THEN** qayta urinish taklif qilinadi; 3 martadan so'ng vaqtinchalik cheklov.
- **GIVEN** kamera ruxsati berilmagan **WHEN** jarayon boshlanadi **THEN** ruxsat so'raladi, ruxsatsiz jarayon davom etmaydi.

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/identification` (sahifa) + `lib/features/settings` (Cubit va data source) · SDK: `myid` paketi
- **Sahifa / BLoC:** `IdentificationPage` / `IdentificationCubit` (`getSessionId()`, `submitIdentification`)
- **Endpoint:** `GET /mobile/identification/session/` → `sessionId`; `POST /mobile/identification/` `{code, base64}` → status; legacy `POST /mobile/identification/legacy/`
- **Statuslar:** `VERIFIED` / `REJECTED` / `ERROR`; qayta urinish ≤3 marta.
- **Xatolar:** MyID `PlatformException.code` → Crashlytics: `101` bekor qilish, `102` kamera, `103` yuz (face), `104` timeout, `105` tarmoq (network).
- Credentials: `AppConstants.myIdClientHash`, `AppConstants.myIdClientHashId`.

## Konflikt / farqlar
- ⚠ **Integratsiya usuli:** TZ (U5, 2-qadam) — tashqi interfeysga **OAuth 2.0** redirect ↔ kod — **embedded MyID SDK** (brauzer redirect yo'q). → [`_konfliktlar.md`](../_konfliktlar.md).
- ⚠ **Vaqt reglamenti:** TZ tashqi xizmatga so'rov ≤5 s, umumiy ≤60 s belgilaydi; kodda alohida timeout metrikasi yo'q (SDK `104 timeout` xatosi orqali boshqariladi). → [`_konfliktlar.md`](../_konfliktlar.md).
