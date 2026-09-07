#파이썬 코드를 쓰는 곳임
# 東大 교재 1-1 산술연산

import math


print(1 + 2)
print(10 - 3)
print(4 * 5)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)

# 연산자 우선순위
print(1 + 2 * 3)
print((1 + 2) * 3)

# 정수와 실수
print(int(1/1))
print(int(3.9))
print(float(3))

#얼마든지 커지는 정수
print(2**10)

#정수와 실수 사이의 변환
print(int(2.9))
print(float(2))
print(int(-2.9))
print(float(-2))

print(float(2))
print(int(2.9))
print((2+0.0))
print(int(2.9))

#반올림
print(round(3.14159, 2))
print(round(3.14159, 3))
print(round(3.9))


#수치 오차
print(math.sin(math.pi))

# 練習: 黄金比 = (√5 + 1) / 2, 약 1.618
print(math.sqrt(5) + 1 / 2)      # 괄호 없이 — 틀린 답
print((math.sqrt(5) + 1) / 2)    # 괄호 있이 — 맞는 답
