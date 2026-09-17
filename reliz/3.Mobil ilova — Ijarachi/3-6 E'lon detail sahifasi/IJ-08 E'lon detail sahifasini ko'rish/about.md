> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)
>
> ⚠ CTA nomi R5 da "Ariza jo'natish" — [3-6 E'lon detail sahifasi](<../about.md>).

# IJ-08 — E'lon detail sahifasini ko'rish

| **Sseneriy ID** | IJ-08 |
| --- | --- |
| **Sseneriy nomi** | E'lon detail sahifasini ko'rish |
| **Guruh** | E'lon ko'rish |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi e'lon detail sahifasini ko'radi. Sahifaga kirishda ko'rishlar soni (+1) avtomatik hisoblanadi. Gallery, qulayliklar, xarita, kommunal to'lovlar, o'xshash e'lonlar va amallar mavjud. |
| **Kirish sharti** | E'lon kartochkasi bosilgan yoki push notification orqali |
| **Chiqish natijasi** | E'lon to'liq ko'rsatiladi; ko'rishlar soni +1 hisoblanadi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Sahifa ochiladi — ko'rishlar (+1) darhol serverga yuboriladi |
| **2** | **Tizim** | Gallery: full-width, swipe, dot indicator, chips (xonalar, maydon, qavat) |
| **3** | **Tizim** | Asosiy blok: nom, manzil, narx; statistika: Ko'rildi, Ariza, Saqlangan (real-time) |
| **4** | **Tizim** | Garov depoziti + ⓘ standart matn; tezkor ma'lumotlar: xonalar, maydon, mebel, qavat, minimal ijara vaqti |
| **5** | **Tizim** | Qulayliklar (ichki + atrofdagi masofasi bilan); kimlar uchun chips; kommunal to'lovlar taqsimoti |
| **6** | **Tizim** | Google Maps embedded; tavsif; o'xshash e'lonlar (kategoriya + tuman + narx diapazoni) |
| **7** | **Tizim** | CTA: 'So'rov jo'natish' (ko'k) |
| **8** | **Foydalanuvchi** | Sevimlilar, 3 nuqta menyu, o'xshash e'lon — tegishli oqim ishga tushadi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Guest** | To'liq ko'radi; 'So'rov jo'natish' o'rnida 'Ro'yxatdan o'ting' |
| **Garov ⓘ** | Bottom sheet: standart matn — barcha e'lonlarda bir xil |
| **Sevimlilar toggle** | To'q rang — saqlangan; qayta bosish — olib tashlanadi |
| **3 nuqta menyusi** | Ulashish (IJ-10), Shikoyat (IJ-11), Blok (IJ-12) |
| **O'xshash e'lonni bosish** | Yangi IJ-08 ochiladi |
| **Push notification orqali** | To'g'ridan-to'g'ri ochiladi; orqaga → asosiy sahifa |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh; banner; Maps yuklanmaydi |
| **E'lon o'chirilgan** | 'Bu e'lon mavjud emas'; orqaga qaytish |
| **Rasm yuklanmadi** | Placeholder; ma'lumotlar davom etadi |
| **Maps yuklanmadi** | Xabar; manzil matni ko'rsatiladi |
| **Ko'rishlar xatosi** | Background qayta urinish; foydalanuvchiga ko'rsatilmaydi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Ko'rishlar (+1) kirishda avtomatik |
| **BQ-2** | Ko'rildi, Ariza, Saqlangan real-time |
| **BQ-3** | Garov ⓘ — barcha e'lonlarda bir xil standart matn |
| **BQ-4** | O'xshash e'lonlar: kategoriya + tuman + narx diapazoni |
| **BQ-5** | Guest: 'Ro'yxatdan o'ting' tugmasi |
| **BQ-6** | Sevimlilar faqat ro'yxatdan o'tganlarga |
| **BQ-7** | 3 nuqta: Ulashish, Shikoyat, Blok |
| **BQ-8** | O'xshash e'lon — yangi IJ-08; navigatsiya steki saqlanadi |
| **BQ-9** | E'lon o'chirilgan/arxivlangan — sahifa yuklanmaydi; xabar |
