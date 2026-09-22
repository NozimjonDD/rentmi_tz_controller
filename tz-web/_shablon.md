# Shablon — tugun `about.md` uchun (web)

Har bir web use-case fayli quyidagi tuzilishga amal qiladi. `tz-mobile` shabloniga o'xshash, lekin **"Kod joylashuvi"** o'rniga **"Backend / API (kutilayotgan)"** — chunki web (VueJS) kodbazasi hozircha yo'q.

```markdown
# <Use-case ID> — <nomi>

**Rollar:** 🛡 Administrator / 🔍 Moderator / 🎧 Call-markaz / 🛠 Support    **Holat:** ✅ / 🟡 / 💤

## TZ manbai
<Use-case ID> · §4.1.1.4 · <1–3 jumla qisqacha>
> TZ dan aniq iqtibos.

## Reliz / R5
- **RELIZ / R5:** <admin panel bo'yicha o'zgarish yoki "yo'q">

## Ishga tushirish shartlari
<TZ dan>

## Bajarish tartibi
1. …

## Vaqt reglamenti
<TZ dan (agar bo'lsa)>

## Qabul kriteriyalari (BDD)
- **GIVEN** … **WHEN** … **THEN** …

## Backend / API (kutilayotgan)
- Web kodbaza taqdim etilmagan → endpointlar TZ va mobil backend asosida **taxmin qilinadi**.
- Mumkin bo'lgan yo'l: `/admin/...` yoki `/api/v1/...` namespace.

## Konflikt / farqlar
- ⚠ <ziddiyat> → [`_konfliktlar.md`](../_konfliktlar.md) yoki "Farq aniqlanmadi."
```

## Qoidalar
1. **TZ birlamchi manba** — har tugun TZ use-case matnidan aniq iqtibos oladi (§4.1.1.4).
2. **Web kod yo'q** — "Backend/API" bo'limi taxminiy; aniq endpoint yo'q joyda "aniqlanmagan" deb yoziladi (o'ylab topilmaydi).
3. **Holat** — TZ da to'liq belgilangan bo'lsa ✅; noaniq/qisman 🟡; keyingi bosqich 💤.
4. **Papka `about.md`** = modul indeksi; leaf = to'liq shablon.
5. Havolalar nisbatan (relative).
