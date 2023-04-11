from lib.cal import add
from lib.cal import substract
from lib.cal import multiply
from lib.cal import divide

print("사칙연산을 하세요")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

choice = input("선택하세요(1/2/3/4):")

x = int(input("첫번째 숫자 : "))
y = int(input("두번째 숫자 : "))

if choice == '1':
    print(x,"+",y, "=", add(x,y))

elif choice == '2':
    print(x,"-",y, "=", substract(x,y))

elif choice == '3':
    print(x,"*",y, "=", multiply(x,y))

elif choice == '4':
    print(x,"/",y, "=", divide(x,y))

else : 
    print("선택할 수 없는 번호입니다.")