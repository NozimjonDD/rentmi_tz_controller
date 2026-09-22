# PIN-kod yaratish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U1 — §4.1.1.4 (6–7 qadam). OTP tasdiqlangach, foydalanuvchi Maxfiylik siyosatiga rozilik bildiradi va PIN-kod o'rnatadi; profil saqlanadi.
> «Foydalanuvchi PIN-kod o'rnatadi; Tizim profilni saqlaydi va asosiy oynaga yo'naltiradi.»
TZ §4.1.6.2: «PIN-kodlar bir tomonlama xeshlash (bcrypt, Argon2 kabi) orqali saqlanishi.»

## Reliz / R5
- **RELIZ:** `2-4 / US 4 LA` — «PIN: **4 digit**», «PIN faqat OTPdan keyin yaratiladi», «Secure PIN storage (encrypted)», «PINdan keyin avtomatik login».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. OTP muvaffaqiyatli tasdiqlangach PIN yaratish ekrani ochiladi.
2. 4-xonali PIN kiritiladi va takroran tasdiqlanadi.
3. PIN **PBKDF2-HMAC-SHA256** bilan xeshlanib secure storage'ga saqlanadi.
4. Biometrika mavjud bo'lsa avtomatik yoqiladi.
5. `OnboardingFlowService.advance(from: pincode)` → keyingi qadam (MyID).

## Qabul kriteriyalari (BDD)
- **GIVEN** OTP tasdiqlangan **WHEN** 4-xonali PIN ikki marta kiritiladi **THEN** xesh saqlanadi va oqim davom etadi.
- **GIVEN** biometrika bor **WHEN** PIN yaratiladi **THEN** biometrik kirish avtomatik yoqiladi.

## Kod joylashuvi
- **Modul:** `lib/features/pincode` · storage `lib/core/services/pincode_storage_service.dart`
- **Sahifa / BLoC:** `PincodeCreatePage` / `PincodeBloc` (`CreatePincodeEvent`)
- **Endpoint:** yo'q — to'liq lokal/secure-storage.
- **Xesh:** `pbkdf2_sha256$<iter>$<salt-b64>$<hash-b64>` (Django uslubi), 10 000 iteratsiya, 16-baytli salt, 32-baytli kalit, constant-time solishtiruv, `Isolate.run` da (UI bloklanmaydi). Eski plaintext PIN'lar to'g'ri kiritilganda xeshga yangilanadi.

## Konflikt / farqlar
- ⚠ TZ "bcrypt/Argon2" ni misol qiladi; kodda **PBKDF2-HMAC-SHA256** — funksional jihatdan mos (bir tomonlama xesh + salt), lekin algoritm boshqacha. Muhim emas, ammo hujjatda aniqlash tavsiya etiladi.
- Farq aniqlanmadi (qolgan qismlar mos).
