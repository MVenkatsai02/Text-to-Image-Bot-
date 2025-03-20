# Gemini 2.0 Text-to-Image Generator

This is a simple Streamlit web app that generates images from text prompts using Google's Gemini 2.0 Flash model.

## Features
- Generate AI-powered images based on text prompts.
- Uses Gemini 2.0 Flash for high-quality image generation.
- Streamlit-based user interface.
- Secure API key handling using `.env` file.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MVenkatsai02/Text-to-Image-Bot-
cd gemini-text-to-image
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage
Run the Streamlit app using:
```bash
streamlit run app.py
```

Enter a text prompt in the input box and click "Generate Image" to see the generated image.

## Dependencies
- `streamlit`
- `Pillow`
- `google-generativeai`
- `python-dotenv`

## License
This project is licensed under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Streamlit & Gemini AI 🚀

