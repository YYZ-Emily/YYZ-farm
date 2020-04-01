fobj=open('../tmp/String.txt')
for x in fobj:
    for i in x:
        if i.isdigit():
            print(i,end='')
fobj.close()

