n = [1,2,3,5,3,6,7,2,7,2,2,4,1,2,4,6,6,7]
m = [6,3,1,3,576,2,23,43,5,6,7,2,2,1]


hash_map = [0] * 11
for i in n:
    
    hash_map[i] += 1
for i in m:
    if i<0 or i>10:
        print(0)
    else:
        print(hash_map[i], i )