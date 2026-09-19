# To'lovlar tarixi (tranzaksiyalar)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
B1 — To'lovlar tarixini ko'rish · Billing moduli (mobil). Foydalanuvchi barcha tranzaksiyalar ro'yxatini (sana, tur, summa, holat) ko'radi va tranzaksiya tafsilotlariga o'tadi. **1-bosqichda faqat skoring hisoboti xaridi tranzaksiyalari** ko'rsatiladi.
> «Tizim barcha tranzaksiyalar ro'yxatini ko'rsatadi (sana, tur, summa, holat); Foydalanuvchi tranzaksiyani tanlaydi va batafsil ma'lumotlarni ko'radi.»

## Reliz / R5
- **RELIZ:** to'lovlar ro'yxati `kind` (income/expense) va `from`/`to` sana oralig'i bo'yicha filtrlanadi; sahifalash (`page`/`page_size`) mavjud. Har tranzaksiyada OFD chek havolasi (`ofdUrl`) bo'lishi mumkin.
- **R5 o'zgarishi:** yo'q (R5 uy egasi "Daromadlarim" blokini "Tez kunda" holatida qoldiradi — real raqamlar 2–3-bosqichda).

## Bajarish tartibi
1. Foydalanuvchi 'Mening hisobotlarim' yoki profilda 'To'lovlar tarixi'ni ochadi.
2. `GET /mobile/payments/list/` — `{page, page_size, kind?, from?, to?}` (sana `yyyy-MM-dd`) chaqiriladi.
3. Ro'yxat sana bo'yicha guruhlanib ko'rsatiladi (`transaction_grouping`); har element ikon/label'ini `Transaction.purpose` belgilaydi.
4. Foydalanuvchi tranzaksiyani tanlab tafsilotlarni ko'radi; mavjud bo'lsa `ofdUrl` (OFD chek) ochiladi.
5. Ro'yxat bo'sh bo'lsa — bo'sh holat ekrani ('Hali to'lovlar amalga oshirilmagan').

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchida kamida bitta tranzaksiya bor **WHEN** to'lovlar tarixi ochiladi **THEN** sana/tur/summa/holat bilan ro'yxat ko'rsatiladi.
- **GIVEN** `from`/`to` filtri berilgan **WHEN** ro'yxat so'raladi **THEN** faqat shu oraliqdagi tranzaksiyalar qaytadi.
- **GIVEN** tranzaksiyada `ofdUrl` mavjud **WHEN** tafsilot ochiladi **THEN** OFD chek havolasi ko'rinadi.
- **GIVEN** tarix bo'sh **WHEN** sahifa ochiladi **THEN** 'Hali to'lovlar amalga oshirilmagan' xabari ko'rsatiladi.

## Kod joylashuvi
- **Modul:** `lib/features/transactions`
- **Sahifa / BLoC:** `TransactionsPage`, `TransactionCard`, `TransactionEmptyState` / `TransactionsBloc`; entity `Transaction` (`provider`, `amountUzs`, `status`, `kind`, `purpose`, `months`, `ofdUrl`, `paidAt`, `createdAt`), `TransactionsSummary`
- **Endpoint:** `GET /mobile/payments/list/` — `{page, page_size, kind(income|expense), from, to}`
- Enumlar: `TransactionKind{income, expense}`, `TransactionStatus{pending, success, failed, cancelled}`, `TransactionPurpose{electricity, gas, hotWater, coldWater, trash, rentmeReport, rentPayment, deposit}`

## Konflikt / farqlar
- ⚠ **Bosqich qamrovi:** TZ B1 keyingi bosqichlarda ijara (3-bosqich) va kommunal (2-bosqich) to'lovlarni ham va'da qiladi. `TransactionPurpose` enum ularni oldindan qamragan, lekin 1-bosqichda real ravishda faqat `rentmeReport` (skoring xaridi) keladi. → [`_konfliktlar.md`](../_konfliktlar.md) B6.
