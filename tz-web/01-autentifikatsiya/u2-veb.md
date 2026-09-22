# U2-veb — Tizimga kirish (Web qismi quyi tizimi, parol)

**Rollar:** 🛡 Administrator / 🔍 Moderator / 🎧 Call-markaz / 🛠 Support    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
U2-veb · §4.1.1.4. Web interfeys foydalanuvchisi username va parol orqali kiradi (JWT).
> «Foydalanuvchi hisobi superadmin tomonidan oldindan yaratilgan (username va parol berilgan); hisob faol holatda; kirish web interfeys orqali amalga oshiriladi.»

## Reliz / R5
- **RELIZ / R5:** admin panel VueJS'da (R5 — algoritm parametrlari, SLA monitoring shu panelda). Kirish oqimiga o'zgarish yo'q.

## Ishga tushirish shartlari
Hisob **superadmin** tomonidan oldindan yaratilgan (username+parol); hisob faol; kirish web interfeys orqali.

## Bajarish tartibi
1. Foydalanuvchi web sahifada 'Kirish'ni bosadi.
2. Username va parolni kiritadi.
3. Tizim tekshiradi — **3 ta noto'g'ri urinishdan so'ng hisob 10 daqiqaga bloklanadi**.
4. To'g'ri ma'lumot → **JWT tokeni** yaratiladi.
5. Audit jurnaliga yozuv kiritiladi.
6. Foydalanuvchi roliga mos web qismi quyi tizimiga yo'naltiriladi.

## Vaqt reglamenti
Umumiy davomiyligi — ≤5 s; parolni tekshirish — ≤2 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** superadmin yaratgan faol hisob **WHEN** to'g'ri username+parol kiritiladi **THEN** JWT yaratiladi, rolga mos panelga o'tadi.
- **GIVEN** 3 marta noto'g'ri parol **WHEN** yana urinsa **THEN** hisob 10 daqiqaga bloklanadi.
- **GIVEN** username topilmadi **WHEN** kirishga urinadi **THEN** kirish rad etiladi.
- **GIVEN** parol unutilgan **WHEN** foydalanuvchi tiklamoqchi **THEN** U2a (faqat superadmin tiklaydi).

## Backend / API (kutilayotgan)
- Kutiladi: `POST /admin/auth/login/` — `{username, password}` → `{access, refresh}` (JWT). Aniq yo'l web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ Kirish/tiklash **faqat superadmin** yaratgan hisoblar uchun; ⚠ **superadmin** roli §4.1.3.2 da ta'riflanmagan → [`_konfliktlar.md`](../_konfliktlar.md) W-A6.
