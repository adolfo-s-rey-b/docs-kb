### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/index.html "Python built-ins reference")
     |
*   [previous](https://docs.python.org/3/reference/toplevel_components.html "9. Top-level components")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python Language Reference](https://docs.python.org/3/reference/index.html)
     »
*   [10\. Full Grammar specification](https://docs.python.org/3/reference/grammar.html)
    
*    
    
    |
*   Theme Auto Light Dark |

10\. Full Grammar specification[¶](https://docs.python.org/3/reference/grammar.html#full-grammar-specification "Link to this heading")

=======================================================================================================================================

This is the full Python grammar, derived directly from the grammar used to generate the CPython parser (see [Grammar/python.gram](https://github.com/python/cpython/tree/3.15/Grammar/python.gram)
). The version here omits details related to code generation and error recovery.

The notation used here is the same as in the preceding docs, and is described in the [notation](https://docs.python.org/3/reference/introduction.html#notation)
 section, except for an extra complication:

*   `~` (“cut”): commit to the current alternative; fail the rule if the alternative fails to parse
    
    Python mainly uses cuts for optimizations or improved error messages. They often appear to be useless in the listing below.
    
    Cuts currently don’t appear inside parentheses, brackets, lookaheads and similar. Their behavior in these contexts is deliberately left unspecified.
    

\# PEG grammar for Python

\# ========================= START OF THE GRAMMAR =========================

\# General grammatical elements and rules:
#
\# \* Strings with double quotes (") denote SOFT KEYWORDS
\# \* Strings with single quotes (') denote KEYWORDS
\# \* Upper case names (NAME) denote tokens in the Grammar/Tokens file
\# \* Rule names starting with "invalid\_" are used for specialized syntax errors
\#     - These rules are NOT used in the first pass of the parser.
\#     - Only if the first pass fails to parse, a second pass including the invalid
\#       rules will be executed.
\#     - If the parser fails in the second phase with a generic syntax error, the
\#       location of the generic failure of the first pass will be used (this avoids
\#       reporting incorrect locations due to the invalid rules).
\#     - The order of the alternatives involving invalid rules matter
\#       (like any rule in PEG).
#
\# Grammar Syntax (see PEP 617 for more information):
#
\# rule\_name: expression
\#   Optionally, a type can be included right after the rule name, which
\#   specifies the return type of the C or Python function corresponding to the
\#   rule:
\# rule\_name\[return\_type\]: expression
\#   If the return type is omitted, then a void \* is returned in C and an Any in
\#   Python.
\# e1 e2
\#   Match e1, then match e2.
\# e1 | e2
\#   Match e1 or e2.
\#   The first alternative can also appear on the line after the rule name for
\#   formatting purposes. In that case, a | must be used before the first
\#   alternative, like so:
\#       rule\_name\[return\_type\]:
\#            | first\_alt
\#            | second\_alt
\# ( e )
\#   Match e (allows also to use other operators in the group like '(e)\*')
\# \[ e \] or e?
\#   Optionally match e.
\# e\*
\#   Match zero or more occurrences of e.
\# e+
\#   Match one or more occurrences of e.
\# s.e+
\#   Match one or more occurrences of e, separated by s. The generated parse tree
\#   does not include the separator. This is otherwise identical to (e (s e)\*).
\# &e
\#   Succeed if e can be parsed, without consuming any input.
\# !e
\#   Fail if e can be parsed, without consuming any input.
\# ~
\#   Commit to the current alternative, even if it fails to parse.
\# &&e
\#   Eager parse e. The parser will not backtrack and will immediately
\#   fail with SyntaxError if e cannot be parsed.
#

\# STARTING RULES
\# ==============

file: \[statements\] ENDMARKER 
interactive: statement\_newline 
eval: expressions NEWLINE\* ENDMARKER 
func\_type: '(' \[type\_expressions\] ')' '->' expression NEWLINE\* ENDMARKER 

\# GENERAL STATEMENTS
\# ==================

statements: statement+ 

statement:
    | compound\_stmt 
    | simple\_stmts 

single\_compound\_stmt:
    | compound\_stmt 

statement\_newline:
    | single\_compound\_stmt NEWLINE 
    | simple\_stmts
    | NEWLINE 
    | ENDMARKER 

simple\_stmts:
    | simple\_stmt !';' NEWLINE  \# Not needed, there for speedup
    | ';'.simple\_stmt+ \[';'\] NEWLINE 

\# NOTE: assignment MUST precede expression, else parsing a simple assignment
\# will throw a SyntaxError.
simple\_stmt:
    | assignment
    | type\_alias
    | import\_stmt
    | star\_expressions 
    | return\_stmt
    | raise\_stmt
    | pass\_stmt
    | del\_stmt
    | yield\_stmt
    | assert\_stmt
    | break\_stmt
    | continue\_stmt
    | global\_stmt
    | nonlocal\_stmt

compound\_stmt:
    | function\_def
    | if\_stmt
    | class\_def
    | with\_stmt
    | for\_stmt
    | try\_stmt
    | while\_stmt
    | match\_stmt

\# SIMPLE STATEMENTS
\# =================

\# NOTE: annotated\_rhs may start with 'yield'; yield\_expr must start with 'yield'
assignment:
    | NAME ':' expression \['=' annotated\_rhs \] 
    | ('(' single\_target ')' 
         | single\_subscript\_attribute\_target) ':' expression \['=' annotated\_rhs \] 
    | (star\_targets '=' )+ annotated\_rhs !'=' \[TYPE\_COMMENT\] 
    | single\_target augassign ~ annotated\_rhs 

annotated\_rhs: yield\_expr | star\_expressions

augassign:
    | '+=' 
    | '-=' 
    | '\*=' 
    | '@=' 
    | '/=' 
    | '%=' 
    | '&=' 
    | '|=' 
    | '^=' 
    | '<<=' 
    | '>>=' 
    | '\*\*=' 
    | '//=' 

return\_stmt:
    | 'return' \[star\_expressions\] 

raise\_stmt:
    | 'raise' expression 'from' expression 
    | 'raise' expression 
    | 'raise' 

pass\_stmt:
    | 'pass' 

break\_stmt:
    | 'break' 

continue\_stmt:
    | 'continue' 

global\_stmt: 'global' ','.NAME+ 

nonlocal\_stmt: 'nonlocal' ','.NAME+ 

del\_stmt:
    | 'del' del\_targets &(';' | NEWLINE) 

yield\_stmt: yield\_expr 

assert\_stmt:
    | 'assert' expression \[',' expression \] 

import\_stmt:
    | import\_name
    | import\_from

\# Import statements
\# -----------------

import\_name:
    | "lazy" 'import' dotted\_as\_names 
    | 'import' dotted\_as\_names 

\# note below: the ('.' | '...') is necessary because '...' is tokenized as ELLIPSIS
import\_from:
    | "lazy" 'from' ('.' | '...')\* dotted\_name 'import' import\_from\_targets 
    | "lazy" 'from' ('.' | '...')+ 'import' import\_from\_targets 
    | 'from' ('.' | '...')\* dotted\_name 'import' import\_from\_targets 
    | 'from' ('.' | '...')+ 'import' import\_from\_targets 

import\_from\_targets:
    | '(' import\_from\_as\_names \[','\] ')' 
    | import\_from\_as\_names !','
    | '\*' 
import\_from\_as\_names:
    | ','.import\_from\_as\_name+ 
import\_from\_as\_name:
    | NAME \['as' NAME \] 

dotted\_as\_names:
    | ','.dotted\_as\_name+ 
dotted\_as\_name:
    | dotted\_name \['as' NAME \] 

dotted\_name:
    | dotted\_name '.' NAME 
    | NAME

\# COMPOUND STATEMENTS
\# ===================

\# Common elements
\# ---------------

block:
    | NEWLINE INDENT statements DEDENT 
    | simple\_stmts

decorators: ('@' named\_expression NEWLINE )+ 

\# Class definitions
\# -----------------

class\_def:
    | decorators class\_def\_raw 
    | class\_def\_raw

class\_def\_raw:
    | 'class' NAME \[type\_params\] \['(' \[arguments\] ')' \] ':' block 

\# Function definitions
\# --------------------

function\_def:
    | decorators function\_def\_raw 
    | function\_def\_raw

function\_def\_raw:
    | 'def' NAME \[type\_params\] '(' \[params\] ')' \['->' expression \] ':' \[func\_type\_comment\] block 
    | 'async' 'def' NAME \[type\_params\] '(' \[params\] ')' \['->' expression \] ':' \[func\_type\_comment\] block 

\# Function parameters
\# -------------------

params:
    | parameters

parameters:
    | slash\_no\_default param\_no\_default\* param\_with\_default\* \[star\_etc\] 
    | slash\_with\_default param\_with\_default\* \[star\_etc\] 
    | param\_no\_default+ param\_with\_default\* \[star\_etc\] 
    | param\_with\_default+ \[star\_etc\] 
    | star\_etc 

\# Some duplication here because we can't write (',' | &')'),
\# which is because we don't support empty alternatives (yet).

slash\_no\_default:
    | param\_no\_default+ '/' ',' 
    | param\_no\_default+ '/' &')' 
slash\_with\_default:
    | param\_no\_default\* param\_with\_default+ '/' ',' 
    | param\_no\_default\* param\_with\_default+ '/' &')' 

star\_etc:
    | '\*' param\_no\_default param\_maybe\_default\* \[kwds\] 
    | '\*' param\_no\_default\_star\_annotation param\_maybe\_default\* \[kwds\] 
    | '\*' ',' param\_maybe\_default+ \[kwds\] 
    | kwds 

kwds:
    | '\*\*' param\_no\_default 

\# One parameter.  This \*includes\* a following comma and type comment.
#
\# There are three styles:
\# - No default
\# - With default
\# - Maybe with default
#
\# There are two alternative forms of each, to deal with type comments:
\# - Ends in a comma followed by an optional type comment
\# - No comma, optional type comment, must be followed by close paren
\# The latter form is for a final parameter without trailing comma.
#

param\_no\_default:
    | param ',' TYPE\_COMMENT? 
    | param TYPE\_COMMENT? &')' 
param\_no\_default\_star\_annotation:
    | param\_star\_annotation ',' TYPE\_COMMENT? 
    | param\_star\_annotation TYPE\_COMMENT? &')' 
param\_with\_default:
    | param default ',' TYPE\_COMMENT? 
    | param default TYPE\_COMMENT? &')' 
param\_maybe\_default:
    | param default? ',' TYPE\_COMMENT? 
    | param default? TYPE\_COMMENT? &')' 
param: NAME annotation? 
param\_star\_annotation: NAME star\_annotation 
annotation: ':' expression 
star\_annotation: ':' star\_expression 
default: '=' expression  | invalid\_default

\# If statement
\# ------------

if\_stmt:
    | 'if' named\_expression ':' block elif\_stmt 
    | 'if' named\_expression ':' block \[else\_block\] 
elif\_stmt:
    | 'elif' named\_expression ':' block elif\_stmt 
    | 'elif' named\_expression ':' block \[else\_block\] 
else\_block:
    | 'else' ':' block 

\# While statement
\# ---------------

while\_stmt:
    | 'while' named\_expression ':' block \[else\_block\] 

\# For statement
\# -------------

for\_stmt:
    | 'for' star\_targets 'in' ~ star\_expressions ':' \[TYPE\_COMMENT\] block \[else\_block\] 
    | 'async' 'for' star\_targets 'in' ~ star\_expressions ':' \[TYPE\_COMMENT\] block \[else\_block\] 

\# With statement
\# --------------

with\_stmt:
    | 'with' '(' ','.with\_item+ ','? ')' ':' \[TYPE\_COMMENT\] block 
    | 'with' ','.with\_item+ ':' \[TYPE\_COMMENT\] block 
    | 'async' 'with' '(' ','.with\_item+ ','? ')' ':' block 
    | 'async' 'with' ','.with\_item+ ':' \[TYPE\_COMMENT\] block 

with\_item:
    | expression 'as' star\_target &(',' | ')' | ':') 
    | expression 

\# Try statement
\# -------------

try\_stmt:
    | 'try' ':' block finally\_block 
    | 'try' ':' block except\_block+ \[else\_block\] \[finally\_block\] 
    | 'try' ':' block except\_star\_block+ \[else\_block\] \[finally\_block\] 

\# Except statement
\# ----------------

except\_block:
    | 'except' expression ':' block 
    | 'except' expression 'as' NAME ':' block 
    | 'except' expressions ':' block 
    | 'except' ':' block 
except\_star\_block:
    | 'except' '\*' expression ':' block 
    | 'except' '\*' expression 'as' NAME ':' block 
    | 'except' '\*' expressions ':' block 
finally\_block:
    | 'finally' ':' block 

\# Match statement
\# ---------------

match\_stmt:
    | "match" subject\_expr ':' NEWLINE INDENT case\_block+ DEDENT 

subject\_expr:
    | star\_named\_expression ',' star\_named\_expressions? 
    | named\_expression

case\_block:
    | "case" patterns guard? ':' block 

guard: 'if' named\_expression 

patterns:
    | open\_sequence\_pattern 
    | pattern

pattern:
    | as\_pattern
    | or\_pattern

as\_pattern:
    | or\_pattern 'as' pattern\_capture\_target 

or\_pattern:
    | '|'.closed\_pattern+ 

closed\_pattern:
    | literal\_pattern
    | capture\_pattern
    | wildcard\_pattern
    | value\_pattern
    | group\_pattern
    | sequence\_pattern
    | mapping\_pattern
    | class\_pattern

\# Literal patterns are used for equality and identity constraints
literal\_pattern:
    | signed\_number !('+' | '-') 
    | complex\_number 
    | strings 
    | 'None' 
    | 'True' 
    | 'False' 

\# Literal expressions are used to restrict permitted mapping pattern keys
literal\_expr:
    | signed\_number !('+' | '-')
    | complex\_number
    | strings
    | 'None' 
    | 'True' 
    | 'False' 

complex\_number:
    | signed\_real\_number '+' imaginary\_number 
    | signed\_real\_number '-' imaginary\_number  

signed\_number:
    | NUMBER
    | '+' NUMBER 
    | '-' NUMBER 

signed\_real\_number:
    | real\_number
    | '+' real\_number 
    | '-' real\_number 

real\_number:
    | NUMBER 

imaginary\_number:
    | NUMBER 

capture\_pattern:
    | pattern\_capture\_target 

pattern\_capture\_target:
    | !"\_" NAME !('.' | '(' | '=') 

wildcard\_pattern:
    | "\_" 

value\_pattern:
    | attr !('.' | '(' | '=') 

attr:
    | name\_or\_attr '.' NAME 

name\_or\_attr:
    | attr
    | NAME

group\_pattern:
    | '(' pattern ')' 

sequence\_pattern:
    | '\[' maybe\_sequence\_pattern? '\]' 
    | '(' open\_sequence\_pattern? ')' 

open\_sequence\_pattern:
    | maybe\_star\_pattern ',' maybe\_sequence\_pattern? 

maybe\_sequence\_pattern:
    | ','.maybe\_star\_pattern+ ','? 

maybe\_star\_pattern:
    | star\_pattern
    | pattern

star\_pattern:
    | '\*' pattern\_capture\_target 
    | '\*' wildcard\_pattern 

mapping\_pattern:
    | '{' '}' 
    | '{' double\_star\_pattern ','? '}' 
    | '{' items\_pattern ',' double\_star\_pattern ','? '}' 
    | '{' items\_pattern ','? '}' 

items\_pattern:
    | ','.key\_value\_pattern+

key\_value\_pattern:
    | (literal\_expr | attr) ':' pattern 

double\_star\_pattern:
    | '\*\*' pattern\_capture\_target 

class\_pattern:
    | name\_or\_attr '(' ')' 
    | name\_or\_attr '(' positional\_patterns ','? ')' 
    | name\_or\_attr '(' keyword\_patterns ','? ')' 
    | name\_or\_attr '(' positional\_patterns ',' keyword\_patterns ','? ')' 

positional\_patterns:
    | ','.pattern+ 

keyword\_patterns:
    | ','.keyword\_pattern+

keyword\_pattern:
    | NAME '=' pattern 

\# Type statement
\# ---------------

type\_alias:
    | "type" NAME \[type\_params\] '=' expression 

\# Type parameter declaration
\# --------------------------

type\_params:
    | '\[' type\_param\_seq '\]' 

type\_param\_seq: ','.type\_param+ \[','\] 

type\_param:
    | NAME \[type\_param\_bound\] \[type\_param\_default\] 
    | '\*' NAME \[type\_param\_starred\_default\] 
    | '\*\*' NAME \[type\_param\_default\] 

type\_param\_bound: ':' expression 
type\_param\_default: '=' expression 
type\_param\_starred\_default: '=' star\_expression 

\# EXPRESSIONS
\# -----------

expressions:
    | expression (',' expression )+ \[','\] 
    | expression ',' 
    | expression

expression:
    | if\_expression
    | disjunction
    | lambdef

if\_expression:
    | disjunction 'if' disjunction 'else' expression 

yield\_expr:
    | 'yield' 'from' expression 
    | 'yield' \[star\_expressions\] 

star\_expressions:
    | star\_expression (',' star\_expression )+ \[','\] 
    | star\_expression ',' 
    | star\_expression

star\_expression:
    | '\*' bitwise\_or 
    | expression

star\_named\_expressions: ','.star\_named\_expression+ \[','\] 

star\_named\_expressions\_sequence: ','.star\_named\_expression\_sequence+ \[','\] 

star\_named\_expression:
    | '\*' bitwise\_or 
    | named\_expression

star\_named\_expression\_sequence:
    | star\_named\_expression

assignment\_expression:
    | NAME ':=' ~ expression 

named\_expression:
    | assignment\_expression
    | expression !':='

disjunction:
    | conjunction ('or' conjunction )+ 
    | conjunction

conjunction:
    | inversion ('and' inversion )+ 
    | inversion

inversion:
    | 'not' inversion 
    | comparison

\# Comparison operators
\# --------------------

comparison:
    | bitwise\_or compare\_op\_bitwise\_or\_pair+ 
    | bitwise\_or

compare\_op\_bitwise\_or\_pair:
    | eq\_bitwise\_or
    | noteq\_bitwise\_or
    | lte\_bitwise\_or
    | lt\_bitwise\_or
    | gte\_bitwise\_or
    | gt\_bitwise\_or
    | notin\_bitwise\_or
    | in\_bitwise\_or
    | isnot\_bitwise\_or
    | is\_bitwise\_or

eq\_bitwise\_or: '==' bitwise\_or 
noteq\_bitwise\_or:
    | ('!=' ) bitwise\_or 
lte\_bitwise\_or: '<=' bitwise\_or 
lt\_bitwise\_or: '<' bitwise\_or 
gte\_bitwise\_or: '>=' bitwise\_or 
gt\_bitwise\_or: '>' bitwise\_or 
notin\_bitwise\_or: 'not' 'in' bitwise\_or 
in\_bitwise\_or: 'in' bitwise\_or 
isnot\_bitwise\_or: 'is' 'not' bitwise\_or 
is\_bitwise\_or: 'is' bitwise\_or 

\# Bitwise operators
\# -----------------

bitwise\_or:
    | bitwise\_or '|' bitwise\_xor 
    | bitwise\_xor

bitwise\_xor:
    | bitwise\_xor '^' bitwise\_and 
    | bitwise\_and

bitwise\_and:
    | bitwise\_and '&' shift\_expr 
    | shift\_expr

shift\_expr:
    | shift\_expr '<<' sum 
    | shift\_expr '>>' sum 
    | sum

\# Arithmetic operators
\# --------------------

sum:
    | sum '+' term 
    | sum '-' term 
    | term

term:
    | term '\*' factor 
    | term '/' factor 
    | term '//' factor 
    | term '%' factor 
    | term '@' factor 
    | factor

factor:
    | '+' factor 
    | '-' factor 
    | '~' factor 
    | power

power:
    | await\_primary '\*\*' factor 
    | await\_primary

\# Primary elements
\# ----------------

\# Primary elements are things like "obj.something.something", "obj\[something\]", "obj(something)", "obj" ...

await\_primary:
    | 'await' primary 
    | primary

primary:
    | primary '.' NAME 
    | primary genexp 
    | primary '(' \[arguments\] ')' 
    | primary '\[' slices '\]' 
    | atom

slices:
    | slice !',' 
    | ','.(slice | starred\_expression)+ \[','\] 

slice:
    | \[expression\] ':' \[expression\] \[':' \[expression\] \] 
    | named\_expression 

atom:
    | NAME
    | 'True' 
    | 'False' 
    | 'None' 
    | strings
    | NUMBER
    | (genexp | tuple | group)
    | (listcomp | list)
    | (dictcomp | setcomp | dict | set)
    | '...' 

group:
    | '(' (yield\_expr | named\_expression) ')' 

\# Lambda functions
\# ----------------

lambdef:
    | 'lambda' \[lambda\_params\] ':' expression 

lambda\_params:
    | lambda\_parameters

\# lambda\_parameters etc. duplicates parameters but without annotations
\# or type comments, and if there's no comma after a parameter, we expect
\# a colon, not a close parenthesis.  (For more, see parameters above.)
#
lambda\_parameters:
    | lambda\_slash\_no\_default lambda\_param\_no\_default\* lambda\_param\_with\_default\* \[lambda\_star\_etc\] 
    | lambda\_slash\_with\_default lambda\_param\_with\_default\* \[lambda\_star\_etc\] 
    | lambda\_param\_no\_default+ lambda\_param\_with\_default\* \[lambda\_star\_etc\] 
    | lambda\_param\_with\_default+ \[lambda\_star\_etc\] 
    | lambda\_star\_etc 

lambda\_slash\_no\_default:
    | lambda\_param\_no\_default+ '/' ',' 
    | lambda\_param\_no\_default+ '/' &':' 

lambda\_slash\_with\_default:
    | lambda\_param\_no\_default\* lambda\_param\_with\_default+ '/' ',' 
    | lambda\_param\_no\_default\* lambda\_param\_with\_default+ '/' &':' 

lambda\_star\_etc:
    | '\*' lambda\_param\_no\_default lambda\_param\_maybe\_default\* \[lambda\_kwds\] 
    | '\*' ',' lambda\_param\_maybe\_default+ \[lambda\_kwds\] 
    | lambda\_kwds 

lambda\_kwds:
    | '\*\*' lambda\_param\_no\_default 

lambda\_param\_no\_default:
    | lambda\_param ',' 
    | lambda\_param &':' 
lambda\_param\_with\_default:
    | lambda\_param default ',' 
    | lambda\_param default &':' 
lambda\_param\_maybe\_default:
    | lambda\_param default? ',' 
    | lambda\_param default? &':' 
lambda\_param: NAME 

\# LITERALS
\# ========

fstring\_middle:
    | fstring\_replacement\_field
    | FSTRING\_MIDDLE 
fstring\_replacement\_field:
    | '{' annotated\_rhs '='? \[fstring\_conversion\] \[fstring\_full\_format\_spec\] '}' 
fstring\_conversion:
    | "!" NAME 
fstring\_full\_format\_spec:
    | ':' fstring\_format\_spec\* 
fstring\_format\_spec:
    | FSTRING\_MIDDLE 
    | fstring\_replacement\_field
fstring:
    | FSTRING\_START fstring\_middle\* FSTRING\_END 

tstring\_format\_spec\_replacement\_field:
    | '{' annotated\_rhs '='? \[fstring\_conversion\] \[tstring\_full\_format\_spec\] '}' 
tstring\_format\_spec:
    | TSTRING\_MIDDLE 
    | tstring\_format\_spec\_replacement\_field
tstring\_full\_format\_spec:
    | ':' tstring\_format\_spec\* 
tstring\_replacement\_field:
    | '{' annotated\_rhs '='? \[fstring\_conversion\] \[tstring\_full\_format\_spec\] '}' 
tstring\_middle:
    | tstring\_replacement\_field
    | TSTRING\_MIDDLE 
tstring:
    | TSTRING\_START tstring\_middle\* TSTRING\_END 

string: STRING 
strings:
    | (fstring|string)+ 
    | tstring+ 

list:
    | '\[' \[star\_named\_expressions\_sequence\] '\]' 

tuple:
    | '(' \[star\_named\_expression\_sequence ',' \[star\_named\_expressions\_sequence\]  \] ')' 

set: '{' star\_named\_expressions\_sequence '}' 

\# Dicts
\# -----

dict:
    | '{' \[double\_starred\_kvpairs\] '}' 

double\_starred\_kvpairs: ','.double\_starred\_kvpair+ \[','\] 

double\_starred\_kvpair:
    | '\*\*' bitwise\_or 
    | kvpair

kvpair: expression ':' expression 

\# Comprehensions & Generators
\# ---------------------------

for\_if\_clauses:
    | for\_if\_clause+ 

for\_if\_clause:
    | 'async' 'for' star\_targets 'in' ~ disjunction ('if' disjunction )\* 
    | 'for' star\_targets 'in' ~ disjunction ('if' disjunction )\* 

listcomp:
    | '\[' star\_named\_expression for\_if\_clauses '\]' 

setcomp:
    | '{' star\_named\_expression for\_if\_clauses '}' 

genexp:
    | '(' ( assignment\_expression | expression !':=' | starred\_expression ) for\_if\_clauses ')' 

dictcomp:
    | '{' kvpair for\_if\_clauses '}' 
    | '{' '\*\*' expression for\_if\_clauses '}' 

\# FUNCTION CALL ARGUMENTS
\# =======================

arguments:
    | args \[','\] &')' 

args:
    | ','.(starred\_expression | ( assignment\_expression | expression !':=') !'=')+ \[',' kwargs \] 
    | kwargs 

kwargs:
    | ','.kwarg\_or\_starred+ ',' ','.kwarg\_or\_double\_starred+ 
    | ','.kwarg\_or\_starred+
    | ','.kwarg\_or\_double\_starred+

starred\_expression:
    | '\*' expression 

kwarg\_or\_starred:
    | NAME '=' expression 
    | starred\_expression 

kwarg\_or\_double\_starred:
    | NAME '=' expression 
    | '\*\*' expression 

\# ASSIGNMENT TARGETS
\# ==================

\# Generic targets
\# ---------------

\# NOTE: star\_targets may contain \*bitwise\_or, targets may not.
star\_targets:
    | star\_target !',' 
    | star\_target (',' star\_target )\* \[','\] 

star\_targets\_list\_seq: ','.star\_target+ \[','\] 

star\_targets\_tuple\_seq:
    | star\_target (',' star\_target )+ \[','\] 
    | star\_target ',' 

star\_target:
    | '\*' (!'\*' star\_target) 
    | target\_with\_star\_atom

target\_with\_star\_atom:
    | t\_primary '.' NAME !t\_lookahead 
    | t\_primary '\[' slices '\]' !t\_lookahead 
    | star\_atom

star\_atom:
    | NAME 
    | '(' target\_with\_star\_atom ')' 
    | '(' \[star\_targets\_tuple\_seq\] ')' 
    | '\[' \[star\_targets\_list\_seq\] '\]' 

single\_target:
    | single\_subscript\_attribute\_target
    | NAME 
    | '(' single\_target ')' 

single\_subscript\_attribute\_target:
    | t\_primary '.' NAME !t\_lookahead 
    | t\_primary '\[' slices '\]' !t\_lookahead 

t\_primary:
    | t\_primary '.' NAME &t\_lookahead 
    | t\_primary '\[' slices '\]' &t\_lookahead 
    | t\_primary genexp &t\_lookahead 
    | t\_primary '(' \[arguments\] ')' &t\_lookahead 
    | atom &t\_lookahead 

t\_lookahead: '(' | '\[' | '.'\
\
\# Targets for del statements\
\# --------------------------\
\
del\_targets: ','.del\_target+ \[','\] \
\
del\_target:\
    | t\_primary '.' NAME !t\_lookahead \
    | t\_primary '\[' slices '\]' !t\_lookahead \
    | del\_t\_atom\
\
del\_t\_atom:\
    | NAME \
    | '(' del\_target ')' \
    | '(' \[del\_targets\] ')' \
    | '\[' \[del\_targets\] '\]' \
\
\# TYPING ELEMENTS\
\# ---------------\
\
\# type\_expressions allow \*/\*\* but ignore them\
type\_expressions:\
    | ','.expression+ ',' '\*' expression ',' '\*\*' expression \
    | ','.expression+ ',' '\*' expression \
    | ','.expression+ ',' '\*\*' expression \
    | '\*' expression ',' '\*\*' expression \
    | '\*' expression \
    | '\*\*' expression \
    | ','.expression+ \
\
func\_type\_comment:\
    | NEWLINE TYPE\_COMMENT &(NEWLINE INDENT)   \# Must be followed by indented block\
    | TYPE\_COMMENT\
\
\# ========================= END OF THE GRAMMAR ===========================\
\
\# ========================= START OF INVALID RULES =======================\
\
#### Previous topic\
\
[9\. Top-level components](https://docs.python.org/3/reference/toplevel_components.html "previous chapter")\
\
#### Next topic\
\
[Python built-ins reference](https://docs.python.org/3/builtins/index.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=10.+Full+Grammar+specification&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fgrammar.html&pagesource=reference%2Fgrammar.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/grammar.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/builtins/index.html "Python built-ins reference")\
     |\
*   [previous](https://docs.python.org/3/reference/toplevel_components.html "9. Top-level components")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python Language Reference](https://docs.python.org/3/reference/index.html)\
     »\
*   [10\. Full Grammar specification](https://docs.python.org/3/reference/grammar.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |