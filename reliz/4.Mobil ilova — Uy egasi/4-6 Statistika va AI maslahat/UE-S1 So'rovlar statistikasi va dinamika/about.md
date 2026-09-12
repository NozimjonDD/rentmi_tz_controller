> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)
>
> ❓ AI maslahat kartochkasi bo'yicha R4 asosiy sahifasi bilan nomuvofiqlik — [4-6 Statistika va AI maslahat](<../about.md>).

**UE-S1 — So'rovlar statistikasi va dinamika**

| **Sseneriy nomi** | So'rovlar statistikasi va dinamika grafigi |
| --- | --- |
| **Guruh** | Statistika |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi tanlangan mulk bo'yicha so'rovlar statistikasini ko'radi: yangi, rad etilgan va tasdiqlangan so'rovlar soni, dinamika grafigi, e'lon to'ldirilganlik holati va AI maslahat kartochkasi. Period: 7, 30 yoki 90 kun. |
| **Kirish sharti** | UE-R1 da statistika ikona bosilgan |
| **Chiqish natijasi** | Uy egasi so'rovlar dinamikasini tahlil qiladi; AI maslahat yoki e'lon tahrirlashga o'tishi mumkin |
| **Sseneriy ID** | UE-S1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Statistika sahifasi ochiladi: sarlavha 'Ko'chmas mulklar bo'yicha so'rovlar statistikasi'; o'ng tepada ikona |
| 2 | **Tizim** | Mulklar gorizontal scroll: har bir karta — e'lon nomi, narx, manzil; E'lon to'ldirilganlik badge (N% To'ldirilgan — sariq/yashil/qizil rang) |
| 3 | **Tizim** | Period selector: 7 kun \| 30 kun \| 90 kun (default: 7 kun) |
| 4 | **Tizim** | AI maslahat kartochkasi (doim ko'rinadi): 'AI maslahat ✦' sarlavhasi + qisqa tavsif matni + 'AI maslahat ✦' tugmasi (gradient ko'k fon) |
| 5 | **Tizim** | 3 ta counter karta: 'Yangi so'rovlar' (N) \| 'Rad etilganlar' (N) \| 'Tasdiqlangan' (N) |
| 6 | **Uy egasi** | Counter kartani bosadi → tegishli rangda chart highlight va filled area ko'rsatiladi (yashil/qizil/ko'k) |
| 7 | **Tizim** | Dinamika multi-line chart: x-o'q — hafta kunlari; y-o'q — so'rovlar soni; 3 chiziq (yashil/qizil/ko'k) |
| 8 | **Uy egasi** | Gorizontal scroll orqali boshqa mulk tanlanadi → statistika yangilanadi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **AI maslahat kartochkasi bosiladi** | UE-AI1 modal ochiladi |
| **E'lon badge bosiladi** | UE-AI1 'E'lon bo'yicha' tabi ochiladi |
| **Period almashtiriladi (7/30/90)** | Counter va chart yangi period bo'yicha yangilanadi |
| **Counter karta bosib turish** | Faqat o'sha kategoriyadagi chart chizig'i highlight ko'rsatiladi; boshqalari xiralashtiradi |
| **So'rovlar bo'sh (tanlangan period)** | 'Bu davrda so'rov yo'q' placeholder; chart bo'sh ko'rsatiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh statistika; banner |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | AI maslahat kartochkasi doim ko'rsatiladi (7+ kun ijaraga berilmaganligiga bog'liq emas) |
| **BQ-2** | Default period: 7 kun |
| **BQ-3** | Counter karta bosilganda tegishli rang bilan chart filled area ko'rsatiladi |
| **BQ-4** | Mulk almashtirilganda barcha statistika (counter, chart, badge) yangi mulk bo'yicha yangilanadi |
| **BQ-5** | E'lon to'ldirilganlik badge rang kodi: <50% — qizil; 50–79% — sariq; 80%+ — yashil |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Sahifa ≤3 s ichida yuklanadi |
| **AC-2** | Period almashtirilganda counter va chart ≤2 s ichida yangilanadi |
| **AC-3** | Counter karta bosilganda tegishli rang bilan chart highlight ko'rsatiladi |
| **AC-4** | AI maslahat kartochkasi doim ko'rinib turadi — sahifani scroll qilganda ham |
| **AC-5** | Mulk almashtirish gorizontal scroll ishlaydi; tanlangan mulk statistikasi to'g'ri ko'rsatiladi |
