# U2a — Web parolni tiklash

**Rollar:** 🛡 Administrator (superadmin roliga ega)    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
U2a · §4.1.1.4 · **Kengaytma (U2-veb ga nisbatan)**. Web foydalanuvchi (admin/moderator/support) parolini unutgan yoki bloklangan bo'lsa, **superadmin** uni tiklaydi.
> «Superadmin web qismi quyi tizimida 'Foydalanuvchilarni boshqarish'ga kiradi; foydalanuvchini topadi va 'Parolni tiklash'ni tanlaydi; tizim vaqtinchalik parol yaratadi.»

## Reliz / R5
- **RELIZ / R5:** o'zgarish yo'q.

## Ishga tushirish shartlari
Web foydalanuvchi hisobi superadmin tomonidan yaratilgan; foydalanuvchi parolini unutgan yoki hisobi bloklangan.

## Bajarish tartibi
1. Ta'sirlangan foydalanuvchi superadminga murojaat qiladi.
2. Superadmin 'Foydalanuvchilarni boshqarish'ga kiradi.
3. Foydalanuvchini topadi, 'Parolni tiklash'ni tanlaydi.
4. Tizim **vaqtinchalik parol** yaratadi.
5. Vaqtinchalik parol **korxona emaili** orqali foydalanuvchiga yuboriladi.
6. Foydalanuvchi vaqtinchalik parol bilan kirganda tizim **yangi parol o'rnatishni talab qiladi**.
7. Yangi parol ikki marta kiritilib tasdiqlanadi.
8. Yangi parol saqlangach, sessiya yaratiladi.
9. Barcha harakatlar audit jurnaliga yoziladi.

## Vaqt reglamenti
Vaqtinchalik parol yuborish — ≤60 s; parolning amal muddati — **24 soat**.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi parolni unutdi **WHEN** superadmin 'Parolni tiklash'ni bosadi **THEN** vaqtinchalik parol (24 soat) korxona emaili orqali yuboriladi.
- **GIVEN** vaqtinchalik parol bilan kirish **WHEN** foydalanuvchi kiradi **THEN** yangi parol o'rnatish talab qilinadi.
- **GIVEN** vaqtinchalik parol muddati o'tdi **WHEN** kirishga urinadi **THEN** qayta tiklash so'raladi.

## Backend / API (kutilayotgan)
- Kutiladi: `POST /admin/users/{id}/password/reset/` (superadmin) → vaqtinchalik parol. Aniq yo'l web repo berilganda.

## Konflikt / farqlar
- ⚠ Parol tiklash **faqat superadmin** orqali (o'z-o'zini tiklash yo'q). ⚠ superadmin §4.1.3.2 da ta'riflanmagan → [`_konfliktlar.md`](../_konfliktlar.md) W-A6.
