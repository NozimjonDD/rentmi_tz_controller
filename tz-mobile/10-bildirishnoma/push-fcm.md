# Push (FCM) va tizim ichidagi bildirishnomalar

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
Bildirishnomalar moduli (§4.2.1) — «Push va tizim ichidagi bildirishnomalarni yuborish». N1 yetkazish tomoni: FCM/APNs orqali push, push o'chirilgan bo'lsa tizim ichidagi xabar ko'rsatiladi.
> «Push o'chirilgan bo'lsa tizim ichidagi xabar ko'rsatiladi.»

## Reliz / R5
- **RELIZ:** N1 yetkazib berish (FCM), tizim ichi ro'yxat.
- **R5 o'zgarishi:** `R5-IJ-11` — saqlangan filtr/e'lon bo'yicha «Narxi tushdi» va «Yangi e'lonlar» push (FCM) + tizim ichida; yangi bildirishnoma triggerlari backend'da.

## Bajarish tartibi (kod)
1. Ishga tushirishda `PushNotificationService.initialize()` — ruxsat so'raladi, Android kanal (`high_importance_channel`) yaratiladi, iOS foreground presentation yoqiladi.
2. Qurilma ro'yxati: `POST /mobile/device/register/` `{fcm_token, device_id, name, device_type}` (`DeviceRegistrationService`); login/guest holatiga qarab auth bilan yoki `postWithoutAuth`; resume/til o'zgarishi/token rotatsiyasida qayta ro'yxatdan o'tadi (debounce 5 s).
3. **Foreground:** iOS — tizim o'zi ko'rsatadi; Android — `flutter_local_notifications` orqali lokal banner.
4. **Background tap:** `onMessageOpenedApp` → `NotificationNavigator.navigateFromPushData`.
5. **Terminated tap:** `getInitialMessage` → `SharedPreferences` (`PENDING_NOTIFICATION_ROUTE`, `PENDING_NOTIFICATION_DATA`) → splash/PIN dan keyin `handlePendingNavigation` replay.
6. Tizim ichi: `GET /mobile/notifications/list/` → ro'yxat; `GET /mobile/notifications/{id}/` → detal; `PATCH /mobile/notifications/{id}/` `{is_read:true}`.

## Deep-link (route) turlari
- Mijoz route'lari (`NotificationRouteTypes`): `chat_list/detail`, `tenant_requests(_detail)`, `landlord_requests(_detail)`, `announcements_list`, `announcement_detail`, `scoring`, `identification`, `favorites`, `notifications`.
- Backend literal route'lari: `requests/detail/<pk>/` (so'rov holati / REPORT_* — rolga qarab tenant/landlord), `homeowner/requests/list/` (yangi so'rov → uy egasi), `announcements/list/` (moderatsiya natijasi), `announcements/tenant/detail/<pk>/` (saqlangan filtr mosligi), `contracts/detail/<pk>/` (uyqudagi shartnoma → so'rovlar sahifasi).

## Qabul kriteriyalari (BDD)
- **GIVEN** ilova foreground'da (Android) **WHEN** push keladi **THEN** lokal banner ko'rsatiladi.
- **GIVEN** ilova yopiq **WHEN** push bosiladi **THEN** route saqlanadi va PIN'dan keyin tegishli ekran ochiladi.
- **GIVEN** so'rov holati push'i **WHEN** bosiladi **THEN** rolga qarab tenant yoki landlord so'rovlar sahifasi ochiladi.

## Kod joylashuvi
- **Servislar:** `lib/core/services/push_notification_service.dart`, `device_registration_service.dart`, `device_id_service.dart`, `notification_navigator.dart`
- **Modul:** `lib/features/notifications` — `NotificationsPage`, `NotificationDetailPage` / `NotificationsBloc`
- **Endpoint:** `GET /mobile/notifications/list/`, `GET /mobile/notifications/{id}/`, `PATCH /mobile/notifications/{id}/`, `POST /mobile/device/register/`
- **Maxfiylik:** FCM payload log'ga yozilmaydi (PII bo'lishi mumkin) — faqat metadata.

## Konflikt / farqlar
- ⚠ **`mark-all-read` backend'da yo'q:** `POST /mobile/notifications/mark-all-read/` — endpoint mavjud emas, chaqiruv jim tushadi (kod izohi bilan belgilangan). → [`_konfliktlar.md`](../_konfliktlar.md).
- Push ruxsati o'chirilgan holatda tizim ichi ro'yxat ishlaydi (TZ talabiga mos).
