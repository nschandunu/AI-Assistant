import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct",
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.6,
            max_tokens=512,
            top_p=0.9
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
