from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/get')
def get():
    r = requests.get('http://www.example.com/')
    return r.text()

if __name__=="__main__":
    app.run(debug=True)
