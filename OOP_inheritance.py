class Animal():
    def __init__(self):
        print("Animal created")

    def eat(self):
        print("Eating")


class Dog (Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

    def bark():
        print("Woof!")

d = Dog()           

