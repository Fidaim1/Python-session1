x = 10
 
if x >= 1 and x <= 9:
     print ('Njeshifror')

elif x >= 10 and x <= 99: 
    print ('Dyshifrore')

elif x >= 100 and x <= 999:
    print ('Treshifror')

else :
    print ('Me e madhe se treshifor')


ud_username = 'Fidaim Ahmeti'
ud_password = '12345'

username = input ('Jepe emrin e shfrytezuesit: ')
password = input ('Jepe passwordin: ')

if username == ud_username and password == ud_password:
    print ('Home Page')

else:
    print ('Incorrect username and pass')