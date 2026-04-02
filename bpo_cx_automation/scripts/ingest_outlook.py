import os
import imaplib
import email

# 1. DEFINICIÓN GLOBAL (Fuera de la función para que todos la vean)
# Usamos join para que funcione bien en Windows
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRONZE_PATH = os.path.join(BASE_DIR, "data", "bronze")

def conectar_y_descargar():
    # 2. VARIABLES LOCALES (Dentro de la función)
    # Usa tu correo personal y la CONTRASEÑA DE APLICACIÓN de 16 letras
    usuario = "kevinlui2939@gmail.com"
    password = "gtdz ngbo egmu nszs" 
    imap_url = "imap.gmail.com"

    # Asegurarnos de que la carpeta existe
    if not os.path.exists(BRONZE_PATH):
        os.makedirs(BRONZE_PATH, exist_ok=True)

    try:
        print("Connecting to Gmail...")
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(usuario, password)
        mail.select("inbox")

        # 3. BUSQUEDA (Ajusta el SUBJECT según el reporte de Genesys)
        # 'UNSEEN' solo descarga los que no has leído
        result, data = mail.search(None, '(SUBJECT "Genesys")')

        if result == 'OK':
            for num in data[0].split():
                result, data = mail.fetch(num, "(RFC822)")
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)

                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart': continue
                    if part.get('Content-Disposition') is None: continue

                    filename = part.get_filename()
                    if filename:
                        filepath = os.path.join(BRONZE_PATH, filename)
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        print(f"✅ Archivo descargado: {filename} en {BRONZE_PATH}")
        
        mail.logout()
        print("Fin del proceso.")

    except Exception as e:
        print(f"❌ Error detectado: {e}")

if __name__ == "__main__":
    conectar_y_descargar()