# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1

# print('Hello', 'world', sep='!', end=' ')
# print('Hello2', 'world2')


# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(f'"{l}"', end=' ')


for i in 'Helloworld':
    if i == ' ':
        break
    print(i, end=' ')
else:
    print('\nNo spaces')