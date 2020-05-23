from flask import Flask, jsonify, make_response
from analyze.api import rest_api_v1
from analyze.api.v1.endpoints.users_api import ns as v1_users_ns
from analyze.views import root
from analyze.views import admin


def create_app():

    app = Flask(__name__)

    # Flask-Restplus
    # Flask-Restplus settings
    app.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['RESTPLUS_ERROR_404_HELP'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register Views BluePrints
    app.register_blueprint(root.get_blueprint())
    app.register_blueprint(admin.get_blueprint())

    # Register API BluePrints
    apiBlueprint = rest_api_v1.get_blueprint()
    rest_api_v1.api.init_app(apiBlueprint)
    rest_api_v1.api.add_namespace(v1_users_ns)
    app.register_blueprint(apiBlueprint)

    # Error handling
    @app.errorhandler(400)
    def handle_400_error(_error):
        """Return a http 400 error to client"""
        return make_response(jsonify({'error': 'Misunderstood'}), 400)

    @app.errorhandler(401)
    def handle_401_error(_error):
        """Return a http 401 error to client"""
        return make_response(jsonify({'error': 'Unauthorised'}), 401)

    @app.errorhandler(404)
    def handle_404_error(_error):
        """Return a http 404 error to client"""
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.errorhandler(500)
    def handle_500_error(_error):
        """Return a http 500 error to client"""
        return make_response(jsonify({'error': 'Server error'}), 500)

    return app
