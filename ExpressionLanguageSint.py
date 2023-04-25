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

import ply.yacc as yacc
from ExpressionLanguageLex import *

# Regras da liguagem
# Definindo a regra de precedência

def p_program(p):
    """
    program : statement
    """
    p[0] = p[1]
  
def p_statement(p):
    '''
    statement : IDENTIFIER ASSIGN expression SEMICOLON
              | IF LPAREN expression RPAREN statement
              | IF LPAREN expression RPAREN statement ELSE statement
              | WHILE LPAREN expression RPAREN statement
              | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement
              | FUNCTION IDENTIFIER LPAREN params RPAREN block
              | CLASS IDENTIFIER block
    '''

def p_params(p):
    '''
    params : IDENTIFIER
           | IDENTIFIER COMMA params
    '''

def p_block(p):
    '''
    block : LBRACE RBRACE
          | LBRACE statements RBRACE
    '''

def p_statements(p):
    '''
    statements : statement
               | statement statements
    '''

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MOD expression
               | LPAREN expression RPAREN
               | expression EQ expression
               | expression NEQ expression
               | expression LT expression
               | expression LE expression
               | expression GT expression
               | expression GE expression
               | expression AND expression
               | expression OR expression
               | NOT expression
               | NUMBER
               | STRING
               | TRUE
               | FALSE
               | NULL
               | IDENTIFIER
               | IDENTIFIER LPAREN args RPAREN
               | NEW IDENTIFIER LPAREN RPAREN
    '''

def p_args(p):
    '''
    args : expression
         | expression COMMA args
    '''


parser = yacc.yacc()

