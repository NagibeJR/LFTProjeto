import ply.lex as lex

#lista global criada para armazenar os retornos do algoritmo

saidas = []

#função para adicionar as classificações dos tokens para ser impressa pelo compilador
def add_lista_saida(t,erro):
  saidas.append((t.lineno,t.type,t.value,erro))

#linguagem léxica de TypeScript

#palavras reservadas

reserved = {
'as' : 'AS',
'boolean': 'BOOLEAN',
'break': 'BREAK',
'case': 'CASE',
'catch': 'CATCH',
'class': 'CLASS',
'const': 'CONST',
'continue': 'CONTINUE',
'debugger': 'DEBUGGER',
'declare': 'DECLARE',
'default': 'DEFAULT',
'delete': 'DELETE',
'do': 'DO',
'else': 'ELSE',
'enum': 'ENUM',
'export': 'EXPORT',
'extends': 'EXTENDS',
'false': 'FALSE',
'finally': 'FINALLY',
'for': 'FOR',
'from': 'FROM',
'function': 'FUNCTION',
'get': 'GET',
'if': 'IF',
'implements': 'IMPLEMENTS',
'import': 'IMPORT',
'in': 'IN',
'infer': 'INFER',
'instanceof': 'INSTANCEOF',
'interface': 'INTERFACE',
'is': 'IS',
'keyof': 'KEYOF',
'let': 'LET',
'module': 'MODULE',
'namespace': 'NAMESPACE',
'never': 'NEVER',
'new': 'NEW',
'null': 'NULL',
'object': 'OBJECT',
'package': 'PACKAGE',
'private': 'PRIVATE',
'protected': 'PROTECTED',
'public': 'PUBLIC',
'readonly': 'READONLY',
'require': 'REQUIRE',
'return': 'RETURN',
'set': 'SET',
'static': 'STATIC',
'super': 'SUPER',
'switch': 'SWITCH',
'symbol': 'SYMBOL',
'this': 'THIS',
'throw': 'THROW',
'true': 'TRUE',
'try': 'TRY',
'type': 'TYPE',
'typeof': 'TYPEOF',
'unique': 'UNIQUE',
'unknown': 'UNKNOWN',
'var': 'VAR',
'void': 'VOID',
'while': 'WHILE',
'with': 'WITH',
'yield': 'YIELD',
}

tokens = [
    'IDENTIFIER',
    'NUMBER',
    'STRING',
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
] + list (reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
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


# Regra para identificadores
def t_IDENTIFIER(t):
    r'[a-zA-Z_$][a-zA-Z0-9_$]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


# Regra para números
def t_NUMBER(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t


# Regra para strings
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    return t

def strings(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    return t

# Regra para ignorar espaços em branco e tabulações
t_ignore = ' \t'


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
  
def t_commentmulti(t):
    r'/\*.*\*/'
    pass
  
def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
  
def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t
  
def t_octal(t):
    r'0o[0-7]+'
    t.value = int(t.value, 8)
    return t 
  
def t_hexadecimal(t):
    r'0x[0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t
  
def t_true(t):
    r'true'
    t.value = True
    return t
  
def t_fale(t):
    r'false'
    t.value = False
    return t
  
def t_null(t):
    r'null'
    t.value = None
    return t

def t_branco(t):
    r'[\t ]+'
    pass

lexer = lex.lex()
  