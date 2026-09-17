> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-04 — Kategoriya bo'yicha e'lonlarga o'tish

| **Sseneriy ID** | IJ-04 |
| --- | --- |
| **Sseneriy nomi** | Kategoriya bo'yicha e'lonlarga o'tish (hot categories) |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi hot categories chipsidan birini bosib IJ-17 ga o'tadi. Kategoriya filter sifatida qo'llaniladi. |
| **Kirish sharti** | Asosiy sahifada; hot categories mavjud |
| **Chiqish natijasi** | Kategoriya filtrlangan IJ-17 ochiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | Chipsidan birini bosadi → kategoriya filter; IJ-17 ochiladi — sarlavhada kategoriya nomi |
| **2** | **Foydalanuvchi** | Qo'shimcha filter (IJ-06) yoki orqaga → asosiy sahifa |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Avval filter bor** | Kategoriya mavjud filtrlarga qo'shiladi |
| **Kategoriyada e'lon yo'q** | Placeholder |
| **Guest** | Cheklovsiz |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Xabar; Retry |
| **Server xatosi** | Xabar va Retry |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Chip → to'g'ridan-to'g'ri IJ-17; aktiv holat yo'q |
| **BQ-2** | Bir vaqtda bitta kategoriya |
| **BQ-3** | Mavjud filtrlarga qo'shiladi — filter tozalanmaydi |
| **BQ-4** | Sarlavhada kategoriya nomi |
| **BQ-5** | Orqaga → asosiy sahifa |
| **BQ-6** | Guest va ro'yxatdan o'tgan uchun bir xil |
