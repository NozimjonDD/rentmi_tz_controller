# E'lonlar — Uy egasi tomoni

E'lonni **yaratish va boshqarish** oqimi: yangi e'lon yaratish, tashqi platformadan import, tahrirlash/o'chirish va lifecycle, «Mulklarim» statuslari hamda e'lon/dashboard statistikasi. TZ use-case'lari **E1** (yaratish) va **E2** (tahrir/o'chirish); R5-UE-04–06 yangi maydon va statuslar bilan to'ldiradi.

**TZ use-case:** E1 — E'lon yaratish · E2 — E'lonni tahrirlash yoki o'chirish · §4.2.1
**Rollar:** 🏠 Uy egasi (tizimga kirgan, identifikatsiyadan o'tgan, hisobi faol).

## Quyi tugunlar

| Tugun | Mazmun | TZ / R5 | Holat |
|---|---|---|---|
| [`elon-yaratish.md`](elon-yaratish.md) | Yangi e'lon: forma (5 tab), foto yuklash, moderatsiya | E1, R5-UE-06 | ✅ |
| [`tashqi-import.md`](tashqi-import.md) | Tashqi havoladan import (OLX/Uybor/Uysot/Joymee) | — (kod) | ✅ |
| [`elon-tahrir.md`](elon-tahrir.md) | Tahrirlash, o'chirish, lifecycle (arxiv/bron/pauza) | E2 | ✅ |
| [`mulklarim.md`](mulklarim.md) | Mening e'lonlarim + statuslar (qoralama/ijarada/bo'sh) | E2, R5-UE-05 | ✅ |
| [`statistika.md`](statistika.md) | E'lon statistikasi, dashboard analitikasi (7/30 kun) | R5-UE-04 | 🟡 |

## E1 → E2 umumiy oqim (kod)

```
Yangi e'lon: [ixtiyoriy] import (platform/link) → forma (5 tab)
   → foto: attachment/create (multipart, id oladi)
   → announcements/create (JSON, attachments_id[])
   → 'moderatsiya kutmoqda' → E4 (web, moderator) → faol

Mulklarim (announcements/list, status filtri):
   tahrir (update/{id}) · o'chirish (delete/{id}) · lifecycle (archive/unarchive/paused/reserved)
```

## E1 asosiy talablari (TZ)
- Foto: **kamida 3, ko'pi bilan 15 ta**.
- Joylashuv xarita xizmati orqali koordinatalari bilan saqlanadi.
- Jiddiy o'zgarish (joylashuv, mulk turi, maydon, xonalar) → qayta moderatsiya; narx o'zgarishi qayta moderatsiya talab qilmaydi.

## Vaqt reglamenti (TZ)
Forma yuklash ≤3 s · validatsiya ≤2 s · foto yuklash ≤15 s · saqlash ≤3 s · o'chirish ≤2 s.

## Kod modullari
`lib/features/listing` (yaratish/tahrir/import) · `lib/features/announcements` (o'chirish + lifecycle + statistika) · `lib/features/landlord_properties` (Mulklarim) · `lib/features/landlord_dashboard` (dashboard statistikasi).

## Konflikt / farqlar
- ⚠ Foto: TZ **max 15** talab qiladi, kodda faqat **min 3** tekshiriladi (`listing.dart:247`), maksimal chegara ko'rinmaydi. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ E'lon tahriri `listing` modulida, o'chirish/lifecycle esa `announcements` modulida — bir amal, ikki modul. → E-K7.
- ⚠ Dashboard «Daromadlarim / Xizmatlar» R5 da «Tez kunda» (raqamsiz). → statistika.md.
