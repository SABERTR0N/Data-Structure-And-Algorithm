d = {}

d['Name'] = 'Alice'
d['Age'] = '25'
print(d['Name'])
print(d.get('Age'))
print(d.get('x',1))

for key, val in d.items():
    print(key,val)

del d['Age']