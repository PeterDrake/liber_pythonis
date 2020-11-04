familiar = 'rabbit'
width = len(familiar)
result = '<'
for i in range(10 - width):
    result = result + ' '
result = result + familiar + '>'
print(result)
