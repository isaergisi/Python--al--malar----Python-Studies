# list yöntemi : listenın adını yazar = koyar ve ardından köşeli parantezle [] karakterlerin arasında virgül olmak şartı ile yazarız.
MyFirstpyList = [1,2,3,"y"]
MyFirstpyList[2]
MyFirstpyList[3]
x,y,z = 1,2,3
YourfirstpyList = [x,y,z]
YourfirstpyList[2]
# listenin içindeki bir karakteri sonradan yeni bir atama ile değiştirebiliriz.
MyFirstpyList[0] = "jesus"
MyFirstpyList #['jesus', 2, 3, 'y']
len(MyFirstpyList)
# listenin sonuna .append() eklersek karakteri son karaktere ekleme yapar 
MyFirstpyList.append("ASLI")
MyFirstpyList #['jesus', 2, 3, 'y', 'ASLI']
#list.count() yaparsak parantez içindeki karakterden listede kac tane var onun sayısını bize verir.
MyFirstpyList.count(2)
#list.insert(,) yaparsak virgülün soluna kaçıncı mevkiye, virgülün sagındaki deger ise ne eklemek istediğimizi gireriz.
MyFirstpyList.insert(3,"cyber")
MyFirstpyList
# list.pop() yaparsak son karakteri listeden atar.
# list.remove() yaparsak parantez içidenki karakteri atar listeden.
MyFirstpyList.pop()
MyFirstpyList.remove(2)
MyFirstpyList    # ['jesus', 3, 'cyber', 'y']
# list.reverse() yaptıgımızda liste tersine cevirilir.
# list.sort() yaparsak küçükten buyuge dogru sıralar.


