from AbstractVisitor import AbstractVisitor
from ExpressionLanguageSint import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitVarDeclID (self, varDeclID):
        varDeclID.id.accept(self)
        print(blank() + 'var ' + varDeclID.id + ';')