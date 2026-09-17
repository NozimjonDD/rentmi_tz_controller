> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)
>
> ⚠ R5 da Actual History stories mobil ilovada yashirilgan (kod saqlanadi) — [3-1 Asosiy sahifa](<../about.md>).

# IJ-02 — Actual stories ko'rish

| **Sseneriy ID** | IJ-02 |
| --- | --- |
| **Sseneriy nomi** | Actual stories ko'rish |
| **Guruh** | Asosiy sahifa |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi Actual story doirachalaridan birini bosib, full screen stories rejimida kontent ko'radi. |
| **Kirish sharti** | Asosiy sahifada; kamida bitta doira mavjud |
| **Chiqish natijasi** | Story ko'riladi; doiracha to'liq rangga o'tadi; CTA bosilsa tegishli sahifaga o'tiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Ijarachi** | Doirachani bosadi → full screen; progress bar; 5 sek avtomatik |
| **2** | **Ijarachi** | O'ng → keyingi; chap → oldingi; ko'rilgan doiracha to'liq rang |
| **3** | **Tizim** | Oxirgi story → avtomatik yopiladi → asosiy sahifa |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Guest** | Marketing kontent; CTA → ro'yxatdan o'tish |
| **CTA bosiladi** | Stories yopiladi → belgilangan sahifa |
| **X yoki swipe down** | Stories yopiladi → asosiy sahifa |
| **Birinchi storyda chap** | Amal bajarilmaydi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Media yuklanmadi** | Placeholder; davom etadi |
| **Internet yo'q** | Faqat kesh |
| **CTA havola noto'g'ri** | Asosiy sahifaga qaytiladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Dinamik tartib: skoring past → maslahat; to'lov kechikkan → ijara tarixi |
| **BQ-2** | Guest — faqat marketing kontent |
| **BQ-3** | Avtomatik 5 sek; qo'lda swipe ham |
| **BQ-4** | Ko'rilgan doiracha to'liq rang — seans davomida |
| **BQ-5** | Loop yo'q |
| **BQ-6** | Har story o'ziga xos CTA havolasi |
| **BQ-7** | X yoki swipe down bilan istalgan vaqtda yopiladi |
