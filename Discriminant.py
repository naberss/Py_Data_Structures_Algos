def discriminant(a, b, c):
    result = ((b ** 2) - (4 * a * c))

    if (result > 0):
        print('two solutions.Discriminant value is' + str(result))
    elif (result == 0):
        print('one solution.Discriminant value is' + str(result))
    else:
        print('No real Solution.Discriminant value is' + str(result))


a = input('type a: ')
b = input('type b: ')
c = input('type c: ')
discriminant(int(a), int(b), int(c))
