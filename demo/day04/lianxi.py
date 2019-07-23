def math(a,b):
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)
    print(n1/n2)
with open ("D:\\softwareDate\\pycharm\\wuch_1906A\\demo\\day04\\cards.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')

        math(line[0],line[1])