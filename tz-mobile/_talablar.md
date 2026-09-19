# Umumiy va funksional bo'lmagan talablar (NFR)

Use-case'larga bog'liq bo'lmagan, lekin **butun mobil ilovaga** taalluqli TZ talablari. Bu fayl "TZ'dan hech narsa qolib ketmasin" tamoyilini ta'minlaydi — quyidagilar alohida flow'larga tegishli emas, ammo har biriga qo'llaniladi.

## 1. Tezlik / javob berish vaqti (TZ §4.1.4.1, §2.2)

| Operatsiya | Talab (pik yuklama) | Kodda |
|---|---|---|
| Ekran navigatsiyasi | ≤ 3 s | — (o'lchanmagan) |
| Kirish / autentifikatsiya | ≤ 5 s | — |
| E'lonlarni qidirish/filtrlash | ≤ 5 s | page_size=5, kesh |
| Yangi e'lon yaratish | ≤ 5 s | — |
| Ariza yuborish/qabul | ≤ 3 s | — |
| Skoring xulosasini shakllantirish | ⚠ **≤5 daq (TZ jadval) / ≤2 daq (S1)** | async polling |
| Hisobot/analitika | ⚠ **≤10 s (TZ) / ≤30 s (A2)** | — |
| Tashqi integratsiya so'rovi | ≤ 15 s | — |

> ⚠ Ba'zi vaqtlar TZ ichida ziddiyatli (skoring 5daq↔2daq; hisobot 10s↔30s) — [`_konfliktlar.md`](_konfliktlar.md) A1, A2.

## 2. Bir vaqtdagi yuklama (TZ §4.1.3.1, §4.1.4)
- Bir vaqtda faol foydalanuvchilar: **1 000 – 5 000**.
- Umumiy ro'yxatdan o'tganlar (1-yil): kamida **30 000**.
- ⚠ Javob-vaqti kafolatlari faqat **1 000** da aniqlangan (5 000 uchun yo'q) — [`_konfliktlar.md`](_konfliktlar.md) A5.

## 3. Ishonchlilik (TZ §4.1.5)
- Mavjudlik ≥ **99,5%** (yillik); MTBF ≥ 2000 s; MTTR ≤ 2 s; tranzaksiya muvaffaqiyati ≥ 0,99.
- Avariyaviy: tranzaksiya rollback; tashqi tizim uzilsa retry + circuit breaker; foydalanuvchi operatsiyasi to'g'ri yakunlanadi.
- **Kodda:** `TokenManager` refresh mutex; DioClient timeout 30 s; xatolar `dartz Either` bilan; Crashlytics.

## 4. Xavfsizlik (TZ §4.1.6)
- PIN/parol bir tomonlama xesh (TZ: bcrypt/Argon2; **kod: PBKDF2-HMAC-SHA256** + salt).
- Shaxsiy ma'lumotlar shifrlangan; aloqa HTTPS/TLS 1.2+; API — JWT/OAuth2.
- 3 ta noto'g'ri urinish → 10 daqiqa blok (⚠ reliz 5/5 — [`_konfliktlar.md`](_konfliktlar.md) C2).
- OWASP Top-10 himoyasi; shaxsiy ma'lumotga kirish audit jurnalida.
- **Kodda:** secure storage (Keychain/EncryptedSharedPreferences), `AuthInterceptor`, log'da telefon/PII maskalanadi.
- ⚠ **Xavf:** Android keystore git tarixida (almashtirilishi shart); MyID prod credentials `AppConstants`da; `secrets.json` (Google key) gitignored.

## 5. Ergonomika / UI (TZ §4.1.7)
- Moslashuvchan (smartfon/planshet); sans-serif shrift ≥14pt; Material (Android) / HIG (iOS).
- Asosiy amallar ≤ 3–5 qadamda; interaktiv yordam; xato xabarlari tushunarli, tavsiya bilan.
- **Kodda:** design tokenlar (`AppColors/AppTextStyles/AppSpacing/AppRadius/...`), Figma-fidelity qoidalari (`.claude/rules/figma-fidelity.md`).

## 6. Tillar (TZ §4.3.3)
- **4 til:** o'zbek (lotin), o'zbek (kirill), rus, ingliz. Birinchi kirishda tanlanadi, keyin o'zgartiriladi.
- **Kodda:** `flutter_localizations` + `.arb` (uz, uz-Cyrl, ru, en); `LocaleProvider` (Provider); backend `Accept-Language` header (`LanguageInterceptor`).

## 7. Tashqi integratsiyalar (TZ §4.1.2)
| Xizmat | TZ | Kod |
|---|---|---|
| Identifikatsiya | REST | **MyID SDK** (`myid`) |
| Skoring/kredit byuro | REST | backend ichida (mobil `/scoring/check|status/`) |
| To'lov | REST + webhook | **Atmos, Payme, Click, Uzum** |
| SMS (OTP) | HTTP/SMPP | backend (`/auth/login/`) |
| Push | FCM/APNs | **Firebase FCM** |
| Xarita | JS/SDK | **Google Maps** + Google Geocoding |
| Valyuta kursi | REST (rejali) | `CurrencyService` (so'm/dollar toggle) |
| Elektron imzo | SDK/API (3-bosqich) | 💤 (contract) |

## 8. Boshqa (TZ §4.1.9, §4.3)
- 24/7 ishlash; texnik xizmat past-yuklama vaqtida.
- Pul summalari **tiyin** aniqligida butun son; sana/vaqt **UTC** (ISO 8601), foydalanuvchiga zonasiga moslashtiriladi.
- Backend: Python (Django/FastAPI), PostgreSQL; **mobil: Flutter/Dart** (TZ §4.3.3, §4.3.4 ga mos).
