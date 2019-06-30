
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
