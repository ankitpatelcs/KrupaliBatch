import re

Nameage="RInKal"
#age=re.findall(r'\d{1,3}',Nameage)
names=re.findall(r'[A-Z][a-z]+',Nameage)

#print(age)
print(names)