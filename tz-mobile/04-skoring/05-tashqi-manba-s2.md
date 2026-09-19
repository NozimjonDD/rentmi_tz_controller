# S2 — Tashqi manbadan skoring ma'lumoti

**Rollar:** 👤 Ijarachi (backend jarayoni)    **Holat:** 🟡 Qisman (mobil tomonda alohida endpoint yo'q)

## TZ manbai
S2 — Skoring ma'lumotlarini tashqi manbadan olish · §4.1.1.4 (S2, S1 tarkibida). Tizim tashqi skoring/kredit byurosi xizmatiga autentifikatsiyalangan so'rov jo'natadi va javobni (kredit reytingi, tarix, soliq qarzdorligi) S1 ga uzatadi.
> «Tizim tashqi skoring xizmatiga autentifikatsiyalangan so'rov jo'natadi …; Tashqi xizmat javob qaytaradi (kredit reytingi, tarix, soliq qarzdorligi va boshqa ko'rsatkichlar); Ma'lumotlar S1 ga uzatiladi.»
> Kengaytma: «Tashqi xizmat mavjud emas → 'ma'lumot olinmadi' holati, S1 faqat ichki ma'lumotlar asosida davom etadi.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6` — natijada «kredit tarixi ma'lumotlari, qarzdorliklar» ko'rsatiladi (tashqi manba natijasi). Alohida S2 user-story mobil relizda ajratilmagan.
- **R5 o'zgarishi:** «Tashqi skoring xizmati mavjud bo'lmasa, bal ichki ma'lumotlar asosida hisoblanadi» (TZ §4.2.1 bilan mos) `R5 · §5 (rule-based v1)`.

## Bajarish tartibi
1. Tashqi manbaga so'rov **backend ichida** amalga oshiriladi — mobil ilova bevosita chaqirmaydi.
2. Mobil faqat `POST /scoring/check/` → `GET /scoring/status/` orqali natijani oladi ([`03-hisoblash-process.md`](03-hisoblash-process.md)).
3. Tashqi manba holati natijada `DataQualityFlags` orqali aks etadi: `cbNoData`/`cbStale` (kredit byurosi), `mibNoData`/`mibStale` (MIB/soliq), `noDataCap`.
4. Manba mavjud bo'lmasa bal ichki ma'lumot asosida hisoblanadi va sifat bayrog'i ko'rsatiladi (data-quality warning widget).

## Qabul kriteriyalari (BDD)
- **GIVEN** tashqi xizmat javob berdi **WHEN** skoring hisoblanadi **THEN** kredit/soliq ko'rsatkichlari faktorlarga qo'shiladi (`credit`, `mib`).
- **GIVEN** tashqi xizmat mavjud emas/timeout **WHEN** hisoblash davom etadi **THEN** bal faqat ichki ma'lumot asosida hisoblanadi va `DataQualityFlags` (`cbNoData`/`mibNoData`) belgilanadi.
- **GIVEN** ma'lumot eskirgan **WHEN** natija ko'rsatiladi **THEN** `cbStale`/`mibStale` ogohlantirishi chiqadi.

## Kod joylashuvi
- **Modul:** backend (kredit byurosi/soliq integratsiyasi); mobil — `lib/features/scoring`
- **Sahifa / BLoC:** alohida sahifa yo'q; `DataQualityFlags` entity + `data_quality_warning` widget natija sahifasida
- **Endpoint:** mobilda alohida S2 endpoint **yo'q** — `POST /mobile/scoring/check/` → `GET /mobile/scoring/status/` orqali bilvosita

## Konflikt / farqlar
- ⚠ **Mobil qamrov:** S2 to'liq backend ichida bajariladi, mobil tomonda alohida endpoint/ekran yo'q — shu sababli holat 🟡. → [`_konfliktlar.md`](../_konfliktlar.md).
- Tashqi manba yo'qligida ichki ma'lumot asosida davom etish TZ (§4.2.1) va R5 bilan mos. Boshqa farq aniqlanmadi.
