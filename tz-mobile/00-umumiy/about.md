# 00 — Umumiy va kirish

Ilovaga birinchi kirish oqimi: splash → til tanlash → onboarding → mehmon (guest) rejimi, hamda ikki rolga umumiy navigatsiya (navbar). Bu tugun reliz **US1–US3** (R1) va R5 navbar o'zgarishlarini qamraydi; TZ da alohida use-case sifatida emas, umumiy interfeys/til talablari (§4.3.3, §4.1.7) sifatida yozilgan.

## Quyi tugunlar

| Tugun | Mazmun | TZ / Reliz | Holat |
|---|---|---|---|
| [`splash.md`](splash.md) | Splash + boshlang'ich initialization + routing | reliz US1 | ✅ |
| [`til-tanlash.md`](til-tanlash.md) | 4 til tanlash, majburiy bosqich | §4.3.3 · US2 | ✅ |
| [`onboarding.md`](onboarding.md) | 3 slayd, guest-first entry | US3 | ✅ |
| [`mehmon-rejimi.md`](mehmon-rejimi.md) | Guest imkoniyatlari (E3 ha, R1 yo'q) | §4.1.3.2 · US3 | ✅ |
| [`navigatsiya.md`](navigatsiya.md) | Ikki navbar (landlord / tenant) | reliz R5-IJ-01 | 🟡 |
| [`faoliyat-rejimlari.md`](faoliyat-rejimlari.md) | Asosiy / texnik xizmat / avariyaviy rejim (mobil) | §4.1.1.3 | 🟡 |

## Umumiy oqim (koddagi haqiqiy holat)

```
splash (/)  →  til tanlash (/language-selection)  →  onboarding (/onboarding)
     → NavigateToGuestMode (guest-first, selectedRole='tenant')
     → tenant dashboard (faqat e'lon ko'rish)
         [talab bo'yicha] → auth (rol → telefon → OTP → PIN) → rol dashboard
```

> ⚠ **Kod TZ/reliz'dan farq qiladi:** reliz US3 onboarding tugagach «ro'yxatdan o'tish yoki mehmon» tanlov ekranini, TZ U1 esa rol tanlashni birinchi qadam sifatida nazarda tutadi. Kodda onboarding skip/complete → to'g'ridan-to'g'ri **guest rejim** (`NavigateToGuestMode`, `selectedRole='tenant'`) — rol tanlash ekrani ko'rsatilmaydi. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md).

## Kod modullari

`lib/features/core_screens/splash` (`SplashBloc`) · `lib/features/core_screens/language` (`LanguageBloc`, `LocaleProvider`) · `lib/features/onboarding` (`OnboardingBloc`) · guest: `AuthGuardService.markPincodeUnlocked()` → `tenantDashboard` · navbar: `lib/features/main` (landlord) va `lib/features/tenant_dashboard` (tenant).

## Asosiy routelar / holat

| Ekran | Route | Saqlash |
|---|---|---|
| Splash | `/` | — (`AppConstants.splashDuration=2000ms`) |
| Til tanlash | `/language-selection` | `SharedPreferences` kalit `language` |
| Onboarding | `/onboarding` | `SharedPreferences` kalit `onboarding_completed` |

Backend endpoint: bu oqimda til/onboarding holati mahalliy `SharedPreferences` da saqlanadi — alohida endpoint aniqlanmagan.
