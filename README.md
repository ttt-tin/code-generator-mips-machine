# Introduction
This project aim to create a code generator for Zcode programming language (which is implemented lexer, parser and static checker previously) using ANTLR tool for executing on an register-based machine (MIPS).
# Challenges
ANTLR provides complete set of tool for create a new programming language included code generator in the compiler. But with ANTLR tool, we have to use JVM to execute the code which is a stack-based machine. Therefore when implement a code generator using register-based machine like MIPS, we have to research a huge amount of knowledge about MIPS and register-based machine and re-implement all of the architecture of code generator like Frame, Emitter and Machine Code.
Another challenge is that register allocation problem in register-based machine. As we know that in register-based machine, we have a limit register to do the calculation and logic using it wisely is extremely important.
# What to do
In this project, we will implement all the Fram, Emitter and Machine Code for MIPS machine. About register allocation, we will use Chaitin's algorithm which is one of the most famous solutions for that problem. This algorithm will solve the register allocation by using graph and coloring theory to allocate registers based on their live ranges.
# Conclusion
Through this project, i learned more about how to create a programming language compiler and how it work.
