import re
import sys

def word_or_number(string):
    return {
        'words': re.findall(r'[a-zA-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', string),
        'numbers': re.findall(r'[0-9]+', string)
    }

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline()
        if line:
            result = word_or_number(line)
            if result['words']:
                print(f"Wyraz: {', '.join(result['words'])}")
            if result['numbers']:
                print(f"Liczba: {', '.join(result['numbers'])}")
        else:                          
            break