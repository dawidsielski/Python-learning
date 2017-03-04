class MyException(Exception):
    """My Exception class"""
    def __init__(self,msg):
        self.msg = msg

error = MyException("Error")
print(error.__doc__)