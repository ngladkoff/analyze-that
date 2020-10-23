from user import User


class Account:
    def __init__(self):
        self.id = None
        self.name = ""
        self.owner = User()
        self.users = []
        self.games = []
