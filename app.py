# app.py
from flask import Flask, render_template, redirect, url_for
from devices import devices, toggle_device, movie_mode, turn_everything_off

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", devices=devices)

@app.route("/toggle/<device>/<state>")
def toggle(device, state):
    toggle_device(device, state.lower() == "on")
    return redirect(url_for("index"))

@app.route("/movie")
def movie():
    movie_mode()
    return redirect(url_for("index"))

@app.route("/all_off")
def all_off():
    turn_everything_off()
    return redirect(url_for("index"))

