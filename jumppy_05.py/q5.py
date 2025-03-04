'''
234라는 10진수의 16진수는 다음과 같이 구할 수 있다. 
이번에는 반대로 16진수의 문자열 0xea를 10진수로 변경해보자.

>>> hex(234) ‘0xea’
'''
#0xea=14*16^1 + 10*16^0=224+10=234

hex_value='0xea'
decimal_value=int(hex_value,16)
print(decimal_value)