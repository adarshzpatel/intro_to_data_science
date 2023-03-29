
from collections import Counter 
# Read strings from keyboard 
StringList1 = []

inp = "_"

while len(inp) != 0 : 
    inp = input("Enter string :")
    if(inp == ""):
        break
    StringList1.append(inp)
    

# Store frequenies of strings 
StringCounter = Counter(StringList1)

# Strings having more than 2 occurences
MStringList1 = [(key,StringCounter[key]) for key in StringCounter]

print("Strings having more than equal 2 occurences: ")

print([st for st,count in MStringList1 if count >= 2])

print("Check if even or odd frequency")

for key,value in MStringList1:
    if(value >= 2 and value % 2 == 0):
        print(key , "even")
    else: 
        print(key,"odd")
        
# Remove strings which have more than two occurences 
MStringList1 = [st for st,count in MStringList1 ]
print("After removing duplicate elemetns")
print(MStringList1)