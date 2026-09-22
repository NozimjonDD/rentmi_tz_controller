# Rol bo'yicha keyingi qadam (post-register flow)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U1 (9-qadam) + U5. Ro'yxatdan o'tgach tizim identifikatsiyani (U5) taklif qiladi (ixtiyoriy). U5 (9–10 qadam): uy egasi → ko'chmas mulklar ro'yxatini yuklash taklifi; ijarachi → skoringdan o'tish taklifi (ixtiyoriy).
> «Agar foydalanuvchi uy egasi rolida ro'yxatdan o'tsa unga tegishli ko'chmas mulklari ro'yxatini yuklab berish taklifi beriladi… Agar foydalanuvchi ijarachi bo'lsa unga skoringdan o'tish taklif beriladi (ixtiyoriy).»

## Reliz / R5
- **RELIZ:** `2-5 MyID / US 5` — «Muvaffaqiyatli identifikatsiyadan so'ng: ijarachi → skoring; uy egasi → ko'chmas mulklarini import qilish sahifasiga».
- **R5 o'zgarishi:** yo'q.

## Ijarachi (👤)
1. PIN → MyID identifikatsiya (02).
2. Identifikatsiyadan so'ng skoring taklifi — **ixtiyoriy** (04-skoring).
3. Skoringsiz ham ijarachi asosiy sahifasiga o'tadi (cheklangan: R1 uchun keyin skoring talab qilinadi).

## Uy egasi (🏠)
1. PIN → MyID identifikatsiya (02).
2. Identifikatsiyadan so'ng **kadastr/iHamkor import** taklifi (02-identifikatsiya → kadastr-import).
3. Import qilsa yoki o'tkazsa — uy egasi asosiy sahifasiga o'tadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi PIN yaratdi **WHEN** MyID tugaydi **THEN** skoring taklifi ko'rsatiladi (ixtiyoriy).
- **GIVEN** uy egasi PIN yaratdi **WHEN** MyID tugaydi **THEN** kadastr import taklifi ko'rsatiladi.

## Kod joylashuvi
- **Modul:** orkestrator `lib/core/services/onboarding_flow_service.dart` (`OnboardingStep{auth, pincode, identification, scoring, payment, cadastre, main}`)
- **Sahifa:** `identification_page` → (ijarachi) `core_screens/scoring/*` / (uy egasi) `landlord_cadastre_onboarding_page`
- **Preflight:** `RequestPreflightService`, `ListingPreflightService` — skoring/kadastr'ni **talab bo'yicha** ochadi.

## Konflikt / farqlar
- ⚠ **Skoring/kadastr majburiy emas.** TZ U1'da bu qadamlar ro'yxatdan o'tish oqimida (ixtiyoriy bo'lsa ham) keladi; kodda ular login zanjiridan **butunlay chiqarilgan** va faqat kerak bo'lganda (preflight) ochiladi. Guest-first yondashuv. → [`_konfliktlar.md`](../../_konfliktlar.md).
