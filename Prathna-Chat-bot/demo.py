
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env file
load_dotenv()

api_key = os.getenv("XAI_API_KEY")

if not api_key:
    print("ERROR: API key not found in .env file.")
    print("Check that your file is named .env")
    print("and contains GROQ_API_KEY=your_actual_key")
    raise SystemExit(1)

try:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": "Reply with: API is working!"}
        ],
        max_completion_tokens=50
    )

    print("SUCCESS: Groq API key is working!")
    print("Model response:", response.choices[0].message.content)

except Exception as e:
    print("ERROR: Groq API request failed.")
    print("Details:", str(e))
