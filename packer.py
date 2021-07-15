#!/usr/bin/env python3

import sys


partitions = [
	("boot", 0x0, 0x50000),
	("uImage_kernel", 0x50000, 0x200000),
	("squashfs", 0x250000, 0x760000),
	("data", 0x9B0000, 16777216-0x9B0000)
]

firmware = open(sys.argv[1], "wb")
for part, offset, size in partitions:
	p = open(part, "rb")
	data = p.read()
	firmware.write(data)
	if len(data) < size:
		size_padd = size - len(data)
		padd = size_padd * b'\x00'
		firmware.write(padd)
		# squashfs should be padded for alignment purposes






