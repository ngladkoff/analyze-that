from flask_restplus import Resource
from app.api.v1.serializers import user
from app.api.rest_api_v1 import api

ns = api.namespace('v1/users', description='Operations relatesd to users')

USERS = [
    {
        'id': 1,
        'userName': 'usr1',
        'fullName': 'Usuario1'
    },
    {
        'id': 2,
        'userName': 'usr2',
        'fullName': 'Usuario2'
    }
]


@ns.route('/')
class UsersCollection(Resource):

    @api.marshal_with(user, as_list=True)
    def get(self):
        """
        Returns list of users.
        """
        users = USERS
        return users
