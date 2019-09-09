  
import random

secret = random.randint(1,10)
temp = input("just guess:")
guess=int(temp)
while guess!=secret:
        temp=input("error,please input again:")
        guess=int(temp)
        if guess == secret:
            print("yes")
        else:
            if guess>secret:
                print("more")
            else:
                print("less")
print("game over")
