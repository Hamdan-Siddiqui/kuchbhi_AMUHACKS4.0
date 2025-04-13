from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def counselling(text):
    given_text = text
    if not os.getenv("GOOGLE_API_KEY"):
        raise "GOOGLE API KEY is misisng."
    
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[f"Classify{given_text} into sad, happy, motivated and demotivated, just write the words as I have written, don't add anything with them not even a full stop"]
    )
    print(response.text)

    if response.text.lower().strip() == "sad":
        suggestion = "It's okay to feel sad sometimes. Allow yourself to heal, and remember, this too shall pass."
    elif response.text.lower().strip() == "happy":
        suggestion = "Cherish these moments and share your happiness with others. Your positivity can light up the world."
    elif response.text.lower().strip() == "motivated":
        suggestion = "You're on fire! Channel that energy into something incredible today."
    else:
        suggestion = "You've faced challenges before and overcome them. Trust that you have the strength to rise again."

    print(suggestion)
    return suggestion
