# PRATHNA 🙏

A simple Streamlit devotional chatbot powered by the xAI (Grok) API. It focuses on Marathi and Hinglish prayers, aartis, mantras, and chanting.

## 1. Requirements
- Python 3.10 or newer
- An xAI API key from https://console.x.ai/
- Internet connection

## 2. Install
Open Command Prompt in this folder:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Add your API key
Copy `.env.example` to `.env`, then open `.env` in Notepad and replace the placeholder:

```text
XAI_API_KEY=your_actual_grok_api_key
```

Keep the key private. Do not upload `.env` to GitHub or share screenshots containing it.

## 4. Run the app

```bat
streamlit run app.py
```

Streamlit should open PRATHNA in your browser. If it does not, visit the local URL printed in Command Prompt, usually `http://localhost:8501`.

## 5. Where to change the model
In `app.py`, search for:

```python
model="grok-4.7",
```

Replace it with a model name enabled for your xAI account if needed.

## Notes
- No login page or database is required.
- Conversation history exists only in the current Streamlit session.
- This is a starter app. The model instructions guide it to stay in devotional scope, but prompt instructions alone are not a perfect security boundary.
- API use may incur charges depending on your xAI account and model pricing.
