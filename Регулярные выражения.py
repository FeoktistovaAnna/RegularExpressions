import re
''' Функция search(pattern, string, flags=0) ищет первое совпадение в строке с 
 регулярным выражением (РВ) и возвращает специальный объект
 соответствия (тип Match) или None 
 pattern - шаблон РВ
 string - строка, где ищем
 flags=0 - необязательный аргумент, один или несколько флагов  '''

from re import search
m1 = search('super', 'superstition')
m2 = search('super', 'insuperable_super')
m3 = search('super', 'without')

#print(m1, m2, m3, sep='\n')

m1 = search('\d+', 'foo123bar')
m2 = search('[a-z]+', '123foo456')
m3 = search('\d+', 'foo.bar')

#print(m1, m2, m3, sep='\n')

''' Функция match(pattern, string, flags=0) возвращает
объект Match если начало строки соответствует РВ '''

from re import match
m1 = match('super', 'superstition')
m2 = match('super', 'insuperable_super')
#print(m1, m2, sep='\n')

''' Функция fullmatch(pattern, string, flags=0) возвращает 
 объект Match, если вся строка соответсвует РВ. Если
 РВ добавить обозначение начала и конца строки ^$, то 
 функция search будет вести себя как fullmatch'''

from re import fullmatch

phone_pattern = '\d{3}-\d{3}-\d{4}'

m1 = fullmatch(phone_pattern, '777-789-1234')
m2 = fullmatch(phone_pattern, '77-79-56')
m3 = fullmatch(phone_pattern, '1111-55-554')
m4 = fullmatch(phone_pattern, 'aaaa-aaa-aaa')

#print(m1, m2, m3, m4, sep='\n')

''' Объект Match сразу приводятся к типу bool '''

#if m1:
#    print('yes')

#if m2:
#    print('yes')
#else:
#    print('no')

''' Метод group() возвращает одну или несколько подгрупп
 совпадения. Если метод вызывается без аргументов, то
 возвращается вся строка совпавшая с РВ. Можно указать
 и несколько групп, тогда вернется кортеж. Вызов без аргументов
 равнозначен вызову с 0. Если передать индекс (отсчет идет 
 с 1, не с 0!) несуществующей 
 группы, то будет возбуждено исключение IndexError
 '''

from re import search

m = search('(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m.group())
#print(m.group(0))
#print(m.group(1))
#print(m.group(2))
#print(m.group(3))
#print(m.group(1, 2, 3))
#print(m.group(1, 2, 3, 3, 3, 2, 2, 1))

# Можно использовать название группы в качестве аргумента
from re import search

m = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
#print(m.group())
#print(m.group('w1'))
#print(m.group('w2'))
#print(m.group('w3'))
#print(m.group('w1', 'w2', 'w3', 'w2', 'w3'))

# Если какая-то группа шаблона не участвовала в сопоставленииб
# то возвращается None

from re import search

m = search('(\w+),(\w+),(\w+)?', 'foo,bar,')
#print(m.group(3))
#print(m.group(1, 2, 3))

''' Метод groups(default=None) возвращает кортеж, содержащий все 
 захваченные группы. Группы, которые не смогли захватить 
 какой-либо результат, будут иметь значение default'''
from re import search

m = search('(\w+),(\w+),(\w+)?', 'foo,bar,')
#print(m.groups())
#print(m.groups(-1))
#print(m.groups(default='Some_value'))

''' Метод groupdict(default=None) возвращает словарь, содержащий 
 все захваченные именованные группы. Если именованных 
 групп нет, то возвращает пустой словарь'''

from re import search

m = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)?', 'foo,bar,')
#print(m.groupdict())
#print(m.groupdict('Нет данных'))
#m = search('(\w+),(\w+),(\w+)?', 'foo,bar,')
#print(m.groupdict())

''' Методы start() и end() возвращают индексы начала и 
конца подстроки, которая совпала с РВ '''
#print(m)
#print(m.start())
#print(m.end())

''' В методы можно передать номер или названия группы. 
 Тогда методы вернут индексы начала и конца подстроки,
 совпадающей с нужной группой'''

text = 'foo123bar456baz'
m = search('(\d+)\D+(?P<num>\d+)', text)
#print(m)
#print(m.group(), m.start(), m.end())
#print(m.group(1), m.start(1), m.end(1))
#print(m.group('num'), m.start('num'), m.end('num'))

''' Если группа не участвует в сопоставлении, то оба 
 метода вернут -1'''

''' Метод span() возвращает кортеж из индексов начала и конца 
 подстроки, соответсвующей РВю Также в него можно передать 
 номер или название группы, тогда
 он вернёт индексы только для группы'''

print(m)
print(m.group(0), m.span(0))
print(m.group(1), m.span(1))
print(m.group(2), m.span(2))