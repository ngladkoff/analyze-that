from flask import Blueprint
from flask_restplus import Api

REST_V1_API = Blueprint('rest_v1_api', __name__, url_prefix='/api/v1')


def get_blueprint():
    return REST_V1_API


api = Api(version='1.0', title="Analyze That API",
          description="Analyze That Interface")
