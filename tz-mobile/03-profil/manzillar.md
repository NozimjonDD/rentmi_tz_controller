# Manzillar (CRUD)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U4 · §4.1.1.4 (3-qadam) — «aloqa» ma'lumotlarini tahrirlash doirasida. TZ manzillar uchun alohida CRUD oqimini batafsil ta'riflamaydi; profil aloqa ma'lumotlarining kengaytmasi sifatida qaraladi.
> «2) Tizim joriy ma'lumotlarni (shaxsiy, aloqa, Rentmi bali, hisobotlar) ko'rsatadi …»

## Reliz / R5
- **RELIZ:** manzillar CRUD alohida US sifatida ajratilmagan (profil, R2 doirasida).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Profil → `addresses_page`: mavjud manzillar ro'yxati (`GET /mobile/addresses/`).
2. Yangi manzil → `add_edit_address_page` → `POST /mobile/addresses/`.
3. Tahrirlash/o'chirish → `PUT` / `DELETE /mobile/addresses/{id}/`.
4. Asosiy (default) manzilni belgilash → `POST /mobile/addresses/{id}/set-default/`.

## Qabul kriteriyalari (BDD)
- **GIVEN** manzillar ro'yxati **WHEN** foydalanuvchi yangi manzil qo'shadi **THEN** `POST /mobile/addresses/` chaqiriladi va ro'yxatga qo'shiladi.
- **GIVEN** mavjud manzil **WHEN** tahrirlanadi yoki o'chiriladi **THEN** `PUT` / `DELETE /mobile/addresses/{id}/` bajariladi.
- **GIVEN** manzil **WHEN** default belgilanadi **THEN** `POST /mobile/addresses/{id}/set-default/` chaqiriladi.

## Kod joylashuvi
- **Modul:** `lib/features/settings`
- **Sahifa / Cubit:** `addresses_page`, `add_edit_address_page` / `AddressesCubit`
- **Endpoint:** `GET/POST /mobile/addresses/` · `PUT/DELETE /mobile/addresses/{id}/` · `POST /mobile/addresses/{id}/set-default/`

## Konflikt / farqlar
- ⚠ Manzillar CRUD TZ U4 da alohida ta'riflanmagan — «aloqa ma'lumotlari» kengaytmasi sifatida kodda amalga oshirilgan. → [`_konfliktlar.md`](../_konfliktlar.md)
