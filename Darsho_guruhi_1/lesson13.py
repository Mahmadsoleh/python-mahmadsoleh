

'''
print("Khush omadied ba bozi")

nom=input("Shumo mikhohed bozi kunet? ")

if nom.lower() == 'bale':
    print('marhamat')
else:
    print('Na kor namekunam')
'''
'''
print("Khush omadied ba bozi")

nom=input("Shumo mikhohed bozi kunet? ")

if nom.lower() != 'bale':
    quit()
'''    


print("Khush omadied ba bozi")

nom=input("Shumo mikhohed bozi kunet? ")

if nom.lower() != 'bale':
    quit()

print("marhamat")
a = 0

nom1=input("Кампиютер ба чанд кисм чудо мешавад? ")
if nom1.lower() == "2":
    print("durust")
    a +=1
else:
    print("Nodurust")

nom1=input("Клавиатура ба чанд кисм чудо мешавад? ")
if nom1.lower() == "5":
    print("durust")
    a +=1
else:
    print("Nodurust")

nom1=input("Клавиатура аз чанд тукма иборат аст? ")
if nom1.lower() == "102":
    print("durust")
    a +=1
else:
    print("Nodurust")

nom1=input("Кисми асоси кампиютер? ")
if nom1.lower() == "Blok":
    print("durust")
    a +=1
else:
    print("Nodurust")

print("Muborak boshad shumo " + str(a)+" misol kor karded ")
print("Shumo kor karded " + str((a/4)*100)+ " %")


