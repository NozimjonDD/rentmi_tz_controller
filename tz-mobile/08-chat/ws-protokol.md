# WebSocket protokoli (ulanish + message turlari)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
TZ da chat transporti (WebSocket) alohida belgilanmagan — chat R1/R2 ichida «uy egasi bilan chat qilish» / «chat orqali xabarlashish» sifatida umumiy eslatiladi. Real vaqtli aloqa mexanizmi **reliz R4** va kod darajasida aniqlangan.
> «(R1) ... uy egasi bilan chat qilish imkoniyati ochiladi.» · «(R2) ... chat orqali xabarlashish imkoniyati.»

## Reliz / R5
- **RELIZ (R4):** chat real vaqtli, doimiy ulanishga tayangan. Ulanish ilova ochilishida (`SplashBloc`) o'rnatiladi; token protokol sarlavhasida uzatiladi.
- **R5 o'zgarishi:** yo'q (R5 chat transportini o'zgartirmaydi; chat tugmasi UI'da tepaga ko'chiriladi, unread badge bilan).

## Bajarish tartibi
1. Ulanish: `wss://…/ws/chat/?device_id=<id>`; JWT `Sec-WebSocket-Protocol: jwt.<token>` sarlavhasida (access log'larda ko'rinmasligi uchun). Backend legacy `?token=` ni ham qabul qiladi.
2. Ulangach server `connection_established` freymini yuboradi (faqat informativ).
3. **Chiquvchi (client→server):** `message` `{content, request_id, new_chat, announcement_id?}`, `typing` `{request_id}`, `read` `{request_id}`, `message_history` `{request_id, page, limit}`, `chat_room_list` `{page, size}`, `delete_chat_room` `{request_id}`.
4. **Kiruvchi (server→client):** `message_history`, `message`, `typing`, `read`, `chat_room_list`, `chat_room_deleted`, `block_occurred`, `error` (`chat_blocked`), `connection_established`, `pong`.
5. Uzilganda eksponensial backoff bilan qayta ulanadi: 2 → 4 → 8 → 16 → 30 s (max), cheksiz urinish; qayta ulangach chat ro'yxati va tarix qayta so'raladi.
6. `request_id` = chat (rental_request) identifikatori; barcha xabarlar shu bilan bog'lanadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** yaroqli JWT token **WHEN** ilova ochiladi **THEN** WebSocket `jwt.<token>` protokoli bilan ulanadi va `connected` holatga o'tadi.
- **GIVEN** ulanish uzildi **WHEN** tarmoq tiklanadi **THEN** backoff bo'yicha qayta ulanadi va chat ro'yxati qayta so'raladi.
- **GIVEN** token yo'q/bo'sh **WHEN** ulanish urinilsa **THEN** ulanish rad etiladi (`No auth token`) va reconnect boshlanmaydi.

## Kod joylashuvi
- **Modul:** `lib/core/services/websocket_service.dart`
- **Sahifa / BLoC:** `WebSocketService` (`connect`, `send`, `requestMessageHistory`, `sendMessage`, `requestChatRoomList`, `requestDeleteChatRoom`, `forceReconnect`); `WebSocketState{disconnected, connecting, connected, reconnecting, error}`; `WebSocketMessageType` (message/typing/read/message_history/chat_room_list/delete_chat_room + kiruvchilar)
- **Endpoint:** `wss://…/ws/chat/?device_id=<id>` — `Sec-WebSocket-Protocol: jwt.<token>`

## Konflikt / farqlar
- ⚠ **Ping/pong o'chirilgan:** backend har xabar uchun `request_id` talab qilgani sababli ilova-darajasidagi ping yuborilmaydi; keep-alive protokol darajasida. Kiruvchi `pong` faqat log qilinadi. → [`_konfliktlar.md`](../_konfliktlar.md) B7.
- ⚠ Chat uchun **REST jonli oqim yo'q** — send/receive/history faqat WS orqali. → B7.
