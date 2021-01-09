
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ASIGNAR CADENA COMA COMDOB CORDER CORIZQ COUT DECIMAL DISTINTO DIV ENTERO FINALLY FLOAT GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO SUMA THEN USING VOIDdeclaracion :  IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion\n    expresion : IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion SUMA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion RESTA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion SUMA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion RESTA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion MULT PARIZQ expresion SUMA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion MULT PARIZQ expresion RESTA expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion MULT expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion MULT expresion PARDER PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR PARIZQ expresion RESTA expresion PARDER DIV expresion PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR PARIZQ expresion SUMA  expresion PARDER DIV expresion PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR PARIZQ expresion RESTA expresion PARDER MULT expresion PUNTOCOMA\n              | IDENTIFICADOR ASIGNAR PARIZQ expresion SUMA  expresion PARDER MULT expresion PUNTOCOMA\n    \n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n               \n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    \n    expresion : ENTERO\n              | FLOAT       \n    expresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR\n    expresion : MIENTRAS PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | MIENTRAS PARIZQ expresion MAYORQUE  expresion PARDER LLAIZQ expresion LLADER\n              | MIENTRAS PARIZQ expresion IGUAL expresion PARDER PARDER LLAIZQ expresion LLADER\n              | SI PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion MAYORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion IGUAL expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion MENORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER\n              | SI PARIZQ expresion MAYORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER\n              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER\n              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MENORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER\n\n\n    '
    
