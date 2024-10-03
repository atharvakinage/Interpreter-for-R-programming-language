from R_lex import *

# Parsing rules for the required constructs (variable declaration,if-else condition,while loop,for loop,repeat loop)

def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMICOLON
                 | ID ASSIGN expression 
                 | ID ASSIGN ID'''
    print("Variable Assignment:", p[1])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    print("While Loop")

def p_statement_for(p):
    '''statement : FOR LPAREN ID IN ID RPAREN LBRACE statements RBRACE
                 | FOR LPAREN ID IN NUMBER COLON NUMBER RPAREN LBRACE statements RBRACE'''
    print("For Loop")

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE'''
    print("If Statement")

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    print("If-Else Statement")

def p_statement_repeat(p):
    '''statement : REPEAT LBRACE statements RBRACE'''
    print("Repeat Loop")

def p_expression_number(p):
    '''expression : NUMBER
                  | ID
    '''
    p[0] = p[1]



def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATEREQ expression
                  | expression LESSEQ expression
                  | expression NOTEQUALTO expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQ expression
    '''
    p[0] = f"{p[1]} {p[2]} {p[3]}"




def p_statements_multiple(p):
    'statements : statement statements'
    pass

def p_statements_single(p):
    'statements : statement'
    pass

def p_other_statement(p):
    '''statements : ID LPAREN STRING RPAREN
                     | ID LPAREN ID RPAREN
                     | ID LPAREN expression RPAREN
                     | ID ASSIGN expression
                     | expression
                     | ID'''
    pass


# Error handling for parsing
def p_error(p):
    if p:
        print("Syntax error at",p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test R code
user_input = ""
print("Enter any one of the loops (for, while, if-else or repeat) or variable assignment (press Enter twice to finish):")
while True: 
    line = input()
    if not line:
        break
    user_input += line + '\n'

# Give the lexer the user's input
lexer.input(user_input)

# Tokenize the user's input
for tok in iter(lexer.token, None):
    print(tok)

print("----------------------------------------------------------------------------------")

result=parser.parse(user_input)
print(result)
    