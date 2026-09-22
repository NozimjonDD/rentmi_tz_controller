# Mening e'lonlarim (Mulklarim)

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
E2 — E'lonni tahrirlash yoki o'chirish · §4.2.1 (1-qadam). "Mening e'lonlarim" — uy egasining barcha e'lonlari ro'yxati; bu yerdan e'lon tanlanadi va E2 amallari (tahrir/faol-nofaol/o'chirish) bajariladi.
> «Uy egasi 'Mening e'lonlarim' bo'limidan e'lonni tanlaydi; Tizim e'lon tafsilotlarini ko'rsatadi va mumkin bo'lgan harakatlarni taqdim etadi.»

## Reliz / R5
- **RELIZ:** uy egasi e'lonlari ro'yxati (E2 kirish nuqtasi).
- **R5 o'zgarishi:** **R5-UE-05** — "Mulklarim" statuslari: **qoralama / ijarada / bo'sh**. Kartada band/bo'sh holati va so'rovlar statistikasi.

## Bajarish tartibi
1. Uy egasi "Mulklarim" ni ochadi: `GET /mobile/announcements/list/` (status filtri bilan).
2. Status filtri: `moderated_status` takroriy paramlari (masalan `?moderated_status=draft&moderated_status=approved`), hudud `district_id`.
3. Kartalar statuslar bo'yicha ko'rsatiladi: `OwnerPropertyStatus{draft (Qoralama), readyToPublish, active (Faol)}` + `OwnerPropertyVacancy{vacant (bo'sh), occupied (band)}`.
4. So'rovlar statistikasi: `GET /mobile/homeowner/requests/statistics/` (total/pending/approved/rejected).
5. Karta bosilsa E2 amallari menyusi ochiladi ([`elon-tahrir.md`](elon-tahrir.md)).

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi Mulklarim ochadi **WHEN** ro'yxat yuklanadi **THEN** e'lonlar statuslar (qoralama/faol) va band/bo'sh holati bilan ko'rinadi.
- **GIVEN** status filtri tanlandi **WHEN** qo'llaniladi **THEN** `moderated_status` paramlari bilan ro'yxat qayta so'raladi.
- **GIVEN** faol e'lon **WHEN** karta ko'rsatiladi **THEN** so'rovlar statistikasi (`requests/statistics/`) counterlari ko'rinadi.

## Kod joylashuvi
- **Modul:** `lib/features/landlord_properties`
- **Sahifa / BLoC:** `LandlordPropertiesPage` / `LandlordPropertiesBloc`; `owner_property_card.dart`, `landlord_properties_filter_sheet.dart`, `statistics_header.dart`; entity `OwnerProperty`, `OwnerPropertyStatus`, `OwnerPropertyVacancy`
- **Endpoint:** `GET /mobile/announcements/list/` (`moderated_status`, `district_id`); `GET /mobile/homeowner/requests/statistics/`

## Konflikt / farqlar
- ⚠ **Statuslar mos emas:** R5-UE-05 uch status (**qoralama / ijarada / bo'sh**) beradi; kodda `OwnerPropertyStatus{draft, readyToPublish, active}` + alohida `OwnerPropertyVacancy{vacant, occupied}` — "ijarada"/"bo'sh" active+vacancy kombinatsiyasiga to'g'ri keladi. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **Ikki katalog:** uy egasi `GET /mobile/announcements/list/`, ijarachi esa `.../tenant/list/` — turli kontrakt. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K8.

## Release 5 — R5-UE-05 — "Mulklarim" statuslari
**Kod holati:** 🟡 (kod statuslari R5 ga to'liq mos emas — E-K10)

**User Story:** Uy egasi sifatida men mulklarimni holati bo'yicha ajratib ko'rishni xohlayman, shunda qaysi uy bo'sh, qaysi ijarada ekanini bir qarashda bilaman.

**Tavsif:** "Mulklarim" bo'limiga qoralama / ijarada / bo'sh statuslari qo'shiladi (mavjud faol / moderatsiyada / rad etilgan / arxiv badge'lariga qo'shimcha). Uy egasi statusni qo'lda o'zgartira oladi.

**Qabul mezonlari:**
- GIVEN e'lon yaratish yakunlanmagan WHEN "Mulklarim" ochilsa THEN e'lon "qoralama" statusida ko'rinadi va tahrirlashni davom ettirish mumkin
- GIVEN uy egasi so'rovni qabul qilib ijaraga berdi WHEN statusni "ijarada"ga o'zgartirsa THEN e'lon katalogda ko'rinmaydi
- GIVEN "ijarada" WHEN "bo'sh"ga o'zgartirilsa THEN e'lon qayta faollashadi (moderatsiya holati saqlangan bo'lsa qayta moderatsiyasiz)
