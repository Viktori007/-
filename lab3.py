'''
Егорова Виктория 21Ис-21 14.11.2022
Задание 3. 
Дано целое число. Если оно является положительным, то вычесть из него 8; если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10. Вывести полученное число.
'''
a = int(input())
if a > 0:
    a=a-8
else:
    if a<0:
      a=a+6
    else:
        a=10
print(a)

