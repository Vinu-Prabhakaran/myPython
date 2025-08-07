
class Animal:

    def __init__(self,type,name,color):
        self.type = type
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.type} with name {self.name} and color {self.color}'

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def who_am_i(self):
        return 'I am an animal'

class Dog(Animal):

    def __init__(self,name,color):
        super().__init__('Dog',name,color)

    def speak(self):
        return f'{self.name} says WOOF!!'

    def who_am_i(self):
        return f'I am a Dog and {super().who_am_i()}'

class Cat(Animal):

    def __init__(self,name,color):
        super().__init__('Cat',name,color)

    def speak(self):
        return f'{self.name} says MEOW!!'

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title : {self.title}, Author : {self.author}, Pages : {self.pages}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'Book with title {self.title} removed')

if __name__ == '__main__':
    some_animal = Animal('Elephant','Charlie','Black')
    print(some_animal)
    dog = Dog('Lola','Yellow')
    print(dog)
    print(dog.who_am_i())
    cat = Cat('Felix','White')
    print(cat)
    print(cat.speak())

    book = Book('Python rocks!','Vinu Prabhakaran', 200)
    print(book)
    print(len(book))
    del book
