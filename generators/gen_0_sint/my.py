import ply.lex as lex
import re
tokens = (
   'SPACE',
   'ENDLINE',
   'ENDFILE',
   'REG',
   'INT',
   'INCLUDE',
   'WORD',
   'SEP'
)
t_SPACE   = 'inf.readSpace\(\)'
t_ENDLINE = 'inf.readEoln\(\)'
t_ENDFILE = 'inf.readEof\(\)'
t_REG = 'registerValidation\(argc,[ ]*argv\);\n'
t_INCLUDE = '[#]include[^\n\t]+\n'
t_WORD = '[^ \n\t]+'
t_SEP = '[ \n\t]'
def t_INT(t):
    r'inf\.readInt\([^,;\)\n\t]+, [^,;\)\n\t]+\)'
    t.value = re.findall(r"inf\.readInt\(([^,;\)\n\t]+), ([^,;\)\n\t]+)\)", t.value)
    return t
t_ignore  = '[]'
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
s = '''#include<iostream>
#include<string>
#include<vector>
#include <random>
#include <chrono>
using namespace std;
mt19937_64 rnd(chrono::steady_clock::now().time_since_epoch().count());
int next(int a, int b){
    return a + rnd()%(b - a + 1);
}
int processInt(int a, int b){
    int res = next(a, b);
    cout << res;
    return res;
}
void processSpace(){
    cout << ' ';
}
void processEoln(){
    cout << endl;
}
void processEof(){
    
}
'''
file = open("validator.cpp")
val_text = file.read()
lexer.input(val_text)
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'INCLUDE' or tok.type == 'REG':
       continue
    if tok.type == 'SEP' or tok.type == 'WORD':
       s += tok.value
    if tok.type == 'INT':
       s += "processInt(" + tok.value[0][0] + ", " + tok.value[0][1] + ")"
    if tok.type == 'SPACE':
       s += "processSpace()"
    if tok.type == 'ENDLINE':
       s += 'processEoln()'
    if tok.type == 'ENDFILE':
       s += 'processEof()'
print(s)
