### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/toplevel_components.html "9. Top-level components")
     |
*   [previous](https://docs.python.org/3/reference/simple_stmts.html "7. Simple statements")
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
*   [8\. Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
    
*    
    
    |
*   Theme Auto Light Dark |

8\. Compound statements[¶](https://docs.python.org/3/reference/compound_stmts.html#compound-statements "Link to this heading")

===============================================================================================================================

Compound statements contain (groups of) other statements; they affect or control the execution of those other statements in some way. In general, compound statements span multiple lines, although in simple incarnations a whole compound statement may be contained in one line.

The [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
, [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)
 and [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 statements implement traditional control flow constructs. [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 specifies exception handlers and/or cleanup code for a group of statements, while the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement allows the execution of initialization and finalization code around a block of code. Function and class definitions are also syntactically compound statements.

A compound statement consists of one or more ‘clauses.’ A clause consists of a header and a ‘suite.’ The clause headers of a particular compound statement are all at the same indentation level. Each clause header begins with a uniquely identifying keyword and ends with a colon. A suite is a group of statements controlled by a clause. A suite can be one or more semicolon-separated simple statements on the same line as the header, following the header’s colon, or it can be one or more indented statements on subsequent lines. Only the latter form of a suite can contain nested compound statements; the following is illegal, mostly because it wouldn’t be clear to which [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
 clause a following [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
 clause would belong:

Copy

if test1: if test2: print(x)

Also note that the semicolon binds tighter than the colon in this context, so that in the following example, either all or none of the [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 calls are executed:

Copy

if x < y < z: print(x); print(y); print(z)

Summarizing:

**compound\_stmt**: [`if_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-if_stmt)
               | [`while_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-while_stmt)
               | [`for_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-for_stmt)
               | [`try_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-try_stmt)
               | [`with_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt)
               | [`match_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-match_stmt)
               | [`funcdef`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-funcdef)
               | [`classdef`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-classdef)
               | [`async_with_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-async_with_stmt)
               | [`async_for_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-async_for_stmt)
               | [`async_funcdef`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-async_funcdef)
**suite**:         [`stmt_list`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-stmt_list)
 NEWLINE | NEWLINE INDENT [`statement`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-statement)
\+ DEDENT
**statement**:     [`stmt_list`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-stmt_list)
 NEWLINE | [`compound_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-compound_stmt)
**stmt\_list**:     [`simple_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-simple_stmt)
 (";" [`simple_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-simple_stmt)
)\* \[";"\]

Note that statements always end in a `NEWLINE` possibly followed by a `DEDENT`. Also note that optional continuation clauses always begin with a keyword that cannot start a statement, thus there are no ambiguities (the ‘dangling [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
’ problem is solved in Python by requiring nested [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
 statements to be indented).

The formatting of the grammar rules in the following sections places each clause on a separate line for clarity.

8.1. The `if` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
 statement is used for conditional execution:

**if\_stmt**: "if" [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
         ("elif" [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
)\*
         \["else" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]

It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section [Boolean operations](https://docs.python.org/3/reference/expressions.html#booleans)
 for the definition of true and false); then that suite is executed (and no other part of the [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
 statement is executed or evaluated). If all expressions are false, the suite of the [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
 clause, if present, is executed.

8.2. The `while` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)
 statement is used for repeated execution as long as an expression is true:

**while\_stmt**: "while" [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
            \["else" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]

This repeatedly tests the expression and, if it is true, executes the first suite; if the expression is false (which may be the first time it is tested) the suite of the `else` clause, if present, is executed and the loop terminates.

A [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 statement executed in the first suite terminates the loop without executing the `else` clause’s suite. A [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 statement executed in the first suite skips the rest of the suite and goes back to testing the expression.

8.3. The `for` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:

**for\_stmt**: "for" [`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)
 "in" [`starred_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression_list)
 ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
          \["else" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]

The [`starred_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression_list)
 expression is evaluated once; it should yield an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 object. An [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 is created for that iterable. The first item provided by the iterator is then assigned to the target list using the standard rules for assignments (see [Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment)
), and the suite is executed. This repeats for each item provided by the iterator. When the iterator is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
, the suite in the `else` clause, if present, is executed, and the loop terminates.

A [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 statement executed in the first suite terminates the loop without executing the `else` clause’s suite. A [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 statement executed in the first suite skips the rest of the suite and continues with the next item, or with the `else` clause if there is no next item.

The for-loop makes assignments to the variables in the target list. This overwrites all previous assignments to those variables including those made in the suite of the for-loop:

Copy

for i in range(10):
    print(i)
    i \= 5             \# this will not affect the for-loop
                      \# because i will be overwritten with the next
                      \# index in the range

Names in the target list are not deleted when the loop is finished, but if the sequence is empty, they will not have been assigned to at all by the loop. Hint: the built-in type [`range()`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
 represents immutable arithmetic sequences of integers. For instance, iterating `range(3)` successively yields 0, 1, and then 2.

Changed in version 3.11: Starred elements are now allowed in the expression list.

8.4. The `try` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The `try` statement specifies exception handlers and/or cleanup code for a group of statements:

**try\_stmt**:  [`try1_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-try1_stmt)
 | [`try2_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-try2_stmt)
 | [`try3_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-try3_stmt)
**try1\_stmt**: "try" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
           ("except" \[[`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\]\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
)+
           \["else" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]
           \["finally" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]
**try2\_stmt**: "try" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
           ("except" "\*" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
)+
           \["else" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]
           \["finally" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)\
\]
**try3\_stmt**: "try" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
           "finally" ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)

Additional information on exceptions can be found in section [Exceptions](https://docs.python.org/3/reference/executionmodel.html#exceptions)
, and information on using the [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise)
 statement to generate exceptions may be found in section [The raise statement](https://docs.python.org/3/reference/simple_stmts.html#raise)
.

Changed in version 3.14: Support for optionally dropping grouping parentheses when using multiple exception types. See [**PEP 758**](https://peps.python.org/pep-0758/)
.

### 8.4.1. `except` clause[¶](https://docs.python.org/3/reference/compound_stmts.html#except-clause "Link to this heading")

The `except` clause(s) specify one or more exception handlers. When no exception occurs in the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 clause, no exception handler is executed. When an exception occurs in the `try` suite, a search for an exception handler is started. This search inspects the `except` clauses in turn until one is found that matches the exception. An expression-less `except` clause, if present, must be last; it matches any exception.

For an `except` clause with an expression, the expression must evaluate to an exception type or a tuple of exception types. Parentheses can be dropped if multiple exception types are provided and the `as` clause is not used. The raised exception matches an `except` clause whose expression evaluates to the class or a [non-virtual base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 of the exception object, or to a tuple that contains such a class.

If no `except` clause matches the exception, the search for an exception handler continues in the surrounding code and on the invocation stack. [\[1\]](https://docs.python.org/3/reference/compound_stmts.html#id22)

If the evaluation of an expression in the header of an `except` clause raises an exception, the original search for a handler is canceled and a search starts for the new exception in the surrounding code and on the call stack (it is treated as if the entire [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement raised the exception).

When a matching `except` clause is found, the exception is assigned to the target specified after the `as` keyword in that `except` clause, if present, and the `except` clause’s suite is executed. All `except` clauses must have an executable block. When the end of this block is reached, execution continues normally after the entire [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement. (This means that if two nested handlers exist for the same exception, and the exception occurs in the `try` clause of the inner handler, the outer handler will not handle the exception.)

When an exception has been assigned using `as target`, it is cleared at the end of the `except` clause. This is as if:

Copy

except E as N:
    foo

was translated to:

Copy

except E as N:
    try:
        foo
    finally:
        del N

This means the exception must be assigned to a different name to be able to refer to it after the `except` clause. Exceptions are cleared because with the traceback attached to them, they form a reference cycle with the stack frame, keeping all locals in that frame alive until the next garbage collection occurs.

Before an `except` clause’s suite is executed, the exception is stored in the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module, where it can be accessed from within the body of the `except` clause by calling [`sys.exception()`](https://docs.python.org/3/library/sys.html#sys.exception "sys.exception")
. When leaving an exception handler, the exception stored in the `sys` module is reset to its previous value:

Copy

\>>> print(sys.exception())
None
\>>> try:
...     raise TypeError
... except:
...     print(repr(sys.exception()))
...     try:
...          raise ValueError
...     except:
...         print(repr(sys.exception()))
...     print(repr(sys.exception()))
...
TypeError()
ValueError()
TypeError()
\>>> print(sys.exception())
None

### 8.4.2. `except*` clause[¶](https://docs.python.org/3/reference/compound_stmts.html#except-star "Link to this heading")

The `except*` clause(s) specify one or more handlers for groups of exceptions ([`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")
 instances). A [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement can have either [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 or `except*` clauses, but not both. The exception type for matching is mandatory in the case of `except*`, so `except*:` is a syntax error. The type is interpreted as in the case of `except`, but matching is performed on the exceptions contained in the group that is being handled. A [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if a matching type is a subclass of `BaseExceptionGroup`, because that would have ambiguous semantics.

When an exception group is raised in the try block, each `except*` clause splits (see [`split()`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup.split "BaseExceptionGroup.split")
) it into the subgroups of matching and non-matching exceptions. If the matching subgroup is not empty, it becomes the handled exception (the value returned from [`sys.exception()`](https://docs.python.org/3/library/sys.html#sys.exception "sys.exception")
) and assigned to the target of the `except*` clause (if there is one). Then, the body of the `except*` clause executes. If the non-matching subgroup is not empty, it is processed by the next `except*` in the same manner. This continues until all exceptions in the group have been matched, or the last `except*` clause has run.

After all `except*` clauses execute, the group of unhandled exceptions is merged with any exceptions that were raised or re-raised from within `except*` clauses. This merged exception group propagates on:

Copy

\>>> try:
...     raise ExceptionGroup("eg",
...         \[ValueError(1), TypeError(2), OSError(3), OSError(4)\])
... except\* TypeError as e:
...     print(f'caught {type(e)} with nested {e.exceptions}')
... except\* OSError as e:
...     print(f'caught {type(e)} with nested {e.exceptions}')
...
caught <class 'ExceptionGroup'> with nested (TypeError(2),)
caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
  + Exception Group Traceback (most recent call last):
  |   File "<doctest default\[0\]>", line 2, in <module>
  |     raise ExceptionGroup("eg",
  |         \[ValueError(1), TypeError(2), OSError(3), OSError(4)\])
  | ExceptionGroup: eg (1 sub-exception)
  +-+---------------- 1 ----------------
    | ValueError: 1
    +------------------------------------

If the exception raised from the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 block is not an exception group and its type matches one of the `except*` clauses, it is caught and wrapped by an exception group with an empty message string. This ensures that the type of the target `e` is consistently [`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")
:

Copy

\>>> try:
...     raise BlockingIOError
... except\* BlockingIOError as e:
...     print(repr(e))
...
ExceptionGroup('', (BlockingIOError(),))

[`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
, [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 and [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 cannot appear in an `except*` clause.

### 8.4.3. `else` clause[¶](https://docs.python.org/3/reference/compound_stmts.html#else-clause "Link to this heading")

The optional `else` clause is executed if the control flow leaves the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 suite, no exception was raised, and no [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
, [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
, or [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 statement was executed. Exceptions in the `else` clause are not handled by the preceding [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 clauses.

### 8.4.4. `finally` clause[¶](https://docs.python.org/3/reference/compound_stmts.html#finally-clause "Link to this heading")

If `finally` is present, it specifies a ‘cleanup’ handler. The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 clause is executed, including any [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 and [`else`](https://docs.python.org/3/reference/compound_stmts.html#except-else)
 clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved. The `finally` clause is executed. If there is a saved exception it is re-raised at the end of the `finally` clause. If the `finally` clause raises another exception, the saved exception is set as the context of the new exception. If the `finally` clause executes a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
, [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 or [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 statement, the saved exception is discarded. For example, this function returns 42.

Copy

def f():
    try:
        1/0
    finally:
        return 42

The exception information is not available to the program during execution of the `finally` clause.

When a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
, [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 or [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 statement is executed in the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 suite of a `try`…`finally` statement, the `finally` clause is also executed ‘on the way out.’

The return value of a function is determined by the last [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement executed. Since the `finally` clause always executes, a `return` statement executed in the `finally` clause will always be the last one executed. The following function returns ‘finally’.

Copy

def foo():
    try:
        return 'try'
    finally:
        return 'finally'

Changed in version 3.8: Prior to Python 3.8, a [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 statement was illegal in the `finally` clause due to a problem with the implementation.

Changed in version 3.14: The compiler emits a [`SyntaxWarning`](https://docs.python.org/3/builtins/exceptions.html#SyntaxWarning "SyntaxWarning")
 when a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
, [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 or [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 appears in a `finally` block (see [**PEP 765**](https://peps.python.org/pep-0765/)
).

8.5. The `with` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement is used to wrap the execution of a block with methods defined by a context manager (see section [With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
). This allows common [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
…[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
…[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 usage patterns to be encapsulated for convenient reuse.

**with\_stmt**:          "with" ( "(" [`with_stmt_contents`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt_contents)
 ","? ")" | [`with_stmt_contents`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt_contents)
 ) ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
**with\_stmt\_contents**: [`with_item`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_item)
 ("," [`with_item`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_item)
)\*
**with\_item**:          [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 \["as" [`target`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target)\
\]

The execution of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement with one “item” proceeds as follows:

1.  The context expression (the expression given in the [`with_item`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_item)
    ) is evaluated to obtain a context manager.
    
2.  The context manager’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     is loaded for later use.
    
3.  The context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     is loaded for later use.
    
4.  The context manager’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     method is invoked.
    
5.  If a target was included in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statement, the return value from [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     is assigned to it.
    
    Note
    
    The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statement guarantees that if the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
     method returns without an error, then [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     will always be called. Thus, if an error occurs during the assignment to the target list, it will be treated the same as an error occurring within the suite would be. See step 7 below.
    
6.  The suite is executed.
    
7.  The context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     method is invoked. If an exception caused the suite to be exited, its type, value, and traceback are passed as arguments to `__exit__()`. Otherwise, three [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
     arguments are supplied.
    
    If the suite was exited due to an exception, and the return value from the [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     method was false, the exception is reraised. If the return value was true, the exception is suppressed, and execution continues with the statement following the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statement.
    
    If the suite was exited for any reason other than an exception, the return value from [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
     is ignored, and execution proceeds at the normal location for the kind of exit that was taken.
    

The following code:

Copy

with EXPRESSION as TARGET:
    SUITE

is semantically equivalent to:

Copy

manager \= (EXPRESSION)
enter \= manager.\_\_enter\_\_
exit \= manager.\_\_exit\_\_
value \= enter()
hit\_except \= False

try:
    TARGET \= value
    SUITE
except:
    hit\_except \= True
    if not exit(\*sys.exc\_info()):
        raise
finally:
    if not hit\_except:
        exit(None, None, None)

except that implicit [special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)
 is used for [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
.

With more than one item, the context managers are processed as if multiple [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements were nested:

Copy

with A() as a, B() as b:
    SUITE

is semantically equivalent to:

Copy

with A() as a:
    with B() as b:
        SUITE

You can also write multi-item context managers in multiple lines if the items are surrounded by parentheses. For example:

Copy

with (
    A() as a,
    B() as b,
):
    SUITE

Changed in version 3.1: Support for multiple context expressions.

Changed in version 3.10: Support for using grouping parentheses to break the statement in multiple lines.

See also

[**PEP 343**](https://peps.python.org/pep-0343/)
 - The “with” statement

The specification, background, and examples for the Python [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

8.6. The `match` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Added in version 3.10.

The match statement is used for pattern matching. Syntax:

**match\_stmt**:   'match' [`subject_expr`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-subject_expr)
 ":" NEWLINE INDENT [`case_block`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-case_block)
\+ DEDENT
**subject\_expr**: [`flexible_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression)
 "," \[[`flexible_expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-flexible_expression_list)\
 \[','\]\]
              | [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
**case\_block**:   'case' [`patterns`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-patterns)
 \[[`guard`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-guard)\
\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)

Note

This section uses single quotes to denote [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
.

Pattern matching takes a pattern as input (following `case`) and a subject value (following `match`). The pattern (which may contain subpatterns) is matched against the subject value. The outcomes are:

*   A match success or failure (also termed a pattern success or failure).
    
*   Possible binding of matched values to a name. The prerequisites for this are further discussed below.
    

The `match` and `case` keywords are [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
.

See also

*   [**PEP 634**](https://peps.python.org/pep-0634/)
     – Structural Pattern Matching: Specification
    
*   [**PEP 636**](https://peps.python.org/pep-0636/)
     – Structural Pattern Matching: Tutorial
    

### 8.6.1. Overview[¶](https://docs.python.org/3/reference/compound_stmts.html#overview "Link to this heading")

Here’s an overview of the logical flow of a match statement:

1.  The subject expression `subject_expr` is evaluated and a resulting subject value obtained. If the subject expression contains a comma, a tuple is constructed using [the standard rules](https://docs.python.org/3/builtins/stdtypes.html#typesseq-tuple)
    .
    
2.  Each pattern in a `case_block` is attempted to match with the subject value. The specific rules for success or failure are described below. The match attempt can also bind some or all of the standalone names within the pattern. The precise pattern binding rules vary per pattern type and are specified below. **Name bindings made during a successful pattern match outlive the executed block and can be used after the match statement**.
    
    Note
    
    During failed pattern matches, some subpatterns may succeed. Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match. The exact behavior is dependent on implementation and may vary. This is an intentional decision made to allow different implementations to add optimizations.
    
3.  If the pattern succeeds, the corresponding guard (if present) is evaluated. In this case all name bindings are guaranteed to have happened.
    
    *   If the guard evaluates as true or is missing, the `block` inside `case_block` is executed.
        
    *   Otherwise, the next `case_block` is attempted as described above.
        
    *   If there are no further case blocks, the match statement is completed.
        

Note

Users should generally never rely on a pattern being evaluated. Depending on implementation, the interpreter may cache values or use other optimizations which skip repeated evaluations.

A sample match statement:

Copy

\>>> flag \= False
\>>> match (100, 200):
...    case (100, 300):  \# Mismatch: 200 != 300
...        print('Case 1')
...    case (100, 200) if flag:  \# Successful match, but guard fails
...        print('Case 2')
...    case (100, y):  \# Matches and binds y to 200
...        print(f'Case 3, y: {y}')
...    case \_:  \# Pattern not attempted
...        print('Case 4, I match anything!')
...
Case 3, y: 200

In this case, `if flag` is a guard. Read more about that in the next section.

### 8.6.2. Guards[¶](https://docs.python.org/3/reference/compound_stmts.html#guards "Link to this heading")

**guard**: "if" [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)

A `guard` (which is part of the `case`) must succeed for code inside the `case` block to execute. It takes the form: [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
 followed by an expression.

The logical flow of a `case` block with a `guard` follows:

1.  Check that the pattern in the `case` block succeeded. If the pattern failed, the `guard` is not evaluated and the next `case` block is checked.
    
2.  If the pattern succeeded, evaluate the `guard`.
    
    *   If the `guard` condition evaluates as true, the case block is selected.
        
    *   If the `guard` condition evaluates as false, the case block is not selected.
        
    *   If the `guard` raises an exception during evaluation, the exception bubbles up.
        

Guards are allowed to have side effects as they are expressions. Guard evaluation must proceed from the first to the last case block, one at a time, skipping case blocks whose pattern(s) don’t all succeed. (I.e., guard evaluation must happen in order.) Guard evaluation must stop once a case block is selected.

### 8.6.3. Irrefutable Case Blocks[¶](https://docs.python.org/3/reference/compound_stmts.html#irrefutable-case-blocks "Link to this heading")

An irrefutable case block is a match-all case block. A match statement may have at most one irrefutable case block, and it must be last.

A case block is considered irrefutable if it has no guard and its pattern is irrefutable. A pattern is considered irrefutable if we can prove from its syntax alone that it will always succeed. Only the following patterns are irrefutable:

*   [AS Patterns](https://docs.python.org/3/reference/compound_stmts.html#as-patterns)
     whose left-hand side is irrefutable
    
*   [OR Patterns](https://docs.python.org/3/reference/compound_stmts.html#or-patterns)
     containing at least one irrefutable pattern
    
*   [Capture Patterns](https://docs.python.org/3/reference/compound_stmts.html#capture-patterns)
    
*   [Wildcard Patterns](https://docs.python.org/3/reference/compound_stmts.html#wildcard-patterns)
    
*   parenthesized irrefutable patterns
    

### 8.6.4. Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#patterns "Link to this heading")

Note

This section uses grammar notations beyond standard EBNF:

*   the notation `SEP.RULE+` is shorthand for `RULE (SEP RULE)*`
    
*   the notation `!RULE` is shorthand for a negative lookahead assertion
    

The top-level syntax for `patterns` is:

**patterns**:       [`open_sequence_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-open_sequence_pattern)
 | [`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)
**pattern**:        [`as_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-as_pattern)
 | [`or_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-or_pattern)
**closed\_pattern**: | [`literal_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-literal_pattern)
                | [`capture_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-capture_pattern)
                | [`wildcard_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-wildcard_pattern)
                | [`value_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-value_pattern)
                | [`group_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-group_pattern)
                | [`sequence_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-sequence_pattern)
                | [`mapping_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-mapping_pattern)
                | [`class_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-class_pattern)

The descriptions below will include a description “in simple terms” of what a pattern does for illustration purposes (credits to Raymond Hettinger for a document that inspired most of the descriptions). Note that these descriptions are purely for illustration purposes and **may not** reflect the underlying implementation. Furthermore, they do not cover all valid forms.

#### 8.6.4.1. OR Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#or-patterns "Link to this heading")

An OR pattern is two or more patterns separated by vertical bars `|`. Syntax:

**or\_pattern**: "|".[`closed_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-closed_pattern)
+

Only the final subpattern may be [irrefutable](https://docs.python.org/3/reference/compound_stmts.html#irrefutable-case)
, and each subpattern must bind the same set of names to avoid ambiguity.

An OR pattern matches each of its subpatterns in turn to the subject value, until one succeeds. The OR pattern is then considered successful. Otherwise, if none of the subpatterns succeed, the OR pattern fails.

In simple terms, `P1 | P2 | ...` will try to match `P1`, if it fails it will try to match `P2`, succeeding immediately if any succeeds, failing otherwise.

#### 8.6.4.2. AS Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#as-patterns "Link to this heading")

An AS pattern matches an OR pattern on the left of the [`as`](https://docs.python.org/3/reference/compound_stmts.html#as)
 keyword against a subject. Syntax:

**as\_pattern**: [`or_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-or_pattern)
 "as" [`capture_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-capture_pattern)

If the OR pattern fails, the AS pattern fails. Otherwise, the AS pattern binds the subject to the name on the right of the as keyword and succeeds. `capture_pattern` cannot be a `_`.

In simple terms `P as NAME` will match with `P`, and on success it will set `NAME = <subject>`.

#### 8.6.4.3. Literal Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#literal-patterns "Link to this heading")

A literal pattern corresponds to most [literals](https://docs.python.org/3/reference/lexical_analysis.html#literals)
 in Python. Syntax:

**literal\_pattern**: [`signed_number`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-signed_number)
                 | [`signed_number`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-signed_number)
 "+" NUMBER
                 | [`signed_number`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-signed_number)
 "-" NUMBER
                 | [`strings`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-strings)
                 | "None"
                 | "True"
                 | "False"
**signed\_number**:   \["+" | "-"\] NUMBER

The rule `strings` and the token `NUMBER` are defined in the [standard Python grammar](https://docs.python.org/3/reference/grammar.html)
. Triple-quoted strings are supported. Raw strings and byte strings are supported. [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
 and [t-strings](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)
 are not supported.

The forms `signed_number '+' NUMBER` and `signed_number '-' NUMBER` are for expressing [complex numbers](https://docs.python.org/3/reference/lexical_analysis.html#imaginary)
; they require a real number on the left and an imaginary number on the right. E.g. `3 + 4j`.

In simple terms, `LITERAL` will succeed only if `<subject> == LITERAL`. For the singletons `None`, `True` and `False`, the [`is`](https://docs.python.org/3/reference/expressions.html#is)
 operator is used.

#### 8.6.4.4. Capture Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#capture-patterns "Link to this heading")

A capture pattern binds the subject value to a name. Syntax:

**capture\_pattern**: !'\_' NAME

A single underscore `_` is not a capture pattern (this is what `!'_'` expresses). It is instead treated as a [`wildcard_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-wildcard_pattern)
.

In a given pattern, a given name can only be bound once. E.g. `case x, x: ...` is invalid while `case [x] | x: ...` is allowed.

Capture patterns always succeed. The binding follows scoping rules established by the assignment expression operator in [**PEP 572**](https://peps.python.org/pep-0572/)
; the name becomes a local variable in the closest containing function scope unless there’s an applicable [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
 or [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
 statement.

In simple terms `NAME` will always succeed and it will set `NAME = <subject>`.

#### 8.6.4.5. Wildcard Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#wildcard-patterns "Link to this heading")

A wildcard pattern always succeeds (matches anything) and binds no name. Syntax:

**wildcard\_pattern**: '\_'

`_` is a [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
 within any pattern, but only within patterns. It is an identifier, as usual, even within `match` subject expressions, `guard`s, and `case` blocks.

In simple terms, `_` will always succeed.

#### 8.6.4.6. Value Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#value-patterns "Link to this heading")

A value pattern represents a named value in Python. Syntax:

**value\_pattern**: [`attr`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-attr)
**attr**:          [`name_or_attr`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-name_or_attr)
 "." NAME
**name\_or\_attr**:  [`attr`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-attr)
 | NAME

The dotted name in the pattern is looked up using standard Python [name resolution rules](https://docs.python.org/3/reference/executionmodel.html#resolve-names)
. The pattern succeeds if the value found compares equal to the subject value (using the `==` equality operator).

In simple terms `NAME1.NAME2` will succeed only if `<subject> == NAME1.NAME2`

Note

If the same value occurs multiple times in the same match statement, the interpreter may cache the first value found and reuse it rather than repeat the same lookup. This cache is strictly tied to a given execution of a given match statement.

#### 8.6.4.7. Group Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#group-patterns "Link to this heading")

A group pattern allows users to add parentheses around patterns to emphasize the intended grouping. Otherwise, it has no additional syntax. Syntax:

**group\_pattern**: "(" [`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)
 ")"

In simple terms `(P)` has the same effect as `P`.

#### 8.6.4.8. Sequence Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#sequence-patterns "Link to this heading")

A sequence pattern contains several subpatterns to be matched against sequence elements. The syntax is similar to the unpacking of a list or tuple.

**sequence\_pattern**:       "\[" \[[`maybe_sequence_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-maybe_sequence_pattern)\
\] "\]"
                        | "(" \[[`open_sequence_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-open_sequence_pattern)\
\] ")"
**open\_sequence\_pattern**:  [`maybe_star_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-maybe_star_pattern)
 "," \[[`maybe_sequence_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-maybe_sequence_pattern)\
\]
**maybe\_sequence\_pattern**: ",".[`maybe_star_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-maybe_star_pattern)
\+ ","?
**maybe\_star\_pattern**:     [`star_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-star_pattern)
 | [`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)
**star\_pattern**:           "\*" ([`capture_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-capture_pattern)
 | [`wildcard_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-wildcard_pattern)
)

There is no difference if parentheses or square brackets are used for sequence patterns (i.e. `(...)` vs `[...]` ).

Note

A single pattern enclosed in parentheses without a trailing comma (e.g. `(3 | 4)`) is a [group pattern](https://docs.python.org/3/reference/compound_stmts.html#group-patterns)
. While a single pattern enclosed in square brackets (e.g. `[3 | 4]`) is still a sequence pattern.

At most one star subpattern may be in a sequence pattern. The star subpattern may occur in any position. If no star subpattern is present, the sequence pattern is a fixed-length sequence pattern; otherwise it is a variable-length sequence pattern.

The following is the logical flow for matching a sequence pattern against a subject value:

1.  If the subject value is not a sequence [\[2\]](https://docs.python.org/3/reference/compound_stmts.html#id23)
    , the sequence pattern fails.
    
2.  If the subject value is an instance of `str`, `bytes` or `bytearray` the sequence pattern fails.
    
3.  The subsequent steps depend on whether the sequence pattern is fixed or variable-length.
    
    If the sequence pattern is fixed-length:
    
    1.  If the length of the subject sequence is not equal to the number of subpatterns, the sequence pattern fails
        
    2.  Subpatterns in the sequence pattern are matched to their corresponding items in the subject sequence from left to right. Matching stops as soon as a subpattern fails. If all subpatterns succeed in matching their corresponding item, the sequence pattern succeeds.
        
    
    Otherwise, if the sequence pattern is variable-length:
    
    1.  If the length of the subject sequence is less than the number of non-star subpatterns, the sequence pattern fails.
        
    2.  The leading non-star subpatterns are matched to their corresponding items as for fixed-length sequences.
        
    3.  If the previous step succeeds, the star subpattern matches a list formed of the remaining subject items, excluding the remaining items corresponding to non-star subpatterns following the star subpattern.
        
    4.  Remaining non-star subpatterns are matched to their corresponding subject items, as for a fixed-length sequence.
        
    
    Note
    
    The length of the subject sequence is obtained via [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
     (i.e. via the [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
     protocol). This length may be cached by the interpreter in a similar manner as [value patterns](https://docs.python.org/3/reference/compound_stmts.html#value-patterns)
    .
    

In simple terms `[P1, P2, P3,` … `, P<N>]` matches only if all the following happens:

*   check `<subject>` is a sequence
    
*   `len(subject) == <N>`
    
*   `P1` matches `<subject>[0]` (note that this match can also bind names)
    
*   `P2` matches `<subject>[1]` (note that this match can also bind names)
    
*   … and so on for the corresponding pattern/element.
    

#### 8.6.4.9. Mapping Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#mapping-patterns "Link to this heading")

A mapping pattern contains one or more key-value patterns. The syntax is similar to the construction of a dictionary. Syntax:

**mapping\_pattern**:     "{" \[[`items_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-items_pattern)\
\] "}"
**items\_pattern**:       ",".[`key_value_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-key_value_pattern)
\+ ","?
**key\_value\_pattern**:   ([`literal_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-literal_pattern)
 | [`value_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-value_pattern)
) ":" [`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)
                     | [`double_star_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-double_star_pattern)
**double\_star\_pattern**: "\*\*" [`capture_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-capture_pattern)

At most one double star pattern may be in a mapping pattern. The double star pattern must be the last subpattern in the mapping pattern.

Duplicate keys in mapping patterns are disallowed. Duplicate literal keys will raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. Two keys that otherwise have the same value will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 at runtime.

The following is the logical flow for matching a mapping pattern against a subject value:

1.  If the subject value is not a mapping [\[3\]](https://docs.python.org/3/reference/compound_stmts.html#id24)
    ,the mapping pattern fails.
    
2.  If every key given in the mapping pattern is present in the subject mapping, and the pattern for each key matches the corresponding item of the subject mapping, the mapping pattern succeeds.
    
3.  If duplicate keys are detected in the mapping pattern, the pattern is considered invalid. A [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
     is raised for duplicate literal values; or a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     for named keys of the same value.
    

Note

Key-value pairs are matched using the two-argument form of the mapping subject’s `get()` method. Matched key-value pairs must already be present in the mapping, and not created on-the-fly via [`__missing__()`](https://docs.python.org/3/reference/datamodel.html#object.__missing__ "object.__missing__")
 or [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
.

In simple terms `{KEY1: P1, KEY2: P2, ... }` matches only if all the following happens:

*   check `<subject>` is a mapping
    
*   `KEY1 in <subject>`
    
*   `P1` matches `<subject>[KEY1]`
    
*   … and so on for the corresponding KEY/pattern pair.
    

#### 8.6.4.10. Class Patterns[¶](https://docs.python.org/3/reference/compound_stmts.html#class-patterns "Link to this heading")

A class pattern represents a class and its positional and keyword arguments (if any). Syntax:

**class\_pattern**:       [`name_or_attr`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-name_or_attr)
 "(" \[[`pattern_arguments`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern_arguments)\
 ","?\] ")"
**pattern\_arguments**:   [`positional_patterns`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-positional_patterns)
 \["," [`keyword_patterns`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-keyword_patterns)\
\]
                     | [`keyword_patterns`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-keyword_patterns)
**positional\_patterns**: ",".[`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)
+
**keyword\_patterns**:    ",".[`keyword_pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-keyword_pattern)
+
**keyword\_pattern**:     NAME "=" [`pattern`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-pattern)

The same keyword should not be repeated in class patterns.

The following is the logical flow for matching a class pattern against a subject value:

1.  If `name_or_attr` is not an instance of the builtin [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
     , raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
2.  If the subject value is not an instance of `name_or_attr` (tested via [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
    ), the class pattern fails.
    
3.  If no pattern arguments are present, the pattern succeeds. Otherwise, the subsequent steps depend on whether keyword or positional argument patterns are present.
    
    For a number of built-in types (specified below), a single positional subpattern is accepted which will match the entire subject; for these types keyword patterns also work as for other types.
    
    If only keyword patterns are present, they are processed as follows, one by one:
    
    1.  The keyword is looked up as an attribute on the subject.
        
        *   If this raises an exception other than [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
            , the exception bubbles up.
            
        *   If this raises [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
            , the class pattern has failed.
            
        *   Else, the subpattern associated with the keyword pattern is matched against the subject’s attribute value. If this fails, the class pattern fails; if this succeeds, the match proceeds to the next keyword.
            
    2.  If all keyword patterns succeed, the class pattern succeeds.
        
    
    If any positional patterns are present, they are converted to keyword patterns using the [`__match_args__`](https://docs.python.org/3/reference/datamodel.html#object.__match_args__ "object.__match_args__")
     attribute on the class `name_or_attr` before matching:
    
    1.  The equivalent of `getattr(cls, "__match_args__", ())` is called.
        
        *   If this raises an exception, the exception bubbles up.
            
        *   If the returned value is not a tuple, the conversion fails and [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
             is raised.
            
        *   If there are more positional patterns than `len(cls.__match_args__)`, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
             is raised.
            
        *   Otherwise, positional pattern `i` is converted to a keyword pattern using `__match_args__[i]` as the keyword. `__match_args__[i]` must be a string; if not [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
             is raised.
            
        *   If there are duplicate keywords, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
             is raised.
            
        
        See also
        
        [Customizing positional arguments in class pattern matching](https://docs.python.org/3/reference/datamodel.html#class-pattern-matching)
        
    2.  Once all positional patterns have been converted to keyword patterns, the match proceeds as if there were only keyword patterns.
        
    
    For the following built-in types the handling of positional subpatterns is different:
    
    *   [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
        
    *   [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
        
    *   [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
        
    *   [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
        
    *   [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
        
    *   [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
        
    *   [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
        
    *   [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
        
    *   [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
        
    *   [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
        
    *   [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
        
    *   [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
        
    
    These classes accept a single positional argument, and the pattern there is matched against the whole object rather than an attribute. For example `int(0|1)` matches the value `0`, but not the value `0.0`.
    

In simple terms `CLS(P1, attr=P2)` matches only if the following happens:

*   `isinstance(<subject>, CLS)`
    
*   convert `P1` to a keyword pattern using `CLS.__match_args__`
    
*   For each keyword argument `attr=P2`:
    
    *   `hasattr(<subject>, "attr")`
        
    *   `P2` matches `<subject>.attr`
        
*   … and so on for the corresponding keyword argument/pattern pair.
    

See also

*   [**PEP 634**](https://peps.python.org/pep-0634/)
     – Structural Pattern Matching: Specification
    
*   [**PEP 636**](https://peps.python.org/pep-0636/)
     – Structural Pattern Matching: Tutorial
    

8.7. Function definitions[¶](https://docs.python.org/3/reference/compound_stmts.html#function-definitions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

A function definition defines a user-defined function object (see section [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)
):

**funcdef**:                   \[[`decorators`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators)\
\] "def" [`funcname`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-funcname)
 \[[`type_params`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-type_params)\
\] "(" \[[`parameter_list`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list)\
\] ")"
                           \["->" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
**decorators**:                [`decorator`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorator)
+
**decorator**:                 "@" [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
 NEWLINE
**parameter\_list**:            [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
 ("," [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
)\* "," "/" \["," \[[`parameter_list_no_posonly`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list_no_posonly)\
\]\]
                             | [`parameter_list_no_posonly`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list_no_posonly)
**parameter\_list\_no\_posonly**: [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
 ("," [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
)\* \["," \[[`parameter_list_starargs`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list_starargs)\
\]\]
                           | [`parameter_list_starargs`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list_starargs)
**parameter\_list\_starargs**:   "\*" [`star_parameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-star_parameter)
 ("," [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
)\* \["," \[[`parameter_star_kwargs`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_star_kwargs)\
\]\]
                           | "\*" ("," [`defparameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-defparameter)
)+ \["," \[[`parameter_star_kwargs`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_star_kwargs)\
\]\]
                           | [`parameter_star_kwargs`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_star_kwargs)
**parameter\_star\_kwargs**:     "\*\*" [`parameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter)
 \[","\]
**parameter**:                 [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \[":" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]
**star\_parameter**:            [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \[":" \["\*"\] [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]
**defparameter**:              [`parameter`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter)
 \["=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]
**funcname**:                  [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)

A function definition is an executable statement. Its execution binds the function name in the current local namespace to a function object (a wrapper around the executable code for the function). This function object contains a reference to the current global namespace as the global namespace to be used when the function is called.

The function definition does not execute the function body; this gets executed only when the function is called. [\[4\]](https://docs.python.org/3/reference/compound_stmts.html#id25)

A function definition may be wrapped by one or more [decorator](https://docs.python.org/3/glossary.html#term-decorator)
 expressions. Decorator expressions are evaluated when the function is defined, in the scope that contains the function definition. The result must be a callable, which is invoked with the function object as the only argument. The returned value is bound to the function name instead of the function object. Multiple decorators are applied in nested fashion. For example, the following code

Copy

@f1(arg)
@f2
def func(): pass

is roughly equivalent to

Copy

def func(): pass
func \= f1(arg)(f2(func))

except that the original function is not temporarily bound to the name `func`.

Changed in version 3.9: Functions may be decorated with any valid [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
. Previously, the grammar was much more restrictive; see [**PEP 614**](https://peps.python.org/pep-0614/)
 for details.

A list of [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)
 may be given in square brackets between the function’s name and the opening parenthesis for its parameter list. This indicates to static type checkers that the function is generic. At runtime, the type parameters can be retrieved from the function’s [`__type_params__`](https://docs.python.org/3/reference/datamodel.html#function.__type_params__ "function.__type_params__")
 attribute. See [Generic functions](https://docs.python.org/3/reference/compound_stmts.html#generic-functions)
 for more.

Changed in version 3.12: Type parameter lists are new in Python 3.12.

When one or more [parameters](https://docs.python.org/3/glossary.html#term-parameter)
 have the form _parameter_ `=` _expression_, the function is said to have “default parameter values.” For a parameter with a default value, the corresponding [argument](https://docs.python.org/3/glossary.html#term-argument)
 may be omitted from a call, in which case the parameter’s default value is substituted. If a parameter has a default value, all following parameters up until the “`*`” must also have a default value — this is a syntactic restriction that is not expressed by the grammar.

**Default parameter values are evaluated from left to right when the function definition is executed.** This means that the expression is evaluated once, when the function is defined, and that the same “pre-computed” value is used for each call. This is especially important to understand when a default parameter value is a mutable object, such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default parameter value is in effect modified. This is generally not what was intended. A way around this is to use `None` as the default, and explicitly test for it in the body of the function, for example:

Copy

def whats\_on\_the\_telly(penguin\=None):
    if penguin is None:
        penguin \= \[\]
    penguin.append("property of the zoo")
    return penguin

Function call semantics are described in more detail in section [Calls](https://docs.python.org/3/reference/expressions.html#calls)
. A function call always assigns values to all parameters mentioned in the parameter list, either from positional arguments, from keyword arguments, or from default values. If the form “`*identifier`” is present, it is initialized to a tuple receiving any excess positional parameters, defaulting to the empty tuple. If the form “`**identifier`” is present, it is initialized to a new ordered mapping receiving any excess keyword arguments, defaulting to a new empty mapping of the same type. Parameters after “`*`” or “`*identifier`” are keyword-only parameters and may only be passed by keyword arguments. Parameters before “`/`” are positional-only parameters and may only be passed by positional arguments.

Changed in version 3.8: The `/` function parameter syntax may be used to indicate positional-only parameters. See [**PEP 570**](https://peps.python.org/pep-0570/)
 for details.

Parameters may have an [annotation](https://docs.python.org/3/glossary.html#term-function-annotation)
 of the form “`: expression`” following the parameter name. Any parameter may have an annotation, even those of the form `*identifier` or `**identifier`. (As a special case, parameters of the form `*identifier` may have an annotation “`: *expression`”.) Functions may have “return” annotation of the form “`-> expression`” after the parameter list. These annotations can be any valid Python expression. The presence of annotations does not change the semantics of a function. See [Annotations](https://docs.python.org/3/reference/compound_stmts.html#annotations)
 for more information on annotations.

Changed in version 3.11: Parameters of the form “`*identifier`” may have an annotation “`: *expression`”. See [**PEP 646**](https://peps.python.org/pep-0646/)
.

It is also possible to create anonymous functions (functions not bound to a name), for immediate use in expressions. This uses lambda expressions, described in section [Lambdas](https://docs.python.org/3/reference/expressions.html#lambda)
. Note that the lambda expression is merely a shorthand for a simplified function definition; a function defined in a “[`def`](https://docs.python.org/3/reference/compound_stmts.html#def)
” statement can be passed around or assigned to another name just like a function defined by a lambda expression. The “`def`” form is actually more powerful since it allows the execution of multiple statements and annotations.

**Programmer’s note:** Functions are first-class objects. A “`def`” statement executed inside a function definition defines a local function that can be returned or passed around. Free variables used in the nested function can access the local variables of the function containing the def. See section [Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming)
 for details.

See also

[**PEP 3107**](https://peps.python.org/pep-3107/)
 - Function Annotations

The original specification for function annotations.

[**PEP 484**](https://peps.python.org/pep-0484/)
 - Type Hints

Definition of a standard meaning for annotations: type hints.

[**PEP 526**](https://peps.python.org/pep-0526/)
 - Syntax for Variable Annotations

Ability to type hint variable declarations, including class variables and instance variables.

[**PEP 563**](https://peps.python.org/pep-0563/)
 - Postponed Evaluation of Annotations

Support for forward references within annotations by preserving annotations in a string form at runtime instead of eager evaluation.

[**PEP 318**](https://peps.python.org/pep-0318/)
 - Decorators for Functions and Methods

Function and method decorators were introduced. Class decorators were introduced in [**PEP 3129**](https://peps.python.org/pep-3129/)
.

8.8. Class definitions[¶](https://docs.python.org/3/reference/compound_stmts.html#class-definitions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

A class definition defines a class object (see section [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)
):

**classdef**:    \[[`decorators`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators)\
\] "class" [`classname`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-classname)
 \[[`type_params`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-type_params)\
\] \[[`inheritance`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-inheritance)\
\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)
**inheritance**: "(" \[[`argument_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-argument_list)\
\] ")"
**classname**:   [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)

A class definition is an executable statement. The inheritance list usually gives a list of base classes (see [Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
 for more advanced uses), so each item in the list should evaluate to a class object which allows subclassing. Classes without an inheritance list inherit, by default, from the base class [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
; hence,

Copy

class Foo:
    pass

is equivalent to

Copy

class Foo(object):
    pass

There may be one or more base classes; see [Multiple inheritance](https://docs.python.org/3/reference/compound_stmts.html#multiple-inheritance)
 below for more information.

The class’s suite is then executed in a new execution frame (see [Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming)
), using a newly created local namespace and the original global namespace. (Usually, the suite contains mostly function definitions.) When the class’s suite finishes execution, its execution frame is discarded but its local namespace is saved. [\[5\]](https://docs.python.org/3/reference/compound_stmts.html#id26)
 A class object is then created using the inheritance list for the base classes and the saved local namespace for the attribute dictionary. The class name is bound to this class object in the original local namespace.

The order in which attributes are defined in the class body is preserved in the new class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
. Note that this is reliable only right after the class is created and only for classes that were defined using the definition syntax.

Class creation can be customized heavily using [metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
.

Classes can also be decorated: just like when decorating functions,

Copy

@f1(arg)
@f2
class Foo: pass

is roughly equivalent to

Copy

class Foo: pass
Foo \= f1(arg)(f2(Foo))

The evaluation rules for the decorator expressions are the same as for function decorators. The result is then bound to the class name.

Changed in version 3.9: Classes may be decorated with any valid [`assignment_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression)
. Previously, the grammar was much more restrictive; see [**PEP 614**](https://peps.python.org/pep-0614/)
 for details.

A list of [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)
 may be given in square brackets immediately after the class’s name. This indicates to static type checkers that the class is generic. At runtime, the type parameters can be retrieved from the class’s [`__type_params__`](https://docs.python.org/3/reference/datamodel.html#type.__type_params__ "type.__type_params__")
 attribute. See [Generic classes](https://docs.python.org/3/reference/compound_stmts.html#generic-classes)
 for more.

Changed in version 3.12: Type parameter lists are new in Python 3.12.

**Programmer’s note:** Variables defined in the class definition are class attributes; they are shared by instances. Instance attributes can be set in a method with `self.name = value`. Both class and instance attributes are accessible through the notation “`self.name`”, and an instance attribute hides a class attribute with the same name when accessed in this way. Class attributes can be used as defaults for instance attributes, but using mutable values there can lead to unexpected results. [Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)
 can be used to create instance variables with different implementation details.

See also

[**PEP 3115**](https://peps.python.org/pep-3115/)
 - Metaclasses in Python 3000

The proposal that changed the declaration of metaclasses to the current syntax, and the semantics for how classes with metaclasses are constructed.

[**PEP 3129**](https://peps.python.org/pep-3129/)
 - Class Decorators

The proposal that added class decorators. Function and method decorators were introduced in [**PEP 318**](https://peps.python.org/pep-0318/)
.

### 8.8.1. Multiple inheritance[¶](https://docs.python.org/3/reference/compound_stmts.html#multiple-inheritance "Link to this heading")

Python classes may have multiple base classes, a technique known as _multiple inheritance_. The base classes are specified in the class definition by listing them in parentheses after the class name, separated by commas. For example, the following class definition:

Copy

\>>> class A: pass
\>>> class B: pass
\>>> class C(A, B): pass

defines a class `C` that inherits from classes `A` and `B`.

The [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order)
 (MRO) is the order in which base classes are searched when looking up an attribute on a class. See [The Python 2.3 Method Resolution Order](https://docs.python.org/3/howto/mro.html#python-2-3-mro)
 for a description of how Python determines the MRO for a class.

Multiple inheritance is not always allowed. Attempting to define a class with multiple inheritance will raise an error if one of the bases does not allow subclassing, if a consistent MRO cannot be created, if no valid metaclass can be determined, or if there is an instance layout conflict. We’ll discuss each of these in turn.

First, all base classes must allow subclassing. While most classes allow subclassing, some built-in classes do not, such as [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
:

Copy

\>>> class SubBool(bool):  \# TypeError
...    pass
Traceback (most recent call last):
   ...
TypeError: type 'bool' is not an acceptable base type

In the resolved MRO of a class, the class’s bases appear in the order they were specified in the class’s bases list. Additionally, the MRO always lists a child class before any of its bases. A class definition will fail if it is impossible to resolve a consistent MRO that satisfies these rules from the list of bases provided:

Copy

\>>> class Base: pass
\>>> class Child(Base): pass
\>>> class Grandchild(Base, Child): pass  \# TypeError
Traceback (most recent call last):
   ...
TypeError: Cannot create a consistent method resolution order (MRO) for bases Base, Child

In the MRO of `Grandchild`, `Base` must appear before `Child` because it is first in the base class list, but it must also appear after `Child` because it is a parent of `Child`. This is a contradiction, so the class cannot be defined.

If some of the bases have a custom [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)
, the metaclass of the resulting class is chosen among the metaclasses of the bases and the explicitly specified metaclass of the child class. It must be a metaclass that is a subclass of all other candidate metaclasses. If no such metaclass exists among the candidates, the class cannot be created, as explained in [Determining the appropriate metaclass](https://docs.python.org/3/reference/datamodel.html#metaclass-determination)
.

Finally, the instance layouts of the bases must be compatible. This means that it must be possible to compute a _solid base_ for the class. Exactly which classes are solid bases depends on the Python implementation.

**CPython implementation detail:** In CPython, a class is a solid base if it has a nonempty [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__")
 definition. Many but not all classes defined in C are also solid bases, including most builtins (such as [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 or [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
) but excluding most concrete [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
 classes. Generally, a C class is a solid base if its underlying struct is different in size from its base class.

Every class has a solid base. [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, the base class, has itself as its solid base. If there is a single base, the child class’s solid base is that class if it is a solid base, or else the base class’s solid base. If there are multiple bases, we first find the solid base for each base class to produce a list of candidate solid bases. If there is a unique solid base that is a subclass of all others, then that class is the solid base. Otherwise, class creation fails.

Example:

Copy

\>>> class Solid1:
...    \_\_slots\_\_ \= ("solid1",)
\>>>
\>>> class Solid2:
...    \_\_slots\_\_ \= ("solid2",)
\>>>
\>>> class SolidChild(Solid1):
...    \_\_slots\_\_ \= ("solid\_child",)
\>>>
\>>> class C1:  \# solid base is \`object\`
...    pass
\>>>
\>>> \# OK: solid bases are \`Solid1\` and \`object\`, and \`Solid1\` is a subclass of \`object\`.
\>>> class C2(Solid1, C1):  \# solid base is \`Solid1\`
...    pass
\>>>
\>>> \# OK: solid bases are \`SolidChild\` and \`Solid1\`, and \`SolidChild\` is a subclass of \`Solid1\`.
\>>> class C3(SolidChild, Solid1):  \# solid base is \`SolidChild\`
...    pass
\>>>
\>>> \# Error: solid bases are \`Solid1\` and \`Solid2\`, but neither is a subclass of the other.
\>>> class C4(Solid1, Solid2):  \# error: no single solid base
...    pass
Traceback (most recent call last):
  ...
TypeError: multiple bases have instance lay-out conflict

8.9. Coroutines[¶](https://docs.python.org/3/reference/compound_stmts.html#coroutines "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Added in version 3.5.

### 8.9.1. Coroutine function definition[¶](https://docs.python.org/3/reference/compound_stmts.html#coroutine-function-definition "Link to this heading")

**async\_funcdef**: \[[`decorators`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators)\
\] "async" "def" [`funcname`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-funcname)
 "(" \[[`parameter_list`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list)\
\] ")"
               \["->" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\] ":" [`suite`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-suite)

Execution of Python coroutines can be suspended and resumed at many points (see [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
). [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expressions, [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 and [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 can only be used in the body of a coroutine function.

Functions defined with `async def` syntax are always coroutine functions, even if they do not contain `await` or `async` keywords.

It is a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 to use a `yield from` expression inside the body of a coroutine function.

An example of a coroutine function:

Copy

async def func(param1, param2):
    do\_stuff()
    await some\_coroutine()

Changed in version 3.7: `await` and `async` are now keywords; previously they were only treated as such inside the body of a coroutine function.

### 8.9.2. The `async for` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-async-for-statement "Link to this heading")

**async\_for\_stmt**: "async" [`for_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-for_stmt)

An [asynchronous iterable](https://docs.python.org/3/glossary.html#term-asynchronous-iterable)
 provides an `__aiter__` method that directly returns an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
, which can call asynchronous code in its `__anext__` method.

The `async for` statement allows convenient iteration over asynchronous iterables.

The following code:

Copy

async for TARGET in ITER:
    SUITE
else:
    SUITE2

Is semantically equivalent to:

Copy

iter \= (ITER).\_\_aiter\_\_()
running \= True

while running:
    try:
        TARGET \= await iter.\_\_anext\_\_()
    except StopAsyncIteration:
        running \= False
    else:
        SUITE
else:
    SUITE2

except that implicit [special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)
 is used for [`__aiter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aiter__ "object.__aiter__")
 and [`__anext__()`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__")
.

It is a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 to use an `async for` statement outside the body of a coroutine function.

### 8.9.3. The `async with` statement[¶](https://docs.python.org/3/reference/compound_stmts.html#the-async-with-statement "Link to this heading")

**async\_with\_stmt**: "async" [`with_stmt`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt)

An [asynchronous context manager](https://docs.python.org/3/glossary.html#term-asynchronous-context-manager)
 is a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 that is able to suspend execution in its _enter_ and _exit_ methods.

The following code:

Copy

async with EXPRESSION as TARGET:
    SUITE

is semantically equivalent to:

Copy

manager \= (EXPRESSION)
aenter \= manager.\_\_aenter\_\_
aexit \= manager.\_\_aexit\_\_
value \= await aenter()
hit\_except \= False

try:
    TARGET \= value
    SUITE
except:
    hit\_except \= True
    if not await aexit(\*sys.exc\_info()):
        raise
finally:
    if not hit\_except:
        await aexit(None, None, None)

except that implicit [special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)
 is used for [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__")
 and [`__aexit__()`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__")
.

It is a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 to use an `async with` statement outside the body of a coroutine function.

See also

[**PEP 492**](https://peps.python.org/pep-0492/)
 - Coroutines with async and await syntax

The proposal that made coroutines a proper standalone concept in Python, and added supporting syntax.

8.10. Type parameter lists[¶](https://docs.python.org/3/reference/compound_stmts.html#type-parameter-lists "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Added in version 3.12.

Changed in version 3.13: Support for default values was added (see [**PEP 696**](https://peps.python.org/pep-0696/)
).

**type\_params**:  "\[" [`type_param`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-type_param)\
 ("," [`type_param`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-type_param)\
)\* "\]"
**type\_param**:   [`typevar`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-typevar)
 | [`typevartuple`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-typevartuple)
 | [`paramspec`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-paramspec)
**typevar**:      [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 (":" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)? ("=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)?
**typevartuple**: "\*" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 ("=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)?
**paramspec**:    "\*\*" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 ("=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
)?

[Functions](https://docs.python.org/3/reference/compound_stmts.html#def)
 (including [coroutines](https://docs.python.org/3/reference/compound_stmts.html#async-def)
), [classes](https://docs.python.org/3/reference/compound_stmts.html#class)
 and [type aliases](https://docs.python.org/3/reference/simple_stmts.html#type)
 may contain a type parameter list:

Copy

def max\[T\](args: list\[T\]) \-> T:
    ...

async def amax\[T\](args: list\[T\]) \-> T:
    ...

class Bag\[T\]:
    def \_\_iter\_\_(self) \-> Iterator\[T\]:
        ...

    def add(self, arg: T) \-> None:
        ...

type ListOrSet\[T\] \= list\[T\] | set\[T\]

Semantically, this indicates that the function, class, or type alias is generic over a type variable. This information is primarily used by static type checkers, and at runtime, generic objects behave much like their non-generic counterparts.

Type parameters are declared in square brackets (`[]`) immediately after the name of the function, class, or type alias. The type parameters are accessible within the scope of the generic object, but not elsewhere. Thus, after a declaration `def func[T](): pass`, the name `T` is not available in the module scope. Below, the semantics of generic objects are described with more precision. The scope of type parameters is modeled with a special function (technically, an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
) that wraps the creation of the generic object.

Generic functions, classes, and type aliases have a [`__type_params__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__type_params__ "definition.__type_params__")
 attribute listing their type parameters.

Type parameters come in three kinds:

*   [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
    , introduced by a plain name (e.g., `T`). Semantically, this represents a single type to a type checker.
    
*   [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")
    , introduced by a name prefixed with a single asterisk (e.g., `*Ts`). Semantically, this stands for a tuple of any number of types.
    
*   [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")
    , introduced by a name prefixed with two asterisks (e.g., `**P`). Semantically, this stands for the parameters of a callable.
    

[`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
 declarations can define _bounds_ and _constraints_ with a colon (`:`) followed by an expression. A single expression after the colon indicates a bound (e.g. `T: int`). Semantically, this means that the `typing.TypeVar` can only represent types that are a subtype of this bound. A parenthesized tuple of expressions after the colon indicates a set of constraints (e.g. `T: (str, bytes)`). Each member of the tuple should be a type (again, this is not enforced at runtime). Constrained type variables can only take on one of the types in the list of constraints.

For `typing.TypeVar`s declared using the type parameter list syntax, the bound and constraints are not evaluated when the generic object is created, but only when the value is explicitly accessed through the attributes `__bound__` and `__constraints__`. To accomplish this, the bounds or constraints are evaluated in a separate [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
.

[`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")
s and [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")
s cannot have bounds or constraints.

All three flavors of type parameters can also have a _default value_, which is used when the type parameter is not explicitly provided. This is added by appending a single equals sign (`=`) followed by an expression. Like the bounds and constraints of type variables, the default value is not evaluated when the object is created, but only when the type parameter’s `__default__` attribute is accessed. To this end, the default value is evaluated in a separate [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. If no default value is specified for a type parameter, the `__default__` attribute is set to the special sentinel object [`typing.NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault")
.

The following example indicates the full set of allowed type parameter declarations:

Copy

def overly\_generic\[\
   SimpleTypeVar,\
   TypeVarWithBound: int,\
   TypeVarWithConstraints: (str, bytes),\
   TypeVarWithDefault \= int,\
   \*SimpleTypeVarTuple \= (int, float),\
   \*\*SimpleParamSpec \= (str, bytearray),\
\](
   a: SimpleTypeVar,
   b: TypeVarWithDefault,
   c: TypeVarWithBound,
   d: Callable\[SimpleParamSpec, TypeVarWithConstraints\],
   \*e: SimpleTypeVarTuple,
): ...

### 8.10.1. Generic functions[¶](https://docs.python.org/3/reference/compound_stmts.html#generic-functions "Link to this heading")

Generic functions are declared as follows:

Copy

def func\[T\](arg: T): ...

This syntax is equivalent to:

Copy

annotation\-def TYPE\_PARAMS\_OF\_func():
    T \= typing.TypeVar("T")
    def func(arg: T): ...
    func.\_\_type\_params\_\_ \= (T,)
    return func
func \= TYPE\_PARAMS\_OF\_func()

Here `annotation-def` indicates an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
, which is not actually bound to any name at runtime. (One other liberty is taken in the translation: the syntax does not go through attribute access on the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
 module, but creates an instance of [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
 directly.)

The annotations of generic functions are evaluated within the annotation scope used for declaring the type parameters, but the function’s defaults and decorators are not.

The following example illustrates the scoping rules for these cases, as well as for additional flavors of type parameters:

Copy

@decorator
def func\[T: int, \*Ts, \*\*P\](\*args: \*Ts, arg: Callable\[P, T\] \= some\_default):
    ...

Except for the [lazy evaluation](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)
 of the [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
 bound, this is equivalent to:

Copy

DEFAULT\_OF\_arg \= some\_default

annotation\-def TYPE\_PARAMS\_OF\_func():

    annotation\-def BOUND\_OF\_T():
        return int
    \# In reality, BOUND\_OF\_T() is evaluated only on demand.
    T \= typing.TypeVar("T", bound\=BOUND\_OF\_T())

    Ts \= typing.TypeVarTuple("Ts")
    P \= typing.ParamSpec("P")

    def func(\*args: \*Ts, arg: Callable\[P, T\] \= DEFAULT\_OF\_arg):
        ...

    func.\_\_type\_params\_\_ \= (T, Ts, P)
    return func
func \= decorator(TYPE\_PARAMS\_OF\_func())

The capitalized names like `DEFAULT_OF_arg` are not actually bound at runtime.

### 8.10.2. Generic classes[¶](https://docs.python.org/3/reference/compound_stmts.html#generic-classes "Link to this heading")

Generic classes are declared as follows:

Copy

class Bag\[T\]: ...

This syntax is equivalent to:

Copy

annotation\-def TYPE\_PARAMS\_OF\_Bag():
    T \= typing.TypeVar("T")
    class Bag(typing.Generic\[T\]):
        \_\_type\_params\_\_ \= (T,)
        ...
    return Bag
Bag \= TYPE\_PARAMS\_OF\_Bag()

Here again `annotation-def` (not a real keyword) indicates an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
, and the name `TYPE_PARAMS_OF_Bag` is not actually bound at runtime.

Generic classes implicitly inherit from [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")
. The base classes and keyword arguments of generic classes are evaluated within the type scope for the type parameters, and decorators are evaluated outside that scope. This is illustrated by this example:

Copy

@decorator
class Bag\[T\](Base\[T\], arg\=T): ...

This is equivalent to:

Copy

annotation\-def TYPE\_PARAMS\_OF\_Bag():
    T \= typing.TypeVar("T")
    class Bag(Base\[T\], typing.Generic\[T\], arg\=T):
        \_\_type\_params\_\_ \= (T,)
        ...
    return Bag
Bag \= decorator(TYPE\_PARAMS\_OF\_Bag())

### 8.10.3. Generic type aliases[¶](https://docs.python.org/3/reference/compound_stmts.html#generic-type-aliases "Link to this heading")

The [`type`](https://docs.python.org/3/reference/simple_stmts.html#type)
 statement can also be used to create a generic type alias:

Copy

type ListOrSet\[T\] \= list\[T\] | set\[T\]

Except for the [lazy evaluation](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)
 of the value, this is equivalent to:

Copy

annotation\-def TYPE\_PARAMS\_OF\_ListOrSet():
    T \= typing.TypeVar("T")

    annotation\-def VALUE\_OF\_ListOrSet():
        return list\[T\] | set\[T\]
    \# In reality, the value is lazily evaluated
    return typing.TypeAliasType("ListOrSet", VALUE\_OF\_ListOrSet(), type\_params\=(T,))
ListOrSet \= TYPE\_PARAMS\_OF\_ListOrSet()

Here, `annotation-def` (not a real keyword) indicates an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. The capitalized names like `TYPE_PARAMS_OF_ListOrSet` are not actually bound at runtime.

8.11. Annotations[¶](https://docs.python.org/3/reference/compound_stmts.html#annotations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Changed in version 3.14: Annotations are now lazily evaluated by default.

Variables and function parameters may carry [annotations](https://docs.python.org/3/glossary.html#term-annotation)
, created by adding a colon after the name, followed by an expression:

Copy

x: annotation \= 1
def f(param: annotation): ...

Functions may also carry a return annotation following an arrow:

Copy

def f() \-> annotation: ...

Annotations are conventionally used for [type hints](https://docs.python.org/3/glossary.html#term-type-hint)
, but this is not enforced by the language, and in general annotations may contain arbitrary expressions. The presence of annotations does not change the runtime semantics of the code, except if some mechanism is used that introspects and uses the annotations (such as [`dataclasses`](https://docs.python.org/3/library/dataclasses.html#module-dataclasses "dataclasses: Generate special methods on user-defined classes.")
 or [`@functools.singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch "functools.singledispatch")
).

By default, annotations are lazily evaluated in an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. This means that they are not evaluated when the code containing the annotation is evaluated. Instead, the interpreter saves information that can be used to evaluate the annotation later if requested. The [`annotationlib`](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "annotationlib: Functionality for introspecting annotations")
 module provides tools for evaluating annotations.

If the [future statement](https://docs.python.org/3/reference/simple_stmts.html#future)
 `from __future__ import annotations` is present, all annotations are instead stored as strings:

Copy

\>>> from \_\_future\_\_ import annotations
\>>> def f(param: annotation): ...
\>>> f.\_\_annotations\_\_
{'param': 'annotation'}

This future statement will be deprecated and removed in a future version of Python, but not before Python 3.13 reaches its end of life (see [**PEP 749**](https://peps.python.org/pep-0749/)
). When it is used, introspection tools like [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
 and [`typing.get_type_hints()`](https://docs.python.org/3/library/typing.html#typing.get_type_hints "typing.get_type_hints")
 are less likely to be able to resolve annotations at runtime.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [8\. Compound statements](https://docs.python.org/3/reference/compound_stmts.html#)
    *   [8.1. The `if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
        
    *   [8.2. The `while` statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
        
    *   [8.3. The `for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
        
    *   [8.4. The `try` statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
        *   [8.4.1. `except` clause](https://docs.python.org/3/reference/compound_stmts.html#except-clause)
            
        *   [8.4.2. `except*` clause](https://docs.python.org/3/reference/compound_stmts.html#except-star)
            
        *   [8.4.3. `else` clause](https://docs.python.org/3/reference/compound_stmts.html#else-clause)
            
        *   [8.4.4. `finally` clause](https://docs.python.org/3/reference/compound_stmts.html#finally-clause)
            
    *   [8.5. The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
        
    *   [8.6. The `match` statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
        *   [8.6.1. Overview](https://docs.python.org/3/reference/compound_stmts.html#overview)
            
        *   [8.6.2. Guards](https://docs.python.org/3/reference/compound_stmts.html#guards)
            
        *   [8.6.3. Irrefutable Case Blocks](https://docs.python.org/3/reference/compound_stmts.html#irrefutable-case-blocks)
            
        *   [8.6.4. Patterns](https://docs.python.org/3/reference/compound_stmts.html#patterns)
            *   [8.6.4.1. OR Patterns](https://docs.python.org/3/reference/compound_stmts.html#or-patterns)
                
            *   [8.6.4.2. AS Patterns](https://docs.python.org/3/reference/compound_stmts.html#as-patterns)
                
            *   [8.6.4.3. Literal Patterns](https://docs.python.org/3/reference/compound_stmts.html#literal-patterns)
                
            *   [8.6.4.4. Capture Patterns](https://docs.python.org/3/reference/compound_stmts.html#capture-patterns)
                
            *   [8.6.4.5. Wildcard Patterns](https://docs.python.org/3/reference/compound_stmts.html#wildcard-patterns)
                
            *   [8.6.4.6. Value Patterns](https://docs.python.org/3/reference/compound_stmts.html#value-patterns)
                
            *   [8.6.4.7. Group Patterns](https://docs.python.org/3/reference/compound_stmts.html#group-patterns)
                
            *   [8.6.4.8. Sequence Patterns](https://docs.python.org/3/reference/compound_stmts.html#sequence-patterns)
                
            *   [8.6.4.9. Mapping Patterns](https://docs.python.org/3/reference/compound_stmts.html#mapping-patterns)
                
            *   [8.6.4.10. Class Patterns](https://docs.python.org/3/reference/compound_stmts.html#class-patterns)
                
    *   [8.7. Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
        
    *   [8.8. Class definitions](https://docs.python.org/3/reference/compound_stmts.html#class-definitions)
        *   [8.8.1. Multiple inheritance](https://docs.python.org/3/reference/compound_stmts.html#multiple-inheritance)
            
    *   [8.9. Coroutines](https://docs.python.org/3/reference/compound_stmts.html#coroutines)
        *   [8.9.1. Coroutine function definition](https://docs.python.org/3/reference/compound_stmts.html#coroutine-function-definition)
            
        *   [8.9.2. The `async for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-async-for-statement)
            
        *   [8.9.3. The `async with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-async-with-statement)
            
    *   [8.10. Type parameter lists](https://docs.python.org/3/reference/compound_stmts.html#type-parameter-lists)
        *   [8.10.1. Generic functions](https://docs.python.org/3/reference/compound_stmts.html#generic-functions)
            
        *   [8.10.2. Generic classes](https://docs.python.org/3/reference/compound_stmts.html#generic-classes)
            
        *   [8.10.3. Generic type aliases](https://docs.python.org/3/reference/compound_stmts.html#generic-type-aliases)
            
    *   [8.11. Annotations](https://docs.python.org/3/reference/compound_stmts.html#annotations)
        

#### Previous topic

[7\. Simple statements](https://docs.python.org/3/reference/simple_stmts.html "previous chapter")

#### Next topic

[9\. Top-level components](https://docs.python.org/3/reference/toplevel_components.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=8.+Compound+statements&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fcompound_stmts.html&pagesource=reference%2Fcompound_stmts.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/compound_stmts.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/toplevel_components.html "9. Top-level components")
     |
*   [previous](https://docs.python.org/3/reference/simple_stmts.html "7. Simple statements")
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
*   [8\. Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
    
*    
    
    |
*   Theme Auto Light Dark |