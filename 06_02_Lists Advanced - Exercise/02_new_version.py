version = input().split(".")
version = [int(v) for v in version]

version[2] += 1

if version[2] > 9:
    version[2] = 0
    version[1] += 1
    if version[1] > 9:
        version[1] = 0
        version[0] += 1

print(".".join(str(v) for v in version))