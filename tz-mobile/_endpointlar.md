# Backend API xaritasi (mobil)

Barcha yo'llar `https://api-mobile-prod.rentmi.uz/api/v1` ga nisbatan. HTTP — yagona `DioClient` orqali (`AuthInterceptor` 401 da avtomatik refresh). Xatolik formati: `{"detail":{"code","message"}}`.

## Auth va sessiya → [`01-auth/`](01-auth/about.md)
| Amal | Endpoint |
|---|---|
| OTP so'rash | `POST /auth/login/` `{phone_number, role}` → `secret` |
| OTP tasdiq | `POST /auth/login/confirm/` `{secret, otp}` → `{access, refresh, data:{user}}` |
| Token refresh | `POST /auth/token/refresh/` `{refresh}` |
| Chiqish | `POST /auth/logout/` |
| Qurilma (FCM) | `POST /mobile/device/register/` `{fcm_token, device_id, name, device_type}` |

## Identifikatsiya → [`02-identifikatsiya/`](02-identifikatsiya/about.md)
| Amal | Endpoint |
|---|---|
| MyID sessiya | `GET /mobile/identification/session/` → `session_id` |
| MyID tasdiq | `POST /mobile/identification/` `{code, image?}` |
| MyID (legacy) | `POST /mobile/identification/legacy/` `{code}` |
| Kadastr preview | `GET /mobile/homeowner-properties/import/preview/` |
| Kadastr import | `POST /mobile/homeowner-properties/import/create/` `{selected_objects}` |

## Profil → [`03-profil/`](03-profil/about.md)
| Amal | Endpoint |
|---|---|
| Profil | `GET /mobile/account/detail/{userId}/` · `PUT /mobile/profile/` |
| Avatar | `PATCH /mobile/account/update/` (multipart) |
| Parol | `POST /mobile/profile/change-password/` |
| Manzillar | `GET/POST /mobile/addresses/` · `PUT/DELETE /mobile/addresses/{id}/` · `POST /mobile/addresses/{id}/set-default/` |

## Skoring → [`04-skoring/`](04-skoring/about.md)
| Amal | Endpoint |
|---|---|
| Skoring boshlash | `POST /mobile/scoring/check/` `{rent_amount}` |
| Holat (polling) | `GET /mobile/scoring/status/` |
| To'liq hisobot | `GET /mobile/tenant/rentme-score/{userId}/?rental_request_id=` |
| Legacy skoring | `GET /mobile/scoring/{userId}/` |
| Daromad | `PATCH /mobile/unconfirmed_income-period/update/` · `POST /mobile/attachments/income-status/` (multipart) |
| Narx | `GET /mobile/report-service/` |

## Billing / to'lov → [`05-billing/`](05-billing/about.md)
| Provayder | Endpoint |
|---|---|
| Universal order | `GET /mobile/orders/active/` · `POST /mobile/universal/orders/` `{provider, amount}` |
| Atmos (karta) | `GET /mobile/card/list/` · `POST /mobile/card/bind/init/` · `/card/bind/confirm/` · `/payment/create/` · `/payment/pre-apply/` · `/payment/apply/` · `DELETE /mobile/card/{id}/delete/` |
| Payme | `POST /mobile/payme/create-order/` · `GET /mobile/payme/order/{id}/` |
| Click | `POST /mobile/click/order-create/` · `POST /mobile/click/status/` |
| Uzum | `POST /mobile/orders/create/` · `GET /mobile/orders/{id}/status/` |
| Holat / tarix | `GET /mobile/payments/status/` · `GET /mobile/payments/list/` |

