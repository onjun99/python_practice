name = "준규"
total_days = 84

print(f"{name}의 96일 코딩 스타트")
print(f"총 {total_days}일, 하루 1커밋")
print("Day 1 시작")

budget = int(input("여행 예산(엔)을 입력하세요: "))
days = int(input("며칠 여행하나요? "))

per_day = budget / days
print(f"하루에 {per_day:.0f}엔 쓸 수 있어요")