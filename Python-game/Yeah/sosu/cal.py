def pre(n):
    if n < 2:   # 2보다 작은 수는 소수가 아님
        return False
    
    for i in range(2, n):
        if n % i == 0:  # 나누어 떨어지는 수가 있으면 소수가 아님
            return False
    return True

