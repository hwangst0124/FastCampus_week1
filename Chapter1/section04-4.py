# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value(Json) -> MongoDB
# 선언

a = {'name' : 'Kim', 'Phone': '010-7777-7777', 'birth': 870214} # 'name' : 'Kim' 은 불가능 'name' : 'Park' 는 가능
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = { 'arr': [1, 2, 3, 4, 5]}

print(type(a))

#출력
# print(a['name1'])  # 직접 조회시 값이 없으면 오류
print(a.get('name'))  # get함수를 사용해서 조회시 값을 안전하게 가져올 수 있음
print(a.get('address'))  # 값이 없을 시 None 출력
print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3,)
print(a)

#keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())

print(list(a.items()))
print(1 in b)
print(2 in b)

print('name' in a)
print('name2' not in a)

# 집합(Sets) (순서x, 중복x)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)
 
t = tuple(b)  #set은 주로 형 변환해서 사용함
print(t) 

l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  # 교집합
print(s1 & s2) # 교집합

print(s1 | s2)  # 합집합
print(s1.union(s2))  # 합집합

print(s1 - s2)  # 차집합
print(s1.difference(s2))  # 차집합

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
# s3.add(7)  #값이 있으므로 자동 필터링

print(s3)

s3.remove(15)
print(s3)

print(type(s3))









