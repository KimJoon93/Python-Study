import sys
import io

#1. 사전 읽고 List에 저장
list_voca = []

with open("C:/Users/Joon/Desktop/jooncodefolder/고유명사_기초/고유명사_기초.txt",'r') as fptr :
    for line in fptr.readlines() :
        if(len(line)) > 1 :
            list_voca.append(line)
#2. 단어크기 출력
print("=====================================")
print("단어 개수: ", len(list_voca))
#3. List 내용 가나다 순 정렬
list_voca.sort()

#4. 10개 단어 출력
print("=====================================")
for i in range(10):
    print(list_voca[i])

#5. "은하수" 포함된 단어 출력
print("=====================================")
for s in list_voca:
    if "은하수" in s:
        print("은하수 포함된 단어: ",s)        

fptr.close()