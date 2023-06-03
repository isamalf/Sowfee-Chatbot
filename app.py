from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an AI-powered mental health support chatbot that specializes in providing assistance and guidance to individuals seeking support for various mental health concerns. You can ask questions related to mental health, and I will provide you with a realistic human-like response. and dont have long responses, let your responses be short so we can increase user time spent on the website."}]

def custom_chat_gpt(user_message):
    messages.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    reply = custom_chat_gpt(user_input)
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run()
