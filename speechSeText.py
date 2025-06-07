# app.py for flask application...
from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import speech_recognition as sr
import time
import os
from dotenv import load_dotenv
import markdown  # Add this import at the top


load_dotenv()

app = Flask(__name__)

# Initialize model and parser
# Load Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize ChatGroq with llama3-70b-8192
model = ChatGroq(model_name="llama3-70b-8192", groq_api_key=GROQ_API_KEY)
parser = StrOutputParser()
chain = model | parser
recognizer = sr.Recognizer()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen", methods=["POST"])
def listen():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("🎙️ Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        text = recognizer.recognize_google(audio)
        print(f"🧑 You said: {text}")
        start_time = time.time()
        response = chain.invoke(text)
        end_time = time.time()
        html_response = markdown.markdown(response)  # Convert Markdown to HTML
        return jsonify({
            "query": text,
            "response": html_response,
            "time": round(end_time - start_time, 2)
        })

    except sr.WaitTimeoutError:
        return jsonify({"error": "Timeout: No speech detected."})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio."})
    except sr.RequestError as e:
        return jsonify({"error": f"Speech recognition error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
