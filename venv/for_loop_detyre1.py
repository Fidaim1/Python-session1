lista_ime = [1,2,3,4,5,6,7,8,9,10]
print (lista_ime)

numrat_cift = []
numrat_tek = []

for number in lista_ime:
    print (number)
    if (number % 2) == 0:
        numrat_cift.append(number)
    else:
        numrat_tek.append(number) 


print ('Numrat cift jane keta numra:', numrat_cift)
print ('Numrat tek jane keta numra:', numrat_tek)



