#Milakshi - Create the project and added starter code

#Kisuri - Changed the range 10 to 100
#import random begininng the code
import random 
number = random.randint(1, 100) 
print("Guess a number between 1 and 100") 
guess = int(input()) 
if guess == number: 
print("You win!") 
else: 
print(f"Wrong! The number was {number}") 


#Apoorwa - Added while  loop
while True:
 # (paste existing code here)
 print("Play again? (y/n)")
 if input().lower() != 'y':
 break

#Sashini - added if condition
 if guess < number: 
    print("Too low!") 
elif guess > number: 
    print("Too high!") 

#Malki -third
while True:
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("You win!")
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    if input("Play again? (y/n): ").lower() != 'y':
        break
