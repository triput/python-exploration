import random

money = 100

#Write your game of chance functions here
# Game of Coin Flip
def coin_flip(flip, bet):
    face = ""
    
    # determine the results of the flip
    num = random.randint(1,2)
    #print(num)
    
    if num == 1:
        face = "heads"
    else:
        face = "tails"
        
    #print(face)    
    if flip == face:
        print("You won! You bet on " + flip + " and the result was " + face)
        print("Your winnings: " + str(bet))
        return bet
    else:
        print("You lost. You bet on " + flip + " and the result was " + face)
        print("Your loss: " + str(-bet))
        return -bet
 
# Game of Cho-Han

def cho_han(guess,bet):
     
    # Roll the dice and get a total
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    die_total = die_one + die_two
     
    # Odd or even?
    if die_total % 2 == 0:
        result = "even"
    else:
        result = "odd"
    
    # Win or lose?
    if result == guess:
        print("Congratulations! You bet the number would be " + guess + ". You rolled a " + str(die_one) + " and a " + str(die_two) + " for a total of " + str(die_total) + ", which is an " + result + " number.")
        print("Your winnings: " + str(bet))
        return bet     
    else:
        print("Sorry, you lost.  You bet the number would be " + guess + ". You rolled a " + str(die_one) + " and a " + str(die_two) + " for a total of " + str(die_total) + ", which is an " + result + " number.")   
        print("Your loss: " + str(-bet))
        return -bet   


# Game of Card Draw
#def card_draw(bet):



















#Call your game of chance functions here
# Test for coin_flip

print ("Welcome to Coin Flip. You have: $" + str(money))

for i in range(10):
    money += coin_flip("tails", 10)
    print(money)
    i = i+1
    
print("Your total at the end of Coin Flip is: $" + str(money))

# Test for cho-han
print ("Welcome to Cho-Han. You have: $" + str(money))

for i in range(10):
    money += cho_han("odd", 10)
    print(money)
    i = i+1
    
print("Your total at the end of Cho-Han is: $" + str(money))