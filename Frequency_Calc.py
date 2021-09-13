#Frequency calculus

from past.builtins import raw_input

mylist = list(open("C:/Users/Lucas/Documents/Aprendendo/ML Mat/Exercicios-Cap01/arquivos/notas.txt", "r"))

for rec in range(len(mylist)):
    mylist[rec] = float(mylist[rec])

mylist.sort()
# print(mylist)

amplitude = max(mylist) - min(mylist)

interval = round(amplitude / abs(int(raw_input("digite a quantidade de classes: "))))
# print(interval)

n = 1
init = min(mylist)
mydic = {}
for rec in range(len(mylist)):
    if (mylist[rec] >= init) and (mylist[rec] < init + interval):
        mydic[mylist[rec]] = n
    else:
       n += 1
       init += interval
       mydic[mylist[rec]] = n

print(mydic)
