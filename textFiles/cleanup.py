

with open("betterHttpTrace.txt","r") as f, open("EvenBetterHttpTrace.txt","w") as g:
    for line in f:
        #print(line)
        if not line.isspace():
            g.write(line[:55]+"\n")
    f.close()
    g.close() 


