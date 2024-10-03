**R language interpreter**


A basic interpreter for R programming language using Python's PLY (Python Lex-Yacc) library. This language supports constructs like variable assignment, loops (for,while,repeat), and conditional statements (if-else). The project is designed to tokenize and parse input source code and recognize the syntax of the language.

**Features**

Lexer: Breaks input code into tokens such as keywords, operators, variables, numbers, and more.  
Parser: Recognizes basic control structures such as:  
- Variable assignment (:=)  
- Conditional statements (if-else)  
- Loops (for, while, repeat) 
- Arithmetic operations (+, -, *, /)  
- Logical operations (AND, OR, comparisons)  

Error Handling: Basic syntax error detection and reporting.

To install ply:  
pip install ply  

To run the interpreter:  
python R_yacc.py

