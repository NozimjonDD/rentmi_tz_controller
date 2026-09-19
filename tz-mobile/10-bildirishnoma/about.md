# 10 — Bildirishnomalar

Push va tizim ichidagi bildirishnomalarni yuborish hamda foydalanuvchi bildirishnoma sozlamalarini yuritish. TZ use-case: **N1** (push-bildirishnoma sozlamalarini boshqarish). Yetkazib berish FCM/APNs orqali; tizim ichida bildirishnomalar ro'yxati va detali ko'rsatiladi.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`push-fcm.md`](push-fcm.md) | FCM push, qurilma ro'yxati, ro'yxat/detal, deep-link | N1 (yetkazish) | ✅ |
| [`sozlamalar-n1.md`](sozlamalar-n1.md) | N1: bildirishnoma turlarini yoqish/o'chirish | N1 (boshqaruv) | ❌ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
backend event → FCM push ─┬─ foreground: iOS native / Android local notification
                          ├─ background tap → NotificationNavigator (deep-link)
                          └─ terminated tap → SharedPreferences (PENDING_NOTIFICATION_ROUTE)
                                              → splash/PIN dan keyin replay
tizim ichi: GET notifications/list/ → ro'yxat → detal (PATCH is_read)
```

## N1 bildirishnoma turlari (TZ)

- Yangi ijara so'rovi keldi (🏠 uy egasi).
- So'rov holati o'zgardi — tasdiqlandi / rad etildi / muhokama (👤 ijarachi).
- E'lon moderatsiya natijasi (🏠 uy egasi).
- Rentmi bali yangilandi — S1 muvaffaqiyatli bajarilgach (👤 ijarachi).
- Saqlangan filtr bo'yicha yangi e'lon (👤 ijarachi).
- **R5 qo'shdi:** «narxi tushdi» va «yangi e'lonlar» (saqlangan filtr/e'lon bo'yicha) push.

## Kod modullari

`lib/features/notifications` (ro'yxat/detal) · `lib/core/services/push_notification_service.dart` (FCM) · `device_registration_service.dart` (qurilma) · `notification_navigator.dart` (deep-link). N1 sozlama toggle'i (qisman): `lib/features/settings/presentation/pages/app_settings_page.dart`.

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Ro'yxat | `GET /mobile/notifications/list/` |
| Detal | `GET /mobile/notifications/{id}/` |
| O'qilgan deb belgilash | `PATCH /mobile/notifications/{id}/` — `{is_read}` |
| Hammasini o'qilgan | `POST /mobile/notifications/mark-all-read/` — ⚠ backend'da yo'q, jim tushadi |
| Qurilma ro'yxati (FCM) | `POST /mobile/device/register/` — `{fcm_token, device_id, name, device_type}` |

> ⚠ **Konflikt:** N1 asosiy funksiyasi — bildirishnoma **turlarini yoqish/o'chirish** — kodda amalga oshirilmagan (faqat bitta global, saqlanmaydigan toggle). Batafsil: [`sozlamalar-n1.md`](sozlamalar-n1.md), [`_konfliktlar.md`](../_konfliktlar.md).
