from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from random import randint
from util import generate_spongebobify_text, create_meme_api_request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = str(request.form["text"])
        text_result = generate_spongebobify_text(text)
        meme_result = create_meme_api_request(text_result)
        return render_template("home.html", result=text_result, img_url=meme_result)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)