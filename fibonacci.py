'''
Вывести ряд Фибоначчи до определенного элемента
'''

n = input()
n = int(n)
fib1 = 1
fib2 = 1
fib1 = str(fib1)
fib2 = str(fib2)
result = "0 "
result += fib1 + " " + fib2
fib1 = int(fib1)
fib2 = int(fib2)
for i in range(2, n): # задаем i из списка

    if i%2 == 1: 
        fib1 = fib2 + fib1
        fib1 = str(fib1)
        result += " " + fib1
        fib1 = int(fib1)
    elif i%2 == 0:
        fib2 = fib1 + fib2
        fib2 = str(fib2)
        result += " " + fib2
        fib2 = int(fib2)

print(result)