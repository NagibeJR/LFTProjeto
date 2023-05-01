import ply.lex as lex

#lista global criada para armazenar os retornos do algoritmo

#linguagem léxica de TypeScript

#palavras reservadas

reserved = {
    'abstract' : 'ABSTRACT',
    'any' : 'ANY', 
    'as' : 'AS', 
    'asserts' : 'ASSERTS', 
    'async': 'ASYNC', 
    'await' : 'AWAIT', 
    'boolean' : 'BOOLEAN', 
    'break' : 'BREAK',
    'case' : 'CASE',
    'catch' : 'CATCH',
    'class' : 'CLASS',
    'const' : 'CONST',
    'constructor' : 'CONSTRUCTOR',
    'continue' : 'CONTINUE',
    'debugger' : 'DEBUGGER', 
    'declare' : 'DECLARE',
    'default' : 'DEFAULT',
    'delete' : 'DELETE',
    'do' : 'DO',
    'else' : 'ELSE',
    'enum' : 'ENUM',
    'export' : 'EXPORT',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'finally' : 'FINALLY',
    'for' : 'FOR',
    'from' : 'FROM',
    'function' : 'FUNCTION',
    'get' : 'GET',
    'global' : 'GLOBAL',
    'if' : 'IF',
    'implements' : 'IMPLEMENTS',
    'import' : 'IMPORT',
    'in' : 'IN',
    'infer' : 'INFER',
    'instanceof' : 'INSTANCEOF',
    'interface' : 'INTERFACE',
    'internal' : 'INTERNAL',
    'is' : 'IS',
    'keyof' : 'KEYOF',
    'let' : 'LET',
    'module' : 'MODULE',
    'namespace' : 'NAMESPACE',
    'never' : 'NEVER',
    'new' : 'NEW',
    'null' : 'NULL',
    'number' : 'NUMBER',
    'object' : 'OBJECT',
    'of' : 'OF',
    'package' : 'PACKAGE',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'readonly' : 'READONLY',
    'require' : 'REQUIRE',
    'return' : 'RETURN',
    'set' : 'SET',
    'static' : 'STATIC',
    'string' : 'STRING',
    'super' : 'SUPER',
    'switch' : 'SWITCH',
    'symbol' : 'SYMBOL',
    'this' : 'THIS',
    'throw' : 'THROW',
    'true' : 'TRUE',
    'try' : 'TRY',
    'type' : 'TYPE',
    'typeof' : 'TYPEOF',
    'undefined' : 'UNDEFINED',
    'unique' : 'UNIQUE',
    'unknown' : 'UNKNOWN',
    'var' : 'VAR',
    'void' : 'VOID',
    'while' : 'WHILE',
    'with' : 'WITH',
    'yield' : 'YIELD',
}

tokens = [
    'ID',
    'NINT',
    'NFLOAT',
    'STRINGD',
    'STRINGS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',
    'ASSIGN',
    'EQ',
    'NEQ',
    'LT',
    'LE',
    'GT',
    'GE',
    'AND',
    'OR',
    'NOT',
    'COMMENTMULTI',
    'COMMENT',
    'OCTAL',
    'HEXADECIMAL',
    'ASPASSIMPLES',
    'ASPASDUPLAS',
] + list (reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = '\['
t_RBRACKET = '\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASPASSIMPLES = r'\''
t_ASPASDUPLAS = r'\"'


# Regra para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# Regra para float
def t_NFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
# Regra para int
def t_NINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para strings
def t_STRINGD(t):
    r'[\"][^\"\n][\"]'

def t_STRINGS(t):
    r'[\'][^\'\n][\']'

# Regra para lidar com quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

  
# Regra para lidar com erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)
  
def t_COMMENT(t):
    r'//.*\n'
    pass
  
def t_COMMENTMULTI(t):
    r'/\*.*\*/'
    pass
  
def t_OCTAL(t):
    r'0o[0-7]+'
    t.value = int(t.value, 8)
    return t 
  
def t_HEXADECIMAL(t):
    r'0x[0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t
  
def t_TRUE(t):
    r'true'
    t.value = True
    return t
  
def t_FALSE(t):
    r'false'
    t.value = False
    return t
  
def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_BRANCO(t):
    r'[\t ]+'
    pass