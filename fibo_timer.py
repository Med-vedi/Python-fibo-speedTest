import time

n = int(input('Какое по счету число последовательности Фибоначчи искать(например, 300)? '))

num = int(input('Колличество циклов для прогонки секундомера(например, 20): '))

class Timer:
	# декоратор/контекстный менеджер

	def __init__(self, num):
		self.num = num
	def __call__(self,func):

		def wrapper(*args, num=num):
			print('-'*10)
			print('Запуск цикла из {}'.format(num), 'повторов')
			print('-'*10)

			result = 0
			# запуск цикла
			for f in range(num):
				start = time.time()
				func(*args)
				end = time.time()
				result += (end-start)
			result/=num
			
			print('-'*10)
			print('Среднее время выполнения цикла %.5f' %(result), 'секунд')
			print('-'*10)
		return wrapper
	# вход для контекстного менеджера(читать здесь https://python-scripts.com/contextlib)
	def __enter__(self):
		self.start = time.time()
		return self
	# выход для контекстного менеджера
	def __exit__(self, *kwargs):
		self.end = time.time()
		run_timing = (self.end-self.start)/num
		print('Время выполнения этой же задачи через контестный менеджер: %.5f'%run_timing, 'секунд')
# принимаем из инпута кол-во прогонов
timer = Timer(num)
#запуск  декоратора

@timer
def fibo(n):
	# последовательность Фибоначчи
	current = 0
	after = 1 

	for num in range(n):
		current, after = after, current + after
	print(current)


# запуск контекстного менеджера
with Timer(num):
	fibo(n)







 