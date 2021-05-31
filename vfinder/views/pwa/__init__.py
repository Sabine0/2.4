from flask import Blueprint, render_template

blueprint = Blueprint("pwa", __name__)


@blueprint.route("/")
def index():  # Endpoint
	return render_template("index.html")
