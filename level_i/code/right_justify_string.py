familiar = 'rabbit'
width = len(familiar)
spaces = ''
for i in range(10 - width):
    spaces = spaces + ' '
result = '<' + spaces + familiar + '>'
print(result)
