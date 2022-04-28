#1
food = "Python's favorite food is perl"
print(food)

#2
multiline = """
Life is too short
You need Python
"""
print(multiline)

#3
head = "Pyhton"
tail = " is fun!"
print(head+tail)

#4
a = "python"
print(a * 2)

#5
print("=" * 50)
print("My Program")
print("=" * 50)

#6
a = "Life is too short jangchanggeun voice"
print(len(a))

#7 파이썬은 0부터 숫자를 센다.
a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[-1])
print(a[0])
b = a[0] + a[1] + a[2] + a[3]
print(b)
print("'"+a[0:4]+"'")
print(a[0:6])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])

#8 Pithon 문자열 -> Python 바꾸기
a = "Pithon"
a[:1]
a[2:]
print(a[:1] + 'y' + a[2:])

#9 문자열 포맷팅
#소수(%f)
#문자1개(%c)
#숫자(%d)
print("I eat %d apples. " % 3)
#문자(%s, but %s는 숫자,문자 등 어떤 형태든 가능)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
day = "three"
#2개이상값넣기
print("I eat %d apples. so I was sick for %s days." % (number,day))
#%표시할때는 %%
print("it is %d%%." % 98)

#format 함수를 사용한 포매팅
print("I eat {0} apples". format(3))

#오른쪽 정렬
print("{0:>10}". format("hi"))

#가운데 정렬
print("{0:^10}". format("hi"))

#공백채우기
print("{0:=^10}". format("hi"))

# f 문자열 포매팅
name = '이주원'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

#'!!!python!!!'
print("{0:!^12}". format("python"))
print(f'{"python":!^12}')

#문자중 b의 개수
a= "hobby"
print(a.count('b'))

#위치 알려주기
a = "Python is the best choice"
print(a.find('b'))
print(a.index('b'))

#문자열 삽입
print(",".join('abcd'))
print(",".join(['a','b','c','d']))

#소문자 -> 대문자 바꾸기
a ="hi"
print(a.upper())

#대문자 -> 소문자
a = "HI"
print(a.lower())

#공백지우기
a = "    jangk34   "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "your leg"))

#문자열 나누기
a = "Life is too short"
print(a.split())
#특정 구분자로 나누기 -> split() 안에 특정 구분자 입력
b = "a:b:c:d"
print(b.split(":"))

#리스트 자료형
odd = [1,3,5,7,9]
print(odd)

a = [1,2,3]
print(a)
print(a[1])
print(a[0]+a[2])

a = [1,2,3,['a','b','c']]
print(a[-1])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a = [1,2, ['a', 'b', ['Life','is']]]
print(a[2][2][0])

#리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
a = "12345"
print(a[0:2])

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
print(b,c)

A = [1,2,3,4,5]
print(A[1:3])

a = [1,2,3, ['a','b','c'],4,5]
print(a[2:5])
print(a[3])

#리스트 더하기(+,*)
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)

#리스트 길이 구하기
a = [1,2,3]
print(len(a))

#리스트 수정
a = [1,2,3]
a[2] = 4
print(a)

#del함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[:2]
print(a)

#append함수 사용해 리스트에 요소 추가
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#sort함수 리스트 정렬
a = [1,4,3,2]
a.sort()
print(a)

a = ['b','a','c']
a.sort()
print(a)

#reverse함수 뒤집기
a = ['a','c','b']
a.reverse()
print(a)

#index함수 배열상 위치 반환
a = [1,2,3]
print(a.index(3))
print(a.index(1))

#insert함수 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

#remove 리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3) #첫번째 동일 값만 제거, 뒷단의 다른 숫자도 삭제시 한번더 함수 명령
print(a)

#pop리스트 요소 끄집어내기
a = [1,2,3]  #리스트의 맨 마지막 요소 돌려주고 그 요소 삭제
a.pop()
print(a)
a = [1,2,3]
a.pop(1)
print(a)

#숫자세기
a = [1,2,3,1]
print(a.count(1)) #1이라는 숫자

#extend확장
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)

########## 튜플 자료형
t = ()
t2 = (1,) ## 1개값은 뒤에 ,
t3 = (1,2,3)
t4 = 1,2,3 ## 가로 없어도 무방
t5 = ('a','b',('ab', 'cd'))

#튜플 인덱싱
t1 = (1,2,'a','b')
print(t1[0])
print(t1[3])
print(t1[1:])
t2 = (3,4)
print(t1 + t2)
print(t2 * 3)

#튜플 길이 구하기
print(len(t1))

t3 = (1,2,3)
t4 = (4,)
print(t3 + t4)

#딕셔너리
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'} # key : value

#딕셔너리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

del a[1] ## 딕셔너리 요소 삭제
print(a)

