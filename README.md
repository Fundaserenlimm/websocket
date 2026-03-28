# 🐍 Simple Python Web Server (Socket)
Bu proje, Python'ın düşük seviyeli socket kütüphanesini kullanarak sıfırdan oluşturulmuş basit bir HTTP/Web Sunucusudur. Herhangi bir dış framework (Flask, Django vb.) kullanmadan HTTP protokolünün nasıl çalıştığını anlamak amacıyla geliştirilmiştir.

# 🚀 Özellikler
Saf Python: Sadece yerleşik socket ve os kütüphaneleri kullanıldı.

Statik Dosya Sunumu: HTML dosyalarını ve görselleri (fotograf.jpeg) tarayıcıya servis eder.

Özel HTTP Yanıtları: Manuel olarak yapılandırılmış HTTP başlıkları (headers) içerir.

# 📂 Dosya Yapısı
server.py: Sunucu mantığının ve socket dinlemesinin yapıldığı ana dosya.

index.html: Sunucuya erişildiğinde gösterilen ana sayfa.

fotograf.jpeg: Sunucu üzerinden servis edilen örnek medya dosyası.

# 🛠 Kurulum ve Çalıştırma
Önce bu depoyu bilgisayarınıza klonlayın:

git clone https://github.com/Fundaserenlimm/websocket.git
cd websocket
Sunucuyu başlatın:
python3 server.py
Tarayıcınızdan şu adrese gidin:
http://127.0.0.1:8080

# 📝 Notlar
Bu sunucu şu an için sadece GET isteklerini desteklemektedir ve eğitim amaçlıdır. Gerçek dünya uygulamaları için gunicorn veya uvicorn gibi üretim seviyesi sunucuların kullanılması önerilir.

http://127.0.0.1:8080

📝 Notlar
Bu sunucu şu an için sadece GET isteklerini desteklemektedir ve eğitim amaçlıdır. Gerçek dünya uygulamaları için gunicorn veya uvicorn gibi üretim seviyesi sunucuların kullanılması önerilir.
