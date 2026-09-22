# A1 — Foydalanuvchini administratsiya qilish

**Rollar:** 🛡 Administrator    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
A1 · §4.1.1.4 · Administrator foydalanuvchilarni boshqaradi: **bloklash/aktivatsiya, rol o'zgartirish, profil tahriri (favqulodda), blacklist, PIN-kodni majburiy tiklash**; RBAC doirasida ruxsatlar va tizim sozlamalari.
> «Quyidagi harakatlardan birini tanlaydi: a) bloklash/aktivatsiya; b) rol o'zgartirish; c) profil ma'lumotlarini tahrirlash (favqulodda holatda); d) blacklist'ga qo'shish/chiqarish; e) PIN-kodni majburiy tiklashga yo'naltirish.»

## Reliz / R5
- **RELIZ / R5:** R5 admin panelida **algoritm parametrlari sozlamalari** (R5-AD-01: Top og'irliklari, «Sizga mos»/tavsiya ballari, «Narxi tushdi» chegarasi, SLA muddati) mavjud — administrator tizim sozlamalari doirasida. reliz admin bo'limi to'liq eksport qilinmagan → W-K2.

## Ishga tushirish shartlari
Administrator tizimga kirgan va **administrator roliga** ega; tizimda kamida bitta boshqariladigan foydalanuvchi mavjud.

## Bajarish tartibi
1. Administrator 'Foydalanuvchilarni boshqarish' bo'limini ochadi.
2. Tizim foydalanuvchilar ro'yxatini beradi (filtr/qidiruv: rol, holat, ro'yxatdan o'tish sanasi va boshqalar).
3. Administrator foydalanuvchini tanlaydi va **to'liq profilini** ko'radi (shaxsiy ma'lumotlar, Rentmi bali, faoliyat tarixi, audit yozuvlari, so'rovlari, chatlari).
4. Harakatlardan birini tanlaydi: **a)** bloklash/aktivatsiya; **b)** rol o'zgartirish; **c)** profil tahriri (favqulodda holatda); **d)** blacklist'ga qo'shish/chiqarish; **e)** PIN-kodni majburiy tiklashga yo'naltirish; shuningdek **RBAC** ruxsatlari va tizim sozlamalariga kirish.
5. Harakatni tasdiqlaydi va **sabab kiritadi** (audit uchun majburiy).
6. Tizim o'zgarishni saqlaydi va foydalanuvchiga bildirishnoma yuboradi.
7. Barcha harakatlar audit jurnaliga batafsil yoziladi (**kim, qachon, nima, sababi**).

## Vaqt reglamenti
Ro'yxatni yuklash — ≤5 s; profil yuklash — ≤3 s; o'zgarishni saqlash — ≤3 s; bildirishnoma — ≤10 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** administrator profilda **WHEN** foydalanuvchini bloklaydi yoki rolini o'zgartiradi **THEN** sabab majburiy, o'zgarish saqlanadi, foydalanuvchiga bildirishnoma, audit yozuvi (kim/qachon/nima/sababi).
- **GIVEN** blacklist'ga qo'shilayotgan foydalanuvchining **faol so'rovlari** bor **WHEN** administrator qo'shmoqchi **THEN** ogohlantirish chiqadi.
- **GIVEN** foydalanuvchi boshqa administrator tomonidan tahrirlanmoqda **WHEN** ikkinchi administrator saqlamoqchi **THEN** konflikt aniqlanadi va qayta yuklash taklif qilinadi.
- **GIVEN** yuqori darajadagi operatsiya **WHEN** administrator bajaradi **THEN** qo'shimcha **ikki faktorli** tasdiq talab qilinadi.

## Backend / API (kutilayotgan)
Web kodbaza yo'q → TZ asosida taxminiy (`/admin/...`):
- `GET /admin/users/` — filtr/qidiruv (rol, holat, sana).
- `GET /admin/users/{id}/` — to'liq profil.
- `POST /admin/users/{id}/block/`, `.../activate/` — `{reason}`.
- `POST /admin/users/{id}/role/` — rol o'zgartirish.
- `POST /admin/users/{id}/blacklist/` — qo'shish/chiqarish.
- `POST /admin/users/{id}/pin/reset/` — PIN-kodni majburiy tiklash.
- Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Ruxsatlar (RBAC) matritsasi** TZ §4.1.3.2 da rasman ta'riflanmagan — W-A3/W-A4 shundan kelib chiqadi. → [`_konfliktlar.md`](../_konfliktlar.md) W-A4; [`07-rollar-va-rbac`](../07-rollar-va-rbac/about.md).
