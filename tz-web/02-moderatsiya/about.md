# 02 — Moderatsiya moduli

Web qismi quyi tizimida **moderator** e'lonlarni tekshiradi/tasdiqlaydi, soxta e'lonlarni bloklaydi va e'lon kataloglarini (klassifikatorlarni) boshqaradi. TZ §4.2.2 (Moderatsiya moduli). Use-case'lar: **E4**, **E5**.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`e4-elon-moderatsiya.md`](e4-elon-moderatsiya.md) | E'lonni tasdiqlash/rad etish/tuzatish, soxta e'lonni bloklash, 24 soatlik navbat | E4 | ✅ |
| [`e5-kataloglar.md`](e5-kataloglar.md) | Kataloglar/klassifikatorlar (obyekt turlari, hududlar, foydalanish shartlari) | E5 | ✅ |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «E'lonlarni tekshirish va tasdiqlash, soxta e'lonlarni bloklash hamda e'lon kataloglari (klassifikatorlar)ni boshqarish.»

- Bir e'lonni ko'rib chiqishning **maksimal navbat muddati — 24 soat**.
- Rad etish va tuzatish talabida **sabab/izoh majburiy**.
- Barcha moderatsiya qarorlari **audit jurnaliga** yoziladi.
- **Soxta e'lon ulushi 5% dan oshmasligi** nazorat qilinadi.

## Muhim eslatma
- E5 kataloglaridagi o'zgarishlar **E1 (e'lon yaratish)** va **E3 (qidirish/filtrlash)** formalariga darhol ta'sir qiladi.
- E4 dan muvaffaqiyatli o'tish — R5 «Tekshirilgan» badge'ining uchta shartidan biri (E4 + U5 identifikatsiya + tegishlilik).

## ⚠ Konflikt
- **Kataloglar/klassifikatorlar** uchun §4.3.2 «batafsil 4.1.11 bandida» deb havola qiladi, biroq **§4.1.11 TZ da mavjud emas** — klassifikatorlar aslida E5 (kataloglar boshqaruvi)da ta'riflangan. → [`_konfliktlar.md`](../_konfliktlar.md) W-B2.

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `GET /admin/moderation/queue/`, `POST /admin/moderation/listings/{id}/approve|reject|request-correction/`, `GET|POST /admin/catalogs/...`. Aniq yo'llar web repo berilganda tasdiqlanadi.
