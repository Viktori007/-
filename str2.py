#Егорова Виктория 21Ис
#Задание 2
#. Задача «Первое и последнее вхождения». Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, ничего не выводите.
a=input()
s=str.count(a,"f")
if s==1:
  print(a.find("f"))
elif s>1 :
  print(a.find("f"), a.rfind("f"))
else:
  print("")
