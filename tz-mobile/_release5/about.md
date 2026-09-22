# Release 5 — user storylar (mobil: Ijarachi + Uy egasi)

Release 5 (17.08.2026) ning **to'liq (boricha) user-storylari**, rol bo'yicha. Manba: `R5 User storylar Ijarachi.pdf`, `R5 User storylar Uy egasi.pdf`. Har story flow'ga bog'langan va kod holati bilan.

| Fayl | Rol | Storylar |
|---|---|---|
| [`ijarachi.md`](ijarachi.md) | 👤 Ijarachi | R5-IJ-01 … R5-IJ-11 (11) |
| [`uy-egasi.md`](uy-egasi.md) | 🏠 Uy egasi | R5-UE-01 … R5-UE-06 (6) |

> Admin R5-storylari (R5-AD-01, R5-AD-02) mobil emas — [`../../tz-web/_release5/`](../../tz-web/_release5/about.md) da.

## Story → flow xaritasi (17 mobil story)

| Story | Nomi | Flow | Kod |
|---|---|---|---|
| R5-IJ-01 | Yangilangan asosiy sahifa | 06-elonlar/tenant/asosiy-sahifa, 00-umumiy/navigatsiya | 🟡 |
| R5-IJ-02 | Skoring-mos uylar | 06-elonlar/tenant/asosiy-sahifa, 04-skoring | 🟡 |
| R5-IJ-03 | Badge'lar tizimi | 06-elonlar/tenant/asosiy-sahifa, elon-detail | 🟡 |
| R5-IJ-04 | Filter yangilanishi | 06-elonlar/tenant/qidiruv-filtr | ✅ |
| R5-IJ-05 | Saqlanganlar | 06-elonlar/tenant/favorites | ✅ |
| R5-IJ-06 | Xarita | 06-elonlar/tenant/xarita | ✅ |
| R5-IJ-07 | E'lon detail | 06-elonlar/tenant/elon-detail | ✅ |
| R5-IJ-08 | Uy egasi ommaviy profili | 06-elonlar/tenant/uy-egasi-profil | ❌ |
| R5-IJ-09 | So'rov formasi maydonlar | 07-sorovlar/tenant/ariza-yuborish | ❌ |
| R5-IJ-10 | So'rov statuslari / bekor | 07-sorovlar/tenant/oz-sorovlarim | 🟡 |
| R5-IJ-11 | Narx/yangi e'lon push | 10-bildirishnoma | 🟡 |
| R5-UE-01 | So'rovlar sahifasi | 07-sorovlar/landlord/korib-chiqish | 🟡 |
| R5-UE-02 | SLA 24 soat countdown | 07-sorovlar/landlord/sla-va-statistika | ❌ |
| R5-UE-03 | Javob vaqti indikatori | 07-sorovlar/landlord, uy-egasi-profil | ❌ |
| R5-UE-04 | Analitika + "Tez kunda" | 06-elonlar/landlord/statistika | 🟡 |
| R5-UE-05 | "Mulklarim" statuslari | 06-elonlar/landlord/mulklarim | 🟡 |
| R5-UE-06 | E'lon formasi maydonlar | 06-elonlar/landlord/elon-yaratish | 🟡 |

## R5 ichidagi ziddiyat (yangi aniqlangan)
- ⚠ **Countdown qizil chegarasi:** batafsil story (R5-UE-02) «**1 soatdan** kam» deydi; `Release 5 17.08.2026.pdf` xulosasi «**7 soatdan** kam» deydi. Ikkalasi R5 — o'zaro zid. → [`_konfliktlar.md`](../_konfliktlar.md) C-R5-1.

## Umumiy holat
17 mobil story: ✅ 4 · 🟡 9 · ❌ 4. Amalga oshirilmagan (❌): R5-IJ-08 (uy egasi profil), R5-IJ-09 (so'rov formasi maydonlar), R5-UE-02 (SLA countdown), R5-UE-03 (javob vaqti indikatori). Batafsil: [`../_status.md`](../_status.md).