## E'lonlar → [`06-elonlar/`](06-elonlar/about.md)
| Amal | Endpoint |
|---|---|
| Tenant home + badge | `GET /mobile/announcements/tenant/home/` |
| Stories | `GET /mobile/stories/` · `POST /mobile/story/media/{id}/seen/` |
| Qidiruv/filtr | `GET /mobile/announcements/tenant/list/` · detail `GET /mobile/announcements/tenant/detail/{id}/` |
| Filtr opsiyalari | `GET /mobile/regions/` · `/category/list/` · `/property/{equipments,nearby-comforts}/list/` |
| Saqlangan filtr | `GET/POST /mobile/saved-filters/list/` · `/saved-filters/` · `PUT/DELETE …/{id}/` |
| Feed | `GET /mobile/announcements/reels/list/` · `POST …/reels/reaction/` |
| Xarita | `GET /mobile/map/locations/` |
| Favorites | `GET /mobile/wishlist/` · `GET /mobile/wishlist/update/?announcement_id=` |
| Yaratish (E1) | `POST /mobile/announcements/create/` · `POST /mobile/attachment/create/` (multipart) |
| Tashqi import | `POST /mobile/platform/link/` `{link}` |
| Tahrir/o'chirish (E2) | `PUT /mobile/announcements/update/{id}/` · `DELETE …/delete/{id}/` · lifecycle `POST /mobile/property/announcements/{id}/{archive|unarchive|paused|reserved}/` |
| Mulklarim | `GET /mobile/announcements/list/` |
| Statistika | `GET /mobile/announcements/{id}/stats/daily/` · `GET /mobile/homeowner/{property,financial}-statistics/` |
| Auditoriya | `GET /mobile/property/tenant-score/audience-count/` |

## So'rovlar → [`07-sorovlar/`](07-sorovlar/about.md)
| Amal | Endpoint |
|---|---|
| Ariza yaratish (R1) | `POST /mobile/rental-request/create/` `{property, announcement, text}` |
| Tenant ro'yxati | `GET /mobile/tenant/requests/list/?status=` · detail `GET /mobile/requests/detail/{id}/` |
| Landlord inbox (R2) | `GET /mobile/homeowner/requests/list/?tab=` |
| Landlord (mulk bo'yicha) | `GET /mobile/homeowner/rental-requests/list/?property=` |
| Holat o'zgartirish | `PATCH /mobile/requests/update/{id}/` `{status | report_status}` |
| Statistika | `GET /mobile/homeowner/requests/statistics/` |

## Chat → [`08-chat/`](08-chat/about.md)
WebSocket: `wss://…/ws/chat/?device_id=` (JWT `Sec-WebSocket-Protocol`). Actions: `chat_room_list`, `message`, `typing`, `read`, `message_history`, `delete_chat_room`. REST fallback: `GET /mobile/chat/list/`.

## Referens/sharh → [`09-referens-va-reviews/`](09-referens-va-reviews/about.md)
| Amal | Endpoint |
|---|---|
| Tenant reference | `POST /mobile/reference/create/?tenant_id=` · ⚠ `POST /admin/user/damage-photo/create/` · `GET /admin/user/{damage-type,complaint-type,contract-breach-type}/list/` |
| Recommendation | `GET /mobile/recommendation/list/` · `/detail/{id}/` · `POST …/attachments/create/` · `POST …/create/` |
| Oilaviy holat | `PATCH /mobile/marital-status/update/` · `POST /mobile/attachments/marital-status/` |
| Sharhlar | `GET /mobile/users/{userId}/reviews/` |

## Bildirishnoma → [`10-bildirishnoma/`](10-bildirishnoma/about.md)
`GET /mobile/notifications/list/` · `GET /mobile/notifications/{id}/` · `PATCH /mobile/notifications/{id}/` `{is_read}` · ⚠ `POST /mobile/notifications/mark-all-read/` (backendda yo'q)

## Support/xavfsizlik → [`11-support-va-xavfsizlik/`](11-support-va-xavfsizlik/about.md)
`/mobile/report-service/` · `GET /mobile/moderation/report-reasons/` · `POST /mobile/moderation/report/` · `POST /mobile/users/block/` · `DELETE /mobile/users/block/{id}/` · `GET /mobile/users/blocked/` · `GET /mobile/users/{id}/block-status/`

## Contract (💤 uyquda) → [`12-contract-dormant/`](12-contract-dormant/about.md)
`POST /mobile/contracts/create/` · `GET …/detail/{id}/` · `PUT …/update/{id}/` · `GET /mobile/homeowner/contract/list/` · `GET /mobile/tenant/contract/list/`

---
> ⚠ Nomlanish: skoring endpointlarida `rentmi`/`rentme` aralash; `tenant_reference` `/admin/` yo'lini ishlatadi (CLAUDE.md "faqat `/mobile/`" qoidasiga zid). Boshqa endpointlar `/mobile/` namespace'da.
