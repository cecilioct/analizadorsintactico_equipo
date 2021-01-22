import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador
import sys

# resultado del analisis
resultado_gramatica = []

#orden en que se aplicarán
precedence = (
    ('right','ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

#declaraciones: declaracion con asignacion y declaracion sin asignacion
#Reconoce datos de tipo entero(int) y decimal (double)
def p_declaracion_asignar(t):
    '''
    
    declaracion :  dec IDENTIFICADOR ASIGNAR expresion PUNTOCOMA 
                |  dec IDENTIFICADOR PUNTOCOMA
    '''
    
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    #print("Resultado: " + str(t[1]))
    t[0] = t[1]

#expresiones complejas con operadores entre parentesis
#expresione limitadas con multiplicacin y division fuera de los parentesis
def p_expresion_formulascomplejas(t):
    '''
    expresion : expresion SUMA PARIZQ expresion SUMA expresion PARDER
              | expresion SUMA PARIZQ expresion RESTA expresion PARDER
              | expresion RESTA PARIZQ expresion SUMA expresion PARDER 
              | expresion RESTA PARIZQ expresion RESTA expresion PARDER 
              | expresion MULT PARIZQ expresion SUMA expresion PARDER 
              | expresion MULT PARIZQ expresion RESTA expresion PARDER
              | expresion SUMA PARIZQ expresion MULT expresion PARDER
              | expresion RESTA PARIZQ expresion MULT expresion PARDER
              | PARIZQ expresion RESTA expresion PARDER DIV expresion
              | PARIZQ expresion SUMA  expresion PARDER DIV expresion
              | PARIZQ expresion RESTA expresion PARDER MULT expresion
              | ASIGNAR PARIZQ expresion SUMA  expresion PARDER MULT expresion 
    '''
    t[1]=t[0]

#expreisones sobre operaiciones básicas donde no se incluye parentesis.
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion
    '''
    t[1]=t[0]

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

#expresiones agrupadas entre:
#parentesis, llaves y corchetes
def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    t[0] = t[2]

# operaciones lógicas completo incluye operaciones
#lógicas entre parentesis
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER 
                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER
    '''
    t[1]=t[0]



# gramatica de expresiones booleanadas simples y con parentesis
def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion 
                |   expresion OR expresion 
                |   expresion NOT expresion 
                |  PARIZQ expresion AND expresion PARDER
                |  PARIZQ expresion OR expresion PARDER
                |  PARIZQ expresion NOT expresion PARDER
    '''
   
    t[1]=t[0]


#expresiones para reconocer número 
#Entero y decimal
def p_expresion_numero(t):
    '''
    expresion : ENTERO
              | FLOAT   
    '''
    t[0] = t[1]

#expresion cadenas
def p_expresion_cadena(t):
    'expresion : COMDOB expresion COMDOB'
    t[0] = t[2]


#defincion para una expresionde tipo IDENTIFICADOR
#Es cualquier palabra que se usa como una variable
def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
       # print("Nombre desconocido ", t[1])
        t[0] = 0


#Bucles WHILE, IF Y FOR con expresiones de tipo operaciones logicas
#Las sentencias de cada bucle esta limitado en cuanto a las operaciones lógicas
def p_expresion_bucles(t):
    '''
    expresion : MIENTRAS PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER
              | MIENTRAS PARIZQ expresion MAYORQUE  expresion PARDER LLAIZQ expresion LLADER
              | MIENTRAS PARIZQ expresion IGUAL expresion PARDER PARDER LLAIZQ expresion LLADER
              | SI PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER
              | SI PARIZQ expresion MAYORQUE expresion PARDER LLAIZQ expresion  LLADER
              | SI PARIZQ expresion IGUAL expresion PARDER LLAIZQ expresion  LLADER
              | SI PARIZQ expresion MENORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER
              | SI PARIZQ expresion MAYORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER
              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER
              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MENORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER


    '''
    t[1]=t[0]

#Salida cuando existe un error sintactico
#Da como salida el tipo de error y el valor en el que se generó
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
        resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

#prueba sintactica
def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
   
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram)) #resultado de la prueba 
        else: print("data vacia")

    print("resultado: ", resultado_gramatica)

    
    if not resultado_gramatica: #sino resgresa ningun valor imprime la frase
        #resultado_gramatica = "Compilacion Exitosa"
        print(resultado_gramatica)
    
    return resultado_gramatica
if __name__ == "__main__":
    #lee el archivo donde se encuentra el código para la prueba en c#
    if len(sys.argv) > 1:
        script = sys.argv[1]
        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        print(chr(27) + "[0;36m" + "INICIA ANALISIS SINTACTICO" + chr(27) + "[0m")
        prueba_sintactica(scriptdata)
        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")
        
          

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        #prueba_sintactica(s)

else:   #Instruccion para pasar un archivo para procesar
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp Cs como parametro")
        print(
            chr(27)
            + "[0;36m"
            + "\t$ python AnalizadorLexico.py"
            + chr(27)
            + "[1;31m"
            + " <prueba>.cs"
            + chr(27)
            + "[0m"
        )
