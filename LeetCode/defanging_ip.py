import re 

ipaddress = "1.1.1.1"
address = "255.100.50.0"

def defang(s):
	return re.sub(r'\.', '[.]', s)

print(defang(address))