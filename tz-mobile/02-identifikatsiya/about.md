# 02 — Identifikatsiya (MyID)

Foydalanuvchi shaxsini tashqi davlat identifikatsiya xizmati (**MyID SDK**) orqali tasdiqlash: PINFL, pasport ma'lumotlari va selfi. TZ use-case: **U5** (foydalanuvchini identifikatsiya qilish, U1 tarkibida). Muvaffaqiyatli identifikatsiyadan so'ng ijarachi skoringga (04), uy egasi esa ko'chmas mulklarini import qilishga yo'naltiriladi.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`myid.md`](myid.md) | MyID SDK oqimi (embedded), statuslar, qayta urinish, xatolar | U5 | ✅ |
| [`kadastr-import.md`](kadastr-import.md) | Uy egasi ko'chmas mulklarini davlat bazasidan import (U5 9-qadam) | U5 | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
login (PIN) → MyID identifikatsiya (SDK, ilova ichida / embedded)
   getSessionId → MyIdConfig → SDK {code, base64} → submitIdentification
   VERIFIED → 👤 ijarachi  → skoring intro (04)
            → 🏠 uy egasi  → kadastr import (mulklar ro'yxati) → uy egasi dashboard
   REJECTED / ERROR → qayta urinish (≤3 marta); MyID xatolari → Crashlytics
```

> ⚠ **Kod TZ'dan farq qiladi:** TZ (U5, 2-qadam) foydalanuvchini tashqi xizmat interfeysiga **OAuth 2.0** orqali yo'naltirishni nazarda tutadi. Kodda esa MyID **ilova ichida (embedded SDK)** ishlaydi — brauzer/OAuth redirect yo'q, `myid` paketi to'g'ridan-to'g'ri kamera + selfi oqimini boshqaradi. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md).

## Kod modullari

Sahifa `lib/features/core_screens/identification/pages/identification_page.dart` · Cubit `IdentificationCubit` (`lib/features/settings/presentation/bloc/identification_cubit.dart`, data source `lib/features/settings/data/datasources/settings_remote_data_source.dart`) · uy egasi importi `lib/features/property_import` + sahifa `lib/features/core_screens/landlord_onboarding/landlord_cadastre_onboarding_page.dart` · SDK `myid` paketi · credentials `AppConstants.myIdClientHash` / `AppConstants.myIdClientHashId`.

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Sessiya olish | `GET /mobile/identification/session/` → `sessionId` |
| Identifikatsiya yuborish | `POST /mobile/identification/` — SDK `{code, base64}` → status |
| Legacy identifikatsiya | `POST /mobile/identification/legacy/` |
| Uy egasi mulklari — preview | `GET /mobile/homeowner-properties/import/preview/` |
| Uy egasi mulklari — import | `POST /mobile/homeowner-properties/import/create/` — `{selected_objects}` |
