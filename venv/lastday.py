lista = []
 
emri = 'ditaefundit'

for i in emri:
    lista.append(i)

print (lista)

lista1 = [i for i in emri]

print (lista1)



my_tuple = [('a',"b"), ('c', 'd'), ('e','f')]
for el in my_tuple:
    print(el)

# Unpacking tuples.

my_tup = (1,2,3,4,5)
a , b, c, d, e, = my_tup
print (c)

a,*_ = my_tup
print(a)

a, _ , c, _ ,e = my_tup
print (a,c,e)

*_ , c, _,_ = my_tup
print (c)


dict1 = {"a": 1, 'b': 2,'c': 3, 'd': 4, 'e' : 5}
 
my_other_dict = {}

for key, value in dict1.items():
    print (key,value)
    my_other_dict[key] = value*2

print (my_other_dict)
my_other_dict = {key:value*2 for key, value in dict1.items() if key != "a"}
print (my_other_dict)