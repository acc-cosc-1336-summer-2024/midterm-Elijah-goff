#write functions here, don't add input('') statements here!
def test_config():
    return True

import random
print('Bot: Can you guess the number I am thinking of?')
SecretNumber = random.randint(1,5)
attempts = 0

while True:
    Guess =int(input('Guess a number:'))
    attempts +=1
    if Guess == SecretNumber:
        print(f'Congratulations! You FINALLY guessed the number in {attempts} attempts. Try Again!')
        break
    elif Guess < SecretNumber:
        print ('Bot: Getting warmer! Guess higher!')
    else:
        print('Bot:So close! Guess lower!')
   
