# 09 — Referens va sharhlar (reviews)

Ishonch mexanizmlari: uy egasi ijarachi haqida **referens** yozadi, ijarachi o'tgan ijarasini **tavsiyanoma (recommendation)** bilan tasdiqlaydi, **oilaviy holat** ma'lumoti kiritiladi va foydalanuvchi **sharhlari (reviews)** ko'rsatiladi. TZ da bu alohida use-case emas — asosan **reliz R3–R5** qo'shimchalari; TZ da **S1** ning 15-qadami kiruvchisi sifatida uchraydi: «Oilaviy holat, farzandlar va daromad to'g'risida ma'lumot yuklash hamda tavsiyanoma qo'shish funksionali ochiladi».

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`tenant-reference.md`](tenant-reference.md) | Uy egasi ijarachi haqida referens yozadi (deeplink, 3-qadamli wizard) | (reliz) | 🟡 |
| [`recommendation.md`](recommendation.md) | Ijarachi o'tgan ijarasini tasdiqlaydi (tavsiyanoma) | S1 (15-qadam) | ✅ |
| [`marital-status.md`](marital-status.md) | Oilaviy holat + tasdiqlovchi fayllar | S1 (15-qadam) | ✅ |
| [`reviews.md`](reviews.md) | Foydalanuvchi sharhlari — faqat o'qish | (reliz R5, yashirin) | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
uy egasi → deeplink /reference/create?tenant_id → 3 qadam (asosiy / muammolar / tavsiya)
   → POST /mobile/reference/create/?tenant_id   (+ /admin/... damage-photo, lookuplar)
ijarachi → skoring tavsiyalari sahifasi → tavsiyanoma yaratish
   → POST /mobile/recommendation/attachments/create (multipart) → /recommendation/create
ijarachi → oilaviy holat sheet → PATCH /mobile/marital-status/update + attachments
har kim → uy egasi profili → GET /mobile/users/{id}/reviews/  (o'qish; R5 buildда yashirin)
```

> ⚠ **Kod TZ/reliz'dan farq qiladi:** (1) `tenant_reference` lookup va damage-photo endpointlari `/admin/` namespace ostida — bu CLAUDE.md qoidasiga zid («all data sources call `/mobile/` … never `/admin/`»), lookuplar `IsAdmin` sabab 401/403 bo'lishi mumkin → wizard text-only rejimga tushadi. (2) reviews faqat o'qish (yozish endpointi yo'q); reyting bloki R5 buildда yashirilgan (RelizF). (3) referens/tavsiyanoma/oilaviy holat TZ da alohida use-case emas — S1 kiruvchisi. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md) B9, B10, B11.

## Kod modullari

`lib/features/tenant_reference` (`TenantReferenceCubit`, 3-qadamli wizard) · `lib/features/recommendation` (`RecommendationListCubit`, `RecommendationDetailCubit`, `CreateRecommendationCubit`; UI `lib/features/core_screens/scoring/pages/`) · `lib/features/marital_status` (`MaritalUploadCubit`) · `lib/features/reviews` (`ReviewsBloc`).

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Referens yaratish | `POST /mobile/reference/create/` — `?tenant_id=` |
| Referens — zarar foto | ⚠ `POST /admin/user/damage-photo/create/` (multipart `photo`) |
| Referens — lug'atlar | ⚠ `GET /admin/user/{damage-type\|complaint-type\|contract-breach-type}/list/` |
| Tavsiyanoma ro'yxati | `GET /mobile/recommendation/list/` · `GET /mobile/recommendation/detail/{id}/` |
| Tavsiyanoma yaratish | `POST /mobile/recommendation/attachments/create/` (multipart) · `POST /mobile/recommendation/create/` |
| Oilaviy holat | `PATCH /mobile/marital-status/update/` — `{marital_status}` |
| Oilaviy holat — fayllar | `POST /mobile/attachments/marital-status/` (multipart) |
| Sharhlar (o'qish) | `GET /mobile/users/{userId}/reviews/` |
