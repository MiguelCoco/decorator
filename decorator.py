#定义装饰器
def document_it(func):
	def new_func(*args,**kwargs):
		print('Running function:',func.__name__)
		print('Positional arguments:', args)
		print('Keyword atguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result is:', result)
		return result
	return new_func

def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return result * result
	return new_function

#应用两个装饰器
@document_it
@square_it
def add_ints(a,b):
	return a + b 
print(add_ints(3,5))

#离def近先执行
@square_it
@document_it
def add_ints(a,b):
	return a + b 
print(add_ints(3,5))
