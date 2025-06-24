# 🛍️ Recomendador de Productos Artesanales

Este proyecto usa Google Gemini y Firestore para recomendar productos artesanales según el perfil del usuario.

---

## 🚀 ¿Qué hace?

✅ Lee productos desde Firestore  
✅ Usa Gemini para sugerir el mejor  
✅ Devuelve JSON: `{"Nombre": "...", "nombreVendedor": "..."}`

---

## 📁 Archivos clave

| Archivo       | Descripción                                      |
|---------------|--------------------------------------------------|
| `main.py`     | Lógica de recomendación con IA                   |
| `app.py`      | Servidor Flask con endpoint público              |
| `run.sh`      | Ejecuta en consola local                         |
| `run_web.sh`  | Ejecuta Flask en segundo plano (Droplet)         |
| `.env.example`| Variables necesarias para correr el proyecto     |

---

## ⚙️ Configuración

1. **Copiá `.env.example` como `.env`** y completalo:

```env
FIREBASE_CRED_BASE64=tu_json_en_base64_sin_saltos
GEMINI_API_KEY=tu_clave_de_api_de_gemini
Instalá dependencias:


pip install -r requirements.txt
Ejecutá (local o Droplet):


# Local
bash run.sh

# Droplet (modo web)
bash run_web.sh
🌐 Acceso web
Si está corriendo en un Droplet DigitalOcean:

👉 http://<IP-DE-TU-DROPLET>:8080

❗ Seguridad
Nunca compartas tu .env.
El archivo .gitignore ya lo excluye del repo.

👤 Autor
Julian Baracat
📧 julian.baracat@gmail.com
🌐 Proyecto académico – Computación en la Nube


