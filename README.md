# Smart Tamil OCR (ஸ்மார்ட் தமிழ் ஆவண மாற்றி)

An AI-powered Optical Character Recognition (OCR) web application specialized for extracting printed Tamil text from images and exporting the output directly to formatted Microsoft Word (.docx) documents.

Powered by **Google Gemini Vision (`gemini-2.5-flash`)** and built with a Python **Flask** backend and a responsive modern web UI.

---

## ✨ Features

- **High-Accuracy Tamil OCR**: Extracts printed Tamil text accurately from uploaded images using Google Gemini multimodal AI.
- **Word Document (.docx) Export**: Download extracted Tamil text as clean Microsoft Word documents with preserved formatting and line breaks.
- **Quick Text-to-Docx Conversion**: Paste or type Tamil text directly to generate `.docx` files on the fly.
- **Modern Responsive Web Interface**:
  - Live backend health & connection status indicator (`பின்னத்துடன் இணைக்கப்பட்டது`).
  - Drag-and-drop & file selector for images.
  - Image preview with clear/reset options.
  - One-click copy to clipboard.
  - Tabbed interface for OCR and direct text-to-document conversion.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Vanilla responsive styling, glassmorphism UI, Noto Sans Tamil typography), JavaScript (Fetch API).
- **Backend**: Python 3.11+, Flask, Flask-CORS.
- **AI / OCR Engine**: Google Generative AI SDK (`google-generativeai`), Gemini 2.5 Flash model.
- **Document Processing**: `python-docx` for `.docx` generation, `Pillow` for image handling.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ installed.
- A Google Gemini API key (from [Google AI Studio](https://aistudio.google.com/)).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sreenisha-s/smart-tamil-ocr.git
   cd smart-tamil-ocr
   ```

2. **Create and activate a virtual environment**:
   - **Windows**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and set your Gemini API key:
     ```env
     GEMINI_API_KEY="your_actual_gemini_api_key"
     ```

---

## 💻 Running the Application

1. **Start the Flask backend**:
   ```powershell
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000/`.

2. **Open the web app**:
   - Navigate to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in any modern web browser.
   - The connection status badge in the top right will display green (**பின்னத்துடன் இணைக்கப்பட்டது**).

---

## 📂 Project Structure

```text
smart-tamil-ocr/
├── app.py              # Flask server and API endpoints (/api/health, /api/ocr, /api/text-to-docx)
├── check_models.py     # Utility script to check Gemini models available to your API key
├── index.html          # Interactive frontend UI with OCR, preview, and export controls
├── requirements.txt    # Project Python dependencies
├── .env.example        # Example environment variable template
├── .gitignore          # Git exclusion rules (ignores .env, venv, pycache, etc.)
└── README.md           # Project documentation
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
