# Qamrov jadvali (web qismi)

Har bir web use-case va modul tz-web'da hujjatlashtirilganini ko'rsatadi.

> ⚠ **Semantika:** tz-mobile'da "Holat" = **kodda amalga oshirilgan**mi. Bu yerda web kodbaza yo'q, shuning uchun **Holat = TZ da belgilangan va hujjatlashtirilgan**mi. Haqiqiy implementatsiya holati (VueJS panelda bor-yo'qligi) — **noma'lum**, web repo berilganda aniqlanadi.

**Belgilar:** ✅ TZ da to'liq belgilangan + hujjatlashtirilgan · 🟡 qisman/noaniq · 💤 keyingi bosqich

## 1. Web use-case'lar (10 ta — hammasi qamralgan)

| ID | Nomi | Modul (hujjat) | Holat | Izoh |
|---|---|---|---|---|
| **U2-veb** | Web kirish (username/parol) | [01-autentifikatsiya](01-autentifikatsiya/u2-veb.md) | ✅ | JWT; 3 xato→10 daq blok |
| **U2a** | Web parolni tiklash | [01-autentifikatsiya](01-autentifikatsiya/u2a-parol-tiklash.md) | ✅ | Faqat superadmin; vaqtinchalik parol 24 soat |
| **E4** | E'lonni moderatsiya qilish | [02-moderatsiya](02-moderatsiya/e4-elon-moderatsiya.md) | ✅ | Tasdiqlash/rad/tuzatish; 24 soat navbat |
| **E5** | E'lon kataloglarini boshqarish | [02-moderatsiya](02-moderatsiya/e5-kataloglar.md) | ✅ | Klassifikatorlar (⚠ W-B2) |
| **A1** | Foydalanuvchini administratsiya | [03-administratorlik](03-administratorlik/a1-foydalanuvchi-admin.md) | ✅ | RBAC, blacklist, 2FA |
| **A2** | Tizim hisobotlarini shakllantirish | [03-administratorlik](03-administratorlik/a2-hisobotlar.md) | ✅ | ⚠ W-A1 (10s↔30s), W-A4 (support anonim) |
| **A3** | Tashqi integratsiyalarni boshqarish | [05-integratsiya](05-integratsiya/a3-integratsiyalar.md) | ✅ | Kalit shifrlangan; sinov so'rovi |
| **A4** | To'lovlarni nazorat qilish | [04-billing-nazorati](04-billing-nazorati/a4-tolovlar-nazorati.md) | ✅ | Reconciliation, refund |
| **T2** | Murojaatni ko'rib chiqish | [06-support-callmarkaz](06-support-callmarkaz/t2-murojaat-korib-chiqish.md) | ✅ | 24 soat; avtomatik eskalatsiya |
| **T3** | Call-markaz ticket yaratish | [06-support-callmarkaz](06-support-callmarkaz/t3-callmarkaz-ticket.md) | ✅ | ⚠ W-A3 (read-only vs yozish) |

## 2. Web modullar (§4.2.2 — 6 ta)

| Modul | Use-case'lar | Hujjat |
|---|---|---|
| Autentifikatsiya | U2-veb, U2a | [01](01-autentifikatsiya/about.md) |
| Moderatsiya | E4, E5 | [02](02-moderatsiya/about.md) |
| Administratorlik | A1, A2 | [03](03-administratorlik/about.md) |
| Billing nazorati | A4 | [04](04-billing-nazorati/about.md) |
| Integratsiya boshqaruvi | A3 | [05](05-integratsiya/about.md) |
| Texnik qo'llab-quvvatlash (admin) | T2, T3 | [06](06-support-callmarkaz/about.md) |

## 3. R5 admin panel qo'shimchalari
- **R5-AD-01** — Algoritm parametrlari sozlamalari (Top og'irliklari, "narxi tushdi" %, SLA muddati) → [05-integratsiya](05-integratsiya/about.md) / [03](03-administratorlik/about.md).
- **R5-AD-02** — SLA monitoring (muddati o'tgan so'rovlar) → [06-support-callmarkaz](06-support-callmarkaz/about.md).

## 4. Rollar va RBAC
[07-rollar-va-rbac](07-rollar-va-rbac/about.md) — Administrator (+superadmin), Moderator, Call-markaz operatori, Texnik qo'llab-quvvatlash; RBAC, sessiya, audit, malaka.

## 5. Diqqat
- ⚠ **Web kod yo'q** → implementatsiya holati noma'lum (W-K1).
- ⚠ **reliz admin bo'limi to'liq emas** (W-K2) — "6. Admin panel" eksporti yo'q; faqat R5 PDF qisman beradi.
- Konfliktlar: [`_konfliktlar.md`](_konfliktlar.md) — W-A1, W-A3, W-A4, W-A6, W-B2, W-B3.

## 6. Loyiha-darajasidagi TZ bo'limlari (na mobil, na web use-case)
Quyidagilar TZ hujjatining o'zida qoladi (jarayon/administrativ — ilova bo'linmasi emas): **1.** Umumiy ma'lumotlar · **3.** Obyekt harakteristikasi · **5.** Yaratish bosqichlari · **6.** Nazorat va qabul · **7.** Ishga tushirishga tayyorlash · **8.** Hujjatlashtirish · **4.3.6** Tashkiliy ta'minot.
