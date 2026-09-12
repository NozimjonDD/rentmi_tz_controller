> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-R1 — So'rovlar asosiy sahifasi**

| **Sseneriy nomi** | So'rovlar asosiy sahifasi (mulklar va umumiy ko'rinish) |
| --- | --- |
| **Guruh** | So'rov boshqaruvi |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi 'So'rovlar' tabida o'ziga tegishli barcha mulklar bo'yicha umumiy so'rovlar sonini ko'radi. Har bir mulk kartasida yangi so'rovlar badge'i ko'rsatiladi. Statistika sahifasiga va muayyan mulk so'rovlariga o'tish mumkin. |
| **Kirish sharti** | Uy egasi tizimga kirgan; kamida bitta faol e'loni mavjud |
| **Chiqish natijasi** | Uy egasi mulklar ro'yxatini va so'rovlar umumiy sonini ko'radi; kerakli mulkni tanlab UE-R2 ga o'tadi |
| **Sseneriy ID** | UE-R1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | Bottom navigation'dagi 'So'rovlar' tabini bosadi |
| 2 | **Tizim** | Sahifa yuklanadi: sarlavha 'So'rovlar', o'ng tepada statistika ikona |
| 3 | **Tizim** | Header: 'Boy aka! Ko'chmas mulklaringiz bo'yicha umumiy N ta so'rov mavjud' |
| 4 | **Tizim** | Mulklar ro'yxati: har bir karta — e'lon nomi, narx, manzil, '+N yangi so'rov' yashil badge |
| 5 | **Uy egasi** | Mulk kartasini bosadi → UE-R2 ga o'tiladi (o'sha mulk bo'yicha so'rovlar ro'yxati) |
| 6 | **Uy egasi** | Statistika ikonasini bosadi → UE-S1 ga o'tiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Yangi so'rov yo'q mulk** | Badge ko'rsatilmaydi; karta odatiy ko'rinishda |
| **Barcha so'rovlar ko'rib chiqilgan** | '+N yangi so'rov' badge yo'qoladi |
| **Mulklar ro'yxati bo'sh** | 'Hali e'lon yo'q. E'lon qo'shing' placeholder va '+' tugmasi ko'rsatiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh ma'lumotlar; 'Internet aloqasi yo'q' banner; pull-to-refresh faol |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Faqat uy egasining o'ziga tegishli e'lonlar ko'rsatiladi |
| **BQ-2** | '+N yangi so'rov' badge faqat ko'rib chiqilmagan (pending) so'rovlar sonini ko'rsatadi |
| **BQ-3** | Umumiy so'rovlar soni header'da real-time yangilanadi |
| **BQ-4** | Pull-to-refresh bilan ro'yxat va badge'lar yangilanadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Sahifa ≤3 s ichida yuklanadi |
| **AC-2** | Har bir mulk kartasida yangi so'rovlar soni to'g'ri ko'rsatiladi |
| **AC-3** | Mulk kartasi bosilganda UE-R2 ochiladi va tegishli mulk bo'yicha so'rovlar ko'rsatiladi |
| **AC-4** | Statistika ikona bosilganda UE-S1 sahifasi ochiladi |
