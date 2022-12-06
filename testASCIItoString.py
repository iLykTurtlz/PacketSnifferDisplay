

data = "41424320202020204445460d0a444546206465660d0a474849206768690d0a0d0a51525371727320"
bytes = bytearray.fromhex(data)
string = bytes.decode()
print(string)

myList = string.split("\r\n")
print(myList)

firstList = myList[:myList.index("")]
secondList = myList[(myList.index("")+1):]
print("Header : ")
print(firstList)
print("Body : ")
print(secondList)

