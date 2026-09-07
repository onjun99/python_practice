#変数

h = 188.0
print(h)    # 188.0

w = 104.0
print(w)    # 104.0
print(w / (h/100.0)**2)    # 29.3

# 변수 재정의
w = 104.0 - 10
print(w)    # 94.0
print(w / (h/100.0)**2)    # 26.5

# 정의되지 않은 변수를 쓰면 NameError
# print(BMI)

#대체

w = w-10
print(w / (h/100.0)**2)    # 23.9

# 누적 대입문
print(w)      # 94.0

w -= 10
print(w)      # 84.0

w += 10
print(w)      # 94.0

w *= 2
print(w)      # 188.0

# 함수 정의 및 반환값

def bmi(h, w):
    return w / (h/100.0)**2

print(bmi(188.0, 104.0)) 

print(1.1*bmi(174.0, 119.0 * 0.454))  

def felt_air_temperature(temperature, humidity):
    return temperature - 1 / 2.3 * (temperature - 10) * (0.8 - humidity / 100)

print(felt_air_temperature(28.0, 50.0))   

# 예약어

def ft_to_cm(f, i):
    return f * 30.48 + i * 2.54

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0.0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0.0

# 연습 quadratic(a, b, c, x)

def quadratic(a, b, c, x):
    return a * x**2 + b * x + c

assert quadratic(1, 2, 1, 3) == 16
assert quadratic(1, -5, -2, 7) == 12

# 로컬 변수

import math

def heron(a, b, c):
    s = 0.5*(a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c) )

print(heron(3, 4, 5))    # 6.0

# 함수 밖에서 s를 쓰면 NameError (확인하려면 주석 풀기)
# print(s)

s = 100
print(heron(3, 4, 5))    # 6.0
print(s)    # 100

# print

def heron(a,b,c):
    s = 0.5*(a+b+c)
    print('The value of s is', s)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#heron(1,1,1) 이렇게 쓰면 값까지 출력이 안됨
print(heron(1,1,1))

# print와 return

def heron(a,b,c):
    s = 0.5*(a+b+c)
    print('The value of s is', s)
    print(math.sqrt(s*(s-a)*(s-b)*(s-c)))         # 이렇게 치면 출력 안됨
    return print(math.sqrt(s*(s-a)*(s-b)*(s-c)))   # 이렇게 치면 출력 안됨 

#위에 return math.sqrt(s*(s-a)*(s-b)*(s-c)) 이렇게 쳐야 출력됨

# 주석과 공란

# heronの公式により三角形の面積を返す
def heron(a,b,c): # a,b,c は三辺の長さ

    # 辺の合計の半分をsに置く
    s = 0.5*(a+b+c)
    print('The value of s is', s)

    return math.sqrt(s * (s-a) * (s-b) * (s-c))

# 연습 문제

import math

def qe_disc(a, b, c):
    return b**2 - 4*a*c

def qe_solution1(a, b, c):
    return math.sqrt(qe_disc(a, b, c))

def qe_solution2(a, b, c):
    return math.sqrt(qe_disc(a, b, c))

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1
#assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
#assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
#assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
#assert round(qe_solution2(1, -5, 6) - 3, 6) == 0

# 글로벌 변수

g = 9.8
def force(m):
    return m*g

force(104)
print(force(104))

g = g/6
force(104)
print(force(104))

a = 10
def foo():
    return a
def bar():
    a = 3
    return a

print(foo())
print(bar())
print(a)

a = 20
print(foo())

def boo(a):
    return a
print(boo(5))
print(a)