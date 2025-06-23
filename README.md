# 🛍️ Recomendador de Productos Artesanales

Este proyecto utiliza Google Gemini y Firestore para recomendar productos de una base de datos, según el perfil de un usuario. Se ejecuta en un entorno controlado como un Droplet de DigitalOcean.

---

## 🚀 ¿Qué hace?

🔹 Carga productos desde Firestore  
🔹 Recibe un perfil de usuario simulado  
🔹 Usa IA (Gemini) para sugerir **un producto óptimo** de la base  
🔹 Devuelve un JSON con nombre del producto y vendedor

---

## 📁 Estructura del proyecto

recomendador-droplet/
├── main.py # Script principal
├── requirements.txt # Dependencias del entorno
├── .env.example # Plantilla para tus credenciales
├── run.sh # Script de ejecución en bash



---

## 🧪 Requisitos

- Python 3.8 o superior
- Cuenta de Google Cloud con:
  - Firestore habilitado
  - API Gemini activada
- Credencial del tipo `service_account` (convertida a base64)
- API Key de Gemini

---

## ⚙️ Configuración

1. 🔐 Copiá `.env.example` como `.env` y completalo:

```env
FIREBASE_CRED_BASE64=tu_json_en_base64_sin_saltos
GEMINI_API_KEY=tu_clave_de_api_de_gemini
📦 Instalá las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
▶️ Ejecutá el script:

bash
Copiar
Editar
bash run.sh
💡 Ejemplo de salida
json
Copiar
Editar
{
  "Nombre": "Caja de madera reciclada",
  "nombreVendedor": "Artesanías del Parque"
}
🧼 Notas
No compartas tu archivo .env ni las claves reales.

Este repositorio usa .gitignore para ignorar .env y archivos temporales.

👤 Autor
Julian Baracat
📧 julian.baracat@gmail.com
🌐 Proyecto académico para Computación en la Nube

