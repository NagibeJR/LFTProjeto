from abc import abstractmethod
from abc import ABCMeta

# Classe abstrata
#declaracao de variaveis

class varDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class varDeclID(varDecl):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

    def accept(self, visitor):
        return visitor.visitVarDeclID(self)
    
class varDeclIDAssign(varDecl):
    def __init__(self, tipo, id, expressao):
        self.tipo = tipo
        self.id = id
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitVarDeclIDAssign(self)
    
class varDeclIDAssignID(varDecl):
    def __init__(self, tipo, id, id2):
        self.tipo = tipo
        self.id = id
        self.id2 = id2

    def accept(self, visitor):
        return visitor.visitVarDeclIDAssignID(self)
    
class varDeclIDAssignList(varDecl):
    def __init__(self, tipo, id, listexp):
        self.tipo = tipo
        self.id = id
        self.listexp = listexp

    def accept(self, visitor):
        return visitor.visitVarDeclIDAssignList(self)
    
class varDeclIDAssignListID(varDecl):
    def __init__(self, tipo, id, listexp, id2):
        self.tipo = tipo
        self.id = id
        self.listexp = listexp
        self.id2 = id2

    def accept(self, visitor):
        return visitor.visitVarDeclIDAssignListID(self)
    
#declaracao de funcoes
class funcDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class funcDeclSignature(funcDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body

    def accept(self, visitor):
        return visitor.visitFuncDeclSignature(self)
    
#assinatura das funcoes
class signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class signatureFunc(signature):
    def __init__(self, tipo, id, funcParametros, tipoReturn, body):
        self.tipo = tipo
        self.id = id
        self.funcparametros = funcParametros
        self.tipo2 = tipoReturn
        self.body = body

    def accept(self, visitor):
        return visitor.visitSignatureFunc(self)
    
#parametros das funcoes
class funcParametros(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class funcParametrosID(funcParametros):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

    def accept(self, visitor):
        return visitor.visitFuncParametrosID(self)
    
class funcParametrosIDList(funcParametros):
    def __init__(self, tipo, id, funcParametros):
        self.tipo = tipo
        self.id = id
        self.funcParametros = funcParametros

    def accept(self, visitor):
        return visitor.visitFuncParametrosIDList(self)
    
#corpo das funcoes
class body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class BodyComandos(body):
    def __init__(self, comandos):
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitBodyComandos(self)
    
class Bodycomando(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class BodyOrComando(body):
    def __init__(self, body):
        self.body = body

    def accept(self, visitor):
        return visitor.visitBodyOrComando(self)
    
class BodyOrComando2(body):
    def __init__(self, comando):
        self.comando = comando

    def accept(self, visitor):
        return visitor.visitBodyOrComando2(self)
    
#comandos
class comando(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class singleComando(comando):
    def __init__(self, comando):
        self.comando = comando

    def accept(self, visitor):
        return visitor.visitSingleComando(self)
    
class CompoundComando(comando):
    def __init__(self, comando, comandos):
        self.comando = comando
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitCompoundComando(self)
    
#comandos simples
class Comando (metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ComandoVarDecl(Comando):
    def __init__(self, varDecl):
        self.varDecl = varDecl

    def accept(self, visitor):
        return visitor.visitComandoVarDecl(self)
    
class ComandoExpressao(Comando):
    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitComandoExpressao(self)
    
class ComandoReturn(Comando):
    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitComandoReturn(self)
    
class ComandoWhile (Comando):
    def __init__(self, expressao, bodyorcomando):
        self.expressao = expressao
        self.bodyorcomando = bodyorcomando

    def accept(self, visitor):
        return visitor.visitComandoWhile(self)
    
class ComandoIf (Comando):
    def __init__(self, expressao, bodyorcomando):
        self.expressao = expressao
        self.bodyorcomando = bodyorcomando

    def accept(self, visitor):
        return visitor.visitComandoIf(self)
    
class ComandoIfElse (Comando):
    def __init__(self, expressao, bodyorcomando, bodyorcomando2):
        self.expressao = expressao
        self.bodyorcomando = bodyorcomando
        self.bodyorcomando2 = bodyorcomando2

    def accept(self, visitor):
        return visitor.visitComandoIfElse(self)
    
class ComandoFor (Comando):
    def __init__(self, expressao, expressao2, expressao3, bodyorcomando):
        self.expressao = expressao
        self.expressao2 = expressao2
        self.expressao3 = expressao3
        self.bodyorcomando = bodyorcomando

    def accept(self, visitor):
        return visitor.visitComandoFor(self)
    
#expressoes
class expressao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressaoID(expressao):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitExpressaoID(self)
    
class ExpressaoInt(expressao):
    def __init__(self, int):
        self.int = int

    def accept(self, visitor):
        return visitor.visitExpressaoInt(self)
    
class ExpressaoFloat(expressao):
    def __init__(self, float):
        self.float = float

    def accept(self, visitor):
        return visitor.visitExpressaoFloat(self)
    
class ExpressaoString(expressao):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        return visitor.visitExpressaoString(self)
    
class ExpressaoPlus(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoPlus(self)
    
class ExpressaoMinus(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoMinus(self)
    
class ExpressaoMult(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoMult(self)
    
class ExpressaoDiv(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoDiv(self)
    
class ExpressaoMod(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoMod(self)
    
class ExpressaoAnd(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoAnd(self)
    
class ExpressaoOr(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2

    def accept(self, visitor):
        return visitor.visitExpressaoOr(self)
    
class ExpressaoGreater(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoGreater(self)
    
class ExpressaoLess(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoLess(self)
    
class ExpressaoGreaterEqual(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoGreaterEqual(self)
    
class ExpressaoLessEqual(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoLessEqual(self)
    
class ExpressaoEqual(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoEqual(self)
    
class ExpressaoNotEqual(expressao):
    def __init__(self, expressao, expressao2):
        self.expressao = expressao
        self.expressao2 = expressao2
    
    def accept(self, visitor):
        return visitor.visitExpressaoNotEqual(self)
    
class ExpressaoAssign(expressao):    
    def __init__(self, id, expressao):
        self.id = id
        self.expressao = expressao
    
    def accept(self, visitor):
        return visitor.visitExpressaoAssign(self)
    
class ExpressaoCall(expressao):
    def __init__(self, call):
        self.call = call
    
    def accept(self, visitor):
        return visitor.visitExpressaoCall(self)
    
class ExpressaoNum(expressao):
    def __init__(self, num):
        self.num = num
    
    def accept(self, visitor):
        return visitor.visitExpressaoNum(self)
    
class EspressaoBool (expressao):
    def __init__(self, bool):
        self.bool = bool
    
    def accept(self, visitor):
        return visitor.visitExpressaoBool(self)
    
#Call
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__(self, id, params):
        self.id = id
        self.params = params

    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)
    
#Params
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleParams(Params):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitSingleParams(self)
    
class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params

    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

#Statement
class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignAssign(Assign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitAssignAssign(self)
    
class NoAssign(Assign):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitNoAssign(self)