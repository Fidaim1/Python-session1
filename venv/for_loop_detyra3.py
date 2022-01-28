import random
numri_random = random.randint(1,10)

numri_random_string = str(numri_random)

for i in range (1,10):
    inputi_i_userit = input ('Shkruaj nje numer:')
    if inputi_i_userit == "":
        print ('Ju lutem shkruani diqka')
    elif inputi_i_userit != numri_random_string:
        print ('E paskate')
    else:
        print ('Bravo')
        break    