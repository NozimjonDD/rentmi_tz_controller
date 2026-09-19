# tz-mobile — «Rentmi» TZ, mobil flow'lar bo'yicha

Bu papka «Rentmi» axborot tizimining **Texnik Topshirig'i (TZ_07_07_2026)** ni, reliz user-storylari (R1–R5) va Release 5 spetsifikatsiyasini **mobil ilova oqimlari (flow)** bo'yicha qayta joylashtiradi. Maqsad — har bir ekran/qadam uchun **"talab qayerda yozilgan + kodda qayerda"** ni bir joyda ko'rsatish.

## Manbalar

| Belgi | Hujjat |
|---|---|
| **TZ** | `TZ_07_07_2026.docx` — rasmiy Texnik Topshiriq (O'z DSt 1986/1987:2018) |
| **R5** | `Release 5 17.08.2026.pdf` |
| **RELIZ** | `rentmi_tz_controller-mark.zip → reliz/…/about.md` (R1–R5 user-storylar) |
| **KOD** | `rentmi-mobile-main` (Flutter, `lib/features/…`) |

## Belgilar

- **Holat:** ✅ bajarilgan · 🟡 qisman · ❌ yo'q · 💤 o'chirilgan (kodda bor, faol emas)
- **Rol:** 👤 Ijarachi · 🏠 Uy egasi · 👥 Mehmon (guest)
- **⚠** — TZ ↔ kod yoki TZ ↔ reliz farqi (batafsil: [`_konfliktlar.md`](_konfliktlar.md))

## Flow'lar xaritasi

| # | Flow | TZ use-case | Rollar | Papka |
|---|---|---|---|---|
| 00 | Umumiy va kirish | US1–US3 | 👥👤🏠 | [`00-umumiy/`](00-umumiy/about.md) |
| 01 | Autentifikatsiya | U1, U2, U3 | 👤🏠👥 | [`01-auth/`](01-auth/about.md) |
| 02 | Identifikatsiya (MyID) | U5 | 👤🏠 | [`02-identifikatsiya/`](02-identifikatsiya/about.md) |
| 03 | Profil va sozlamalar | U4 | 👤🏠 | [`03-profil/`](03-profil/about.md) |
| 04 | Skoring (Rentmi bali) | S1, S2 | 👤 | [`04-skoring/`](04-skoring/about.md) |
| 05 | Billing / to'lovlar | B1 | 👤🏠 | [`05-billing/`](05-billing/about.md) |
| 06 | E'lonlar | E1, E2, E3 | 👤🏠👥 | [`06-elonlar/`](06-elonlar/about.md) |
| 07 | So'rovlar (arizalar) | R1, R2 | 👤🏠 | [`07-sorovlar/`](07-sorovlar/about.md) |
| 08 | Chat (aloqa) | (reliz R4) | 👤🏠 | [`08-chat/`](08-chat/about.md) |
| 09 | Referens va sharhlar | (reliz R3–R5) | 👤🏠 | [`09-referens-va-reviews/`](09-referens-va-reviews/about.md) |
| 10 | Bildirishnomalar | N1 | 👤🏠 | [`10-bildirishnoma/`](10-bildirishnoma/about.md) |
| 11 | Qo'llab-quvvatlash va xavfsizlik | T1 + UGC | 👤🏠👥 | [`11-support-va-xavfsizlik/`](11-support-va-xavfsizlik/about.md) |
| 12 | Elektron shartnoma (3-bosqich) | — | 👤🏠 | [`12-contract-dormant/`](12-contract-dormant/about.md) 💤 |

## Yordamchi fayllar (ildizda)

- [`_shablon.md`](_shablon.md) — har bir tugun `about.md` uchun standart shablon
- [`_status.md`](_status.md) — barcha tugunlar × holat (bajarilgan/qisman/yo'q) bitta jadvalda
- [`_endpointlar.md`](_endpointlar.md) — konsolidatsiyalangan backend API xaritasi (flow bo'yicha)
- [`_talablar.md`](_talablar.md) — funksional bo'lmagan (NFR) va umumiy TZ talablari (tezlik, xavfsizlik, tillar, ergonomika)
- [`_konfliktlar.md`](_konfliktlar.md) — TZ ↔ reliz/R5 ↔ kod ziddiyatlari

## Qamrov

Bu papka **faqat mobil ilova** oqimlarini qamraydi. TZ dagi web/admin use-case'lar (U2-veb, U2a, E4, E5, A1–A4, T2, T3) bu yerga kirmaydi — ular kelajakda alohida `tz-web/` da hujjatlanadi.

TZ dagi barcha mobil use-case'lar (U1–U5, S1, S2, B1, E1–E3, R1, R2, N1, T1) hamda funksional bo'lmagan talablar to'liq qamrab olingan — qamrov nazorati [`_status.md`](_status.md) da.
