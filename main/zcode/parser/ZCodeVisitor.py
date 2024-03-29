# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mptype.
    def visitMptype(self, ctx:ZCodeParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcall.
    def visitFuncall(self, ctx:ZCodeParser.FuncallContext):
        return self.visitChildren(ctx)



del ZCodeParser