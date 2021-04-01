def close10(x, y):

    if abs(10 - x > 10 - y):
        return x

    elif (10 - x < 10 - y):
        return y

    else:
        return 0

print(close10(50, 100))

