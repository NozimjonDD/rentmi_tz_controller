# tz-web — «Rentmi» TZ, web (admin panel) qismi

Bu papka «Rentmi» axborot tizimining **Texnik Topshirig'i (TZ_07_07_2026)** ning **web qismi quyi tizimi** (administrator, moderator, texnik qo'llab-quvvatlash, call-markaz uchun VueJS admin panel) qismini modul/ssenariy bo'yicha ajratadi. `tz-mobile/` ning juftligi.

## Manbalar

| Belgi | Hujjat |
|---|---|
| **TZ** | `TZ_07_07_2026.docx` — rasmiy Texnik Topshiriq (web use-case'lar §4.1.1.4, web modullar §4.2.2) |
| **R5** | `Release 5 17.08.2026.pdf` — admin panel qismi (algoritm parametrlari, SLA monitoring) |
| **RELIZ** | `reliz/…` — admin/moderator funksiyalari (cheklangan; admin panel bo'limi to'liq eksport qilinmagan) |
| **KOD** | ⚠ **Web (VueJS) kodbazasi taqdim etilmagan** — bu hujjat **spetsifikatsiya asosida**. Kod berilsa, "Backend/API" bo'limlari kod-mapping bilan to'ldiriladi. |

## Belgilar
- **Holat:** ✅ TZ da to'liq belgilangan · 🟡 qisman/aniqlanmagan · 💤 keyingi bosqich
- **Rol:** 🛡 Administrator (+superadmin) · 🔍 Moderator · 🎧 Call-markaz operatori · 🛠 Texnik qo'llab-quvvatlash
- **⚠** — TZ ichidagi yoki TZ↔reliz ziddiyati → [`_konfliktlar.md`](_konfliktlar.md)

## Modullar / flow'lar (§4.2.2)

| # | Modul (flow) | Web use-case'lar | Rollar | Papka |
|---|---|---|---|---|
| 01 | Autentifikatsiya | U2-veb, U2a | 🛡🔍🎧🛠 | [`01-autentifikatsiya/`](01-autentifikatsiya/about.md) |
| 02 | Moderatsiya | E4, E5 | 🔍 | [`02-moderatsiya/`](02-moderatsiya/about.md) |
| 03 | Administratorlik | A1, A2 | 🛡🛠 | [`03-administratorlik/`](03-administratorlik/about.md) |
| 04 | Billing nazorati | A4 | 🛡 | [`04-billing-nazorati/`](04-billing-nazorati/about.md) |
| 05 | Integratsiya boshqaruvi | A3 | 🛡 | [`05-integratsiya/`](05-integratsiya/about.md) |
| 06 | Texnik qo'llab-quvvatlash + call-markaz | T2, T3 | 🛠🎧 | [`06-support-callmarkaz/`](06-support-callmarkaz/about.md) |
| 07 | Rollar va RBAC | — (§4.1.3.2, §4.1.6) | barcha | [`07-rollar-va-rbac/`](07-rollar-va-rbac/about.md) |

## Yordamchi fayllar

- [`_shablon.md`](_shablon.md) — tugun `about.md` shabloni
- [`_status.md`](_status.md) — barcha web use-case'lar × holat
- [`_endpointlar.md`](_endpointlar.md) — kutilayotgan admin/backend API (TZ asosida)
- [`_talablar.md`](_talablar.md) — web-tegishli talablar (sessiya, RBAC, xavfsizlik, audit)
- [`_konfliktlar.md`](_konfliktlar.md) — web-tegishli ziddiyatlar
- [`_release5/`](_release5/about.md) — **Release 5 admin user-storylar** (R5-AD-01, R5-AD-02)

## Qamrov

Bu papka **web qismi quyi tizimini** to'liq qamraydi: **10 web use-case** (U2-veb, U2a, E4, E5, A1, A2, A3, A4, T2, T3) + **6 web modul** (§4.2.2) + web rollar/RBAC (§4.1.3.2, §4.1.6). Mobil oqimlar — [`../tz-mobile/`](../tz-mobile/README.md).

> Loyiha-darajasidagi TZ bo'limlari (1. administrativ, 5. bosqichlar, 6. qabul, 7. ishga tushirish, 8. hujjatlashtirish) — na mobil, na web use-case; ular TZ hujjatining o'zida qoladi. Qisqa ro'yxat: [`_status.md`](_status.md) §oxiri.
