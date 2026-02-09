g=[
    [0,1,0,1],
    [1,0,0,1],
    [0,0,0,1],
    [1,1,1,0]
]

g2={
    'a':['b','d'],
    'b':['a','d'],
    'c':['d'],
    'd':['a','b','c']
    }
for i in g2:
    print(i,g2[i])

#joining
v=['a','b','c','d']
print('  ','  '.join(v))
for i,j in enumerate(g):
    print(v[i],j)