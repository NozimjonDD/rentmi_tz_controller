# tenant — Ijarachi so'rovlari

**Rollar:** 👤 Ijarachi    **Holat:** 🟡 Qisman
**TZ use-case:** R1 — Ijara so'rovini yuborish · §4.2.1

## Quyi qadamlar

| Qadam | Fayl | TZ |
|---|---|---|
| Ariza yuborish | [`ariza-yuborish.md`](ariza-yuborish.md) | R1 (1–7 qadam) |
| O'z so'rovlarim (statuslar + bekor qilish) | [`oz-sorovlarim.md`](oz-sorovlarim.md) | R1 (chiquvchi holat) |

## R1 to'liq bajarish tartibi (TZ)

1. Ijarachi e'lon tafsilotlarida 'So'rov yuborish'ni tanlaydi.
2. Tizim so'rov formasini ko'rsatadi (qo'shimcha savol/ma'lumotlar; uy egasi bilan chat imkoniyati).
3. Ijarachi ma'lumotlarni kiritadi.
4. Tizim Rentmi balini tekshiradi; ball mavjud bo'lmasa → S1 (Rentmi hisobotini xarid qilish) taklif qilinadi.
5. So'rov 'ko'rib chiqish kutmoqda' holatida saqlanadi.
6. Uy egasiga push + tizim ichidagi bildirishnoma yuboriladi.
7. Ijarachiga so'rov yuborilganligi haqida tasdiq ko'rsatiladi.

## Kengaytmalar (TZ)
- Ayni e'lon bo'yicha takroriy so'rov mavjud → yangi so'rov taqiqlanadi, mavjud holatni ko'rish taklif qilinadi.
- Ijarachi blacklist'da → so'rov taqiqlanadi.
- E'lon yuborish paytida nofaol bo'lib qolsa → ijarachiga xabar, so'rov bekor qilinadi.

## Kod joylashuvi
- **Modul:** `lib/features/tenant_requests`
- **Sahifa / BLoC:** `TenantRequestsPage` / `TenantRequestsBloc`; so'rov formasi `RentalRequestDialog` (bottom sheet)
- **Endpoint:** `POST /mobile/rental-request/create/`, `GET /mobile/tenant/requests/list/`, `GET /mobile/requests/detail/{id}/`, `PATCH /mobile/requests/update/{id}/`

## Konflikt / farqlar
- ⚠ So'rov formasi TZ "kiruvchi ma'lumotlar" (kirish sanasi, byudjet, ijara muddati) va R5 tuzilgan maydonlarini **to'plamaydi** — faqat erkin matn. → [`_konfliktlar.md`](../../_konfliktlar.md).
