from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__, static_folder="../static", template_folder="../templates")

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle(
    'css/main.scss',
    filters='libsass',
    output='css/main.css'
)
assets.register('scss_all', scss)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet/<name>")
def greet(name: str):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
