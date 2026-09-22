# 06 — E'lonlar (E'lonlar boshqaruvi)

Ijaraga beriladigan ko'chmas mulk obyektlari bo'yicha e'lonlarni yaratish, tahrirlash, qidirish va filtrlash. TZ use-case'lari: **E1** (e'lon yaratish), **E2** (tahrirlash / o'chirish), **E3** (qidirish / filtrlash). Modul TZ §4.2.1 da tavsiflangan. R5 shu domenning asosiy qismini qayta quradi: badge'lar tizimi, skoring-mos uylar, xarita, uy egasi ommaviy profili, filter yangilanishi.

## Ikki tomon

E'lonlar oqimi ikki rol atrofida bo'linadi — **ijarachi/mehmon** (iste'mol) va **uy egasi** (yaratish/boshqaruv):

| Tomon | Mazmun | TZ | Papka |
|---|---|---|---|
| 👤👥 **Tenant** | Katalog, qidiruv/filtr, xarita, lenta, saqlanganlar, e'lon detali, uy egasi profili | E3 | [`tenant/`](tenant/about.md) |
| 🏠 **Landlord** | E'lon yaratish, tahrir/o'chirish, tashqi import, mulklarim, statistika | E1, E2 | [`landlord/`](landlord/about.md) |

## Quyi tugunlar

### 👤👥 Tenant (`tenant/`)

| Tugun | Mazmun | TZ / R5 | Holat |
|---|---|---|---|
| [`asosiy-sahifa.md`](tenant/asosiy-sahifa.md) | Home: bo'limlar, badge'lar, skoring-mos uylar, stories | reliz IJ-01/IJ-02, R5-IJ-01–03 | ✅ |
| [`qidiruv-filtr.md`](tenant/qidiruv-filtr.md) | E'lon qidiruvi, ko'p mezonli filtr, saqlangan filtrlar | E3, R5-IJ-04/05 | ✅ |
| [`xarita.md`](tenant/xarita.md) | Xarita orqali qidirish (pin, klaster, bottom sheet) | E3, R5-IJ-06 | ✅ |
| [`feed.md`](tenant/feed.md) | Lenta (reels) — vertikal e'lonlar oqimi, like/dislike | (reliz kengaytmasi) | ✅ |
| [`favorites.md`](tenant/favorites.md) | Saqlangan uylar (wishlist) | E3 (saqlash) | ✅ |
| [`elon-detail.md`](tenant/elon-detail.md) | E'lon tafsiloti, badge'lar, Ko'rildi/Ariza statistikasi | E3 (detail), R5-IJ-07 | ✅ |
| [`uy-egasi-profil.md`](tenant/uy-egasi-profil.md) | Uy egasi ommaviy profili (Tasdiqlangan, javob vaqti) | R5-IJ-08 | ❌ |

### 🏠 Landlord (`landlord/`)

| Tugun | Mazmun | TZ / R5 | Holat |
|---|---|---|---|
| [`elon-yaratish.md`](landlord/elon-yaratish.md) | Yangi e'lon yaratish (forma, foto, moderatsiya) | E1, R5-UE-06 | ✅ |
| [`elon-tahrir.md`](landlord/elon-tahrir.md) | Tahrirlash, o'chirish, lifecycle (arxiv/bron/pauza) | E2 | ✅ |
| [`tashqi-import.md`](landlord/tashqi-import.md) | Tashqi platforma havolasidan import (OLX/Uybor/…) | — (kod) | ✅ |
| [`mulklarim.md`](landlord/mulklarim.md) | Mening e'lonlarim + statuslar (qoralama/ijarada/bo'sh) | E2, R5-UE-05 | ✅ |
| [`statistika.md`](landlord/statistika.md) | E'lon statistikasi, uy egasi analitikasi (7/30 kun) | R5-UE-04 | 🟡 |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
👤 IJARACHI:  home (tenant/home) → katalog (tenant/list, filtr) → detail (tenant/detail)
                 ↘ xarita (map/locations)   ↘ lenta (reels/list)   ↘ saqlanganlar (wishlist)
                 → ariza (R1 · 07-sorovlar)

