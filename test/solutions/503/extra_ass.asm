.data
.text
.globl main
main:
li $t0, 23
li $t1, 345
add $t2, $t0, $t1
li $t0, 65
add $t1, $t2, $t0
li $t0, 345
add $t3, $t1, $t0
li $t0, 654
add $t4, $t3, $t0
li $v0, 1
move $a0, $t4
syscall
.end main
