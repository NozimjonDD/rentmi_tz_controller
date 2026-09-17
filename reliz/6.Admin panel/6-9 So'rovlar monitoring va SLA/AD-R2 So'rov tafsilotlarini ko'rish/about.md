> Manba: [Release 4 14.06.2026 · Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360160)
>
> ⚠ 7 kunlik muddat R5 da 24 soat — [4-5 SLA va javob vaqti](<../../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>).

**AD-R2 — So'rov tafsilotlarini ko'rish**

| **Sseneriy nomi** | So'rov tafsilotlarini ko'rish |
| --- | --- |
| **Guruh** | So'rovlar monitoring |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator tanlangan so'rovning to'liq tafsilotlarini ko'radi: ijarachi profili (Rentmi skore, to'lov intizomi, ijara tarixi), uy egasi ma'lumotlari, so'rov xabari, holat jadvali (audit trail) va ijarachi-uy egasi chat tarixi. Barcha ma'lumotlar faqat ko'rish rejimida (read-only). |
| **Kirish sharti** | AD-R1 da so'rov qatori bosilgan |
| **Chiqish natijasi** | Administrator so'rovning to'liq tarixini va barcha tomon ma'lumotlarini ko'radi |
| **Sseneriy ID** | AD-R2 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | So'rov tafsilot sahifasi ochiladi: sarlavha 'So'rov tafsilotlari'; ← (AD-R1 ga qaytish) |
| 2 | **Tizim** | Ijarachi bloki (read-only): avatar, ism, MyID holati, telefon, Rentmi skore gauge, ruxsat holati (Ha/Yo'q) |
| 3 | **Tizim** | So'rov bloki: so'rov xabari, yuborilgan sana/vaqt, joriy holat badge |
| 4 | **Tizim** | Ijarachi to'liq profili (read-only, toggle holatidan qat'iy nazar admin uchun barchasi ochiq): Daromadlar, To'lov intizomi (kredit byuro, MIB, soliq), Ijara tarixi (tavsiyanomalar, to'lov intizomi, kommunal, zarar, shikoyat, shartnoma) |
| 5 | **Tizim** | Uy egasi bloki (read-only): ism, telefon, e'lon nomi va manzili |
| 6 | **Tizim** | Holat o'zgarish jadvali (audit trail): har bir holat o'zgarishi — sana/vaqt, yangi holat, amal bajargan tomon |
| 7 | **Tizim** | Chat tarixi bo'limi: ijarachi va uy egasi o'rtasidagi barcha xabarlar, sana separatori bilan (read-only; rasm yuklab olish mumkin) |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Chat tarixi bo'sh** | So'rov yuborilgan lekin hali xabar almashilmagan bo'lsa 'Chat boshlanmagan' placeholder |
| **So'rov bekor qilingan (7 kun)** | Holat jadvali 'Ko'rib chiqilmagan' yozuvi bilan ko'rsatiladi |
| **← bosiladi** | AD-R1 ga qaytiladi; filter va scroll pozitsiyasi saqlanadi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q / server xatosi** | Xabar va Retry; kesh ma'lumotlar ko'rsatiladi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Barcha ma'lumotlar faqat ko'rish rejimida — hech qanday tahrirlash yoki holat o'zgartirish imkoni yo'q |
| **BQ-2** | Admin uchun ijarachi profili toggle holatidan qat'iy nazar to'liq ko'rsatiladi (daromadlar, ijara tarixi xiralashtirilmaydi) |
| **BQ-3** | Chat tarixi barcha xabarlarni ko'rsatadi — o'chirilgan xabarlar ham '\[O'chirilgan xabar\]' ko'rinishida aks etadi |
| **BQ-4** | Holat audit trail: so'rov yaratilganidan boshlab barcha holat o'zgarishlari sana/vaqt va amal bajargan tomon bilan |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Sahifa ≤3 s ichida yuklanadi |
| **AC-2** | Ijarachi Rentmi skore gauge to'g'ri qiymat va rang bilan ko'rsatiladi |
| **AC-3** | Chat tarixi to'liq xronologik tartibda ko'rsatiladi; rasm xabarlar preview sifatida aks etadi |
| **AC-4** | Holat audit trail barcha o'zgarishlarni sana/vaqt bilan ko'rsatadi |
| **AC-5** | Sahifada hech qanday tahrirlash elementi (input, button) yo'q — faqat ko'rish |
