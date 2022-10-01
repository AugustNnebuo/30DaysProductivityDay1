#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ROCK PAPER SCISSORS

import random  #import the random module
print("Welcome to the Rock-Paper-Scissors Game By Sommiee! Enjoyyy...")
print()
def play():
    """This is a Programmed version of the game Rock-Paper-Scissors. in this game, rock beats 
    scissors, scissors beats paper and paper beats rock. ie r>s,s>p and p>r. if both players 
    get the same thing, then its a tie."""
    condition=False
    user=input("What is your choice? r for rock, s for scissors and p for paper.")
    computer= random.choice(['r','p','s'])
    
    condition = is_win(user,computer)
    
    if user==computer:        #
        #the if function returns tie in a situation both users play the same thing
        return "tie" 
    elif condition:
        return "Yaayy! You won!"
    else:
        #the else function returns you lost in a situation the player doesn't win
        return "You lost"
        
    
def is_win(player, opponent):
    #return true if player wins
    #(r>s,s>p and p>r)
    if (player=="r" and opponent == "s") or (player=="s" and opponent == "p") or (player=="p" and opponent =="r"):
        return True
    
    else:    # the else clause is initiated for a rare case when the function is_win is not true
        False
    
play()


# In[ ]:




