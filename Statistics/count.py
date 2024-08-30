import re
pattern= '[a-z]'
sentence= "Namaste! it's me Unique Adhikari. A CSIT student. My favourite animal is rabbit"
count={}

for match in re.finditer(pattern, sentence.lower()):
    char= match.group()
    if char in count:
        count[char]+=1
    else:
        count[char]=1

print(count)