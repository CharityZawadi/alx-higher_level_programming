def magic_calculation(a, b):
    if a < b:
        return a + b
    else:
        result = 0
        for i in range(4, 6):
            result = add(result, i)
        return result

def add(a, b):
    return a + b

# Test
a = 3
b = 2
print(magic_calculation(a, b))

