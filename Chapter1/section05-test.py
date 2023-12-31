# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k,v in q1.items():
    if k == '가을':
        print(v)


# print(''.join([q1[s] for s in q1 if s == '가을']))


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if v == '사과' :
        print(k, v)
        break
else:
    print("사과 없음")

# hasApple = ['사과다!' for key, val in q2.items() if key == '사과' or val == '사과']

# if len(hasApple) > 0:
#     print('사과 있음')
# else:
#     print('사과 없음' )


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 823

if 0 > score or 100 < score:
    print("?")
elif score > 81:
    print("A학점")
elif score > 61:
    print("B학점")
elif score > 41:
    print("C학점")
elif score > 21:
    print("D학점")
else:
    print("E학점")


# score = 100
# grade = ''
# if 0 < score > 100:
#     grade = '나가'
# elif score > 80:
#     grade = 'A'
# elif score > 60:
#     grade = 'B'
# elif score > 40:
#     grade = 'C'
# elif score > 20:
#     grade = 'D'
# elif score >= 0:
#     grade = 'E'

# print(grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 555
b = 6
c = 18
best = 0

best = a
if best < b:
    best = b
if best < c:
    best = c

print(best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v == "정":
        continue
    else:
        print(v, end="")
print()
print(''.join([v for v in q3 if v != '정']))
new_q3 = [v for v in q3 if v != '정']
print(new_q3)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=' ')
print()
print(' '.join([str(s) for s in range(1, 101) if s % 2 != 0]))
# print(' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for v in q4:
    if len(v) >= 5:
        print(v, end=' ')

print([s for s in q4 if len(s) >= 5])


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q5:
    if v.islower():
        print(v, end=" ")

print() 
print(' '.join([v for v in q5 if v.islower()]))


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q6:
    if v.islower():
        print(v.upper(), end=' ')
    else:
        print(v.lower(), end=' ')

print()    
print([s.upper() if s.islower() else s.lower() for s in q5])
new_q6 = [x for x in range(1, 101) if x % 2 != 0]
print(new_q6)

# 리스트 컴프리헨션
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 101)]
print(numbers2)

x = [x for x in range(1, 100) if x != 2] 