🏠 UY EGASI:  yangi e'lon (attachment/create → announcements/create) → moderatsiya (E4, web)
                 → Mulklarim (announcements/list, status) → tahrir/o'chirish/lifecycle
                 → statistika (stats/daily, homeowner/*-statistics)
```

> ⚠ **Ikki katalog endpointi (E-K8):** ijarachi katalogi `GET /mobile/announcements/tenant/list/` (+ `tenant/detail/{id}/`), uy egasi «Mulklarim» esa `GET /mobile/announcements/list/` (status filtri bilan) — bir domen, ikki xil ro'yxat kontrakti. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md).

## Kod modullari

| Modul | Vazifasi | Asosiy BLoC/Cubit |
|---|---|---|
| `lib/features/tenant_dashboard` | Ijarachi asosiy sahifasi, badge'lar, stories, skoring | `TenantHomeBloc`, `TenantScoreCubit`, `TenantStoriesCubit` |
| `lib/features/announcements` | Katalog, filtr, saqlangan filtr, e'lon detali, statistika | `AnnouncementsBloc`, `AnnouncementDetailBloc`, `FilterCubit`, `FilterSessionCubit`, `AnnouncementStatsBloc` |
| `lib/features/map` | Xarita orqali qidirish | `MapCubit` |
| `lib/features/feed` | Lenta (reels) | `FeedBloc` |
| `lib/features/favorites` | Saqlangan uylar (wishlist) | `FavoritesBloc` |
| `lib/features/blocks` | E'lon/uy egasini bloklash | `BlockActionCubit`, `BlockedUsersBloc` |
| `lib/features/listing` | E'lon yaratish/tahrirlash, tashqi import | `ListingBloc` |
| `lib/features/landlord_properties` | Mening e'lonlarim (statuslar) | `LandlordPropertiesBloc` |
| `lib/features/landlord_dashboard` | Uy egasi dashboard statistikasi | `DashboardBloc` |

## Asosiy talablar (TZ §4.2.1)

- Har bir e'lon **kamida 3 ta, ko'pi bilan 15 ta** fotosuratga ega bo'lishi (kodda min 3 tekshiriladi — `listing.dart:247`).
- Yangi va **jiddiy tahrirlangan** e'lonlar moderatsiyadan o'tadi (E4 — web/admin, bu yerga kirmaydi).
- Obyekt joylashuvi xarita xizmati orqali koordinatalari bilan saqlanadi.
- Faqat **faol (moderatsiyadan o'tgan)** e'lonlar katalogda ko'rsatiladi.

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Ijarachi katalogi (E3) | `GET /mobile/announcements/tenant/list/` (filtr param) |
| Ijarachi asosiy sahifasi | `GET /mobile/announcements/tenant/home/` (badge'lar shu yerdan) |
| E'lon detali (ijarachi) | `GET /mobile/announcements/tenant/detail/{id}/` |
| Xarita | `GET /mobile/map/locations/` (zoom, ne/sw, filtr) |
| Lenta | `GET /mobile/announcements/reels/list/`, `POST …/reels/reaction/` |
| Saqlangan uylar | `GET /mobile/wishlist/`, `GET /mobile/wishlist/update/?announcement_id=` |
| Saqlangan filtrlar | `GET/POST /mobile/saved-filters/list/`, `/saved-filters/`, `…/update/{id}/`, `…/delete/{id}/` |
| E'lon yaratish (E1) | `POST /mobile/attachment/create/` → `POST /mobile/announcements/create/` |
| Tashqi import | `POST /mobile/platform/link/` `{link}` |
| Tahrir / o'chirish (E2) | `PUT /mobile/announcements/update/{id}/`, `DELETE /mobile/announcements/delete/{id}/` |
| Lifecycle | `POST /mobile/property/announcements/{id}/{archive\|unarchive\|paused\|reserved}/` |
| Mulklarim | `GET /mobile/announcements/list/` (status filtri) |
| E'lon statistikasi | `GET /mobile/announcements/{id}/stats/daily/?days=` |
| Uy egasi dashboard | `GET /mobile/homeowner/property-statistics/`, `/financial-statistics/` |

## Konflikt / farqlar (domen bo'yicha)

Barcha tafsilotlar: [`_konfliktlar.md`](../_konfliktlar.md).

- ⚠ **E-K1 — Badge'lar manbai:** R5 badge'lar (*Sizga mos / Top / Narxi tushdi*) faqat `tenant/home/` javobida keladi; `announcements` entity'sida bu maydonlar yo'q (`tenant_announcement_model.dart` da faqat `is_favorited`). "Tekshirilgan" = backend `moderated_status`, spec pill (xona/m²/qavat) = frontend.
- ⚠ **E-K2 — Stories:** R5 «Actual History stories mobil ilovada yashiriladi (kod saqlanadi)» deydi, ammo kodda stories faol (`GET /mobile/stories/`, `tenant_stories_cubit.dart`).
- ⚠ **E-K3 — Saqlangan filtrlar Clean Arch chetlab:** `FilterSessionCubit` `DioClient` ni to'g'ridan-to'g'ri chaqiradi (repository/usecase qatlamisiz).
- ⚠ **E-K4 — Favorites GET-mutatsiya:** wishlist o'zgarishi `GET /mobile/wishlist/update/` orqali (POST/DELETE emas).
- ⚠ **E-K5 — rooms/pets faqat frontend:** filtrda `rooms_min/rooms_max/pets` yuboriladi, lekin backend spec kutilmoqda (`announcement_filter.dart:381`).
- ⚠ **E-K6 — Uy egasi ommaviy profili yo'q:** R5-IJ-08 talab qiladi, kodda faqat `ownerName`/`ownerUserId` bor, alohida profil ekrani/endpointi yo'q.
- ⚠ **E-K7 — E2 amali ikki modulda:** e'lon tahriri `lib/features/listing` da, o'chirish/lifecycle esa `lib/features/announcements` da — bitta use-case, ikki modul.
- ⚠ **E-K8 — Ikki katalog endpointi:** ijarachi `…/tenant/list/` ↔ uy egasi `…/list/` (status filtri) — turli ro'yxat kontrakti.
- ⚠ **Foto maksimal chegara:** TZ max 15 talab qiladi, kodda faqat min 3 tekshiriladi (`listing.dart:247`).
- ⚠ **Mulklarim statuslari:** R5-UE-05 (qoralama/ijarada/bo'sh) ↔ kod `OwnerPropertyStatus{draft,readyToPublish,active}` + `OwnerPropertyVacancy{vacant,occupied}`.
