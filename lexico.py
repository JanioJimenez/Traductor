from diccionario import *

tokens = (       
    'NUMERO',           # [0-9]          
    'SUJETO',
    'VERBO'
)
# Tokens


# Ignored characters
t_ignore = "\t"
   

def t_NUMERO(t):
    r'\d+'
    try:    
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d", t.value)
        t.value = 0
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
