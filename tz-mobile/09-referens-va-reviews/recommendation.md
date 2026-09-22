# Tavsiyanoma (recommendation)

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · Skoring moduli (15-qadam). Skoring hisoboti olingach ijarachi o'tgan ijara tajribasini tasdiqlovchi tavsiyanoma qo'shishi mumkin.
> «(S1, 15-qadam) Oilaviy holat, farzandlar va daromad to'g'risida ma'lumot yuklash hamda **tavsiyanoma qo'shish** funksionali ochiladi.»

## Reliz / R5
- **RELIZ:** ijarachi o'tgan uy egasi va ijara davri bo'yicha tavsiyanoma yaratadi; kvitansiya/hujjat fayllari biriktiriladi. Fayllar avval yuklanadi, so'ng tavsiyanoma yaratishda `attachment_ids` orqali bog'lanadi.
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Ijarachi skoring tavsiyalari sahifasidan (`ScoringRecommendationsPage`) yangi tavsiyanoma yaratishga o'tadi (`CreateRecommendationPage`).
2. Har fayl: `POST /mobile/recommendation/attachments/create/` (multipart `image`) → `attachment.id` qaytadi (nullable `recommendation` FK bilan saqlanadi).
3. Forma: `POST /mobile/recommendation/create/` (JSON) — `property_name`, `latitude`, `longitude`, `landlord_name`, `landlord_phone`, `rental_start`, `rental_end` (`yyyy-MM-dd`), `attachment_ids`. Backend fayllarni yangi tavsiyanomaga bulk-update bilan bog'laydi.
4. Ro'yxat/detal: `GET /mobile/recommendation/list/`, `GET /mobile/recommendation/detail/{id}/` (`RecommendationStatus` bilan).

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi fayl biriktirdi **WHEN** `attachments/create` chaqiriladi **THEN** `attachment.id` qaytadi va keyingi `create` da `attachment_ids` ga qo'shiladi.
- **GIVEN** forma to'ldirildi **WHEN** yuborish bosiladi **THEN** `POST /mobile/recommendation/create/` JSON body bilan yuboriladi va ro'yxatda paydo bo'ladi.
- **GIVEN** tavsiyanoma tanlandi **WHEN** detal ochiladi **THEN** `recommendation/detail/{id}/` holat bilan ko'rsatiladi.

## Kod joylashuvi
- **Modul:** `lib/features/recommendation` (UI: `lib/features/core_screens/scoring/pages/create_recommendation_page.dart`, `scoring_recommendations_page.dart`)
- **Sahifa / BLoC:** `CreateRecommendationCubit`, `RecommendationListCubit`, `RecommendationDetailCubit`; entitilar `Recommendation`, `RecommendationAttachment`, `RecommendationDraft`, `RecommendationStatus`
- **Endpoint:** `GET /mobile/recommendation/list/`, `GET /mobile/recommendation/detail/{id}/`, `POST /mobile/recommendation/attachments/create/` (multipart), `POST /mobile/recommendation/create/` (JSON)

## Konflikt / farqlar
- ⚠ TZ da tavsiyanoma S1 ning 15-qadam kiruvchisi sifatida qisqa eslatiladi; to'liq maydonlar/oqim reliz va kodda aniqlangan. → [`_konfliktlar.md`](../_konfliktlar.md) B11.
- Endpointlar to'liq `/mobile/` ostida — farq (referensdan farqli) yo'q.
