guess = int(100/2)
low = 0
high = 100
answer = ''
correct = 'c'
too_low = 'l'
too_high = 'h'
ask_action = 'Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.'

print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number' + ' ' + str(guess) + '?')
    answer = input(ask_action)
    if answer == correct:
        print('Game over. Your secret number was:', guess)
        break
    if answer == too_low:
        low = guess
    elif answer == too_high:
        high = guess
    else:
        print('Sorry, I did not understand your input.')

    guess = int((low + high) / 2)
