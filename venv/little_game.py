import random
random_number = random.randint(0,10)
print (random_number)


am_i_a_loser = False

for i in range(10):
    a = int(input('Shkruaj nje numer:'))
    if a == random_number:
        print ('Well done')
        am_i_a_loser = False
        break
    else:
        print ('Nope try again')
        

if am_i_a_loser:
    print ('You are a loser')
    

else:
    print ('You are a genius')
    

