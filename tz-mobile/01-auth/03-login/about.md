# 03 — Kirish (Login, PIN)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U2 — Tizimga kirish (mobil ilova, PIN) · §4.1.1.4. Ro'yxatdan o'tgan foydalanuvchi telefon raqami + PIN orqali kiradi.
> «Telefon raqamini kiritadi → Tizim raqam va hisob holatini tekshiradi → PIN-kodni kiritadi → Tizim PIN-ni saqlangan xesh bilan taqqoslaydi → sessiya va autentifikatsiya tokeni yaratiladi → rolga mos asosiy oynaga yo'naltiriladi.»

## Reliz / R5
- **RELIZ:** `2-4 / US 4 LA` — «PINdan keyin avtomatik login», «JWT + refresh token», «Multi-device login mavjud». `AD-05`: «Bloklangan foydalanuvchi tizimga kira olmaydi».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Foydalanuvchi 'Tizimga kirish'ni tanlaydi, telefon raqamini kiritadi.
2. Tizim raqam va hisob holatini tekshiradi.
3. PIN kiritiladi → saqlangan xesh bilan taqqoslanadi.
4. Noto'g'ri PIN: urinishlar hisoblagichi oshadi (3 → 10 daq blok).
5. To'g'ri PIN: sessiya + JWT yaratiladi, audit yoziladi.
6. Rolga mos asosiy oynaga yo'naltiriladi.

## Vaqt reglamenti (TZ)
Umumiy ≤5 s · PIN tekshirish ≤2 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** ro'yxatdan o'tgan foydalanuvchi **WHEN** to'g'ri PIN kiritadi **THEN** JWT sessiya yaratiladi va rol dashboard'ga o'tadi.
- **GIVEN** 3 marta noto'g'ri PIN **WHEN** yana urinsa **THEN** hisob 10 daqiqaga bloklanadi, U3 (PIN tiklash) taklif qilinadi.
- **GIVEN** raqam topilmadi **WHEN** kirishga urinsa **THEN** U1 (ro'yxatdan o'tish) ga yo'naltiriladi.

## Kod joylashuvi
- **Modul:** `lib/features/auth` + `lib/features/pincode`
- **Sahifa / BLoC:** `PincodeVerifyPage` / `PincodeBloc` (`VerifyPincodeEvent`, states `PincodeVerifying(firstPincode, attemptsLeft)`, `PincodeError(message, attemptsLeft)`)
- **Endpoint:** kirish PIN mahalliy tekshiriladi; token amal qilishi `POST /auth/token/refresh/` orqali; qayta OTP kerak bo'lsa `/auth/login/`.

## Konflikt / farqlar
- ⚠ TZ da U2 "telefon + PIN" alohida oqim; kodda kirish ko'p hollarda **splash → PIN gate** orqali (token mavjud bo'lsa) amalga oshadi, telefon qayta kiritilmaydi. Guest-first tufayli farq. → [`_konfliktlar.md`](../../_konfliktlar.md).
