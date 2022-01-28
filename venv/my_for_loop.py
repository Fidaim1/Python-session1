lista_ime = [1,2,3,4,5,122]

print(lista_ime)
print(lista_ime[0])
print(lista_ime[1])

for number in lista_ime:
    print(number)


lista_me_emra = ['erjona', 'loreta', 'albini', 'temal']
lista_me_boolean = [True,False,False,True]

lista_me_emra.extend(lista_ime)
lista_me_emra.extend(lista_me_boolean)

for name in lista_me_emra:
    print(name)

lista_emra = []
lista_numra = []
lista_bool = []

print('a eshte kjo liste int:',isinstance(lista_ime, list))

print('lista me emra', lista_emra)
print('lista me emra', lista_numra)

for element in lista_me_emra:
    print(element)
    if isinstance(element,str):
        lista_emra.append(element)
    elif isinstance (element, bool):
        lista_bool.append (element)
    else :
        lista_numra.append(element)
       

print('lista me emra', lista_emra)
print('lista me numra', lista_numra)
print('lista me bool', lista_bool)

