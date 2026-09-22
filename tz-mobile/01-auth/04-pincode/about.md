# 04 — PIN-kod (yaratish / tekshirish / tiklash / biometrika)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

PIN gate — mobil autentifikatsiyaning asosiy mexanizmi. Yaratish [`02-register/pin-yaratish.md`](../02-register/pin-yaratish.md) da; bu yerda tekshirish, tiklash (U3) va biometrika.

## TZ manbai
- **U2** — PIN tekshirish (kirishda).
- **U3** — PIN-kodni tiklash · §4.1.1.4.
> U3: «'PIN-kodni unutdim' → telefon → SMS OTP → yangi PIN ikki marta → eski PIN bekor qilinadi → audit + bildirishnoma → avtomatik kirish.»
- **§4.1.6.2** — 3 ta noto'g'ri urinish → 10 daqiqa blok.

## Reliz / R5
- **RELIZ:** `2-4 / US 4 LA` — «Secure PIN storage», «OTP attempt limit: 5». `AD-A1`: «Foydalanuvchiga PIN tiklash SMS yuboriladi; foydalanuvchi yangi PIN o'rnatadi» (admin tomonidan majburiy tiklash).
- **R5 o'zgarishi:** yo'q.

## PIN tekshirish (U2)
- Kiritilgan PIN saqlangan xesh bilan constant-time taqqoslanadi.
- **Brute-force blok:** 3 urinish → 10 daqiqa blok; blok **persistent** (`pincode_failed_attempts`, `pincode_lockout_until`) — ilova o'chirilsa ham saqlanadi. Blok davomida biometrika ham bloklanadi.

## PIN tiklash (U3)
1. 'PIN-kodni unutdim' → telefon raqami.
2. SMS OTP (§ TZ: 5 daqiqa; total ≤60 s).
3. Yangi PIN ikki marta kiritiladi (eski bilan bir xil bo'lmasligi kerak).
4. Yangi xesh saqlanadi, eski bekor qilinadi, audit + bildirishnoma, avtomatik kirish.

## Biometrika
- `local_auth` (`BiometricService`) orqali; PIN yaratishda avtomatik yoqiladi (mavjud bo'lsa); tekshirish sahifasida avtomatik so'raladi (blok bo'lmasa).

## Qabul kriteriyalari (BDD)
- **GIVEN** 3 marta noto'g'ri PIN **WHEN** yana urinsa **THEN** 10 daqiqa blok, biometrika ham bloklanadi.
- **GIVEN** PIN unutildi **WHEN** OTP tasdiqlanadi **THEN** yangi PIN o'rnatiladi, avtomatik kiriladi.
- **GIVEN** yangi PIN eski bilan bir xil **WHEN** kiritiladi **THEN** rad etiladi.

## Kod joylashuvi
- **Modul:** `lib/features/pincode` · `lib/core/services/pincode_storage_service.dart`, `biometric_service.dart`
- **Sahifa / BLoC:** `PincodeCreatePage`, `PincodeVerifyPage` / `PincodeBloc` (`CreatePincodeEvent`, `VerifyPincodeEvent`, `ResetPincodeEvent`, `AuthenticateWithBiometricEvent`)
- **Storage:** `FlutterSecureStorage` (Android `encryptedSharedPreferences`, iOS Keychain `first_unlock`), kalit `user_pincode`.
- **Endpoint:** tiklashda OTP `POST /auth/login/`; PIN'ning o'zi lokal.

## Konflikt / farqlar
- ⚠ **Urinish/blok:** TZ **3 → 10 daq** ↔ reliz **5 → 5 daq**. Kodda PIN uchun **3 → 10 daq** (TZ ga mos), lekin OTP uchun reliz qiymatlari. → [`_konfliktlar.md`](../../_konfliktlar.md) C2.
