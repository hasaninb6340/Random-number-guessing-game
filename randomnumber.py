import random
level=-1
while ((level>4)or(level<0)):
    level=int(input("...........................choose level 1, 2 or 3............................................ "))
    if((level>4)or(level<0)):
        print(".................................please enter in range 1 to 3..............................................")
if(level==1):
    chances=8
    score=80
    levelbonous=0
elif(level==2):
    chances=4
    score=40
    levelbonous=10
elif(level==3):
    chances=2
    score=30
    levelbonous=30    
highnumbers=-1
lownumber=0
while highnumbers<lownumber:
    highnumbers=int(input("..............................Enter largest number ......  "))
    lownumber=int(input("................................Enter smallest number ....... "))
    if(lownumber>highnumbers):
        print("...............Enter correct range ..........................")
number=random.randint(lownumber,highnumbers)
while(chances>0):
    guess=int(input(".......................Guess number.......................... "))
    if(guess==number):
        print("..............................You guessed it..................................")
        print(".....................you win...........................................")
        print("Your score is..........................................................")
        print((score*level)+levelbonous)
        chances=-1
    else:
        if(guess>number):
            print(".........................you entered largest number.................................................")
        else:
            print("........................you entered smallest number.....................................................") 
    score=score-10    
    chances=chances-1
if(score==0):
    print("........................You failed try again. your score is zero..........................................")

4