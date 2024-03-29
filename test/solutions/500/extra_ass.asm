.data
.text
.globl main
main:
li $t0, 2
li $t1, 3
add $t2, $t0, $t1
li $t0, 4
add $t1, $t2, $t0
li $t0, 5
add $t3, $t1, $t0
li $t0, 6
add $t4, $t3, $t0
li $v0, 1
move $a0, $t4
syscall
.end main
