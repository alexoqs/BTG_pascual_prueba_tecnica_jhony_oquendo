@echo off

:: Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate

:: Instalar dependencias
pip install -e .

:: Ejecutar la aplicación
uvicorn src.application.main:app --reload