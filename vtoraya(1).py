sl = {}
d = 0
string1 = input()
string2 = string1.split()
print(string2)
for i in range (len(string2)-1):
    string3 = string1.split()
    if string3[i] != string3[i+1]:
        d += 1
        sl[d] = string3[i] 
print(sl.keys())