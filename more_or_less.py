import random
attempts=0

# Asking the user to input a number between 1 and 3.
level=int(input('Choose the difficulty(1, 2, 3): '))

if level == 1:
   number = random.randint(0,10)
   a = int(input('Enter a number between 0 and 10 : '))
elif level == 2:
    number = random.randint(0,100)
    # Asking the user to input a number between 0 and 100.
    a = int(input('Enter a number between 0 and 100 : '))
else :
    number = random.randint(0,1000)
    a = int(input('Entrez un nombre entre 0 et 1000 : '))

# Checking if the number is not equal to the user input.
while number != a: 
    if a<number:
        print(f'The number is greater than {a}')
    else:
        print(f'The number is smaller than {a}')

    a = int(input('Enter a number : '))
    attempts += 1

# Printing the message"
print(f'Congratulations, you found it in  {attempts} tries')
