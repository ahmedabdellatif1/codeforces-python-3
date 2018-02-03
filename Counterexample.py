
l, r = [int(x) for x in input().split()]


if (l % 2 != 0):
    l += 1
if (abs(l - r)) < 2:
    print('-1')
else:
    print(str(l) + " " + str(l + 1) + " " + str(l + 2))