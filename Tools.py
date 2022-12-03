from operator import *
def str_to_hex(s):
	res = int(s,16)
	return hex(res)
	
	
def str_to_int(s):
	return int(s,16)

# str to bin cause our hex is a string
def str_to_bin(s):
    # print(s)
    
    res = ""
    for i in range (len(s)):
        tmp = (int(s[i], 16))
        tmp = (bin(tmp))[2:]
        while(len(tmp) < 4):
            tmp="0"+tmp
        res = res+tmp
    return res

# solution un peu de travers mais bon
def binary_sum(s1, s2):
# prends deux mots de 16 bits (0bXXXXXXXX) et les additionne
    # print(s1)
    # print(s2)
    # print(len(s1))
    # print(len(s2))
    
    if (len(s1) != 18) or (len(s2) != 18):
        print("Les operandes ne sont pas de taille 16")
        return
    
    s1dec = int(s1, 2)
    s2dec = int(s2, 2)
    res = bin(add(s1dec, s2dec))

    if(len(res) == 19):
        res = res[3:]
        res = "0b"+res
        res = binary_sum(res, "0b0000000000000001")
    else :
        res= res [2:]
    
    return res