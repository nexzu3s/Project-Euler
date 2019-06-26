total = 0
lim =1000

for i in range(lim):
    if (i % 3 == 0) or (i % 5 ==0):
        total+=i
print (total)
