import re

s = "dawid.sielski@outlook.com ddfdfdfasdjHDFOIV 876 8YT HJGO8 GJH V    dawiddawid22@gmail.com   tyrbodivx@wp.pl lj 4;kj4kj 2;lkns;ljdvn  "

print(s.split())

print(re.findall(r"[a-z0-9]*\.?[a-z0-9]*@[a-z0-9]+\.[a-z0-9]*", s)) #find email
print(re.search(r"[a-z0-9]*\.?[a-z0-9]*@[a-z0-9]+\.[a-z0-9]*", s)) #find email

