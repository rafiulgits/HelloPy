
def encode_string(value):
	key = __encode_string(value.encode()).decode()
	key = key.replace('=\n', '')
	return key[::-1]


def decode_string(key):
	key = key[::-1]
	key += '=\n'
	try:
		return __decode_string(key.encode()).decode()
	except UnicodeDecodeError as e:
		return None




from hashlib import md5,sha256
def hashvalue(key):
	a = sha256(key.encode()).hexdigest()
	return int(a, 16)


print(hashvalue('sakkhat.inc') %10**16)
print(hashvalue('gear-bangladesh')%10**16)
print(hashvalue('honny') % 10**16)