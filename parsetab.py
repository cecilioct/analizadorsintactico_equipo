
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ASIGNAR CADENA COMA COMDOB CORDER CORIZQ COUT DECIMAL DISTINTO DIV ENTERO FINALLY FLOAT GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO SUMA THEN USING VOID decdeclaracion :  dec IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion\n    expresion : expresion SUMA PARIZQ expresion SUMA expresion PARDER\n              | expresion SUMA PARIZQ expresion RESTA expresion PARDER\n              | expresion RESTA PARIZQ expresion SUMA expresion PARDER \n              | expresion RESTA PARIZQ expresion RESTA expresion PARDER \n              | expresion MULT PARIZQ expresion SUMA expresion PARDER \n              | expresion MULT PARIZQ expresion RESTA expresion PARDER\n              | expresion SUMA PARIZQ expresion MULT expresion PARDER\n              | expresion RESTA PARIZQ expresion MULT expresion PARDER\n              | PARIZQ expresion RESTA expresion PARDER DIV expresion\n              | PARIZQ expresion SUMA  expresion PARDER DIV expresion\n              | PARIZQ expresion RESTA expresion PARDER MULT expresion\n              | ASIGNAR PARIZQ expresion SUMA  expresion PARDER MULT expresion \n    \n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n               \n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    \n    expresion : ENTERO\n              | FLOAT   \n    expresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR\n    expresion : MIENTRAS PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | MIENTRAS PARIZQ expresion MAYORQUE  expresion PARDER LLAIZQ expresion LLADER\n              | MIENTRAS PARIZQ expresion IGUAL expresion PARDER PARDER LLAIZQ expresion LLADER\n              | SI PARIZQ expresion MENORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion MAYORQUE expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion IGUAL expresion PARDER LLAIZQ expresion  LLADER\n              | SI PARIZQ expresion MENORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER\n              | SI PARIZQ expresion MAYORIGUAL expresion PARDER LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER SINO LLAIZQ expresion IGUAL expresion PUNTOCOMA LLADER\n              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER\n              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MENORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ expresion LLADER\n\n\n    '
    
