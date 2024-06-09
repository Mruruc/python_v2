class Custom_Exception1(Exception):
    pass


class Custom_Exception2(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info
        super().__init__(self.message)
