from flask_restplus import fields
from analyze.api.rest_api_v1 import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True,
                         description='The unique identifier of a user'),
    'userName': fields.String(required=True, description='User alias'),
    'fullName': fields.String(required=True, description='User Full Name')
})
