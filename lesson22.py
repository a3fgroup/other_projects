# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = set('hello')
# s3 = {i for i in range(1, 11)}
# s4 = set()
#
#
# print(s)
# print(s2)
# print(s3)
# print(type(s4))
#
#
# nums = [1, 2, 3, 3, 1, 2, 4, 5]
# nums2 = list(set(nums))
# print(nums2)

#
# a = set('abracadabra')
# b = set('alacazam')
#
# c = a - b   # Вычитание - убираем из а все буквы, которые есть в b
# d = a | b   # Объединение - буквы в а или в b
# e = a & b   # Пересечение - буквы и в а и в b
# f = a ^ b   # Множество из элементов - буквы в а или b, но не в обоих
#
# print(a, b, c, d, e, f, sep='\n')


# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s.copy()
#
# print(s, id(s))
# print(s, id(s2))
# s.add('melon')
# print(s)
# s.remove('orange')
# print(s)
#
# s.discard('orange')
# print(s)
#
# s.pop()
# print(s)

# s.clear()
# print(s)


a = frozenset('hello')
a.add('apple')
print(a)