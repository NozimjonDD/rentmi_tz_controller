# Web qismi — umumiy va funksional bo'lmagan talablar

Web qismi quyi tizimiga (admin panel) taalluqli, use-case'larga bog'liq bo'lmagan TZ talablari.

## 1. Web sessiya va kirish xavfsizligi (§4.1.6.1)
- Web qismiga **faqat autentifikatsiyadan o'tgan** foydalanuvchilar kiradi (mobil guest'dan farqli).
- Har bir operatsiya **avtorizatsiya tekshiruvidan** o'tadi (RBAC).
- **Administrator darajasidagi operatsiyalar** qo'shimcha tasdiqlash (ikki faktorli) bilan himoyalanadi.
- Sessiya **15 daqiqa faoliyatsizlikdan so'ng** avtomatik yakunlanadi.
> «Tizim web qismi quyi tizimda har bir foydalanuvchi sessiyasini yaratadi va faoliyatsizlik davrida (15 daqiqa) avtomatik ravishda yakunlaydi.»

## 2. RBAC — rolga asoslangan kirish (§4.1.3.2, §4.1.6.1)
- Har rol o'z vakolatlariga mos kirish huquqiga ega. Batafsil rollar × amal: [`07-rollar-va-rbac/about.md`](07-rollar-va-rbac/about.md).
- ⚠ TZ da RBAC **matritsasi** «Konsepsiya hujjatida» deb havola qilinadi, TZ ning o'zida to'liq keltirilmagan.

## 3. Audit jurnali
- Barcha web operatsiyalari (kirish, moderatsiya, administratsiya, billing, integratsiya, support) **audit jurnaliga** yoziladi (kim, qachon, nima, sababi bilan). Kritik operatsiyalarda sabab **majburiy** (A1).

## 4. Ichki foydalanuvchilar (§4.1.3.1)
- Administratorlar, moderatorlar va boshqa ichki foydalanuvchilar — kamida **20 ta ish o'rni**.

## 5. Malaka talablari (§4.1.3.3)
- **Administrator:** AT sohasida oliy ma'lumot; ≥2 yil tajriba; maxsus o'qitish.
- **Moderator:** o'rta-maxsus/oliy; moderatsiya siyosati bilan tanish; o'qitish.
- **Call-markaz operatori:** o'rta-maxsus; aloqa ko'nikmalari; o'qitish.
- **Texnik qo'llab-quvvatlash:** AT oliy ma'lumot; ma'lumotlar bazasi/tarmoq tajribasi.

## 6. Tezlik (web operatsiyalari, use-case'lardan)
| Operatsiya | Talab |
|---|---|
| Web kirish/autentifikatsiya | ≤ 5 s (parol ≤2 s) |
| Ro'yxatlarni yuklash (foydalanuvchi/so'rov/tranzaksiya) | ≤ 5 s |
| Hisobot shakllantirish | ⚠ **≤30 s (A2/A4)** — §4.1.4.1 jadvalda «10 s» ([`_konfliktlar.md`](_konfliktlar.md) W-A1) |
| Eksport (PDF/XLSX/CSV) | ≤ 15 s |
| Integratsiya sinov so'rovi | ≤ 15 s |

## 7. Platforma (§4.3.3, §4.3.4)
- Admin panel — **VueJS SPA** (zamonaviy SPA framework). ⚠ Kodbaza taqdim etilmagan.
- Backend umumiy (mobil bilan bir xil): Python (Django/FastAPI), PostgreSQL, REST (JSON).

## 8. Ish rejimi (§4.1.3.4)
- Administrator, moderator, call-markaz, support uchun ish rejimi «RENTME» MChJ ichki mehnat qoidalariga muvofiq (mobil 24/7 dan farqli).
