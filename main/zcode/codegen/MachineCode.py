'''
*   @author Dr.Nguyen Hua Phung
*   @version 1.0
*   28/6/2006
*   This class provides facilities for method generation
*
'''
from abc import ABC, abstractmethod, ABCMeta

class MachineCode(ABC):
    @abstractmethod
    def emitADD(self, des, reg1, reg2):
        pass

    @abstractmethod
    def emitADDI(self, des, reg1, i):
        pass

    @abstractmethod
    def emitLOADI(self, des, i):
        pass

    @abstractmethod
    def emitLOADW(self, des, var):
        pass

    @abstractmethod
    def emitLOADA(self, des, var):
        pass

    @abstractmethod
    def emitSYSCALL(self):
        pass

    @abstractmethod
    def emitLABEL(self, name):
        pass

    @abstractmethod
    def emitDATA(self):
        pass

    @abstractmethod
    def emitTEXT(self):
        pass

    @abstractmethod
    def emitVARIABLE(self, name, type, value):
        pass

    @abstractmethod
    def emitMAIN(self):
        pass

    @abstractmethod
    def emitGLOBAL(self, name):
        pass

    @abstractmethod
    def emitEND(self, name):
        pass

    @abstractmethod
    def emitJAL(self, name):
        pass

    @abstractmethod
    def emitJR(self, name):
        pass


class MIPSCode(MachineCode):
    END = "\n"
    INDENT = "\t"

    def emitADD(self, des, reg1, reg2):
        return 'add $' + des + ', $' + reg1 + ', $' + reg2 + MIPSCode.END

    def emitADDI(self, des, reg1, i):
        return 'addi $' + des + ', $' + reg1 + ', ' + i + MIPSCode.END

    def emitLOADW(self, des, var):
        return 'lW $' + des + ', ' + var + MIPSCode.END

    def emitLOADI(self, des, i):
        return 'li $' + des + ', ' + i + MIPSCode.END 

    def emitLOADA(self, des, var):
        return 'la $' + des + ', ' + var + MIPSCode.END 

    def emitSYSCALL(self):
        return 'syscall' + MIPSCode.END

    def emitLABEL(self, name):
        return name + ':' + MIPSCode.END

    def emitDATA(self):
        return '.data' + MIPSCode.END

    def emitTEXT(self):
        return '.text' + MIPSCode.END

    def emitVARIABLE(self, name, typ, value):
        return name + ': ' + typ + ' ' + value + MIPSCode.END

    def emitMOVE(self, des, source):
        return 'move $' + des + ', $' + source + MIPSCode.END

    def emitMAIN(self):
        return 'main:' + MIPSCode.END

    def emitGLOBAL(self, name):
        return '.globl ' + name + MIPSCode.END

    def emitENTER(self, name):
        return '.ent ' + name + MIPSCode.END

    def emitEND(self, name):
        return '.end ' + name + MIPSCode.END

    def emitJAL(self, name):
        return 'jal ' + name + MIPSCode.END

    def emitJR(self, name):
        return 'jr $' + name + MIPSCode.END
    
    
    
