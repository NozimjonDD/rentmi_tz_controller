> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)

**IJ-N1 — Xabarnoma ko'rish**

| **Sseneriy nomi** | Xabarnoma ko'rish (so'rovlar va xabarlar) |
| --- | --- |
| **Guruh** | Bildirishnomalar |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ijarachi xabarnoma sahifasida so'rovlar holati va chat xabarlari bo'yicha bildirishnomalarni ko'radi. Ikki tab mavjud: So'rovlar va Xabarlar. Barcha o'qilmagan xabarlarni bir vaqtda belgilash imkoniyati bor. |
| **Kirish sharti** | Ijarachi tizimga kirgan; kamida bitta bildirishnoma mavjud |
| **Chiqish natijasi** | Ijarachi bildirishnomalarni ko'radi va tegishli sahifaga o'ta oladi |
| **Sseneriy ID** | IJ-N1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | Xabarnoma (qo'ng'iroq) ikonasini bosadi yoki push notification'dan kiradi |
| 2 | **Tizim** | Xabarnoma sahifasi ochiladi: ✓✓ (mark all read) tugmasi o'ng tepada; 2 tab: 'So'rovlar (N)' \| 'Xabarlar (N)' |
| 3 | **Tizim** | So'rovlar tabida: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar sub-tabs |
| 4 | **Tizim** | Har bir bildirishnoma kartasi: holat ikona, e'lon mini-kartasi (rasm, nom, maydon, qavat, narx), sana/vaqt, o'qilmagan nuqta (ko'k) |
| 5 | **Tizim** | Tasdiqlangan bildirishnomada 'Uy egasi bilan bog'lanish' ko'k tugmasi ko'rsatiladi |
| 6 | **Ijarachi** | Bildirishnoma kartasini bosadi → IJ-R2 (so'rovlar) yoki IJ-C2 (xabarlar) ga o'tiladi |
| 7 | **Ijarachi** | ✓✓ tugmasi → barcha bildirishnomalar o'qilgan deb belgilanadi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Tasdiqlangan so'rov bildirishnomasi** | 'Uy egasi bilan bog'lanish' tugmasi bosilganda IJ-R3 modal ochiladi |
| **Rad etilgan so'rov bildirishnomasi** | Karta bosilganda IJ-R2 ga o'tiladi; o'sha e'lon (IJ-08) ga kirganida modal ko'rsatiladi |
| **Yangi chat xabari (Xabarlar tab)** | Karta bosilganda IJ-C2 chat ekrani ochiladi |
| **Xabarnomalar bo'sh** | 'Hali bildirishnoma yo'q' placeholder ko'rsatiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh bildirishnomalar; banner ko'rsatiladi |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | So'rovlar tab: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar sub-tabs |
| **BQ-2** | O'qilmagan bildirishnomalar ko'k nuqta bilan belgilanadi; bosilganda yo'qoladi |
| **BQ-3** | Tasdiqlangan so'rov bildirishnomada 'Uy egasi bilan bog'lanish' tugmasi ko'rsatiladi |
| **BQ-4** | ✓✓ tugmasi barcha tablar uchun umumiy — bir bosishda hammasi o'qilgan bo'ladi |
| **BQ-5** | Tab raqami (N) real-time o'qilmagan soni ko'rsatadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Xabarnoma sahifasi ≤3 s ichida yuklanadi |
| **AC-2** | So'rovlar tabida sub-tabs to'g'ri filtrlaydi |
| **AC-3** | Tasdiqlangan bildirishnoma kartasida 'Uy egasi bilan bog'lanish' tugmasi ko'rinadi |
| **AC-4** | ✓✓ bosilganda tab raqami (N) nolga tushadi va ko'k nuqtalar yo'qoladi |
| **AC-5** | Push notification orqali kelganida to'g'ridan-to'g'ri tegishli karta ko'rsatiladi |
