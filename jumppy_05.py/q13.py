'''
Q13. random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
'''
import random
a=[]  #번호 저장할 리스트

while len(a)<6:
  num.random.randint(1,45)
  if num not in a:
    a.append(num)

print(a)
