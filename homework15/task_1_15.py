class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age



    def talk(self):
        print(f"Здравствуйте, меня зовут {self.firstname} {self.lastname} мне {self.age} лет")


tom = Person("Карл", "Джонсон", 26)
tom.talk()
