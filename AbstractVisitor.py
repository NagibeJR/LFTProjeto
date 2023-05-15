from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
#declaracao de variaveis

    @abstractmethod
    def visitProgramaFuncDecl(self, programa):
        pass

    @abstractmethod
    def visitProgramaVarDecl(self, programa):
        pass

    @abstractmethod
    def visitProgramaFuncDeclProgram(self, programa):
        pass

    @abstractmethod
    def visitProgramaVarDeclProgram(self, programa):
        pass

    @abstractmethod
    def visitVarDecl(self, varDecl):
        pass
      
    def visitVarDeclID(self, varDeclID):
        pass

    @abstractmethod
    def visitVarDeclIDAssign(self, varDeclIDAssign):
        pass
      
    @abstractmethod
    def visitVarDeclIDAssignID(self, varDeclIDAssignID):
        pass

    @abstractmethod
    def visitVarDeclIDAssignList(self, varDeclIDAssignList):
        pass 

    @abstractmethod
    def visitVarDeclIDAssignListTIPO(self, varDeclIDAssignListTIPO):
        pass 

#declaracao de funcoes
    @abstractmethod
    def visitFuncDecl(self, funcDecl):
        pass 

    @abstractmethod
    def visitFuncDeclSignature(self, funcDeclSignature):
        pass 

#assinatura das funcoes
    @abstractmethod
    def visitSignature(self, signature):
        pass 

    @abstractmethod
    def visitSignatureFunc(self, signatureFunc):
        pass
      
#parametros das funcoes
    @abstractmethod
    def visitFuncParametros(self, funcParametros):
        pass

    @abstractmethod
    def visitFuncParametrosID(self, funcParametrosID):
        pass

    @abstractmethod
    def visitFuncParametrosIDList(self, funcParametrosIDList):
        pass

#corpo das funcoes
    @abstractmethod
    def visitBody(self, body):
        pass

    @abstractmethod
    def visitBodyComandos(self, BodyComandos):
        pass

    @abstractmethod
    def visitBodyComando(self, BodyComando):
        pass

    @abstractmethod
    def visitBodyOrComando(self, BodyOrComando):
        pass

    @abstractmethod
    def visitBodyOrComando2(self, BodyOrComando2):
        pass

#comandos
    @abstractmethod
    def visitComando(self, comando):
        pass

    @abstractmethod
    def visitSingleComando(self, singleComando):
        pass

    @abstractmethod
    def visitCompoundComando(self, CompoundComando):
        pass

#comandos simples
    @abstractmethod
    def visitComandoVarDecl(self, ComandoVarDecl):
        pass

    @abstractmethod
    def visitComandoExpressao(self, ComandoExpressao):
        pass

    @abstractmethod
    def visitComandoReturn(self, ComandoReturn):
        pass

    @abstractmethod
    def visitComandoWhile(self, ComandoWhile):
        pass

    @abstractmethod
    def visitComandoIf(self, ComandoIf):
        pass

    @abstractmethod
    def visitComandoIfElse(self, ComandoIfElse):
        pass

    @abstractmethod
    def visitComandoFor(self, ComandoFor):
        pass

#expressoes
    @abstractmethod
    def visitExpressao(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoID(self, ExpressaoID):
        pass  

    @abstractmethod
    def visitExpressaoInt(self, ExpressaoInt):
        pass

    @abstractmethod
    def visitExpressaoFloat(self, ExpressaoFloat):
        pass

    @abstractmethod
    def visitExpressaoString(self, ExpressaoString):
        pass

    @abstractmethod
    def visitExpressaoPlus(self, ExpressaoPlus):
        pass
      
    @abstractmethod
    def visitExpressaoMinus(self, ExpressaoMinus):
        pass

    @abstractmethod
    def visitExpressaoMult(self, ExpressaoMult):
        pass

    @abstractmethod
    def visitExpressaoDiv(self, ExpressaoDiv):
        pass

    @abstractmethod
    def visitExpressaoMod(self, ExpressaoMod):
        pass

    @abstractmethod
    def visitExpressaoAnd(self, ExpressaoAnd):
        pass

    @abstractmethod
    def visitExpressaoOr(self, ExpressaoOr):
        pass

    @abstractmethod
    def visitExpressaoGreater(self, ExpressaoGreater):
        pass

    @abstractmethod
    def visitExpressaoLess(self, ExpressaoLess):
        pass

    @abstractmethod
    def visitExpressaoGreaterEqual(self, ExpressaoGreaterEqual):
        pass

    @abstractmethod
    def visitExpressaoLessEqual(self, ExpressaoLessEqual):
        pass

    @abstractmethod
    def visitExpressaoEqual(self, ExpressaoEqual):
        pass

    @abstractmethod
    def visitExpressaoNotEqual(self, ExpressaoNotEqual):
        pass

    @abstractmethod
    def visitExpressaoAssign(self, ExpressaoAssign):
        pass
  
    @abstractmethod
    def visitExpressaoCall(self, ExpressaoCall):
        pass

    @abstractmethod
    def visitExpressaoNum(self, ExpressaoNum):
        pass

    @abstractmethod
    def visitExpressaoBool(self, EspressaoBool):
        pass

    @abstractmethod
    def visitExpressaoIncrement(self, ExpressaoIncrement):
        pass

    @abstractmethod
    def visitExpressaoDecrement(self, ExpressaoDecrement):
        pass

    @abstractmethod
    def visitExpressaoExpo(self, ExpressaoExpo):
        pass

    @abstractmethod
    def visitExpressaoIncrementn(self, ExpressaoIncrementn):
        pass

    @abstractmethod
    def visitExpressaoDecrementn(self, ExpressaoDecrementn):
        pass

    @abstractmethod
    def visitExpressaoMultincrement(self, ExpressaoMultincrement):
        pass

    @abstractmethod
    def visitExpressaoDivideincrement(self, ExpressaoDivideincrement):
        pass

    @abstractmethod
    def visitExpressaoModincrement(self, ExpressaoModincrement):
        pass

    @abstractmethod
    def visitExpressaoEEQ(self, ExpressaoEEQ):
        pass

    @abstractmethod
    def visitExpressaoNNEQ(self, ExpressaoNNEQ):
        pass

    @abstractmethod
    def visitExpressaoNOT(self, ExpressaoNOT):
        pass

    @abstractmethod
    def visitExpressaoFIM(self, ExpressaoFIM):
        pass

    @abstractmethod
    def visitExpOpexp(self, ExpOpexp):
        pass

#Call
    @abstractmethod
    def visitCall(self, Call):
        pass

    @abstractmethod
    def visitNoParamsCall(self, NoParamsCall):
        pass

#Params
    @abstractmethod
    def visitParams(self, Params):
        pass

    @abstractmethod
    def visitSingleParams(self, SingleParams):
        pass

    @abstractmethod
    def visitCompoundParams(self, CompoundParams):
        pass

#Statement
    @abstractmethod
    def visitAssign(self, Assign):
        pass

    @abstractmethod
    def visitAssignAssign(self, AssignAssign):
        pass

    @abstractmethod
    def visitNoAssign(self, NoAssign):
        pass

    @abstractmethod
    def visittipodecl(self, tipodecl):
        pass

    @abstractmethod
    def visittipodecltipo(self, tipodecltipo):
        pass

    @abstractmethod
    def visitstring(self, String):
        pass

    @abstractmethod
    def visittipo(self, Tipo):
        pass

