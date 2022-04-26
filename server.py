from time import sleep

from flask import Flask, render_template

from scraper import getBlockTable

app = Flask(__name__)


@app.before_request
def getBlock():
    global BLOCK
    try:
        BLOCK = getBlockTable()
    except Exception as e:
        print(e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getBlock")
def index():
    return render_template("block.html", block=BLOCK)


app.run(debug=True)
