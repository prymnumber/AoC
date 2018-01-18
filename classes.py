class food():
    def __init__(self,v_name,v_size,v_taste):
        self.edible = True
        self.name = v_name
        self.size = v_size
        self.taste = v_taste

    def whatAmIEating(self):
        return self.name

class fruit(food):
    def __init__(self,v_name,v_size,v_taste,v_color,v_ripe):
        food.__init__(self,v_name,v_size,v_taste)
        #super().__init__(self,v_name,v_size,v_taste)
        self.color = v_color
        self.ripe = v_ripe

    def eat(self):
        if self.ripe:
            print('crunch crunch crunch')
        else:
            print('can'+'\''+'t not ripe yet')

momo = food('momo','small','delicious')

apple = fruit('fruit','any','sweet','red',False)
apple.eat()
print(apple.name)
print(apple.color)

print(fruit.__class__.mro())
