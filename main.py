
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Lấy API key từ biến môi trường trên Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"reply": response.choices[0].message["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
