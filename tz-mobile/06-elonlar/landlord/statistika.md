# E'lon va dashboard statistikasi

**Rollar:** 🏠 Uy egasi    **Holat:** 🟡 Qisman (Daromadlarim/Xizmatlar — "Tez kunda")

## TZ manbai
TZ §4.2.1 e'lon statistikasi bo'yicha alohida ssenariy bermaydi; bu E1/E2 boshqaruvining kuzatuv qismidir. TZ faqat "faol e'lonlar katalogda ko'rsatiladi" va so'rov/ko'rish oqimlarini belgilaydi; ko'rsatkichlarni to'plash — reliz/kod kengaytmasi.
> «E'lonni tahrirlash, faol/nofaol va boshqa statuslarga olish va o'chirish.»

## Reliz / R5
- **RELIZ:** to'g'ridan-to'g'ri manba yo'q.
- **R5 o'zgarishi:** **R5-UE-04** — Uy egasi asosiy sahifasida **Analitika** bloki: 7 kun / 30 kun switch — **Ko'rishlar, So'rovlar, Yoqtirishlar, Qo'ng'iroqlar** counterlari; **Daromadlarim** va **Xizmatlar** bloklari UI to'liq, ammo raqamlar o'rnida "**Tez kunda**" (2–3-bosqichga tayyorgarlik).

## Bajarish tartibi
1. **E'lon darajasida:** `GET /mobile/announcements/{id}/stats/daily/?days=` — `total_views`, `total_likes`, `total_phone_views`, `total_requests` + kunlik nuqtalar (`views`, `likes`, `phone_views`, `requests`).
2. **Tracking:** e'lon ko'rilganda `POST /mobile/announcements/{id}/view/`; telefon ko'rilganda `POST /mobile/announcements/{id}/phone-view/` (ikkalasi ham fire-and-forget — xatoda faqat log).
3. **Dashboard darajasida:** `GET /mobile/homeowner/property-statistics/` (e'lonlar bo'yicha agregat) va `GET /mobile/homeowner/financial-statistics/` (Daromadlarim — "Tez kunda").
4. Analitika bloki 7/30 kun switch bilan counterlarni ko'rsatadi (`announcement_stats_chart.dart`, `stats_range_selector.dart`).

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi e'lon statistikasini ochadi **WHEN** `days=7` yoki `days=30` tanlanadi **THEN** mos oraliq uchun ko'rishlar/so'rovlar/yoqtirishlar/qo'ng'iroqlar grafigi ko'rinadi.
- **GIVEN** e'lon detali ochildi **WHEN** ko'rish yuz beradi **THEN** `POST .../view/` qayd etiladi (UI bloklanmaydi).
- **GIVEN** Daromadlarim bloki **WHEN** dashboard ochiladi **THEN** raqamlar o'rnida "Tez kunda" ko'rsatiladi (R5-UE-04).

## Kod joylashuvi
- **Modul:** `lib/features/announcements` (e'lon stats) + `lib/features/landlord_dashboard` (dashboard)
- **Sahifa / BLoC:** `AnnouncementStatsBloc` (`announcement_stats_chart.dart`, `stats_range_selector.dart`, `stats_legend.dart`); `DashboardBloc` (`landlord_dashboard`)
- **Endpoint:** `GET /mobile/announcements/{id}/stats/daily/?days=`; `POST /mobile/announcements/{id}/view/`, `.../phone-view/`; `GET /mobile/homeowner/property-statistics/`, `/mobile/homeowner/financial-statistics/`

## Konflikt / farqlar
- ⚠ **Daromadlarim/Xizmatlar — raqamsiz:** R5-UE-04 bo'yicha bu bloklar "Tez kunda" holatida (2–3-bosqich), shu sabab Holat 🟡. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **Tracking fire-and-forget:** `view`/`phone-view` POST xatoligi UI'da ishlanmaydi (`announcement_stats_remote_data_source.dart:41/52` — "failed silently").
- ⚠ **TZ da yo'q:** e'lon statistikasi va dashboard analitikasi TZ §4.2.1 da tavsiflanmagan — reliz/kod kengaytmasi.

## Release 5 — R5-UE-04 — Asosiy sahifa: Analitika va "Tez kunda" bloklari
**Kod holati:** 🟡 (analitika qisman/mock; "Tez kunda" placeholder'lar bor)

**User Story:** Uy egasi sifatida men mulklarim bo'yicha faollik ko'rsatkichlarini bir ekranda ko'rishni xohlayman, shunda e'lonlarim samarasini baholay olaman.

**Tavsif:** Analitika bloki: 7 kun / 30 kun switch; Ko'rishlar, So'rovlar, Yoqtirishlar, Qo'ng'iroqlar counterlari (o'zgarish belgisi bilan). Daromadlarim va Xizmatlar bloklari UI to'liq quriladi, lekin raqamlar/kontent o'rnida "Tez kunda" (2–3-bosqichga tayyorgarlik).

**Qabul mezonlari:**
- GIVEN uy egasi asosiy sahifada WHEN "7 kun" tanlansa THEN barcha counterlar 7 kunlik davr bo'yicha yangilanadi
- GIVEN davr almashtirildi WHEN "30 kun" tanlansa THEN counterlar 30 kunlik davrga o'tadi
- GIVEN Daromadlarim bloki WHEN sahifa yuklansa THEN raqamlar o'rnida "Tez kunda", blok bosilganda ham to'lov funksionali ochilmaydi
- GIVEN Xizmatlar bloki WHEN sahifa yuklansa THEN kontent o'rnida "Tez kunda"
