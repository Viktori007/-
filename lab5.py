'''
Егорова Виктория 21Ис-21 14.11.2022
Задание 5. 
Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер числа, отличного от остальных. 
'''
a = int(input())
b = int(input())
c = int(input())
if a==b:
    print(3)
elif b==c:
    print(1)
else:
    print(2)

