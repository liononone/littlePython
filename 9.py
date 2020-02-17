import re
m=re.search(r'[1-9]\d{5}','bjfu 122333   sdff 355543')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)

print(m.group(0))