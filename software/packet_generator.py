#! /usr/bin/python
import struct

NPack = 643
tvalue = 643
f = open('/home/elvis/Workspace/automated-grading-new/data/packetout', 'wb')

f.write(b"SS")
f.write(struct.pack('I',0))
f.write(struct.pack('H',NPack))
f.write(b'E')

f.write(b"SL")
f.write(struct.pack('I',10000)) #Define Sampling Duration here
f.write(struct.pack('H',0))
f.write(b'E')


for i in range(0,NPack):
	f.write(b"SD")
	f.write(struct.pack('I',tvalue))
	if (i%2):
		f.write(b'\xFF\xFF')
	else:
		f.write(b'\xF0\xF0')
	f.write(b'E')
	tvalue = tvalue - 1

f.close()
