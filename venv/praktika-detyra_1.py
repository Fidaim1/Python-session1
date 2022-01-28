import random

while True:
    zgjidhjet = ['rock', 'paper' , 'scissors']
    computer = random.choice(zgjidhjet)
    lojtari = None

    while lojtari not in zgjidhjet:
        lojtari = input ('rock , paper , or scissors ?:').lower()
        


    if lojtari == computer:
        print ("lojtari:" ,lojtari)
        print ("computer:",computer)
        print ("Baraz!")

    elif lojtari == "rock":
        if computer == "paper":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni humbur!")
        if computer == "scissors":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni Fituar!")


    elif lojtari == "scissors":
        if computer == "rock":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni humbur!")
        if computer == "paper":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni Fituar!")

    elif lojtari == "paper":
        if computer == "scissors":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni humbur!")
        if computer == "rock":
            print ("lojtari:" ,lojtari)
            print ("computer:",computer)
            print ("Ju keni Fituar!")
    luaj_perseri = input("Deshironi te luani prape? (po/jo):",).lower()

    if luaj_perseri != "po":
        break

print ("Mirupafshim!")
   
            

    
    
    

