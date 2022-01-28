class Drejtkendshi:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def perimetri(self):
        return 2*self.a + 2*self.b

    def syprina(self):
        return self.a * self.b

my_obj = Drejtkendshi(2,4)
print (my_obj.perimetri())
print (my_obj.syprina())


class Katrori(Drejtkendshi): # (inherit) class eshte me trashegu nje kalse te re nga nje klase prindore
    def __init__(self,a):
        super().__init__(a,a)  # (super) eshte metode qe e thirr initin e parent class
        self.a = a
        
    # def perimetri(self):
    #     return 4*self.a 

    # def syprina(self):
    #     return self.a * self.a

my_obj = Katrori(5)
print (my_obj.perimetri())
print (my_obj.syprina())