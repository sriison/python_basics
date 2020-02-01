mylist=[1,2,3,4]
print(type(mylist))

class Dog():

    def __init__(self ,breed,name):
        self.breed = breed
        self.name = name

my_dog = Dog(breed ='lab',name='tiger')
print(my_dog.name)
print(type(my_dog))
