from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet/<name>")
def greet(name: str):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
