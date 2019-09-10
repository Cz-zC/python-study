score = int(input('input score:'))
if 100>=score>=90:
    print('A')
if 90>score>=80:
    print('B')
if 80>score>=60:
    print('C')
if 60>score>=0:
    print('D')
if score<0 or score>100:
    print('error')
