.data
.text
.globl main
main:
li $t0, 9999
li $t1, 9999
add $t2, $t0, $t1
li $v0, 1
move $a0, $t2
syscall
.end main
