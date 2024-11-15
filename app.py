# app.py
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Replace with your MongoDB Atlas connection string
app.config["MONGO_URI"] = "mongodb+srv://vedanshtyagibrd19:Zr9Yd2y5ckvcFg3K@cluster0.uwigs.mongodb.net/bank?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    if name:
        # Insert the name into the MongoDB collection 'users'
        mongo.db.users.insert_one({"name": name})
        return redirect(url_for('thank_you'))
    return "No name provided", 400

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting your name!"

if __name__ == '__main__':
    app.run(debug=True)
