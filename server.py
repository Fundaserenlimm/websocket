import socket
import os

HOST = '127.0.0.1'
PORT = 8080

def create_http_response(content, content_type="text/html"):
    # HTTP protokolüne uygun başlık oluşturma
    response = "HTTP/1.1 200 OK\r\n"
    response += f"Content-Type: {content_type}; charset=utf-8\r\n"
    response += f"Content-Length: {len(content)}\r\n"
    response += "Connection: close\r\n"
    response += "\r\n"
    return response.encode('utf-8') + content

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"CV Sunucusu Hazır: http://{HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode('utf-8')
            if not request: continue
            
            # Tarayıcı hangi dosyayı istiyor? (index.html mi yoksa profil.jpg mi?)
            path = request.split()[1]
            
            if path == "/" or path == "/index.html":
                with open("index.html", "rb") as f:
                    content = f.read()
                conn.sendall(create_http_response(content, "text/html"))
            
            elif path == "/fotograf.jpeg":
                try:
                    with open("fotograf.jpeg", "rb") as f:
                        content = f.read()
                     # image/jpeg olarak gönderdiğimizden emin olalım
                    conn.sendall(create_http_response(content, "image/jpeg"))
                except FileNotFoundError:
                    print("Hata: fotograf.jpeg dosyası bulunamadı!")
                    conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
            
            print(f"{path} dosyası gönderildi.")