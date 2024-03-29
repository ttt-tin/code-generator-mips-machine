import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_0(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(2+3+4+5+6);}"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_1(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(0+0);}"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_int_2(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100+99);}"""
        expect = "199"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_int_3(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(23+345+65+345+654);}"""
        expect = "1432"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_4(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(9999+9999);}"""
        expect = "19998"
        self.assertTrue(TestCodeGen.test(input,expect,504))
