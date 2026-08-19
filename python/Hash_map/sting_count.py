s="sdfiyuouihaodhfnouqqef"
q=["d","a","t","f","w","m","o"]

hash_list = [0] * 27

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1
for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(ch ,hash_list[index])