import ply.lex as lex
import re
import os
tokens = (
   'SPACE',
   'ENDLINE',
   'ENDFILE',
   'REG',
   'INT3',
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
def t_INT3(t):
    r'inf\.readInt\([^,;\)\n\t]+, [^,;\)\n\t]+, [^,;\)\n\t]+\)'
    t.value = re.findall(r"inf\.readInt\(([^,;\)\n\t]+), ([^,;\)\n\t]+), ([^,;\)\n\t]+)\)", t.value)
    return t
t_ignore  = '[]'
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()

strategy = ""
s = '''#include<iostream>
#include<string>
#include<vector>
#include <random>
#include <chrono>
#include <map>
#include <fstream>
using namespace std;
mt19937_64 rnd(chrono::steady_clock::now().time_since_epoch().count());
map<string, int> __STRATEGY{{{0}}};
int next(int a, int b) {{
    return a + rnd()%(b - a + 1);
}}
int processInt(int l, int r, const string& name) {{
    int res;
    cin >> res;
    ofstream fout(name + ".txt", ios::app);
    fout << res << " " << l << " " << r << endl;
    fout.close();
    return res;
}}
void processSpace() {{
    cout << ' ';
}}
void processEoln() {{
    cout << endl;
}}
void processEof() {{
    
}}
'''
file = open("validator.cpp")
val_text = file.read()
lexer.input(val_text)
q = 0
var_names = []
end = ""
while True:
    q += 1
    cur = "\"" + str(q) + "\""
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'INCLUDE' or tok.type == 'REG':
       continue
    if tok.type == 'SEP' or tok.type == 'WORD':
       end += tok.value
    if tok.type == 'INT3' or tok.type == 'INT':
       if tok.type == 'INT3':
           cur = tok.value[0][2]
       end += "processInt(" + tok.value[0][0] + ", " + tok.value[0][1] + ", " + cur + ")"
       var_names.append(cur)
    if tok.type == 'SPACE':
       end += "processSpace()"
    if tok.type == 'ENDLINE':
       end += 'processEoln()'
    if tok.type == 'ENDFILE':
       end += 'processEof()'
print(s.format(strategy) + end, file = open("agr.cpp", mode="w"))
os.system("g++ -o agr.exe agr.cpp")
dr = input("введите относительный адрес папки с тестами\n")
print(len(var_names))
arr = []
for x in os.listdir(dr):
    if x[-4:] == ".txt" or x[-3:] == ".in":
        file_path = dr + "/" + x
        os.system("agr.exe < " + file_path)
os.system("del agr.exe")
os.system("del agr.cpp")
for y in var_names:
    x = y[1:-1]
    
    print("variable " + x)
    L = pow(2, 200)
    R = -L
    fl = 0
    fr = 0
    with open(x + ".txt", 'r', encoding='utf-8') as file:
        for line in file:
            x, l, r = line.split()
            x = int(x)
            l = int(l)
            r = int(r)
            if x == l:
                fl = 1
            if x == r:
                fr = 1
            L = min(L, x)
            R = max(R, x)
    print("min value ", L)
    print("max value ", R)
    print("assgn min ", fl)
    print("assign max ", fr)
for y in var_names:
    x = y[1:-1]
    os.system("del " + x + ".txt")
        
