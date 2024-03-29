from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([FuncDecl("main",
			self.visit(ctx.mptype()),
                        [],
                        None,
                        BlockStmt([self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:ZCodeParser.MptypeContext):
        if ctx.INTTYPE():
            return IntegerType()
        else:
            return VoidType()

    def visitBody(self,ctx:ZCodeParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:ZCodeParser.FuncallContext):
        return FuncCall(ctx.ID().getText(),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:ZCodeParser.ExpContext):
        if ctx.funcall():
            return self.visit(ctx.funcall())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.ID():
            return ID(ctx.ID().getText())
        else:
            return BinExpr('+', self.visit(ctx.exp()[0]), self.visit(ctx.exp()[1]))
