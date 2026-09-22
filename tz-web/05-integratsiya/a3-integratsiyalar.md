# A3 — Tashqi integratsiyalarni boshqarish

**Rollar:** 🛡 Administrator    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
A3 · §4.1.1.4 · Administrator ulangan tashqi xizmatlar holatini ko'radi, parametrlarini (endpoint, kalit, timeout, retry) sozlaydi, sinov so'rovi bilan tekshiradi va integratsiyani yoqadi/o'chiradi.
> «Tizim ulangan tashqi xizmatlar ro'yxatini va real vaqtdagi holatini ko'rsatadi (identifikatsiya, skoring byurosi, to'lov tizimlari, SMS, push, xarita); … parametrlarini sozlaydi (endpoint, kalit/token muddati, qayta urinish va timeout sozlamalari) — kalitlar shifrlangan saqlanadi.»

## Reliz / R5
- **RELIZ / R5:** admin panel VueJS'da (R5 — algoritm parametrlari, SLA monitoring). Integratsiya boshqaruvi oqimiga o'zgarish yo'q.

## Ishga tushirish shartlari
Administrator web qismi quyi tizimiga kirgan; tizimga kamida bitta tashqi integratsiya ulangan.

## Bajarish tartibi
1. Administrator 'Integratsiyalar' bo'limini ochadi.
2. Tizim ulangan tashqi xizmatlar ro'yxatini va real vaqtdagi holatini ko'rsatadi (identifikatsiya, skoring byurosi, to'lov tizimlari, SMS, push, xarita).
3. Administrator xizmatni tanlaydi va tafsilotlarni ko'radi (holat, oxirgi muvaffaqiyatli so'rov, xatoliklar statistikasi, javob vaqti).
4. Integratsiya parametrlarini sozlaydi (endpoint, kalit/token muddati, qayta urinish va timeout) — **kalitlar shifrlangan saqlanadi**.
5. Integratsiyani **sinov so'rovi** orqali tekshiradi.
6. Zaruratga ko'ra integratsiyani vaqtincha o'chiradi yoki yoqadi.
7. Barcha o'zgarishlar audit jurnaliga yoziladi.

## Vaqt reglamenti
Ro'yxatni yuklash — ≤5 s; sinov so'rovi natijasi — ≤15 s; sozlamalarni saqlash — ≤3 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** kamida bitta integratsiya ulangan **WHEN** administrator 'Integratsiyalar'ni ochadi **THEN** xizmatlar ro'yxati real vaqtdagi holati bilan ko'rsatiladi.
- **GIVEN** xizmat tanlangan **WHEN** administrator tafsilotni ochadi **THEN** holat, oxirgi muvaffaqiyatli so'rov, xatolik statistikasi va javob vaqti ko'rinadi.
- **GIVEN** yangi parametrlar (endpoint/kalit/timeout/retry) **WHEN** administrator saqlaydi **THEN** kalit shifrlangan saqlanadi va o'zgarish audit jurnaliga yoziladi.
- **GIVEN** sinov so'rovi yuborildi **WHEN** kalit noto'g'ri **THEN** sinov rad etiladi va xato ko'rsatiladi.
- **GIVEN** tashqi xizmat javob bermaydi **WHEN** holat tekshiriladi **THEN** 'mavjud emas' holati va ogohlantirish ko'rsatiladi.

## Backend / API (kutilayotgan)
- Kutiladi: `GET /admin/integrations/` (ro'yxat + holat), `GET /admin/integrations/{id}/` (statistika/javob vaqti), `PATCH /admin/integrations/{id}/` (endpoint/kalit/timeout/retry — kalit shifrlangan), `POST /admin/integrations/{id}/test/` (sinov so'rovi), `POST /admin/integrations/{id}/toggle/` (yoqish/o'chirish). Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Ssenariylar tartibi:** ro'yxatda A4 (to'lovlar) A3 (integratsiya) dan oldin kelgan (tartib buzilgan). → [`_konfliktlar.md`](../_konfliktlar.md) W-B3.
