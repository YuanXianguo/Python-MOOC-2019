n = eval(input())
nM = abs(n)
if nM == 0:
    nadd = nsub = 10
    nmul = 0
else:
    sign = n // nM
    nadd = sign * abs(nM + 10)
    nsub = sign * abs(nM - 10)
    nmul = sign * abs(nM * 10)
print(nM, nadd, nsub, nmul)
