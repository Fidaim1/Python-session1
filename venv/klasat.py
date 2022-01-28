class Njeriu:
    
    # funksion qe kthen rrogen
    def get_rroga(self):
        return 700
    @property
    def mosha(self):
        if self.emri == 'Erjona':
            return 28
        return 25
        
    # funksion qe kthen vendbainim
    def get_vendbanimi(self):
        return 'Prishtine'
    
    def __init__(self,emri,mbiemri):
        self.emri = emri
        self.mbiemri = mbiemri


emri = 'Temal'
mbiemri = 'hello'
njeri_1 = Njeriu (emri ,mbiemri)

print (njeri_1.get_rroga())
print (njeri_1.get_vendbanimi())
print (njeri_1.mosha)

print (njeri_1.emri) 
print (njeri_1.mbiemri) 
