a=[0x0f,0x09,0x02,0x0c,0xf8,0xfa,0x30,0xf0,0x22,0x22,0xfa,0x30,0xf0,0x22,0x22,0xfa,0x30,0xf0,0x22,0x22,0xfa,0x35,0xed,0xe4,0xf6,0xfa,0xe4,0xec,0x35,0xe1,0x22,0x22,0xc6]
#1 0 0 0 0 1 0 1 1 0 0 0 1
c=""
for i in range(len(a)):
	c+=chr((a[i]^0x66)-0x23)

print(c)