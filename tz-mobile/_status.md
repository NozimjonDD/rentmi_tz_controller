# Qamrov va holat jadvali

Har bir TZ mobil use-case va reliz/R5 funksiyasi qamrab olinganini va kod'dagi holatini ko'rsatadi. Bu fayl "TZ'dan hech narsa qolib ketmasin" nazorati.

**Holat:** ✅ bajarilgan · 🟡 qisman · ❌ yo'q · 💤 o'chirilgan (kodda bor, faol emas)

## 1. TZ mobil use-case'lar (15 ta — hammasi qamralgan)

| ID | Nomi | Flow (hujjat) | Holat | Izoh |
|---|---|---|---|---|
| **U1** | Foydalanuvchini ro'yxatdan o'tkazish | [01-auth/02-register](01-auth/02-register/about.md) | ✅ | Guest-first oqim (K1); OTP muddati/urinishlar konflikti (C1, C2) |
| **U2** | Tizimga kirish (PIN) | [01-auth/03-login](01-auth/03-login/about.md) | ✅ | — |
| **U3** | PIN-kodni tiklash | [01-auth/04-pincode](01-auth/04-pincode/about.md) | ✅ | — |
| **U4** | Foydalanuvchi profilini boshqarish | [03-profil](03-profil/about.md) | 🟡 | **Faol qurilmalarni boshqarish** va **telefon o'zgartirish** endpoint'lari kodda yo'q |
| **U5** | Foydalanuvchini identifikatsiya (MyID) | [02-identifikatsiya](02-identifikatsiya/about.md) | ✅ | + uy egasi kadastr import |
| **S1** | Rentmi hisobotini xarid qilish | [04-skoring](04-skoring/about.md) | ✅ | Amal muddati aniqlanmagan (C4); farzandlar/daromad maydonlari qisman (B11) |
| **S2** | Skoring ma'lumotini tashqi manbadan | [04-skoring/05-tashqi-manba-s2](04-skoring/05-tashqi-manba-s2.md) | ✅ | Backend ichida (`/scoring/check`→`/status`) |
| **B1** | To'lovlar tarixini ko'rish | [05-billing](05-billing/about.md) | ✅ | 1-bosqichda faqat skoring xaridi tranzaksiyalari (B6) |
| **E1** | E'lon yaratish | [06-elonlar/landlord](06-elonlar/landlord/elon-yaratish.md) | ✅ | Foto max-15 tekshirilmaydi (E-K10); + tashqi import |
| **E2** | E'lonni tahrirlash/o'chirish | [06-elonlar/landlord](06-elonlar/landlord/elon-tahrir.md) | ✅ | Ikki modulda (E-K7) |
| **E3** | E'lonlarni qidirish/filtrlash | [06-elonlar/tenant](06-elonlar/tenant/qidiruv-filtr.md) | ✅ | rooms/pets frontend-only (E-K5); saved-filter Clean Arch chetlab (E-K3) |
| **R1** | Ijara so'rovini yuborish | [07-sorovlar/tenant](07-sorovlar/tenant/ariza-yuborish.md) | 🟡 | **Strukturalangan maydonlar yo'q** — faqat erkin matn (K4) |
| **R2** | Ijara so'rovini ko'rib chiqish | [07-sorovlar/landlord](07-sorovlar/landlord/korib-chiqish.md) | 🟡 | **24h SLA countdown yo'q** (K3/C3); "muhokama" amali yo'q; statistika qisman mock |
| **N1** | Push-bildirishnoma sozlamalari | [10-bildirishnoma](10-bildirishnoma/sozlamalar-n1.md) | ❌ | **Amalda yo'q** — faqat bitta global toggle, saqlanmaydi |
| **T1** | Murojaat yuborish | [11-support-va-xavfsizlik](11-support-va-xavfsizlik/murojaat-t1.md) | 🟡 | `support` statik kontakt; ticket-oqim = `report_service` (K7) |

## 2. Reliz / R5 qo'shimcha funksiyalari (TZ use-case'da yo'q)

