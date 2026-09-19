# 11 — Qo'llab-quvvatlash va xavfsizlik

Texnik qo'llab-quvvatlash (murojaat) hamda foydalanuvchi kontenti xavfsizligi: moderatsiya/shikoyat, bloklash va maxfiylik. TZ use-case: **T1** (murojaat yuborish) + UGC xavfsizlik mexanizmlari (App Store Guideline 1.2).

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`murojaat-t1.md`](murojaat-t1.md) | T1: murojaat/yordam — statik kontakt sahifasi | T1 | 🟡 |
| [`report-service.md`](report-service.md) | To'liq hisobot (Rentmi) tarifi xizmati | — (S1 bilan bog'liq) | ✅ |
| [`moderation-shikoyat.md`](moderation-shikoyat.md) | UGC: shikoyat/report qilish | UGC (E4 web) | ✅ |
| [`block-va-privacy.md`](block-va-privacy.md) | Foydalanuvchini bloklash + maxfiylik markazi | UGC / Guideline 1.2 | ✅ |

## Umumiy holat (kod'dagi haqiqiy holat)

```
YORDAM (T1):  Profil → Qo'llab-quvvatlash → statik kontaktlar (Telegram/telefon/email)
              ⚠ chipta (ticket) tizimi YO'Q; guest ham Telegram orqali

XAVFSIZLIK:   e'lon/user → "Shikoyat" → moderation report (backend)
              user → "Bloklash" → blocks; darhol e'lon/chat/favorites filtrlanadi
              Profil → Maxfiylik → bloklangan foydalanuvchilar, shartlar
```

> ⚠ **Asosiy konflikt:** T1 TZ da **chipta tizimi** (kategoriya, mavzu, tavsif, fayl, ticket raqami) sifatida yozilgan; kodda esa `support` = **statik kontakt sahifasi**. Batafsil: [`murojaat-t1.md`](murojaat-t1.md), [`_konfliktlar.md`](../_konfliktlar.md).

## Kod modullari

`lib/features/support` (statik kontakt) · `lib/features/report_service` (hisobot tarifi) · `lib/features/moderation` (shikoyat) · `lib/features/blocks` (bloklash) · `lib/features/settings/presentation/pages/privacy_page.dart` (maxfiylik).

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Hisobot tarifi | `GET /mobile/report-service/` |
| Shikoyat sabablari | `GET /mobile/moderation/report-reasons/?applies_to=` |
| Shikoyat yuborish | `POST /mobile/moderation/report/` — `{content_type, object_id, reason_code, description?}` |
| Bloklash | `POST /mobile/users/block/` — `{blocked_user_id, reason, description?}` |
| Blokni yechish | `DELETE /mobile/users/block/{userId}/` |
| Bloklanganlar ro'yxati | `GET /mobile/users/blocked/` |
| Blok holati | `GET /mobile/users/{userId}/block-status/` |
| Murojaat (T1) | yo'q — statik kontakt (`url_launcher`) |

## Route'lar
`/settings/blocked-users` · `/settings/my-reports` · `/settings/privacy`
