from flask import Blueprint, render_template, jsonify
import random
blueprint = Blueprint("api", __name__)


@blueprint.route("/")
def index():  # Endpoint

	data = list(range(1,100))
	random.shuffle(data)

	return jsonify(data)
