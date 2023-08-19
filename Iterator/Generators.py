def square_number():
    i = 1
    while True:
        yield i * i
        i += 1


for n in square_number():
    if n > 25:
        break
    print(n)
a = square_number()
