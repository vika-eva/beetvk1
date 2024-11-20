import re
# from validate_email import validate_email

reg = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

class Validate1:
    def __init__(self, value):
        self.value = value
        self.validate(value)

    @staticmethod
    def validate(value):
        if re.search(reg, value):
            print("Validate1 its ok")
            return True
        else:
            print("Error")

b = Validate1("vik5768khkja@gmail.com")