from typing import Reversible


#Strings
x=("Eriona eshte mesuese e mire")
print(x)

#Integers
y=("10")
print(y)

#Lists
veturat=["Mercedes","Bmw","Audi","Range Rover"]
print(veturat)

#Tuples
veturat=("Mercedes","Bmw","Audi","Range Rover")
print(veturat)

#Shtimi i elementeve mbrenda listave
lista1=["Fidaim"]
lista1.append("Fidaim")
print(lista1)

#Shikimi i elementeve mbrenda listave
print(len(veturat))

#Bashkimi i listave
lista1.extend(veturat)
print(lista1)

#Qasja ne element te listets
print(lista1 [3])

#Printimi i dy apo me shume elementeve mbrenda listave
print(lista1[:2])

#Boolien True ose False
a=True
b=False

lista1.append(a)
lista1.append(b)


lista3=["1","1","2","2","3"]
print(set(lista3))