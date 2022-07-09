import sys
import logging
from flask import Flask
from flask import request
from flask import Blueprint
from flask import render_template

logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    stream=sys.stdout,
    level=logging.DEBUG,
    )
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        username = request.form['username']
        # logger.info(f'new user: {username}')
        return render_template('click.html', username = username)
    return render_template('main.html')

@bp.route("/click", methods=["POST"])
def click():
    json_data = request.get_json()
    logging.info(f"user:{json_data['username']}, hold_time:{json_data['hold_time']}")
    return "True"


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app