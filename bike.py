class bike:
  def __init__(self, color, engine_size, brand, model):
    self.color = color
    self.engine_size = engine_size
    self.brand = brand
    self.model = model

def shout_out(self):
    print('I am a '+self.engine_size+' cc '+self.color+' '+self.brand+' '+self.model)
    #print('hi thre')

x = bike('red','750','suzuki','gsxr')
print(x.color)
shout_out(x)
