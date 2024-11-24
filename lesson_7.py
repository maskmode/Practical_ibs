class Animal:
    instance_count = 0

    def __init__(self):
        Animal.instance_count += 1

    @staticmethod
    def get_instance_count():
        print(Animal.instance_count)

    def voice(self):
        print("ррррр")

class Dog(Animal):
    def voice(self):
        print("гав-гав")

class Cat(Animal):
    def voice(self):
        print("мяу-мяу")

class Raven(Animal):
    def voice(self):
        print("кар-кар")

barbos = Dog()
barbos.voice()

murka = Cat()
murka.voice()

edgar = Raven()
edgar.voice()

Animal.get_instance_count()