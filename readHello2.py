file = open('test.txt','rt')

while True:
    str = file.read()
    if not str:
        break
    print(str,end ='')
file.close()