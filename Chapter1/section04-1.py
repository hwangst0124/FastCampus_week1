# 데이터 타입

''' 
    파이썬 데이터 타입 종류
    - Boolean
    - Numbers
    - String
    - Bytes
    - Lists
    - Tuples
    - Sets
    - Dictionaries
'''

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(v_tuple)

print()

print('v_str1 = ', type(v_str1))
print('v_bool = ', type(v_bool))
print('v_str2 = ', type(v_str2))
print('v_float = ', type(v_float))
print('v_int = ', type(v_int))
print('v_dict = ', type(v_dict))
print('v_list = ', type(v_list))
print('v_tuple = ', type(v_tuple))
print('v_set = ', type(v_set))

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)
result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y += 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = divmod(100, 8) # n = 몫, m = 나머지
print(n, m)

import math

print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수 출력
print(math.floor(3.874)) # 3.874 보다 작으면서 가장 큰 정수 출력


# +
print("##### + #####")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 
print("i1 + f1 : ", i1 + f1)  # 실수와 정수끼리

# -
print("##### - #####")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)
print("i1 - f1: ", i1 - f1)

# *
print("##### * #####")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)
print("i1 * f1: ", i1 * f1)

# /
print("##### / #####")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)
print("i1 / f1: ", i1 / f1)
print("f1 / i1: ", f1 / i1)

# //
print("##### // #####")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)
print("i1 // f1: ", i1 // f1)
print("f1 // i1: ", f1 // i1)

# %
print("##### % #####")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)
print("i1 % f1 :", i1 % f1)
print("f1 % i1 :", f1 % i1)

# **
print("##### ** #####")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)
print("i1 ** f1: ", i1 ** f1)
print("f1 ** i1: ", f1 ** i1)