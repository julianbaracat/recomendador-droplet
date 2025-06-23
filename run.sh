#!/bin/bash
echo "🔄 Cargando entorno..."

# Cargar variables de entorno
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo "❌ Falta el archivo .env"
    exit 1
fi

echo "🚀 Ejecutando recomendador..."
python3 main.py