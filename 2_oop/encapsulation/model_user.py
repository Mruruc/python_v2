class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def getPassword(self):
        return self.__password

    def __str__(self):
        return f"{self.username}, {self.__password}"
