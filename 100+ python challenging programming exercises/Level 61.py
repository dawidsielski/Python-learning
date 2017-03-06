"""line 2008""" 
import zlib
# seq = 'hello world!hello world!hello world!hello world!'
# compressed = zlib.compress(seq)
# print(compressed)

s = b'hello world!hello world!hello world!hello world!'
# s = s.encode('utf-8')
t = zlib.compress(s)
print (t)
print (zlib.decompress(t))