print("დავალება N1")

user_num1 = int(input("შეიყვანეთ თქვენი რიცხვი:"))
if user_num1 == 10:
    print(True)

else:
    print(False)



print("დავ. N2")

user_num2 = int(input("შეიყვანეთ თქვენი რიცხვი:"))
if user_num2 %2==0:
    print(True)
else:
    print(False)


print("დავ. N3")

user_num3 = int(input("შეიყვანეთ რიცხვი: "))
if user_num3  >49 and user_num3 <101:
    print(True)
else:
    print(False)



print("დავ. N4")

user_num4 = int(input("შეიყვანეთ 1-ლი რიცხვი: "))
user_num5 = int(input("შეიყვანეთ მე-2 რიცხვი: "))
user_num6 = int(input("შეიყვანეთ მე-3 რიცხვი: "))
if user_num4 != user_num5 and user_num5 != user_num6 and user_num6 != user_num4 and user_num6 != user_num5 and user_num5 != user_num4:
    print(True)
else:
    print(False)



print("დავ. N5")

user_num7 = input("შეიყვანეთ სახელი: ")
user_num8 = int(input("შეიყვანეთ პაროლი: "))
if user_num7 == "admin" and user_num8 == 12345:
    print(True)
else:
    print(False)