| Funksiya | Flow | Holat | Izoh |
|---|---|---|---|
| Splash | [00-umumiy/splash](00-umumiy/splash.md) | ✅ | US1 |
| Til tanlash (4 til) | [00-umumiy/til-tanlash](00-umumiy/til-tanlash.md) | ✅ | US2, §4.3.3 |
| Onboarding | [00-umumiy/onboarding](00-umumiy/onboarding.md) | ✅ | US3; guest-first |
| Navigatsiya (navbar) | [00-umumiy/navigatsiya](00-umumiy/navigatsiya.md) | 🟡 | "Saved" tab yo'q (K2) |
| Asosiy sahifa + badge'lar | [06-elonlar/tenant/asosiy-sahifa](06-elonlar/tenant/asosiy-sahifa.md) | 🟡 | Badge'lar faqat home endpoint (E-K1) |
| Stories (Actual History) | 06-elonlar/tenant/asosiy-sahifa | 🟡 | R5 "yashiriladi" ↔ kodda faol (E-K2/C5) |
| Xarita orqali qidirish | [06-elonlar/tenant/xarita](06-elonlar/tenant/xarita.md) | ✅ | Backend klaster |
| Feed (Lenta) | [06-elonlar/tenant/feed](06-elonlar/tenant/feed.md) | ✅ | Reaksiya fire-and-forget (K11g) |
| Favorites (wishlist) | [06-elonlar/tenant/favorites](06-elonlar/tenant/favorites.md) | 🟡 | GET-mutatsiya (E-K4) |
| Uy egasi ommaviy profili | [06-elonlar/tenant/uy-egasi-profil](06-elonlar/tenant/uy-egasi-profil.md) | ❌ | R5-IJ-08 amalga oshirilmagan (E-K6) |
| Chat | [08-chat](08-chat/about.md) | ✅ | WS-only; SLA/countdown yo'q (B8) |
| Tenant reference | [09-referens-va-reviews/tenant-reference](09-referens-va-reviews/tenant-reference.md) | ✅ | `/admin/` yo'l qoidabuzarlik (B9) |
| Recommendation | [09-.../recommendation](09-referens-va-reviews/recommendation.md) | ✅ | S1 kiruvchisi |
| Oilaviy holat | [09-.../marital-status](09-referens-va-reviews/marital-status.md) | 🟡 | farzandlar/daromad yo'q (B11) |
| Sharhlar (reviews) | [09-.../reviews](09-referens-va-reviews/reviews.md) | 🟡 | Faqat o'qish; reyting R5'da yashiringan (B10) |
| Bildirishnomalar (ro'yxat) | [10-bildirishnoma/push-fcm](10-bildirishnoma/push-fcm.md) | ✅ | FCM + in-app; mark-all-read yo'q (K10) |
| Moderatsiya/shikoyat | [11-.../moderation-shikoyat](11-support-va-xavfsizlik/moderation-shikoyat.md) | ✅ | UGC |
| Bloklash + maxfiylik | [11-.../block-va-privacy](11-support-va-xavfsizlik/block-va-privacy.md) | ✅ | Apple Guideline 1.2 |
| Elektron shartnoma | [12-contract-dormant](12-contract-dormant/about.md) | 💤 | To'liq yozilgan, o'chirilgan (3-bosqich) |

## 3. Yakuniy hisob

- **TZ mobil use-case'lar:** 15 dan — ✅ 10 · 🟡 4 (U4, R1, R2, T1) · ❌ 1 (N1). **Barchasi qamralgan.**
- **Funksional bo'lmagan talablar** (tezlik, ishonchlilik, xavfsizlik, tillar, ergonomika, integratsiyalar): [`_talablar.md`](_talablar.md).
- **Konfliktlar:** [`_konfliktlar.md`](_konfliktlar.md) — C1–C7 (TZ↔reliz), A1/A2/A5 (TZ ichi), B4–B11, E-K1–E-K10, K1–K13 (kod↔spec + texnik qarz).
- **Web/admin use-case'lar** (U2-veb, E4, E5, A1–A4, T2, T3): qamrovdan tashqarida (kelajakda `tz-web/`).

## 4. E'tibor talab qiladigan bo'shliqlar (mobil, 1-bosqich)

1. **N1 (❌)** — push sozlamalari deyarli yo'q; TZ 5 tur bildirishnoma sozlamasini talab qiladi.
2. **R2 SLA (🟡)** — R5 markaziy funksiyasi (24h countdown) amalga oshirilmagan.
3. **U4 (🟡)** — faol qurilmalar boshqaruvi va telefon o'zgartirish endpoint'lari yo'q.
4. **R1 (🟡)** — ariza strukturalangan maydonlari yo'q.
5. **Uy egasi ommaviy profili (❌)** — R5 ishonch mexanizmi yo'q.
