def number_pattern(n):
    if type(n) != int:
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    return ' '.join(str(i) for i in range(1, n+1))

print(number_pattern(4))
print(number_pattern(-1))