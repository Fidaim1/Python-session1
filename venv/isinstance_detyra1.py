lista_ime = [1,2,3,4,False,True,'Apple','Samsug','Lenovo',6,'Acer',False,False,7,8,9,'iPHONE',True,20,40]

lista_numra = []
lista_emra = []
lista_bool = []

lista_numra_veqant = []
lista_emra_veqant = []



for element in lista_ime:
    print(element)
    if isinstance (element,str):
        lista_emra.append(element)
        if len(element) > 3:
            lista_emra_veqant.append(element)
    elif isinstance (element, bool):
        lista_bool.append (element)
    else :
        lista_numra.append(element)




print('lista me emra', lista_emra)
print('lista me numra', lista_numra)
print('lista me bool', lista_bool)
print (lista_emra_veqant)
