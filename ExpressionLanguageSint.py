# Rascunho da gramatica
## statement : IDENTIFIER ASSIGN expression SEMICOLON
##           | IF LPAREN expression RPAREN statement
##           | IF LPAREN expression RPAREN statement ELSE statement
##           | WHILE LPAREN expression RPAREN statement
##           | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement
##           | FUNCTION IDENTIFIER LPAREN params RPAREN block
##           | CLASS IDENTIFIER block

## params : IDENTIFIER
##        | IDENTIFIER COMMA params

## block : LBRACE RBRACE
##       | LBRACE statements RBRACE

## statements : statement
##            | statement statements

## expression : expression PLUS expression
##            | expression MINUS expression
##            | expression TIMES expression
##            | expression DIVIDE expression
##            | expression MOD expression
##            | LPAREN expression RPAREN
##            | expression EQ expression
##            | expression NEQ expression
##            | expression LT expression
##            | expression LE expression
##            | expression GT expression
##            | expression GE expression
##            | expression AND expression
##            | expression OR expression
##            | NOT expression
##            | NUMBER
##            | STRING
##            | TRUE
##            | FALSE
##            | NULL
##            | IDENTIFIER
##            | IDENTIFIER LPAREN args RPAREN
##            | NEW IDENTIFIER LPAREN RPAREN

## args : expression
##      | expression COMMA args



# Definição das regras de produção
import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *

# Regras da liguagem
# Definindo a regra de precedência
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('right', 'NOT')
)

# Define a função program que representa a regra inicial da gramática
def p_program(p):
    'program : statements'
    p[0] = ('program', p[1])

# Define a função statements que representa uma lista de statements
def p_statements(p):
    '''
    statements : statement
               | statement statements
    '''
    if len(p) == 2:
        p[0] = ('statements', [p[1]])
    else:
        p[0] = ('statements', [p[1]] + p[2][1])

# Define a função statement para cada uma das produções da gramática
def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_statement_if(p):
    '''
    statement : IF LPAREN expression RPAREN statement
              | IF LPAREN expression RPAREN statement ELSE statement
    '''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if-else', p[3], p[5], p[7])

def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN statement'
    p[0] = ('while', p[3], p[5])

def p_statement_for(p):
    'statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_statement_function(p):
    'statement : FUNCTION IDENTIFIER LPAREN params RPAREN block'
    p[0] = ('function', p[2], p[4], p[6])

def p_statement_class(p):
    'statement : CLASS IDENTIFIER block'
    p[0] = ('class', p[2], p[3])

# Define a função params que representa uma lista de parâmetros
def p_params(p):
    '''
    params : IDENTIFIER
           | IDENTIFIER COMMA params
    '''
    if len(p) == 2:
        p[0] = ('params', [p[1]])
    else:
        p[0] = ('params', [p[1]] + p[3][1])

# Define a função block que representa um bloco de statements
def p_block(p):
    '''
    block : LBRACE statements RBRACE
          | LBRACE RBRACE
    '''
    if len(p) == 4:
        p[0] = ('block', p[2])
    else:
        p[0] = ('block', [])

# Define a função expression que representa uma expressão

def p_expression_binary(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MOD expression
               | expression EQ expression
               | expression NEQ expression
               | expression LT expression
               | expression LE expression
               | expression GT expression
               | expression GE expression
               | expression AND expression
               | expression OR expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_unary(p):
    '''
    expression : NOT expression
    '''
    p[0] = ('NOT', p[2])

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

def p_expression_value(p):
    '''
    expression : NUMBER
               | STRING
               | TRUE
               | FALSE
               | NULL
               | IDENTIFIER
               | IDENTIFIER LPAREN args RPAREN
               | NEW IDENTIFIER LPAREN RPAREN
    '''
    p[0] = p[1]

def p_args(p):
    '''
    args : expression
         | expression COMMA args
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a entrada '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe: fim inesperado do arquivo")

data2 = '''
function some (a, b){ 
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
'''
lexer = lex.lex()
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=True)

