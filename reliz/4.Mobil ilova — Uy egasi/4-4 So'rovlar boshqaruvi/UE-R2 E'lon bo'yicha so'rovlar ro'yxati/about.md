> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-R2 — E'lon bo'yicha so'rovlar ro'yxati**

| **Sseneriy nomi** | E'lon bo'yicha so'rovlar ro'yxati |
| --- | --- |
| **Guruh** | So'rov boshqaruvi |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi tanlangan mulk bo'yicha kelgan barcha so'rovlarni ko'radi. Holat tablari, ijarachi Rentmi skore va tezkor qaror tugmalari mavjud. Har bir kartada chat ikona orqali ijarachi bilan muloqot qilish mumkin. |
| **Kirish sharti** | UE-R1 dan mulk tanlangan; kamida bitta so'rov mavjud |
| **Chiqish natijasi** | Uy egasi so'rovlarni holat bo'yicha ko'radi; tafsilotga kiradi yoki tezkor qaror qabul qiladi |
| **Sseneriy ID** | UE-R2 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Sahifa ochiladi: header'da mulk nomi dropdown; tabs: Barchasi \| Yangi so'rovlar (badge) \| Rad etilgan \| Tasdiqlangan |
| 2 | **Tizim** | Har bir ijarachi kartasi: avatar + telefon raqami + holat badge + Rentmi gauge (N/100 + label: Ishonchli/O'rtacha/Ishonchsiz) + 'Batafsil' tugmasi + chat ikona |
| 3 | **Tizim** | Yangi so'rov kartasida: 'Qabul qilish' (ko'k) + 'Rad qilish' (pushti) tugmalari qo'shimcha ko'rsatiladi |
| 4 | **Uy egasi** | Tab tanlab filtrlaydi (Yangi so'rovlar / Rad etilgan / Tasdiqlangan) |
| 5 | **Uy egasi** | 'Batafsil' tugmasini bosadi → UE-R3 ga o'tiladi |
| 6 | **Uy egasi** | Chat ikonasini bosadi → UE-C1 chat ekrani ochiladi |
| 7 | **Uy egasi** | Dropdown (▼) bosiladi → Ko'chmas mulklar bottom sheet ochiladi; boshqa mulk tanlanadi → sahifa yangilanadi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Ro'yxat bo'sh (tanlangan tab bo'yicha)** | 'Bu holat bo'yicha so'rov yo'q' placeholder ko'rsatiladi |
| **Tezkor 'Qabul qilish'** | UE-R4 qabul oqimi ishga tushadi (UE-R3 ga o'tmasdan) |
| **Tezkor 'Rad qilish'** | UE-R4 rad oqimi ishga tushadi (UE-R3 ga o'tmasdan) |
| **Tasdiqlangan kartada** | Holat badge 'Tasdiqlangan' ko'rsatiladi; qaror tugmalari yo'q; chat ikona mavjud |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh; banner; pull-to-refresh faol |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Tabs: Barchasi \| Yangi so'rovlar \| Rad etilgan \| Tasdiqlangan; badge faqat Yangi so'rovlarda |
| **BQ-2** | 'Qabul qilish' va 'Rad qilish' tugmalari faqat Yangi so'rovlar holatida ko'rsatiladi |
| **BQ-3** | Chat ikona barcha holatlarda (yangi, tasdiqlangan, rad etilgan) ko'rsatiladi; faqat rad etilgan so'rovlarda chat ikona disabled |
| **BQ-4** | Dropdown orqali mulkni almashtirish mumkin — sahifa yangilanadi |
| **BQ-5** | Pull-to-refresh bilan holat va badge'lar yangilanadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | So'rovlar ro'yxati ≤3 s ichida yuklanadi |
| **AC-2** | Yangi so'rov kartasida 'Qabul qilish' va 'Rad qilish' tugmalari ko'rinadi; boshqa holatlarda ko'rinmaydi |
| **AC-3** | Chat ikona bosilganda UE-C1 chat ekrani ochiladi; rad etilgan so'rovda chat ikona disabled ko'rinadi |
| **AC-4** | Tab filtri bosilganda ro'yxat ≤2 s ichida yangilanadi |
| **AC-5** | Dropdown orqali mulk almashtirilganda so'rovlar yangi mulk bo'yicha ko'rsatiladi |
