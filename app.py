from flask import (
    Flask,
    render_template,
    jsonify
)

app = Flask(__name__)


@app.route('/views/<view>')
def render_view(view):
    return render_template("/views/{}.html".format(view))


@app.route('/')
def render_index():
    return render_template("index.html")


@app.route('/api/v<version>/')
def render_api_root(version):
    return jsonify({
        "onboard": {
            "url": "https://www.moveplus.app/views/welcome",
            "version": 1
        }
    })
