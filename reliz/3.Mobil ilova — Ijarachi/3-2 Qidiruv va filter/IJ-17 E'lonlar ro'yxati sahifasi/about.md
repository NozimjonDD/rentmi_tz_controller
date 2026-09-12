> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-17 — E'lonlar ro'yxati sahifasi

| **Sseneriy ID** | IJ-17 |
| --- | --- |
| **Sseneriy nomi** | E'lonlar ro'yxati sahifasi (xarita + filter) |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | IJ-04, IJ-05, IJ-06 dan ochiladigan asosiy e'lonlar sahifasi. Ro'yxat va xarita ko'rinishlari o'rtasida almashtirish mumkin. Pin → mini kartochka → IJ-08. |
| **Kirish sharti** | IJ-04, IJ-05, IJ-06 dan yoki 'Hammasi >' bosilganda |
| **Chiqish natijasi** | Foydalanuvchi e'lonlarni ro'yxat yoki xarita ko'rinishida ko'radi |

## Asosiy oqim — Ro'yxat ko'rinishi

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Sarlavha: kategoriya nomi / qidiruv so'zi / 'Barcha e'lonlar'; natijalar soni; filterlar chip/badge |
| **2** | **Foydalanuvchi** | Ko'rinish almashtirish → IJ-03 sikli; Filter → IJ-06; E'lon → IJ-08 |

## Asosiy oqim — Xarita ko'rinishi

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | 'Xaritada ko'rish' (chap tepada) → Google Maps; e'lonlar pin sifatida narx bilan |
| **2** | **Foydalanuvchi** | Pinni bosadi → mini kartochka (rasm, nom, narx, maydon, qavat) → bosish → IJ-08 |
| **3** | **Foydalanuvchi** | Orqaga (←) → ro'yxat ko'rinishiga |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **'Hammasi >'** | Sarlavhada bo'lim nomi |
| **Chip o'chiriladi** | O'sha parametr olib tashlanadi; ro'yxat yangilanadi |
| **Bo'sh natija** | 'Topilmadi'; tugmalar |
| **Xaritada pin yo'q** | 'Bu hududda e'lonlar yo'q' |
| **Guest** | To'liq ochiq |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Banner; kesh; xarita yuklanmaydi |
| **Google Maps yuklanmadi** | Xabar; ro'yxatga o'tish taklif |
| **Server xatosi** | Xabar va Retry |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Sarlavha kontekstga qarab |
| **BQ-2** | 'Xaritada ko'rish' chap tepada; orqaga → ro'yxatga |
| **BQ-3** | Pin → mini kartochka: rasm, nom, narx, maydon, qavat |
| **BQ-4** | Mini kartochka → IJ-08 |
| **BQ-5** | Chip o'chirilganda parametr olib tashlanadi |
| **BQ-6** | Xarita pinlari dinamik yangilanadi |
| **BQ-7** | Guest va ro'yxatdan o'tgan uchun bir xil |
