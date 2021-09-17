# média, mediana, moda, variância e desvio padrão
import math

def read_Arq(path):
    mylist = list(open(path, 'r'))
    for rec in range(len(mylist)):
        mylist[rec] = float(mylist[rec])

    return mylist


def media(mylist):
    return sum(mylist) / len(mylist)


def mediana(mylist):
    middle = len(mylist) / 2
    if (middle % 2 != 0):
        return mylist[int(middle)]
    else:
        return (mylist[int(middle)] + mylist[int(middle - 1)]) / 2


def moda(mylist):
    max_counter = 0
    max_value = 0
    returnlist = {}
    for rec in mylist:
        actual_counter = mylist.count(rec)

        if actual_counter > max_counter:
            max_counter = actual_counter
            max_value = rec
        elif actual_counter == max_counter:
            returnlist[rec] = actual_counter
            returnlist[max_value] = max_counter

    for rec in returnlist.keys():
        if returnlist[rec] >= max_counter:
            return returnlist
        else:
            return max_value


def variance(my_list):
    dividend = 0
    divisor = len(my_list)
    arith_avg = media(my_list)
    for rec in range(divisor):
        dividend += ((my_list[rec] - arith_avg) ** 2)

    return dividend / divisor


def standardDeviation(var):
    return abs(math.sqrt(var))

mylist2 = [15, 12, 16, 10, 11]

print(standardDeviation(variance(mylist2)))
