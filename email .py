import re 
file = open("email.txt",'r') #opening file
l1 = []
for i in file:
    l1.append(i) # generating list
list = re.findall("[\w]{4,10}@\w{3,8}.\w{2,4}","".join(l1))#pattern
for i in list:
    print(i) # printing