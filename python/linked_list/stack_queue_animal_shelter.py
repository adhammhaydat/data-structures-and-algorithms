
class Cat:
    def __init__(self):
        self.type='cat'
        self.next=None

class Dog:
    def __init__(self):
        self.type='dog'
        self.next=None

class Animal_shelter:
    def __init__(self):
        self.front_dog=None
        self.front_cat=None
        self.rear_dog=None
        self.rear_cat=None

    def enqueue(self,animal):
        """
       Arguments: animal
        animal can be either a dog or a cat object.
        """
        if animal.type=="dog":
            if not self.rear_dog:
                self.rear_dog=animal
                self.front_dog=animal
            else:
                self.rear_dog.next=animal
                self.rear_dog=animal
        if animal.type=="cat":
            if not self.rear_cat:
                self.rear_cat=animal
                self.front_cat=animal
            else:
                self.rear_cat.next=animal
                self.rear_cat=animal

    def dequeue(self,pref):
        """
        Arguments: pref
        pref can be either "dog" or "cat"
        """


        if pref=="dog":
            if not self.rear_dog:
                raise Exception('The queue are empty')
            temp=self.front_dog
            self.front_dog=self.front_dog.next
            temp.next=None
            return temp.type
        if pref=="cat":
            if not self.rear_cat:
                raise Exception('The queue are empty')
            temp=self.front_cat
            self.front_cat=self.front_cat.next
            temp.next=None
            return temp.type

        else:
            return None

if __name__=="__main__":
    dog=Dog()
    cat=Cat()
    animal=Animal_shelter()
    animal.enqueue(dog)
    animal.enqueue(cat)
    print(animal.dequeue("cat"))