_lr_action_items = {'dec':([0,],[2,]),'PARIZQ':([0,4,6,7,8,9,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,79,80,81,82,83,84,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[6,17,6,6,6,6,6,38,39,40,6,44,46,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,46,44,6,6,6,44,109,110,111,112,113,114,6,6,6,6,6,6,6,6,6,44,46,48,46,44,48,44,46,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'ASIGNAR':([0,6,7,8,9,12,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,72,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[4,4,4,4,4,4,41,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,97,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'RESTA':([0,3,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,78,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,109,110,111,112,113,114,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,176,177,178,179,180,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,220,221,222,223,224,225,226,227,228,229,230,231,232,233,236,237,],[7,-46,19,7,7,7,7,-43,-44,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,61,-21,19,19,19,7,7,7,19,-15,7,-16,7,-17,7,-18,19,19,19,19,19,19,19,19,19,19,19,7,-22,7,7,7,7,-23,-24,-45,19,19,19,7,101,103,107,-16,-15,19,19,19,7,7,7,7,7,7,7,7,7,-15,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-40,-41,-42,19,19,19,19,19,19,19,19,19,-15,-16,-17,-16,-15,-17,-15,-16,7,7,19,19,19,19,19,19,7,7,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,7,7,7,7,7,7,7,-14,19,19,7,19,19,19,19,19,7,7,-47,-48,19,-50,-51,-52,7,7,19,19,-49,19,19,7,7,7,7,19,19,19,19,7,7,-55,-56,19,19,-53,-54,]),'LLAIZQ':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,146,147,149,150,151,152,153,155,173,174,175,176,177,178,179,180,185,191,192,199,200,216,217,218,219,220,221,222,223,228,229,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,173,174,176,177,178,179,180,8,8,8,185,8,8,8,8,8,8,8,8,8,8,220,221,222,223,8,8,8,8,8,8,]),'CORIZQ':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'ENTERO':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'FLOAT':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'COMDOB':([0,3,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,116,117,118,137,138,145,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,176,177,178,179,180,182,185,191,192,193,194,196,197,198,199,200,203,220,221,222,223,228,229,230,231,236,237,],[12,-46,12,12,12,12,-43,-44,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-21,69,12,12,12,-15,12,-16,12,-17,12,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,12,-22,12,12,12,12,-23,-24,-45,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-40,-41,-42,12,12,12,12,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,12,12,12,12,12,12,12,-14,12,12,12,-47,-48,-50,-51,-52,12,12,-49,12,12,12,12,12,12,-55,-56,-53,-54,]),'IDENTIFICADOR':([0,2,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,40,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,154,155,173,174,176,177,178,179,180,185,191,192,199,200,206,207,220,221,222,223,228,229,],[3,16,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,72,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,181,3,3,3,3,3,3,3,3,3,3,3,3,3,210,211,3,3,3,3,3,3,]),'MIENTRAS':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'SI':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'PARA':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'$end':([1,3,5,10,11,34,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,98,116,117,118,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,193,194,196,197,198,203,230,231,236,237,],[0,-46,-2,-43,-44,-21,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-1,-40,-41,-42,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,-47,-48,-50,-51,-52,-49,-55,-56,-53,-54,]),'SUMA':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,18,-43,-44,63,-21,18,18,18,74,-15,-16,-17,-18,18,18,18,18,18,18,18,18,18,18,18,-22,-23,-24,-45,18,18,18,100,104,106,-16,-15,18,18,18,-15,-40,-41,-42,18,18,18,18,18,18,18,18,18,-15,-16,-17,-16,-15,-17,-15,-16,18,18,18,18,18,18,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,18,18,18,18,18,18,18,-47,-48,18,-50,-51,-52,18,18,-49,18,18,18,18,18,18,-55,-56,18,18,-53,-54,]),'MULT':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,108,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,20,-43,-44,20,-21,20,20,20,20,20,20,-17,-18,20,20,20,20,20,20,20,20,20,20,20,-22,-23,-24,-45,20,20,20,102,105,20,20,20,20,20,20,20,138,-40,-41,-42,20,20,20,20,20,20,20,20,20,155,20,20,-17,20,20,-17,20,20,20,20,20,20,20,20,-3,138,-9,138,-5,-10,-7,138,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,20,20,20,20,20,20,20,-47,-48,20,-50,-51,-52,20,20,-49,20,20,20,20,20,20,-55,-56,20,20,-53,-54,]),'DIV':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,108,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,21,-43,-44,21,-21,21,21,21,21,21,21,-17,-18,21,21,21,21,21,21,21,21,21,21,21,-22,-23,-24,-45,21,21,21,21,21,21,21,21,21,21,21,21,137,145,-40,-41,-42,21,21,21,21,21,21,21,21,21,21,21,-17,21,21,-17,21,21,21,21,21,21,21,21,145,137,-9,137,145,-10,145,137,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,21,21,21,21,21,21,21,-47,-48,21,-50,-51,-52,21,21,-49,21,21,21,21,21,21,-55,-56,21,21,-53,-54,]),'POTENCIA':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,22,-43,-44,22,-21,22,22,22,22,-15,-16,-17,-18,22,22,22,22,22,22,22,22,22,22,22,-22,-23,-24,-45,22,22,22,22,22,22,-16,-15,22,22,22,-15,-40,-41,-42,22,22,22,22,22,22,22,22,22,-15,-16,-17,-16,-15,-17,-15,-16,22,22,22,22,22,22,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,22,22,22,22,22,22,22,-47,-48,22,-50,-51,-52,22,22,-49,22,22,22,22,22,22,-55,-56,22,22,-53,-54,]),'MODULO':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,23,-43,-44,23,-21,23,23,23,23,-15,-16,-17,-18,23,23,23,23,23,23,23,23,23,23,23,-22,-23,-24,-45,23,23,23,23,23,23,-16,-15,23,23,23,-15,-40,-41,-42,23,23,23,23,23,23,23,23,23,-15,-16,-17,-16,-15,-17,-15,-16,23,23,23,23,23,23,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,23,23,23,23,23,23,23,-47,-48,23,-50,-51,-52,23,23,-49,23,23,23,23,23,23,-55,-56,23,23,-53,-54,]),'MENORQUE':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,181,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,24,-43,-44,24,-21,24,24,24,24,-15,-16,-17,-18,24,24,24,24,24,24,24,24,24,24,24,79,-23,-24,-45,89,92,24,24,24,24,-16,-15,24,24,24,-15,-40,-41,-42,24,24,24,24,24,24,24,24,24,-15,-16,-17,-16,-15,-17,-15,-16,24,24,24,24,24,24,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,192,-14,24,24,24,24,24,24,24,-47,-48,24,-50,-51,-52,24,24,-49,24,24,24,24,24,24,-55,-56,24,24,-53,-54,]),'MAYORQUE':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,181,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,25,-43,-44,25,-21,25,25,25,25,-15,-16,-17,-18,25,25,25,25,25,25,25,25,25,25,25,80,-23,-24,-45,90,93,25,25,25,25,-16,-15,25,25,25,-15,-40,-41,-42,25,25,25,25,25,25,25,25,25,-15,-16,-17,-16,-15,-17,-15,-16,25,25,25,25,25,25,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,191,-14,25,25,25,25,25,25,25,-47,-48,25,-50,-51,-52,25,25,-49,25,25,25,25,25,25,-55,-56,25,25,-53,-54,]),'MENORIGUAL':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,26,-43,-44,26,-21,26,26,26,26,-15,-16,-17,-18,26,26,26,26,26,26,26,26,26,26,26,81,-23,-24,-45,26,95,26,26,26,26,-16,-15,26,26,26,-15,-40,-41,-42,26,26,26,26,26,26,26,26,26,-15,-16,-17,-16,-15,-17,-15,-16,26,26,26,26,26,26,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,26,26,26,26,26,26,26,-47,-48,26,-50,-51,-52,26,26,-49,26,26,26,26,26,26,-55,-56,26,26,-53,-54,]),'MAYORIGUAL':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,27,-43,-44,27,-21,27,27,27,27,-15,-16,-17,-18,27,27,27,27,27,27,27,27,27,27,27,82,-23,-24,-45,27,96,27,27,27,27,-16,-15,27,27,27,-15,-40,-41,-42,27,27,27,27,27,27,27,27,27,-15,-16,-17,-16,-15,-17,-15,-16,27,27,27,27,27,27,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,27,27,27,27,27,27,27,-47,-48,27,-50,-51,-52,27,27,-49,27,27,27,27,27,27,-55,-56,27,27,-53,-54,]),'IGUAL':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,28,-43,-44,28,-21,28,28,28,28,-15,-16,-17,-18,28,28,28,28,28,28,28,28,28,28,28,83,-23,-24,-45,91,94,28,28,28,28,-16,-15,28,28,28,-15,-40,-41,-42,28,28,28,28,28,28,28,28,28,-15,-16,-17,-16,-15,-17,-15,-16,28,28,28,28,28,28,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,28,28,28,28,28,199,200,-47,-48,28,-50,-51,-52,28,28,-49,28,28,228,229,28,28,-55,-56,28,28,-53,-54,]),'DISTINTO':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,29,-43,-44,29,-21,29,29,29,29,-15,-16,-17,-18,29,29,29,29,29,29,29,29,29,29,29,84,-23,-24,-45,29,29,29,29,29,29,-16,-15,29,29,29,-15,-40,-41,-42,29,29,29,29,29,29,29,29,29,-15,-16,-17,-16,-15,-17,-15,-16,29,29,29,29,29,29,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,29,29,29,29,29,29,29,-47,-48,29,-50,-51,-52,29,29,-49,29,29,29,29,29,29,-55,-56,29,29,-53,-54,]),'AND':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,30,-43,-44,64,-21,30,30,30,30,-15,-16,-17,-18,30,30,30,30,30,30,30,30,30,30,30,-22,-23,-24,-45,30,30,30,64,64,64,-16,-15,30,30,30,-15,-40,-41,-42,30,30,30,30,30,30,30,30,30,-15,-16,-17,-16,-15,-17,-15,-16,30,30,30,30,30,30,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,30,30,30,30,30,30,30,-47,-48,30,-50,-51,-52,30,30,-49,30,30,30,30,30,30,-55,-56,30,30,-53,-54,]),'OR':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,31,-43,-44,65,-21,31,31,31,31,-15,-16,-17,-18,31,31,31,31,31,31,31,31,31,31,31,-22,-23,-24,-45,31,31,31,65,65,65,-16,-15,31,31,31,-15,-40,-41,-42,31,31,31,31,31,31,31,31,31,-15,-16,-17,-16,-15,-17,-15,-16,31,31,31,31,31,31,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,31,31,31,31,31,31,31,-47,-48,31,-50,-51,-52,31,31,-49,31,31,31,31,31,31,-55,-56,31,31,-53,-54,]),'NOT':([3,5,10,11,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,70,71,73,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,189,190,193,194,195,196,197,198,201,202,203,204,205,224,225,226,227,230,231,232,233,236,237,],[-46,32,-43,-44,66,-21,32,32,32,32,-15,-16,-17,-18,32,32,32,32,32,32,32,32,32,32,32,-22,-23,-24,-45,32,32,32,66,66,66,-16,-15,32,32,32,-15,-40,-41,-42,32,32,32,32,32,32,32,32,32,-15,-16,-17,-16,-15,-17,-15,-16,32,32,32,32,32,32,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,32,32,32,32,32,32,32,-47,-48,32,-50,-51,-52,32,32,-49,32,32,32,32,32,32,-55,-56,32,32,-53,-54,]),'PARDER':([3,10,11,33,34,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,75,76,77,78,85,86,87,88,99,116,117,118,119,120,121,122,123,124,125,126,129,130,131,132,133,134,135,136,139,140,141,142,143,144,148,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,193,194,196,197,198,203,214,215,230,231,236,237,],[-46,-43,-44,62,-21,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,62,62,62,-16,-15,116,117,118,128,-40,-41,-42,146,147,148,149,150,151,152,153,-15,-16,-17,-16,-15,-17,-15,-16,166,167,168,169,170,171,175,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,-47,-48,-50,-51,-52,-49,218,219,-55,-56,-53,-54,]),'LLADER':([3,10,11,34,35,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,116,117,118,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,183,184,186,187,188,193,194,195,196,197,198,203,208,209,226,227,230,231,234,235,236,237,],[-46,-43,-44,-21,67,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-40,-41,-42,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,193,194,196,197,198,-47,-48,203,-50,-51,-52,-49,212,213,230,231,-55,-56,236,237,-53,-54,]),'CORDER':([3,10,11,34,36,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,116,117,118,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,193,194,196,197,198,203,230,231,236,237,],[-46,-43,-44,-21,68,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,-40,-41,-42,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,-47,-48,-50,-51,-52,-49,-55,-56,-53,-54,]),'PUNTOCOMA':([3,10,11,34,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,62,67,68,69,73,116,117,118,127,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,182,193,194,196,197,198,201,202,203,204,205,230,231,232,233,236,237,],[-46,-43,-44,-21,-15,-16,-17,-18,-19,-20,-25,-26,-27,-28,-29,-30,-37,-38,-39,-22,-23,-24,-45,98,-40,-41,-42,154,-3,-4,-9,-6,-5,-10,-7,-8,-11,-13,-31,-32,-33,-34,-35,-36,-12,-14,-47,-48,-50,-51,-52,206,207,-49,208,209,-55,-56,234,235,-53,-54,]),'PLUSPLUS':([210,211,],[214,215,]),'SINO':([212,213,],[216,217,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,6,7,8,9,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,38,39,41,44,46,48,61,63,64,65,66,74,89,90,91,92,93,94,95,96,97,100,101,102,103,104,105,106,107,109,110,111,112,113,114,137,138,145,155,173,174,176,177,178,179,180,185,191,192,199,200,220,221,222,223,228,229,],[5,33,34,35,36,37,42,43,45,47,49,50,51,52,53,54,55,56,57,58,59,60,70,71,73,75,76,77,78,85,86,87,88,99,119,120,121,122,123,124,125,126,127,129,130,131,132,133,134,135,136,139,140,141,142,143,144,164,165,172,182,183,184,186,187,188,189,190,195,201,202,204,205,224,225,226,227,232,233,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> dec IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar','analizador_sintactico.py',18),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',22),
  ('expresion -> expresion SUMA PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',28),
  ('expresion -> expresion SUMA PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',29),
  ('expresion -> expresion RESTA PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',30),
  ('expresion -> expresion RESTA PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',31),
  ('expresion -> expresion MULT PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',32),
  ('expresion -> expresion MULT PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',33),
  ('expresion -> expresion SUMA PARIZQ expresion MULT expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',34),
  ('expresion -> expresion RESTA PARIZQ expresion MULT expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',35),
  ('expresion -> PARIZQ expresion RESTA expresion PARDER DIV expresion','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',36),
  ('expresion -> PARIZQ expresion SUMA expresion PARDER DIV expresion','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',37),
  ('expresion -> PARIZQ expresion RESTA expresion PARDER MULT expresion','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',38),
  ('expresion -> ASIGNAR PARIZQ expresion SUMA expresion PARDER MULT expresion','expresion',8,'p_expresion_formulascomplejas','analizador_sintactico.py',39),
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
