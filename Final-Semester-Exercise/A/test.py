import re

str =  "Joey: (he’s just picked up their bill) Hey! So, what’s with the 20 percent tip? Did I do something wrong?"

regular = re.sub(r'\)\s',"", str)

print(regular)


