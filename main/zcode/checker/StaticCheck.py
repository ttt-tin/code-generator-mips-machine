
"""
 * @author nhphung
"""
from AST import *
from Visitor import * 
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.parreg = partype
        self.retreg = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntegerType())),
    Symbol("putIntLn",MType([IntegerType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        return [self.visit(x,c) for x in ast.decls]

    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.body)) 
    

    def visitFuncCall(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.args]
        
        res = self.lookup(ast.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntegerLit(self,ast, c): 
        return IntegerType()
    

