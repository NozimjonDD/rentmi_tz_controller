# E'lonlar — Ijarachi / Mehmon tomoni

E'lonni **iste'mol qilish** oqimi: asosiy sahifa, katalog qidiruvi va filtri, xarita, lenta, saqlangan uylar, e'lon tafsiloti va uy egasi ommaviy profili. TZ use-case **E3** (qidirish/filtrlash) shu tomonning o'zagi; reliz IJ-01/IJ-02 va R5-IJ-01–08 uni to'ldiradi.

**TZ use-case:** E3 — E'lonlarni qidirish va filtrlash · §4.2.1
**Rollar:** 👤 Ijarachi (ro'yxatdan o'tgan) / 👥 Mehmon (guest) — guest ko'ra oladi, ammo so'rov yubora olmaydi (reliz IJ-01 BQ-3).

## Quyi tugunlar

| Tugun | Mazmun | TZ / R5 | Holat |
|---|---|---|---|
| [`asosiy-sahifa.md`](asosiy-sahifa.md) | Home: bo'limlar, xona chips, badge'lar, skoring-mos uylar, stories | reliz IJ-01/IJ-02, R5-IJ-01–03 | ✅ |
| [`qidiruv-filtr.md`](qidiruv-filtr.md) | E'lon qidiruvi, ko'p mezonli filtr, saqlangan filtrlar | E3, R5-IJ-04/05 | ✅ |
| [`xarita.md`](xarita.md) | Xarita orqali qidirish (pin, klaster, bottom sheet) | E3, R5-IJ-06 | ✅ |
| [`feed.md`](feed.md) | Lenta (reels) — vertikal oqim, like/dislike | (reliz kengaytmasi) | ✅ |
| [`favorites.md`](favorites.md) | Saqlangan uylar (wishlist) | E3 (saqlash) | ✅ |
| [`elon-detail.md`](elon-detail.md) | E'lon tafsiloti, badge'lar, Ko'rildi/Ariza statistikasi | E3 (detail), R5-IJ-07 | ✅ |
| [`uy-egasi-profil.md`](uy-egasi-profil.md) | Uy egasi ommaviy profili (Tasdiqlangan, javob vaqti) | R5-IJ-08 | ❌ |

## E3 to'liq bajarish tartibi (TZ)

1. Foydalanuvchi e'lonlar katalogini ochadi.
2. Tizim faol e'lonlarni oldindan belgilangan tartibda ko'rsatadi (sana bo'yicha kamayib + ijarachi skoring bali asosida).
3. Foydalanuvchi qidiruv/filtr parametrlarini kiritadi (hudud, narx oralig'i, obyekt turi, maydon, xonalar soni …).
4. Tizim filtrlarga mos e'lonlarni shakllantiradi va ko'rsatadi.
5. Foydalanuvchi e'lonni tanlaydi yoki filtrlarni o'zgartiradi.
6. Qo'shimcha: ro'yxatdan o'tgan foydalanuvchi filtrlarni saqlaydi; mos yangi e'lon paydo bo'lganda push keladi.
7. Foydalanuvchi e'lon egasiga ijara so'rovi yuborishi, e'lonni bloklashi, ulashishi va shikoyat qilishi mumkin.

## Vaqt reglamenti (TZ)
Katalogni yuklash — ≤3 s · filtrlash natijalarini shakllantirish — ≤5 s.

## Kod modullari
`lib/features/tenant_dashboard` (home) · `lib/features/announcements` (katalog, filtr, detail) · `lib/features/map` · `lib/features/feed` · `lib/features/favorites` · `lib/features/blocks` (e'lon/uy egasini bloklash).

## Konflikt / farqlar
- ⚠ Badge'lar (Sizga mos/Top/Narxi tushdi) faqat `tenant/home/` javobida; katalog ro'yxatida yo'q. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K1.
- ⚠ Stories R5 da «yashiriladi» deyilgan, kodda faol. → E-K2.
- ⚠ Saqlangan filtr Clean Arch chetlab (`FilterSessionCubit`); favorites GET-mutatsiya; rooms/pets frontend-only. → E-K3, E-K4, E-K5.
