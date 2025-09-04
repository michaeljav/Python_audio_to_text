++++++++++++++++++PARA CREAR PROJECTO NUEVO

# 1 step

# crear entorno virtual

py -m venv venv
python -m venv venv

Desglose del comando

py
Es el Python Launcher (el que ya estás usando en Windows). Llama a la versión de Python que tienes instalada (3.13.4 en tu caso).

-m venv
Le dice a Python: “ejecuta el módulo venv”.

venv es un módulo incluido en Python que sirve para crear entornos virtuales.

venv (al final)
Es el nombre de la carpeta donde se creará el entorno virtual.

Puedes llamarla como quieras (venv, .venv, env, etc.), pero por convención casi siempre se usa venv.

# activar entorno virtual (windows / Mac)

source venv/Scripts/activate

# activar entorno virtual (Windows PowerShell)

venv\Scripts\activate

# 2 Step 2) Install dependencies

faster-whisper is fast and runs fully offline (CPU or GPU).
pip install faster-whisper soundfile tqdm

# 3 para saber que paquetes usa este projecto

pip freeze > requirements.txt
-nota: esto es para instalar si no existe venv
pip install -r requirements.txt

# RUN IT

# Auto language detection

python transcribe.py meeting.m4a --model small

# Force Spanish and enable VAD for noisy audio

python transcribe.py meeting.m4a --model small --language es --vad
py transcribe.py ejemplo.mp3 --model small --language es --vad

## Model size guide (pick one)

tiny/base: fastest, lower accuracy.

small: good balance (recommended start).

medium: better accuracy, slower.

large-v3: highest accuracy, slowest & heaviest.
