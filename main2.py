print("Hello")

score = float(input("請輸入成績"))
if score >= 60:
    print("PASS")
else:
    print("FAIL")

if score >= 90:
    print("Rank A")
elif score >= 80:
    print("Rank B")
elif score >= 70:
    print("Rank C")
else:
    print("Rank D")