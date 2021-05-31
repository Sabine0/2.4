from flask import Flask, abort, render_template, url_for
from vfinder.views import pwa, api


def build_app():
	app = Flask(__name__, template_folder="views/templates")

	# Routes

	app.register_blueprint(pwa.blueprint)
	app.register_blueprint(api.blueprint, url_prefix="/api")

	return app
