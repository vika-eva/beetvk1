
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

msg = input("Enter a message: ")

try:
    with open("logs.txt", "a+", encoding = "utf-8") as f:
        f.write("Error" + "\n")
    if msg != 0:
        raise CustomException(msg)
except CustomException as e:
    print("error", e)

