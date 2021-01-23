import os
import numpy as np 
import pandas as pd 
from flask import Flask, abort, render_template, redirect, url_for, request, make_response


app = Flask(__name__)

# Route to redirect - when the onload event occurs - to the login page directly
@app.route("/")
def hello():
    # See line 40
    return render_template("index.html")

# Successive app routes, flaskin it
@app.route("/econ")  
def econ():
    return render_template("Economic Impact.html")

@app.route("/mussels")    
def mussels():
    return render_template("Frog and Zebra Muscles Graph.html")

@app.route("/density")   
def density():
    return render_template("Density.html")

@app.route("/invasion")  
def invasion():
    return render_template("Invasion Spread.html")

if __name__ == "__main__":
    app.run(debug=True)
