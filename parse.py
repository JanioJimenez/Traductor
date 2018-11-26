from lexico import *
from ply import lex
lexer = lex.lex()

# Parsing rules


def p_gramatica(t):
      'statement : SUJETO'

def p_error(t):
    print("Syntax error at '%s'" % t.value)

from ply import yacc
parser = yacc.yacc()

f = open("archi.txt","r")
linea = f.read()

parser.parse(linea)
