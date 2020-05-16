from pwn import *
from Crypto.Util.number import *
#context.log_level = 'debug'

def lsb(time,e,c,n):
	c_=long(pow(time,e))
	c_*=c
	c_%=n
	return(c_)
#r=process('./election' )
#gdb.attach(r)
r=remote('edu-ctf.csie.org',10192)
ans=0
r.sendlineafter("> ","1")
exec(r.recvline())
exec(r.recvline())
exec(r.recvline())
print(type(n))
print(type(c))
print(type(e))
offset=n%16
for i in range(1,260):
	r.sendlineafter("> ","2")
	t=pow(16,i)
	c_=lsb(t,e,c,n)
	r.sendline(str(c_))
	exec(r.recvline())
	for j in range(0,15):
		count=(16-((offset*j)%16))%16
		if(count==m):
			m=j
			break
	ans+=long(n*m/t+15/16)
	if(t>(long(n/16+1))):
		print(ans)
		break
print(long_to_bytes(ans))
	

