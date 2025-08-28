import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

load_dotenv()

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
async def hello_world():

    prompt1 = request.data.decode()

    print(prompt1)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": 'Extract flashcards with at least 1 sentence from the text. Respond in json. json example: {"flashcards": ["flashcard1", "flashcard2"]}'
            },
            {
                "role": "user",
                "content": prompt1,
            }
        ],
        model="moonshotai/kimi-k2-instruct",
        response_format={"type": "json_object"},
        temperature=1.0
    )


    return chat_completion.choices[0].message.content