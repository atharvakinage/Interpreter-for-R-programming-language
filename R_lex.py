import ply.lex as lex
import ply.yacc as yacc

# List of tokens
tokens = (
    'ID',
    'NUMBER',
    'PLUS',     
    'MINUS',    
    'TIMES',    
    'DIVIDE',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COLON',
    'WHILE',
    'FOR',
    'IF',
    'ELSE',
    'REPEAT',
    'STRING',
    'NOTEQUALTO',
    'EQ',
    'GREATER',
    'LESS',
    'GREATEREQ',
    'LESSEQ',
    'AND',
    'OR',
    'IN',
)

# Regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r'\:'
t_WHILE = r'while'
t_FOR = r'for'
t_IF = r'if'
t_ELSE = r'else'
t_REPEAT = r'repeat'
t_NOTEQUALTO = r'\!'
t_GREATER = r'\>'
t_LESS = r'<'
t_GREATEREQ = r'>='
t_LESSEQ = r'<='
t_AND = r'AND'
t_OR = r'OR'
t_EQ=r'=='
t_IN = r'in'

def t_ID(t):
    r'[a-zA-Z._][a-zA-Z0-9._]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the double quotes
    return t

def t_ASSIGN(t):
    r'<-'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Reserved words
reserved = {
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'repeat': 'REPEAT',
    'in': 'IN'
}

# Build the lexer
lexer = lex.lex()

