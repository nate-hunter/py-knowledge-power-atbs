import time, sys

print('hello')
indent = 0
indent_increasing = True

try:
	while True:
		print(' ' * indent, end='')
		print('********')
		time.sleep(0.1)

		if indent_increasing:
			indent += 1
			if indent == 20:
				print(' ' * (indent - 8), end='')
				print('~~~~~~~~*******+')
				indent_increasing = False
		else:
			indent -= 1
			if indent == 0:
				print('+*******~~~~~~~~')
				indent_increasing = True
except KeyboardInterrupt:
	sys.exit()