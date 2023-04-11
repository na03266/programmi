import tkinter as tk

# 햄버거의 종류와 가격을 딕셔너리로 정의합니다.
menu = {"1": {"name": "치즈버거", "price": 5000},
        "2": {"name": "불고기버거", "price": 6000},
        "3": {"name": "새우버거", "price": 5500}}

# 버튼을 눌렀을 때 실행되는 함수입니다.
def button_clicked():
    # 사용자로부터 햄버거의 종류와 수량을 입력받습니다.
    burger = burger_var.get()
    quantity = int(quantity_var.get())

    # 가격을 계산합니다.
    price = menu[burger]["price"] * quantity

    # 결과를 출력합니다.
    result_label.config(text="햄버거 종류: " + menu[burger]["name"] + "\n수량: " + str(quantity) + "\n가격: " + str(price) + "원")

# GUI를 생성합니다.
root = tk.Tk()
root.title("햄버거 주문 프로그램")

# 햄버거 종류를 선택하는 라디오 버튼을 생성합니다.
burger_var = tk.StringVar()
burger_var.set("1")
for key in menu:
    burger_radio = tk.Radiobutton(root, text=menu[key]["name"], variable=burger_var, value=key)
    burger_radio.pack()

# 수량을 입력하는 엔트리를 생성합니다.
quantity_var = tk.StringVar()
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.pack()

# 주문 버튼을 생성합니다.
order_button = tk.Button(root, text="주문", command=button_clicked)
order_button.pack()

# 결과를 출력하는 라벨을 생성합니다.
result_label = tk.Label(root, text="")
result_label.pack()

# GUI를 실행합니다.
root.mainloop()