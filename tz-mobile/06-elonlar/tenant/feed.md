# Lenta (Feed / reels)

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1. Lenta — TZ da alohida ssenariy sifatida yozilmagan; bu E3 katalogini iste'mol qilishning muqobil (vertikal, reels-uslubidagi) usuli. Faqat faol e'lonlar ko'rsatiladi (§4.2.1).
> «Faqat faol (moderatsiyadan o'tgan) e'lonlar katalogda ko'rsatiladi.»

## Reliz / R5
- **RELIZ:** Yangi navbar elementi **Lenta** (Main / Saved / **Lenta** / So'rovlar / Profil) — R5-IJ-01 navbar tarkibida.
- **R5 o'zgarishi:** navbarda Lenta rasman kiritiladi; reaksiya (like/dislike) mexanizmi — reliz kengaytmasi (TZ da yo'q).

## Bajarish tartibi
1. Foydalanuvchi navbardan **Lenta** ni ochadi.
2. `GET /mobile/announcements/reels/list/` (`page`, `page_size`) — vertikal oqim uchun e'lonlar sahifalab yuklanadi.
3. Foydalanuvchi yuqoriga/pastga suradi; har karta rasm/parametrlar bilan ko'rinadi.
4. Yoqtirish/yoqtirmaslik: `POST /mobile/announcements/reels/reaction/` `{announcement_id, reaction: like|dislike}`.

## Qabul kriteriyalari (BDD)
- **GIVEN** Lenta ochilgan **WHEN** ro'yxat oxiriga yaqinlashadi **THEN** keyingi sahifa (`page+1`) yuklanadi.
- **GIVEN** kartada like bosildi **WHEN** reaksiya yuboriladi **THEN** `reaction:like` bilan POST jo'natiladi.
- **GIVEN** faqat faol e'lonlar **WHEN** lenta yuklanadi **THEN** moderatsiyadan o'tmagan e'lon ko'rinmaydi.

## Kod joylashuvi
- **Modul:** `lib/features/feed`
- **Sahifa / BLoC:** `FeedPage` / `FeedBloc`; `feed_card.dart`, `feed_action_buttons.dart`
- **Endpoint:** `GET /mobile/announcements/reels/list/`; `POST /mobile/announcements/reels/reaction/`

## Konflikt / farqlar
- ⚠ **Reaksiya — fire-and-forget:** like/dislike POST'ining natijasi/xatoligi UI'da ishlanmaydi (`feed_remote_data_source.dart` — xatoda faqat log). → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **TZ da yo'q:** Lenta va reels reaksiyasi TZ E3 da tavsiflanmagan — reliz/kod kengaytmasi.
