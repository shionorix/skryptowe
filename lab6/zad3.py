import sys
import functools

print(len(list(filter(lambda x: int(x) % 2 == 0, functools.reduce(lambda a, b: a + b, list(open(file, 'r').read().replace('\n', ' ').split() for file in sys.argv[1:]))))))