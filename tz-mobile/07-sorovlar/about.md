# 07 — So'rovlar (arizalar)

Ijarachi va uy egasi o'rtasidagi ijara so'rovlarini yuborish, ko'rib chiqish va holatini yuritish. TZ use-case'lari: **R1** (ijara so'rovini yuborish — ijarachi), **R2** (ijara so'rovini ko'rib chiqish — uy egasi). Kontakt ma'lumotlari faqat tasdiqlangach ochiladi; keyingi bosqich (elektron shartnoma) 3-bosqichda — [`12-contract-dormant/`](../12-contract-dormant/about.md).

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`tenant/`](tenant/about.md) | Ijarachi: ariza yuborish, o'z so'rovlari, statuslar, bekor qilish | R1 | 🟡 |
| [`landlord/`](landlord/about.md) | Uy egasi: kiruvchi so'rovlar, qaror, tenant skoring, SLA/statistika | R2 | 🟡 |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
IJARACHI                                    UY EGASI
e'lon detali → "Ariza jo'natish"
  → identifikatsiya tekshiruvi (yo'q → sheet)
  → Rentmi bali tekshiruvi (yo'q → S1 taklif)
  → so'rov formasi (⚠ faqat erkin matn)
  → POST rental-request/create/
      ──── push + tizim bildirishnoma ────▶  kiruvchi so'rovlar (tab: Yangi)
                                               → tenant skoring detali + xabar
  o'z so'rovlarim ◀─ status (pending/approved/rejected) ─ Qabul / Rad (PATCH status)
  bekor qilish (PATCH status:rejected)                    tasdiqlansa → kontakt ochiladi
```

> ⚠ **Kod TZ/R5 dan farq qiladi:** (1) so'rov formasida R5 tuzilgan maydonlari (kirish sanasi / byudjet / ijara muddati / to'lov kuni) **yo'q** — faqat erkin matn; (2) alohida "bekor qilingan" status yo'q — bekor qilish `rejected` ga o'tkazadi; (3) R5 markaziy **24 soatlik SLA countdown amalga oshirilmagan**. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md).

## TZ moduli (§4.2.1 — So'rovlar boshqaruvi)

- **Vazifasi:** ijara so'rovlarini yuborish, ko'rib chiqish va holatini yuritish, chat orqali muloqot.
- **Asosiy talablar:** so'rov yuborish uchun ijarachida Rentmi bali bo'lishi; ayni e'lon bo'yicha takroriy so'rov taqiqlanadi; **7 kun** ko'rib chiqilmagan so'rov avtomatik belgilanadi va uy egasiga bildirishnoma (R5 da → 24 soat, konflikt).

## Kod modullari

`lib/features/tenant_requests` (ijarachi) · `lib/features/landlord_requests` (uy egasi global inbox) · `lib/features/rental_requests` (bitta mulk bo'yicha so'rovlar).

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| So'rov yaratish (ijarachi) | `POST /mobile/rental-request/create/` — `{property, announcement, text}` |
| Ijarachi so'rovlari | `GET /mobile/tenant/requests/list/?status=` |
| So'rov detali | `GET /mobile/requests/detail/{id}/` |
| Holatni yangilash / bekor qilish | `PATCH /mobile/requests/update/{id}/` — `{status, announcement}` |
| Uy egasi kiruvchi so'rovlari | `GET /mobile/homeowner/requests/list/?tab=new\|approved\|rejected\|contracts` |
| Mulk bo'yicha so'rovlar | `GET /mobile/homeowner/rental-requests/list/?property=&status=` |
| To'liq hisobot so'rash / rozilik | `PATCH /mobile/requests/update/{id}/` — `{report_status}` |
