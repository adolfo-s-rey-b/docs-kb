### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/simple_stmts.html "7. Simple statements")
     |
*   [previous](https://docs.python.org/3/reference/import.html "5. The import system")
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
*   [6\. Expressions](https://docs.python.org/3/reference/expressions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

6\. Expressions[¶](https://docs.python.org/3/reference/expressions.html#expressions "Link to this heading")

============================================================================================================

This chapter explains the meaning of the elements of expressions in Python.

**Syntax Notes:** In this and the following chapters, [grammar notation](https://docs.python.org/3/reference/introduction.html#notation)
 will be used to describe syntax, not lexical analysis.

When (one alternative of) a syntax rule has the form:

**name**: othername

and no semantics are given, the semantics of this form of `name` are the same as for `othername`.

6.1. Arithmetic conversions[¶](https://docs.python.org/3/reference/expressions.html#arithmetic-conversions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

When a description of an arithmetic operator below uses the phrase “the numeric arguments are converted to a common real type”, this means that the operator implementation for built-in numeric types works as described in the [Numeric Types](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
 section of the standard library documentation.

Some additional rules apply for certain operators and non-numeric operands (for example, a string as a left argument to the `%` operator). Extensions must define their own conversion behavior.

6.2. Atoms[¶](https://docs.python.org/3/reference/expressions.html#atoms "Link to this heading")

-------------------------------------------------------------------------------------------------

Atoms are the most basic elements of expressions. The simplest atoms are [builtin constants](https://docs.python.org/3/reference/expressions.html#atom-singletons)
, [names](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
 and [literals](https://docs.python.org/3/reference/expressions.html#atom-literals)
. More complex atoms are enclosed in paired delimiters:

*   `()` (parentheses): [groups](https://docs.python.org/3/reference/expressions.html#parenthesized)
    , [tuple displays](https://docs.python.org/3/reference/expressions.html#tuple-display)
    , [yield atoms](https://docs.python.org/3/reference/expressions.html#yieldexpr)
    , and [generator expressions](https://docs.python.org/3/reference/expressions.html#genexpr)
    ;
    
*   `[]` (square brackets): [list displays](https://docs.python.org/3/reference/expressions.html#lists)
    ;
    
*   `{}` (curly braces): [dictionary](https://docs.python.org/3/reference/expressions.html#dict)
     and [set](https://docs.python.org/3/reference/expressions.html#set)
     displays.
    

Formally, the syntax for atoms is:

**atom**:
   | [`builtin_constant`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-builtin_constant)
   | [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
   | [`literal`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-literal)
   | [`parenthesized_enclosure`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-parenthesized_enclosure)
   | [`bracketed_enclosure`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-bracketed_enclosure)
   | [`braced_enclosure`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-braced_enclosure)
**parenthesized\_enclosure**:
   | [`group`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-group)
   | [`tuple`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-tuple)
   | [`yield_atom`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_atom)
   | [`generator_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-generator_expression)
**bracketed\_enclosure**:
   | [`listcomp`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-listcomp)
   | [`list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-list)
**braced\_enclosure**:
   | [`dictcomp`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-dictcomp)
   | [`dict`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-dict)
   | [`setcomp`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-setcomp)
   | [`set`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-set)

### 6.2.1. Built-in constants[¶](https://docs.python.org/3/reference/expressions.html#built-in-constants "Link to this heading")

The keywords `True`, `False`, and `None` name [built-in constants](https://docs.python.org/3/builtins/constants.html#built-in-consts)
. The token `...` names the [`Ellipsis`](https://docs.python.org/3/builtins/constants.html#Ellipsis "Ellipsis")
 constant.

Evaluation of these atoms yields the corresponding value.

Note

Several more built-in constants are available as global variables, but only the ones mentioned here are [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
. In particular, these names cannot be reassigned or used as attributes:

Copy

\>>> False \= 123
  File "<input>", line 1
   False = 123
   ^^^^^
SyntaxError: cannot assign to False

Formally, the syntax for built-in constants is:

**builtin\_constant**: 'True' | 'False' | 'None' | '...'

### 6.2.2. Identifiers (Names)[¶](https://docs.python.org/3/reference/expressions.html#atom-identifiers "Link to this heading")

An identifier occurring as an atom is a name. See section [Names (identifiers and keywords)](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
 for lexical definition and section [Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming)
 for documentation of naming and binding.

When the name is bound to an object, evaluation of the atom yields that object. When a name is not bound, an attempt to evaluate it raises a [`NameError`](https://docs.python.org/3/builtins/exceptions.html#NameError "NameError")
 exception.

#### 6.2.2.1. Private name mangling[¶](https://docs.python.org/3/reference/expressions.html#index-5 "Link to this heading")

When an identifier that textually occurs in a class definition begins with two or more underscore characters and does not end in two or more underscores, it is considered a _private name_ of that class.

See also

The [class specifications](https://docs.python.org/3/reference/compound_stmts.html#class)
.

More precisely, private names are transformed to a longer form before code is generated for them. If the transformed name is longer than 255 characters, implementation-defined truncation may happen.

The transformation is independent of the syntactical context in which the identifier is used but only the following private identifiers are mangled:

*   Any name used as the name of a variable that is assigned or read or any name of an attribute being accessed.
    
    The [`__name__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")
     attribute of nested functions, classes, and type aliases is however not mangled.
    
*   The name of imported modules, e.g., `__spam` in `import __spam`. If the module is part of a package (i.e., its name contains a dot), the name is _not_ mangled, e.g., the `__foo` in `import __foo.bar` is not mangled.
    
*   The name of an imported member, e.g., `__f` in `from spam import __f`.
    

The transformation rule is defined as follows:

*   The class name, with leading underscores removed and a single leading underscore inserted, is inserted in front of the identifier, e.g., the identifier `__spam` occurring in a class named `Foo`, `_Foo` or `__Foo` is transformed to `_Foo__spam`.
    
*   If the class name consists only of underscores, the transformation is the identity, e.g., the identifier `__spam` occurring in a class named `_` or `__` is left as is.
    

### 6.2.3. Literals[¶](https://docs.python.org/3/reference/expressions.html#literals "Link to this heading")

A _literal_ is a textual representation of a value. Python supports numeric, string and bytes literals. [Format strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
 and [template strings](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)
 are treated as string literals.

Numeric literals consist of a single [`NUMBER`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-NUMBER)
 token, which names an integer, floating-point number, or an imaginary number. See the [Numeric literals](https://docs.python.org/3/reference/lexical_analysis.html#numbers)
 section in Lexical analysis documentation for details.

String and bytes literals may consist of several tokens. See section [String literal concatenation](https://docs.python.org/3/reference/expressions.html#string-concatenation)
 for details.

Note that negative and complex numbers, like `-3` or `3+4.2j`, are syntactically not literals, but [unary](https://docs.python.org/3/reference/expressions.html#unary)
 or [binary](https://docs.python.org/3/reference/expressions.html#binary)
 arithmetic operations involving the `-` or `+` operator.

Evaluation of a literal yields an object of the given type ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
, [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, or [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template")
) with the given value. The value may be approximated in the case of floating-point and imaginary literals.

The formal grammar for literals is:

**literal**: [`strings`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-strings)
 | [`NUMBER`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-NUMBER)

#### 6.2.3.1. Literals and object identity[¶](https://docs.python.org/3/reference/expressions.html#literals-and-object-identity "Link to this heading")

All literals correspond to immutable data types, and hence the object’s identity is less important than its value. Multiple evaluations of literals with the same value (either the same occurrence in the program text or a different occurrence) may obtain the same object or a different object with the same value.

CPython implementation detail

For example, in CPython, _small_ integers with the same value evaluate to the same object:

Copy

\>>> x \= 7
\>>> y \= 7
\>>> x is y
True

However, large integers evaluate to different objects:

Copy

\>>> x \= 123456789
\>>> y \= 123456789
\>>> x is y
False

This behavior may change in future versions of CPython. In particular, the boundary between “small” and “large” integers has already changed in the past.

CPython will emit a [`SyntaxWarning`](https://docs.python.org/3/builtins/exceptions.html#SyntaxWarning "SyntaxWarning")
 when you compare literals using `is`:

Copy

\>>> x \= 7
\>>> x is 7
<input>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
True

See [When can I rely on identity tests with the is operator?](https://docs.python.org/3/faq/programming.html#faq-identity-with-is)
 for more information.

[Template strings](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)
 are immutable but may reference mutable objects as [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation")
 values. For the purposes of this section, two t-strings have the “same value” if both their structure and the _identity_ of the values match.

**CPython implementation detail:** Currently, each evaluation of a template string results in a different object.

#### 6.2.3.2. String literal concatenation[¶](https://docs.python.org/3/reference/expressions.html#string-literal-concatenation "Link to this heading")

Multiple adjacent string or bytes literals, possibly using different quoting conventions, are allowed, and their meaning is the same as their concatenation:

Copy

\>>> "hello" 'world'
"helloworld"

This feature is defined at the syntactical level, so it only works with literals. To concatenate string expressions at run time, the ‘+’ operator may be used:

Copy

\>>> greeting \= "Hello"
\>>> space \= " "
\>>> name \= "Blaise"
\>>> print(greeting + space + name)   \# not: print(greeting space name)
Hello Blaise

Literal concatenation can freely mix raw strings, triple-quoted strings, and formatted string literals. For example:

Copy

\>>> "Hello" r', ' f"{name}!"
"Hello, Blaise!"

This feature can be used to reduce the number of backslashes needed, to split long strings conveniently across long lines, or even to add comments to parts of strings. For example:

Copy

re.compile("\[A-Za-z\_\]"       \# letter or underscore
           "\[A-Za-z0-9\_\]\*"   \# letter, digit or underscore
          )

However, bytes literals may only be combined with other byte literals; not with string literals of any kind. Also, template string literals may only be combined with other template string literals:

Copy

\>>> t"Hello" t"{name}!"
Template(strings=('Hello', '!'), interpolations=(...))

Formally:

**strings**: ([`STRING`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-STRING)
 | [`fstring`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-fstring)
)+ | [`tstring`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-tstring)
+

### 6.2.4. Parenthesized groups[¶](https://docs.python.org/3/reference/expressions.html#parenthesized-groups "Link to this heading")

A _parenthesized group_ is an expression enclosed in parentheses. The group evaluates to the same value as the expression inside.

Groups are used to override or clarify [operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
, in the same way as in math notation. For example:

Copy

\>>> 3 << 2 | 4
12
\>>> 3 << (2 | 4)   \# Override precedence of the | (bitwise OR)
192
\>>> (3 << 2) | 4   \# Same as without parentheses (but more clear)
12

Note that not everything in parentheses is a _group_. Specifically, a parenthesized group must include exactly one expression, and cannot end with a comma. See [tuple displays](https://docs.python.org/3/reference/expressions.html#tuple-display)
 and [generator expressions](https://docs.python.org/3/reference/expressions.html#genexpr)
 for other parenthesized forms.

Formally, the syntax for groups is:

**group**: '(' [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 ')'

### 6.2.5. Container displays[¶](https://docs.python.org/3/reference/expressions.html#container-displays "Link to this heading")

For constructing builtin containers (lists, sets, tuples or dictionaries), Python provides special syntax called _displays_. There are subtle differences between the four kinds of displays, detailed in the following sections. All displays, however, consist of comma-separated items enclosed in paired delimiters.

For example, a _list display_ is a series of expressions enclosed in square brackets:

Copy

\>>> \["one", "two", "three"\]
\['one', 'two', 'three'\]
\>>> \[1 + 2, 2 + 3\]
\[3, 5\]

In list, tuple and dictionary (but not set) displays, the series may be empty:

Copy

\>>> \[\]  \# empty list
\[\]
\>>> ()  \# empty tuple
()
\>>> {}  \# empty dictionary
{}

If the series is not empty, the items may be followed by an additional comma, which has no effect:

Copy

\>>> \["one", "two", "three",\]  \# note comma after "three"
\['one', 'two', 'three'\]

Note

The trailing comma is often used for displays that span multiple lines (using [implicit line joining](https://docs.python.org/3/reference/lexical_analysis.html#implicit-joining)
), so when a future programmer adds a new entry at the end, they do not need to modify an existing line:

Copy

\>>> \[\
...     'one',\
...     'two',\
...     'three',\
... \]
\['one', 'two', 'three'\]

At runtime, when a display is evaluated, the listed items are evaluated from left to right and placed into a new container of the appropriate type.

For tuple, list and set (but not dict) displays, any item in the display may be prefixed with an asterisk (`*`). This denotes [iterable unpacking](https://docs.python.org/3/reference/expressions.html#iterable-unpacking)
. At runtime, the asterisk-prefixed expression must evaluate to an iterable, whose contents are inserted into the container at the location of the unpacking. For example:

Copy

\>>> numbers \= (1, 2)
\>>> \[\*numbers, 'word', \*numbers\]
\[1, 2, 'word', 1, 2\]

Dictionary displays use a similar mechanism called _dictionary unpacking_, denoted with a double asterisk (`**`). See [Dictionary displays](https://docs.python.org/3/reference/expressions.html#dict)
 for details.

A more advanced form of displays are _comprehensions_, where items are computed via a set of looping and filtering instructions. See the [Comprehensions](https://docs.python.org/3/reference/expressions.html#comprehensions)
 section for details.

Added in version 3.5: Iterable and dictionary unpacking in displays, originally proposed by [**PEP 448**](https://peps.python.org/pep-0448/)
.

#### 6.2.5.1. List displays[¶](https://docs.python.org/3/reference/expressions.html#list-displays "Link to this heading")

A _list display_ is a possibly empty series of expressions enclosed in square brackets. For example:

Copy

\>>> \["one", "two", "three"\]
\['one', 'two', 'three'\]
\>>> \["one"\]  \# One-element list
\['one'\]
\>>> \[\]       \# empty list
\[\]

See [Container displays](https://docs.python.org/3/reference/expressions.html#displays)
 for general information on displays.

The formal grammar for list displays is:

**list**: '\[' \[[`flexible_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression_list)\
\] '\]'

#### 6.2.5.2. Set displays[¶](https://docs.python.org/3/reference/expressions.html#set-displays "Link to this heading")

A _set display_ is a _non-empty_ series of expressions enclosed in curly braces. For example:

Copy

\>>> {"one", "two", "three"}
{'one', 'three', 'two'}
\>>> {"one"}  \# One-element set
{'one'}

See [Container displays](https://docs.python.org/3/reference/expressions.html#displays)
 for general information on displays.

There is no special syntax for the empty set. The `{}` literal is a [dictionary display](https://docs.python.org/3/reference/expressions.html#dict)
 that constructs an empty dictionary. Call [`set()`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 with no arguments to get an empty set.

The formal grammar for set displays is:

**set**: '{' [`flexible_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression_list)
 '}'

#### 6.2.5.3. Tuple displays[¶](https://docs.python.org/3/reference/expressions.html#tuple-displays "Link to this heading")

A _tuple display_ is a series of expressions enclosed in parentheses. For example:

Copy

\>>> (1, 2)
(1, 2)
\>>> ()  \# an empty tuple
()

See [Container displays](https://docs.python.org/3/reference/expressions.html#displays)
 for general information on displays.

To avoid ambiguity, if a tuple display has exactly one element, it requires a trailing comma. Without it, you get a [parenthesized group](https://docs.python.org/3/reference/expressions.html#parenthesized)
:

Copy

\>>> ('single',)  \# single-element tuple
('single',)
\>>> ('single')   \# no comma: single string
'single'

To put it in other words, a tuple display is a parenthesized list of either:

*   two or more comma-separated expressions, or
    
*   zero or more expressions, each followed by a comma.
    

Since tuples are immutable, [object identity rules for literals](https://docs.python.org/3/reference/expressions.html#literals-identity)
 also apply to tuples: at runtime, two occurrences of tuples with the same values may or may not yield the same object.

Note

Python’s syntax also includes [expression lists](https://docs.python.org/3/reference/expressions.html#exprlists)
, where a comma-separated list of expressions is _not_ enclosed in parentheses but evaluates to tuple.

In other words, when it comes to tuple syntax, the comma is more important that the use of parentheses. Only the empty tuple is spelled without a comma.

The formal grammar for tuple displays is:

**tuple**:
   | '(' [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
 (',' [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
)+ \[','\] ')'
   | '(' [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
 ',' ')'
   | '(' ')'

#### 6.2.5.4. Dictionary displays[¶](https://docs.python.org/3/reference/expressions.html#dictionary-displays "Link to this heading")

A _dictionary display_ is a possibly empty series of _dict items_ enclosed in curly braces. Each dict item is a colon-separated pair of expressions: the _key_ and its associated _value_. For example:

Copy

\>>> {1: 'one', 2: 'two'}
{1: 'one', 2: 'two'}

At runtime, when a dictionary comprehension is evaluated, the expressions are evaluated from left to right. Each key object is used as a key into the dictionary to store the corresponding value. This means that you can specify the same key multiple times in the comprehension, and the final dictionary’s value for a given key will be the last one given. For example:

Copy

\>>> {
...     1: 'this will be overridden',
...     2: 'two',
...     1: 'also overridden',
...     1: 'one',
... }
{1: 'one', 2: 'two'}

Instead of a key-value pair, a dict item may be an expression prefixed by a double asterisk `**`. This denotes _dictionary unpacking_. At runtime, the expression must evaluate to a [mapping](https://docs.python.org/3/glossary.html#term-mapping)
; each item of the mapping is added to the new dictionary. As with key-value pairs, later values replace values already set by earlier items and unpackings. This may be used to override a set of defaults:

Copy

\>>> defaults \= {'color': 'blue', 'count': 8}
\>>> overrides \= {'color': 'yellow'}
\>>> {\*\*defaults, \*\*overrides}
{'color': 'yellow', 'count': 8}

Added in version 3.5: Unpacking into dictionary displays, originally proposed by [**PEP 448**](https://peps.python.org/pep-0448/)
.

The formal grammar for dict displays is:

**dict**:                   '{' \[[`double_starred_kvpairs`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-double_starred_kvpairs)\
\] '}'
**double\_starred\_kvpairs**: ','.[`double_starred_kvpair`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-double_starred_kvpair)
\+ \[','\]
**double\_starred\_kvpair**:  '\*\*' [`or_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_expr)
 | [`kvpair`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-kvpair)
**kvpair**:                 [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 ':' [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)

### 6.2.6. Comprehensions[¶](https://docs.python.org/3/reference/expressions.html#comprehensions "Link to this heading")

List, set and dictionary _comprehensions_ are a form of [container displays](https://docs.python.org/3/reference/expressions.html#displays)
 where items are computed via a set of looping and filtering instructions rather than listed explicitly.

In its simplest form, a comprehension consists of a single expression followed by a `for` clause. The `for` clause has the same syntax as the header of a [for statement](https://docs.python.org/3/reference/compound_stmts.html#for)
, without a trailing colon.

For example, a list of the first ten squares is:

Copy

\>>> \[x\*\*2 for x in range(10)\]
\[0, 1, 4, 9, 16, 25, 36, 49, 64, 81\]

At run time, a list comprehension creates a new list. The expression after `in` must evaluate to an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
. For each element of this iterable, the element is bound to the `for` clause’s target as in a `for` statement, then the expression before `for` is evaluated with the target in scope and the result is added to the new list. Thus, the example above is roughly equivalent to defining and calling the following function:

Copy

def make\_list\_of\_squares(iterable):
    result \= \[\]
    for x in iterable:
        result.append(x\*\*2)
    return result

make\_list\_of\_squares(range(10))

Set comprehensions work similarly. For example, here is a set of lowercase letters:

Copy

\>>> {x.lower() for x in \['a', 'A', 'b', 'C'\]}
{'c', 'a', 'b'}

At run time, this corresponds roughly to calling this function:

Copy

def make\_lowercase\_set(iterable):
    result \= set()
    for x in iterable:
        result.add(x.lower())
    return result

make\_lowercase\_set(\['a', 'A', 'b', 'C'\])

Dictionary comprehensions start with a colon-separated key-value pair instead of an expression. For example:

Copy

\>>> {func.\_\_name\_\_: func for func in \[print, hex, any\]}
{'print': <built-in function print>,
 'hex': <built-in function hex>,
 'any': <built-in function any>}

At run time, this corresponds roughly to:

Copy

def make\_dict\_mapping\_names\_to\_functions(iterable):
    result \= {}
    for func in iterable:
        result\[func.\_\_name\_\_\] \= func
    return result

make\_dict\_mapping\_names\_to\_functions(\[print, hex, any\])

As in other kinds of dictionary displays, the same key may be specified multiple times. Earlier values are overwritten by ones that are evaluated later.

There are no _tuple comprehensions_. A similar syntax is instead used for [generator expressions](https://docs.python.org/3/reference/expressions.html#genexpr)
, from which you can construct a tuple like this:

Copy

\>>> tuple(x\*\*2 for x in range(10))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Changed in version 3.8: Prior to Python 3.8, in dict comprehensions, the evaluation order of key and value was not well-defined. In CPython, the value was evaluated before the key. Starting with 3.8, the key is evaluated before the value, as proposed by [**PEP 572**](https://peps.python.org/pep-0572/)
.

#### 6.2.6.1. Filtering in comprehensions[¶](https://docs.python.org/3/reference/expressions.html#filtering-in-comprehensions "Link to this heading")

The `for` clause may be followed by an `if` clause with an expression.

For example, a list of names from the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 module that start with `f` is:

Copy

\>>> \[name for name in vars(math) if name.startswith('f')\]
\['fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum'\]

At run time, the expression after `if` is evaluated before each element is added to the resulting container, and if it is false, the element is skipped. Thus, the above example roughly corresponds to defining and calling the following function:

Copy

def get\_math\_f\_names(iterable):
    result \= \[\]
    for name in iterable:
        if name.startswith('f'):
           result.append(name)
    return result

get\_math\_f\_names(vars(math))

Filtering is a special case of more complex comprehensions. See the next section for a more formal description.

#### 6.2.6.2. Complex comprehensions[¶](https://docs.python.org/3/reference/expressions.html#complex-comprehensions "Link to this heading")

Generally, a comprehension’s initial `for` clause may be followed by zero or more additional `for` or `if` clauses. For example, here is a list of names exposed by two Python modules, filtered to only include names that start with `a`:

Copy

\>>> import array
\>>> import math
\>>> \[\
...     name\
...     for module in \[array, math\]\
...     for name in vars(module)\
...     if name.startswith('a')\
... \]
\['array', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh'\]

At run time, this roughly corresponds to defining and calling:

Copy

def get\_a\_names(iterable):
    result \= \[\]
    for module in iterable:
        for name in vars(module):
            if name.startswith('a'):
                result.append(name)
    return result

get\_a\_names(\[array, math\])

The elements of the new container are those that would be produced by considering each of the `for` or `if` clauses a block, nesting from left to right, and evaluating the expression to produce an element (or dictionary entry) each time the innermost block is reached.

Aside from the iterable expression in the leftmost `for` clause, the comprehension is executed in a separate implicitly nested scope. This ensures that names assigned to in the target list don’t “leak” into the enclosing scope. For example:

Copy

\>>> x \= 'old value'
\>>> \[x\*\*2 for x in range(10)\]  \# this \`x\` is local to the comprehension
\>>> x
'old value'

The iterable expression in the leftmost `for` clause is evaluated directly in the enclosing scope and then passed as an argument to the implicitly nested scope.

Subsequent `for` clauses and any filter condition in the leftmost `for` clause cannot be evaluated in the enclosing scope as they may depend on the values obtained from the leftmost iterable.

To ensure the comprehension always results in a container of the appropriate type, `yield` and `yield from` expressions are prohibited in the implicitly nested scope.

[Assignment expressions](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
 are not allowed inside comprehension iterable expressions (that is, the expressions after the `in` keyword), nor anywhere within comprehensions that appear directly in a class definition.

Changed in version 3.8: `yield` and `yield from` prohibited in the implicitly nested scope.

#### 6.2.6.3. Unpacking in comprehensions[¶](https://docs.python.org/3/reference/expressions.html#unpacking-in-comprehensions "Link to this heading")

If the expression of a list or set comprehension is starred, the result will be [unpacked](https://docs.python.org/3/reference/expressions.html#iterable-unpacking)
 to produce zero or more elements.

This is often used for “flattening” lists, for example:

Copy

\>>> students \= \['Petr', 'Blaise', 'Jarka'\]
\>>> teachers \= \['Salim', 'Bartosz'\]
\>>> lists\_of\_people \= \[students, teachers\]
\>>> \[\*people for people in lists\_of\_people\]
\['Petr', 'Blaise', 'Jarka', 'Salim', 'Bartosz'\]

At run time, this comprehension roughly corresponds to:

Copy

def flatten\_names(lists\_of\_people):
    result \= \[\]
    for people in lists\_of\_people:
        result.extend(people)
    return result

In dict comprehensions, a double-starred expression will be evaluated and then unpacked using [dictionary unpacking](https://docs.python.org/3/reference/expressions.html#dict-unpacking)
, inserting zero or more key/value pairs into the new dictionary. As in other kinds of dictionary displays, if the same key is specified multiple times, the associated value in the resulting dictionary will be the last one specified.

For example:

Copy

\>>> system\_defaults \= {'color': 'blue', 'count': 8}
\>>> user\_defaults \= {'color': 'yellow'}
\>>> overrides \= {'count': 5}

\>>> configuration\_sets \= \[system\_defaults, user\_defaults, overrides\]

\>>> {\*\*d for d in configuration\_sets}
{'color': 'yellow', 'count': 5}

Added in version 3.15: Unpacking in comprehensions using the `*` and `**` operators was introduced in [**PEP 798**](https://peps.python.org/pep-0798/)
.

#### 6.2.6.4. Asynchronous comprehensions[¶](https://docs.python.org/3/reference/expressions.html#asynchronous-comprehensions "Link to this heading")

In an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 function, an `async for` clause may be used to iterate over a [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
. A comprehension in an `async def` function may consist of either a `for` or `async for` clause following the leading expression, may contain additional `for` or `async for` clauses, and may also use [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expressions.

If a comprehension contains `async for` clauses, or if it contains `await` expressions or other asynchronous comprehensions anywhere except the iterable expression in the leftmost `for` clause, it is called an _asynchronous comprehension_. An asynchronous comprehension may suspend the execution of the coroutine function in which it appears.

Added in version 3.6: Asynchronous comprehensions were introduced in [**PEP 530**](https://peps.python.org/pep-0530/)
.

Changed in version 3.11: Asynchronous comprehensions are now allowed inside comprehensions in asynchronous functions. Outer comprehensions implicitly become asynchronous.

#### 6.2.6.5. Formal grammar for comprehensions[¶](https://docs.python.org/3/reference/expressions.html#formal-grammar-for-comprehensions "Link to this heading")

The formal grammar for comprehensions is:

**listcomp**:      '\[' [`comprehension`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comprehension)\
 '\]'
**setcomp**:       '{' [`comprehension`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comprehension)
 '}'
**comprehension**: [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
 [`for_if_clause`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-for_if_clause)
+

**dictcomp**:
    | '{' [`kvpair`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-kvpair)
 [`for_if_clause`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-for_if_clause)
\+ '}'
    | '{' '\*\*' [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 [`for_if_clause`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-for_if_clause)
\+ '}'

**for\_if\_clause**:
    | \['async'\] 'for' [`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)
 'in' [`or_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_test)
 ('if' [`or_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_test)
)\*

### 6.2.7. Generator expressions[¶](https://docs.python.org/3/reference/expressions.html#generator-expressions "Link to this heading")

The syntax for _generator expressions_ is the same as for list [comprehensions](https://docs.python.org/3/reference/expressions.html#comprehensions)
, except that they are enclosed in parentheses instead of brackets. For example:

Copy

\>>> iterator \= (x \*\* 2 for x in range(10))
\>>> iterator
<generator object <genexpr> at ...>

At runtime, a generator expression evaluates to a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)
 which yields the same values as the corresponding list comprehension:

Copy

\>>> list(iterator)
\[0, 1, 4, 9, 16, 25, 36, 49, 64, 81\]

Thus, the example above is roughly equivalent to defining and calling the following generator function:

Copy

def make\_generator\_of\_squares(iterator):
    for x in iterator:
        yield x \*\* 2

make\_generator\_of\_squares(iter(range(10)))

The enclosing parentheses can be omitted in calls when the generator expression is the only positional argument and there are no keyword arguments. See the [Calls section](https://docs.python.org/3/reference/expressions.html#calls)
 for details. For example:

Copy

\# The parentheses after \`sum\` are part of the call syntax:
\>>> sum(x \*\* 2 for x in range(10))
285

\# The generator needs its own parentheses if it's not the only argument:
\>>> sum((x \*\* 2 for x in range(10)), start\=1000)
1285

The iterable expression in the leftmost `for` clause is evaluated immediately, so that an error raised by this expression will be emitted at the point where the generator expression is defined, rather than at the point where the first value is retrieved:

Copy

\>>> (x \*\* 2 for x in nonexistent\_iterable)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent\_iterable' is not defined

After the expression is evaluated, an iterator is created from the result, as if [`iter()`](https://docs.python.org/3/builtins/functions.html#iter "iter")
 was called on it. Any error raised when creating the iterator is also emitted immediately:

Copy

\>>> (x \*\* 2 for x in None)
Traceback (most recent call last):
  ...
TypeError: 'NoneType' object is not iterable

All other expressions are evaluated lazily, in the same fashion as normal generators (that is, when the iterator is asked to yield a value):

Copy

\>>> iterator \= (nonexistent\_value for x in range(10))
\>>> iterator
<generator object <genexpr> at ...>
\>>> list(iterator)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent\_value' is not defined

Copy

\>>> iterator \= (x \* y for x in range(10) for y in nonexistent\_iterable)
\>>> iterator
<generator object <genexpr> at ...>
\>>> list(iterator)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent\_iterable' is not defined

To avoid interfering with the expected operation of the generator expression itself, `yield` and `yield from` expressions are prohibited inside the implicitly nested scope.

If a generator expression contains either `async for` clauses or [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expressions it is called an _asynchronous generator expression_. An asynchronous generator expression returns a new asynchronous generator object, which is an asynchronous iterator (see [Asynchronous Iterators](https://docs.python.org/3/reference/datamodel.html#async-iterators)
).

The formal grammar for generator expressions is:

**generator\_expression**: "(" [`comprehension`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comprehension)
 ")"

Added in version 3.6: Asynchronous generator expressions were introduced.

Changed in version 3.7: Prior to Python 3.7, asynchronous generator expressions could only appear in [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 coroutines. Starting with 3.7, any function can use asynchronous generator expressions.

Changed in version 3.8: `yield` and `yield from` prohibited in the implicitly nested scope.

### 6.2.8. Yield expressions[¶](https://docs.python.org/3/reference/expressions.html#yield-expressions "Link to this heading")

**yield\_atom**:       "(" [`yield_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_expression)
 ")"
**yield\_from**:       "yield" "from" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
**yield\_expression**: "yield" [`yield_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_list)
 | [`yield_from`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_from)

The yield expression is used when defining a [generator](https://docs.python.org/3/glossary.html#term-generator)
 function or an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function and thus can only be used in the body of a function definition. Using a yield expression in a function’s body causes that function to be a generator function, and using it in an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 function’s body causes that coroutine function to be an asynchronous generator function. For example:

Copy

def gen():  \# defines a generator function
    yield 123

async def agen(): \# defines an asynchronous generator function
    yield 123

Due to their side effects on the containing scope, `yield` expressions are not permitted as part of the implicitly defined scopes used to implement comprehensions and generator expressions.

Changed in version 3.8: Yield expressions prohibited in the implicitly nested scopes used to implement comprehensions and generator expressions.

Generator functions are described below, while asynchronous generator functions are described separately in section [Asynchronous generator functions](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions)
.

When a generator function is called, it returns an iterator known as a generator. That generator then controls the execution of the generator function. The execution starts when one of the generator’s methods is called. At that time, the execution proceeds to the first yield expression, where it is suspended again, returning the value of [`yield_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_list)
 to the generator’s caller, or `None` if `yield_list` is omitted. By suspended, we mean that all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation stack, and the state of any exception handling. When the execution is resumed by calling one of the generator’s methods, the function can proceed exactly as if the yield expression were just another external call. The value of the yield expression after resuming depends on the method which resumed the execution. If [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#generator.__next__ "generator.__next__")
 is used (typically via either a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 or the [`next()`](https://docs.python.org/3/builtins/functions.html#next "next")
 builtin) then the result is [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
. Otherwise, if [`send()`](https://docs.python.org/3/builtins/stdtypes.html#generator.send "generator.send")
 is used, then the result will be the value passed in to that method.

All of this makes generator functions quite similar to coroutines; they yield multiple times, they have more than one entry point and their execution can be suspended. The only difference is that a generator function cannot control where the execution should continue after it yields; the control is always transferred to the generator’s caller.

Yield expressions are allowed anywhere in a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 construct. If the generator is not resumed before it is finalized (by reaching a zero reference count or by being garbage collected), the generator-iterator’s [`close()`](https://docs.python.org/3/builtins/stdtypes.html#generator.close "generator.close")
 method will be called, allowing any pending [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clauses to execute.

When `yield from <expr>` is used, the supplied expression must be an iterable. The values produced by iterating that iterable are passed directly to the caller of the current generator’s methods. Any values passed in with [`send()`](https://docs.python.org/3/builtins/stdtypes.html#generator.send "generator.send")
 and any exceptions passed in with [`throw()`](https://docs.python.org/3/builtins/stdtypes.html#generator.throw "generator.throw")
 are passed to the underlying iterator if it has the appropriate methods. If this is not the case, then `send()` will raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 or [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
, while `throw()` will just raise the passed in exception immediately.

When the underlying iterator is complete, the [`value`](https://docs.python.org/3/builtins/exceptions.html#StopIteration.value "StopIteration.value")
 attribute of the raised [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 instance becomes the value of the yield expression. It can be either set explicitly when raising `StopIteration`, or automatically when the subiterator is a generator (by returning a value from the subgenerator).

Changed in version 3.3: Added `yield from <expr>` to delegate control flow to a subiterator.

The parentheses may be omitted when the yield expression is the sole expression on the right hand side of an assignment statement.

See also

[**PEP 255**](https://peps.python.org/pep-0255/)
 - Simple Generators

The proposal for adding generators and the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 statement to Python.

[**PEP 342**](https://peps.python.org/pep-0342/)
 - Coroutines via Enhanced Generators

The proposal to enhance the API and syntax of generators, making them usable as simple coroutines.

[**PEP 380**](https://peps.python.org/pep-0380/)
 - Syntax for Delegating to a Subgenerator

The proposal to introduce the [`yield_from`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_from)
 syntax, making delegation to subgenerators easy.

[**PEP 525**](https://peps.python.org/pep-0525/)
 - Asynchronous Generators

The proposal that expanded on [**PEP 492**](https://peps.python.org/pep-0492/)
 by adding generator capabilities to coroutine functions.

#### 6.2.8.1. Examples[¶](https://docs.python.org/3/reference/expressions.html#examples "Link to this heading")

Here is a simple example that demonstrates the behavior of generators and generator functions:

Copy

\>>> def echo(value\=None):
...     print("Execution starts when 'next()' is called for the first time.")
...     try:
...         while True:
...             try:
...                 value \= (yield value)
...             except Exception as e:
...                 value \= e
...     finally:
...         print("Don't forget to clean up when 'close()' is called.")
...
\>>> generator \= echo(1)
\>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
\>>> print(next(generator))
None
\>>> print(generator.send(2))
2
\>>> generator.throw(TypeError, "spam")
TypeError('spam',)
\>>> generator.close()
Don't forget to clean up when 'close()' is called.

For examples using `yield from`, see [PEP 380: Syntax for Delegating to a Subgenerator](https://docs.python.org/3/whatsnew/3.3.html#pep-380)
 in “What’s New in Python.”

#### 6.2.8.2. Asynchronous generator functions[¶](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions "Link to this heading")

The presence of a yield expression in a function or method defined using [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 further defines the function as an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function.

When an asynchronous generator function is called, it returns an asynchronous iterator known as an asynchronous generator object. That object then controls the execution of the generator function. An asynchronous generator object is typically used in an [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 statement in a coroutine function analogously to how a generator object would be used in a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 statement.

Calling one of the asynchronous generator’s methods returns an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 object, and the execution starts when this object is awaited on. At that time, the execution proceeds to the first yield expression, where it is suspended again, returning the value of [`yield_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_list)
 to the awaiting coroutine. As with a generator, suspension means that all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation stack, and the state of any exception handling. When the execution is resumed by awaiting on the next object returned by the asynchronous generator’s methods, the function can proceed exactly as if the yield expression were just another external call. The value of the yield expression after resuming depends on the method which resumed the execution. If [`__anext__()`](https://docs.python.org/3/builtins/stdtypes.html#agen.__anext__ "agen.__anext__")
 is used then the result is [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
. Otherwise, if [`asend()`](https://docs.python.org/3/builtins/stdtypes.html#agen.asend "agen.asend")
 is used, then the result will be the value passed in to that method.

If an asynchronous generator happens to exit early by [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
, the caller task being cancelled, or other exceptions, the generator’s async cleanup code will run and possibly raise exceptions or access context variables in an unexpected context–perhaps after the lifetime of tasks it depends, or during the event loop shutdown. To prevent this, the caller must explicitly close the async generator by calling [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
 method to finalize the generator and ultimately detach it from the event loop.

In an asynchronous generator function, yield expressions are allowed anywhere in a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 construct. However, if an asynchronous generator is not resumed before it is finalized (by reaching a zero reference count or by being garbage collected), then a yield expression within a `try` construct could result in a failure to execute pending [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clauses. In this case, it is the responsibility of the event loop or scheduler running the asynchronous generator to call the asynchronous generator-iterator’s [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
 method and run the resulting awaitable, thus allowing any pending `finally` clauses to execute.

To handle finalization when an asynchronous generator is about to be garbage collected, an event loop should define a _finalizer_ function which takes an asynchronous generator-iterator and schedules the awaitable returned by [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
. This _finalizer_ may be registered by calling [`sys.set_asyncgen_hooks()`](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks "sys.set_asyncgen_hooks")
. When first iterated over, an asynchronous generator-iterator will store the registered _finalizer_ to be called upon finalization. For a reference example of a _finalizer_ method see the implementation of `asyncio.BaseEventLoop._asyncgen_finalizer_hook` in [Lib/asyncio/base\_events.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/base_events.py)
.

The expression `yield from <expr>` is a syntax error when used in an asynchronous generator function.

6.3. Primaries[¶](https://docs.python.org/3/reference/expressions.html#primaries "Link to this heading")

---------------------------------------------------------------------------------------------------------

Primaries represent the most tightly bound operations of the language. Their syntax is:

**primary**: [`atom`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-atom)
 | [`attributeref`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-attributeref)
 | [`subscription`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-subscription)
 | [`call`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-call)

### 6.3.1. Attribute references[¶](https://docs.python.org/3/reference/expressions.html#attribute-references "Link to this heading")

An attribute reference is a primary followed by a period and a name:

**attributeref**: [`primary`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-primary)
 "." [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)

The primary must evaluate to an object of a type that supports attribute references, which most objects do. This object is then asked to produce the attribute whose name is the identifier. The type and value produced is determined by the object. Multiple evaluations of the same attribute reference may yield different objects.

This production can be customized by overriding the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 method or the [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 method. The `__getattribute__()` method is called first and either returns a value or raises [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 if the attribute is not available.

If an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 is raised and the object has a `__getattr__()` method, that method is called as a fallback.

### 6.3.2. Subscriptions and slicings[¶](https://docs.python.org/3/reference/expressions.html#subscriptions-and-slicings "Link to this heading")

The _subscription_ syntax is usually used for selecting an element from a [container](https://docs.python.org/3/reference/datamodel.html#sequence-types)
 – for example, to get a value from a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
:

Copy

\>>> digits\_by\_name \= {'one': 1, 'two': 2}
\>>> digits\_by\_name\['two'\]  \# Subscripting a dictionary using the key 'two'
2

In the subscription syntax, the object being subscribed – a [primary](https://docs.python.org/3/reference/expressions.html#primaries)
 – is followed by a _subscript_ in square brackets. In the simplest case, the subscript is a single expression.

Depending on the type of the object being subscribed, the subscript is sometimes called a [key](https://docs.python.org/3/glossary.html#term-key)
 (for mappings), [index](https://docs.python.org/3/glossary.html#term-index)
 (for sequences), or _type argument_ (for [generic types](https://docs.python.org/3/glossary.html#term-generic-type)
). Syntactically, these are all equivalent:

Copy

\>>> colors \= \['red', 'blue', 'green', 'black'\]
\>>> colors\[3\]  \# Subscripting a list using the index 3
'black'

\>>> list\[str\]  \# Parameterizing the list type using the type argument str
list\[str\]

At runtime, the interpreter will evaluate the primary and the subscript, and call the primary’s [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 or [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 [special method](https://docs.python.org/3/glossary.html#term-special-method)
 with the subscript as argument. For more details on which of these methods is called, see [\_\_class\_getitem\_\_ versus \_\_getitem\_\_](https://docs.python.org/3/reference/datamodel.html#classgetitem-versus-getitem)
.

To show how subscription works, we can define a custom object that implements [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 and prints out the value of the subscript:

Copy

\>>> class SubscriptionDemo:
...     def \_\_getitem\_\_(self, key):
...         print(f'subscripted with: {key!r}')
...
\>>> demo \= SubscriptionDemo()
\>>> demo\[1\]
subscripted with: 1
\>>> demo\['a' \* 3\]
subscripted with: 'aaa'

See [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 documentation for how built-in types handle subscription.

Subscriptions may also be used as targets in [assignment](https://docs.python.org/3/reference/simple_stmts.html#assignment)
 or [deletion](https://docs.python.org/3/reference/simple_stmts.html#del)
 statements. In these cases, the interpreter will call the subscripted object’s [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
 or [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__")
 [special method](https://docs.python.org/3/glossary.html#term-special-method)
, respectively, instead of [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
.

Copy

\>>> colors \= \['red', 'blue', 'green', 'black'\]
\>>> colors\[3\] \= 'white'  \# Setting item at index
\>>> colors
\['red', 'blue', 'green', 'white'\]
\>>> del colors\[3\]  \# Deleting item at index 3
\>>> colors
\['red', 'blue', 'green'\]

All advanced forms of _subscript_ documented in the following sections are also usable for assignment and deletion.

#### 6.3.2.1. Slicings[¶](https://docs.python.org/3/reference/expressions.html#slicings "Link to this heading")

A more advanced form of subscription, _slicing_, is commonly used to extract a portion of a [sequence](https://docs.python.org/3/reference/datamodel.html#datamodel-sequences)
. In this form, the subscript is a [slice](https://docs.python.org/3/glossary.html#term-slice)
: up to three expressions separated by colons. Any of the expressions may be omitted, but a slice must contain at least one colon:

Copy

\>>> number\_names \= \['zero', 'one', 'two', 'three', 'four', 'five'\]
\>>> number\_names\[1:3\]
\['one', 'two'\]
\>>> number\_names\[1:\]
\['one', 'two', 'three', 'four', 'five'\]
\>>> number\_names\[:3\]
\['zero', 'one', 'two'\]
\>>> number\_names\[:\]
\['zero', 'one', 'two', 'three', 'four', 'five'\]
\>>> number\_names\[::2\]
\['zero', 'two', 'four'\]
\>>> number\_names\[:\-3\]
\['zero', 'one', 'two'\]
\>>> del number\_names\[4:\]
\>>> number\_names
\['zero', 'one', 'two', 'three'\]

When a slice is evaluated, the interpreter constructs a [`slice`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 object whose [`start`](https://docs.python.org/3/builtins/functions.html#slice.start "slice.start")
, [`stop`](https://docs.python.org/3/builtins/functions.html#slice.stop "slice.stop")
 and [`step`](https://docs.python.org/3/builtins/functions.html#slice.step "slice.step")
 attributes, respectively, are the results of the expressions between the colons. Any missing expression evaluates to [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
. This `slice` object is then passed to the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 or [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 [special method](https://docs.python.org/3/glossary.html#term-special-method)
, as above.

Copy

\# continuing with the SubscriptionDemo instance defined above:
\>>> demo\[2:3\]
subscripted with: slice(2, 3, None)
\>>> demo\[::'spam'\]
subscripted with: slice(None, None, 'spam')

#### 6.3.2.2. Comma-separated subscripts[¶](https://docs.python.org/3/reference/expressions.html#comma-separated-subscripts "Link to this heading")

The subscript can also be given as two or more comma-separated expressions or slices:

Copy

\# continuing with the SubscriptionDemo instance defined above:
\>>> demo\[1, 2, 3\]
subscripted with: (1, 2, 3)
\>>> demo\[1:2, 3\]
subscripted with: (slice(1, 2, None), 3)

This form is commonly used with numerical libraries for slicing multi-dimensional data. In this case, the interpreter constructs a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 of the results of the expressions or slices, and passes this tuple to the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 or [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 [special method](https://docs.python.org/3/glossary.html#term-special-method)
, as above.

The subscript may also be given as a single expression or slice followed by a comma, to specify a one-element tuple:

Copy

\>>> demo\['spam',\]
subscripted with: ('spam',)

#### 6.3.2.3. “Starred” subscriptions[¶](https://docs.python.org/3/reference/expressions.html#starred-subscriptions "Link to this heading")

Added in version 3.11: Expressions in _tuple\_slices_ may be starred. See [**PEP 646**](https://peps.python.org/pep-0646/)
.

The subscript can also contain a starred expression. In this case, the interpreter unpacks the result into a tuple, and passes this tuple to [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 or [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
:

Copy

\# continuing with the SubscriptionDemo instance defined above:
\>>> demo\[\*range(10)\]
subscripted with: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

Starred expressions may be combined with comma-separated expressions and slices:

Copy

\>>> demo\['a', 'b', \*range(3), 'c'\]
subscripted with: ('a', 'b', 0, 1, 2, 'c')

#### 6.3.2.4. Formal subscription grammar[¶](https://docs.python.org/3/reference/expressions.html#formal-subscription-grammar "Link to this heading")

**subscription**:     [`primary`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-primary)
 '\[' [`subscript`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-subscript)\
 '\]'
**subscript**:        [`single_subscript`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-single_subscript)
 | [`tuple_subscript`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-tuple_subscript)
**single\_subscript**: [`proper_slice`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-proper_slice)
 | [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
**proper\_slice**:     \[[`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\] ":" \[[`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\] \[ ":" \[[`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\] \]
**tuple\_subscript**:  ','.([`single_subscript`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-single_subscript)
 | [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
)+ \[','\]

Recall that the `|` operator [denotes ordered choice](https://docs.python.org/3/reference/introduction.html#notation)
. Specifically, in `subscript`, if both alternatives would match, the first (`single_subscript`) has priority.

### 6.3.3. Calls[¶](https://docs.python.org/3/reference/expressions.html#calls "Link to this heading")

A call calls a callable object (e.g., a [function](https://docs.python.org/3/glossary.html#term-function)
) with a possibly empty series of [arguments](https://docs.python.org/3/glossary.html#term-argument)
:

**call**:                 [`primary`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-primary)
 "(" \[[`argument_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-argument_list)\
 \[","\] | [`comprehension`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comprehension)\
\] ")"
**argument\_list**:        [`positional_arguments`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-positional_arguments)
 \["," [`starred_and_keywords`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_and_keywords)\
\]
                        \["," [`keywords_arguments`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keywords_arguments)\
\]
                      | [`starred_and_keywords`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_and_keywords)
 \["," [`keywords_arguments`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keywords_arguments)\
\]
                      | [`keywords_arguments`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keywords_arguments)
**positional\_arguments**: [`positional_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-positional_item)
 ("," [`positional_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-positional_item)
)\*
**positional\_item**:      [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 | "\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
**starred\_and\_keywords**: ("\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 | [`keyword_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keyword_item)
)
                      ("," "\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 | "," [`keyword_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keyword_item)
)\*
**keywords\_arguments**:   ([`keyword_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keyword_item)
 | "\*\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)
                      ("," [`keyword_item`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-keyword_item)
 | "," "\*\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)\*
**keyword\_item**:         [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 "=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)

An optional trailing comma may be present after the positional and keyword arguments but does not affect the semantics.

The primary must evaluate to a callable object (user-defined functions, built-in functions, methods of built-in objects, class objects, methods of class instances, and all objects having a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method are callable). All argument expressions are evaluated before the call is attempted. Please refer to section [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function)
 for the syntax of formal [parameter](https://docs.python.org/3/glossary.html#term-parameter)
 lists.

If keyword arguments are present, they are first converted to positional arguments, as follows. First, a list of unfilled slots is created for the formal parameters. If there are N positional arguments, they are placed in the first N slots. Next, for each keyword argument, the identifier is used to determine the corresponding slot (if the identifier is the same as the first formal parameter name, the first slot is used, and so on). If the slot is already filled, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised. Otherwise, the argument is placed in the slot, filling it (even if the expression is `None`, it fills the slot). When all arguments have been processed, the slots that are still unfilled are filled with the corresponding default value from the function definition. (Default values are calculated, once, when the function is defined; thus, a mutable object such as a list or dictionary used as default value will be shared by all calls that don’t specify an argument value for the corresponding slot; this should usually be avoided.) If there are any unfilled slots for which no default value is specified, a `TypeError` exception is raised. Otherwise, the list of filled slots is used as the argument list for the call.

**CPython implementation detail:** An implementation may provide built-in functions whose positional parameters do not have names, even if they are ‘named’ for the purpose of documentation, and which therefore cannot be supplied by keyword. In CPython, this is the case for functions implemented in C that use [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 to parse their arguments.

If there are more positional arguments than there are formal parameter slots, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised, unless a formal parameter using the syntax `*identifier` is present; in this case, that formal parameter receives a tuple containing the excess positional arguments (or an empty tuple if there were no excess positional arguments).

If any keyword argument does not correspond to a formal parameter name, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised, unless a formal parameter using the syntax `**identifier` is present; in this case, that formal parameter receives a dictionary containing the excess keyword arguments (using the keywords as keys and the argument values as corresponding values), or a (new) empty dictionary if there were no excess keyword arguments.

If the syntax `*expression` appears in the function call, `expression` must evaluate to an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
. Elements from these iterables are treated as if they were additional positional arguments. For the call `f(x1, x2, *y, x3, x4)`, if _y_ evaluates to a sequence _y1_, …, _yM_, this is equivalent to a call with M+4 positional arguments _x1_, _x2_, _y1_, …, _yM_, _x3_, _x4_.

A consequence of this is that although the `*expression` syntax may appear _after_ explicit keyword arguments, it is processed _before_ the keyword arguments (and any `**expression` arguments – see below). So:

Copy

\>>> def f(a, b):
...     print(a, b)
...
\>>> f(b\=1, \*(2,))
2 1
\>>> f(a\=1, \*(2,))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for keyword argument 'a'
\>>> f(1, \*(2,))
1 2

It is unusual for both keyword arguments and the `*expression` syntax to be used in the same call, so in practice this confusion does not often arise.

If the syntax `**expression` appears in the function call, `expression` must evaluate to a [mapping](https://docs.python.org/3/glossary.html#term-mapping)
, the contents of which are treated as additional keyword arguments. If a parameter matching a key has already been given a value (by an explicit keyword argument, or from another unpacking), a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised.

When `**expression` is used, each key in this mapping must be a string. Each value from the mapping is assigned to the first formal parameter eligible for keyword assignment whose name is equal to the key. A key need not be a Python identifier (e.g. `"max-temp °F"` is acceptable, although it will not match any formal parameter that could be declared). If there is no match to a formal parameter the key-value pair is collected by the `**` parameter, if there is one, or if there is not, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised.

Formal parameters using the syntax `*identifier` or `**identifier` cannot be used as positional argument slots or as keyword argument names.

Changed in version 3.5: Function calls accept any number of `*` and `**` unpackings, positional arguments may follow iterable unpackings (`*`), and keyword arguments may follow dictionary unpackings (`**`). Originally proposed by [**PEP 448**](https://peps.python.org/pep-0448/)
.

A call always returns some value, possibly `None`, unless it raises an exception. How this value is computed depends on the type of the callable object.

If it is—

a user-defined function:

The code block for the function is executed, passing it the argument list. The first thing the code block will do is bind the formal parameters to the arguments; this is described in section [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function)
. When the code block executes a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement, this specifies the return value of the function call. If execution reaches the end of the code block without executing a `return` statement, the return value is `None`.

a built-in function or method:

The result is up to the interpreter; see [Built-in functions](https://docs.python.org/3/builtins/functions.html#built-in-funcs)
 for the descriptions of built-in functions and methods.

a class object:

A new instance of that class is returned.

a class instance method:

The corresponding user-defined function is called, with an argument list that is one longer than the argument list of the call: the instance becomes the first argument.

a class instance:

The class must define a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method; the effect is then the same as if that method was called.

6.4. Await expression[¶](https://docs.python.org/3/reference/expressions.html#await-expression "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Suspend the execution of [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 on an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 object. Can only be used inside a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
.

**await\_expr**: "await" [`primary`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-primary)

Added in version 3.5.

6.5. The power operator[¶](https://docs.python.org/3/reference/expressions.html#the-power-operator "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The power operator binds more tightly than unary operators on its left; it binds less tightly than unary operators on its right. The syntax is:

**power**: ([`await_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-await_expr)
 | [`primary`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-primary)
) \["\*\*" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)\
\]

Thus, in an unparenthesized sequence of power and unary operators, the operators are evaluated from right to left (this does not constrain the evaluation order for the operands): `-1**2` results in `-1`.

The power operator has the same semantics as the built-in [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
 function, when called with two arguments: it yields its left argument raised to the power of its right argument. Numeric arguments are first [converted to a common type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
, and the result is of that type.

For int operands, the result has the same type as the operands unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, `10**2` returns `100`, but `10**-2` returns `0.01`.

Raising `0.0` to a negative power results in a [`ZeroDivisionError`](https://docs.python.org/3/builtins/exceptions.html#ZeroDivisionError "ZeroDivisionError")
. Raising a negative number to a fractional power results in a [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 number. (In earlier versions it raised a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.)

This operation can be customized using the special [`__pow__()`](https://docs.python.org/3/reference/datamodel.html#object.__pow__ "object.__pow__")
 and [`__rpow__()`](https://docs.python.org/3/reference/datamodel.html#object.__rpow__ "object.__rpow__")
 methods.

6.6. Unary arithmetic and bitwise operations[¶](https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

All unary arithmetic and bitwise operations have the same priority:

**u\_expr**: [`power`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-power)
 | "-" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 | "+" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 | "~" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)

The unary `-` (minus) operator yields the negation of its numeric argument; the operation can be overridden with the [`__neg__()`](https://docs.python.org/3/reference/datamodel.html#object.__neg__ "object.__neg__")
 special method.

The unary `+` (plus) operator yields its numeric argument unchanged; the operation can be overridden with the [`__pos__()`](https://docs.python.org/3/reference/datamodel.html#object.__pos__ "object.__pos__")
 special method.

The unary `~` (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of `x` is defined as `-(x+1)`. It only applies to integral numbers or to custom objects that override the [`__invert__()`](https://docs.python.org/3/reference/datamodel.html#object.__invert__ "object.__invert__")
 special method.

In all three cases, if the argument does not have the proper type, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception is raised.

6.7. Binary arithmetic operations[¶](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

The binary arithmetic operations have the conventional priority levels. Note that some of these operations also apply to certain non-numeric types. Apart from the power operator, there are only two levels, one for multiplicative operators and one for additive operators:

**m\_expr**: [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 | [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 "\*" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 | [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 "@" [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 |
        [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 "//" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 | [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 "/" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
 |
        [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 "%" [`u_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-u_expr)
**a\_expr**: [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 | [`a_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-a_expr)
 "+" [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)
 | [`a_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-a_expr)
 "-" [`m_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-m_expr)

The `*` (multiplication) operator yields the product of its arguments. The arguments must either both be numbers, or one argument must be an integer and the other must be a sequence. In the former case, the numbers are [converted to a common real type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
 and then multiplied together. In the latter case, sequence repetition is performed; a negative repetition factor yields an empty sequence.

This operation can be customized using the special [`__mul__()`](https://docs.python.org/3/reference/datamodel.html#object.__mul__ "object.__mul__")
 and [`__rmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmul__ "object.__rmul__")
 methods.

Changed in version 3.14: If only one operand is a complex number, the other operand is converted to a floating-point number.

The `@` (at) operator is intended to be used for matrix multiplication. No builtin Python types implement this operator.

This operation can be customized using the special [`__matmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__matmul__ "object.__matmul__")
 and [`__rmatmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmatmul__ "object.__rmatmul__")
 methods.

Added in version 3.5.

The `/` (division) and `//` (floor division) operators yield the quotient of their arguments. The numeric arguments are first [converted to a common type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
. Division of integers yields a float, while floor division of integers results in an integer; the result is that of mathematical division with the ‘floor’ function applied to the result. Division by zero raises the [`ZeroDivisionError`](https://docs.python.org/3/builtins/exceptions.html#ZeroDivisionError "ZeroDivisionError")
 exception.

The division operation can be customized using the special [`__truediv__()`](https://docs.python.org/3/reference/datamodel.html#object.__truediv__ "object.__truediv__")
 and [`__rtruediv__()`](https://docs.python.org/3/reference/datamodel.html#object.__rtruediv__ "object.__rtruediv__")
 methods. The floor division operation can be customized using the special [`__floordiv__()`](https://docs.python.org/3/reference/datamodel.html#object.__floordiv__ "object.__floordiv__")
 and [`__rfloordiv__()`](https://docs.python.org/3/reference/datamodel.html#object.__rfloordiv__ "object.__rfloordiv__")
 methods.

The `%` (modulo) operator yields the remainder from the division of the first argument by the second. The numeric arguments are first [converted to a common type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
. A zero right argument raises the [`ZeroDivisionError`](https://docs.python.org/3/builtins/exceptions.html#ZeroDivisionError "ZeroDivisionError")
 exception. The arguments may be floating-point numbers, e.g., `3.14%0.7` equals `0.34` (since `3.14` equals `4*0.7 + 0.34`.) The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand [\[1\]](https://docs.python.org/3/reference/expressions.html#id22)
.

The floor division and modulo operators are connected by the following identity: `x == (x//y)*y + (x%y)`. Floor division and modulo are also connected with the built-in function [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
: `divmod(x, y) == (x//y, x%y)`. [\[2\]](https://docs.python.org/3/reference/expressions.html#id23)
.

In addition to performing the modulo operation on numbers, the `%` operator is also overloaded by string objects to perform old-style string formatting (also known as interpolation). The syntax for string formatting is described in the Python Library Reference, section [printf-style String Formatting](https://docs.python.org/3/builtins/stdtypes.html#old-string-formatting)
.

The _modulo_ operation can be customized using the special [`__mod__()`](https://docs.python.org/3/reference/datamodel.html#object.__mod__ "object.__mod__")
 and [`__rmod__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmod__ "object.__rmod__")
 methods.

The floor division operator, the modulo operator, and the [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
 function are not defined for complex numbers. Instead, convert to a floating-point number using the [`abs()`](https://docs.python.org/3/builtins/functions.html#abs "abs")
 function if appropriate.

The `+` (addition) operator yields the sum of its arguments. The arguments must either both be numbers or both be sequences of the same type. In the former case, the numbers are [converted to a common real type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
 and then added together. In the latter case, the sequences are concatenated.

This operation can be customized using the special [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
 and [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
 methods.

Changed in version 3.14: If only one operand is a complex number, the other operand is converted to a floating-point number.

The `-` (subtraction) operator yields the difference of its arguments. The numeric arguments are first [converted to a common real type](https://docs.python.org/3/builtins/stdtypes.html#stdtypes-mixed-arithmetic)
.

This operation can be customized using the special [`__sub__()`](https://docs.python.org/3/reference/datamodel.html#object.__sub__ "object.__sub__")
 and [`__rsub__()`](https://docs.python.org/3/reference/datamodel.html#object.__rsub__ "object.__rsub__")
 methods.

Changed in version 3.14: If only one operand is a complex number, the other operand is converted to a floating-point number.

6.8. Shifting operations[¶](https://docs.python.org/3/reference/expressions.html#shifting-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The shifting operations have lower priority than the arithmetic operations:

**shift\_expr**: [`a_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-a_expr)
 | [`shift_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-shift_expr)
 ("<<" | ">>") [`a_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-a_expr)

These operators accept integers as arguments. They shift the first argument to the left or right by the number of bits given by the second argument.

The left shift operation can be customized using the special [`__lshift__()`](https://docs.python.org/3/reference/datamodel.html#object.__lshift__ "object.__lshift__")
 and [`__rlshift__()`](https://docs.python.org/3/reference/datamodel.html#object.__rlshift__ "object.__rlshift__")
 methods. The right shift operation can be customized using the special [`__rshift__()`](https://docs.python.org/3/reference/datamodel.html#object.__rshift__ "object.__rshift__")
 and [`__rrshift__()`](https://docs.python.org/3/reference/datamodel.html#object.__rrshift__ "object.__rrshift__")
 methods.

A right shift by _n_ bits is defined as floor division by `pow(2,n)`. A left shift by _n_ bits is defined as multiplication with `pow(2,n)`.

6.9. Binary bitwise operations[¶](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Each of the three bitwise operations has a different priority level:

**and\_expr**: [`shift_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-shift_expr)
 | [`and_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_expr)
 "&" [`shift_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-shift_expr)
**xor\_expr**: [`and_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_expr)
 | [`xor_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-xor_expr)
 "^" [`and_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_expr)
**or\_expr**:  [`xor_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-xor_expr)
 | [`or_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_expr)
 "|" [`xor_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-xor_expr)

The `&` operator yields the bitwise AND of its arguments, which must be integers or one of them must be a custom object overriding [`__and__()`](https://docs.python.org/3/reference/datamodel.html#object.__and__ "object.__and__")
 or [`__rand__()`](https://docs.python.org/3/reference/datamodel.html#object.__rand__ "object.__rand__")
 special methods.

The `^` operator yields the bitwise XOR (exclusive OR) of its arguments, which must be integers or one of them must be a custom object overriding [`__xor__()`](https://docs.python.org/3/reference/datamodel.html#object.__xor__ "object.__xor__")
 or [`__rxor__()`](https://docs.python.org/3/reference/datamodel.html#object.__rxor__ "object.__rxor__")
 special methods.

The `|` operator yields the bitwise (inclusive) OR of its arguments, which must be integers or one of them must be a custom object overriding [`__or__()`](https://docs.python.org/3/reference/datamodel.html#object.__or__ "object.__or__")
 or [`__ror__()`](https://docs.python.org/3/reference/datamodel.html#object.__ror__ "object.__ror__")
 special methods.

6.10. Comparisons[¶](https://docs.python.org/3/reference/expressions.html#comparisons "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Unlike C, all comparison operations in Python have the same priority, which is lower than that of any arithmetic, shifting or bitwise operation. Also unlike C, expressions like `a < b < c` have the interpretation that is conventional in mathematics:

**comparison**:    [`or_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_expr)
 ([`comp_operator`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comp_operator)
 [`or_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_expr)
)\*
**comp\_operator**: "<" | ">" | "==" | ">=" | "<=" | "!="
               | "is" \["not"\] | \["not"\] "in"

Comparisons yield boolean values: `True` or `False`. Custom _rich comparison methods_ may return non-boolean values. In this case Python will call [`bool()`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 on such value in boolean contexts.

Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y and y <= z`, except that `y` is evaluated only once (but in both cases `z` is not evaluated at all when `x < y` is found to be false).

Formally, if _a_, _b_, _c_, …, _y_, _z_ are expressions and _op1_, _op2_, …, _opN_ are comparison operators, then `a op1 b op2 c ... y opN z` is equivalent to `a op1 b and b op2 c and ... y opN z`, except that each expression is evaluated at most once.

Note that `a op1 b op2 c` doesn’t imply any kind of comparison between _a_ and _c_, so that, e.g., `x < y > z` is perfectly legal (though perhaps not pretty).

### 6.10.1. Value comparisons[¶](https://docs.python.org/3/reference/expressions.html#value-comparisons "Link to this heading")

The operators `<`, `>`, `==`, `>=`, `<=`, and `!=` compare the values of two objects. The objects do not need to have the same type.

Chapter [Objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects)
 states that objects have a value (in addition to type and identity). The value of an object is a rather abstract notion in Python: For example, there is no canonical access method for an object’s value. Also, there is no requirement that the value of an object should be constructed in a particular way, e.g. comprised of all its data attributes. Comparison operators implement a particular notion of what the value of an object is. One can think of them as defining the value of an object indirectly, by means of their comparison implementation.

Because all types are (direct or indirect) subtypes of [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, they inherit the default comparison behavior from `object`. Types can customize their comparison behavior by implementing _rich comparison methods_ like [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
, described in [Basic customization](https://docs.python.org/3/reference/datamodel.html#customization)
.

The default behavior for equality comparison (`==` and `!=`) is based on the identity of the objects. Hence, equality comparison of instances with the same identity results in equality, and equality comparison of instances with different identities results in inequality. A motivation for this default behavior is the desire that all objects should be reflexive (i.e. `x is y` implies `x == y`).

A default order comparison (`<`, `>`, `<=`, and `>=`) is not provided; an attempt raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. A motivation for this default behavior is the lack of a similar invariant as for equality.

The behavior of the default equality comparison, that instances with different identities are always unequal, may be in contrast to what types will need that have a sensible definition of object value and value-based equality. Such types will need to customize their comparison behavior, and in fact, a number of built-in types have done that.

The following list describes the comparison behavior of the most important built-in types.

*   Numbers of built-in numeric types ([Numeric Types — int, float, complex](https://docs.python.org/3/builtins/stdtypes.html#typesnumeric)
    ) and of the standard library types [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
     and [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     can be compared within and across their types, with the restriction that complex numbers do not support order comparison. Within the limits of the types involved, they compare mathematically (algorithmically) correct without loss of precision.
    
    The not-a-number values `float('NaN')` and `decimal.Decimal('NaN')` are special. Any ordered comparison of a number to a not-a-number value is false. A counter-intuitive implication is that not-a-number values are not equal to themselves. For example, if `x = float('NaN')`, `3 < x`, `x < 3` and `x == x` are all false, while `x != x` is true. This behavior is compliant with IEEE 754.
    
*   `None` and [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
     are singletons. [**PEP 8**](https://peps.python.org/pep-0008/)
     advises that comparisons for singletons should always be done with `is` or `is not`, never the equality operators.
    
*   Binary sequences (instances of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    ) can be compared within and across their types. They compare lexicographically using the numeric values of their elements.
    
*   Strings (instances of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) compare lexicographically using the numerical Unicode code points (the result of the built-in function [`ord()`](https://docs.python.org/3/builtins/functions.html#ord "ord")
    ) of their characters. [\[3\]](https://docs.python.org/3/reference/expressions.html#id24)
    
    Strings and binary sequences cannot be directly compared.
    
*   Sequences (instances of [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
    , [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
    , or [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
    ) can be compared only within each of their types, with the restriction that ranges do not support order comparison. Equality comparison across these types results in inequality, and ordering comparison across these types raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
    Sequences compare lexicographically using comparison of corresponding elements. The built-in containers typically assume identical objects are equal to themselves. That lets them bypass equality tests for identical objects to improve performance and to maintain their internal invariants.
    
    Lexicographical comparison between built-in collections works as follows:
    
    *   For two collections to compare equal, they must be of the same type, have the same length, and each pair of corresponding elements must compare equal (for example, `[1,2] == (1,2)` is false because the type is not the same).
        
    *   Collections that support order comparison are ordered the same as their first unequal elements (for example, `[1,2,x] <= [1,2,y]` has the same value as `x <= y`). If a corresponding element does not exist, the shorter collection is ordered first (for example, `[1,2] < [1,2,3]` is true).
        
*   Mappings (instances of [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
    ) compare equal if and only if they have equal `(key, value)` pairs. Equality comparison of the keys and values enforces reflexivity.
    
    Order comparisons (`<`, `>`, `<=`, and `>=`) raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
*   Sets (instances of [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
     or [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
    ) can be compared within and across their types.
    
    They define order comparison operators to mean subset and superset tests. Those relations do not define total orderings (for example, the two sets `{1,2}` and `{2,3}` are not equal, nor subsets of one another, nor supersets of one another). Accordingly, sets are not appropriate arguments for functions which depend on total ordering (for example, [`min()`](https://docs.python.org/3/builtins/functions.html#min "min")
    , [`max()`](https://docs.python.org/3/builtins/functions.html#max "max")
    , and [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
     produce undefined results given a list of sets as inputs).
    
    Comparison of sets enforces reflexivity of its elements.
    
*   Most other built-in types have no comparison methods implemented, so they inherit the default comparison behavior.
    

User-defined classes that customize their comparison behavior should follow some consistency rules, if possible:

*   Equality comparison should be reflexive. In other words, identical objects should compare equal:
    
    > `x is y` implies `x == y`
    
*   Comparison should be symmetric. In other words, the following expressions should have the same result:
    
    > `x == y` and `y == x`
    > 
    > `x != y` and `y != x`
    > 
    > `x < y` and `y > x`
    > 
    > `x <= y` and `y >= x`
    
*   Comparison should be transitive. The following (non-exhaustive) examples illustrate that:
    
    > `x > y and y > z` implies `x > z`
    > 
    > `x < y and y <= z` implies `x < z`
    
*   Inverse comparison should result in the boolean negation. In other words, the following expressions should have the same result:
    
    > `x == y` and `not x != y`
    > 
    > `x < y` and `not x >= y` (for total ordering)
    > 
    > `x > y` and `not x <= y` (for total ordering)
    
    The last two expressions apply to totally ordered collections (e.g. to sequences, but not to sets or mappings). See also the [`@total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
     decorator.
    
*   The [`hash()`](https://docs.python.org/3/builtins/functions.html#hash "hash")
     result should be consistent with equality. Objects that are equal should either have the same hash value, or be marked as unhashable.
    

Python does not enforce these consistency rules. In fact, the not-a-number values are an example for not following these rules.

### 6.10.2. Membership test operations[¶](https://docs.python.org/3/reference/expressions.html#membership-test-operations "Link to this heading")

The operators [`in`](https://docs.python.org/3/reference/expressions.html#in)
 and [`not in`](https://docs.python.org/3/reference/expressions.html#not-in)
 test for membership. `x in s` evaluates to `True` if _x_ is a member of _s_, and `False` otherwise. `x not in s` returns the negation of `x in s`. All built-in sequences and set types support this as well as dictionary, for which `in` tests whether the dictionary has a given key. For container types such as list, tuple, set, frozenset, dict, or collections.deque, the expression `x in y` is equivalent to `any(x is e or x == e for e in y)`.

For the string and bytes types, `x in y` is `True` if and only if _x_ is a substring of _y_. An equivalent test is `y.find(x) != -1`. Empty strings are always considered to be a substring of any other string, so `"" in "abc"` will return `True`.

For user-defined classes which define the [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 method, `x in y` returns `True` if `y.__contains__(x)` returns a true value, and `False` otherwise.

For user-defined classes which do not define [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 but do define [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
, `x in y` is `True` if some value `z`, for which the expression `x is z or x == z` is true, is produced while iterating over `y`. If an exception is raised during the iteration, it is as if [`in`](https://docs.python.org/3/reference/expressions.html#in)
 raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, `x in y` is `True` if and only if there is a non-negative integer index _i_ such that `x is y[i] or x == y[i]`, and no lower integer index raises the [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 exception. (If any other exception is raised, it is as if [`in`](https://docs.python.org/3/reference/expressions.html#in)
 raised that exception).

The operator [`not in`](https://docs.python.org/3/reference/expressions.html#not-in)
 is defined to have the inverse truth value of [`in`](https://docs.python.org/3/reference/expressions.html#in)
.

### 6.10.3. Identity comparisons[¶](https://docs.python.org/3/reference/expressions.html#is-not "Link to this heading")

The operators [`is`](https://docs.python.org/3/reference/expressions.html#is)
 and [`is not`](https://docs.python.org/3/reference/expressions.html#is-not)
 test for an object’s identity: `x is y` is true if and only if _x_ and _y_ are the same object. An Object’s identity is determined using the [`id()`](https://docs.python.org/3/builtins/functions.html#id "id")
 function. `x is not y` yields the inverse truth value. [\[4\]](https://docs.python.org/3/reference/expressions.html#id25)

6.11. Boolean operations[¶](https://docs.python.org/3/reference/expressions.html#boolean-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

**or\_test**:  [`and_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_test)
 | [`or_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_test)
 "or" [`and_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_test)
**and\_test**: [`not_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-not_test)
 | [`and_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-and_test)
 "and" [`not_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-not_test)
**not\_test**: [`comparison`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-comparison)
 | "not" [`not_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-not_test)

In the context of Boolean operations, and also when expressions are used by control flow statements, the following values are interpreted as false: `False`, `None`, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true. User-defined objects can customize their truth value by providing a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
 method.

The operator [`not`](https://docs.python.org/3/reference/expressions.html#not)
 yields `True` if its argument is false, `False` otherwise.

The expression `x and y` first evaluates _x_; if _x_ is false, its value is returned; otherwise, _y_ is evaluated and the resulting value is returned.

The expression `x or y` first evaluates _x_; if _x_ is true, its value is returned; otherwise, _y_ is evaluated and the resulting value is returned.

Note that neither [`and`](https://docs.python.org/3/reference/expressions.html#and)
 nor [`or`](https://docs.python.org/3/reference/expressions.html#or)
 restrict the value and type they return to `False` and `True`, but rather return the last evaluated argument. This is sometimes useful, e.g., if `s` is a string that should be replaced by a default value if it is empty, the expression `s or 'foo'` yields the desired value. Because [`not`](https://docs.python.org/3/reference/expressions.html#not)
 has to create a new value, it returns a boolean value regardless of the type of its argument (for example, `not 'foo'` produces `False` rather than `''`.)

6.12. Assignment expressions[¶](https://docs.python.org/3/reference/expressions.html#assignment-expressions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

**assignment\_expression**: \[[`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
 ":="\] [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)

An assignment expression (sometimes also called a “named expression” or “walrus”) assigns an [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 to an [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
, while also returning the value of the `expression`.

One common use case is when handling matched regular expressions:

Copy

if matching := pattern.search(data):
    do\_something(matching)

Or, when processing a file stream in chunks:

Copy

while chunk := file.read(9000):
    process(chunk)

Assignment expressions must be surrounded by parentheses when used as expression statements and when used as sub-expressions in slicing, conditional, lambda, keyword-argument, and comprehension-if expressions and in `assert`, `with`, and `assignment` statements. In all other places where they can be used, parentheses are not required, including in `if` and `while` statements.

Added in version 3.8: See [**PEP 572**](https://peps.python.org/pep-0572/)
 for more details about assignment expressions.

6.13. Conditional expressions[¶](https://docs.python.org/3/reference/expressions.html#conditional-expressions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

**conditional\_expression**: [`or_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_test)
 \["if" [`or_test`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_test)\
 "else" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]
**expression**:             [`conditional_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-conditional_expression)
 | [`lambda_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-lambda_expr)

A conditional expression (sometimes called a “ternary operator”) is an alternative to the if-else statement. As it is an expression, it returns a value and can appear as a sub-expression.

The expression `x if C else y` first evaluates the condition, _C_ rather than _x_. If _C_ is true, _x_ is evaluated and its value is returned; otherwise, _y_ is evaluated and its value is returned.

See [**PEP 308**](https://peps.python.org/pep-0308/)
 for more details about conditional expressions.

6.14. Lambdas[¶](https://docs.python.org/3/reference/expressions.html#lambda "Link to this heading")

-----------------------------------------------------------------------------------------------------

**lambda\_expr**: "lambda" \[[`parameter_list`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list)\
\] ":" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)

Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. The expression `lambda parameters: expression` yields a function object. The unnamed object behaves like a function object defined with:

def <lambda>(parameters):
    return expression

See section [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function)
 for the syntax of parameter lists. Note that functions created with lambda expressions cannot contain statements or annotations.

6.15. Expression lists[¶](https://docs.python.org/3/reference/expressions.html#expression-lists "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

**starred\_expression**:       "\*" [`or_expr`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-or_expr)
 | [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
**flexible\_expression**:      [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 | [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
**flexible\_expression\_list**: [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
 ("," [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
)\* \[","\]
**starred\_expression\_list**:  [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
 ("," [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
)\* \[","\]
**expression\_list**:          [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 ("," [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)\* \[","\]
**yield\_list**:               [`expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression_list)
 | [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
 "," \[[`starred_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression_list)\
\]

Except when part of a list or set display, an expression list containing at least one comma yields a tuple. The length of the tuple is the number of expressions in the list. The expressions are evaluated from left to right.

A trailing comma is required only to create a one-item tuple, such as `1,`; it is optional in all other cases. A single expression without a trailing comma doesn’t create a tuple, but rather yields the value of that expression. (To create an empty tuple, use an empty pair of parentheses: `()`.)

### 6.15.1. Iterable unpacking[¶](https://docs.python.org/3/reference/expressions.html#index-92 "Link to this heading")

In an expression list or tuple, list or set display, any expression may be prefixed with an asterisk (`*`). This denotes _iterable unpacking_.

At runtime, the asterisk-prefixed expression must evaluate to an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
. The iterable is expanded into a sequence of items, which are included in the new tuple, list, or set, at the site of the unpacking.

Added in version 3.5: Iterable unpacking in expression lists, originally proposed by [**PEP 448**](https://peps.python.org/pep-0448/)
.

Added in version 3.11: Any item in an expression list may be starred. See [**PEP 646**](https://peps.python.org/pep-0646/)
.

6.16. Evaluation order[¶](https://docs.python.org/3/reference/expressions.html#evaluation-order "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is evaluated before the left-hand side.

In the following lines, expressions will be evaluated in the arithmetic order of their suffixes:

Copy

expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 \* (expr3 \- expr4)
expr1(expr2, expr3, \*expr4, \*\*expr5)
expr3, expr4 \= expr1, expr2

6.17. Operator precedence[¶](https://docs.python.org/3/reference/expressions.html#operator-precedence "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The following table summarizes the operator precedence in Python, from highest precedence (most binding) to lowest precedence (least binding). Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. Operators in the same box group left to right (except for exponentiation and conditional expressions, which group from right to left).

Note that comparisons, membership tests, and identity tests, all have the same precedence and have a left-to-right chaining feature as described in the [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
 section.

| Operator | Description |
| --- | --- |
| `(expressions...)`,<br><br>`[expressions...]`, `{key: value...}`, `{expressions...}` | Binding or parenthesized expression, list display, dictionary display, set display |
| `x[index]`, `x[index:index]` `x(arguments...)`, `x.attribute` | Subscription (including slicing), call, attribute reference |
| [`await x`](https://docs.python.org/3/reference/expressions.html#await) | Await expression |
| `**` | Exponentiation [\[5\]](https://docs.python.org/3/reference/expressions.html#id26) |
| `+x`, `-x`, `~x` | Positive, negative, bitwise NOT |
| `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, remainder [\[6\]](https://docs.python.org/3/reference/expressions.html#id27) |
| `+`, `-` | Addition and subtraction |
| `<<`, `>>` | Shifts |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `\|` | Bitwise OR |
| [`in`](https://docs.python.org/3/reference/expressions.html#in)<br>, [`not in`](https://docs.python.org/3/reference/expressions.html#not-in)<br>, [`is`](https://docs.python.org/3/reference/expressions.html#is)<br>, [`is not`](https://docs.python.org/3/reference/expressions.html#is-not)<br>, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, including membership tests and identity tests |
| [`not x`](https://docs.python.org/3/reference/expressions.html#not) | Boolean NOT |
| [`and`](https://docs.python.org/3/reference/expressions.html#and) | Boolean AND |
| [`or`](https://docs.python.org/3/reference/expressions.html#or) | Boolean OR |
| [`if`](https://docs.python.org/3/reference/expressions.html#if-expr)<br> – `else` | Conditional expression |
| [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) | Lambda expression |
| `:=` | Assignment expression |

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [6\. Expressions](https://docs.python.org/3/reference/expressions.html#)
    *   [6.1. Arithmetic conversions](https://docs.python.org/3/reference/expressions.html#arithmetic-conversions)
        
    *   [6.2. Atoms](https://docs.python.org/3/reference/expressions.html#atoms)
        *   [6.2.1. Built-in constants](https://docs.python.org/3/reference/expressions.html#built-in-constants)
            
        *   [6.2.2. Identifiers (Names)](https://docs.python.org/3/reference/expressions.html#atom-identifiers)
            *   [6.2.2.1. Private name mangling](https://docs.python.org/3/reference/expressions.html#index-5)
                
        *   [6.2.3. Literals](https://docs.python.org/3/reference/expressions.html#literals)
            *   [6.2.3.1. Literals and object identity](https://docs.python.org/3/reference/expressions.html#literals-and-object-identity)
                
            *   [6.2.3.2. String literal concatenation](https://docs.python.org/3/reference/expressions.html#string-literal-concatenation)
                
        *   [6.2.4. Parenthesized groups](https://docs.python.org/3/reference/expressions.html#parenthesized-groups)
            
        *   [6.2.5. Container displays](https://docs.python.org/3/reference/expressions.html#container-displays)
            *   [6.2.5.1. List displays](https://docs.python.org/3/reference/expressions.html#list-displays)
                
            *   [6.2.5.2. Set displays](https://docs.python.org/3/reference/expressions.html#set-displays)
                
            *   [6.2.5.3. Tuple displays](https://docs.python.org/3/reference/expressions.html#tuple-displays)
                
            *   [6.2.5.4. Dictionary displays](https://docs.python.org/3/reference/expressions.html#dictionary-displays)
                
        *   [6.2.6. Comprehensions](https://docs.python.org/3/reference/expressions.html#comprehensions)
            *   [6.2.6.1. Filtering in comprehensions](https://docs.python.org/3/reference/expressions.html#filtering-in-comprehensions)
                
            *   [6.2.6.2. Complex comprehensions](https://docs.python.org/3/reference/expressions.html#complex-comprehensions)
                
            *   [6.2.6.3. Unpacking in comprehensions](https://docs.python.org/3/reference/expressions.html#unpacking-in-comprehensions)
                
            *   [6.2.6.4. Asynchronous comprehensions](https://docs.python.org/3/reference/expressions.html#asynchronous-comprehensions)
                
            *   [6.2.6.5. Formal grammar for comprehensions](https://docs.python.org/3/reference/expressions.html#formal-grammar-for-comprehensions)
                
        *   [6.2.7. Generator expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
            
        *   [6.2.8. Yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)
            *   [6.2.8.1. Examples](https://docs.python.org/3/reference/expressions.html#examples)
                
            *   [6.2.8.2. Asynchronous generator functions](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions)
                
    *   [6.3. Primaries](https://docs.python.org/3/reference/expressions.html#primaries)
        *   [6.3.1. Attribute references](https://docs.python.org/3/reference/expressions.html#attribute-references)
            
        *   [6.3.2. Subscriptions and slicings](https://docs.python.org/3/reference/expressions.html#subscriptions-and-slicings)
            *   [6.3.2.1. Slicings](https://docs.python.org/3/reference/expressions.html#slicings)
                
            *   [6.3.2.2. Comma-separated subscripts](https://docs.python.org/3/reference/expressions.html#comma-separated-subscripts)
                
            *   [6.3.2.3. “Starred” subscriptions](https://docs.python.org/3/reference/expressions.html#starred-subscriptions)
                
            *   [6.3.2.4. Formal subscription grammar](https://docs.python.org/3/reference/expressions.html#formal-subscription-grammar)
                
        *   [6.3.3. Calls](https://docs.python.org/3/reference/expressions.html#calls)
            
    *   [6.4. Await expression](https://docs.python.org/3/reference/expressions.html#await-expression)
        
    *   [6.5. The power operator](https://docs.python.org/3/reference/expressions.html#the-power-operator)
        
    *   [6.6. Unary arithmetic and bitwise operations](https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations)
        
    *   [6.7. Binary arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
        
    *   [6.8. Shifting operations](https://docs.python.org/3/reference/expressions.html#shifting-operations)
        
    *   [6.9. Binary bitwise operations](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations)
        
    *   [6.10. Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
        *   [6.10.1. Value comparisons](https://docs.python.org/3/reference/expressions.html#value-comparisons)
            
        *   [6.10.2. Membership test operations](https://docs.python.org/3/reference/expressions.html#membership-test-operations)
            
        *   [6.10.3. Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)
            
    *   [6.11. Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)
        
    *   [6.12. Assignment expressions](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
        
    *   [6.13. Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
        
    *   [6.14. Lambdas](https://docs.python.org/3/reference/expressions.html#lambda)
        
    *   [6.15. Expression lists](https://docs.python.org/3/reference/expressions.html#expression-lists)
        *   [6.15.1. Iterable unpacking](https://docs.python.org/3/reference/expressions.html#index-92)
            
    *   [6.16. Evaluation order](https://docs.python.org/3/reference/expressions.html#evaluation-order)
        
    *   [6.17. Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
        

#### Previous topic

[5\. The import system](https://docs.python.org/3/reference/import.html "previous chapter")

#### Next topic

[7\. Simple statements](https://docs.python.org/3/reference/simple_stmts.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=6.+Expressions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fexpressions.html&pagesource=reference%2Fexpressions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/expressions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/simple_stmts.html "7. Simple statements")
     |
*   [previous](https://docs.python.org/3/reference/import.html "5. The import system")
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
*   [6\. Expressions](https://docs.python.org/3/reference/expressions.html)
    
*    
    
    |
*   Theme Auto Light Dark |