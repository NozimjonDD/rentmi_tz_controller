# 08 — Chat (aloqa)

Ijarachi ↔ uy egasi o'rtasida real vaqtli xabarlashuv (matn, rasm, fayl). Chat **faqat WebSocket** orqali ishlaydi — jonli xabar oqimi, typing, o'qildi kvitansiyalari va chat ro'yxati WS-push orqali keladi. TZ da chat alohida use-case sifatida ajratilmagan, **R1** (ijara so'rovini yuborish) va **R2** (so'rovni ko'rib chiqish) ichida «uy egasi bilan chat / chat orqali xabarlashish» sifatida eslatiladi; to'liq oqim **reliz R4** da spetsifikatsiyalangan.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`ws-protokol.md`](ws-protokol.md) | WebSocket ulanish, autentifikatsiya, reconnect, message turlari | (reliz R4) | ✅ |
| [`xabar-va-bloklash.md`](xabar-va-bloklash.md) | Chat ro'yxati / detali, fayl yuklash, bloklash (`block_occurred`) | R1, R2 (reliz R4) | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
app start (SplashBloc) → WebSocket.connect()  [JWT: Sec-WebSocket-Protocol: jwt.<token>]
   chat ro'yxati:  ChatListBloc → requestChatRoomList() → WS "chat_room_list" push
       ChatType bo'yicha: rented (Ijaraga olingan) / rentedOut (Ijaraga berilgan)
   chat detali:   ChatDetailBloc → requestMessageHistory(page, limit)
       yuborish:  sendMessage {content, request_id, new_chat, announcement_id?}
       kiruvchi:  "message" / "typing" / "read" / "block_occurred" / error(chat_blocked)
   uzilishda:     eksponensial backoff reconnect (2→4→8→16→30 s), cheksiz urinish
```

> ⚠ **Kod TZ/reliz'dan farq qiladi:** (1) Chat'da **24 soatlik SLA / countdown YO'Q** — R5 dagi «Javob berishingiz kerak: HH:MM:SS» taymeri faqat **so'rovlar boshqaruviga** (R2 / [`07-sorovlar/`](../07-sorovlar/about.md)) tegishli. (2) Chat **REST API amalda yo'q** — barcha jonli oqim WebSocket orqali; faqat `GET /mobile/chat/list/` pre-connect fallback sifatida qoladi. Batafsil: [`_konfliktlar.md`](../_konfliktlar.md) B7, B8.

## Kod modullari

`lib/features/chat` — bloklar `ChatListBloc`, `ChatDetailBloc`; sahifalar `ChatListPage`, `ChatDetailPage`, `ChatDetailLoaderPage`. Yadro xizmati `lib/core/services/websocket_service.dart` (`WebSocketService`, `WebSocketMessageType`). Fayl yuklash `chat_file_service` (multipart). Bloklash integratsiyasi `lib/features/blocks`.

## Asosiy kanallar / endpointlar

| Amal | Kanal / Endpoint |
|---|---|
| WebSocket ulanish | `wss://…/ws/chat/?device_id=<id>` — JWT `Sec-WebSocket-Protocol: jwt.<token>` |
| Chat ro'yxati (WS) | chiquvchi `chat_room_list` `{page, size}` → kiruvchi `chat_room_list` (results, unread_count) |
| Xabar tarixi (WS) | chiquvchi `message_history` `{request_id, page, limit}` → kiruvchi `message_history` |
| Xabar yuborish (WS) | `message` `{content, request_id, new_chat, announcement_id?}` |
| Chat ro'yxati (REST fallback) | `GET /mobile/chat/list/` — `{my_property, page, page_size}` |
| Fayl yuklash | `chat_file_service` — multipart upload, so'ng WS `message` (`file_id`/`media_url`) |
