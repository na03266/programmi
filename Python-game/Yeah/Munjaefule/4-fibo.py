def fibo(n):
    piblist = [0, 1, 1]
    while piblist[-1] < n:
        piblist.append(piblist[-1] + piblist[-2])
    return piblist[:-1]

n = int(input("숫자를 입력하세요: "))
print(fibo(n))