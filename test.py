r = []
r.append([0,0])
r.append([0,1])
r.append([-1,-1])
r.append([-1,-1])
r.append(2)
r.append("00")

k=[[0for k in range(5)]for i in range(5)]

tree = [{}]
tree[0]["key"] = 50
i = 1
print("next" + str(i))

print(r)
print(r[4])
print(r[3][0])
print(r[5][1])
print(k)
print(tree[0])
print(tree[0]["key"])

tmp = [0,0]

print(tmp)

a = [0,1]
b = [0,1]

if a == b:
    print("a=B")
else:
    print("a!=B")
