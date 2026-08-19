numbers = [1, 2, 3, 4, 5]

def square(num):
    return num * num

result = map(square, numbers)

print(list(result))