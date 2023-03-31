a=2
print(type(a), 'a=', a)
b=3
print(type(b), 'b=', b)
c=a==b
print(type(c), 'c=', c)
P3="reshenie"
print(type(P3), 'P3=', P3)
print(P3+str(a-b))
l1=[a,b,c,P3]
print(type(l1), 'l1=', l1)
print(set(l1))
d= (1, 2, 3)
print(type(d), 'd=', d)
e=(4, 5, 6)
print(type(e), 'e=', e)
f=d+e
print(list(f))
g1={"string": 2}
print(g1)
g2={"string": "ddd"}
print(g2)
g3={3: "fff"}
print(g3)
nn1=None
g4={c: nn1}
print(g4)
f1=[1, 2, 3]
g5={c: f1}
print(g5)
g6={2.5: {1: 2}}
print(g6)
g7={"ss": "aa"}
print(g7)
g8={1: 2}
print(g8)
g9={d: e}
print(g9)

