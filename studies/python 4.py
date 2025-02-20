MyString = "bu ders bogaziciliden"
MyString[3]
# veriable tanımlayıp yazdırmak istediğimiz karakter sayısını köşeli parantez içinde yazarsak görebiliriz.
#  b 0. u 1. bosluk 2. d ise 3. karakter
len(MyString)
# len() komutu dizinin,tanımlanan veriablenin, karkater sayısını verir.
MyString[len(MyString)-1]
# bu komut bize son karakteri verir.
MyString[-5]
# eger köşeli parantez içindeki rakam eksi olursa sondan başlar saymaya
name = " isa "
surname = " ergisi"
fullname = name + surname
print(fullname)
fullname *5 
# eger bir variablede belli bir yerdenbir yere kadar karakterleri almak istersek : veraible [start:stop:step]
# yani ne demek istedik : variable [basladıgın karakter:durdugumuz karakter:kacar kacar ilerledik]
veriable = "SMSN2023blgmuh"
veriable[0:4:1] #'SMSN'
veriable[0:6:1] #'SMSN20'
veriable[0:6:2]  #'SS2'
# steppingsize = -1 dersek veriableyi ters cevirir.
veriable[::-1]
# variable.index() komutu parantez içişne çift tırnak "" ile yazılan karakter veriablede ilk kaçıncı karakterde varsa onun numarasını verir.
veriable.index("2")
veriable.index("b")
# string içşnde tek bir kaarakteri sonradan yeniden atama yaparak değiştiremeyiz.
veriable[1] = b #hata aldık
numlist = 12345
print(numlist)
numlist[1]= 0 #hata aldık
