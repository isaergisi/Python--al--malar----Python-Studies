a = 5 < 3
b = 5 > 3
c = 5 >= 3
d = 5 <= 3



print(a)
print(b)
print(c)
print(d)

print(a+b)
print(c+b)
print("ac")

# eger x == y dersek x y ye esit mi diye sormus oluruz 
# eger x = y dersek x in degerini y ye esitleriz

x = 10
y = 2
print( int(x == y)) 

#eger esit değil diyecek olursak ise x != y
print( int(x != y)) 

# eger iki kıyas yapmak istersek :
print (x<y and 1<3)
# and de her ikisi de true deggilse true sonucu cıkmaz

# or ekinde herhangi birisi true olması sonucun true olmasına yeter
print (x>y and 1<3)

# bir listenin içinde herhangi bir karakteri aratmak istediğimizde ; ve varsa o karakter true sonucunu istersek eger in komutunu ekleriz

print("x" in ["x",3,5,0,"*"])

dict = {"a" : 190 , "fatıma":1994}
print("fatıma" in dict)     # ditionaryde fatıma var mı diye baktık ve var ture, eger kiliti degil de anahtarı girseydik false alcaktık.
