
import os, base64
from google.cloud import firestore
import google.generativeai as genai
from datetime import datetime, timezone

# 🔐 Configurar credenciales desde variable de entorno BASE64
cred_path = "/tmp/firebase.json"
with open(cred_path, "wb") as f:
    f.write(base64.b64decode(os.environ["FIREBASE_CRED_BASE64"]))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
db = firestore.Client()

def main(args):
    # Simulamos un usuario de ejemplo
    usuario = {
        "nombre": "Ejemplo",
        "intereses": ["cerámica", "reciclado"],
        "ubicacion": "Palermo"
    }

    productos_ref = db.collection("productos")
    productos_docs = productos_ref.stream()
    productos = []
    for p in productos_docs:
        data = p.to_dict()
        productos.append({
            "Nombre": data.get("Nombre", ""),
            "Material": data.get("Material", ""),
            "Ubicación": data.get("Ubicación", ""),
            "nombreVendedor": data.get("nombreVendedor", "")
        })

    texto_productos = "\n".join([str(p) for p in productos])
    prompt = f"""
Sos un asistente experto en ferias artesanales.

Elegí solo un producto del listado que mejor encaje con este usuario:

USUARIO: {usuario}
PRODUCTOS: {texto_productos}

Devolvé JSON válido:
{{"Nombre": "...", "nombreVendedor": "..."}}"""

    try:
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        respuesta = modelo.generate_content(prompt)
        salida = respuesta.text.strip()
        return {"body": salida}
    except Exception as e:
        return {"body": f"Error: {str(e)}"}