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