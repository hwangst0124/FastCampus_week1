# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'Banana', 'Orange']
e = [10, 100, ['pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]  #리스트 안에 있는 원소들이 c리스트에 들어감 (Slice 사용)
print(c)

c[1] = ['a', 'b', 'c']  #리스트 안에 리스트 자체가 들어감
print(c)

#리스트 안에 있는 원소를 삭제
del c[1]
print(c)

del c[-1]
print(c)
print()
print()
print()

#리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2)  #리스트에서 숫자 2를 찾아서 지움  del y[1]와의 차이점 : 인덱스의 번호로 지움
y.remove(7)
print(y)
y.pop()
print(y)
ex = [88,77]
# y.append(ex)  #append: [6, 5, 4, 3, [88, 77]]
y.extend(ex)  #extend: [6, 5, 4, 3, 88, 77]
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2] # error

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

# 튜플 함수

z = (5, 2, 1, 3, 1)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))