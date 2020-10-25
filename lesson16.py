l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

names = ['Ivanov', 'Petrov', 'Sidorov']


# print(l[4][0])

# print(l[0:3])

l[2] = 'world'
# print(l)

# l[:2] = [10, 15]
# print(l)

l.append('new')
l.extend([5, 7])
l2 = ['hi', 19]
l += l2
l.insert(1, 'test')
# l.remove('world')
# el = l.pop(1)
# print(l, l.count('test'))
# l.sort()
# l3 = ['hello', 'hi', 'David', 'world', 'test']
# l3.sort()
# l = sorted(l3)
# print(l, l.count('test'), l3, sep='\n')

# l.reverse()
# l.copy()
# l.clear()
print(l)
