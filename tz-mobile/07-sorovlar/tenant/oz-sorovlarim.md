# O'z so'rovlarim (statuslar + bekor qilish)

**Rollar:** 👤 Ijarachi    **Holat:** 🟡 Qisman

## TZ manbai
R1 (chiquvchi ma'lumotlar) — «Yangi ijara so'rovi yozuvi (noyob identifikator bilan)». Ijarachi o'z so'rovlari ro'yxatini va holatini ko'radi. TZ so'rovni ijarachi tomonidan bekor qilishni alohida use-case sifatida belgilamaydi — bekor qilish R5 da qo'shilgan.
> R1 holatlari TZ da: 'ko'rib chiqish kutmoqda' → 'tasdiqlangan' / 'rad etildi' / 'muhokama davom etmoqda'.

## Reliz / R5
- **RELIZ:** `IJ-R1` `R4` — so'rov yuborish va holat kuzatish.
- **R5 o'zgarishi:** `R5-IJ-10` — statuslar nomlanishi «ko'rilmoqda / kutilmoqda / qabul qilindi / rad etildi / **bekor qilingan**»; so'rovni **bekor qilish tugmasi** (faqat hali ko'rib chiqilmagan so'rovlar uchun); bekor qilingan so'rov ro'yxatda tegishli badge bilan.

## Bajarish tartibi (kod)
1. `GET /mobile/tenant/requests/list/?status=` — statuslar bo'yicha filtrlangan ro'yxat (pagination).
2. Kartada `TenantRequestStatusBadge` — holat pill'i.
3. Detal: `GET /mobile/requests/detail/{id}/` (bottom sheet).
4. Bekor qilish: `PATCH /mobile/requests/update/{id}/` `{status: 'rejected', announcement}`.
5. Uy egasi to'liq hisobot so'ragan bo'lsa: rozilik/rad — `PATCH …` `{report_status: 'approved' | 'rejected'}` (`full_report_consent_section`).

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachining so'rovlari **WHEN** ro'yxat ochiladi **THEN** har biri holat badge'i bilan ko'rinadi (matn backend'dan).
- **GIVEN** ko'rib chiqilmagan so'rov **WHEN** ijarachi bekor qiladi **THEN** `PATCH … {status:'rejected'}` yuboriladi.
- **GIVEN** uy egasi to'liq hisobot so'ragan **WHEN** ijarachi rozilik beradi **THEN** `report_status: 'approved'` yuboriladi.

## Kod joylashuvi
- **Modul:** `lib/features/tenant_requests`
- **Sahifa / BLoC:** `TenantRequestsPage` / `TenantRequestsBloc`; `tenant_request_status_badge`, `tenant_request_detail_bottom_sheet`, `full_report_consent_section`
- **Model:** `RequestStatus` enum — **3 qiymat** (`pending` / `approved` / `rejected`); ko'rinadigan matn backend `statusText` (Accept-Language) dan olinadi.
- **Endpoint:** `GET /mobile/tenant/requests/list/`, `GET /mobile/requests/detail/{id}/`, `PATCH /mobile/requests/update/{id}/`

## Konflikt / farqlar
- ⚠ **"Bekor qilingan" alohida status yo'q:** kodda bekor qilish `{status:'rejected'}` yuboradi — R5-IJ-10 talab qilgan alohida "bekor qilingan" holati/badge yo'q, u rad etilgan bilan bir xil ko'rinadi. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ Mijoz statusi 3 qiymat; R5 dagi 5 ta nomlanish (ko'rilmoqda/kutilmoqda/qabul/rad/bekor) faqat backend `statusText` orqali ajratilishi mumkin — mijoz mantig'i uni farqlamaydi.
