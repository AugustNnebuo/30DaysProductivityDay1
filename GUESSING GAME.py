#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. THE GUESSING GAME (COMPUTER)
#import random

import random   
#imports the random module
secretnumber=random.randint(1,20)   
#initialises the secret number to be a range from 1 to 19.
print("I am thinking of a number")      

for guessesTaken in range(1,7):            
# the for loop works for only guesses taken from the !st to ^th time. this is ton limit the number of guesses the player can make
    print("Take a guess.")
    guess=int(input("You can try only 7 times. "))     
    #the player can put in his guess which must be a number because of the int statement added
    
    #the if and elif statement gives the player guesses, as to whether his guess is higher or lower than the secretnumber.
    if guess<secretnumber:
        print("Your guess is too low")
    elif guess> secretnumber:
        print("Your guess is too high")
    else:
        break  # the for loop breaks if the condition is correct
    
if guess==secretnumber: 
    print("Goodjob! You guessed my number in " + str( guessesTaken ) + " guesses!")
else:
    print("Nope! the number i was thinking of was "+ str( secretnumber))


# In[ ]:




