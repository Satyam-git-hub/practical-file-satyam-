str="an apple a day keeps doc away"
str2="a banana is good for health"
print(str)
print(str2)
str=list(str)
str2=list(str2)
n=5
str[:n],str2[:n]=str2[:n],str[:n]

def LtoS(s):
    str1 = ""

    for ele in s:
        str1 += ele
    return str1
print(LtoS(str))
print(LtoS(str2))