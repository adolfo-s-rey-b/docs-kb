### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/compound_stmts.html "8. Compound statements")
     |
*   [previous](https://docs.python.org/3/reference/expressions.html "6. Expressions")
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
*   [7\. Simple statements](https://docs.python.org/3/reference/simple_stmts.html)
    
*    
    
    |
*   Theme Auto Light Dark |

7\. Simple statements[¶](https://docs.python.org/3/reference/simple_stmts.html#simple-statements "Link to this heading")

=========================================================================================================================

A simple statement is comprised within a single logical line. Several simple statements may occur on a single line separated by semicolons. The syntax for simple statements is:

**simple\_stmt**: [`expression_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-expression_stmt)
             | [`assert_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt)
             | [`assignment_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assignment_stmt)
             | [`augmented_assignment_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augmented_assignment_stmt)
             | [`annotated_assignment_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-annotated_assignment_stmt)
             | [`pass_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-pass_stmt)
             | [`del_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-del_stmt)
             | [`return_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-return_stmt)
             | [`yield_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-yield_stmt)
             | [`raise_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-raise_stmt)
             | [`break_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-break_stmt)
             | [`continue_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-continue_stmt)
             | [`import_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-import_stmt)
             | [`future_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-future_stmt)
             | [`global_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-global_stmt)
             | [`nonlocal_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-nonlocal_stmt)
             | [`type_stmt`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-type_stmt)

7.1. Expression statements[¶](https://docs.python.org/3/reference/simple_stmts.html#expression-statements "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Expression statements are used (mostly interactively) to compute and write a value, or (usually) to call a procedure (a function that returns no meaningful result; in Python, procedures return the value `None`). Other uses of expression statements are allowed and occasionally useful. The syntax for an expression statement is:

**expression\_stmt**: [`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)

An expression statement evaluates the expression list (which may be a single expression).

In interactive mode, if the value is not `None`, it is converted to a string using the built-in [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 function and the resulting string is written to standard output on a line by itself (except if the result is `None`, so that procedure calls do not cause any output.)

7.2. Assignment statements[¶](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Assignment statements are used to (re)bind names to values and to modify attributes or items of mutable objects:

**assignment\_stmt**: ([`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)
 "=")+ ([`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)
 | [`yield_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_expression)
)
**target\_list**:     [`target`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target)
 ("," [`target`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target)
)\* \[","\]
**target**:          [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
                 | "(" \[[`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)\
\] ")"
                 | "\[" \[[`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)\
\] "\]"
                 | [`attributeref`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-attributeref)
                 | [`subscription`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-subscription)
                 | "\*" [`target`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target)

(See section [Primaries](https://docs.python.org/3/reference/expressions.html#primaries)
 for the syntax definitions for _attributeref_ and _subscription_.)

An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

Assignment is defined recursively depending on the form of the target (list). When a target is part of a mutable object (an attribute reference or subscription), the mutable object must ultimately perform the assignment and decide about its validity, and may raise an exception if the assignment is unacceptable. The rules observed by various types and the exceptions raised are given with the definition of the object types (see section [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)
).

Assignment of an object to a target list, optionally enclosed in parentheses or square brackets, is recursively defined as follows.

*   If the target list is a single target with no trailing comma, optionally in parentheses, the object is assigned to that target.
    
*   Else:
    
    *   If the target list contains one target prefixed with an asterisk, called a “starred” target: The object must be an iterable with at least as many items as there are targets in the target list, minus one. The first items of the iterable are assigned, from left to right, to the targets before the starred target. The final items of the iterable are assigned to the targets after the starred target. A list of the remaining items in the iterable is then assigned to the starred target (the list can be empty).
        
    *   Else: The object must be an iterable with the same number of items as there are targets in the target list, and the items are assigned, from left to right, to the corresponding targets.
        

Assignment of an object to a single target is recursively defined as follows.

*   If the target is an identifier (name):
    
    *   If the name does not occur in a [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
         or [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
         statement in the current code block: the name is bound to the object in the current local namespace.
        
    *   Otherwise: the name is bound to the object in the global namespace or the outer namespace determined by [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
        , respectively.
        
    
    The name is rebound if it was already bound. This may cause the reference count for the object previously bound to the name to reach zero, causing the object to be deallocated and its destructor (if it has one) to be called.
    
*   If the target is an attribute reference: The primary expression in the reference is evaluated. It should yield an object with assignable attributes; if this is not the case, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     is raised. That object is then asked to assign the assigned object to the given attribute; if it cannot perform the assignment, it raises an exception (usually but not necessarily [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    ).
    
    Note: If the object is a class instance and the attribute reference occurs on both sides of the assignment operator, the right-hand side expression, `a.x` can access either an instance attribute or (if no instance attribute exists) a class attribute. The left-hand side target `a.x` is always set as an instance attribute, creating it if necessary. Thus, the two occurrences of `a.x` do not necessarily refer to the same attribute: if the right-hand side expression refers to a class attribute, the left-hand side creates a new instance attribute as the target of the assignment:
    
    Copy
    
    class Cls:
        x \= 3             \# class variable
    inst \= Cls()
    inst.x \= inst.x + 1   \# writes inst.x as 4 leaving Cls.x as 3
    
    This description does not necessarily apply to descriptor attributes, such as properties created with [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
    .
    
*   If the target is a subscription: The primary expression in the reference is evaluated. Next, the subscript expression is evaluated. Then, the primary’s [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
     method is called with two arguments: the subscript and the assigned object.
    
    Typically, [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
     is defined on mutable sequence objects (such as lists) and mapping objects (such as dictionaries), and behaves as follows.
    
    If the primary is a mutable sequence object (such as a list), the subscript must yield an integer. If it is negative, the sequence’s length is added to it. The resulting value must be a nonnegative integer less than the sequence’s length, and the sequence is asked to assign the assigned object to its item with that index. If the index is out of range, [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
     is raised (assignment to a subscripted sequence cannot add new items to a list).
    
    If the primary is a mapping object (such as a dictionary), the subscript must have a type compatible with the mapping’s key type, and the mapping is then asked to create a key/value pair which maps the subscript to the assigned object. This can either replace an existing key/value pair with the same key value, or insert a new key/value pair (if no key with the same value existed).
    
    If the target is a slicing: The primary expression should evaluate to a mutable sequence object (such as a list). The assigned object should be [iterable](https://docs.python.org/3/glossary.html#term-iterable)
    . The slicing’s lower and upper bounds should be integers; if they are `None` (or not present), the defaults are zero and the sequence’s length. If either bound is negative, the sequence’s length is added to it. The resulting bounds are clipped to lie between zero and the sequence’s length, inclusive. Finally, the sequence object is asked to replace the slice with the items of the assigned sequence. The length of the slice may be different from the length of the assigned sequence, thus changing the length of the target sequence, if the target sequence allows it.
    

Although the definition of assignment implies that overlaps between the left-hand side and the right-hand side are ‘simultaneous’ (for example `a, b = b, a` swaps two variables), overlaps _within_ the collection of assigned-to variables occur left-to-right, sometimes resulting in confusion. For instance, the following program prints `[0, 2]`:

Copy

x \= \[0, 1\]
i \= 0
i, x\[i\] \= 1, 2         \# i is updated, then x\[i\] is updated
print(x)

See also

[**PEP 3132**](https://peps.python.org/pep-3132/)
 - Extended Iterable Unpacking

The specification for the `*target` feature.

### 7.2.1. Augmented assignment statements[¶](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements "Link to this heading")

Augmented assignment is the combination, in a single statement, of a binary operation and an assignment statement:

**augmented\_assignment\_stmt**: [`augtarget`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augtarget)
 [`augop`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augop)
 ([`expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression_list)
 | [`yield_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_expression)
)
**augtarget**:                 [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 | [`attributeref`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-attributeref)
 | [`subscription`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-subscription)
**augop**:                     "+=" | "-=" | "\*=" | "@=" | "/=" | "//=" | "%=" | "\*\*="
                           | ">>=" | "<<=" | "&=" | "^=" | "|="

(See section [Primaries](https://docs.python.org/3/reference/expressions.html#primaries)
 for the syntax definitions of the last three symbols.)

An augmented assignment evaluates the target (which, unlike normal assignment statements, cannot be an unpacking) and the expression list, performs the binary operation specific to the type of assignment on the two operands, and assigns the result to the original target. The target is only evaluated once.

An augmented assignment statement like `x += 1` can be rewritten as `x = x + 1` to achieve a similar, but not exactly equal effect. In the augmented version, `x` is only evaluated once. Also, when possible, the actual operation is performed _in-place_, meaning that rather than creating a new object and assigning that to the target, the old object is modified instead.

Unlike normal assignments, augmented assignments evaluate the left-hand side _before_ evaluating the right-hand side. For example, `a[i] += f(x)` first looks-up `a[i]`, then it evaluates `f(x)` and performs the addition, and lastly, it writes the result back to `a[i]`.

With the exception of assigning to tuples and multiple targets in a single statement, the assignment done by augmented assignment statements is handled the same way as normal assignments. Similarly, with the exception of the possible _in-place_ behavior, the binary operation performed by augmented assignment is the same as the normal binary operations.

For targets which are attribute references, the same [caveat about class and instance attributes](https://docs.python.org/3/reference/simple_stmts.html#attr-target-note)
 applies as for regular assignments.

### 7.2.2. Annotated assignment statements[¶](https://docs.python.org/3/reference/simple_stmts.html#annotated-assignment-statements "Link to this heading")

[Annotation](https://docs.python.org/3/glossary.html#term-variable-annotation)
 assignment is the combination, in a single statement, of a variable or attribute annotation and an optional assignment statement:

**annotated\_assignment\_stmt**: [`augtarget`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augtarget)
 ":" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
                           \["=" ([`starred_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-starred_expression)\
 | [`yield_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_expression)\
)\]

The difference from normal [Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment)
 is that only a single target is allowed.

The assignment target is considered “simple” if it consists of a single name that is not enclosed in parentheses. For simple assignment targets, if in class or module scope, the annotations are gathered in a lazily evaluated [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. The annotations can be evaluated using the [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__")
 attribute of a class or module, or using the facilities in the [`annotationlib`](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "annotationlib: Functionality for introspecting annotations")
 module.

If the assignment target is not simple (an attribute, subscript node, or parenthesized name), the annotation is never evaluated.

If a name is annotated in a function scope, then this name is local for that scope. Annotations are never evaluated and stored in function scopes.

If the right hand side is present, an annotated assignment performs the actual assignment as if there was no annotation present. If the right hand side is not present for an expression target, then the interpreter evaluates the target except for the last [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
 or [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__")
 call.

See also

[**PEP 526**](https://peps.python.org/pep-0526/)
 - Syntax for Variable Annotations

The proposal that added syntax for annotating the types of variables (including class variables and instance variables), instead of expressing them through comments.

[**PEP 484**](https://peps.python.org/pep-0484/)
 - Type hints

The proposal that added the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
 module to provide a standard syntax for type annotations that can be used in static analysis tools and IDEs.

Changed in version 3.8: Now annotated assignments allow the same expressions in the right hand side as regular assignments. Previously, some expressions (like un-parenthesized tuple expressions) caused a syntax error.

Changed in version 3.14: Annotations are now lazily evaluated in a separate [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. If the assignment target is not simple, annotations are never evaluated.

7.3. The `assert` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Assert statements are a convenient way to insert debugging assertions into a program:

**assert\_stmt**: "assert" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)
 \["," [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]

The simple form, `assert expression`, is equivalent to

Copy

if \_\_debug\_\_:
    if not expression: raise AssertionError

The extended form, `assert expression1, expression2`, is equivalent to

Copy

if \_\_debug\_\_:
    if not expression1: raise AssertionError(expression2)

These equivalences assume that [`__debug__`](https://docs.python.org/3/builtins/constants.html#debug__ "__debug__")
 and [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
 refer to the built-in variables with those names. In the current implementation, the built-in variable `__debug__` is `True` under normal circumstances, `False` when optimization is requested (command line option [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
). The current code generator emits no code for an [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert)
 statement when optimization is requested at compile time. Note that it is unnecessary to include the source code for the expression that failed in the error message; it will be displayed as part of the stack trace.

Assignments to [`__debug__`](https://docs.python.org/3/builtins/constants.html#debug__ "__debug__")
 are illegal. The value for the built-in variable is determined when the interpreter starts.

7.4. The `pass` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

**pass\_stmt**: "pass"

[`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass)
 is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed, for example:

Copy

def f(arg): pass    \# a function that does nothing (yet)

class C: pass       \# a class with no methods (yet)

7.5. The `del` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-del-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

**del\_stmt**: "del" [`target_list`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-target_list)

Deletion is recursively defined very similar to the way assignment is defined. Rather than spelling it out in full details, here are some hints.

Deletion of a target list recursively deletes each target, from left to right.

Deletion of a name removes the binding of that name from the local or global namespace, depending on whether the name occurs in a [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
 statement in the same code block. Trying to delete an unbound name raises a [`NameError`](https://docs.python.org/3/builtins/exceptions.html#NameError "NameError")
 exception.

Deletion of attribute references and subscriptions is passed to the primary object involved; deletion of a slicing is in general equivalent to assignment of an empty slice of the right type (but even this is determined by the sliced object).

Changed in version 3.2: Previously it was illegal to delete a name from the local namespace if it occurs as a free variable in a nested block.

7.6. The `return` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

**return\_stmt**: "return" \[[`expression_list`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression_list)\
\]

[`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 may only occur syntactically nested in a function definition, not within a nested class definition.

If an expression list is present, it is evaluated, else `None` is substituted.

[`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 leaves the current function call with the expression list (or `None`) as return value.

When [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 passes control out of a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement with a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause, that `finally` clause is executed before really leaving the function.

In a generator function, the [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement indicates that the generator is done and will cause [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 to be raised. The returned value (if any) is used as an argument to construct `StopIteration` and becomes the [`StopIteration.value`](https://docs.python.org/3/builtins/exceptions.html#StopIteration.value "StopIteration.value")
 attribute.

In an asynchronous generator function, an empty [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement indicates that the asynchronous generator is done and will cause [`StopAsyncIteration`](https://docs.python.org/3/builtins/exceptions.html#StopAsyncIteration "StopAsyncIteration")
 to be raised. A non-empty `return` statement is a syntax error in an asynchronous generator function.

7.7. The `yield` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

**yield\_stmt**: [`yield_expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-yield_expression)

A [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 statement is semantically equivalent to a [yield expression](https://docs.python.org/3/reference/expressions.html#yieldexpr)
. The `yield` statement can be used to omit the parentheses that would otherwise be required in the equivalent yield expression statement. For example, the yield statements

Copy

yield <expr\>
yield from <expr\>

are equivalent to the yield expression statements

Copy

(yield <expr\>)
(yield from <expr\>)

Yield expressions and statements are only used when defining a [generator](https://docs.python.org/3/glossary.html#term-generator)
 function, and are only used in the body of the generator function. Using [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 in a function definition is sufficient to cause that definition to create a generator function instead of a normal function.

For full details of [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 semantics, refer to the [Yield expressions](https://docs.python.org/3/reference/expressions.html#yieldexpr)
 section.

7.8. The `raise` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

**raise\_stmt**: "raise" \[[`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
 \["from" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)\
\]\]

If no expressions are present, [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise)
 re-raises the exception that is currently being handled, which is also known as the _active exception_. If there isn’t currently an active exception, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 exception is raised indicating that this is an error.

Otherwise, [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise)
 evaluates the first expression as the exception object. It must be either a subclass or an instance of [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
. If it is a class, the exception instance will be obtained when needed by instantiating the class with no arguments.

The _type_ of the exception is the exception instance’s class, the _value_ is the instance itself.

A traceback object is normally created automatically when an exception is raised and attached to it as the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
 attribute. You can create an exception and set your own traceback in one step using the [`with_traceback()`](https://docs.python.org/3/builtins/exceptions.html#BaseException.with_traceback "BaseException.with_traceback")
 exception method (which returns the same exception instance, with its traceback set to its argument), like so:

Copy

raise Exception("foo occurred").with\_traceback(tracebackobj)

The `from` clause is used for exception chaining: if given, the second _expression_ must be another exception class or instance. If the second expression is an exception instance, it will be attached to the raised exception as the [`__cause__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__cause__ "BaseException.__cause__")
 attribute (which is writable). If the expression is an exception class, the class will be instantiated and the resulting exception instance will be attached to the raised exception as the `__cause__` attribute. If the raised exception is not handled, both exceptions will be printed:

Copy

\>>> try:
...     print(1 / 0)
... except Exception as exc:
...     raise RuntimeError("Something bad happened") from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(1 / 0)
          ~~^~~
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("Something bad happened") from exc
RuntimeError: Something bad happened

A similar mechanism works implicitly if a new exception is raised when an exception is already being handled. An exception may be handled when an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 or [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause, or a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, is used. The previous exception is then attached as the new exception’s [`__context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__context__ "BaseException.__context__")
 attribute:

Copy

\>>> try:
...     print(1 / 0)
... except:
...     raise RuntimeError("Something bad happened")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(1 / 0)
          ~~^~~
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("Something bad happened")
RuntimeError: Something bad happened

Exception chaining can be explicitly suppressed by specifying [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 in the `from` clause:

Copy

\>>> try:
...     print(1 / 0)
... except:
...     raise RuntimeError("Something bad happened") from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened

Additional information on exceptions can be found in section [Exceptions](https://docs.python.org/3/reference/executionmodel.html#exceptions)
, and information about handling exceptions is in section [The try statement](https://docs.python.org/3/reference/compound_stmts.html#try)
.

Changed in version 3.3: [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 is now permitted as `Y` in `raise X from Y`.

Added the [`__suppress_context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__suppress_context__ "BaseException.__suppress_context__")
 attribute to suppress automatic display of the exception context.

Changed in version 3.11: If the traceback of the active exception is modified in an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 clause, a subsequent `raise` statement re-raises the exception with the modified traceback. Previously, the exception was re-raised with the traceback it had when it was caught.

7.9. The `break` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

**break\_stmt**: "break"

[`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 may only occur syntactically nested in a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)
 loop, but not nested in a function or class definition within that loop.

It terminates the nearest enclosing loop, skipping the optional `else` clause if the loop has one.

If a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 loop is terminated by [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
, the loop control target keeps its current value.

When [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 passes control out of a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement with a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause, that `finally` clause is executed before really leaving the loop.

7.10. The `continue` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

**continue\_stmt**: "continue"

[`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 may only occur syntactically nested in a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)
 loop, but not nested in a function or class definition within that loop. It continues with the next cycle of the nearest enclosing loop.

When [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
 passes control out of a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement with a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause, that `finally` clause is executed before really starting the next loop cycle.

7.11. The `import` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

**import\_stmt**:     \["lazy"\] "import" [`module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-module)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\] ("," [`module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-module)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\])\*
                 | \["lazy"\] "from" [`relative_module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-relative_module)
 "import" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\]
                 ("," [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\])\*
                 | \["lazy"\] "from" [`relative_module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-relative_module)
 "import" "(" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\]
                 ("," [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\])\* \[","\] ")"
                 | "from" [`relative_module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-relative_module)
 "import" "\*"
**module**:          ([`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 ".")\* [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
**relative\_module**: "."\* [`module`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-module)
 | "."+

The basic import statement (no [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
 clause) is executed in two steps:

1.  find a module, loading and initializing it if necessary
    
2.  define a name or names in the current namespace for the scope where the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
     statement occurs, just as an assignment statement would (including [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
     and [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
     semantics).
    

When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for each clause, just as though the clauses had been separated out into individual import statements.

The details of the first step, finding and loading modules, are described in greater detail in the section on the [import system](https://docs.python.org/3/reference/import.html#importsystem)
, which also describes the various types of packages and modules that can be imported, as well as all the hooks that can be used to customize the import system. Note that failures in this step may indicate either that the module could not be located, _or_ that an error occurred while initializing the module, which includes execution of the module’s code.

If the requested module is retrieved successfully, it will be made available in the local namespace in one of three ways:

*   If the module name is followed by `as`, then the name following `as` is bound directly to the imported module.
    
*   If no other name is specified, and the module being imported is a top level module, the module’s name is bound in the local namespace as a reference to the imported module
    
*   If the module being imported is _not_ a top level module, then the name of the top level package that contains the module is bound in the local namespace as a reference to the top level package. The imported module must be accessed using its full qualified name rather than directly
    

The [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
 form uses a slightly more complex process:

1.  find the module specified in the [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
     clause, loading and initializing it if necessary;
    
2.  for each of the identifiers specified in the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
     clauses:
    
    1.  check if the imported module has an attribute by that name
        
    2.  if not, attempt to import a submodule with that name and then check the imported module again for that attribute
        
    3.  if the attribute is not found, [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
         is raised.
        
    4.  otherwise, a reference to that value is stored in the current namespace, using the name in the `as` clause if it is present, otherwise using the attribute name
        

Examples:

Copy

import foo                 \# foo imported and bound locally
import foo.bar.baz         \# foo, foo.bar, and foo.bar.baz imported, foo bound locally
import foo.bar.baz as fbb  \# foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as fbb
from foo.bar import baz    \# foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as baz
from foo import attr       \# foo imported and foo.attr bound as attr

If the list of identifiers is replaced by a star (`'*'`), all public names defined in the module are bound in the local namespace for the scope where the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statement occurs.

The _public names_ defined by a module are determined by checking the module’s namespace for a variable named `__all__`; if defined, it must be a sequence of strings which are names defined or imported by that module. Names containing non-ASCII characters must be in the [normalization form](https://www.unicode.org/reports/tr15/#Norm_Forms)
 NFKC; see [Non-ASCII characters in names](https://docs.python.org/3/reference/lexical_analysis.html#lexical-names-nonascii)
 for details. The names given in `__all__` are all considered public and are required to exist. If `__all__` is not defined, the set of public names includes all names found in the module’s namespace which do not begin with an underscore character (`'_'`). `__all__` should contain the entire public API. It is intended to avoid accidentally exporting items that are not part of the API (such as library modules which were imported and used within the module).

The wild card form of import — `from module import *` — is only allowed at the module level. Attempting to use it in class or function definitions will raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
.

When specifying what module to import you do not have to specify the absolute name of the module. When a module or package is contained within another package it is possible to make a relative import within the same top package without having to mention the package name. By using leading dots in the specified module or package after [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
 you can specify how high to traverse up the current package hierarchy without specifying exact names. One leading dot means the current package where the module making the import exists. Two dots means up one package level. Three dots is up two levels, etc. So if you execute `from . import mod` from a module in the `pkg` package then you will end up importing `pkg.mod`. If you execute `from ..subpkg2 import mod` from within `pkg.subpkg1` you will import `pkg.subpkg2.mod`. The specification for relative imports is contained in the [Package Relative Imports](https://docs.python.org/3/reference/import.html#relativeimports)
 section.

[`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")
 is provided to support applications that determine dynamically the modules to be loaded.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `import` with arguments `module`, `filename`, `sys.path`, `sys.meta_path`, `sys.path_hooks`.

### 7.11.1. Lazy imports[¶](https://docs.python.org/3/reference/simple_stmts.html#lazy "Link to this heading")

The [`lazy`](https://docs.python.org/3/reference/simple_stmts.html#lazy)
 keyword is a [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
 that only has special meaning when it appears immediately before an [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 or [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
 statement. When an import statement is preceded by the `lazy` keyword, the import becomes _lazy_: the module is not loaded immediately at the import statement. Instead, a lazy proxy object is created and bound to the name. The actual module is loaded on first use of that name.

Lazy imports are only permitted at module scope. Using [`lazy`](https://docs.python.org/3/reference/simple_stmts.html#lazy)
 inside a function, class body, or [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
/[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
/[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 block raises a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. Star imports cannot be lazy (`lazy from module import *` is a syntax error), and [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
 cannot be lazy.

When using `lazy from ... import`, each imported name is bound to a lazy proxy object. The first access to any of these names triggers loading of the entire module and resolves only that specific name to its actual value. Other names remain as lazy proxies until they are accessed.

Example:

Copy

lazy import json
import sys

print('json' in sys.modules)  \# False - json module not yet loaded

\# First use triggers loading
result \= json.dumps({"hello": "world"})

print('json' in sys.modules)  \# True - now loaded

If an error occurs during module loading (such as [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 or [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
), it is raised at the point where the lazy import is first used, not at the import statement itself.

See [**PEP 810**](https://peps.python.org/pep-0810/)
 for the full specification of lazy imports.

Added in version 3.15.

#### 7.11.1.1. Compatibility via `__lazy_modules__`[¶](https://docs.python.org/3/reference/simple_stmts.html#compatibility-via-lazy-modules "Link to this heading")

As an alternative to using the [`lazy`](https://docs.python.org/3/reference/simple_stmts.html#lazy)
 keyword, a module can opt into lazy loading for specific imports by defining a module-level [`__lazy_modules__`](https://docs.python.org/3/reference/datamodel.html#module.__lazy_modules__ "module.__lazy_modules__")
 variable. When present, it must be a container of fully qualified module name strings. Any regular (non-`lazy`) [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statement at module scope whose target appears in `__lazy_modules__` is treated as a lazy import, exactly as if the `lazy` keyword had been used.

This provides a way to enable lazy loading for specific dependencies without changing individual `import` statements. This is useful when supporting Python versions older than 3.15 while using lazy imports in 3.15+:

Copy

\_\_lazy\_modules\_\_ \= \["json", "pathlib"\]

import json     \# loaded lazily (name is in \_\_lazy\_modules\_\_)
import os       \# loaded eagerly (name not in \_\_lazy\_modules\_\_)

import pathlib  \# loaded lazily

Relative imports are resolved to their absolute name before the lookup, so `__lazy_modules__` must always contain fully qualified module names.

For `from`\-style imports, the relevant name is the module following `from`, not the names of its members:

Copy

\# In mypackage/mymodule.py
\_\_lazy\_modules\_\_ \= \["mypackage", "mypackage.sub.utils"\]

from . import helper         \# loaded lazily: . resolves to mypackage
from .sub.utils import func  \# loaded lazily: .sub.utils resolves to mypackage.sub.utils
import json                  \# loaded eagerly (not in \_\_lazy\_modules\_\_)

Imports inside functions, class bodies, or [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
/[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
/[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 blocks are always eager, regardless of `__lazy_modules__`.

Added in version 3.15.

### 7.11.2. Future statements[¶](https://docs.python.org/3/reference/simple_stmts.html#future-statements "Link to this heading")

A _future statement_ is a directive to the compiler that a particular module should be compiled using syntax or semantics that will be available in a specified future release of Python where the feature becomes standard.

The future statement is intended to ease migration to future versions of Python that introduce incompatible changes to the language. It allows use of the new features on a per-module basis before the release in which the feature becomes standard.

**future\_stmt**: "from" "\_\_future\_\_" "import" [`feature`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-feature)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\]
             ("," [`feature`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-feature)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\])\*
             | "from" "\_\_future\_\_" "import" "(" [`feature`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-feature)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\]
             ("," [`feature`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-feature)
 \["as" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)\
\])\* \[","\] ")"
**feature**:     [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)

A future statement must appear near the top of the module. The only lines that can appear before a future statement are:

*   the module docstring (if any),
    
*   comments,
    
*   blank lines, and
    
*   other future statements.
    

The only feature that requires using the future statement is `annotations` (see [**PEP 563**](https://peps.python.org/pep-0563/)
).

All historical features enabled by the future statement are still recognized by Python 3. The list includes `absolute_import`, `division`, `generators`, `generator_stop`, `unicode_literals`, `print_function`, `nested_scopes` and `with_statement`. They are all redundant because they are always enabled, and only kept for backwards compatibility.

A future statement is recognized and treated specially at compile time: Changes to the semantics of core constructs are often implemented by generating different code. It may even be the case that a new feature introduces new incompatible syntax (such as a new reserved word), in which case the compiler may need to parse the module differently. Such decisions cannot be pushed off until runtime.

For any given release, the compiler knows which feature names have been defined, and raises a compile-time error if a future statement contains a feature not known to it.

The direct runtime semantics are the same as for any import statement: there is a standard module [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
, described later, and it will be imported in the usual way at the time the future statement is executed.

The interesting runtime semantics depend on the specific feature enabled by the future statement.

Note that there is nothing special about the statement:

Copy

import \_\_future\_\_ \[as name\]

That is not a future statement; it’s an ordinary import statement with no special semantics or syntax restrictions.

Code compiled by calls to the built-in functions [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 and [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 that occur in a module `M` containing a future statement will, by default, use the new syntax or semantics associated with the future statement. This can be controlled by optional arguments to `compile()` — see the documentation of that function for details.

A future statement typed at an interactive interpreter prompt will take effect for the rest of the interpreter session. If an interpreter is started with the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 option, is passed a script name to execute, and the script includes a future statement, it will be in effect in the interactive session started after the script is executed.

See also

[**PEP 236**](https://peps.python.org/pep-0236/)
 - Back to the \_\_future\_\_

The original proposal for the \_\_future\_\_ mechanism.

7.12. The `global` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

**global\_stmt**: "global" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 ("," [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
)\*

The [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
 statement causes the listed identifiers to be interpreted as globals. It would be impossible to assign to a global variable without `global`, although free variables may refer to globals without being declared global.

The `global` statement applies to the entire current scope (module, function body or class definition). A [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 is raised if a variable is used or assigned to prior to its global declaration in the scope.

At the module level, all variables are global, so a `global` statement has no effect. However, variables must still not be used or assigned to prior to their `global` declaration. This requirement is relaxed in the interactive prompt ([REPL](https://docs.python.org/3/glossary.html#term-REPL)
).

**Programmer’s note:** [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
 is a directive to the parser. It applies only to code parsed at the same time as the `global` statement. In particular, a `global` statement contained in a string or code object supplied to the built-in [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 function does not affect the code block _containing_ the function call, and code contained in such a string is unaffected by `global` statements in the code containing the function call. The same applies to the [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 and [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 functions.

7.13. The `nonlocal` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

**nonlocal\_stmt**: "nonlocal" [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 ("," [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
)\*

When the definition of a function or class is nested (enclosed) within the definitions of other functions, its nonlocal scopes are the local scopes of the enclosing functions. The [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
 statement causes the listed identifiers to refer to names previously bound in nonlocal scopes. It allows encapsulated code to rebind such nonlocal identifiers. If a name is bound in more than one nonlocal scope, the nearest binding is used. If a name is not bound in any nonlocal scope, or if there is no nonlocal scope, a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 is raised.

The [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
 statement applies to the entire scope of a function or class body. A [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 is raised if a variable is used or assigned to prior to its nonlocal declaration in the scope.

See also

[**PEP 3104**](https://peps.python.org/pep-3104/)
 - Access to Names in Outer Scopes

The specification for the [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
 statement.

**Programmer’s note:** [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
 is a directive to the parser and applies only to code parsed along with it. See the note for the [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
 statement.

7.14. The `type` statement[¶](https://docs.python.org/3/reference/simple_stmts.html#the-type-statement "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

**type\_stmt**: 'type' [`identifier`](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
 \[[`type_params`](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-type_params)\
\] "=" [`expression`](https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression)

The `type` statement declares a type alias, which is an instance of [`typing.TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType")
.

For example, the following statement creates a type alias:

Copy

type Point \= tuple\[float, float\]

This code is roughly equivalent to:

Copy

annotation\-def VALUE\_OF\_Point():
    return tuple\[float, float\]
Point \= typing.TypeAliasType("Point", VALUE\_OF\_Point())

`annotation-def` indicates an [annotation scope](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
, which behaves mostly like a function, but with several small differences.

The value of the type alias is evaluated in the annotation scope. It is not evaluated when the type alias is created, but only when the value is accessed through the type alias’s `__value__` attribute (see [Lazy evaluation](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)
). This allows the type alias to refer to names that are not yet defined.

Type aliases may be made generic by adding a [type parameter list](https://docs.python.org/3/reference/compound_stmts.html#type-params)
 after the name. See [Generic type aliases](https://docs.python.org/3/reference/compound_stmts.html#generic-type-aliases)
 for more.

`type` is a [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
.

Added in version 3.12.

See also

[**PEP 695**](https://peps.python.org/pep-0695/)
 - Type Parameter Syntax

Introduced the `type` statement and syntax for generic classes and functions.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [7\. Simple statements](https://docs.python.org/3/reference/simple_stmts.html#)
    *   [7.1. Expression statements](https://docs.python.org/3/reference/simple_stmts.html#expression-statements)
        
    *   [7.2. Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
        *   [7.2.1. Augmented assignment statements](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements)
            
        *   [7.2.2. Annotated assignment statements](https://docs.python.org/3/reference/simple_stmts.html#annotated-assignment-statements)
            
    *   [7.3. The `assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
        
    *   [7.4. The `pass` statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement)
        
    *   [7.5. The `del` statement](https://docs.python.org/3/reference/simple_stmts.html#the-del-statement)
        
    *   [7.6. The `return` statement](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement)
        
    *   [7.7. The `yield` statement](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
        
    *   [7.8. The `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
        
    *   [7.9. The `break` statement](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)
        
    *   [7.10. The `continue` statement](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)
        
    *   [7.11. The `import` statement](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
        *   [7.11.1. Lazy imports](https://docs.python.org/3/reference/simple_stmts.html#lazy)
            *   [7.11.1.1. Compatibility via `__lazy_modules__`](https://docs.python.org/3/reference/simple_stmts.html#compatibility-via-lazy-modules)
                
        *   [7.11.2. Future statements](https://docs.python.org/3/reference/simple_stmts.html#future-statements)
            
    *   [7.12. The `global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)
        
    *   [7.13. The `nonlocal` statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)
        
    *   [7.14. The `type` statement](https://docs.python.org/3/reference/simple_stmts.html#the-type-statement)
        

#### Previous topic

[6\. Expressions](https://docs.python.org/3/reference/expressions.html "previous chapter")

#### Next topic

[8\. Compound statements](https://docs.python.org/3/reference/compound_stmts.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=7.+Simple+statements&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fsimple_stmts.html&pagesource=reference%2Fsimple_stmts.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/simple_stmts.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/compound_stmts.html "8. Compound statements")
     |
*   [previous](https://docs.python.org/3/reference/expressions.html "6. Expressions")
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
*   [7\. Simple statements](https://docs.python.org/3/reference/simple_stmts.html)
    
*    
    
    |
*   Theme Auto Light Dark |