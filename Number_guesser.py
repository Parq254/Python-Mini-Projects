import random

top_of_range = input('Enter a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please Enter a number larger than 0 on next entry')
        quit()
else:
    print('Please Type a number next time')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time')
        continue

    if user_guess == random_number:
        print('You got it correct')
        break
    else:
        if user_guess > random_number:
            print('You guessed above number')
        else:
            print('You were below number')


print('You got in', guesses, 'guesses')
