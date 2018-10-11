s = input()
pos = s.find('h')
p = s.rfind('h')
sb = s[0:pos + 1]
se = s[p:-1] + s[-1]
ch = s[pos + 1:p]
print(s[0:p] + ch + se)
