##Rascunho da gramática
##programa -> funcdecl | funcdecl programa | vardecl ; | vardecl ; programa
##funcdecl -> signature body
##vardecl -> tipodecl ID : tipo | tipodecl ID : tipo = expressao | tipodecl ID : tipo = ID | tipodecl ID : tipo [ ] = [ ] | tipodecl ID : tipo [ ] = [ listexp ] | tipodecl ID : ( tipo | tipo ) [ ] = [ listexp ]
##signature -> tipofunc ID ( funcparametros ) : tipo body
##body -> { comandos }
##tipofunc -> FUNCTION | CONST
##funcparametros -> ID : tipo , funcparametros | ID : tipo
##comandos -> comando | comando comandos
##comando -> vardecl ; | expressao ; | while ( expressao ) bodyorcomando | return expressao ; | if ( expressao ) bodyorexpressao | if ( expressao ) bodyorcomando else bodyorcomando | for ( opexp ; opexp ; opexp) bodyorcomando
##opexp -> expressao | VOID
##bodyorcomando -> body | comando
##expressao -> expressao + expressao | expressao - expressao | expressao * expressao | expressao / expressao | expressao % expressao | expressao && expressao | expressao || expressao | expressao == expressao | expressao != expressao | expressao < expressao | expressao > expressao | expressao <= expressao | expressao >= expressao | NINT | NFLOAT | string | call | assign | ID | TRUE | FALSE 
##call -> ID ( parametros ) | ID ( )
##parametros -> expressao , parametros | expressao
##assign -> ID = expressao
##tipodecl -> LET | VAR | CONST
##tipo -> STRING
##      | BOOLEAN
##      | NUMBER
##listexp -> expressao , listexp | expressao
##string -> STRINGD | STRINGS

# Definição das regras de produção
import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

