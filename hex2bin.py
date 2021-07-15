#!/usr/bin/env python2

import sys, struct

data_bin = ''
with open(sys.argv[1]) as hexdump:
	data = hexdump.read()
	data = data.split("\n")
	for i in data:
		data_hex = i[10:57].split(' ')
		for j in data_hex:
			data_bin += struct.pack("B", int(j, 16))

binary_file = open(sys.argv[2], "wb")
binary_file.write(data_bin)
binary_file.close()