_lr_action_items = {'IDENTIFICADOR':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,38,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,133,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,218,219,232,233,234,235,240,241,],[2,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,66,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,158,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,222,223,31,31,31,31,31,31,]),'RESTA':([0,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,70,71,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,134,135,136,137,138,139,140,141,144,145,146,147,148,149,150,151,153,154,155,156,157,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,232,233,234,235,236,237,238,239,240,241,242,243,244,245,248,249,],[5,-46,16,5,5,5,5,-43,-44,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,16,-46,-21,16,16,16,5,5,69,5,-15,-16,-17,-18,16,16,16,16,16,16,16,16,16,16,16,-22,5,5,5,5,-23,-24,-45,16,16,5,5,5,94,16,16,16,69,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-40,-41,-42,16,16,16,16,16,16,16,16,16,135,137,141,-16,-15,16,16,16,16,16,16,5,5,5,5,5,5,5,5,-31,-32,-33,-34,-35,-36,5,5,5,5,5,5,5,-15,-16,-17,-16,-15,-17,-15,-16,5,5,5,5,16,16,5,16,16,16,16,16,5,5,16,16,16,16,-47,-48,16,-50,-51,-52,5,5,16,16,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,16,16,5,5,5,5,16,16,16,16,5,5,-55,-56,16,16,-53,-54,]),'PARIZQ':([0,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,72,73,74,75,76,77,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[4,4,4,4,4,4,36,37,38,40,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,40,91,92,93,96,97,98,99,100,101,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LLAIZQ':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,125,126,128,129,130,131,132,134,135,136,137,138,139,140,141,150,151,152,153,154,155,156,157,167,168,169,170,173,179,180,199,200,228,229,230,231,232,233,234,235,240,241,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,150,151,153,154,155,156,157,6,6,6,6,6,6,6,6,6,6,173,6,6,6,6,6,6,6,6,6,6,6,6,6,6,232,233,234,235,6,6,6,6,6,6,]),'CORIZQ':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'ENTERO':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FLOAT':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'COMDOB':([0,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,134,135,136,137,138,139,140,141,144,145,146,147,148,149,150,151,153,154,155,156,157,167,168,169,170,173,179,180,193,194,196,197,198,199,200,203,204,205,206,207,208,209,210,211,212,213,214,215,232,233,234,235,240,241,242,243,248,249,],[10,10,10,10,10,-43,-44,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-46,-21,63,10,10,10,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,10,10,10,10,-23,-24,-45,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-40,-41,-42,10,10,10,10,10,10,10,10,-31,-32,-33,-34,-35,-36,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-47,-48,-50,-51,-52,10,10,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,10,10,10,10,10,10,-55,-56,-53,-54,]),'MIENTRAS':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'SI':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'PARA':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'$end':([1,2,3,8,9,31,32,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,67,102,103,104,144,145,146,147,148,149,193,194,196,197,198,203,204,205,206,207,208,209,210,211,212,213,214,215,242,243,248,249,],[0,-46,-2,-43,-44,-46,-21,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-1,-40,-41,-42,-31,-32,-33,-34,-35,-36,-47,-48,-50,-51,-52,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,-55,-56,-53,-54,]),'ASIGNAR':([2,31,66,],[14,60,90,]),'SUMA':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,15,-43,-44,15,-46,-21,15,15,15,68,-15,-16,-17,-18,15,15,15,15,15,15,15,15,15,15,15,-22,-23,-24,-45,15,15,95,15,15,15,68,-40,-41,-42,15,15,15,15,15,15,15,15,15,134,138,140,-16,-15,15,15,15,15,15,15,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,15,15,15,15,15,15,15,15,15,15,15,-47,-48,15,-50,-51,-52,15,15,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,15,15,15,15,15,15,-55,-56,15,15,-53,-54,]),'MULT':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,142,143,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,17,-43,-44,17,-46,-21,17,17,17,70,17,17,-17,-18,17,17,17,17,17,17,17,17,17,17,17,-22,-23,-24,-45,17,17,17,17,17,17,70,-40,-41,-42,17,17,17,17,17,17,17,17,17,136,139,17,17,17,17,17,17,17,17,17,168,170,-31,-32,-33,-34,-35,-36,17,17,-17,17,17,-17,17,17,17,17,17,17,17,17,17,17,17,17,17,-47,-48,17,-50,-51,-52,17,17,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,17,17,17,17,17,17,-55,-56,17,17,-53,-54,]),'DIV':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,142,143,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,18,-43,-44,18,-46,-21,18,18,18,18,18,18,-17,-18,18,18,18,18,18,18,18,18,18,18,18,-22,-23,-24,-45,18,18,18,18,18,18,18,-40,-41,-42,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,167,169,-31,-32,-33,-34,-35,-36,18,18,-17,18,18,-17,18,18,18,18,18,18,18,18,18,18,18,18,18,-47,-48,18,-50,-51,-52,18,18,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,18,18,18,18,18,18,-55,-56,18,18,-53,-54,]),'POTENCIA':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,19,-43,-44,19,-46,-21,19,19,19,19,-15,-16,-17,-18,19,19,19,19,19,19,19,19,19,19,19,-22,-23,-24,-45,19,19,19,19,19,19,19,-40,-41,-42,19,19,19,19,19,19,19,19,19,19,19,19,-16,-15,19,19,19,19,19,19,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,19,19,19,19,19,19,19,19,19,19,19,-47,-48,19,-50,-51,-52,19,19,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,19,19,19,19,19,19,-55,-56,19,19,-53,-54,]),'MODULO':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,20,-43,-44,20,-46,-21,20,20,20,20,-15,-16,-17,-18,20,20,20,20,20,20,20,20,20,20,20,-22,-23,-24,-45,20,20,20,20,20,20,20,-40,-41,-42,20,20,20,20,20,20,20,20,20,20,20,20,-16,-15,20,20,20,20,20,20,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,20,20,20,20,20,20,20,20,20,20,20,-47,-48,20,-50,-51,-52,20,20,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,20,20,20,20,20,20,-55,-56,20,20,-53,-54,]),'MENORQUE':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,158,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,21,-43,-44,21,-46,-21,21,21,21,21,-15,-16,-17,-18,21,21,21,21,21,21,21,21,21,21,21,72,-23,-24,-45,82,85,21,21,21,21,21,-40,-41,-42,21,21,21,21,21,21,21,21,21,21,21,21,-16,-15,21,21,21,21,21,21,-31,-32,-33,-34,-35,-36,180,-15,-16,-17,-16,-15,-17,-15,-16,21,21,21,21,21,21,21,21,21,21,21,-47,-48,21,-50,-51,-52,21,21,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,21,21,21,21,21,21,-55,-56,21,21,-53,-54,]),'MAYORQUE':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,158,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,22,-43,-44,22,-46,-21,22,22,22,22,-15,-16,-17,-18,22,22,22,22,22,22,22,22,22,22,22,73,-23,-24,-45,83,86,22,22,22,22,22,-40,-41,-42,22,22,22,22,22,22,22,22,22,22,22,22,-16,-15,22,22,22,22,22,22,-31,-32,-33,-34,-35,-36,179,-15,-16,-17,-16,-15,-17,-15,-16,22,22,22,22,22,22,22,22,22,22,22,-47,-48,22,-50,-51,-52,22,22,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,22,22,22,22,22,22,-55,-56,22,22,-53,-54,]),'MENORIGUAL':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,23,-43,-44,23,-46,-21,23,23,23,23,-15,-16,-17,-18,23,23,23,23,23,23,23,23,23,23,23,74,-23,-24,-45,23,88,23,23,23,23,23,-40,-41,-42,23,23,23,23,23,23,23,23,23,23,23,23,-16,-15,23,23,23,23,23,23,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,23,23,23,23,23,23,23,23,23,23,23,-47,-48,23,-50,-51,-52,23,23,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,23,23,23,23,23,23,-55,-56,23,23,-53,-54,]),'MAYORIGUAL':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,24,-43,-44,24,-46,-21,24,24,24,24,-15,-16,-17,-18,24,24,24,24,24,24,24,24,24,24,24,75,-23,-24,-45,24,89,24,24,24,24,24,-40,-41,-42,24,24,24,24,24,24,24,24,24,24,24,24,-16,-15,24,24,24,24,24,24,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,24,24,24,24,24,24,24,24,24,24,24,-47,-48,24,-50,-51,-52,24,24,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,24,24,24,24,24,24,-55,-56,24,24,-53,-54,]),'IGUAL':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,25,-43,-44,25,-46,-21,25,25,25,25,-15,-16,-17,-18,25,25,25,25,25,25,25,25,25,25,25,76,-23,-24,-45,84,87,25,25,25,25,25,-40,-41,-42,25,25,25,25,25,25,25,25,25,25,25,25,-16,-15,25,25,25,25,25,25,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,25,25,25,25,25,199,200,25,25,25,25,-47,-48,25,-50,-51,-52,25,25,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,25,25,240,241,25,25,-55,-56,25,25,-53,-54,]),'DISTINTO':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,26,-43,-44,26,-46,-21,26,26,26,26,-15,-16,-17,-18,26,26,26,26,26,26,26,26,26,26,26,77,-23,-24,-45,26,26,26,26,26,26,26,-40,-41,-42,26,26,26,26,26,26,26,26,26,26,26,26,-16,-15,26,26,26,26,26,26,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,26,26,26,26,26,26,26,26,26,26,26,-47,-48,26,-50,-51,-52,26,26,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,26,26,26,26,26,26,-55,-56,26,26,-53,-54,]),'AND':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,27,-43,-44,57,-46,-21,27,27,27,27,-15,-16,-17,-18,27,27,27,27,27,27,27,27,27,27,27,-22,-23,-24,-45,27,27,57,27,27,27,27,-40,-41,-42,27,27,27,27,27,27,27,27,27,57,57,57,-16,-15,27,27,27,27,27,27,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,27,27,27,27,27,27,27,27,27,27,27,-47,-48,27,-50,-51,-52,27,27,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,27,27,27,27,27,27,-55,-56,27,27,-53,-54,]),'OR':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,28,-43,-44,58,-46,-21,28,28,28,28,-15,-16,-17,-18,28,28,28,28,28,28,28,28,28,28,28,-22,-23,-24,-45,28,28,58,28,28,28,28,-40,-41,-42,28,28,28,28,28,28,28,28,28,58,58,58,-16,-15,28,28,28,28,28,28,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,28,28,28,28,28,28,28,28,28,28,28,-47,-48,28,-50,-51,-52,28,28,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,28,28,28,28,28,28,-55,-56,28,28,-53,-54,]),'NOT':([2,3,8,9,30,31,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,71,78,79,80,81,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,144,145,146,147,148,149,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,193,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,236,237,238,239,242,243,244,245,248,249,],[-46,29,-43,-44,59,-46,-21,29,29,29,29,-15,-16,-17,-18,29,29,29,29,29,29,29,29,29,29,29,-22,-23,-24,-45,29,29,59,29,29,29,29,-40,-41,-42,29,29,29,29,29,29,29,29,29,59,59,59,-16,-15,29,29,29,29,29,29,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,29,29,29,29,29,29,29,29,29,29,29,-47,-48,29,-50,-51,-52,29,29,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,29,29,29,29,29,29,-55,-56,29,29,-53,-54,]),'PARDER':([8,9,30,31,32,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,71,78,79,80,102,103,104,105,106,107,108,109,110,111,112,114,115,116,117,118,119,120,121,122,123,124,127,144,145,146,147,148,149,159,160,161,162,163,164,165,166,193,194,196,197,198,203,204,205,206,207,208,209,210,211,212,213,214,215,226,227,242,243,248,249,],[-43,-44,56,-46,-21,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,56,102,103,104,-40,-41,-42,125,126,127,128,129,130,131,132,56,56,56,-16,-15,144,145,146,147,148,149,152,-31,-32,-33,-34,-35,-36,-15,-16,-17,-16,-15,-17,-15,-16,-47,-48,-50,-51,-52,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,230,231,-55,-56,-53,-54,]),'LLADER':([8,9,31,32,33,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,102,103,104,144,145,146,147,148,149,171,172,174,175,176,193,194,195,196,197,198,203,204,205,206,207,208,209,210,211,212,213,214,215,220,221,238,239,242,243,246,247,248,249,],[-43,-44,-46,-21,61,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-40,-41,-42,-31,-32,-33,-34,-35,-36,193,194,196,197,198,-47,-48,215,-50,-51,-52,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,224,225,242,243,-55,-56,248,249,-53,-54,]),'CORDER':([8,9,31,32,34,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,102,103,104,144,145,146,147,148,149,193,194,196,197,198,203,204,205,206,207,208,209,210,211,212,213,214,215,242,243,248,249,],[-43,-44,-46,-21,62,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-40,-41,-42,-31,-32,-33,-34,-35,-36,-47,-48,-50,-51,-52,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,-55,-56,-53,-54,]),'PUNTOCOMA':([8,9,31,32,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,102,103,104,113,144,145,146,147,148,149,181,182,183,184,185,186,187,188,189,190,191,192,193,194,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,242,243,244,245,248,249,],[-43,-44,-46,-21,67,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-40,-41,-42,133,-31,-32,-33,-34,-35,-36,203,204,205,206,207,208,209,210,211,212,213,214,-47,-48,-50,-51,-52,218,219,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-12,-14,-49,220,221,-55,-56,246,247,-53,-54,]),'PLUSPLUS':([222,223,],[226,227,]),'SINO':([224,225,],[228,229,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,4,5,6,7,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,37,40,57,58,59,60,68,69,70,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,134,135,136,137,138,139,140,141,150,151,153,154,155,156,157,167,168,169,170,173,179,180,199,200,232,233,234,235,240,241,],[3,30,32,33,34,35,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,64,65,71,78,79,80,81,41,42,43,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,159,160,161,162,163,164,165,166,171,172,174,175,176,177,178,189,190,191,192,195,201,202,216,217,236,237,238,239,244,245,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','analizador_sintactico.py',18),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',22),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion SUMA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',28),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion RESTA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',29),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion SUMA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',30),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion RESTA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',31),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion MULT PARIZQ expresion SUMA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',32),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion MULT PARIZQ expresion RESTA expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',33),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion SUMA PARIZQ expresion MULT expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',34),
  ('expresion -> IDENTIFICADOR ASIGNAR expresion RESTA PARIZQ expresion MULT expresion PARDER PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',35),
  ('expresion -> IDENTIFICADOR ASIGNAR PARIZQ expresion RESTA expresion PARDER DIV expresion PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',36),
  ('expresion -> IDENTIFICADOR ASIGNAR PARIZQ expresion SUMA expresion PARDER DIV expresion PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',37),
  ('expresion -> IDENTIFICADOR ASIGNAR PARIZQ expresion RESTA expresion PARDER MULT expresion PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',38),
  ('expresion -> IDENTIFICADOR ASIGNAR PARIZQ expresion SUMA expresion PARDER MULT expresion PUNTOCOMA','expresion',10,'p_expresion_formulascomplejas','analizador_sintactico.py',39),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',60),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',61),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',62),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',63),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',64),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',65),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizador_sintactico.py',87),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',92),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',93),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',94),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',100),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',101),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',102),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',103),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',104),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',105),
  ('expresion -> PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',106),
  ('expresion -> PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',107),
  ('expresion -> PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',108),
  ('expresion -> PARIZQ expresion PARDER MAYORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',109),
  ('expresion -> PARIZQ expresion PARDER IGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',110),
  ('expresion -> PARIZQ expresion PARDER DISTINTO PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',111),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',137),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',138),
  ('expresion -> expresion NOT expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',139),
  ('expresion -> PARIZQ expresion AND expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',140),
  ('expresion -> PARIZQ expresion OR expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',141),
  ('expresion -> PARIZQ expresion NOT expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',142),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizador_sintactico.py',161),
  ('expresion -> FLOAT','expresion',1,'p_expresion_numero','analizador_sintactico.py',162),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','analizador_sintactico.py',167),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizador_sintactico.py',173),
  ('expresion -> MIENTRAS PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion LLADER','expresion',9,'p_expresion_bucles','analizador_sintactico.py',182),
  ('expresion -> MIENTRAS PARIZQ expresion MAYORQUE expresion PARDER LLAIZQ expresion LLADER','expresion',9,'p_expresion_bucles','analizador_sintactico.py',183),
  ('expresion -> MIENTRAS PARIZQ expresion IGUAL expresion PARDER PARDER LLAIZQ expresion LLADER','expresion',10,'p_expresion_bucles','analizador_sintactico.py',184),
  ('expresion -> SI PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion LLADER','expresion',9,'p_expresion_bucles','analizador_sintactico.py',185),
  ('expresion -> SI PARIZQ expresion MAYORQUE expresion PARDER LLAIZQ expresion LLADER','expresion',9,'p_expresion_bucles','analizador_sintactico.py',186),
  ('expresion -> SI PARIZQ expresion IGUAL expresion PARDER LLAIZQ expresion LLADER','expresion',9,'p_expresion_bucles','analizador_sintactico.py',187),
  ('expresion -> SI PARIZQ expresion MENORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER','expresion',19,'p_expresion_bucles','analizador_sintactico.py',188),
  ('expresion -> SI PARIZQ expresion MAYORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER','expresion',19,'p_expresion_bucles','analizador_sintactico.py',189),
  ('expresion -> PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER','expresion',16,'p_expresion_bucles','analizador_sintactico.py',190),
  ('expresion -> PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MENORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER','expresion',16,'p_expresion_bucles','analizador_sintactico.py',191),
]
