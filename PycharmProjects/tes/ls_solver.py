import numpy as np, re

with open("hh.txt")as f:
    text = f.read()

eqS = text.split("\n")
n = []
coefs = []

for eq in eqS:
    coefs.append([int(nn.replace(" ", "")) for nn in re.findall("[-]? *\d+", eq.split("=")[0])])
    n.append(int(eq.split("=")[1]))

for x in coefs:
    for i in range(22 - len(x)):
        x.append(0)

x = np.linalg.solve(np.array(coefs), np.array(n))

Flag = ""
for xx in x:
    Flag += chr(int(xx) + ((xx)-int(xx) > 0.5))

print(Flag)
