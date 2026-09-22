# 07 — Rollar va RBAC (web qismi)

Web qismi quyi tizimidagi rollar, ularning vakolatlari (§4.1.3.2), malaka talablari (§4.1.3.3), sessiya va kirishni tabaqalashtirish (§4.1.6.1). Bu **modul emas** — barcha web modullar bo'ylab kesuvchi (cross-cutting) hujjat. TZ RBAC (kirish huquqlari) matritsasini alohida bermaganligi sabab bir nechta ziddiyat aynan shu yerdan kelib chiqadi: **W-A3, W-A4, W-A6**.

## Web rollari va vakolatlari (§4.1.3.2)

| Rol | Belgi | Asosiy vakolatlari (TZ §4.1.3.2) | Web modullar |
|---|---|---|---|
| Administrator | 🛡 | Tizimni web admin portali orqali **to'liq boshqaradi**; barcha operatsiyalar va ma'lumotlarga kirish | 01, 03 (A1, A2), 04 (A4), 05 (A3) |
| Moderator | 🔍 | E'lonlarni tekshirish/tasdiqlash, soxta e'lonlarni bloklash | 01, 02 (E4, E5) |
| Call-markaz operatori | 🎧 | Murojaatlarni qabul qilish va qo'llab-quvvatlash; **faqat ko'rish (o'qish) huquqi** | 01, 06 (T3) |
| Texnik qo'llab-quvvatlash xodimi | 🛠 | Admin web panelida **ticket boshqaruvi, eskalatsiya, holat yangilash**; analitikaga cheklangan (anonimlashtirilgan) kirish; tizim jurnallariga faqat o'qish | 01, 03 (A2 — ⚠ W-A4), 06 (T2) |
| superadmin | 🛡 | Admin hisoblarini yaratish, parolni tiklash (U2-veb, U2a) — §4.1.3.2 ro'yxatida **rasman ta'riflanmagan** (⚠ W-A6) | 01 (U2-veb, U2a) |

> Ijarachi, Uy egasi, Ro'yxatdan o'tmagan (guest) — mobil rollari; web qismi quyi tizimiga kirmaydi (mobil oqimlar: `../../tz-mobile/`).

## Malaka talablari (§4.1.3.3)

| Rol | Malaka (TZ §4.1.3.3) |
|---|---|
| Administrator | Oliy IT ma'lumot; AT boshqaruvi bo'yicha ≥2 yil tajriba; maxsus o'qitish kursidan o'tgan |
| Moderator | O'rta maxsus yoki oliy ma'lumot; maxsus o'qitish kursi; moderatsiya siyosati/qoidalari bilan tanish |
| Call-markaz operatori | O'rta maxsus ma'lumot; aloqa ko'nikmalari; o'qitish kursidan o'tgan |
| Texnik qo'llab-quvvatlash xodimi | Oliy IT ma'lumot; tizim administrirovaniyesi, ma'lumotlar bazalari va tarmoq texnologiyalari bo'yicha amaliy tajriba |

> Ichki foydalanuvchilarni o'qitish va bilim nazorati — TZ 7-bo'limida.

## RBAC, sessiya va xavfsizlik (§4.1.6.1)

- Web qismiga faqat **autentifikatsiyadan o'tgan** foydalanuvchilar kiradi (mobil guestdan farqli — u autentifikatsiyasiz cheklangan kirishga ega).
- Har bir foydalanuvchi roliga mos **RBAC** huquqlariga ega; web qismida **har bir operatsiya avtorizatsiya tekshiruvidan** o'tadi.
- **Administrator darajasidagi operatsiyalar** qo'shimcha tasdiqlash / ikki faktorli mexanizmlar bilan himoyalanadi (§4.2.2, §4.1.6.1).
- Web sessiya **15 daqiqa faoliyatsizlikdan so'ng** avtomatik yakunlanadi (§4.1.6.1). Mobil bilan farq: [`../01-autentifikatsiya/about.md`](../01-autentifikatsiya/about.md).
- Barcha ichki harakatlar (kirish, moderatsiya, hisobot, billing, integratsiya, ticket) **audit jurnaliga** yoziladi.

## ⚠ Konfliktlar (RBAC dan kelib chiqadi)

| ID | Mavzu | Qisqacha |
|---|---|---|
| [W-A3](../_konfliktlar.md) | Call-markaz operatori huquqi | §4.1.3.2 + §4.2.2 «faqat ko'rish (o'qish)» ↔ T3 operator «yangi ticket yaratadi» (yozish amali) |
| [W-A4](../_konfliktlar.md) | Support xodimi ma'lumot doirasi | §4.1.3.2 «anonimlashtirilgan analitikaga cheklangan kirish» ↔ A2 da support «foydalanuvchilar, to'lovlar, skoring» hisobotlarini shakllantiradi (shaxsiy/moliyaviy) |
| [W-A6](../_konfliktlar.md) | «superadmin» roli ta'riflanmagan | U2-veb, U2a, §4.2.2 da faol ishlatiladi ↔ §4.1.3.2 rollar ro'yxatida yo'q (faqat «Administrator») |

## Backend / API (kutilayotgan)
Web kodbaza yo'q. RBAC odatda JWT rol/claim va endpoint darajasidagi ruxsat orqali amalga oshiriladi (`/admin/...` namespace). Sessiya muddati (15 daq faoliyatsizlik) token/refresh siyosatida sozlanadi; administrator operatsiyalari uchun qo'shimcha tasdiqlash bosqichi kutiladi. Aniq rol×huquq matritsasi va yo'llar web repo berilganda tasdiqlanadi.
