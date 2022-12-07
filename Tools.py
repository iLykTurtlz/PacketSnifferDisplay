from operator import __add__ as add
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

# binary sucks in python
"""
def binary_sum(s1, s2):
'''prends deux mots de 16 bits (0bXXXXXXXX) et les additionne
pour verfier le checksum
''' 
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

    
"""
    
# meilleure solution
def hex_sum(h1,h2):
    """additionne deux hexa et gere les 'overflow' pour
    verifier le checksum"""
    # print(h1)
    # print(h2)
    
    max_len = max(len(h1), len(h2))
    res = hex(int(h1, 16) + int(h2, 16))
    # print(res)
    if(max_len < len(res)):
        # python hex toomfoolery
        res = res[3:]
        res = "0x"+res
        res= hex(int(res, 16) + int("0x01",16))
    return res
    
    
    
def convertIPAddress(addressHex):
        return f"{int(addressHex[0:2],16)}.{int(addressHex[2:4],16)}.{int(addressHex[4:6],16)}.{int(addressHex[6:8],16)}"
    
