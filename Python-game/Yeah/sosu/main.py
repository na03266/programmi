from cal import pre

m = int(input("숫자를 입력하세요>>>"))

for i in range(1, m):
    if pre(i):
        print(i, end=" ")