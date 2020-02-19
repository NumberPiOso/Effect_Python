# utils.py
def to_str(data):
	if isinstance(data, str):
		return data
	elif isinstance(data, bytes):
		return data.decode()
	else:
		raise(TypeError(f' Must supply str or bytes, found {type(data)}.'))
