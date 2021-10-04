class Exception:
    print("Value cannot be converted to number")

def sum(arg1, arg2):
    if isinstance(arg1, str):
        arg1 = convert(arg1)
    if isinstance(arg2, str):
        arg2 = convert(arg2)
    return arg1 + arg2

def convert(arg):
    try:
        float(arg)
    except ValueError:   
        raise Exception()
    else:
        arg = float(arg)
    return arg

suma = sum(2.1, 3)

#print(f'__name__ = {__name__}')

if __name__ == '__main__':
    print(f'suma = {suma}')

