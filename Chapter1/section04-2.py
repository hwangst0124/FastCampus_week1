# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "NiceMan"
str3 = ''
str4 = str('ace')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collenction\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

#멀티라인
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

#문자열 형 변환
print(str(77) + 'a')
print(str(10.4))


a = 'niceman'
b = 'orange'

# print(a.islower())
# print(a.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))

a = 'niceman'
b = 'orange'

print(a[0:3]) # 0~2번째 글자 출력
print(a[0:4]) # 0~3번째 글자 출력
print(a[0:len(a)-1]) # 0~마지막 전까지 글자 출력 
print(a[0:len(a)]) # 0~마지막까지 출력
print(a[:]) # 전체출력
print(b[0:4:2]) # 0~3번째 까지 +2씩 0과 2 출력 
print(b[1:-2]) #1~뒤에서2번째 직전까지 출력 orange -> ran
print(b[::-1])

