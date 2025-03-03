class Person:
    body = 1
    eyes = 2
    hands = 2
    legs = 2

    def __init__(self, name: str, age: int, home_adr, nationality: str, live, sport: str, email: str, parents):
        self.name = name
        self.age = age
        self.home_addr = home_adr
        self.nationality = nationality
        self.live = live
        self.sport = sport
        self.email = email
        self.parents = parents

class Student(Person):

    def __init__(self, name, age, home_adr, nationality, live, sport, email, parents, id_card_student):
        super().__init__(name, age, home_adr, nationality, live, sport, email, parents)
        self.id_card_student = id_card_student

    def about_stud(self):
        print(f"about me {self.name}, {self.age}, {self.home_addr}, {self.nationality}, {self.live}, {self.sport}, {self.email}, {self.parents}, {self.id_card_student}")



class Teacher(Person):

    def __init__(self, name, age, home_adr, nationality, live, sport, email, parents, id_card_teacher, salary):
        Person.__init__(self, name, age, home_adr, nationality, live, sport, email, parents)
        self.id_card_teacher = id_card_teacher
        self.salary = salary

    def about_teach(self):
        print(f"about {self.name}, {self.age}, {self.salary}, {self.id_card_teacher}")

