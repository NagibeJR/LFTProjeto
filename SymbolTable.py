SymbolTable = []

INT = 'int'
FLOAT = 'float'
STRING = 'string'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'

DEBUG = 0
Number = [INT, FLOAT]

def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()