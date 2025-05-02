from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def counselling(text):
    given_text = text
    my_api_key = os.getenv("GOOGLE_API_KEY")
    print("*****************" + (my_api_key[-4:] if my_api_key else "None"))

    if not my_api_key:
        raise Exception("GOOGLE API KEY is missing.")

    client = genai.Client(api_key=my_api_key)

    prompt = (
        f"Classify the following text into one of the categories exactly as written: "
        f"Happiness / Joy / Contentment, Sadness / Grief / Disappointment, "
        f"Anxiety / Worry / Nervousness, Anger / Frustration / Irritability, "
        f"Fear / Panic, Tiredness / Fatigue / Low Energy, Confusion / Disorientation. "
        f"Just return the exact category text, nothing else, no punctuation.\n\nText: {given_text}"
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )

    emotion = response.text.strip()
    print(f"Detected emotion: {emotion}")

    if emotion == "Happiness / Joy / Contentment":
        suggestion = "That's wonderful! Embrace these feelings and let them fuel your day."
    elif emotion == "Sadness / Grief / Disappointment":
        suggestion = "Take time to acknowledge your feelings. Healing is a process, and you're not alone."
    elif emotion == "Anxiety / Worry / Nervousness":
        suggestion = "Breathe deeply. Focus on what you can control, and take one step at a time."
    elif emotion == "Anger / Frustration / Irritability":
        suggestion = "Try to pause and reflect. Channel your energy into something constructive."
    elif emotion == "Fear / Panic":
        suggestion = "You're safe. Remind yourself of what you know and breathe through the fear."
    elif emotion == "Tiredness / Fatigue / Low Energy":
        suggestion = "Rest is essential. Prioritize self-care and recharge your body and mind."
    elif emotion == "Confusion / Disorientation":
        suggestion = "Take a moment to ground yourself. Clarity often follows a pause."
    else:
        suggestion = "Your feelings are valid. Take care of yourself, and seek support if you need it."

    print(suggestion)
    return suggestion, emotion
