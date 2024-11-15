from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# MongoDB URI (ensure it's correctly set for Vercel's environment)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    if name:
        mongo.db.users.insert_one({"name": name})
        return redirect(url_for('thank_you'))
    return "No name provided", 400

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting your name!"

# Vercel handler
if __name__ != "__main__":
    # Treat the app as a callable function for Vercel
    vercel_app = app
else:
    # Run locally
    app.run(debug=True)
