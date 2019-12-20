lt = []
for i in range(5):
    lt.append(i)
lt[1] = 'pyth'
lt.insert(1,'yuan')
lt.pop(0)
for i in range(3):
    lt.pop(0)
if 0 in lt:
    print(True)
else:
    print(False)
    lt.append(0)
    print( "Now",True)
print(lt.index(0), len(lt), max(lt))
lt.clear()
print(lt)
