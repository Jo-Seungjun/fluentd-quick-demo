
import pdb
import logging
from flask import request
from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('click.html', username = username)
    return render_template('main.html')

@app.route("/click", methods=["POST"])
def click():
    json_data = request.get_json()
    logging.info(f"user:{json_data['username']} agent:{request.headers['User-Agent']} hold_time:{json_data['hold_time']}")
    return "True"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)