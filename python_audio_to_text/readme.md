# 🚀 How to Create a New Project

## 1. Create a Virtual Environment

```bash
py -m venv venv
python -m venv venv
```

**Command breakdown:**

- **`py`**  
  The Python Launcher (already on Windows). It calls the installed Python version (3.13.4 in your case).

- **`-m venv`**  
  Tells Python: “run the `venv` module.”

- **`venv` (at the end)**  
  The folder name where the virtual environment will be created.  
  You can name it as you like (`venv`, `.venv`, `env`, etc.), but the convention is usually `venv`.

### Activate the virtual environment

- **Windows / Mac (Git Bash or terminal):**

  ```bash
  source venv/Scripts/activate
  ```

- **Windows PowerShell:**
  ```bash
  venv\Scripts\activate
  ```

---

## 2. Install Dependencies

```bash
pip install faster-whisper soundfile tqdm
```

> `faster-whisper` runs completely offline and works with CPU or GPU.

---

## 3. Manage Project Packages

- Save installed packages:

  ```bash
  pip freeze > requirements.txt
  ```

- Reinstall dependencies (if no `venv` exists):
  ```bash
  pip install -r requirements.txt
  ```

---

## 4. Run It

### Auto language detection

```bash
python transcribe.py meeting.m4a --model small
```

### Force Spanish + VAD (for noisy audio)

```bash
python transcribe.py meeting.m4a --model small --language es --vad
py transcribe.py ejemplo.mp3 --model small --language es --vad
```

---

## 5. Model Size Guide

- **tiny / base** → fastest, but lowest accuracy
- **small** → good balance (**recommended start**)
- **medium** → higher accuracy, slower
- **large-v3** → best accuracy, but slowest and heaviest
