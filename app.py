from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse, urljoin
import requests


app = Flask(__name__)

# Route to redirect - when the onload event occurs - to the login page directly
@app.route("/")
def hello():
    # See line 40
    return render_template("index.html")

# Successive app routes, flaskin it
@app.route("/Economic impact")    #page of a single dashboard
@login_required
def dashboard():
    # Verify data storage type/structure here
    return render_template("Economic impact.html")

@app.route("/Frog and Zebra Muscles Graph")    #page of a single dashboard
@login_required
def frogs():
    # Verify data storage type/structure here
    return render_template("Frog and Zebra Muscles Graph.html")

@app.route("/Density")    #page of a single dashboard
@login_required
def invasion():
    return render_template("Density.html")

if __name__ == "__main__":
    app.run(debug=True)
