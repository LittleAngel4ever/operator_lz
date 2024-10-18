'''
Вывести ряд Фибоначчи до определенного элемента
'''

print("Введите число n: ")
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
'''  
задания чисел фибоначчи до определенного 
чередование 1 и 2 переменных чтобы их перезаписать 
перезаписью являеться сумма 2 переменных 
'''
for i in range(2, n):     
        
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

print("Ряд чисел Фибоначчи: ")
print(result)