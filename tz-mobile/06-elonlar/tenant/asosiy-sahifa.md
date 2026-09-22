# Ijarachi asosiy sahifasi (Home)

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1. Asosiy sahifa E3 ning kirish nuqtasi: faol e'lonlar oldindan belgilangan tartibda (sana kamayib + ijarachi skoring bali asosida) bo'limlarga ajratilib ko'rsatiladi.
> «Tizim faol e'lonlarni oldindan belgilangan tartibda ko'rsatadi (sana bo'yicha kamayib, va ijarachining skoring bali asosida).»

## Reliz / R5
- **RELIZ:** `3-1 Asosiy sahifa / IJ-01` — sahifa komponentlari parallel yuklanadi (Actual story, Rentmi Score, e'lon bo'limlari); Score bloki: tugallangan → ball (0–100), aks holda 'Skoringdan o'ting' (BQ-1/BQ-2); guest e'lonlarni ko'radi, so'rov imkonsiz (BQ-3); faqat manual pull-to-refresh (BQ-4); stories tartibi backend dinamik (BQ-5). `IJ-02` — Actual stories full-screen (5 sek avto, swipe, CTA).
- **R5 o'zgarishi:** **R5-IJ-01/02** — salomlashish header, yangi navbar (Main/Saved/Lenta/So'rovlar/Profil), shahar chip ("Toshkentda uy qidiramizmi?"), xona soni chips (Barchasi/1/2/3/4+), bo'limlar (**TOP kvartiralar / Kvartiralar / Rentmi Maslahat beradi / Villa**, har birida "Hammasi >"), **skoring-mos uylar bloki** (gauge, "Skoringizga mos N ta uy"). **R5-IJ-03** — badge'lar tizimi (Sizga mos / Top / Tekshirilgan / Narxi tushdi) va rasm ustida parametrlar. Stories R5 da «yashiriladi» deyilgan (kod saqlanadi).

## Bajarish tartibi
1. Token tekshiriladi; mavjud va muddati o'tmagan bo'lsa — ijarachi rejimi, aks holda guest.
2. `GET /mobile/announcements/tenant/home/` — bo'limlar (kategoriyalar) va ularning e'lonlari keladi; badge bayroqlari shu javobda.
3. Rentmi Score bloki: `TenantScoreCubit` ballni ko'rsatadi yoki 'Skoringdan o'ting' (guest/tugallanmagan).
4. Stories qatori: `GET /mobile/stories/`; ko'rilganda `POST /mobile/story/media/{id}/seen/`.
5. Xona soni chips va shahar chip filtrni katalogga (qidiruv-filtr) uzatadi.
6. Pull-to-refresh — barcha komponentlar qayta yuklanadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** ro'yxatdan o'tgan ijarachi **WHEN** home ochiladi **THEN** bo'limlar, chips, skoring bloki va badge'li kartalar ≤3 s ichida ko'rinadi (badge'lar keshdan).
- **GIVEN** guest **WHEN** home ochiladi **THEN** e'lonlar ko'rinadi, Score blokida faqat 'Skoringdan o'ting', shaxsiy ball ko'rsatilmaydi.
- **GIVEN** "Narxi tushdi" badge'li e'lon **WHEN** karta ko'rsatiladi **THEN** badge faqat home javobidagi bayroqqa qarab chiqadi (real narx tarixi asosida).

## Kod joylashuvi
- **Modul:** `lib/features/tenant_dashboard`
- **Sahifa / BLoC:** `TenantDashboardPage` / `TenantHomeBloc` (+ `TenantScoreCubit`, `TenantStoriesCubit`); widget'lar: `tenant_property_section`, `tenant_score_card`, `tenant_category_chips`, `tenant_stories_row`, `tenant_story_viewer`
- **Endpoint:** `GET /mobile/announcements/tenant/home/`; `GET /mobile/stories/`; `POST /mobile/story/media/{id}/seen/`

## Konflikt / farqlar
- ⚠ **Badge'lar manbai:** *Sizga mos / Top / Narxi tushdi* faqat `tenant/home/` javobida keladi — `announcements` entity'sida bu maydonlar yo'q. "Tekshirilgan" = backend `moderated_status` (`moderation_status.dart`), spec pill (xona/m²/qavat) = frontend, `is_favorited` = backend. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K1.
- ⚠ **Stories:** R5 «Actual History stories yashiriladi (kod saqlanadi)» ↔ kodda faol (`tenant_stories_cubit.dart`, `GET /mobile/stories/`). → E-K2.
- ⚠ **Skoring-mos uylar bloki (R5-IJ-01):** gauge/score card mavjud, ammo "Skoringizga mos N ta uy" alohida hisoblovchi endpoint (R5 backend) kodda topilmadi — blok qisman.

