# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\6\5\61\n\5\r\5\16\5\62")
        buf.write("\3\6\6\6\66\n\6\r\6\16\6\67\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\6\rG\n\r\r\r\16\rH\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\3\20\2\2\21\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2T\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5&\3\2\2\2\7*")
        buf.write("\3\2\2\2\t\60\3\2\2\2\13\65\3\2\2\2\r9\3\2\2\2\17;\3\2")
        buf.write("\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31")
        buf.write("F\3\2\2\2\33L\3\2\2\2\35N\3\2\2\2\37P\3\2\2\2!\"\7o\2")
        buf.write("\2\"#\7c\2\2#$\7k\2\2$%\7p\2\2%\4\3\2\2\2&\'\7k\2\2\'")
        buf.write("(\7p\2\2()\7v\2\2)\6\3\2\2\2*+\7x\2\2+,\7q\2\2,-\7k\2")
        buf.write("\2-.\7f\2\2.\b\3\2\2\2/\61\t\2\2\2\60/\3\2\2\2\61\62\3")
        buf.write("\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\n\3\2\2\2\64\66")
        buf.write("\t\3\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\67")
        buf.write("8\3\2\2\28\f\3\2\2\29:\7-\2\2:\16\3\2\2\2;<\7*\2\2<\20")
        buf.write("\3\2\2\2=>\7+\2\2>\22\3\2\2\2?@\7}\2\2@\24\3\2\2\2AB\7")
        buf.write("\177\2\2B\26\3\2\2\2CD\7=\2\2D\30\3\2\2\2EG\t\4\2\2FE")
        buf.write("\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\r")
        buf.write("\2\2K\32\3\2\2\2LM\13\2\2\2M\34\3\2\2\2NO\13\2\2\2O\36")
        buf.write("\3\2\2\2PQ\13\2\2\2Q \3\2\2\2\6\2\62\67H\3\b\2\2")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    ADDITION = 6
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    SEMI = 11
    WS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'+'", "'('", "')'", "'{'", "'}'", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "ADDITION", "LB", "RB", 
            "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "ADDITION", 
                  "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


