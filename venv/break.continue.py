lista_me_emra = ['erjona', 'loreta', 'albini', 'temal']

for name in lista_me_emra:
    print(name)
    if name == 'albini':
        print ('brake it')
        break 
    print (name)

print ('==========')

for name in lista_me_emra:
    if name == 'albini':
        continue
    print (name)