from flask import Flask, request, render_template, make_response, render_template_string
from urllib.parse import unquote
import logging
logging.basicConfig(level=logging.INFO)

import bot

app = Flask(__name__)

# obviously this is the vulnerable function. XSS Triggered by the 404 page
@app.errorhandler(404)
def page_not_found(e):
    url = unquote(request.url)
    return render_template_string(f'Page not found: %s' % url), 404


@app.route('/')
def index():
    return render_template('index.html', error="")


@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        url = request.form["url"]
        if not url.startswith("http") and not url.startswith("https"):
            return {"failure": 1, "message": "Invalid URL."}
        else:
            bot.visit_page(url)
            return make_response(render_template('index.html', error=f"You went to page: {url}"))

    except OSError:
    # except Exception as exception:
        #logging.error("Error: %s", exception)
        return {"failure": 1, "message": "Something went wrong."}




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)