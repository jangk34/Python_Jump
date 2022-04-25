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


