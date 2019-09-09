guess=5
while guess != 8:
    temp=input("erroe,please inpute again:")
    guess = int (temp)
    if guess == 8:
        print("yes")
    else:
        if guess>8:
             print ("more")
        else:
         print("less")
         
         
ps:pay attention on expected an indented block
