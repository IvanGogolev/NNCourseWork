import ply.lex as lex
import re
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
using namespace std;
mt19937_64 rnd(chrono::steady_clock::now().time_since_epoch().count());
map<string, int> __STRATEGY{{{0}}};
int next(int a, int b) {{
    return a + rnd()%(b - a + 1);
}}
int processInt(int l, int r) {{
    int res = next(l, r);
    cout << res;
    return res;
}}
int processInt(int l, int r, const string& name) {{
    int res = 0;
    if(__STRATEGY.count(name)) {{
        if(__STRATEGY[name] == 1)res = l;
        else if(__STRATEGY[name] == 2)res = r;
        else res = next(l, r);
    }}else {{
        res = next(l, r);
    }}
    cout << res;
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
       end += "processInt(" + tok.value[0][0] + ", " + tok.value[0][1] + ", " + cur + ")"
       var_names.append(cur)
    if tok.type == 'SPACE':
       end += "processSpace()"
    if tok.type == 'ENDLINE':
       end += 'processEoln()'
    if tok.type == 'ENDFILE':
       end += 'processEof()'
print(s.format(strategy) + end, file = open("gen.cpp", mode="w"))

for i in range(pow(2, len(var_names))):
    strategy = ""
    for j in range(len(var_names)):
        if j:
            strategy += ","
        if i & pow(2, j):
            strategy += "{" + str(var_names[j]) + ", 2}\n"
        else:
            strategy += "{" + str(var_names[j]) + ", 1}\n"
    file_name = "gen" + str(i) + ".cpp"
    print(s.format(strategy) + end, file = open(file_name, mode="w"))
