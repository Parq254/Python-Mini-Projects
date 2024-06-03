print('Quiz Game')


playing = input('Do you want to play? ')

if playing != 'yes':
    print("We'll play another time")
    quit()

print("Okay Let's play :)")
score = 0

answer = input('What does CPU stand for? ')
if answer == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('Incorrect try again!')

answer = input('What does PSU stand for? ')
if answer == 'power supply unit':
    print('correct!')
    score += 1
else:
    print('Incorrect try again!')

answer = input('What does GPU stand for? ')
if answer == 'graphic processing unit':
    print('correct!')
    score += 1
else:
    print('Incorrect try again!')

answer = input('What does RAM stand for? ')
if answer == 'random access memory':
    print('correct!')
    score += 1
else:
    print('Incorrect try again!')

answer = input('What does ROM stand for? ')
if answer == 'read only memory':
    print('correct!')
    score += 1
else:
    print('Incorrect try again!')

print('You got ' + str(score) + ' questions Correct!')
print('You got ' + str((score / 4) * 100) + '%')
