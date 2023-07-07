# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print("1. 아래 문자열의 길이를 구해보세요. \nq1변수의 문자열의 길이 = ", len(q1))
print()


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('2. print 함수를 사용해서 아래와 같이 출력해보세요.')
print('apple;orange;banana;lemon')
print()

# 3. 화면에 * 기호 100개를 표시하세요.
print('3. 화면에 * 기호 100개를 표시하세요.')
print('*' * 100)
print()

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print('4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.')
print("4. type = ", type(int("30")), int("30"))
print("4. type = ", type(float("30")), float("30"))
print("4. type = ", type(complex("30")), complex("30"))
print("4. type = ", type(str(30)), str(30))

print()
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
str5 = "Niceman"
print('5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.')
print(str5[4:])

str5_idx = str5.index("man")
print("5. ", str5[str5_idx:str5_idx+3])

print()

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
print('6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"')
str6 = "Strawberry"
print(str6[::-1])
print()

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
print('7. 다음 문자열에서 "-"를 제거 후 출력하세요. : "010-7777-9999"')
str7 = "010-7777-9999"
new_str7 = str7.replace('-','')
print(new_str7)

print()
# 정규 표현식
import re
print("7. ", re.sub('[^0-9]','', str7))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
print('8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"')
str8 = 'http://daum.net'
print(str8[5:])
print()

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
print('9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"')
str9 = 'NiceMan'
print(str9.upper())
print(str9.lower())

print()
# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
print('10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"')
str10 = "abcdefghijklmn"
print(str10[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
list11 = ["Banana", "Apple", "Orange"]
print('다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]')
list11.remove('Apple')
print(list11)

print()
# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuple12 = (1,2,3,4)
print('12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)')
print(list(tuple12))
print()

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
print("13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>")
dict13 = {"성인" : 100000, "청소년" : 70000, "아동" : 30000}
print(dict13)
print()

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
print('14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.')
dict13["소아"] = 0
print(dict13)
print()

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.')
print(dict13.keys())
print(list(dict13.keys()))
print()

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print("16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.")
print(dict13.values())
print(list(dict13.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
