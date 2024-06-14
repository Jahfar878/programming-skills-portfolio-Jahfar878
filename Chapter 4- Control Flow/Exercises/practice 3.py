#Nested decision statement

amount1=int(input("Enter amount 1:"))
amount2=int(input('Enter amount 2 '))


if amount1>300 and amount2 < 400:
    if amount1 > amount2:
        print("amount2 is greater")
    elif amount1 < amount2:
        print("amount2 is greater")
    else:
        print("amounts are not in valid range")        