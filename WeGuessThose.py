print("this be the game of guessing the number, guess the number or become plumber")
print("pick a number between 50000/10000 and 1000000/1000000")
number=3
chance=0
while chance<5:
    guess=int(input("Guess that number plumber"))
    if (guess==number):
         print("Damn u smartyBOI")
    elif(guess<number):
        print("too low plumber")
    else:
        print("too high")
    chance=chance+1

    
if  (chances>5):
    print("u just got coconut-mauled")
