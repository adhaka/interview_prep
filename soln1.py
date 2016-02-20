

#  solution to problem 1

import sys

inp_list = []


while True:
	try:
		value = raw_input()
		inp_list.append(value)
	except (EOFError):
		break


pro_data = []
for val in inp_list:
	d = map(int, val.strip().split(' '))
	pro_data.append(d)




