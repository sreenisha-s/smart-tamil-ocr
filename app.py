import os
import sys
import io

# Ensure UTF-8 output on Windows consoles to prevent cp1252 encoding crashes
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import google.generativeai as genai
from docx import Document
import PIL.Image
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- 1. Initialize Flask App and Configure API ---
app = Flask(__name__)
CORS(app) # This is crucial to allow your webpage to communicate with this server

try:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("[OK] Gemini API configured successfully.")
except Exception as e:
    print(f"[ERROR] Could not configure Gemini API: {e}")
    model = None

# --- 2. Define API Routes (The "Kitchen" Logic) ---

@app.route('/')
def index():
    return send_file('index.html')

# This route is for the initial health check from the frontend
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "api_configured": model is not None})

# This route handles the image OCR request
@app.route('/api/ocr', methods=['POST'])
def process_ocr():
    if model is None:
        return jsonify({"error": "Gemini API not configured"}), 500
        
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    try:
        img = PIL.Image.open(file.stream)
        prompt = "Perform OCR on this image of Tamil text. Extract the text accurately. Preserve original line breaks."
        response = model.generate_content([prompt, img])
        
        return jsonify({"text": response.text})
    except Exception as e:
        print(f"[ERROR] OCR Error: {e}")
        return jsonify({"error": str(e)}), 500

# This route handles converting text to a .docx file
@app.route('/api/text-to-docx', methods=['POST'])
def text_to_docx():
    data = request.get_json()
    text = data.get('text', '')

    try:
        document = Document()
        document.add_heading('Tamil OCR Result', level=1)
        for line in text.split('\n'):
            document.add_paragraph(line)
        
        # Save document to a memory buffer
        mem_file = io.BytesIO()
        document.save(mem_file)
        mem_file.seek(0)

        return send_file(
            mem_file,
            as_attachment=True,
            download_name='tamil-document.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
    except Exception as e:
        print(f"[ERROR] DOCX Error: {e}")
        return jsonify({"error": str(e)}), 500

# --- 3. Run the Flask App ---
if __name__ == "__main__":
    # The port must be 5000 to match the JavaScript in your HTML file
    app.run(host='0.0.0.0', port=5000, debug=False)