# Regras da liguagem
precedence = (
    ('left', 'COMMA'),
    ('right', 'ASSIGN', 'INCREMENTN', 'DECREMENTN', 'TIMESINCREMENT', 'DIVIDEINCREMENT', 'MODINCREMENT'),
    ('right', 'INTER', 'COLON'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ', 'EEQ', 'NNEQ'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'IN', 'INSTANCEOF'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'EXPO'),
    ('right', 'DECREMENT', 'INCREMENT', 'NOT'),
    ('left', 'LPAREN','RPAREN') 
)

# Regras da linguagem
def p_programa(p):
    '''programa : funcdecl'''
    p[0] = sa.ProgramaFuncDecl(p[1])

def p_programaFuncDeclPrograma(p):
    '''programa : funcdecl programa'''
    p[0] = sa.programaFuncDeclPrograma(p[1], p[2])

def p_programaComandos(p):
    '''programa : comandos'''
    p[0] = sa.programaComandos(p[1])

def p_programaComandosPrograma(p):
    '''programa : comandos programa'''
    p[0] = sa.programaComandosPrograma(p[1], p[3])

def p_vardecl(p):
    '''vardecl : tipodecl ID COLON tipo'''
    p[0] = sa.varDeclID(p[1], p[2])
  
def p_vardecl2(p):
    '''vardecl : tipodecl ID COLON tipo ASSIGN expressao'''
    p[0] = sa.varDeclIDAssign(p[1], p[2], p[6])
  
def p_vardecl3(p):
  '''vardecl : tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET RBRACKET'''
  p[0] = sa.varDeclIDAssignList(p[1], p[2], None)
  
def p_vardecl4(p):
  '''vardecl : tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET listexp RBRACKET'''
  p[0] = sa.varDeclIDAssignList(p[1], p[2], p[9])

def p_vardecl5(p):
  '''vardecl : tipodecl ID COLON LPAREN tipo BAR tipo RPAREN RBRACKET LBRACKET RBRACKET ASSIGN LBRACKET listexp RBRACKET'''
  p[0] = sa.varDeclIDAssignListTIPO(p[1], p[2], p[5], p[7], p[14])
                                        
def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.funcDeclSignature(p[1], p[2])
  
def p_signature1(p):
    '''signature : tipofunc ID LPAREN funcparametros RPAREN COLON tipo body'''
    p[0] = sa.signatureFunc(p[1], p[2], p[4], p[7], p[8])
  
def p_signature2(p):
    '''signature : tipofunc ID LPAREN funcparametros RPAREN COLON tipo SEMICOLON'''
    p[0] = sa.signatureFunc(p[1], p[2], p[4], p[7], None)

def p_body(p): 
    '''body : LBRACE comandos RBRACE'''
    p[0] = sa.BodyComandos(p[2])

def p_tipofunc(p):
    '''tipofunc : FUNCTION
                | CONST
    '''
    p[0] = sa.tipo(p[1])

def p_funcparametros(p):
    '''funcparametros : ID COLON tipo COMMA funcparametros
                 | ID COLON tipo'''
    if len(p) == 6:
        p[0] = sa.funcParametrosIDList(p[1], p[3], p[5])
    else:
        p[0] = sa.funcParametrosID(p[1], p[3])
 
def p_comandos(p):
    '''comandos : comando
            | comando comandos'''
    if len(p) == 2:
        p[0] = sa.singleComando(p[1])
    else:
        p[0] = sa.CompoundComando(p[1], p[2])

def p_comando(p):
    '''comando :  RETURN expressao SEMICOLON'''
    p[0] = sa.ComandoReturn(p[2])

def p_comando1(p):
    '''comando : expressao SEMICOLON'''
    p[0] = sa.ComandoExpressao(p[1])

def p_comandoWHILE(p):
    '''comando : WHILE LPAREN expressao RPAREN bodyorcomando'''
    p[0] = sa.ComandoWhile(p[3], p[5])

def p_comandopIF(p):
    '''comando : IF LPAREN expressao RPAREN bodyorcomando'''
    p[0] = sa.ComandoIf(p[3], p[5])

def p_comandoIFELSE(p):
    '''comando : IF LPAREN expressao RPAREN bodyorcomando ELSE bodyorcomando'''
    p[0] = sa.ComandoIfElse(p[3], p[5], p[7])

def p_comandoFOR(p):
    '''comando : FOR LPAREN opexp SEMICOLON opexp SEMICOLON opexp RPAREN bodyorcomando'''
    p[0] = sa.ComandoFor(p[3], p[5], p[7], p[9])

def p_opexp(p):
    '''opexp : expressao
             | VOID
    '''
    if isinstance(p[1], sa.exp):
        p[0] = sa.ExpOpexp(p[1])
    else:
        p[0] = sa.ExpOpexp(None)

def p_bodyorcomando(p):
    '''bodyorcomando : body
                     | comando
    '''
    if isinstance(p[1], sa.body):
        p[0] = sa.BodyOrComando(p[1])
    else:
        p[0] = sa.BodyOrComando2(p[1])

##expressao
def p_expressaoPLUS(p):
    '''expressao : expressao PLUS expressao'''
    p[0] = sa.ExpressaoPlus(p[1], p[3])

def p_expressaoMINUS(p):
    '''expressao : expressao MINUS expressao'''
    p[0] = sa.ExpressaoMinus(p[1], p[3])

def p_expressaoTIMES(p):
    '''expressao : expressao TIMES expressao'''
    p[0] = sa.ExpressaoMult(p[1], p[3])

def p_expressaoDIVIDE(p):
    '''expressao : expressao DIVIDE expressao'''
    p[0] = sa.ExpressaoDiv(p[1], p[3])

def p_expressaoMOD(p):
    '''expressao : expressao MOD expressao'''
    p[0] = sa.ExpressaoMod(p[1], p[3])

def p_expressaoOR(p):
    '''expressao : expressao OR expressao'''
    p[0] = sa.ExpressaoOr(p[1], p[3])

def p_expressaoAND(p):
    '''expressao : expressao AND expressao'''
    p[0] = sa.ExpressaoAnd(p[1], p[3])

def p_expressaoEQ(p):
    '''expressao : expressao EQ expressao'''
    p[0] = sa.ExpressaoEqual(p[1], p[3])

def p_expressaoNEQ(p):
    '''expressao : expressao NEQ expressao'''
    p[0] = sa.ExpressaoNotEqual(p[1], p[3])

def p_expressaoGE(p):
    '''expressao : expressao GE expressao'''
    p[0] = sa.ExpressaoGreaterEqual(p[1], p[3])

def p_expressaoLE(p):
    '''expressao : expressao LE expressao'''
    p[0] = sa.ExpressaoLessEqual(p[1], p[3])

def p_expressaoLT(p):
    '''expressao : expressao LT expressao'''
    p[0] = sa.ExpressaoLess(p[1], p[3])

def p_expressaoGT(p):
    '''expressao : expressao GT expressao'''
    p[0] = sa.ExpressaoGreater(p[1], p[3])

def p_expressaoINCREMENT(p):
    '''expressao : expressao INCREMENT'''
    p[0] = sa.ExpressaoIncrement(p[1])

def p_expressaoEXPO(p):
    '''expressao : expressao EXPO expressao'''
    p[0] = sa.ExpressaoExpo(p[1], p[3])

def p_expressaoDECREMENT(p):
    '''expressao : expressao DECREMENT'''
    p[0] = sa.ExpressaoDecrement(p[1])

def p_expressaoINCREMENTN(p):
    '''expressao : INCREMENTN expressao'''
    p[0] = sa.ExpressaoIncrementn(p[2])

def p_expressaoDECREMENTN(p):
    '''expressao : DECREMENTN expressao'''
    p[0] = sa.ExpressaoDecrementn(p[2])

def p_expressaoTIMESINCREMENT(p):
    '''expressao : expressao TIMESINCREMENT expressao'''
    p[0] = sa.ExpressaoMultincrement(p[1], p[3])

def p_expressaoDIVIDEINCREMENT(p):
    '''expressao : expressao DIVIDEINCREMENT expressao'''
    p[0] = sa.ExpressaoDivideincrement(p[1], p[3])

def p_expressaoMODINCREMENT(p):
    '''expressao : expressao MODINCREMENT expressao'''
    p[0] = sa.ExpressaoModincrement(p[1], p[3])

def p_expressaoEEQ(p):
    '''expressao : expressao EEQ expressao'''
    p[0] = sa.ExpressaoEEQ(p[1], p[3])

def p_expressaoVardecl(p):
    '''expressao : vardecl'''
    p[0] = sa.ExpressaoVarDecl(p[1])

def p_expressaoNNEQ(p):
    '''expressao : expressao NNEQ expressao'''
    p[0] = sa.ExpressaoNNEQ(p[1], p[3])

def p_expressaoFIM(p):
    '''expressao : expressao INTER expressao INTER expressao'''
    p[0] = sa.ExpressaoFIM(p[1], p[3], p[5])

def p_expressaoNINT(p):
    '''expressao : NINT'''
    p[0] = sa.ExpressaoInt(p[1])

def p_expressaoNFLOAT(p):
    '''expressao : NFLOAT'''
    p[0] = sa.ExpressaoFloat(p[1])

def p_expressaostring(p):
    '''expressao : string'''
    p[0] = sa.ExpressaoString(p[1])

def p_expressaocall(p):
    '''expressao : call'''
    p[0] = sa.ExpressaoCall(p[1])

def p_expressaoassign(p):
    '''expressao : assign'''
    p[0] = sa.ExpressaoAssign(p[1])

def p_expressaoID(p):
    '''expressao : ID'''
    p[0] = sa.ExpressaoID(p[1])

def p_expressaoBOOLEAN(p):
    '''expressao : FALSE
           | TRUE'''
    p[0] = sa.EspressaoBool(p[1])

def p_expressaoNOT(p):
    '''expressao : NOT expressao'''
    p[0] = sa.ExpressaoNOT(p[2])

def p_call(p): 
    '''call : ID LPAREN parametros RPAREN
            | ID LPAREN RPAREN
    '''
    if len(p) == 5:
        p[0] = sa.ParamsCall(p[1], p[3])
    else:
        p[0] = sa.NoParamsCall(p[1])

def p_parametros(p):
    '''parametros : expressao COMMA parametros
                  | expressao
    '''
    if len(p) == 4:
        p[0] = sa.CompoundParams(p[1], p[3])
    else:
        p[0] = sa.SingleParams(p[1])

def p_assign(p):
    '''assign : ID ASSIGN expressao
    '''
    p[0] = sa.AssignAssign(p[1], p[3])

def p_tipodecl(p):
    '''tipodecl : LET
                | VAR
                | CONST tipo
    '''
    if len(p) == 3:
      p[0] = sa.tipodecltipo(p[1], p[2])
    else:
      p[0] = sa.tipodecl(p[1])

def p_tipo(p):
    '''tipo : STRING
            | NUMBER
            | BOOLEAN
    '''
    p[0] = sa.tipo(p[1])

def p_listexp(p):
    '''listexp : expressao 
               | expressao COMMA listexp
    '''
    if len(p) == 4:
        p[0] = sa.CompoundListexp(p[1], p[3])
    else:
        p[0] = sa.SingleListexp(p[1])
  

def p_string(p):
    '''string : STRINGD
              | STRINGS
    '''
    p[0] = sa.string(p[1])

def p_error(p):
    print("Syntax error in input! %s" % p)


# Build the parser
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
result = parser.parse(debug=True)

