# Yordam materiallari va muhitlar

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** 🟡 Qisman

## TZ manbai
TZ §4.1.10 — Qo'shimcha talablar (o'qitish materiallari, sinov muhitlari).
> **§4.1.10.1** «Video yo'riqnomalar — asosiy funksiyalar bo'yicha o'quv videolari… o'zbek (lotin va kirill), rus va ingliz tillarida»; «Interaktiv yordam bo'limi — tez-tez so'raladigan savollar»; «yozma qo'llanma — PDF formatida».
> **§4.1.10.2** «Development / Testing-Staging / Production muhitlari… mustaqil, alohida ma'lumotlar bazasi».
> **§4.1.10.3** «Mavjud tizimlar bilan integratsiya — 4.1.2-bandida» → [`_talablar.md`](../_talablar.md) §7.

## Reliz / R5
- **RELIZ:** `2-7 Profil`, `Settings` — FAQ va support bo'limlari sozlamalarda.
- **R5 o'zgarishi:** yo'q.

## 4.1.10.1 — O'qitish materiallari (mobil)

| Material | TZ talabi | Kodda | Holat |
|---|---|---|---|
| **Interaktiv yordam / FAQ** | tizim ichida savol-javob | `lib/features/faq` → `GET /mobile/faqs/`, route `/settings/faq` | ✅ |
| **Video yo'riqnomalar** | 4 tilda o'quv videolari | Kodda topilmadi | ❌ |
| **PDF qo'llanma** | batafsil PDF | Kodda topilmadi (skoring hisoboti PDF bor, lekin foydalanuvchi qo'llanmasi emas) | ❌ |

## 4.1.10.2 — Muhitlar (dev / staging / prod)
- **Kodda:** `AppConstants` uch muhitni qo'llab-quvvatlaydi — `_prodDomain` (`api-mobile-prod.rentmi.uz`), `_stageDomain` (`stage-api.rentmi.uz`), `_localDomain` (dev). `--dart-define=API_ENV=production` bilan almashtiriladi.
- **Developer vositasi:** ish vaqtida **base-URL switcher** (`BaseUrlStore` + `DioClient.setBaseUrl`) — staging/local ga o'tish; `lib/features/developer/…/tools_tab.dart`.
- **Holat:** ✅ (muhitlar ajratilgan; DB'lar backend tomonda alohida).

## 4.1.10.3 — Mavjud tizimlar bilan integratsiya
→ TZ §4.1.2 ga havola. Batafsil: [`_talablar.md`](../_talablar.md) §7 (Identifikatsiya/MyID, skoring, to'lov, SMS, push, xarita).

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi 'Yordam / FAQ' ni ochadi **WHEN** sahifa yuklanadi **THEN** tez-tez so'raladigan savollar ko'rsatiladi (`GET /mobile/faqs/`).
- **GIVEN** developer rejimi yoqilgan **WHEN** base-URL almashtiriladi **THEN** ilova staging/local muhitga ulanadi.

## Kod joylashuvi
- **FAQ:** `lib/features/faq` (`FaqCubit`, `faq_page`) → `GET /mobile/faqs/`.
- **Support (kontakt):** `lib/features/support` (statik — Telegram/telefon/email) → [`murojaat-t1.md`](murojaat-t1.md).
- **Muhitlar:** `lib/core/constants/app_constants.dart`, `lib/features/developer/…/tools_tab.dart`, `lib/core/network/base_url_store.dart`.

## Konflikt / farqlar
- ⚠ **Video yo'riqnomalar va PDF qo'llanma kodda yo'q** — TZ §4.1.10.1 talab qiladi (4 tilda), mobil ilovada mos ekran/resurs topilmadi. → [`_konfliktlar.md`](../_konfliktlar.md) (mobil bo'shliq).
- FAQ ✅ mavjud, lekin video/PDF qism amalga oshirilmagan.
