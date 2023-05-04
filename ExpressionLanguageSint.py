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
    '''
    programa : funcdecl
             | funcdecl programa
             | vardecl SEMICOLON
             | vardecl SEMICOLON programa
    '''
    if(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
    elif(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_funcdecl(p):
    '''
    funcdecl : signature body
    '''

def p_vardecl(p):
    '''vardecl : tipodecl ID COLON tipo
               | tipodecl ID COLON tipo ASSIGN expressao
               | tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET RBRACKET
               | tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET listexp RBRACKET
               | tipodecl ID COLON tipo LPAREN tipo RBRACKET ASSIGN LBRACKET listexp RBRACKET
    '''
  
def p_signature(p):
    '''signature : tipofunc ID LPAREN funcparametros RPAREN COLON tipo body
                 | tipofunc ID LPAREN funcparametros RPAREN COLON tipo SEMICOLON
    '''

def p_body(p):
    '''body : LBRACE comandos RBRACE
    '''

def p_tipofunc(p):
    '''tipofunc : FUNCTION
                | CONST
    '''

def p_funcparametros(p):
    '''funcparametros : ID COLON tipo COMMA funcparametros
                      | ID COLON tipo
    '''

def p_comandos(p):
    '''comandos : comando
                | comando comandos
    '''

def p_comando(p):
    '''comando : vardecl SEMICOLON
               | expressao SEMICOLON
               | WHILE LPAREN expressao RPAREN bodyorcomando
               | RETURN expressao SEMICOLON
               | IF LPAREN expressao RPAREN bodyorcomando 
               | IF LPAREN expressao RPAREN bodyorcomando ELSE bodyorcomando
               | FOR LPAREN opexp SEMICOLON opexp SEMICOLON opexp RPAREN bodyorcomando
    '''

def p_opexp(p):
    '''opexp : expressao
             | VOID
    '''

def p_bodyorcomando(p):
    '''bodyorcomando : body
                     | comando
    '''


def p_expressao(p):
    '''expressao : expressao PLUS expressao
                 | expressao MINUS expressao
                 | expressao TIMES expressao
                 | expressao DIVIDE expressao
                 | expressao MOD expressao
                 | expressao AND expressao
                 | expressao OR expressao
                 | expressao EQ expressao
                 | expressao NEQ expressao
                 | expressao LT expressao
                 | expressao GT expressao
                 | expressao LE expressao
                 | expressao GE expressao
                 | expressao INCREMENT 
                 | expressao EXPO expressao 
                 | expressao DECREMENT
                 | expressao INCREMENTN expressao
                 | expressao DECREMENTN expressao
                 | expressao TIMESINCREMENT expressao
                 | expressao DIVIDEINCREMENT expressao
                 | expressao MODINCREMENT expressao
                 | expressao EEQ expressao
                 | expressao NNEQ expressao
                 | expressao INTER expressao COLON expressao 
                 | NINT
                 | NFLOAT
                 | string
                 | call
                 | assign
                 | ID
                 | TRUE
                 | FALSE
    '''

def p_call(p): 
    '''call : ID LPAREN parametros RPAREN
            | ID LPAREN RPAREN
    '''

def p_parametros(p):
    '''parametros : expressao COMMA parametros
                  | expressao
    '''

def p_assign(p):
    '''assign : ID ASSIGN expressao
    '''

def p_tipodecl(p):
    '''tipodecl : LET
                | VAR
                | CONST tipo
    '''

def p_tipo(p):
    '''tipo : STRING
            | NUMBER
            | BOOLEAN
    '''

def p_listexp(p):
    '''listexp : expressao 
               | expressao COMMA listexp
    '''

def p_string(p):
    '''string : STRINGD
              | STRINGS
    '''

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

