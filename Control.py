########제어문

### if문

money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else:
    print("걸어가라")

#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    print("걸어가")

#주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라
pocket = ['paper', 'money', 'cellphone']
if 'card' in pocket :
    print("버스를 타고 가라")
else :
    print("걸어가라")

# 또는
if 'card' not in pocket :
    print("걸어가라")
else:
    print("버스를 타고 가라")

#주머니에 돈이 있으면 택시를타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['paper', 'money']
card =True
if 'money' in pocket :
    print("택시를 타라")
elif card :
    print("택시를 타라")
else :
    print("걸어가라")

## 중요 ! 조건부 표현식
# message = "success" if score >= 60 else "failure"
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
