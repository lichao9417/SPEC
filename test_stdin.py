import sys

data = ""
for line in sys.stdin:
    if line != "\n":#停止条件
        data += line
    else:
        break
print(data)