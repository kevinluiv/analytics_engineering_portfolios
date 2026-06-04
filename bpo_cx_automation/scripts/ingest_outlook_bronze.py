import os
import imaplib
import email
from datetime import datetime

# --- 1. CONFIGURACIÓN DE RUTAS (Estructura de Carpeta Bronze) ---
# Buscamos la raíz del proyecto para que las rutas siempre funcionen
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRONZE_BASE = os.path.join(BASE_DIR, "data", "bronze")

# Creamos subcarpetas para segmentar el negocio
MS_PATH = os.path.join(BRONZE_BASE, "member_services")
TECH_PATH = os.path.join(BRONZE_BASE, "tech_support")

def inicializar_carpetas():
    """Asegura que el 'Data Lake' tenga sus divisiones listas."""
    for path in [MS_PATH, TECH_PATH]:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print(f"📁 Carpeta creada: {path}")

def conectar_y_descargar():
    # Credenciales (Recuerda proteger estas variables después)
    usuario = "kevinlui2939@gmail.com"
    password = "gtdz ngbo egmu nszs" 
    imap_url = "imap.gmail.com"

    try:
        print("🚀 Iniciando conexión con Gmail...")
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(usuario, password)
        mail.select("inbox")

        # Buscamos correos que contengan "Genesys" en el asunto
        # Puedes ser más específico: '(SUBJECT "Genesys Report")'
        result, data = mail.search(None, '(SUBJECT "Genesys")')

        if result == 'OK':
            emails_ids = data[0].split()
            print(f"📧 Se encontraron {len(emails_ids)} correos potenciales.")

            for num in emails_ids:
                # Descargamos el contenido del correo
                result, data = mail.fetch(num, "(RFC822)")
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                subject = msg.get('Subject')
                print(f"🔍 Procesando: {subject}")

                # --- 2. LÓGICA DE CLASIFICACIÓN (Socio Estratégico) ---
                if "Member Services" in subject or "HISTORICO_MS":
                    current_target = MS_PATH
                    print("📌 Destino: Member Services")
                elif "Tech Support" in subject or "HISTORICO_TS":
                    current_target = TECH_PATH
                    print("📌 Destino: Tech Support")
                else:
                    print("⚠️ Asunto no reconocido, se omite este correo.")
                    continue

                # --- 3. EXTRACCIÓN DE ADJUNTOS CON TRAZABILIDAD ---
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart': continue
                    if part.get('Content-Disposition') is None: continue

                    filename = part.get_filename()
                    if filename:
                        # Creamos el Timestamp para evitar sobreescritura (Inmutabilidad)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                        new_filename = f"{timestamp}_{filename}"
                        
                        filepath = os.path.join(current_target, new_filename)
                        
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        print(f"✅ Archivo guardado: {new_filename}")

        mail.logout()
        print("🏁 Proceso de ingesta finalizado con éxito.")

    except Exception as e:
        print(f"❌ Error en el pipeline: {e}")
        

if __name__ == "__main__":
    inicializar_carpetas()
    conectar_y_descargar()