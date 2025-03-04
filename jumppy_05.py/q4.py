'''
filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
'''
numbers=[1,-2,3,-5,8,-3]
a=list(filter(lambda x:x>=0,numbers))

print(a)