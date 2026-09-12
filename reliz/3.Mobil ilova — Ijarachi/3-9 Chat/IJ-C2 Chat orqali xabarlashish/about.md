> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)

**IJ-C2 — Chat orqali xabarlashish**

| **Sseneriy nomi** | Chat orqali xabarlashish |
| --- | --- |
| **Guruh** | Chat |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ijarachi uy egasi bilan chat orqali matn va rasm almashadi. Ijarachi faqat o'zi yuborgan xabarlarni tahrirlashi yoki o'chirishi mumkin. Xabar uzun bosilganda amallar menyusi, multi-select rejim, header search va 3-nuqta menyu mavjud. |
| **Kirish sharti** | IJ-C1 da chat tanlangan yoki IJ-R3 'Chat orqali yozish' bosilgan |
| **Chiqish natijasi** | Ijarachi uy egasiga xabar yuboradi; xabar threadda ko'rsatiladi |
| **Sseneriy ID** | IJ-C2 |

**Asosiy oqim — Matn xabar yuborish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Chat ekrani ochiladi: yuqorida mulk mini-kartasi (nomi, manzil, maydon, narx); sarlavhada uy egasi ismi + 'N daqiqa oldin onlayn edi'; qidiruv va 3-nuqta ikonalari |
| 2 | **Tizim** | Xabar tarixi yuklanadi: sana separator, ijarachi xabarlari o'ngda (yashil), uy egasi xabarlari chapda (oq) |
| 3 | **Ijarachi** | Matn maydoniga bosadi, xabar yozadi, yuborish tugmasini bosadi |
| 4 | **Tizim** | Xabar threadga qo'shiladi; ✓ belgisi ko'rinadi (yuborildi); uy egasi o'qigach ✓✓ bo'ladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Rasm yuborish** | Paperclip ikonasini bosish → galereya ochiladi → rasm tanlanadi → 2-ustun grid preview ko'rsatiladi → yuborish |
| **Xabarni tahrirlash (faqat o'zining)** | Uzun bosish → 'Tahrirlash' tanlash → matn maydoni to'ldiriladi → saqlash; faqat ijarachining o'z xabariga amal qo'llanadi |
| **Xabarni o'chirish (faqat o'zining)** | Uzun bosish → 'O'chirish' → tasdiqlash modali → o'chiriladi; faqat ijarachining o'z xabariga amal qo'llanadi |
| **Nusxa olish** | Uzun bosish → 'Nusxa olish' → bufer xotiraga nusxalanadi |
| **Qaytarish (Reply)** | Uzun bosish → 'Qaytarish' → matn maydonida quote ko'rsatiladi → yangi xabar quote bilan yuboriladi |
| **Multi-select rejim** | Bitta xabar uzun bosiladi → checkbox rejimi → bir nechta xabar tanlanadi → mass copy yoki mass delete |
| **Xabarda qidiruv** | Header search ikonasi → qidiruv satri → matn kiritiladi → mos xabarlarga scroll |
| **3-nuqta menyu** | 'Telefon qilish' → uy egasiga qo'ng'iroq; 'Block qilish' → IJ-C3 ga o'tish |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Xabar saqlanmaydi; 'Internet aloqasi yo'q' xabari; matn saqlanib qoladi |
| **Rasm hajmi >5 MB** | 'Fayl hajmi ruxsat etilganidan katta' xabari; yuklanmaydi |
| **Server xatosi** | Xabar yuborilmadi belgisi; Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Ijarachi faqat o'zi yuborgan xabarlarni tahrirlashi va o'chirishi mumkin; uy egasining xabarlariga bu amallar qo'llanilmaydi |
| **BQ-2** | Delivery status: ✓ — yuborildi, ✓✓ — o'qildi |
| **BQ-3** | Rasm formati: jpg, png, pdf; hajm: ≤5 MB |
| **BQ-4** | Xabarlar sana separatori bilan guruhlangan (kun bo'yicha) |
| **BQ-5** | Mulk mini-kartasi chatning kontekstini doimo ko'rsatib turadi |
| **BQ-6** | Multi-select rejimda faqat o'z xabarlarini mass delete qilish mumkin |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Xabar yuborilgandan ≤1 s ichida threadda ko'rsatiladi |
| **AC-2** | Faqat ijarachining o'z xabarida uzun bosishda 'Tahrirlash' va 'O'chirish' variantlari ko'rinadi; uy egasining xabarida faqat 'Nusxa olish' va 'Qaytarish' ko'rinadi |
| **AC-3** | Rasm 2-ustun grid preview ko'rsatiladi; yuborilgandan keyin chat threadda ko'rsatiladi |
| **AC-4** | Uy egasi xabarni o'qiganda ✓ → ✓✓ ga o'tadi |
| **AC-5** | Qidiruv mos xabarga avtomatik scroll qiladi |
| **AC-6** | 3-nuqta 'Telefon qilish' bosilganda qurilma telefon ilovasi uy egasi raqami bilan ochiladi |
