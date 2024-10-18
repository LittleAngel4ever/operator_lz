'''
Определить простое ли число.
'''

# открываем файлы
input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()
n = int(data[0])

for i in range(2, 25000): # задаем i  из списка

    if n%i == 0 and i != n: # задаем условие для выполнения задачи
        output.write(str('N')) # выводим полченный ответ
        break # завершаем цикл, если условие выполнилось
    
    elif i == n: #если предыдущее условие не выполнилось задаем условие, при котором i равно заданному числу
        output.write(str('Y')) # выводим полченный ответ

if n == 1: # условие, если заданное число равно 1
    output.write(str('N')) # выводим полченный ответ 

# закрываем файлы
input_data.close()
output.close()