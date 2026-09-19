# E'lon tafsiloti (Detail)

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1 (5-qadam). Foydalanuvchi ro'yxatdan e'lonni tanlaydi; tafsilotdan ijara so'rovi yuborishi, bloklashi, ulashishi va shikoyat qilishi mumkin.
> «Foydalanuvchi e'lonni tanlaydi yoki filtrlarni o'zgartiradi … e'lon egasiga ijara so'rovi yuborishi, e'lonni bloklashi, ulashishi va shikoyat qilishi mumkin.»

## Reliz / R5
- **RELIZ:** `IJ-08` — e'lon kartochkasidan detail'ga o'tish (guest ham ko'radi, so'rov imkonsiz — IJ-01 BQ-3).
- **R5 o'zgarishi:** **R5-IJ-07** — rasm ustida parametrlar, yangi maydonlar (**minimal ijara davri**, **kirish sanasi**, **e'lon joylangan vaqt**), **Ko'rildi / Ariza / Saqlangan** statistika bloki, badge'lar qatori (Tekshirilgan, Sizga mos, javob vaqti indikatori "Odatda N soatda javob beradi"), uy egasi bloki → **ommaviy profil** ([`uy-egasi-profil.md`](uy-egasi-profil.md)), CTA "**Ariza jo'natish**".

## Bajarish tartibi
1. Foydalanuvchi kartani bosadi: `GET /mobile/announcements/tenant/detail/{id}/`.
2. Ko'rish tracking: `POST /mobile/announcements/{id}/view/` (statistika uchun).
3. Detail bo'limlari render qilinadi: rasm header, spec (xona/m²/qavat), narx, tavsif, qulayliklar, atrofdagi qulayliklar, joylashuv (xarita), o'xshash e'lonlar.
4. Badge'lar ko'rsatiladi: "Tekshirilgan" (`moderated_status`), spec pill (frontend), `is_favorited` (backend).
5. Amallar: "Ariza jo'natish" (R1 → [`07-sorovlar`](../../07-sorovlar/about.md)), yurakcha (wishlist), ulashish, bloklash (`lib/features/blocks`), shikoyat.

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi kartani bosadi **WHEN** detail ochiladi **THEN** e'lon to'liq tafsiloti va Ko'rildi/Ariza/Saqlangan statistikasi ko'rinadi, ko'rish qayd etiladi.
- **GIVEN** guest **WHEN** detail ochiladi **THEN** e'lon ko'rinadi, ammo "Ariza jo'natish" ro'yxatdan o'tishga yo'naltiradi.
- **GIVEN** moderatsiyadan o'tgan + tegishli e'lon **WHEN** detail ko'rsatiladi **THEN** "Tekshirilgan" badge chiqadi.

## Kod joylashuvi
- **Modul:** `lib/features/announcements`
- **Sahifa / BLoC:** `AnnouncementDetailPage` / `AnnouncementDetailBloc`; widget'lar: `detail_image_header`, `detail_property_specs`, `detail_price_section`, `detail_posted_at`, `detail_similar_section`, `detail_action_buttons`, `moderation_status_visuals`
- **Endpoint:** `GET /mobile/announcements/tenant/detail/{id}/`; tracking `POST /mobile/announcements/{id}/view/` (+ `/phone-view/` qo'ng'iroqda)

## Konflikt / farqlar
- ⚠ **Badge'lar aralash manba:** "Tekshirilgan" = backend `moderated_status`; spec pill = frontend; "Sizga mos"/"Narxi tushdi" — home/list badge bayroqlaridan (detail entity'sida bu maydonlar to'liq emas). → [`_konfliktlar.md`](../../_konfliktlar.md) E-K1.
- ⚠ **Javob vaqti indikatori (R5-IJ-07):** "Odatda N soatda javob beradi" — R5 backend agregatiga tayanadi (kamida 3 javob, 30 kun mediana); kod tomonda to'liq bog'lanmagan bo'lishi mumkin.
- ⚠ **Uy egasi bloki → ommaviy profil:** o'tish nuqtasi bor, ammo ommaviy profil ekrani kodda yo'q (`uy-egasi-profil.md`). → E-K6.
