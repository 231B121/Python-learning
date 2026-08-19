numbers = [10, 15, 20, 25, 30]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, numbers)

print(list(result))

#  map()     → sabhi items ko change/process karo
#  filter()  → kuch items ko select karo
#  reduce()  → sab items ko combine karke ONE result banao
#