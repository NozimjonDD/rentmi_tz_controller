# landlord — Uy egasi so'rovlari

**Rollar:** 🏠 Uy egasi    **Holat:** 🟡 Qisman
**TZ use-case:** R2 — Ijara so'rovini ko'rib chiqish · §4.2.1

## Quyi qadamlar

| Qadam | Fayl | TZ |
|---|---|---|
| Kiruvchi so'rovlarni ko'rib chiqish (qabul / rad) | [`korib-chiqish.md`](korib-chiqish.md) | R2 |
| Tenant skoring detali | [`tenant-skoring.md`](tenant-skoring.md) | R2 (3-qadam) |
| SLA countdown va statistika | [`sla-va-statistika.md`](sla-va-statistika.md) | R2 (9-qadam), R5-UE-02 |

## R2 to'liq bajarish tartibi (TZ)

1. Uy egasi 'Kiruvchi so'rovlar' bo'limini ochadi va e'lonlaridan birini tanlaydi.
2. Tizim so'rovlar ro'yxatini holati bo'yicha ko'rsatadi.
3. Uy egasi so'rovni tanlab tafsilotlarini ko'rib chiqadi (ijarachi ma'lumotlari, Rentmi bali va xulosa, so'rov xabari, chat).
4. Qaror: tasdiqlash / rad etish / **qo'shimcha savol berish**.
5. Tasdiqlash → 'tasdiqlangan', ijarachiga bildirishnoma + uy egasi kontakti ochiladi (mazkur TT shu yerda yakunlanadi).
6. Rad etish → sabab (ixtiyoriy), 'rad etildi', bildirishnoma.
7. Qo'shimcha savol → xabar, 'muhokama davom etmoqda'.
8. Qaror audit jurnaliga yoziladi.
9. Uy egasi so'rovlar bo'yicha statistika va tavsiyalarni ko'radi.

## Ikki inbox (kod)

- **Global inbox** — barcha e'lonlar bo'yicha, tab'lar bilan: `lib/features/landlord_requests`, `GET /mobile/homeowner/requests/list/?tab=new|approved|rejected|contracts`.
- **Bitta mulk bo'yicha** — `lib/features/rental_requests`, `GET /mobile/homeowner/rental-requests/list/?property=`.

## Kod joylashuvi
- **Modul:** `lib/features/landlord_requests` · `lib/features/rental_requests`
- **Sahifa / BLoC:** `LandlordRequestsOverviewPage`, `LandlordRequestsPage` / `LandlordRequestsBloc`; `RentalRequestsPage` / `RentalRequestsBloc`
- **Endpoint:** `GET /mobile/homeowner/requests/list/`, `GET /mobile/homeowner/rental-requests/list/`, `PATCH /mobile/requests/update/{id}/`

## Konflikt / farqlar
- ⚠ **"Muhokama" (qo'shimcha savol) amali yo'q** — kodda faqat Qabul / Rad; TZ 4-/7-qadamdagi 'muhokama davom etmoqda' holati amalga oshirilmagan.
- ⚠ **24 soatlik SLA countdown yo'q** (R5-UE-02 markaziy funksiyasi). → [`sla-va-statistika.md`](sla-va-statistika.md), [`_konfliktlar.md`](../../_konfliktlar.md).
