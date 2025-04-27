TNet Main Server
TNet, cihazlar arasında IP adresi ataması ve güvenli mesajlaşmayı yöneten, basit bir IoT ağı sunucusudur.
Bu sunucu, cihazların kaydını alır, kimliklerini doğrular ve cihazlar arasında şifreli mesaj alışverişine izin verir.

Özellikler
📡 DHCP benzeri IP/ID yönetimi

🔒 Cihaz doğrulama ve şifreli mesajlaşma

📚 JSON tabanlı cihaz veritabanı

🚫 Yetkisiz erişimlere karşı IP engelleme (anti-DHCP spoofing)

🎛️ Komut satırı üzerinden sunucu kontrolü (örneğin JSON sıfırlama)

🛠️ Otomatik subdomain yönetimi (s1, s2)

Başlangıç
Gereksinimler
Python 3.x

Flask kütüphanesi

Requests kütüphanesi

Windows işletim sistemi (opsiyonel: winsound ve msg komutları için)

Kurulum
Depoyu klonlayın veya kodları indirin.

Gerekli Python kütüphanelerini kurun:

bash
Kopyala
Düzenle
pip install flask requests
tnetdb.json dosyasını aşağıdaki formatta oluşturun veya sunucuyu ilk başlatmada kendiliğinden oluşturmasına izin verin.

Çalıştırma
bash
Kopyala
Düzenle
python tnet_server.py
Sunucu arka planda çalışacak ve 8080 portunu dinleyecektir.

API Kullanımı
1. Cihaz Kayıt (POST /)
Amaç: Cihazın IP, MAC ve mod bilgilerini sunucuya kaydeder.

İstek:

json
Kopyala
Düzenle
{
    "ip": "192.168.1.5",
    "mac": "AA:BB:CC:DD:EE:FF",
    "statu": "online",
    "passs": "tnet123321123321"
}
Dönüş:

json
Kopyala
Düzenle
{
    "your_dhcp": "dev3"
}
2. Mesaj Gönderme (POST /message)
Amaç: Cihazlar arası şifreli mesaj gönderir.

İstek:

json
Kopyala
Düzenle
{
    "dhcp": "dev3",
    "dhcp2": "dev1",
    "message": "Merhaba Dünya"
}
Dönüş:

Başarılıysa: Message sent.

Yetkisizse: Access Denied (403)

Komutlar
Sunucu çalışırken komut satırından aşağıdaki komutlar verilebilir:


Komut	Açıklama
r /j	Veritabanını (tnetdb.json) sıfırlar.
r /j /t <saniye>	Belirtilen süre sonra veritabanını sıfırlar.
r	Sunucuyu kapatır ve çıkış yapar.
Güvenlik
Her cihaz, sunucuya kayıt olurken doğru şifre (tnet123321123321) göndermelidir.

Yanlış davranan IP adresleri blcip listesine alınır ve engellenir.

Mesajlar, Base64 + özel çarpanlı şifreleme yöntemiyle kodlanarak iletilir.

Dosya Yapısı
tnet_server.py — Ana sunucu kodu

tnetdb.json — Cihaz kayıtlarının saklandığı dosya

register/ — İsteğe bağlı kayıt dosyalarının tutulacağı klasör

Notlar
Sunucu Windows odaklıdır (winsound, msg gibi Windows'a özgü modüller kullanır).

Gerçek sahada kullanılacaksa HTTPS ve daha güçlü şifreleme eklenmesi önerilir.

Lisans
🛡️ Bu proje kişisel veya eğitim amaçlı kullanılabilir.
Dağıtmadan veya ticari kullanmadan önce geliştiriciye danışılması tavsiye edilir.
