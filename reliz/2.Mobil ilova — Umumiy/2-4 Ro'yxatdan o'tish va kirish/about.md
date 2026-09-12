# 2-4 Ro'yxatdan o'tish va kirish

**Manba:** [US 4](<US 4 LA - Login Authentication/about.md>) · [AD-05](<../../6.Admin panel/6-1 Foydalanuvchilar boshqaruvi/AD-05 Foydalanuvchini boshqarish amallari/about.md>) · [AD-A1](<../../6.Admin panel/6-1 Foydalanuvchilar boshqaruvi/AD-A1 Foydalanuvchini administratsiya qilish/about.md>)

## Joriy talablar

- Role: uy egasi / ijarachi / guest `R1 · US 4`
- Role change settings orqali mumkin `R1 · US 4`
- Phone format: +998 `R1 · US 4`
- OTP: 6 digit, 1 min validity `R1 · US 4`
- Resend cooldown: 30–60 sekund `R1 · US 4`
- OTP attempt limit: 5 `R1 · US 4`
- PIN: 4 digit `R1 · US 4`
- PIN faqat OTPdan keyin yaratiladi `R1 · US 4`
- PINdan keyin avtomatik login `R1 · US 4`
- JWT + refresh token ishlatiladi `R1 · US 4`
- Multi-device login mavjud `R1 · US 4`
- Blocked user OTP stageda to‘xtatiladi `R1 · US 4`
- Bloklangan foydalanuvchi tizimga kira olmaydi `R2 · AD-05`
- Blacklistdagi foydalanuvchi ro’yxatdan o’ta olmaydi `R2 · AD-05`
- Foydalanuvchiga PIN tiklash SMS yuboriladi; foydalanuvchi yangi PIN o'rnatadi `R4 · AD-A1 (PIN tiklash)`
- Ijarachi ↔ Uy egasi roli o'zgartiriladi; foydalanuvchiga bildirishnoma `R4 · AD-A1 (Rol o'zgartirish)`
