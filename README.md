# TNet Main Server

TNet, cihazlar arasında IP adresi ataması ve güvenli mesajlaşmayı yöneten, basit bir IoT ağı sunucusudur.  
Bu sunucu, cihazların kaydını alır, kimliklerini doğrular ve cihazlar arasında şifreli mesaj alışverişine izin verir.

---

## Özellikler

📡 **DHCP benzeri IP/ID yönetimi**  
🔒 **Cihaz doğrulama ve şifreli mesajlaşma**  
📚 **JSON tabanlı cihaz veritabanı**  
🚫 **Yetkisiz erişimlere karşı IP engelleme** (anti-DHCP spoofing)  
🎛️ **Komut satırı üzerinden sunucu kontrolü** (örneğin JSON sıfırlama)  
🛠️ **Otomatik subdomain yönetimi** (s1, s2)

---

## Başlangıç

### Gereksinimler

- Python 3.x
- Flask kütüphanesi
- Requests kütüphanesi
- Windows işletim sistemi (opsiyonel: `winsound` ve `msg` komutları için)

---

### Kurulum

1. Depoyu klonlayın veya kodları indirin.

2. Gerekli Python kütüphanelerini kurun:

   ```bash
   pip install flask requests
