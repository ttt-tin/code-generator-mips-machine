from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import MIPSCode



class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.data = '.data\n'
        self.text = '.text\n'
        self.globl = ''
        self.regTable = {
            'v': ['',''],
            'a': ['','','',''],
            't': ['','','','','','','','','',''],
            's': ['','','','','','','']
        }
        self.mips = MIPSCode()

    def getReg (self, typ, var = 'temp'):
        for i in range(0, len(self.regTable[typ])):
            if self.regTable[typ][i] == '':
                self.regTable[typ][i] = var
                return typ + str(i)
        return None

    def freeReg (self, reg):
        typ = reg[0]
        index = int(reg[1])
        self.regTable[typ][index] = ''

    def emitICONST(self, in_):
        reg = self.getReg('t')
        if reg:
            return self.mips.emitLOADI(reg, str(in_)), reg
        else:
            raise IllegalRuntimeException("No register left")

    def emitADDOP(self, op, in1, in2, typ):
        if type(typ) is IntegerType:
            reg = self.getReg('t')
            return self.mips.emitADD(reg, in1, in2), reg

    def emitMETHOD (self, name, in_, frame):
        reg = self.getReg('v')
        code = self.mips.emitGLOBAL(name) + (self.mips.emitENTER(name) if frame.name != 'main' else '') + self.mips.emitLABEL(name)
        return code

    def emitPUTINT (self, reg):
        self.regTable['v'][0] = 'temp'
        reg1 = self.getReg('a')
        return self.mips.emitLOADI('v0', '1') + self.mips.emitMOVE(reg1, reg) + self.mips.emitSYSCALL()
            
    def emitENDMETHOD (self, reg, frame):
        if reg == None:
            if frame.name != 'main':
                return self.mips.emitJR('ra') + self.mips.emitEND(frame.name)
            else:
                return self.mips.emitEND(frame.name)

    def emitENDING (self):
        print(self.text)
        file = open(self.filename, "w")
        file.write(''.join(self.data + self.text + self.globl))
        file.close()

    def printout(self, in_, reg):
        #in_: String
        if type(in_) is list:
            for x in in_:
                self.printout(x, reg)
        else:
            if reg == 'text':
                self.text = self.text + in_
            elif reg == 'data':
                self.text = self.data + in_
            elif reg == 'globl':
                self.text = self.globl + in_

    def clearBuff(self, reg):
        self[reg].clear()





        
