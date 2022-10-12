func_1_calls = 6

def func_1():
	global func_1_calls
	func_1_calls = func_1_calls + 1
	return func_1_calls
