from operator import index

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютеры']

first_result = (len(x)-len(y) for x, y  in zip(first, second) if len(x) != len(y))
i = 0
j = 0

# second_result = (print(first[i], "-", second[j]) for i in range(0, len(first)) for j in range(0, len(second)) if i == j)
#second_result = (len(first[i])<len(second[j]) for i in range(0, len(first)) for j in range(0, len(second)) if i == j)
second_result = (len(x)<len(second[j]) for x in first for j in range(0, len(second)) if first.index(x) == j)
print(list(first_result))
print(list(second_result))


