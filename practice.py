import random 

def number_guess():
  print('-' * 24)
  print("Guess The Number")
  print('-' * 24)
  
  random_number = random.randint(1,10)
  total_tries = 0
  guess = 0

  while guess != random_number and total_tries < 5:
    guess = int(input("Enter a number between 1 and 10 "))
    if guess < random_number:
      print("Too low")
      total_tries += 1
    else: 
      print("Too high")
      total_tries += 1
  
  if guess == random_number:
    print("You won! It took you ",total_tries, "tries to guess the correct number")
  else:
    print("You lost, the correct number was ", random_number)
  
 
number_guess()