def is_my_number_cift(numri):
     
    if numri % 2 == 0:
        return True
    else:
        return False

def check_lista_ime(lista):
    for item in lista:
        if is_my_number_cift(item):
            lista_cift.append(item)
        else:
            lista_tek.append(item)
    return lista_cift, lista_tek    
    

lista_ime = [1,2,3,4,5,6,7,8,9,10]
lista_cift =[]
lista_tek = []
print ('tek', lista_tek)
print ('cift', lista_cift)
vlera1, vlera2 = check_lista_ime(lista_ime)
print ('vlera1 eshte',vlera1)
print ('vlera2 eshte',vlera2)
    
# args eshte kur deshirojm me thirr parametra pa fund

def test_funk(*args):
     print (args)

def my_keyword_funk(**kwargs):
    print ('my kwargs', kwargs)
    return kwargs

test_funk('erjona', 'miftari', 28)
print ('=======')
my_dickt = my_keyword_funk(emri='erjona', mbiemri= 'miftari', mosha=28)

for element in my_dickt.values():
    print (element)