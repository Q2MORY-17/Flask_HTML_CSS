from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home_simple_app.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)