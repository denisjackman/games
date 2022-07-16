'''
    solo learn class example
'''
class animal:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('Woof!')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

felix = Cat("Ginger", 4)
rover = Cat("dog coloured", 4)
stumpy = Cat("brown", 3)
Sugar = Cat("tabby",16)
Frankie = Cat("tabby", 1)

print(Frankie.color)

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

rect = Rectangle(7, 8)
print(rect.color)
