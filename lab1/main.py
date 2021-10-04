class StringException(Exception):
    pass

class TypeException(Exception):
    pass

def sum(arg1, arg2):
    if isinstance(arg1, str):
        arg1 = convert(arg1)
    if isinstance(arg2, str):
        arg2 = convert(arg2)
    exc_flag = False
    try:
        arg1 + arg2
    except TypeError:
        exc_flag = True
    finally:
        if exc_flag == True:
            raise TypeException("Invalid data type")
        else:
            return arg1 + arg2

def convert(arg):
    exc_flag = False
    try:
        float(arg)
    except ValueError:   
        exc_flag = True
    finally:
        if exc_flag == True:
            raise StringException("String cannot be converted to number")
        else:
            arg = float(arg)
    return arg

#print(f'__name__ = {__name__}')

if __name__ == '__main__':
    print(f'suma = {sum(2.1, 3)}')

