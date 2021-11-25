import sys
from collections import Counter

print(dict(sorted(Counter([len(input) for input in sys.stdin.read().split()]).items())))