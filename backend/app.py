import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

app = Flask(__name__)

@app.route("/")
async def hello_world():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Extract flashcards with at least 1 sentence from the text."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": """Duck is the common name for numerous species of waterfowl in the family Anatidae. Ducks are generally smaller and shorter-necked than swans and geese, which are members of the same family. Divided among several subfamilies, they are a form taxon; they do not represent a monophyletic group (the group of all descendants of a single common ancestral species), since swans and geese are not considered ducks. Ducks are mostly aquatic birds, and may be found in both fresh water and sea water.

Ducks are sometimes confused with several types of unrelated water birds with similar forms, such as loons or divers, grebes, gallinules and coots.""",
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "flashcards",
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
        
    )
    return chat_completion.choices[0].message.content