n = int(input("숫자를 입력하세요: "))

for i in range(2, n+1):
    matni = True
    for j in range(2, i):
        if i % j == 0:
            matni = False
            break
    if matni:
        print(i)