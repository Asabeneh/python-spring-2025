from datetime import datetime
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self, sound):
        return sound

# print(Dog.name)
# print(Dog.age)
# print(Dog.bark())
d1 = Dog('little Puppy', 4)
print(d1.name)
print(d1.age)
print(d1.bark('Wooof woof'))

d2 = Dog('little Fluffy', 2)
print(d2.name)
print(d2.age)
print(d2.bark('Wooow woow'))


class Person:
    def __init__(self, first_name, last_name, birth_year, weight, height):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.weight = weight 
        self.height = height
    def get_person_info(self):
        age = self.calculate_age()
        return f'He is {self.first_name} {self.last_name}. He was born in {self.birth_year}. He is now {age} years old.'
    def calculate_age(self):
         current_year = datetime.now().year
         age = current_year - self.birth_year
         return age
    def calculate_bmi(self):
        return round(self.weight / self.height ** 2, 1)
    def check_health_status(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return 'Under weight'
        elif bmi >= 18.5 and bmi < 24.9:
            return 'Normal'
        elif bmi >= 24.9 and bmi < 30:
            return 'Overweight'
        elif bmi >= 30:
            return 'Obese'
        

p1 = Person('Asab', 'Yeta', 1925, 75, 1.73)   # Creating an object from class - Instantiating an object
print(p1)
print(p1.first_name)
print(p1.last_name)
print(p1.birth_year)
print(p1.get_person_info())
print(p1.calculate_age())
print(p1.calculate_bmi())
print(p1.check_health_status())


p2 = Person('John', 'Doe', 1990, 78, 1.88)   # Creating an object from class - Instantiating an object
print(p2)
print(p2.first_name)
print(p2.last_name)
print(p2.birth_year)
print(p2.get_person_info())
print(p2.calculate_age())
print(p2.calculate_bmi())
print(p2.check_health_status())



p3 = Person('Marta', 'Doe', 1995, 70, 1.70)   # Creating an object from class - Instantiating an object
print(p3)
print(p3.first_name)
print(p3.last_name)
print(p3.birth_year)
print(p3.get_person_info())
print(p3.calculate_age())
print(p3.calculate_bmi())
print(p3.check_health_status())




class Student(Person):
    def __init__(self, first_name, last_name, birth_year, weight, height, gender):
        super().__init__(first_name, last_name, birth_year, weight, height)
        self.gender = gender
        self.skills = []
        self.points = 0
    def get_person_info(self):
        age = self.calculate_age()
        pronoun = 'He' if self.gender == 'Male' else 'She'
        return f'{pronoun} is {self.first_name} {self.last_name}. {pronoun} was born in {self.birth_year}. {pronoun} is now {age} years old.' 
    def add_skill(self, skill):
        if type(skill) == list:
            self.skills.extend(skill)
        else:
            self.skills.append(skill)
    def get_skills(self):
        for skill in self.skills:
            print(skill)
    def add_point(self, point):
        self.points += point
    def get_all_points(self):
        return self.points


s1 = Student('David', 'Robert', 1988, 75, 1.71, 'Male')
s1.add_skill('Python')
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('MySQL')
s1.add_skill(['MongoDB','Pandas','Matplotlib','Machine learning'])
s1.add_point(5)
s1.add_point(25)
s1.add_point(40)
s1.add_point(25)
print(s1.get_person_info())
print(s1.get_skills())
print(s1.get_all_points())
s2 = Student('Sara', 'Robert', 1995, 75, 1.68, 'Female')
print(s2.get_person_info())
