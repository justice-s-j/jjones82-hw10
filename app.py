# module 10 - Flask Application
# Justice Jones 11/03/2025

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)