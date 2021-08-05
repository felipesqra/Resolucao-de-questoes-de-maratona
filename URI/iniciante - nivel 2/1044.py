input = input().split()
a = float(input[0])
b = float(input[1])

def fun(a, b):
    result = ''

    if (a == 0 or b == 0):
        if (a != b):
            result = 'Nao sao Multiplos'
        else:
            result = 'Sao Multiplos'
    elif (a < b):
        if (b%a == 0):
            result = 'Sao Multiplos'
        else:
            result = 'Nao sao Multiplos'
    else:
        if (a%b == 0):
            result = 'Sao Multiplos'
        else:
            result = 'Nao sao Multiplos'

    return result

print(fun(a,b))