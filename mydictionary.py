x={'key':'value'}

y={'emri':'Erjona', 'mbiemri':'Miftari'}
print('ky eshte my dict', y)

emri= y['emri']
print(emri)

mbiemri= y['mbiemri']
print(mbiemri)

test= y.get('test')
print('test me get eshte',test)

test_get= y.get('test','une jam e mire')
print(test_get)
print('mos me ka ndryshu my dict',y)





#metoda items per me kthy

print('metoda item po kthejka',y.items())
y_items = y.items()
print('tipi i items eshte:',type(y_items))

#metoda values()
print('values are:',y.values())

#printimi i dyt i key dictionary

z={'emri':'Erjona', 'mbiemri':'Miftari','emri':'test'}
print(z)

# menyra 1 e add element to dict
z['mosha'] = 15
print (z)

# menyra 2 eshte me update

a={'gjinia':'femer'}

z.update(a)
print(z)

print('my values', z.values())
print('my keys', z.keys())


# metoda from keys()

my_keys = z.keys()

my_other_keys = {'a,','b','c'}

my_other_keys = dict.fromkeys(my_other_keys,'test')
print('my other dict is:', my_other_keys)

my_other_dict_1 = dict.fromkeys(my_keys,'test')
print('my other dict 1 is:', my_other_dict_1)