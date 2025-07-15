from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="AIzaSyBkUxc1zRgvumzIRaqOyR9vTYt2mEnOxDI")
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        response = model.generate_content(prompt)
        return jsonify({"blog": response.text})
    except Exception as e:
        return jsonify({"blog": f"Error: {str(e)}"})
