IMAGE_SIZE equ 125 ; 125 sectors (64,000 bytes) per image

read_image:
    pusha ; save registers

    mov ah, 0x02 ; 'Read Sectors Into Memory' function
    mov al, IMAGE_SIZE ; sector amount

    mov cl, 0x02 ; sector (0x02 is the first 'available' sector)
    mov ch, 0x00 ; cylinder (from 0x0 to 0x3FF)
    mov dh, 0x00 ; head number (from 0x0 to 0xF)

    int 0x13 ; call the BIOS interrupt
    jc disk_error ; if the carry flag is set, an error occurred

    popa ; restore registers
    ret ; return from function

disk_error:
    mov si, DISK_ERROR_MESSAGE ; load the address of the error message
    mov cl, ah ; load the error code

    mov ah, 0x00 ; 'Set Video Mode' function
    mov al, 0x03 ; 80x25 text mode

    int 0x10 ; call the BIOS interrupt

    call print ; print the error message
    call print_hex ; print the error code in hex
    call line_break ; add a line break

    hlt ; halt the system

DISK_ERROR_MESSAGE: db "Error: Disk read failed with code 0x", 0