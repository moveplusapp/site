from flask import (
    Flask,
    render_template
)

app = Flask(__name__)


@app.route('/views/<view>')
def render_view(view):
    return render_template("/views/{}.html".format(view))


@app.route('/')
def render_index():
    return render_template("index.html")
