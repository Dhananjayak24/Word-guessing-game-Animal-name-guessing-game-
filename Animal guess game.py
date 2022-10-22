#random module is imported to automatically guess random animal from tuple
import random

animal_list=( "Lion,  Tiger, Goat, Horse, Donkey, Dog, Cat, Pig, Panther, Leopard, Cheetah, Cow, Walrus, Otter, Giraffe, Sheep, Rabbit, Monkey, ")
#tuple is split to use next for random code
animal_list=animal_list.split()
#taking player details
name = input("Please enter your name : ")
print("Hello "+ name+", welcome to animal name guessing game")
response = input("Are you ready? (Y/N) : ")

if response.lower() == "y":
    print("yah! Lets begin the game")
    print("Note : You have total 5 attempts to guess letters."
          "You can also consider hint")
elif response.lower() == "n":
    print("Okay, Sorry to see you leaving... ")
    exit()
else:
    print("Please enter Y/N")
    response = input("Are you ready? (Y/N) : ")
#coding for automatic random guess
guessed_word=random.choice(animal_list)
guessed_word=str(guessed_word)
#length is used for hint and result calculation
length=len(guessed_word)
#-1 is used as it was counting the space next to word
length=(length-1)
#converted to str so as to use in last print statement
length1=str(length)

guess_count=1
#guessed correct letters are stored in list for final display with append
letter_storage=[]
guessed_word=guessed_word.lower().strip()
while guess_count<=int(length1):
    letter=input("please guess a letter : ")
#to assure player is entering a single letter only
    if len(letter)>1:
        print("Please enter single letter")
    else:
       if letter.lower() in guessed_word:
           print("yes")
           letter_storage.append(letter)
           guess_count += 1
       else:
           guess_count += 1
           response2=input("you guessed wrong. Need Hint(Y/N)")
           if response2.lower()== "y":
               hint = print("First letter: " + guessed_word[0] + ", last letter: " + guessed_word[-2] + ", lenght is " + length1)
           elif response2.lower()=="n":
               continue
           else:
               print("Please enter Y/N")
               continue
#the list is converted to dictionary and back to list to remove duplicates from list as dictionary can have only single keys
letter_storage1=list(dict.fromkeys(letter_storage))
result= ((int(len(letter_storage1))/int(length1))*100)
result=round(result,2)
result=str(result)
print(letter_storage1)
print("Hurray!!! you guessed :"+ str(letter_storage1)+ " letters right." "\n","Correct word is: "+ guessed_word +"\n","Your score is: "+ str(result)+ "%")

