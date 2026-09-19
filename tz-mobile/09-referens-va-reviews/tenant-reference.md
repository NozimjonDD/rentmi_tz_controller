# Ijarachi referensi (tenant reference)

**Rollar:** 🏠 Uy egasi    **Holat:** 🟡 Qisman (lug'atlar `/admin/` sabab degrade bo'lishi mumkin)

## TZ manbai
TZ da alohida use-case sifatida yo'q. Ishonch/ijara tarixi ma'lumotlarini to'plash g'oyasi S1 (skoring) va uy egasi profili konteksti bilan bog'lanadi — uy egasi o'z ijarachisi haqida strukturalangan referens qoldiradi.
> «(S1, 15-qadam) ... tavsiyanoma qo'shish funksionali ochiladi.» — referens shu ishonch mexanizmlarining uy egasi tomoni.

## Reliz / R5
- **RELIZ:** referens deeplink orqali ochiladi (`/reference/create?tenant_id=`); 3 qadamli wizard — (1) asosiy ma'lumot, (2) muammolar/zarar (lug'atlar + foto), (3) tavsiya. Zarar fotolari multipart yuklanadi.
- **R5 o'zgarishi:** yo'q (R5 uy egasi ommaviy profili va "Tekshirilgan" badge'iga urg'u beradi; referensning o'zini o'zgartirmaydi).

## Bajarish tartibi
1. Uy egasi deeplink (`/reference/create`) orqali `tenant_id` bilan wizardni ochadi (`TenantReferenceWizardPage`, `kReferenceWizardStepCount = 3`).
2. Lug'atlar yuklanadi: `GET /admin/user/damage-type/list/`, `/complaint-type/list/`, `/contract-breach-type/list/`. Xatolikda (401/403) repository ularni bo'sh bundle'ga yutadi — wizard text-only rejimda davom etadi.
3. **1-qadam** asosiy ma'lumot (ijara davri, oylik to'lov); **2-qadam** muammolar/shikoyat/shartnoma buzilishi turlari + zarar fotolari `POST /admin/user/damage-photo/create/` (multipart `photo`); **3-qadam** yakuniy tavsiya.
4. Yuborish: `POST /mobile/reference/create/?tenant_id=` (JSON body — `TenantReferenceCubit` yig'adi) → `TenantReferenceSuccessPage`.

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi `tenant_id` deeplink orqali kirdi **WHEN** wizard ochiladi **THEN** 3 qadam (1/3 … 3/3) navigatsiyasi ko'rsatiladi.
- **GIVEN** lug'at endpointlari 401/403 qaytardi **WHEN** wizard yuklanadi **THEN** ilova qulamaydi — text-only rejimga tushadi.
- **GIVEN** barcha majburiy maydonlar to'ldirildi **WHEN** yuborish bosiladi **THEN** `POST /mobile/reference/create/?tenant_id=` chaqiriladi va muvaffaqiyat sahifasi ko'rsatiladi.

## Kod joylashuvi
- **Modul:** `lib/features/tenant_reference`
- **Sahifa / BLoC:** `TenantReferenceWizardPage` + `StepBasicInfoPage`/`StepIssuesPage`/`StepRecommendationPage` / `TenantReferenceCubit`; entitilar `TenantReference`, `DamagePhoto`, `ReferenceLookup`, `ReferenceUserType`; deeplink `lib/core/deeplink/deeplink_target.dart` (`routeName = '/reference/create'`)
- **Endpoint:** `POST /mobile/reference/create/` `?tenant_id=`; ⚠ `POST /admin/user/damage-photo/create/`; ⚠ `GET /admin/user/{damage-type|complaint-type|contract-breach-type}/list/`

## Konflikt / farqlar
- ⚠ **`/admin/` namespace:** lookup va damage-photo endpointlari `/admin/user/...` ostida — bu CLAUDE.md qoidasiga zid («all data sources call `/mobile/` … never `/admin/`», Phase 3 standarti). damage-photo backend `c0e58a6` da `AllowAny` qilingan, lekin lug'atlar `IsAdmin` sabab 401/403 bo'lishi mumkin. → [`_konfliktlar.md`](../_konfliktlar.md) B9.
- ⚠ TZ da referens alohida use-case emas — ishonch mexanizmi sifatida reliz/kod qo'shган. → B11.
