# Tavsiyalar va skoringni yaxshilash

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 15-qadam). Hisobotdan so'ng tavsiyanoma qo'shish funksionali ochiladi.
> «Oilaviy holat, farzandlar va daromad to'g'risida ma'lumot yuklash hamda **tavsiyanoma qo'shish** funksionali ochiladi.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6` — funksional talablar orasida «**Recommendation screens**», «Recommendation engine» (bog'liqlik); natijada «tavsiyalar» ko'rsatiladi.
- **R5 o'zgarishi:** tavsiyalar rule-based v1 sifatida — «badge va tavsiyalar faqat ko'maklashuvchi ma'lumot» `R5 · §5`.

## Bajarish tartibi
1. Natija sahifasidan tavsiyalar bo'limiga o'tiladi (`scoring_recommendations_page`).
2. Tavsiyanoma yaratish (`create_recommendation_page`) — foydalanuvchi tavsiyanoma qo'shadi; havola yaratilsa `link_created_sheet` ko'rsatiladi.
3. Skoringni yaxshilash maslahatlari (`score_improve_tips_page`) — ballni oshirish bo'yicha amaliy tavsiyalar (`score_improve_tip_card`, `score_improve_tavsiya_card`).
4. Ball karuseli (`score_carousel_page`) — band/faktorlar bo'yicha slaydlar.
5. Self-scoring (`tenant_self_scoring_page`) — ijarachi o'z ballini xaridsiz dastlabki baholash.

## Qabul kriteriyalari (BDD)
- **GIVEN** natija tayyor **WHEN** tavsiyalar ochiladi **THEN** ijobiy/salbiy faktorlar bo'yicha tavsiyalar va yaxshilash maslahatlari ko'rsatiladi.
- **GIVEN** foydalanuvchi tavsiyanoma qo'shadi **WHEN** saqlanadi **THEN** havola/yozuv yaratiladi va tasdiq ko'rsatiladi.
- **GIVEN** ijarachi self-scoring ochadi **WHEN** ma'lumot kiritiladi **THEN** dastlabki baholash natijasi ko'rsatiladi.

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/scoring`
- **Sahifa / BLoC:** `ScoringRecommendationsPage`, `CreateRecommendationPage`, `ScoreImproveTipsPage`, `ScoreCarouselPage`, `TenantSelfScoringPage`
- **Endpoint:** tavsiya/self-scoring mahalliy oqim; skoring ma'lumoti [`04-natija-band-faktor.md`](04-natija-band-faktor.md) endpointlaridan keladi

## Konflikt / farqlar
- ⚠ **Self-scoring:** `tenant_self_scoring_page` — TZ S1 da aniq ko'rsatilmagan qo'shimcha funksiya (xaridsiz dastlabki baholash). → [`_konfliktlar.md`](../_konfliktlar.md).
- Tavsiyanoma qo'shish TZ 15-qadam bilan mos. Boshqa farq aniqlanmadi.
