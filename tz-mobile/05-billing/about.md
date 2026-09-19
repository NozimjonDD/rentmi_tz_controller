# 05 — Billing / to'lovlar

To'lovlar tarixini ko'rish va to'lov provayderlari bilan integratsiya. **1-bosqichda faqat skoring hisoboti (Rentmi hisoboti) xaridi tranzaksiyalari** ko'rsatiladi; ijara to'lovlari (3-bosqich) hamda xizmat/kommunal to'lovlar (2-bosqich) keyingi bosqichlarga qoldirilgan. TZ use-case: **B1** (to'lovlar tarixini ko'rish). Skoring hisobotining o'zini xarid qilish TZ **S1** ga tegishli — bu yerda uning to'lov (billing) qismi hujjatlanadi.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`provayderlar.md`](provayderlar.md) | To'lov provayderlari: Atmos (karta+OTP), Payme, Click, Uzum | S1 (4–5 qadam) | ✅ |
| [`universal-order.md`](universal-order.md) | Universal Order — skoring access gate (paid Order = access) | S1 | ✅ |
| [`tranzaksiyalar.md`](tranzaksiyalar.md) | To'lovlar tarixi ro'yxati va tafsilotlari (OFD chek) | B1 | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
skoring xaridi (S1) → provayder tanlash
   Atmos:  karta bind/init → bind/confirm(OTP) → payment/create → pre-apply → apply(OTP)
   Payme:  payme/create-order → payUrl → tashqi ilova → payme/order/{id}/ (status)
   Click:  click/order-create → payUrl → tashqi ilova → click/status/
   Uzum:   orders/create → deepLink → tashqi ilova → orders/{id}/status/
       → POST /mobile/universal/orders/ {provider, amount}  → Order(status=new)
       → provayder to'lovni tasdiqlaydi → Order.status=paid, scoringId bog'lanadi
           → "paid Order mavjud" = skoring access OCHILADI
to'lovlar tarixi (B1): GET /mobile/payments/list/ → Transaction ro'yxati (kind, from/to)
```

> ⚠ **Kod TZ'dan farq qiladi:** (1) B1 1-bosqichda faqat skoring xaridi tranzaksiyalari; `Transaction.purpose` enum kommunal/ijara turlarini oldindan qamragan, lekin real ravishda faqat `rentmeReport` keladi. (2) Pro/obuna (subscription) — **legacy shim**: gating `paid Order` mavjudligiga tayanadi, `/subscription/*` endpointlar kodda **yo'q** (`TODO_SUBSCRIPTION.md`, to'lov hozircha simulyatsiya). Batafsil: [`_konfliktlar.md`](../_konfliktlar.md) B5, B6.

## Kod modullari

`lib/features/subscription` — to'lov provayderlari, Universal Order, Pro shim · `lib/features/transactions` — B1 to'lovlar tarixi. Bloklar: `PaymentBloc` (Atmos), `PaymeBloc`, `ClickBloc`, `UzumBloc`, `SubscriptionCubit` (Order gate), `PaymentStatusCubit`, `TransactionsBloc`.

## Pul birligi

- **Tiyin:** Atmos (`priceTiyin`) — 1 so'm = 100 tiyin.
- **So'm:** Payme / Click / Uzum va Universal Order (`amount`).

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Faol order | `GET /mobile/orders/active/` → `Order` yoki 204 (null) |
| Order yaratish | `POST /mobile/universal/orders/` — `{provider, amount}` → `Order` |
| Karta ro'yxati | `GET /mobile/card/list/` |
| Karta bog'lash | `POST /mobile/card/bind/init/` · `POST /mobile/card/bind/confirm/` (OTP) |
| Karta o'chirish | `DELETE /mobile/card/{id}/delete/` |
| Atmos to'lov | `POST /mobile/payment/create/` · `/payment/pre-apply/` · `/payment/apply/` (OTP) |
| Payme | `POST /mobile/payme/create-order/` · `GET /mobile/payme/order/{id}/` |
| Click | `POST /mobile/click/order-create/` · `POST /mobile/click/status/` |
| Uzum | `POST /mobile/orders/create/` · `GET /mobile/orders/{id}/status/` |
| Provayder holati | `GET /mobile/payments/status/` |
| To'lovlar tarixi (B1) | `GET /mobile/payments/list/` — `{page, page_size, kind, from, to}` |
