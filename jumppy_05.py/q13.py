'''
Q13. random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
'''
import random
a=random.sample(range(1,46),6)

print(a)