n = [1,2,3,5,3,6,7,2,7,2,2,4,1,2,4,6,6,7]
m = [6,3,1,3,576,2,23,43,5,6,7,2,2,1]

fre_map = {}
for i in n:
    if i in fre_map:
        fre_map[i] += 1
    else:
        fre_map[i] = 1
for i in m:
    if i in fre_map:
        print(i,fre_map[i])
    else:
        print(i,0)