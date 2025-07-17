# 🔥 LeCore Backend – v2

This is the version 2 backend for the **LeCore App**, powered by Flask and Hugging Face, with new intelligent image captioning features.

---

## ✨ New in v2

### ✅ Hugging Face Integration
- Uses **Salesforce BLIP** (`blip-image-captioning-base`) model
- Live AI-powered image-to-text generation

### ✅ Image Upload Support
- Accepts user-uploaded `.jpg`, `.jpeg`, `.png` images
- Automatically converts image to RGB for processing

### ✅ Prompt-based Captions
- Optional text prompt to guide the AI's response
- Without prompt, AI auto-generates description

### ✅ Robust Error Handling
- Returns proper error if:
  - No image uploaded
  - Invalid/corrupt image format
  - Internal model issues

### ✅ Optimized Cache Usage
- Avoids permission errors by redirecting all Hugging Face cache to writable folders (`/tmp` or `/home/user/.cache/...`)
- Fully supported on **Hugging Face Spaces**

---

## 🔐 Security & Tokens
- No hardcoding of API credentials in code

---

## 📦 Folder Contents
lecore-backend/
├── image_analyzer.py # Flask API logic
├── requirements.txt # All dependencies
├── Procfile # Hugging Face launch command
└── README.md # You’re here!


---

## 📍 Next Update in v3?

- 🔄 Chat history with images
- 🌍 Multi-language captions
- 🧠 More advanced model (BLIP-2 or CLIP)

---

👨‍💻 Developer
LeCore is proudly developed by:

👨‍💻 LeoN (@Leonrobin2009)
🎓 Young developer passionate about AI and Android
🌍 Based in Kerala, India 🇮🇳
📬 Contact: leonrobin2009@gmail.com
---

## 📄 License

This project is licensed under the [MIT License](./LICENSE) © 2025 **Leon Robin**.

You are free to use, modify, and distribute this app with proper credit to the original developer._____
