import random as ra

list = ['가위','바위','보']
gold = {'가위': 1,'바위': 2,'보': 0}

a= ra.choice(list)
b= ra.choice(list)

print ("A : " , a)
print ("B : " , b)

id_a = list.index(a)
id_b = list.index(b)

if id_a == id_b :
    print ('비겼습니다')
else :
    print ('%s가 이겼습니다.'%('A' if gold[a] != list.index(b) else 'B') )    