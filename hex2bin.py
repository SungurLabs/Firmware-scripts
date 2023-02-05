#!/usr/bin/env python2

import sys, struct

data_bin = bytearray()
with open(sys.argv[1]) as hexdump:
        for line in hexdump:
                data_hex= line[10:57].split(" ")
                for i in data_hex:
                        data_bin += struct.pack("B", int(i, 16))

binary_file = open(sys.argv[2], "wb")
binary_file.write(data_bin)
binary_file.close()
