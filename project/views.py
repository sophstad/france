from flask import render_template
from app import app, pages

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")