# Release 5 — user storylar (web: Admin)

Release 5 (17.08.2026) ning **admin panel** bo'yicha to'liq user-storylari. Manba: `R5 User storylar Admin.pdf`.

| Fayl | Rol | Storylar |
|---|---|---|
| [`admin.md`](admin.md) | 🛡 Administrator | R5-AD-01, R5-AD-02 (2) |

> Ijarachi/Uy egasi R5-storylari mobil — [`../../tz-mobile/_release5/`](../../tz-mobile/_release5/about.md) da.

## Story → flow xaritasi

| Story | Nomi | Flow | Kod |
|---|---|---|---|
| R5-AD-01 | Algoritm parametrlari sozlamalari | 03-administratorlik, 05-integratsiya | spec |
| R5-AD-02 | SLA monitoring | 06-support-callmarkaz | spec |

## Izoh
- **R5-AD-01** — R3 algoritm sozlamalari moduli kengaytmasi (Top og'irliklari, badge mezonlari, SLA muddati, javob vaqti parametrlari). Bu parametrlar **mobil** tarafdagi badge, skoring-mos, SLA countdown va javob vaqti indikatorini boshqaradi.
- **R5-AD-02** — so'rovlar monitoring bo'limiga SLA ko'rinishi (muddati o'tgan so'rovlar, uy egasi kesimida mediana javob vaqti).
- Web kodbaza yo'q → implementatsiya holati noma'lum (W-K1).
