emri = input ('Shkruaj emrin tend:')
emri = emri.capitalize()
print (emri)

x = 'Erjona'
print(len(emri))

if emri == x:
     print('Ju keni shkruajtur emrin sakt')

else:
    print ('Ju keni shkruajtur emrin gabim')



emri = input ('Shkruaj emrin tend:')
mbiemri = input ('Shkruaj mbiemrin tend:')
gjinia = input ('Gjinia:')

if gjinia.lower() == 'femer' or gjinia.lower() =='f':
    gjinia = 'F'

if gjinia.lower () == 'mashkull' or gjinia.lower () == 'm':
    gjinia = 'M'

else: 
    gjinia =''
    print ('kjo gjini nuk ekziston')



te_dheneat_e_mia = {'Emri':emri, 'mbiemri': mbiemri,}
print(te_dheneat_e_mia)
 
if gjinia != '':
     te_dheneat_e_mia['gjinia'] = gjinia
else: 
    print ('qa ke bo kshtu!!!!')
      
print(te_dheneat_e_mia)      