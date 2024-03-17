import random


class Multy(object):
    def int(self,vari_1,vari_2):

     self.vari_1 = vari_1
     self.vari_2 = vari_2
    def printer(self):
        print(self.vari_1)
        print(self.vari_2)
    def randomer(self):
        self.vari_1 = random.randint
        self.vari_2 = random.randint
        print(self.vari_1)
        print(self.vari_2)
    def Sum(self):
        print(self.vari_1 + self.vari_2)
    def Max(self):
        if (self.vari_1 > self.vari_2):
            print('max='+str(self.vari_1))
        else:
            print('max='+str(self.vari_2))

if __name__ =='main':
    m = Multy(1,2)
    m.printer()
    m.randomer()
    m.Sum()
    m.Max()