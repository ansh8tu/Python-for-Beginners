class Person:
    def __init__(self, name):
        self.name = name
        print(f'Hello {name}, nice to see you!')

    def talk(name):
        print(f'Hello, {name} do you know I can talk!')

name = input('> Enter your name : ')
p1 = Person(name)
Person.talk(name)
