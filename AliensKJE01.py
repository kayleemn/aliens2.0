# aliens.py with else
#intered in the math
#INIT variable
l = int(0) #l =  aliens that have landed
w = int(0) #w = Weeks that have passed
week = str("week")
lc = False
wc = False


# Intro
print ("Today we will be calculating the amount of aliens that has a population corresponding to the amount of weeks.")
print("How many aliens have landed on Earth?")

#tests

while lc == False:
    try:
        l = int(input("please insert an amount of aliens that have landed on Earth"))
        if l > 0:
             #Please insert a number that is greater than 0 to see the amount of aliens that landed on earth.
            print("How many weeks have passed?")
            lc = True
            #This checks to see if the user typed a number greater than 0.
        else:
            print(" Try again, a positive number")
    except ValueError:
        print("only a number is excepted.")
         # You only can escape the While loop if you have typed a positive number.

while wc == False:
    try:
        w = int(input("please insert the amount of weeks that has passed"))
          # insert the amount of weeks that passed.
        if w > 0:
            wc = True
             #This checks to see if you have typed a positive number.
        else:
            print(" Try again, put in a number")
            # Not escaping the loop.
                 # Stays in loop unitl the user types the apporiate number.
    except ValueError:
          print("wrong number.")
#math
for i in range (w):
    if (i == 1):
        week = "weeks"
        print("After", i + 1, week, "there will be", l*2**(i+1), " aliens on Earth.")
         #You only get this line if you escape the loop.
        

