temp = input("inpute a number:")
guess = int (temp)
secret=8
if guess == secret:
    print("yes")
else:
    if guess>secret:
         print ("more")
    else:
         print("less")
  
