import os
from flask import Flask, jsonify, make_response, Blueprint
from flask import redirect, session, url_for
from flask_assets import Environment, Bundle
from authlib.integrations.flask_client import OAuth

from analyze.api import rest_api_v1
from analyze.api.v1.endpoints.users_api import ns as v1_users_ns
from analyze.views import root
from analyze.views import admin
from urllib.parse import urlencode


class AnalyzeFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='{{',
        variable_end_string='}}',
        comment_start_string='{#',
        comment_end_string='#}',
    ))


def create_app():

    app = AnalyzeFlask(__name__)
    app.secret_key = "34059085-1f90-48ed-b305-0e95120fe634"

    # Flask-Assets
    assets = Environment(app)

    css = Bundle('css/all.css',
                 'css/fontawesome.css',
                 'css/foundation.css',
                 'css/style.css',
                 output='gen/packed.css')
    assets.register('css', css)

    js = Bundle('js/jquery.js',
                'js/what-input.js',
                'js/foundation.js',
                'js/vue.js',
                'js/app.js',
                output='gen/packed.js')
    assets.register('js', js)

    # Flask-Restplus
    # Flask-Restplus settings
    app.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['RESTPLUS_ERROR_404_HELP'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register Auth0
    domain = os.environ.get('AUTH0_DOMAIN')
    baseUrl = "https://" + domain
    accessTokenUrl = "https://" + domain + "/oauth/token"
    authorizeUrl = "https://" + domain + "/authorize"
    app.oauth = OAuth(app)
    app.auth0 = app.oauth.register(
        'auth0',
        client_id=os.environ.get('AUTH0_CLIENT_ID'),
        client_secret=os.environ.get('AUTH0_CLIENT_SECRET'),
        api_base_url=baseUrl,
        access_token_url=accessTokenUrl,
        authorize_url=authorizeUrl,
        client_kwargs={
            'scope': 'openid profile email',
        },
    )

    # Register Views BluePrints
    app.register_blueprint(root.get_blueprint())
    app.register_blueprint(admin.get_blueprint())

    bpc = Blueprint('bpc', __name__)

    @bpc.route('/callback')
    def callback_handling():
        app.auth0.authorize_access_token()
        resp = app.auth0.get('userinfo')
        userinfo = resp.json()

        # Store the user information in flask session.
        session['jwt_payload'] = userinfo
        session['profile'] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        return redirect('/')

    @bpc.route('/login')
    def login():
        return app.auth0.authorize_redirect(
            redirect_uri=os.environ.get('AUTH0_CALLBACK_URL'))

    @bpc.route('/logout')
    def logout():
        session.clear()
        params = {'returnTo': url_for('root.index', _external=True),
                  'client_id': os.environ.get('AUTH0_CLIENT_ID')}
        return redirect(app.auth0.api_base_url + '/v2/logout?' +
                        urlencode(params))

    app.register_blueprint(bpc)

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
