import random

answer = random.randint(1, 100)
tries = 0

print("1~100 사이의 숫자를 맞춰보세요!")

while True:
    try:
        guess = int(input("입력: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue

    tries += 1
    if guess < answer:
        print("더 큰 수입니다.")
    elif guess > answer:
        print("더 작은 수입니다.")
    else:
        print(f"정답! {tries}번 만에 맞췄습니다.")
        break
