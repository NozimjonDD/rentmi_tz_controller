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
