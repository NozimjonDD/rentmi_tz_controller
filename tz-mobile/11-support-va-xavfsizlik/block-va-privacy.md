# Bloklash va maxfiylik

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
TZ mobil use-case'larida foydalanuvchini bloklash alohida yozilmagan — bu App Store **Guideline 1.2** (UGC: bloklash + shikoyat + maxfiylik) talabini qondirish uchun qo'shilgan xavfsizlik qatlami. TZ §4.1.6 umumiy xavfsizlik/maxfiylik tamoyillariga hamohang.

## Reliz / R5
- **RELIZ:** UGC xavfsizlik (bloklash, shikoyat) — Guideline 1.2.
- **R5 o'zgarishi:** yo'q (R5 doirasidan tashqari, lekin R5 «faqat platforma orqali muloqot» xabari bilan mos).

## Bajarish tartibi (kod)
1. Bloklash: `block_user_bottom_sheet` → `POST /mobile/users/block/` `{blocked_user_id, reason, description?}`.
2. Blokni yechish: `DELETE /mobile/users/block/{userId}/`.
3. Bloklanganlar ro'yxati: `GET /mobile/users/blocked/` (pagination, search) — `blocked_users_page` (`/settings/blocked-users`).
4. Blok holati: `GET /mobile/users/{userId}/block-status/`.
5. **`BlockedUsersSyncBus`** — bloklash/yechish darhol e'lonlar, chat va favorites ro'yxatlarini filtrlaydi (real-time sinxronizatsiya).
6. Maxfiylik markazi: `PrivacyPage` (`/settings/privacy`) — «Xavfsizlik» (bloklangan foydalanuvchilar) va «Huquqiy» (shartlar) bo'limlari.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi **WHEN** boshqa foydalanuvchini bloklaydi **THEN** `POST users/block/` yuboriladi va e'lon/chat/favorites darhol filtrlanadi.
- **GIVEN** o'zini bloklashga urinish **WHEN** yuboriladi **THEN** `SelfBlockException`.
- **GIVEN** allaqachon bloklangan **WHEN** qayta bloklanadi **THEN** `AlreadyBlockedException`; admin'ni bloklash → `CannotBlockAdminException`.

## Kod joylashuvi
- **Modul:** `lib/features/blocks` — `BlockedUsersBloc`, `BlockActionCubit`, `BlockStatusCubit`; `block_user_bottom_sheet`, `blocked_users_page`
- **Maxfiylik:** `lib/features/settings/presentation/pages/privacy_page.dart` (App Store Guideline 1.2 hub)
- **Endpoint:** `POST /mobile/users/block/`, `DELETE /mobile/users/block/{userId}/`, `GET /mobile/users/blocked/`, `GET /mobile/users/{userId}/block-status/`
- **Route'lar:** `/settings/blocked-users`, `/settings/my-reports`, `/settings/privacy`
- **Sync:** `BlockedUsersSyncBus` — bloklash o'zgarishlari announcements/chat/favorites bloklariga tarqaladi.

## Konflikt / farqlar
- Farq aniqlanmadi — TZ mobil use-case'i yo'q, lekin Guideline 1.2 / xavfsizlik talablariga to'liq mos.
- Bloklash sabablari (`BlockReason`) enum sifatida; server `reason` apiValue qabul qiladi.
