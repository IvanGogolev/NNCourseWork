import ply.lex as lex
import re
tokens = (
   'MAINFUN',
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
t_MAINFUN = 'int[ ]+main\(int[ ]+argc,[ ]+char[ ]+\*argv\[\]\)'
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
int last = -1;
vector<int> vars;
int q_pr_in = 0;
int q_pr_out = 0;
int processInt(int l, int r, const string& name, int f_in) {{
    if(f_in) {{
        int var;
        cin >> var;
        vars.push_back(var);
        q_pr_in++;
        if(var != r)last = q_pr_in;
        return var;
    }}else {{
        q_pr_out++;
        int res = -1;
        if(q_pr_out < last) {{
            res = vars[q_pr_out - 1];
        }} else if(q_pr_out == last) {{
            res = vars[q_pr_out - 1] + 1;
        }} else {{
            res =  l;
        }}
        cout << res;
        return res;
    }}
}}
void processSpace(int f_in) {{
    if(!f_in)cout << ' ';
}}
void processEoln(int f_in) {{
    if(!f_in)cout << endl;
}}
void processEof(int f_in) {{
    
}}
int f_in = 1;
void process();
int main(int argc, char *argv[]) {{
    process();
    f_in = 0;
    process();
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
    if tok.type == 'MAINFUN':
       end += "void process()\n"
       
    if tok.type == 'SEP' or tok.type == 'WORD':
       end += tok.value
    if tok.type == 'INT3' or tok.type == 'INT':
       end += "processInt(" + tok.value[0][0] + ", " + tok.value[0][1] + ", " + cur + ", f_in" + ")"
       var_names.append(cur)
    if tok.type == 'SPACE':
       end += "processSpace(f_in)"
    if tok.type == 'ENDLINE':
       end += 'processEoln(f_in)'
    if tok.type == 'ENDFILE':
       end += 'processEof(f_in)'

print(s.format(strategy) + end, file = open("gen.cpp", mode="w"))


