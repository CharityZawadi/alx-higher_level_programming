#!/usr/bin/python3

def magic_calculation(a, b):
    add, sub = 0, ('add', 'sub')

    if a < b:
        c = a + b
        for i in range(4, 6):
            c = locals()[sub[0]](c, i)
        return c
    else:
        return locals()[sub[1]](a, b)

# Example usage
if __name__ == "__main__":
    a_value = 5
    b_value = 3
    result = magic_calculation(a_value, b_value)
    print(result)

