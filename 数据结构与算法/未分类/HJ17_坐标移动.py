s = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
s_list = s.split(';')
print(s_list)
# 判断坐标是否合格
r_list = []
for one in s_list:
    if one:
        if one.startswith("A") or \
                one.startswith("W") or \
                one.startswith("S") or \
                one.startswith('D'):
            if one[1:].isdigit() and 0 < len(one[1:]) < 3:
                r_list.append(one)

print(r_list)

a = [0, 0]

for i in r_list:
    if i.startswith("A"):
        n = int(i[1:])
        a[0] -= n
    elif i.startswith("D"):
        n = int(i[1:])
        a[0] += n
    elif i.startswith("W"):
        n = int(i[1:])
        a[1] += n
    elif i.startswith("S"):
        n = int(i[1:])
        a[1] -= n

print(a)
print(','.join([str(i) for i in a]))
print(a[0], ",", a[1])
