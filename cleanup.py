

with open("data.txt","r") as f, open("rawPacketsCleanedup.txt","w") as g:
    for line in f:
        #print(line)
        if not line.isspace():
            g.write(line[:55]+"\n")



