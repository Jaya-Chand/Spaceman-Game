# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:29:39 2020

@author: Minerva
"""

##SPACEMAN LEVEL 1 GAME
##Level 1 game consists of:
##workbank
##ASCII art

from random import randint


spaceman_ASCII=["FAIL1","FAIL2","FAIL3","FAIL4","FAIL5","FAIL6","FAIL7"]


##Choosing words with an Astrophysics theme
wordbank=["spectroscopy","stellar","martian","asteroid","rover","crater","supernova","hydrogen","core","comet"]

##Picks random word from list and splits into array with each element as a character 
spaceman_word=list(wordbank[randint(0,len(wordbank))])

print(spaceman_word)

print("WELCOME TO A SPACEMAN (a politically correct version of Hangman)!")

attempt=["_ "]*len(spaceman_word)
Fails=0
guessed_letters=[]

while attempt!=spaceman_word and Fails<7:
    success=False
    guess=input("\nPlease enter your letter guess: ")
    ###Looping method inefficient but starting off
    for i in range(0,len(spaceman_word)):
        if guess==spaceman_word[i]:
            print("\nWell done!" , guess, "appears in the word")
            attempt[i]=guess
            print(attempt)
            success=True
            guessed_letters.append(guess)
    if success==False:
        Fails+=1
        print(Fails)
        print("\nBad luck", guess,"does not appear in the word")
        print(spaceman_ASCII[Fails])
        
if Fails>7:
    print(spaceman_ASCII[Fails])
    print("GAME OVER! u suck")
    
print("Congratulations! You guessed the word",spaceman_word)       
            