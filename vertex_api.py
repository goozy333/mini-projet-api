import vertexai
from vertexai.preview.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

def get_joke():
    vertexai.init(
        project=os.getenv("GCP_PROJECT"),
        location=os.getenv("GCP_REGION")
    )

    model = GenerativeModel(model_name="gemini-1.5-flash")  # version rapide & gratuite

    prompt = "Raconte-moi une blague drôle, courte et originale en français."

    chat = model.start_chat()
    response = chat.send_message(prompt)

    return response.text