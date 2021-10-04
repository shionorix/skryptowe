import sys

def prime_check(num):
    try:
        num = int(num)
    except:
        return
    for i in range(2, (num//2)+1):
        if num % i == 0:
            break
    else:
        print(num)

#print(sys.argv)       
for i in range(1, len(sys.argv)):
    prime_check(sys.argv[i])