import time
a=input("set your username")
b=input("set your password")
while True:
    input1=input("enter your username")
    if input1==a:
        break
    print("not correct")
while True:
    input1=input("enter your password")
    if input1==b:
        break
    print("not correct")
print("access authorized")
input()
#time.sleep(10)

