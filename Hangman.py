#Hangman Game nicely explained in the given link: https://inventwithpython.com/chapter9.html


import random

HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']
with open("words.txt","r") as f:
    content=f.read()
words=content.split(" ")
alphabet_set="abcdefghijklmnopqrstuvwxyz"
alphabet=alphabet_set
print("Lets Play H A N G M A N")


player=""

def wordtoguess():
    guess_word=random.choice(words).lower()
    return guess_word

def guess(alphabet):
    while True:
        guess=input("Guess the character ").lower()
        if guess not in alphabet:
            print("Letter is already done guess different")
            guess=input("Guess the character ").lower()
            return guess
        elif(len(guess)!=1):
            print("Guess only single letter")
            guess=input("Guess the character ").lower()
            return guess
        else:
            return guess

def guesscheck(wrong,alphabet,correctletter,partblank):
    
    if wrong < len(HANGMANPICS):
        print(HANGMANPICS[wrong])
    print("Letters to guess from: "+alphabet)
    for i in range(len(guess_word)):
        if guess_word[i] in correctletter:
            partblank=partblank[:i]+guess_word[i]+partblank[i+1:]        
    return partblank    

guess_word=wordtoguess()
partblank="_"*len(guess_word)
print("word length to guess "+partblank+"length of word: ",len(partblank))
wrong = 0
again1=False
correctletter=""    

def playagain():

     playagain=input("Do you want to play again. Type Y/N: ").lower()
     if playagain=='y':
        global guess_word,partblank,wrong,correctletter,alphabet
        guess_word=wordtoguess() 
        partblank="_"*len(guess_word)
        print("word length to guess "+partblank+"length of word: ",len(partblank))  
        wrong = 0
        correctletter=""
        alphabet=alphabet_set
        partblank=guesscheck(wrong,alphabet,correctletter,partblank)
        
     else:
         return 0
        
         



while True:
    
    if wrong == len(HANGMANPICS):
        print("You ran out of attempts try next time")
        print("Correct word was: "+guess_word)
        choice=playagain()
        if choice ==0:
            print("Thanks for Playing Hangman")
            break
        
    elif(partblank==guess_word):
        print("You won!!")
        choice=playagain()
        if choice ==0:
            print("Thanks for Playing Hangman")
            break

    else:
        player=guess(alphabet)
        if player in guess_word:
            correctletter=correctletter+player
        else:
            wrong+=1
            print("You guessed a wrong word")
        alphabet=alphabet.replace(player,"")
        partblank=guesscheck(wrong,alphabet,correctletter,partblank)
        print("word guessed till now: ")         
        for i in range(len(partblank)):
            print(partblank[i],end=" ")
        print("\n You have",len(HANGMANPICS)-wrong," chances left")
            

        
        
