# Xabar (ro'yxat/detal) va bloklash

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
R1 — Ijara so'rovini yuborish · R2 — Ijara so'rovini ko'rib chiqish (So'rovlar boshqaruvi moduli). Chat so'rov oqimi ichida ijarachi va uy egasi o'rtasidagi xabarlashuv kanali sifatida ochiladi.
> «(R2) ... so'rov xabari va chat orqali xabarlashish imkoniyati.»

## Reliz / R5
- **RELIZ (R4):** chat ro'yxati ikki tabga bo'linadi — Ijaraga olingan (`rented`) / Ijaraga berilgan (`rentedOut`); har chatda o'qilmagan hisoblagich (`unread_count`). Xabar turlari: matn, rasm, fayl. Foydalanuvchini bloklash mumkin (chat ko'rinishda qoladi, lekin qulf ikoni bilan). 
- **R5 o'zgarishi:** yo'q (chat mantig'i o'zgarmaydi; asosiy sahifada chat tugmasi tepaga chiqariladi, «faqat platforma orqali muloqot» xavfsizlik xabari qo'shiladi).

## Bajarish tartibi
1. **Ro'yxat:** `ChatListBloc` `requestChatRoomList()` yuboradi; WS `chat_room_list` push kelganda chatlar `ChatType` bo'yicha ajratiladi. REST ishlatilmaydi. Bloklangan foydalanuvchilar keshi (`BlockRepository`) bilan annotatsiya qilinadi.
2. **Detal:** `ChatDetailBloc` `requestMessageHistory(page, limit)` bilan tarixni yuklaydi; server yangi-eskidan qaytaradi, UI eski-yangiga teskari qiladi. Sahifalash: `LoadMoreMessages`.
3. **Yuborish:** `sendMessage {content, request_id, new_chat, announcement_id?}`. Xabar serverdan qaytib kelganda ro'yxatga qo'shiladi (optimistik emas). `typing` 3 soniyada avtomatik o'chadi.
4. **Fayl:** `chat_file_service` multipart bilan yuklaydi (`getFileType`/`getMessageType`), so'ng WS `message` `{message_type, file_id, media_url}` (yoki bir nechta uchun `file_ids`, `media_urls`).
5. **Bloklash:** kiruvchi `block_occurred` `{other_user_id, action, direction}` — `ChatDetailState.pendingBlockEvent` ga yoziladi va sahifa `BlockStatusCubit` ga uzatadi. `error` `message=chat_blocked` bo'lsa — blok holati qayta yuklanadi.
6. **O'chirish:** `DeleteChat` optimistik olib tashlaydi va `delete_chat_room` yuboradi; server soft-delete qilib yangi `chat_room_list` push qiladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** WS ulangan **WHEN** chat ro'yxati so'raladi **THEN** chatlar `rented`/`rentedOut` tablarga ajratilib, unread hisoblagich bilan ko'rsatiladi.
- **GIVEN** foydalanuvchi rasm tanladi **WHEN** yuborish bosiladi **THEN** fayl multipart yuklanadi va `message_type=image` bilan WS xabar yuboriladi.
- **GIVEN** suhbatdosh foydalanuvchini bloklaydi **WHEN** `block_occurred` keladi **THEN** chat qulf/muted uslubda ko'rsatiladi, tarix saqlanadi.
- **GIVEN** chat bloklangan **WHEN** xabar yuborilsa **THEN** server `error: chat_blocked` qaytaradi va blok holati qayta yuklanadi.

## Kod joylashuvi
- **Modul:** `lib/features/chat`
- **Sahifa / BLoC:** `ChatListPage`, `ChatDetailPage`, `ChatDetailLoaderPage` / `ChatListBloc`, `ChatDetailBloc`; entitilar `Chat` (`ChatType{rented, rentedOut}`, `isBlockedByMe`, `isInactive`, `unreadCount`), `ChatMessage` (`MessageType{text, image, file}`, `mediaUrls`, `isRead`)
- **Endpoint:** WS `chat_room_list`, `message_history`, `message`, `typing`, `read`, `delete_chat_room`, `block_occurred`; REST fallback `GET /mobile/chat/list/` `{my_property, page, page_size}`; fayl `chat_file_service` multipart

## Konflikt / farqlar
- ⚠ **REST metodlari olib tashlangan:** send/getById/getMessages/markAsRead/deleteChat/createChat REST endpointlari mavjud emas edi (404/405) — olib tashlangan, faqat `GET /mobile/chat/list/` (deep-link/push pre-connect fallback) qoldi. → [`_konfliktlar.md`](../_konfliktlar.md) B7.
- ⚠ Chat'da **24 soatlik SLA/countdown yo'q** — bu R5 mexanizmi faqat so'rovlar boshqaruviga tegishli ([`07-sorovlar/`](../07-sorovlar/about.md)). → B8.
