# LibroBot 🤖📚

An AI-powered smart library assistant robot built using ESP32, ESP32-CAM, ultrasonic sensors, and an intelligent backend.

## 📂 Structure

```
LibroBot/
├── firmware/       # ESP32 control code
├── backend/        # FastAPI + OCR processing
```

## 🚀 Quick Start

### ESP32

- Open `librobot_main.ino` in Arduino IDE
- Edit `config.h` for WiFi credentials
- Upload to ESP32

### Backend

```bash
cd backend
pip install fastapi uvicorn opencv-python pytesseract
uvicorn app:app --reload
```
