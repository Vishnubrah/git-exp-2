
a=[2,3,5,8]
squared=[x**2 for x in a]
print(squared)

result=[i for i in range(5,31) if i%5==0]
print(result)


word=['python','java','c','c++','json']
print([i for i in word if i.startswith('j')])

a=[21,32,436,5675,8]
a.append([3,45,34,3464,54])
print(a)
