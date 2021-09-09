from past.builtins import raw_input

number = abs(float(raw_input("Calculate square root of? ")))
guess = abs(float(raw_input("Initial guess? ")))

# xn+1 = ( xn + S / xn ) / 2

epsilon = 0.001

while True:
    # difference = (guess **2) - number
    difference = guess ** 2 - number

    # Print both
    print('%a : %a' % (round(guess, 4), round(difference, 4)))

    # Gonna repeat until end of the line
    if abs(difference) <= epsilon:
        break

    # if it doesnt satisfy the precedent case, changes 'guess' accordingly
    guess = (guess + number / guess) / 2.0
