#!/bin/bash
echo "🔄 Cargando entorno..."

# Cargar variables de entorno
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo "❌ Falta el archivo .env"
    exit 1
fi

echo "🚀 Iniciando servidor Flask..."
nohup python3 app.py > flask.log 2>&1 &
echo "✅ Flask corriendo en segundo plano (puerto 8080)"
