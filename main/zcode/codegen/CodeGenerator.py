'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), list()), CName(self.libName)),
                    Symbol("putInt", MType(list(), 'v0'), CName(self.libName)),
                    Symbol("putIntLn", MType(list(), 'v0'), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.path = dir_
        self.emit = Emitter(self.path + "/extra_ass.asm")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        e = SubBody(None, self.env)
        for x in ast.decls:
            e = self.visit(x, e)
        # generate default constructor
        self.emit.emitENDING()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.return_type is None
        isMain = consdecl.name == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        returnReg = '' if isInit or isMain else consdecl.return_type
        methodName = "<init>" if isInit else consdecl.name
        inReg = list() if isMain else list()
        mtype = MType(inReg, returnReg)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, frame), 'text')

        glenv = o

        # Generate code for parameter declarations
        body = consdecl.body
        # Generate code for statements
        self.emit.printout(list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body)), 'text' if isMain else 'globl')
        self.emit.printout(self.emit.emitENDMETHOD(None, frame), 'text' if isMain else 'globl')

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.return_type)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.return_type), CName('extra_ass'))] + subctxt.sym)

    def visitFuncCall(self, ast, o):
        #ast: FuncCall
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        list_code = ''
        list_reg = list()
        list_type = list()
        for x in ast.args:
            str1, reg1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (list_code + str1, list_reg.append(reg1), list_type.append(typ1))
        if ast.name == 'putInt':
            return in_[0] + self.emit.emitPUTINT(list_reg[0])

    def visitIntegerLit(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        code, reg = self.emit.emitICONST(ast.val)
        return code, reg, IntegerType()

    def visitBinExpr(self, ast, o):
        op = str(ast.op)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        lhs, reg1, leftType = self.visit(ast.left, Access(frame,nenv,False,True))
        rhs, reg2, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
        
        if op == '+':
            code, reg = self.emit.emitADDOP(op, reg1, reg2, leftType)

        if type(ast.left) is IntegerLit:
            self.emit.freeReg(reg1)
        if type(ast.right) is IntegerLit:
            self.emit.freeReg(reg2)

        return lhs + rhs + code, reg, leftType
    