from flask import Flask, render_template, request, redirect, url_for
from fibonacci import Fibonacci
import lorem



app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get('fibonacci'):
            number = request.form.get('fibonacci')
            return redirect(url_for('result', number=number))
    else:
        return render_template("index.html")

@app.route("/results", methods=["POST", "GET"])
def result():
    number = request.args.get("number")
    number = int(number)
    response = Fibonacci(number).iter()
    paragraphe = lorem.paragraph()
    return render_template("results.html", response=response, paragraphe=paragraphe)

