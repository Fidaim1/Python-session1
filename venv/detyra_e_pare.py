# STRINGJET

teksti='Kjo eshte nje detyre me stringje'
print(teksti)

# 1) Ketu eshte perdorur metoda (split) per ndarjen e variables ne nje liste.
teksti='Kjo eshte nje detyre me stringje'
print(teksti.split())

# 2) Ketu eshte perdorur metoda (capitalize) per zevedesimin e shkronjes te pare ne te madhe.
lower_case_text='shkronja'
print(lower_case_text.capitalize())

# 3) Printimi i tre elementeve te pare tek variabla teksti.
print(teksti[:3])

# 4) Printimi i fjales 'detyre' nga variabla teksti.
print(teksti[14:20])

# 5) Perdorimi i operatorit (+) per krijimin e variables C.
a='mate'
b='matika'
c=(a+b)
print(c)

# LISTAT

lista_ime= ['1','2','3','4','1','2','True','False','test','test','emri']
print(lista_ime)

# 1) Printimi i gjatesis se listes behet me metoden (len).
print(len(lista_ime))

# 2) Update i listes me emrin Fidaim me metoden (append).
lista_ime.append('Fidaim')
print(lista_ime)

# 3) Bashkimi i listave me metoden (extend).
lista2= ['mbiemri','mosha']
lista_ime.extend(lista2)
print(lista_ime)

# 4) Heqja e duplicates nga lista me metoden (set).
print(set(lista_ime))

# TUPLES

# 1) Krijimi i nje Tuple dhe vertetimi i tipit (Tuple)
firma= ('nike',)
print(type(firma))

# DICTS

# 1) Krijimi i nje variable te tipit Dict.
a= {'emri':'Fidaim','mbiemri':'Ahmeti','mosha':'26'}
print(a)

# 2) Shtimi i (key).
a['numri i telefonit']= 38349844721
print(a)

# 3) Konfirmimi me update i Dict.
b= {'numri i telefonit':38349844721}
a.update(b)
print(a)

# 4) Printimi i vetem (Keys).
print(a.keys())

# 5) Printimi i vetem (Values).
print(a.values())

# 6) Krijimi i nje dict te ri me te gjitha values True.
my_keys= a.keys()
my_other_keys = {'emri,','mbiemri','mosha','numri i telefonit'}
my_other_keys = dict.fromkeys(my_other_keys,'True')
print(my_other_keys)


