
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMArightASSIGNINCREMENTNDECREMENTNTIMESINCREMENTDIVIDEINCREMENTMODINCREMENTrightINTERCOLONleftORleftANDleftEQNEQEEQNNEQleftLTLEGTGEININSTANCEOFleftPLUSMINUSleftTIMESDIVIDEMODrightEXPOrightDECREMENTINCREMENTNOTleftLPARENRPARENABSTRACT AND ANY AS ASSERTS ASSIGN ASYNC AWAIT BOOLEAN BREAK CASE CATCH CLASS COLON COMMA COMMENT COMMENTMULTI CONST CONSTRUCTOR CONTINUE DEBUGGER DECLARE DECREMENT DECREMENTN DEFAULT DELETE DIVIDE DIVIDEINCREMENT DO DOT DQUOTE EEQ ELSE ENUM EQ EXPO EXPORT EXTENDS FALSE FINALLY FOR FROM FUNCTION GE GET GLOBAL GT HEXADECIMAL ID IF IMPLEMENTS IMPORT IN INCREMENT INCREMENTN INFER INSTANCEOF INTER INTERFACE INTERNAL IS KEYOF LBRACE LBRACKET LE LET LPAREN LT MINUS MOD MODINCREMENT MODULE NAMESPACE NEQ NEVER NEW NFLOAT NINT NNEQ NOT NULL NUMBER OBJECT OCTAL OF OR PACKAGE PLUS PRIVATE PROTECTED PUBLIC RBRACE RBRACKET READONLY REQUIRE RETURN RPAREN SEMICOLON SET SQUOTE STATIC STRING STRINGD STRINGS SUPER SWITCH SYMBOL THIS THROW TIMES TIMESINCREMENT TRUE TRY TYPE TYPEOF UNDEFINED UNIQUE UNKNOWN VAR VOID WHILE WITH YIELDprograma : funcdeclprograma : funcdecl programaprograma : vardecl SEMICOLONprograma : vardecl SEMICOLON programavardecl : tipodecl ID COLON tipovardecl : tipodecl ID COLON tipo ASSIGN expressaovardecl : tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET RBRACKETvardecl : tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET listexp RBRACKETvardecl : tipodecl ID COLON tipo LPAREN tipo RBRACKET ASSIGN LBRACKET listexp RBRACKETfuncdecl : signature bodysignature : tipofunc ID LPAREN funcparametros RPAREN COLON tipo bodysignature : tipofunc ID LPAREN funcparametros RPAREN COLON tipo SEMICOLONbody : LBRACE comandos RBRACEtipofunc : FUNCTION\n                | CONST\n    funcparametros : ID COLON tipo COMMA funcparametros\n                 | ID COLON tipocomandos : comando\n            | comando comandoscomando : vardecl SEMICOLON\n           | RETURN expressao SEMICOLONcomando : expressao SEMICOLONcomando : WHILE LPAREN expressao RPAREN bodyorcomandocomando : IF LPAREN expressao RPAREN bodyorcomandocomando : IF LPAREN expressao RPAREN bodyorcomando ELSE bodyorcomandocomando : FOR LPAREN opexp SEMICOLON opexp SEMICOLON opexp RPAREN bodyorcomandoopexp : expressao\n             | VOID\n    bodyorcomando : body\n                     | comando\n    expressao : expressao PLUS expressaoexpressao : expressao MINUS expressaoexpressao : expressao TIMES expressaoexpressao : expressao DIVIDE expressaoexpressao : expressao MOD expressaoexpressao : expressao OR expressaoexpressao : expressao AND expressaoexpressao : expressao EQ expressaoexpressao : expressao NEQ expressaoexpressao : expressao GE expressaoexpressao : expressao LE expressaoexpressao : expressao LT expressaoexpressao : expressao GT expressaoexpressao : expressao INCREMENTexpressao : expressao EXPO expressaoexpressao : expressao DECREMENTexpressao : INCREMENTN expressaoexpressao : DECREMENTN expressaoexpressao : expressao TIMESINCREMENT expressaoexpressao : expressao DIVIDEINCREMENT expressaoexpressao : expressao MODINCREMENT expressaoexpressao : expressao EEQ expressaoexpressao : expressao NNEQ expressaoexpressao : expressao INTER expressao INTER expressaoexpressao : NINTexpressao : NFLOATexpressao : stringexpressao : callexpressao : assignexpressao : IDexpressao : FALSE\n           | TRUEexpressao : NOT expressaocall : ID LPAREN parametros RPAREN\n            | ID LPAREN RPAREN\n    parametros : expressao COMMA parametros\n                  | expressao\n    assign : ID ASSIGN expressao\n    tipodecl : LET\n                | VAR\n                | CONST tipo\n    tipo : STRING\n            | NUMBER\n            | BOOLEAN\n    listexp : expressao \n               | expressao COMMA listexp\n    string : STRINGD\n              | STRINGS\n    '
    
