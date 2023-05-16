from ExpressionLanguageSint import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor():

    def visitProgramaFuncDecl(self, programa):
        programa.funcdecl.accept(self)

    def visitProgramaComandos(self, programa):
        programa.comandos.accept(self)

    def visitProgramaFuncDeclPrograma(self, programa):
        programa.funcdecl.accept(self)
        programa.programa.accept(self)

    def visitProgramaComandosPrograma(self, programa):
        programa.comandos.accept(self)
        programa.programa.accept(self)

    def visitVarDeclID(self, varDeclID):
        print(varDeclID.tipo, ' ', end='', sep='')
        print(varDeclID.id, ' ', end='', sep='')

    def visitVarDeclIDAssign(self, varDeclIDAssign):
        print(varDeclIDAssign.tipo)
        print(varDeclIDAssign.id)
        varDeclIDAssign.expressao.accept(self)
  
    def visitVarDeclIDAssignID(self, varDeclIDAssignID):
        print(varDeclIDAssignID.tipo)
        print(varDeclIDAssignID.id)
        print(varDeclIDAssignID.id2)
        varDeclIDAssignID.expressao.accept(self)

    def visitVarDeclIDAssignList(self, varDeclIDAssignList):
        print(varDeclIDAssignList.tipo)
        print(varDeclIDAssignList.id)
        varDeclIDAssignList.listexp.accept(self)
  
    def visitVarDeclIDAssignListTIPO(self, varDeclIDAssignListTIPO):
        print(varDeclIDAssignListTIPO.tipodecl)
        print(varDeclIDAssignListTIPO.id)
        print(varDeclIDAssignListTIPO.tipo1)
        print(varDeclIDAssignListTIPO.tipo2)
        varDeclIDAssignListTIPO.listexp.accept(self)
  
    def visitFuncDeclSignature(self, signature):
        signature.signature.accept(self)
        signature.body.accept(self)
  
    def visitSignatureFunc(self, signatureFunc):
        print(signatureFunc.id)
        signatureFunc.sigParams.accept(self)

    def VisitFuncParametrosID(self, funcParametrosID):
        print(funcParametrosID.tipo)
        print(funcParametrosID.id)

    def VisitFuncParametrosIDList(self, funcParametrosIDList):
        print(funcParametrosIDList.tipo)
        print(funcParametrosIDList.id)
        funcParametrosIDList.funcParametros.accept(self)
  
    def visitBodyComandos(self, BodyComandos):
        BodyComandos.comandos.accept(self)

    def visitBodyOrComando(self, BodyOrComando):
        BodyOrComando.body.accept(self)

    def visitBodyOrComando2(self, BodyOrComando2):
        BodyOrComando2.comando.accept(self)

    def visitSingleComando(self, singleComando):
        singleComando.comando.accept(self)

    def visitCompoundComando(self, CompoundComando):
        CompoundComando.comando.accept(self)
        CompoundComando.comandos.accept(self)

    def visitComandoExpressao(self, ComandoExpressao):
        ComandoExpressao.expressao.accept(self)

    def visitComandoVarDecl(self, ComandoVarDecl):
        ComandoVarDecl.vardecl.accept(self)

    def visitComandoWhile(self, ComandoWhile):
        ComandoWhile.expressao.accept(self)
        ComandoWhile.bodyorcomando.accept(self)

    def visitComandoReturn(self, ComandoReturn):
        ComandoReturn.expressao.accept(self)

    def visitComandoIf(self, ComandoIf):
        ComandoIf.expressao.accept(self)
        ComandoIf.bodyorcomando.accept(self)

    def visitComandoIfElse(self, ComandoIfElse):
        ComandoIfElse.expressao.accept(self)
        ComandoIfElse.bodyorcomando1.accept(self)
        ComandoIfElse.bodyorcomando2.accept(self)

    def visitComandoFor(self, ComandoFor):
        ComandoFor.expressao1.accept(self)
        ComandoFor.expressao2.accept(self)
        ComandoFor.expressao3.accept(self)
        ComandoFor.bodyorcomando.accept(self)

    def visitExpressaoPlus(self, ExpressaoPlus):
        ExpressaoPlus.expressao1.accept(self)
        print('+')
        ExpressaoPlus.expressao2.accept(self)

    def visitExpressaoMinus(self, ExpressaoMinus):
        ExpressaoMinus.expressao1.accept(self)
        print('-')
        ExpressaoMinus.expressao2.accept(self)

    def visitExpressaoMult(self, ExpressaoMult):
        ExpressaoMult.expressao1.accept(self)
        print('*')
        ExpressaoMult.expressao2.accept(self)

    def visitExpressaoDiv(self, ExpressaoDiv):
        ExpressaoDiv.expressao1.accept(self)
        print('/')
        ExpressaoDiv.expressao2.accept(self)

    def visitExpressaoMod(self, ExpressaoMod):
        ExpressaoMod.expressao1.accept(self)
        print('%')
        ExpressaoMod.expressao2.accept(self)

    def visitExpressaoIncrement(self, ExpressaoIncrement):
        ExpressaoIncrement.expressao.accept(self)
        print('++')

    def visitExpressaoDecrement(self, ExpressaoDecrement):
        ExpressaoDecrement.expressao.accept(self)
        print('--')

    def visitExpressaoExpo(self, ExpressaoExpo):
        ExpressaoExpo.expressao1.accept(self)
        print('**')
        ExpressaoExpo.expressao2.accept(self)

    def visitExpressaoIncrementn(self, ExpressaoIncrementn):
        ExpressaoIncrementn.expressao1.accept(self)
        print('+=')
        ExpressaoIncrementn.expressao2.accept(self)

    def visitExpressaoDecrementn(self, ExpressaoDecrementn):
        ExpressaoDecrementn.expressao1.accept(self)
        print('-=')
        ExpressaoDecrementn.expressao2.accept(self)

    def visitMultIncrementoExp(self, ExpressaoMultincrement):
        ExpressaoMultincrement.expressao1.accept(self)
        print('*=')
        ExpressaoMultincrement.expressao2.accept(self)

    def visitExpressaoDivideincrement(self, ExpressaoDivideincrement):
        ExpressaoDivideincrement.expressao1.accept(self)
        print('/=')
        ExpressaoDivideincrement.expressao2.accept(self)

    def visitExpressaoModincrement(self, ExpressaoModincrement):
        ExpressaoModincrement.expressao1.accept(self)
        print('%=')
        ExpressaoModincrement.expressao2.accept(self)

    def visitExpressaoEqual(self, ExpressaoEqual):
        ExpressaoEqual.expressao1.accept(self)
        print('==')
        ExpressaoEqual.expressao2.accept(self)

    def visitExpressaoEEQ(self, ExpressaoEEQ):
        ExpressaoEEQ.expressao1.accept(self)
        print('===')
        ExpressaoEEQ.expressao2.accept(self)

    def visitExpressaoNotEqual(self, ExpressaoNotEqual):
        ExpressaoNotEqual.expressao1.accept(self)
        print('!=')
        ExpressaoNotEqual.expressao2.accept(self)

    def visitExpressaoNNEQ(self, ExpressaoNNEQ):
        ExpressaoNNEQ.expressao1.accept(self)
        print('!==')
        ExpressaoNNEQ.expressao2.accept(self)

    def visitExpressaoGreater(self, ExpressaoGreater):
        ExpressaoGreater.expressao1.accept(self)
        print('>')
        ExpressaoGreater.expressao2.accept(self)

    def visitExpressaoGreaterEqual(self, ExpressaoGreaterEqual):
        ExpressaoGreaterEqual.expressao1.accept(self)
        print('>=')
        ExpressaoGreaterEqual.expressao2.accept(self)

    def visitExpressaoLess(self, ExpressaoLess):
        ExpressaoLess.expressao1.accept(self)
        print('<')
        ExpressaoLess.expressao2.accept(self)

    def visitExpressaoLessEqual(self, ExpressaoLessEqual):
        ExpressaoLessEqual.expressao1.accept(self)
        print('<=')
        ExpressaoLessEqual.expressao2.accept(self)

    def visitExpressaoAnd(self, ExpressaoAnd):
        ExpressaoAnd.expressao1.accept(self)
        print('&&')
        ExpressaoAnd.expressao2.accept(self)

    def visitExpressaoOr(self, ExpressaoOr):
        ExpressaoOr.expressao1.accept(self)
        print('||')
        ExpressaoOr.expressao2.accept(self)

    def ExpressaoNOT(self, ExpressaoNOT):
        print('!')
        ExpressaoNOT.expressao.accept(self)

    def visitExpressaoFIM(self, ExpressaoFIM):
        ExpressaoFIM.expressao1.accept(self)
        print('?')
        ExpressaoFIM.expressao2.accept(self)
        print(':')
        ExpressaoFIM.expressao3.accept(self)

    def visitExpressaoAssign(self, ExpressaoAssign):
        ExpressaoAssign.assign.accept(self)

    def visitExpressaoInt(self, ExpressaoInt):
        print(ExpressaoInt.float)

    def visitRealExp(self, ExpressaoFloat):
        print(ExpressaoFloat.int)

    def visitExpressaoID(self, ExpressaoID):
        print(ExpressaoID.id)

    def visitExpressaoString(self, ExpressaoString):
        ExpressaoString.string.accept(self)

    def visitExpressaoCall(self, ExpressaoCall):
        ExpressaoCall.id.accept(self)

    def visitExpressaoBool(self, EspressaoBool):
        print(EspressaoBool.bool)

    def visitExpOpexp( self, expOpexp):
        expOpexp.expressao.accept(self)

    def visitSingleListexp(self, listexp):
        listexp.expressao.accept(self)

    def CompoundListexp(self, listexp):
        listexp.expressao.accept(self)
        print(',')
        listexp.listexp.accept(self)

    def visitParamsCall(self, paramsCall):
        print(paramsCall.id)
        paramsCall.params.accept(self)

    def visitNoParamsCall(self, paramsCall):
        print(paramsCall.id)
        print( '()')

    def visitSingleParams(self, params):
        params.expressao.accept(self)

    def visitCompoundParams(self, params):
        params.expressao.accept(self)
        print(', ')
        params.params.accept(self)

    def visitAssignAssign(self, assign):
        print(assign.id)
        print('=')
        assign.expressao.accept(self)

    def visittipodecl(self, tipodecl):
        print(tipodecl.tipo)

    def visittipodecltipo(self, tipodecltipo):
        print(tipodecltipo.tipo)
        print(tipodecltipo.tipo2)
  
    def visitstring(self, string):
        print(string.string)

    data2 = '''
    function some (a: number, b: number): number { 
        a = 88 + 44; 
        b = 70; 
        sumparabola(1, 2, 3); 
        if (b==70){     
            while (true){ 
                c = 38; 
                sumparabola(5, true, false); 
                while (c){ 
                    sumparabola(5, true, true); 
                } 
            }
        } 
        soma(); 
        sumparabolac(2); 
        return true; 
    }
    {
        let a: number = 1;
    }
    '''
    lexer = lex.lex()
    lexer.input(data2)
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    for r in result:
        r.accept(visitor)