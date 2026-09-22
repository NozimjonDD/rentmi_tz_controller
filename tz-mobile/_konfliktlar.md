# Konfliktlar va farqlar

Uch xil: **(1) TZ ↔ reliz/R5** (spetsifikatsiyalar orasida), **(2) Kod ↔ spetsifikatsiya** (kod hujjatdan chetlashgan), **(3) Kod ichidagi texnik qarz**. Har bir `about.md` shu yerdagi ID'larga havola qiladi.

To'liq spec-tahlil (web use-case'lar bilan): loyiha ildizidagi `TZ_konflikt_report.html` / `.md`.

---

## 1. TZ ↔ reliz / R5 (spetsifikatsiyalar orasida)

| ID | Mavzu | TZ | Reliz / R5 | Tegishli flow |
|---|---|---|---|---|
| **C1** | OTP amal muddati | **5 daqiqa** (U1/U3) | **1 daqiqa** (US4) | [01-auth](01-auth/02-register/telefon-otp.md) |
| **C2** | OTP/PIN xato urinishlar | **3 → 10 daq** (§4.1.6.2) | **5 → 5 daq** (US4) | [01-auth](01-auth/04-pincode/about.md) |
| **C3** | So'rov SLA muddati | **7 kun** (R2) | **24 soat** (R5) — R5 o'zi "hujjatlar nomuvofiqligi" deb tan olgan | [07-sorovlar](07-sorovlar/landlord/about.md) |
| **C4** | Skoring amal muddati | belgilanmagan | R1 "muddatsiz" ↔ R4 "muddati o'tadi"; aniq qiymat **hech qayerda yo'q** | [04-skoring](04-skoring/about.md) |
| **C5** | Guest stories | — | R3 ko'rsatadi ↔ R5 yashiradi | [06-elonlar](06-elonlar/tenant/asosiy-sahifa.md) |
| **C6** | Skoring modeli | "past/o'rtacha/yuqori" | R5 "GREEN/YELLOW/RED + hard-reject + affordability" | [04-skoring](04-skoring/about.md) |
| **C7** | Atama | "ko'chib kelish sanasi", "so'rov" | R5 "kirish sanasi", "ariza", "bron" | 06/07 |
| **C-R5-1** | Countdown qizil chegarasi (R5 ichida zid) | R5 batafsil story (R5-UE-02): **1 soatdan** kam qolganda qizil | `Release 5 …pdf` xulosasi: **7 soatdan** kam | [_release5](_release5/about.md) |
| **A2** | Skoring shakllantirish vaqti | §4.1.4.1 "5 daqiqa" ↔ S1 "≤2 daqiqa" (TZ ichida) | — | [04-skoring](04-skoring/about.md) |
| **A5** | Bir vaqtdagi FU / SLA qamrovi | §4.1.3.1 "1000–5000" ↔ SLA faqat 1000 da | — | [_talablar](_talablar.md) |
| **A1** | Hisobot vaqti (asosan web A2) | §4.1.4.1 "10 s" ↔ A2 "30 s" | — | web (ma'lumot uchun) |
| **B4** | Rol o'zgartirish | §4.2.1 modul va'da qiladi ↔ U4 use-case qamramaydi | reliz US4 "settings orqali" | [01-auth](01-auth/01-rol-tanlash/about.md), [03-profil](03-profil/rol-almashtirish.md) |

---

## 2. Kod ↔ spetsifikatsiya (kod hujjatdan chetlashgan)

| ID | Mavzu | Spetsifikatsiya | Kodda |
|---|---|---|---|
| **K1** | Onboarding oqimi | TZ: rol → telefon → OTP → PIN → MyID → skoring (majburiy) | **Guest-first**: rol majburiy emas; login'dan keyin faqat PIN→MyID→dashboard; skoring/kadastr talab bo'yicha |
| **K2** | Pastki navbar | R5: Main/**Saved**/Lenta/So'rovlar/Profil | **"Saved" tab yo'q**; landlord: Portfelim/Chat/So'rovlar/Profil/+Add; tenant: Home/Chat/Lenta/So'rovlar/Filter |
| **K3** | So'rov SLA countdown | R5: 24 soat countdown, "javob berishingiz kerak HH:MM:SS", 7 soatda qizil | **Kodda umuman yo'q** — faqat Qabul/Rad, taymer yo'q |
| **K4** | Ariza formasi | R5: kirish sanasi, byudjet, muddat, to'lov kuni | **Faqat erkin matn** (`{property, announcement, text}`) |
| **K5** | "Bekor qilingan" status | R5: alohida status | **`status:'rejected'`** (bekor = rad) |
| **K6** | Guest stories | R5: yashiriladi | Kodda `tenant_stories` **faol** (`/stories/`) |
| **K7** | Support | TZ T1: tizim ichi murojaat (ticket) | `support` = **statik kontakt sahifasi**; ticket = `report_service` |
| **K8** | `/admin/` yo'l | CLAUDE.md: "faqat `/mobile/`" | `tenant_reference` `/admin/user/damage-photo/…` va lookuplarni chaqiradi |
| **K9** | Skoring band manbai | CLAUDE.md: `/score-band` endpoint + `fromScore()` | Band **inline** keladi (`ScoreBand.fromString`); alohida endpoint yo'q |
| **K10** | mark-all-read | — | `POST /mobile/notifications/mark-all-read/` backendda yo'q (jim tushadi) |
| **K12** | PIN xesh algoritmi | TZ: bcrypt/Argon2 | **PBKDF2-HMAC-SHA256** (funksional mos, algoritm boshqa) |

---

## 3. Kod ichidagi texnik qarz / mock'lar

| ID | Joy | Muammo |
|---|---|---|
| **K11a** | `landlord_requests` statistika | Dinamika grafigi + tile'lar **mock** (backend endpoint yo'q) |
| **K11b** | `auth_local_data_source` | `getCachedUser()` **soxta user** qaytaradi |
| **K11c** | `settings/EditPersonalInfoCubit` | Mock (deps yo'q, sahifada yaratiladi) |
| **K11d** | `favorites` | `isFavorite()` = `false` stub; toggle **GET orqali mutatsiya** |
| **K11e** | `listing` | `getListing/getUserListings/deleteListing` = `UnimplementedError` |
| **K11f** | `announcements/filter_session_cubit` | Saqlangan filtrlar Clean Arch'ni chetlab, DioClient'ni to'g'ridan-to'g'ri chaqiradi |
| **K11g** | `feed` | Reaksiyalar fire-and-forget (xatolik ishlovi/rollback yo'q) |
| **K11h** | filtr `rooms`/`pets` | Faqat frontend (backend spec kutilmoqda) |
| **K13a** | Nomlanish | Paket `uzrentme` ↔ mahsulot `rentmi`; skoring endpointlarida `rentmi`/`rentme` aralash |
| **K13b** | Xavfsizlik | Android keystore git tarixida; App Store auditi 7 CRITICAL + 7 HIGH |

---

## 4. Billing / chat / referens konfliktlari (flow 05, 08, 09)

| ID | Mavzu | Tafsilot |
|---|---|---|
| **B5** | Pro/obuna — legacy shim | `ProStatus/SubscriptionPlan{lite,pro}` saqlangan, lekin gating faqat `paid Order`; `/subscription/status|activate|cancel` kodda **yo'q**; to'lov hozircha simulyatsiya (`TODO_SUBSCRIPTION.md`). |
| **B6** | Obuna darajasi/narx belgilanmagan | TZ lite/pro yoki narxlash siyosatini rasmiy belgilamaydi; kod bir martalik `Order` amount modelidan foydalanadi. B1 1-bosqichda faqat `rentmeReport` tranzaksiyasi keladi (kommunal/ijara — 2–3-bosqich). |
| **B7** | Chat REST oqim yo'q | send/history/markAsRead REST metodlari 404/405 → olib tashlangan; faqat `GET /mobile/chat/list/` (pre-connect fallback). Ilova-darajasidagi ping/pong o'chirilgan. |
| **B8** | Chat SLA yo'q | R5 «Javob berishingiz kerak: HH:MM:SS» taymeri chatga emas, faqat so'rovlar boshqaruviga (07) tegishli — chat'da countdown yo'q. |
| **B9** | `/admin/` yo'l (tenant_reference) | lookup + damage-photo `/admin/user/...` ostida — CLAUDE.md «never `/admin/`» (Phase 3) qoidasiga zid; lug'atlar `IsAdmin` sabab 401/403 bo'lishi mumkin (wizard text-only rejimga tushadi). |
| **B10** | Sharhlar faqat o'qish | sharh yozish/yaratish endpointi kodda yo'q (faqat `GET .../reviews/`); reyting bloki R5 buildida yashirilgan (RelizF). |
| **B11** | Referens/tavsiya/oilaviy — qisman | TZ S1 (12/15-qadam) qisqa eslatadi; **farzandlar/daromad strukturalangan maydonlari kodda yo'q** (faqat oilaviy holat bool + fayllar). Referens/tavsiya alohida TZ use-case emas — reliz/kod qo'shgan. |

## 5. E'lonlar konfliktlari (flow 06)

| ID | Mavzu | Tafsilot |
|---|---|---|
| **E-K1** | Badge manbai | R5 *Sizga mos/Top/Narxi tushdi* faqat `tenant/home/` javobida; katalog entity'sida yo'q. "Tekshirilgan" = backend `moderated_status`; spec pill (xona/m²/qavat) = frontend; `is_favorited` = backend. |
| **E-K2** | Stories | R5 «Actual History yashiriladi (kod saqlanadi)» ↔ kodda faol (`GET /mobile/stories/`, `tenant_stories_cubit`). |
| **E-K3** | Saqlangan filtr Clean Arch chetlab | `FilterSessionCubit` `DioClient` ni to'g'ridan-to'g'ri chaqiradi (repository/usecase qatlamisiz). |
| **E-K4** | Favorites GET-mutatsiya | wishlist o'zgarishi `GET /mobile/wishlist/update/` orqali (POST/DELETE emas) — REST semantikasiga zid. |
| **E-K5** | rooms/pets frontend-only | filtr `rooms_min/rooms_max/pets` yuboradi, backend spec kutilmoqda (`announcement_filter.dart`). |
| **E-K6** | Uy egasi ommaviy profili yo'q | R5-IJ-08 talab qiladi; kodda faqat `ownerName/ownerUserId`, alohida ekran/endpoint yo'q (❌). |
| **E-K7** | E2 amali ikki modulda | e'lon tahriri `lib/features/listing`, o'chirish/lifecycle `lib/features/announcements` — bitta use-case, ikki modul. |
| **E-K8** | Ikki katalog endpointi | ijarachi `…/tenant/list/` ↔ uy egasi «Mulklarim» `…/list/` (status filtri) — turli ro'yxat kontrakti. |
| **E-K9** | Tashqi import platformalari | kodda **OLX / Uybor / Joyme** (`joyme.uz`); TZ mapping'dagi "Uysot/Joymee" kodda yo'q. |
| **E-K10** | "Mulklarim" statuslari + foto | kod `{draft, readyToPublish, active}` + `{vacant, occupied}` — R5 «qoralama/ijarada/bo'sh» ga to'liq mos emas; foto **max-15 chegara kodda tekshirilmaydi** (faqat min-3). |

## Umumiy tavsiya

1. **Parametrlashtirish:** SLA soati, OTP muddati/urinishlar, skoring muddati/narxi — admin sozlamasiga chiqarish (C1–C4, K3).
2. **TZ ni R5 qarorlari bilan sinxronlash** (rasmiy dopolneniye): C3, C4, K1, K2.
3. **Mock/stub'larni backend tayyor bo'lgach real qilish** (K11-guruh).
4. **`/admin/` yo'llarni `/mobile/` ga ko'chirish** (K8).
