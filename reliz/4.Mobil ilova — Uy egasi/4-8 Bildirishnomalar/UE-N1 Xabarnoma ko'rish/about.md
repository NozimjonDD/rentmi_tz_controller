> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-N1 — Xabarnoma ko'rish**

| **Sseneriy nomi** | Xabarnoma ko'rish (so'rovlar va xabarlar) |
| --- | --- |
| **Guruh** | Bildirishnomalar |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi xabarnoma sahifasida yangi so'rovlar va chat xabarlari bo'yicha bildirishnomalarni ko'radi. Ikki tab: So'rovlar va Xabarlar. Barcha bildirishnomalarni bir vaqtda o'qilgan deb belgilash imkoniyati bor. |
| **Kirish sharti** | Uy egasi tizimga kirgan; kamida bitta bildirishnoma mavjud |
| **Chiqish natijasi** | Uy egasi bildirishnomalarni ko'radi va tegishli sahifaga o'ta oladi |
| **Sseneriy ID** | UE-N1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | Xabarnoma ikonasini bosadi yoki push notification'dan kiradi |
| 2 | **Tizim** | Xabarnoma sahifasi: ✓✓ (mark all read) o'ng tepada; 2 tab: 'So'rovlar (N)' \| 'Xabarlar (N)' |
| 3 | **Tizim** | So'rovlar tabida sub-tabs: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar |
| 4 | **Tizim** | Har bir bildirishnoma kartasi: holat ikona, ijarachi ismi + Rentmi bali (qisqa), e'lon mini-kartasi, sana/vaqt, o'qilmagan nuqta (ko'k) |
| 5 | **Tizim** | Yangi so'rov bildirishnomasi kartasida: 'Qabul qilish' + 'Rad qilish' tezkor tugmalari ko'rsatiladi |
| 6 | **Uy egasi** | Bildirishnoma kartasini bosadi → UE-R2 (so'rovlar) yoki UE-C1 (xabarlar) ga o'tiladi |
| 7 | **Uy egasi** | ✓✓ tugmasi → barcha bildirishnomalar o'qilgan belgilanadi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Yangi so'rov bildirishnomasi (tezkor qaror)** | 'Qabul qilish' → UE-R4 qabul oqimi; 'Rad qilish' → UE-R4 rad oqimi |
| **Chat xabari bildirishnomasi** | Karta bosilganda UE-C1 chat ekrani ochiladi |
| **Xabarnomalar bo'sh** | 'Hali bildirishnoma yo'q' placeholder ko'rsatiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh bildirishnomalar; banner |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | So'rovlar tab sub-tabs: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar |
| **BQ-2** | Yangi so'rov bildirishnomasi kartasida tezkor 'Qabul qilish' / 'Rad qilish' tugmalari mavjud |
| **BQ-3** | O'qilmagan bildirishnomalar ko'k nuqta bilan belgilanadi; bosilganda yo'qoladi |
| **BQ-4** | ✓✓ tugmasi barcha tablar uchun umumiy |
| **BQ-5** | Tab raqami (N) real-time o'qilmagan soni ko'rsatadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Xabarnoma sahifasi ≤3 s ichida yuklanadi |
| **AC-2** | Yangi so'rov kartasida tezkor 'Qabul qilish' va 'Rad qilish' tugmalari ko'rinadi |
| **AC-3** | ✓✓ bosilganda tab raqami (N) nolga tushadi va ko'k nuqtalar yo'qoladi |
| **AC-4** | Push notification orqali kelganida tegishli bildirishnoma highlight ko'rsatiladi |
