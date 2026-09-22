# Tizim faoliyat rejimlari (mobil kontekst)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** 🟡 Qisman

## TZ manbai
TZ §4.1.1.3 — Tizimning faoliyat rejimlari. Uchta rejim belgilanadi: **asosiy**, **texnik xizmat** va **avariyaviy**.
> «**Asosiy rejim** — barcha funksional imkoniyatlar to'liq… 24 soat, 7 kun ishlaydi.»
> «**Texnik xizmat rejimi** — rejalashtirilgan ishlar, yangilashlar va zahira nusxa olish… tizim vaqtincha cheklanishi mumkin. Foydalanuvchilar oldindan xabardor qilinadi.»
> «**Avariyaviy rejim** — komponent ishdan chiqishi natijasida… tizim foydalanuvchi ma'lumotlarini saqlab qolishni ta'minlaydi, joriy operatsiyalarni to'g'ri yakunlash imkoniyatini beradi va administratorga avtomatik bildirishnoma yuboradi.»

## Reliz / R5
- **RELIZ:** `2-1 Splash screen / US 1 SS` — «Error holatida retry imkoniyati», «Foydalanuvchiga cashda saqlangan malumotlar internetga qayt ulanguniga qadar ko'rsatilishi kerak».
- **R5 o'zgarishi:** yo'q.

## Rejimlar — mobil ilovada qanday ko'rinadi

| TZ rejimi | Mobil ilovadagi holat | Holat |
|---|---|---|
| **Asosiy** | Barcha ekranlar/funksiyalar to'liq ishlaydi (24/7) | ✅ |
| **Texnik xizmat** | Server texnik xizmatda (503/maintenance) → foydalanuvchiga xabar + retry | 🟡 aniq "maintenance" ekrani kodda yo'q, umumiy xatolik ekrani ishlaydi |
| **Avariyaviy** | Tarmoq/server uzilsa → **kesh ko'rsatiladi**, retry, joriy ma'lumot yo'qolmaydi | ✅ |

## Bajarish tartibi (mobil)
1. **Asosiy:** normal ishlash.
2. **Texnik xizmat / server uzilishi:** `DioClient` `503/502` yoki `connectionError` qaytaradi → foydalanuvchiga tushunarli xabar (`RuntimeLabels.errorNoInternet` / `serverError`) + qayta urinish.
3. **Avariyaviy / offline:** splash va sahifalar keshdan ma'lumot ko'rsatadi; internet qaytguncha kesh saqlanadi (US1); tranzaksion operatsiyalar `dartz Either` orqali xavfsiz uziladi (ma'lumot buzilmaydi); jiddiy xatolar **Firebase Crashlytics** ga yuboriladi (TZ dagi "administratorga bildirishnoma" ning mobil ekvivalenti).

## Qabul kriteriyalari (BDD)
- **GIVEN** internet yo'q **WHEN** ilova ochiladi **THEN** kesh ko'rsatiladi + banner + retry (US1 Scenario 3).
- **GIVEN** server xatosi (5xx) **WHEN** so'rov yuboriladi **THEN** tushunarli xatolik xabari + qayta urinish, joriy ma'lumot yo'qolmaydi.
- **GIVEN** kritik xatolik **WHEN** yuz beradi **THEN** Crashlytics ga yoziladi.

## Kod joylashuvi
- **Splash/error + kesh:** `lib/features/core_screens/splash` (`SplashBloc`), `00-umumiy/splash.md`.
- **Tarmoq xatolari:** `lib/core/network/dio_client.dart` (`_handleDioError` → `NetworkException`/`ServerException`), `RuntimeLabels`.
- **Crash hisoboti:** `lib/main.dart` — `FirebaseCrashlytics` (`recordFlutterFatalError`, `PlatformDispatcher.onError`).
- **Kesh/offline:** feature'lardagi `*_local_data_source` (SharedPreferences) + `cached_network_image`.

## Konflikt / farqlar
- ⚠ Kodda alohida **"texnik xizmat rejimi" ekrani** (maintenance banner) yo'q — server 5xx umumiy xatolik sifatida ko'rsatiladi. Rejalashtirilgan texnik xizmat haqida **oldindan xabar** (push/banner) mexanizmi ko'rinmaydi. → [`_konfliktlar.md`](../_konfliktlar.md) (mobil bo'shliq).
- TZ "administratorga bildirishnoma" — bu backend/admin funksiyasi; mobil tomonda ekvivalenti Crashlytics.
