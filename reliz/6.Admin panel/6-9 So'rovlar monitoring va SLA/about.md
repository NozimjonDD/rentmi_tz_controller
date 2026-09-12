# 6-9 So'rovlar monitoring va SLA

**Manba:** [Release 4 14.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665) · [Release 5 17.08.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) · muddat (SLA): [4-5 SLA va javob vaqti](<../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>)

## Joriy talablar

- So'rovlar jadval ko'rinishi: ijarachi, uy egasi, e'lon nomi, sana, holat `R4`
- Holat bo'yicha filter: Barchasi | Yangi | Tasdiqlangan | Rad etilgan | Muddati o'tgan `R4`
  > Izoh: R5 da so'rov holatlariga "bekor qilingan" qo'shilgan — [3-8 So'rovlar](<../../3.Mobil ilova — Ijarachi/3-8 So'rovlar/about.md>).
- Qidiruv: ijarachi ismi yoki telefon, e'lon nomi bo'yicha `R4`
- Sana oralig'i filtri `R4`
- Jami so'rovlar soni, holat bo'yicha taqsimot statistikasi `R4`
- Ijarachi ma'lumotlari (Rentmi skore, ijara tarixi) — faqat ko'rish rejimi `R4`
- Uy egasi ma'lumotlari va qaror tarixi `R4`
- So'rov holati o'zgarish vaqt jadvali (audit trail) `R4`
- SLA monitoring: muddati o'tgan so'rovlar ro'yxati, uy egasi kesimida o'rtacha javob vaqti hisoboti `R5`
- So'rovlar monitoring bo'limiga SLA ko'rinishi qo'shiladi: "ko'rib chiqilmagan" (muddati o'tgan) so'rovlar ro'yxati (ijarachi, uy egasi, e'lon, o'tgan vaqt), uy egasi kesimida o'rtacha/mediana javob vaqti hisoboti, davr bo'yicha filtrlash va eksport. `R5 · R5-AD-02`
  > ⚠ Konflikt: R4 · AD-R1 BQ-5 da — Eksport funksionali yo'q
  >
  > ⚠ Konflikt: R4 · AD-R2 da — So'rov bekor qilingan (7 kun)
  >
  > Izoh: R5 eksportni SLA ko'rinishi uchun qo'shadi; so'rov muddati 7 kundan 24 soatga o'zgargan — [4-5 SLA va javob vaqti](<../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>).

## Use case'lar

| ID | Nomi | Reliz | Holati |
| --- | --- | --- | --- |
| [AD-R1](<AD-R1 So'rovlar monitoring ro'yxati/about.md>) | So'rovlar monitoring ro'yxati | R4 | ⚠ Eksport R5 da qo'shilgan |
| [AD-R2](<AD-R2 So'rov tafsilotlarini ko'rish/about.md>) | So'rov tafsilotlarini ko'rish | R4 | ⚠ 7 kunlik muddat R5 da 24 soat |
| [R5-AD-02](<R5-AD-02 SLA monitoring/about.md>) | SLA monitoring | R5 | Joriy |
