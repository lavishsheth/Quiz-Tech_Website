from flask import Flask, render_template, request
import openai
from time import sleep

app = Flask(__name__)

# Read OpenAI API key from a file or environment variable
openai.api_key = "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"

import openai
from time import sleep

def bot(prompt, engine='gpt-3.5-turbo-instruct', temp=0.5, top_p=1.0, tokens=1000, freq_pen=0.0, pres_pen=0.5, stop=['<<END>>']):
    max_retry = 1
    retry = 0
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                # top_p=top_p,
                # frequency_penalty=freq_pen,
                # presence_penalty=pres_pen,
                # stop=[" User:", " AI:"]
                )
            text = response['choices'][0]['text'].strip()
            return text
        except openai.error.OpenAIError as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            sleep(1)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = bot(prompt=userText)
    return str(bot_response)

if __name__ == "__main__":
    app.run(debug=True)
