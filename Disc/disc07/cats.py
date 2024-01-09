class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        if self.is_alive:
            self.lives -= 1
        else:
            print("No live to lose!")
        if self.lives == 0:
            self.is_alive = False

class NoisyCat(Cat):
    def talk(self):
        print((f"{self.name} says meow!\n") * 2, end="")

    def __repr__(self):
        return f"NoisyCat('{self.name}', '{self.owner}')"

    def __str__(self):
        return f"{self.owner}'s cat {self.name}"








