import re
import sys

args = sys.argv[1:]

plik = open(args[0],'r')
content = plik.read()
comments = re.findall(r"/\*[a-zA-Z0-9\s\n\,\.]*\*/", content)
oneLines = re.findall(r"//[a-zA-Z0-9\s\n\,\.]*\n", content)
functions = re.findall(r"\b(?!\bfor\b|\bwhile\b)\b([a-zA-Z0-9]*)\s*\([^()]*\)\s*{", content)

if '--wrap' in args:
    for i in range(len(comments)):
        comments[i] = comments[i].replace('/*\n', '')
        comments[i] = comments[i].replace('\n*/', '')
        split = comments[i].split("\n")
        print(f'// {" ".join(split)}')
else:
    print("\n".join(comments))

print("".join(oneLines))
print(f'Wykryte definicje funkcji: {" ".join(functions)}')
