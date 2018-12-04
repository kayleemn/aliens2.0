# aliens.py with else
#entered in the math
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
             #insert a number that is greater than 0 to see the amount of aliens that landed on earth.
            print("How many weeks have passed?")
            lc = True
            #This checks to see if the user typed a number greater than 0.
        else:
            print(" Try again, a positive number")
    except ValueError:
        print("only a number is excepted.")
         # You only can escape the While loop if you ave typed a positive number.


