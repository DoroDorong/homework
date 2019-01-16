# gatcha.py
import random
result = ['소유욕','뜨거운 가슴','모래가면','별의 바다','깊이 빠지다','기억의 조각','엉키는 시선','그리운 바닷바람','너는 내 거','격전','그해 가을','나란히','찾았다','방황하는 눈동자','어둠 속의 빛','바다보다 깊은','부드러운 마음','바깥 세상','따뜻한 순간','빗속의 만남']
ruby = int(input("돈을 넣어 주세요:"))
while ruby:
    if ruby > 200:
        print((random.choice(result))+"을(를) 획득하였읍니다.")
        print("남은 루비는 %d개입니다." %(ruby-200))
        ruby = ruby-200
    elif ruby == 200:
        print((random.choice(result))+"을(를) 획득하였읍니다.")
        print("루비가 다 떨어졌습니다. 충전하시겠습니까?")
        break
    else:
        print("띠용?! 돈이 없다네요?! 출근해서 돈이나 벌어와!")
        print("1회 시행까지 필요한 루비는 %d개입니다" %(200-ruby))
        break
