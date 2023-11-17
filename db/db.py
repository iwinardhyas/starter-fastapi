#host without cyclic
class mydb(object):
    def __init__(self):
        self.host = "db4free.net"
        self.port = 3306
        self.database = "testdht11"
        self.username = "testdht11"
        self.password = "#testdht11"

class mydb2(object):
    def __init__(self):
        self.host = "52.220.113.182"
        self.port = 3310
        self.database = "test"
        self.username = "user_test"
        self.password = "user_test*123#"

class mydb3(object):
    def __init__(self):
        self.host = "process.env.HOST"
        self.port = "process.env.PORT"
        self.database = "process.env.DATABASE"
        self.username = "process.env.USERNAME"
        self.password = "process.env.PASSWORD"