---

## Release 5 — R5-IJ-01 — Yangilangan asosiy sahifa
**Kod holati:** 🟡 (navbar'da "Saved" yo'q — K2; stories yashirilishi ↔ kodda faol — E-K2)

**User Story:** Ijarachi sifatida men yangilangan asosiy sahifada kerakli bo'limlarga tez o'tishni xohlayman, shunda uy qidirishni bir ekrandan boshlay olaman.

**Tavsif:** Asosiy sahifa yangi dizaynda: salomlashish headeri, tepada chat va bildirishnoma tugmalari, "Toshkentda uy qidiramizmi?" klikabel shahar tanlovi, xona soni chips filtri, bo'limlar (TOP kvartiralar / Kvartiralar / Rentmi Maslahat beradi / Villa), "Xarita orqali qidirish" banneri. Pastki navbar: Main, Saved, Lenta, So'rovlar, Profil. Actual History stories yashirin qoladi.

**Qabul mezonlari:**
- GIVEN ijarachi tizimga kirgan WHEN asosiy sahifa ochilsa THEN header, chips, barcha bo'limlar va yangi navbar 3 soniya ichida yuklanadi
- GIVEN shahar nomi ko'rsatilgan WHEN "Toshkentda" bosilsa THEN shahar/hudud tanlash oynasi ochiladi va tanlov barcha bo'limlarga qo'llanadi
- GIVEN xona chips'lari WHEN "2 xona" tanlansa THEN bo'limlardagi e'lonlar 2 xonalilarga filtrlanadi
- GIVEN bo'lim mavjud WHEN "Hammasi >" bosilsa THEN shu bo'limning to'liq ro'yxat sahifasi ochiladi
- GIVEN yangi navbar WHEN "Lenta" bosilsa THEN e'lonlar lentasi ochiladi (yangi sahifa emas)

---

## Release 5 — R5-IJ-02 — Skoring-mos uylar bloki
**Kod holati:** 🟡 (skoring-mos endpoint bor)

**User Story:** Ijarachi sifatida men skoring balimga mos uylar sonini ko'rishni xohlayman, shunda arizam qabul qilinish ehtimoli yuqori uylarga e'tibor qarata olaman.

**Tavsif:** Asosiy sahifada gauge (ball), "Skoringizga mos N ta uy" va "Arizalaringiz ustuvor ko'rib chiqiladi" izohi. Bosilganda mos uylar ro'yxati ochiladi. Moslik: ijarachi bali ≥ e'lonning minimal skoring talabi. Soni soatlik keshda.

**Qabul mezonlari:**
- GIVEN ijarachi skoringdan o'tgan WHEN asosiy sahifa ochilsa THEN blokda joriy bal va mos uylar soni ko'rinadi
- GIVEN ijarachi skoringdan o'tmagan WHEN asosiy sahifa ochilsa THEN blok "Skoringdan o'ting" CTA bilan (S1 ga yo'naltiradi)
- GIVEN blok ko'rsatilgan WHEN bosilsa THEN faqat mos e'lonlardan iborat ro'yxat ochiladi
- GIVEN mos uy yo'q WHEN blok ochilsa THEN "Hozircha mos uy topilmadi" ko'rsatiladi

---

## Release 5 — R5-IJ-03 — Badge'lar tizimi
**Kod holati:** 🟡 (badge'lar faqat home endpoint — E-K1)

**User Story:** Ijarachi sifatida men e'lon kartalarida ishonch va moslik belgilarini ko'rishni xohlayman, shunda qaysi uyga ariza berishni tezroq hal qila olaman.

**Tavsif:** To'rt badge: "Sizga mos" (ikki tomonlama moslik), "Top" (og'irlikli ball, hudud kesimida), "Tekshirilgan" (moderatsiya + identifikatsiya + tegishlilik AND), "Narxi tushdi" (narx tarixi). Rasm ustida m²/xona/qavat va kartada ko'rishlar soni.

**Qabul mezonlari:**
- GIVEN e'lon uch shartning barchasiga javob beradi WHEN karta ko'rsatilsa THEN "Tekshirilgan" chiqadi; birorta shart bajarilmasa — chiqmaydi
- GIVEN e'lon ijarachi filtriga mos VA ijarachi e'lon talabiga mos WHEN karta ko'rsatilsa THEN "Sizga mos" chiqadi
- GIVEN narx 7–14 kunda belgilangan foizdan ko'p pasaygan WHEN karta ko'rsatilsa THEN "Narxi tushdi" chiqadi; sun'iy ko'tarib-tushirishda chiqmaydi
- GIVEN tegishlilik ma'lumoti yo'q WHEN karta ko'rsatilsa THEN "Tekshirilgan" ko'rsatilmaydi (default: yashirish)
