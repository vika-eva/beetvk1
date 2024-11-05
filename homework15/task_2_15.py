class Dog:
    age_factor = 7
    def __init__(self, age_h):
        self.age_h = age_h

    def human_age(self):
        #print(self.age_h * self.age_factor)
        return self.age_h * self.age_factor


pers = Dog(3)
print(pers.human_age())