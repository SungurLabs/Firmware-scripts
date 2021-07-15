#!/usr/bin/env python3

import sys


partitions = [
	("boot", 0x0, 0x50000),
	("uImage_kernel", 0x50000, 0x200000),
	("squashfs", 0x250000, 0x760000),
	("data", 0x9B0000, 16777216-0x9B0000)
]

firmware = open(sys.argv[1], "rb")
for part, offset, size in partitions:
	firmware.seek(offset, 0) # Moves the cursor up to the offset.
	data = firmware.read(size)
	output = open(part, "wb")
	output.write(data)
	print("{} - saved!".format(part))
	output.close()