_lr_action_items = {'LET':([0,2,12,13,14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[7,7,7,-10,7,7,-13,-20,-22,-21,7,7,-23,-29,-30,-24,7,-25,7,-26,]),'VAR':([0,2,12,13,14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[8,8,8,-10,8,8,-13,-20,-22,-21,8,8,-23,-29,-30,-24,8,-25,8,-26,]),'CONST':([0,2,12,13,14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[9,9,9,-10,41,41,-13,-20,-22,-21,41,41,-23,-29,-30,-24,41,-25,41,-26,]),'FUNCTION':([0,2,12,13,46,],[10,10,10,-10,-13,]),'$end':([1,2,11,12,13,21,46,],[0,-1,-2,-3,-10,-4,-13,]),'SEMICOLON':([3,18,19,20,24,26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,109,111,113,123,125,130,135,140,150,155,160,],[12,-72,-73,-74,48,50,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,84,-44,-46,-47,-48,-63,-5,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-49,-50,-51,-52,-53,122,-27,-28,-65,-68,-64,-6,-54,142,147,-7,-8,-9,]),'LBRACE':([4,18,19,20,46,120,121,140,141,146,147,154,],[14,-72,-73,-74,-13,14,14,14,14,-11,-12,14,]),'ID':([5,6,7,8,9,10,14,17,18,19,20,23,25,31,32,40,45,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,139,141,142,143,148,153,154,156,158,],[15,16,-69,-70,-15,-14,30,-71,-72,-73,-74,30,30,30,30,30,82,-13,-20,-22,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-21,30,30,30,30,30,30,-23,-29,-30,-24,82,30,30,30,-25,30,30,30,-26,]),'STRING':([9,41,44,116,117,129,],[18,18,18,18,18,18,]),'NUMBER':([9,41,44,116,117,129,],[19,19,19,19,19,19,]),'BOOLEAN':([9,41,44,116,117,129,],[20,20,20,20,20,20,]),'RETURN':([14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[25,25,-13,-20,-22,-21,25,25,-23,-29,-30,-24,25,-25,25,-26,]),'WHILE':([14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[27,27,-13,-20,-22,-21,27,27,-23,-29,-30,-24,27,-25,27,-26,]),'IF':([14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[28,28,-13,-20,-22,-21,28,28,-23,-29,-30,-24,28,-25,28,-26,]),'FOR':([14,23,46,48,50,84,120,121,131,132,133,134,141,148,154,158,],[29,29,-13,-20,-22,-21,29,29,-23,-29,-30,-24,29,-25,29,-26,]),'INCREMENTN':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[31,31,31,31,31,31,-13,-20,-22,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-21,31,31,31,31,31,31,-23,-29,-30,-24,31,31,31,-25,31,31,31,-26,]),'DECREMENTN':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[32,32,32,32,32,32,-13,-20,-22,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-21,32,32,32,32,32,32,-23,-29,-30,-24,32,32,32,-25,32,32,32,-26,]),'NINT':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[33,33,33,33,33,33,-13,-20,-22,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-21,33,33,33,33,33,33,-23,-29,-30,-24,33,33,33,-25,33,33,33,-26,]),'NFLOAT':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[34,34,34,34,34,34,-13,-20,-22,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-21,34,34,34,34,34,34,-23,-29,-30,-24,34,34,34,-25,34,34,34,-26,]),'FALSE':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[38,38,38,38,38,38,-13,-20,-22,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-21,38,38,38,38,38,38,-23,-29,-30,-24,38,38,38,-25,38,38,38,-26,]),'TRUE':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[39,39,39,39,39,39,-13,-20,-22,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-21,39,39,39,39,39,39,-23,-29,-30,-24,39,39,39,-25,39,39,39,-26,]),'NOT':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[40,40,40,40,40,40,-13,-20,-22,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-21,40,40,40,40,40,40,-23,-29,-30,-24,40,40,40,-25,40,40,40,-26,]),'STRINGD':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[42,42,42,42,42,42,-13,-20,-22,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-21,42,42,42,42,42,42,-23,-29,-30,-24,42,42,42,-25,42,42,42,-26,]),'STRINGS':([14,23,25,31,32,40,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,84,114,119,120,121,122,124,131,132,133,134,141,142,143,148,153,154,156,158,],[43,43,43,43,43,43,-13,-20,-22,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-21,43,43,43,43,43,43,-23,-29,-30,-24,43,43,43,-25,43,43,43,-26,]),'COLON':([15,82,118,],[44,117,129,]),'LPAREN':([16,18,19,20,27,28,29,30,81,],[45,-72,-73,-74,73,74,75,76,116,]),'ASSIGN':([18,19,20,30,81,126,138,],[-72,-73,-74,77,114,137,144,]),'LBRACKET':([18,19,20,81,137,144,],[-72,-73,-74,115,143,153,]),'RBRACKET':([18,19,20,30,33,34,35,36,37,38,39,42,43,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,113,115,123,127,130,143,151,152,157,159,],[-72,-73,-74,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,-44,-46,-47,-48,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-49,-50,-51,-52,-53,-65,-68,126,-64,138,-54,150,155,-75,160,-76,]),'COMMA':([18,19,20,30,33,34,35,36,37,38,39,42,43,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,111,112,113,123,128,130,152,],[-72,-73,-74,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,-44,-46,-47,-48,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-49,-50,-51,-52,-53,-65,124,-68,-64,139,-54,156,]),'RPAREN':([18,19,20,30,33,34,35,36,37,38,39,42,43,64,66,76,78,79,80,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,108,109,110,111,112,113,123,128,130,136,145,149,],[-72,-73,-74,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,-44,-46,111,-47,-48,-63,118,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,-49,-50,-51,-52,-53,120,121,-27,-28,123,-65,-67,-68,-64,-17,-54,-66,-16,154,]),'RBRACE':([22,23,46,47,48,50,84,131,132,133,134,148,158,],[46,-18,-13,-19,-20,-22,-21,-23,-29,-30,-24,-25,-26,]),'PLUS':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[51,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,51,-44,-46,51,51,-63,-31,-32,-33,-34,-35,51,51,51,51,51,51,51,51,-45,51,51,51,51,51,51,51,51,51,-65,51,51,-64,51,51,51,]),'MINUS':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[52,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,52,-44,-46,52,52,-63,-31,-32,-33,-34,-35,52,52,52,52,52,52,52,52,-45,52,52,52,52,52,52,52,52,52,-65,52,52,-64,52,52,52,]),'TIMES':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[53,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,53,-44,-46,53,53,-63,53,53,-33,-34,-35,53,53,53,53,53,53,53,53,-45,53,53,53,53,53,53,53,53,53,-65,53,53,-64,53,53,53,]),'DIVIDE':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[54,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,54,-44,-46,54,54,-63,54,54,-33,-34,-35,54,54,54,54,54,54,54,54,-45,54,54,54,54,54,54,54,54,54,-65,54,54,-64,54,54,54,]),'MOD':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[55,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,55,-44,-46,55,55,-63,55,55,-33,-34,-35,55,55,55,55,55,55,55,55,-45,55,55,55,55,55,55,55,55,55,-65,55,55,-64,55,55,55,]),'OR':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[56,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,56,-44,-46,56,56,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,56,56,56,-52,-53,56,56,56,56,-65,56,56,-64,56,56,56,]),'AND':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[57,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,57,-44,-46,57,57,-63,-31,-32,-33,-34,-35,57,-37,-38,-39,-40,-41,-42,-43,-45,57,57,57,-52,-53,57,57,57,57,-65,57,57,-64,57,57,57,]),'EQ':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[58,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,58,-44,-46,58,58,-63,-31,-32,-33,-34,-35,58,58,-38,-39,-40,-41,-42,-43,-45,58,58,58,-52,-53,58,58,58,58,-65,58,58,-64,58,58,58,]),'NEQ':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[59,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,59,-44,-46,59,59,-63,-31,-32,-33,-34,-35,59,59,-38,-39,-40,-41,-42,-43,-45,59,59,59,-52,-53,59,59,59,59,-65,59,59,-64,59,59,59,]),'GE':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[60,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,60,-44,-46,60,60,-63,-31,-32,-33,-34,-35,60,60,60,60,-40,-41,-42,-43,-45,60,60,60,60,60,60,60,60,60,-65,60,60,-64,60,60,60,]),'LE':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[61,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,61,-44,-46,61,61,-63,-31,-32,-33,-34,-35,61,61,61,61,-40,-41,-42,-43,-45,61,61,61,61,61,61,61,61,61,-65,61,61,-64,61,61,61,]),'LT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[62,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,62,-44,-46,62,62,-63,-31,-32,-33,-34,-35,62,62,62,62,-40,-41,-42,-43,-45,62,62,62,62,62,62,62,62,62,-65,62,62,-64,62,62,62,]),'GT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[63,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,63,-44,-46,63,63,-63,-31,-32,-33,-34,-35,63,63,63,63,-40,-41,-42,-43,-45,63,63,63,63,63,63,63,63,63,-65,63,63,-64,63,63,63,]),'INCREMENT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[64,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,64,-44,-46,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-65,64,64,-64,64,64,64,]),'EXPO':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[65,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,65,-44,-46,65,65,-63,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-65,65,65,-64,65,65,65,]),'DECREMENT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[66,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,66,-44,-46,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-65,66,66,-64,66,66,66,]),'TIMESINCREMENT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[67,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,67,-44,-46,67,67,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,67,67,67,-52,-53,67,67,67,67,-65,67,67,-64,67,-54,67,]),'DIVIDEINCREMENT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[68,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,68,-44,-46,68,68,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,68,68,68,-52,-53,68,68,68,68,-65,68,68,-64,68,-54,68,]),'MODINCREMENT':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[69,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,69,-44,-46,69,69,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,69,69,69,-52,-53,69,69,69,69,-65,69,69,-64,69,-54,69,]),'EEQ':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[70,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,70,-44,-46,70,70,-63,-31,-32,-33,-34,-35,70,70,-38,-39,-40,-41,-42,-43,-45,70,70,70,-52,-53,70,70,70,70,-65,70,70,-64,70,70,70,]),'NNEQ':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[71,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,71,-44,-46,71,71,-63,-31,-32,-33,-34,-35,71,71,-38,-39,-40,-41,-42,-43,-45,71,71,71,-52,-53,71,71,71,71,-65,71,71,-64,71,71,71,]),'INTER':([26,30,33,34,35,36,37,38,39,42,43,49,64,66,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,112,113,123,125,130,152,],[72,-60,-55,-56,-57,-58,-59,-61,-62,-77,-78,72,-44,-46,72,72,-63,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-45,72,72,72,-52,-53,119,72,72,72,-65,72,72,-64,72,119,72,]),'ELSE':([46,48,50,84,131,132,133,134,148,158,],[-13,-20,-22,-21,-23,-29,-30,-24,-25,-26,]),'VOID':([75,122,142,],[109,109,109,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,12,],[1,11,21,]),'funcdecl':([0,2,12,],[2,2,2,]),'vardecl':([0,2,12,14,23,120,121,141,154,],[3,3,3,24,24,24,24,24,24,]),'signature':([0,2,12,],[4,4,4,]),'tipodecl':([0,2,12,14,23,120,121,141,154,],[5,5,5,5,5,5,5,5,5,]),'tipofunc':([0,2,12,],[6,6,6,]),'body':([4,120,121,140,141,154,],[13,132,132,146,132,132,]),'tipo':([9,41,44,116,117,129,],[17,17,81,127,128,140,]),'comandos':([14,23,],[22,47,]),'comando':([14,23,120,121,141,154,],[23,23,133,133,133,133,]),'expressao':([14,23,25,31,32,40,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,114,119,120,121,122,124,141,142,143,153,154,156,],[26,26,49,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,112,113,125,130,26,26,108,112,26,108,152,152,26,152,]),'string':([14,23,25,31,32,40,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,114,119,120,121,122,124,141,142,143,153,154,156,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'call':([14,23,25,31,32,40,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,114,119,120,121,122,124,141,142,143,153,154,156,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'assign':([14,23,25,31,32,40,51,52,53,54,55,56,57,58,59,60,61,62,63,65,67,68,69,70,71,72,73,74,75,76,77,114,119,120,121,122,124,141,142,143,153,154,156,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'funcparametros':([45,139,],[83,145,]),'opexp':([75,122,142,],[107,135,149,]),'parametros':([76,124,],[110,136,]),'bodyorcomando':([120,121,141,154,],[131,134,148,158,]),'listexp':([143,153,156,],[151,157,159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> funcdecl','programa',1,'p_programa','ExpressionLanguageSint.py',49),
  ('programa -> funcdecl programa','programa',2,'p_program1','ExpressionLanguageSint.py',53),
  ('programa -> vardecl SEMICOLON','programa',2,'p_program2','ExpressionLanguageSint.py',57),
  ('programa -> vardecl SEMICOLON programa','programa',3,'p_program3','ExpressionLanguageSint.py',61),
  ('vardecl -> tipodecl ID COLON tipo','vardecl',4,'p_vardecl','ExpressionLanguageSint.py',65),
  ('vardecl -> tipodecl ID COLON tipo ASSIGN expressao','vardecl',6,'p_vardecl2','ExpressionLanguageSint.py',68),
  ('vardecl -> tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET RBRACKET','vardecl',9,'p_vardecl3','ExpressionLanguageSint.py',72),
  ('vardecl -> tipodecl ID COLON tipo LBRACKET RBRACKET ASSIGN LBRACKET listexp RBRACKET','vardecl',10,'p_vardecl4','ExpressionLanguageSint.py',76),
  ('vardecl -> tipodecl ID COLON tipo LPAREN tipo RBRACKET ASSIGN LBRACKET listexp RBRACKET','vardecl',11,'p_vardecl5','ExpressionLanguageSint.py',80),
  ('funcdecl -> signature body','funcdecl',2,'p_funcdecl','ExpressionLanguageSint.py',84),
  ('signature -> tipofunc ID LPAREN funcparametros RPAREN COLON tipo body','signature',8,'p_signature1','ExpressionLanguageSint.py',88),
  ('signature -> tipofunc ID LPAREN funcparametros RPAREN COLON tipo SEMICOLON','signature',8,'p_signature2','ExpressionLanguageSint.py',92),
  ('body -> LBRACE comandos RBRACE','body',3,'p_body','ExpressionLanguageSint.py',96),
  ('tipofunc -> FUNCTION','tipofunc',1,'p_tipofunc','ExpressionLanguageSint.py',100),
  ('tipofunc -> CONST','tipofunc',1,'p_tipofunc','ExpressionLanguageSint.py',101),
  ('funcparametros -> ID COLON tipo COMMA funcparametros','funcparametros',5,'p_funcparametros','ExpressionLanguageSint.py',106),
  ('funcparametros -> ID COLON tipo','funcparametros',3,'p_funcparametros','ExpressionLanguageSint.py',107),
  ('comandos -> comando','comandos',1,'p_comandos','ExpressionLanguageSint.py',114),
  ('comandos -> comando comandos','comandos',2,'p_comandos','ExpressionLanguageSint.py',115),
  ('comando -> vardecl SEMICOLON','comando',2,'p_comando','ExpressionLanguageSint.py',122),
  ('comando -> RETURN expressao SEMICOLON','comando',3,'p_comando','ExpressionLanguageSint.py',123),
  ('comando -> expressao SEMICOLON','comando',2,'p_comando1','ExpressionLanguageSint.py',130),
  ('comando -> WHILE LPAREN expressao RPAREN bodyorcomando','comando',5,'p_comandoWHILE','ExpressionLanguageSint.py',134),
  ('comando -> IF LPAREN expressao RPAREN bodyorcomando','comando',5,'p_comandopIF','ExpressionLanguageSint.py',138),
  ('comando -> IF LPAREN expressao RPAREN bodyorcomando ELSE bodyorcomando','comando',7,'p_comandoIFELSE','ExpressionLanguageSint.py',142),
  ('comando -> FOR LPAREN opexp SEMICOLON opexp SEMICOLON opexp RPAREN bodyorcomando','comando',9,'p_comandoFOR','ExpressionLanguageSint.py',146),
  ('opexp -> expressao','opexp',1,'p_opexp','ExpressionLanguageSint.py',150),
  ('opexp -> VOID','opexp',1,'p_opexp','ExpressionLanguageSint.py',151),
  ('bodyorcomando -> body','bodyorcomando',1,'p_bodyorcomando','ExpressionLanguageSint.py',159),
  ('bodyorcomando -> comando','bodyorcomando',1,'p_bodyorcomando','ExpressionLanguageSint.py',160),
  ('expressao -> expressao PLUS expressao','expressao',3,'p_expressaoPLUS','ExpressionLanguageSint.py',169),
  ('expressao -> expressao MINUS expressao','expressao',3,'p_expressaoMINUS','ExpressionLanguageSint.py',173),
  ('expressao -> expressao TIMES expressao','expressao',3,'p_expressaoTIMES','ExpressionLanguageSint.py',177),
  ('expressao -> expressao DIVIDE expressao','expressao',3,'p_expressaoDIVIDE','ExpressionLanguageSint.py',181),
  ('expressao -> expressao MOD expressao','expressao',3,'p_expressaoMOD','ExpressionLanguageSint.py',185),
  ('expressao -> expressao OR expressao','expressao',3,'p_expressaoOR','ExpressionLanguageSint.py',189),
  ('expressao -> expressao AND expressao','expressao',3,'p_expressaoAND','ExpressionLanguageSint.py',193),
  ('expressao -> expressao EQ expressao','expressao',3,'p_expressaoEQ','ExpressionLanguageSint.py',197),
  ('expressao -> expressao NEQ expressao','expressao',3,'p_expressaoNEQ','ExpressionLanguageSint.py',201),
  ('expressao -> expressao GE expressao','expressao',3,'p_expressaoGE','ExpressionLanguageSint.py',205),
  ('expressao -> expressao LE expressao','expressao',3,'p_expressaoLE','ExpressionLanguageSint.py',209),
  ('expressao -> expressao LT expressao','expressao',3,'p_expressaoLT','ExpressionLanguageSint.py',213),
  ('expressao -> expressao GT expressao','expressao',3,'p_expressaoGT','ExpressionLanguageSint.py',217),
  ('expressao -> expressao INCREMENT','expressao',2,'p_expressaoINCREMENT','ExpressionLanguageSint.py',221),
  ('expressao -> expressao EXPO expressao','expressao',3,'p_expressaoEXPO','ExpressionLanguageSint.py',225),
  ('expressao -> expressao DECREMENT','expressao',2,'p_expressaoDECREMENT','ExpressionLanguageSint.py',229),
  ('expressao -> INCREMENTN expressao','expressao',2,'p_expressaoINCREMENTN','ExpressionLanguageSint.py',233),
  ('expressao -> DECREMENTN expressao','expressao',2,'p_expressaoDECREMENTN','ExpressionLanguageSint.py',237),
  ('expressao -> expressao TIMESINCREMENT expressao','expressao',3,'p_expressaoTIMESINCREMENT','ExpressionLanguageSint.py',241),
  ('expressao -> expressao DIVIDEINCREMENT expressao','expressao',3,'p_expressaoDIVIDEINCREMENT','ExpressionLanguageSint.py',245),
  ('expressao -> expressao MODINCREMENT expressao','expressao',3,'p_expressaoMODINCREMENT','ExpressionLanguageSint.py',249),
  ('expressao -> expressao EEQ expressao','expressao',3,'p_expressaoEEQ','ExpressionLanguageSint.py',253),
  ('expressao -> expressao NNEQ expressao','expressao',3,'p_expressaoNNEQ','ExpressionLanguageSint.py',258),
  ('expressao -> expressao INTER expressao INTER expressao','expressao',5,'p_expressaoFIM','ExpressionLanguageSint.py',262),
  ('expressao -> NINT','expressao',1,'p_expressaoNINT','ExpressionLanguageSint.py',266),
  ('expressao -> NFLOAT','expressao',1,'p_expressaoNFLOAT','ExpressionLanguageSint.py',270),
  ('expressao -> string','expressao',1,'p_expressaostring','ExpressionLanguageSint.py',274),
  ('expressao -> call','expressao',1,'p_expressaocall','ExpressionLanguageSint.py',278),
  ('expressao -> assign','expressao',1,'p_expressaoassign','ExpressionLanguageSint.py',282),
  ('expressao -> ID','expressao',1,'p_expressaoID','ExpressionLanguageSint.py',286),
  ('expressao -> FALSE','expressao',1,'p_expressaoBOOLEAN','ExpressionLanguageSint.py',290),
  ('expressao -> TRUE','expressao',1,'p_expressaoBOOLEAN','ExpressionLanguageSint.py',291),
  ('expressao -> NOT expressao','expressao',2,'p_expressaoNOT','ExpressionLanguageSint.py',295),
  ('call -> ID LPAREN parametros RPAREN','call',4,'p_call','ExpressionLanguageSint.py',299),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','ExpressionLanguageSint.py',300),
  ('parametros -> expressao COMMA parametros','parametros',3,'p_parametros','ExpressionLanguageSint.py',308),
  ('parametros -> expressao','parametros',1,'p_parametros','ExpressionLanguageSint.py',309),
  ('assign -> ID ASSIGN expressao','assign',3,'p_assign','ExpressionLanguageSint.py',317),
  ('tipodecl -> LET','tipodecl',1,'p_tipodecl','ExpressionLanguageSint.py',322),
  ('tipodecl -> VAR','tipodecl',1,'p_tipodecl','ExpressionLanguageSint.py',323),
  ('tipodecl -> CONST tipo','tipodecl',2,'p_tipodecl','ExpressionLanguageSint.py',324),
  ('tipo -> STRING','tipo',1,'p_tipo','ExpressionLanguageSint.py',332),
  ('tipo -> NUMBER','tipo',1,'p_tipo','ExpressionLanguageSint.py',333),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','ExpressionLanguageSint.py',334),
  ('listexp -> expressao','listexp',1,'p_listexp','ExpressionLanguageSint.py',339),
  ('listexp -> expressao COMMA listexp','listexp',3,'p_listexp','ExpressionLanguageSint.py',340),
  ('string -> STRINGD','string',1,'p_string','ExpressionLanguageSint.py',349),
  ('string -> STRINGS','string',1,'p_string','ExpressionLanguageSint.py',350),
]
