import random as ra
import sys

dice = [i for i in range (1 , 7)]
gamecount = 10

for j in range (0, gamecount):
    a=ra.choice(dice)
    b=ra.choice(dice)

    # print ("a의 주사위 값: ", a)

    # print ("b의 주사위 값: ", b)

    # if(a>b) :
    #     print("a가 커요")
    # elif(a==b) :
    #     print("같아요")
    # else :
    #     print("b가 커요")
    if(a==b) :
        print("비겼습니다")
        sys.exit()
    else :
        print('%s가 이겼습니다'%('a' if a >b else 'b'))        

