class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, I am {0}!".format(self.name))
person_1 = Person(input())
person_1.greet()
