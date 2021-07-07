import re

string = "race a ecar"

def valid_palin(s):
    if s == "":
        return True 
		
    s = s.lower()
    s = re.sub('[^A-Za-z0-9]+', '', s)

    if list(s) == list(reversed(s)):
        return True
    else: 
        return False

print(valid_palin(string))