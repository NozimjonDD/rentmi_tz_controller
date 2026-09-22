# 12 — Elektron shartnoma (uyquda / dormant)

**Holat:** 💤 O'chirilgan (kodda to'liq bor, faol emas)

Elektron ijara shartnomasi — TZ bo'yicha **3-bosqich** funksiyasi (mazkur TZ 1-bosqich doirasiga kirmaydi). Kod bazasida to'liq yozilgan, ammo `TODO(contract-removal)` bilan o'chirib qo'yilgan: router case'lari va import'lar izohlangan, deep-link route'lari so'rovlar sahifasiga yo'naltiriladi.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`holat.md`](holat.md) | Nega o'chirilgan, 3-bosqich, uyqudagi endpointlar | — (3-bosqich) | 💤 |

## TZ manbai

R2 (5-qadam) — «Tasdiqlash: … mazkur TT doirasida ssenariy shu yerda yakunlanadi (keyingi bosqich — elektron ijara shartnomasi — **3-bosqichda**)». Ya'ni so'rov tasdiqlangach kontakt ochiladi, shartnoma esa keyingi bosqichga qoldiriladi.

## Kod modullari

`lib/features/contract` — to'liq clean-architecture modul: `contract_creation_bloc`, `contracts_list_bloc`, `contract_acceptance_bloc`; sahifalar `contract_creation_page`, `contract_view_page`, `contracts_list_page`, `offerta_page` va bosqichlar (`step1..step4`, tenant `step1_islamic_finance_page` va boshqalar).

## Uyqudagi endpointlar (chaqirilmaydi)

| Amal | Endpoint |
|---|---|
| Yaratish | `POST /mobile/contracts/create/` |
| Detal | `GET /mobile/contracts/detail/{id}/` |
| Holatni yangilash | `PATCH /mobile/contracts/update/{id}/` — `{status}` |
| Uy egasi ro'yxati | `GET /mobile/homeowner/contract/list/` |
| Ijarachi ro'yxati | `GET /mobile/tenant/contract/list/` |

> ⚠ **Holat:** funksiya kodda mavjud, lekin faol emas — 3-bosqichga qoldirilgan. Batafsil: [`holat.md`](holat.md), [`_konfliktlar.md`](../_konfliktlar.md).
