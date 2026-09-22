# Sharhlar (reviews) — faqat o'qish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan (faqat o'qish)

## TZ manbai
TZ da sharhlar alohida use-case sifatida yo'q — ishonch signali sifatida uy egasi ommaviy profili konteksti bilan bog'lanadi (reliz R5).
> «(R5) Uy egasi ommaviy profili: ... Eslatma: **reyting** va "Rentmi kafolati" bloklari dizayndan R5 buildida yashiriladi (RelizF).»

## Reliz / R5
- **RELIZ (R5):** foydalanuvchi sharhlari va reyting agregati ommaviy profil uchun rejalashtirilgan.
- **R5 o'zgarishi:** reyting bloki R5 **buildida yashirilgan** (RelizF) — kod saqlanadi, ko'rsatilmaydi. Shu sabab bu modul kodda faqat o'qish (read-only) sifatida mavjud.

## Bajarish tartibi
1. Uy egasi ommaviy profili (yoki foydalanuvchi profili) ochilganda `GET /mobile/users/{userId}/reviews/` `{page, page_size}` chaqiriladi.
2. Javob: sharhlar ro'yxati (`Review`) va agregat statistika (`ReviewsStats`).
3. UI reyting/sharhlarni ko'rsatadi — lekin R5 buildida bu blok yashirin (RelizF).

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchining sharhlari bor **WHEN** `users/{id}/reviews/` so'raladi **THEN** sharhlar ro'yxati va `averageRating`/`distribution` qaytadi.
- **GIVEN** sharh yo'q **WHEN** endpoint chaqiriladi **THEN** `ReviewsStats.empty` (0 reyting, bo'sh taqsimot) qaytadi.
- **GIVEN** R5 build **WHEN** ommaviy profil ochiladi **THEN** reyting bloki ko'rinmaydi (yashirilgan).

## Kod joylashuvi
- **Modul:** `lib/features/reviews`
- **Sahifa / BLoC:** `ReviewsBloc`; entitilar `Review` (`rating` 1–5, `tags`, `author`), `ReviewAuthor`, `ReviewsStats` (`averageRating`, `distribution` 1–5, `totalCount`)
- **Endpoint:** `GET /mobile/users/{userId}/reviews/` — `{page, page_size}`

## Konflikt / farqlar
- ⚠ **Faqat o'qish:** sharh yozish/yaratish endpointi kodda yo'q; modul faqat `GET .../reviews/` ni chaqiradi. → [`_konfliktlar.md`](../_konfliktlar.md) B10.
- ⚠ Reyting bloki R5 buildida yashirilgan (RelizF) — ko'rsatish hozircha o'chirilgan, kod saqlanadi. → B10.
