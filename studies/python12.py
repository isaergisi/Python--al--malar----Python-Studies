# kosul komutlarında if önce eklenir ve ardındna koşul eklenir.
myfirstconditionalsentence  = 14 + 86
mysecondconditionalsentence = 15 + 56/4


if myfirstconditionalsentence/3 > mysecondconditionalsentence :
    print( " aziz bayar university")
elif myfirstconditionalsentence/3 <  mysecondconditionalsentence :
    print("pamukkale university")
else :
    print ("19 mayis university")


# basit anlatımla if elif ve else komutlarının mantıgını gosterdim.
# datayı kullanıcıdan isteyelim:

schoolnumber =input("Please, enter your school ID number:\n" )

if schoolnumber[0:3] == 24 :
    print("Your university starting year: 2024")
else :
    print("Your university starting year: 2023 and before")

 # kosulu belirttikten sonra : (iki nokta) koymayı unutmayın.
 




