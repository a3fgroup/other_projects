# t1 = (1, 2, 3)
# l1 = [1, 2, 3]

# Упаковка кортежа:
# t1 = 1, 2, 3

# t1 = tuple((1, 2, 3))
# t1 = ()
# t1 = (1, )

# t1 = (1, 2, 3)
#
# print(t1.__sizeof__())
# print(l1.__sizeof__())

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
#
# print(t3)
# print(t3.count('l'))
# print(t3.index('o'))
#
#
# for i in t3:
#     if i == '  ':
#         continue
#     print(f'"{i}"', end=' ')


# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
#
# t1[4][0] = 'new'
# t1[4].append('hello')
# print(t1, id(t1))


# Распаковка кортежа:
# t1 = (1, 2, 3)
# x = t1[0]
# y = t1[1]
# z = t1[2]
# Записать можно так:
# x, y, z = t1

#print(x, y, z)


# x = 1
# y = 2
#
# print(x, y)
# x, y = y, x
# print(x, y)
