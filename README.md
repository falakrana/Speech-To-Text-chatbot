# 🎧 Flask Voice Assistant using Groq's LLaMA 3 (70B)

This project is a real-time voice assistant built using **Flask**, **Groq's LLaMA 3 (70B)** via `langchain_groq`, and **speech recognition**. The assistant listens to your speech, transcribes it, sends it to the Groq LLM for a response, and displays the result in a web UI with markdown rendering.

---

## 🚀 Features

* 🎤 Speech-to-Text via Google Speech Recognition
* 🧠 LLM Response using Groq's `llama3-70b-8192`
* 🌐 Flask-based web interface
* ⏱️ Response time tracking
* 🕋️ Markdown rendering for formatted output

---

## 💠 Tech Stack

* **Backend**: Flask, LangChain, Groq LLM
* **Speech Recognition**: `speech_recognition`
* **Environment Management**: `python-dotenv`
* **Frontend**: HTML + JavaScript (basic template)

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/flask-groq-voice-assistant.git
cd flask-groq-voice-assistant
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, here’s the command to install manually:

```bash
pip install flask langchain langchain-groq speechrecognition python-dotenv markdown
```

### 4. Set up your environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔐 You can get your API key from [Groq Cloud](https://console.groq.com/keys).

---

## ▶️ Running the App

```bash
python app.py
```

Visit **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

---

## 📂 Project Structure

```
├── app.py
├── .env
├── templates/
│   └── index.html
├── static/          # (Optional - if you have custom CSS/JS)
├── README.md
└── requirements.txt
```

---

## 📝 Example Usage

1. Click the "Start Listening" button (HTML button in index.html).
2. Speak into your microphone.
3. The assistant will:

   * Transcribe your speech
   * Send it to Groq's LLM
   * Display the markdown-rendered response along with latency

---

## ✅ To Do (Optional Enhancements)

* Add a loader while processing
* WebSocket integration for real-time updates
* Add microphone control toggle UI
* Improve front-end design with Bootstrap/Tailwind

---

## 📄 License

MIT License. Feel free to modify and distribute.

---

## 🤝 Credits

* [LangChain](https://github.com/langchain-ai/langchain)
* [Groq Cloud](https://groq.com/)
* [Flask](https://flask.palletsprojects.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
