import my_lib 

def main():
	func_1_result = my_lib.func_1()
	print(func_1_result) # must be 1

	func_1_result = my_lib.func_1()
	print(func_1_result) # must be 2

	func_1_result = my_lib.func_1()
	print(func_1_result)

	func_1_result = my_lib.func_1()
	print(func_1_result)
	
main()