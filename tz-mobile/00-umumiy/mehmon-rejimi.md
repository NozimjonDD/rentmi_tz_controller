# Mehmon (guest) rejimi

**Rollar:** 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
§4.1.3.2 — Foydalanuvchi rollari. Ro'yxatdan o'tmagan foydalanuvchi (guest) cheklangan imkoniyatlarga ega.
> «Ro'yxatdan o'tmasdan cheklangan imkoniyatlar bilan mobil ilovani ko'rib chiqayotgan potensial ijarachi yoki uy egasi ro'lidagi foydalanuvchi. Faqat ayrim e'lonlarni ko'rish va tizim bo'yicha umumiy ma'lumot olish imkoniyatiga ega.»

## Reliz / R5
- **RELIZ:** `2-3 US 3` — «Guest user faqat listings ko'ra oladi», «Full features uchun register kerak». `3-1 IJ-01`:
  - `BQ-3` — «Guest e'lonlarni ko'ra oladi; so'rov imkonsiz»
  - `BQ-2` — «Guestga faqat 'Skoringdan o'ting'; shaxsiy ball ko'rsatilmaydi»
- **R5 o'zgarishi:** yo'q (asosiy sahifa qayta qurilgan, guest imkoniyatlari o'zgarmagan).

## Bajarish tartibi
1. Onboardingdan keyin `NavigateToGuestMode` → `AuthGuardService.markPincodeUnlocked()` + `tenantDashboard`.
2. Guest e'lonlar ro'yxati va detalini ko'radi (E3 — ruxsat).
3. So'rov yuborish (R1) urinishida ro'yxatdan o'tish talab qilinadi.
4. Asosiy sahifada skoring bloki faqat 'Skoringdan o'ting' — shaxsiy ball yo'q.

## Qabul kriteriyalari (BDD)
- **GIVEN** guest **WHEN** e'lonlar ro'yxatini ochadi **THEN** e'lonlarni ko'ra oladi (E3).
- **GIVEN** guest **WHEN** ijara so'rovi (R1) yubormoqchi **THEN** ro'yxatdan o'tish + skoring talab qilinadi.
- **GIVEN** guest **WHEN** asosiy sahifa skoring bloki **THEN** faqat 'Skoringdan o'ting', shaxsiy ball ko'rsatilmaydi.

## Kod joylashuvi
- **Modul:** guest kirishi — `lib/features/onboarding` (`NavigateToGuestMode`) → `lib/features/tenant_dashboard`
- **Xizmat:** `AuthGuardService.markPincodeUnlocked()` + `tenantDashboard`
- **Endpoint:** ochiq e'lonlar — [`06-elonlar`](../06-elonlar/about.md); guest uchun alohida endpoint yo'q.

## Konflikt / farqlar
- ⚠ **Guest — TZ da alohida rol, kodda esa emas.** TZ §4.1.3.2 guestni alohida rol sifatida sanaydi; kodda guest alohida rol qiymati emas — `selectedRole='tenant'` bilan PIN gate ochilgan ijarachi dashboardidan foydalanadi. → [`_konfliktlar.md`](../_konfliktlar.md)
