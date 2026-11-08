### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/executionmodel.html "4. Execution model")
     |
*   [previous](https://docs.python.org/3/reference/lexical_analysis.html "2. Lexical analysis")
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
*   [3\. Data model](https://docs.python.org/3/reference/datamodel.html)
    
*    
    
    |
*   Theme Auto Light Dark |

3\. Data model[¶](https://docs.python.org/3/reference/datamodel.html#data-model "Link to this heading")

========================================================================================================

3.1. Objects, values and types[¶](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

_Objects_ are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. Even code is represented by objects.

Every object has an identity, a type and a value. An object’s _identity_ never changes once it has been created; you may think of it as the object’s address in memory. The [`is`](https://docs.python.org/3/reference/expressions.html#is)
 operator compares the identity of two objects; the [`id()`](https://docs.python.org/3/builtins/functions.html#id "id")
 function returns an integer representing its identity.

**CPython implementation detail:** For CPython, `id(x)` is the memory address where `x` is stored.

An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type. The [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
 function returns an object’s type (which is an object itself). Like its identity, an object’s _type_ is also unchangeable. [\[1\]](https://docs.python.org/3/reference/datamodel.html#id20)

The _value_ of some objects can change. Objects whose value can change are said to be _mutable_; objects whose value is unchangeable once they are created are called _immutable_. (The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value, it is more subtle.) An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected. An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.

**CPython implementation detail:** CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references. See the documentation of the [`gc`](https://docs.python.org/3/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.")
 module for information on controlling the collection of cyclic garbage. Other implementations act differently and CPython may change. Do not depend on immediate finalization of objects when they become unreachable (so you should always close files explicitly).

Note that the use of the implementation’s tracing or debugging facilities may keep objects alive that would normally be collectable. Also note that catching an exception with a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
…[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 statement may keep objects alive.

Some objects contain references to “external” resources such as open files or windows. It is understood that these resources are freed when the object is garbage-collected, but since garbage collection is not guaranteed to happen, such objects also provide an explicit way to release the external resource, usually a `close()` method. Programs are strongly recommended to explicitly close such objects. The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
…[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 statement and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement provide convenient ways to do this.

Some objects contain references to other objects; these are called _containers_. Examples of containers are tuples, lists and dictionaries. The references are part of a container’s value. In most cases, when we talk about the value of a container, we imply the values, not the identities of the contained objects; however, when we talk about the mutability of a container, only the identities of the immediately contained objects are implied. So, if an immutable container (like a tuple) contains a reference to a mutable object, its value changes if that mutable object is changed.

Types affect almost all aspects of object behavior. Even the importance of object identity is affected in some sense: for immutable types, operations that compute new values may actually return a reference to any existing object with the same type and value, while for mutable objects this is not allowed. For example, after `a = 1; b = 1`, _a_ and _b_ may or may not refer to the same object with the value one, depending on the implementation. This is because [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 is an immutable type, so the reference to `1` can be reused. This behaviour depends on the implementation used, so should not be relied upon, but is something to be aware of when making use of object identity tests. However, after `c = []; d = []`, _c_ and _d_ are guaranteed to refer to two different, unique, newly created empty lists. (Note that `e = f = []` assigns the _same_ object to both _e_ and _f_.)

3.2. The standard type hierarchy[¶](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Below is a list of the types that are built into Python. Extension modules (written in C, Java, or other languages, depending on the implementation) can define additional types. Future versions of Python may add types to the type hierarchy (e.g., rational numbers, efficiently stored arrays of integers, etc.), although such additions will often be provided via the standard library instead.

Some of the type descriptions below contain a paragraph listing ‘special attributes.’ These are attributes that provide access to the implementation and are not intended for general use. Their definition may change in the future.

### 3.2.1. None[¶](https://docs.python.org/3/reference/datamodel.html#none "Link to this heading")

This type has a single value. There is a single object with this value. This object is accessed through the built-in name `None`. It is used to signify the absence of a value in many situations, e.g., it is returned from functions that don’t explicitly return anything. Its truth value is false.

### 3.2.2. NotImplemented[¶](https://docs.python.org/3/reference/datamodel.html#notimplemented "Link to this heading")

This type has a single value. There is a single object with this value. This object is accessed through the built-in name [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
. Numeric methods and rich comparison methods should return this value if they do not implement the operation for the operands provided. (The interpreter will then try the reflected operation, or some other fallback, depending on the operator.) It should not be evaluated in a boolean context.

See [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)
 for more details.

Changed in version 3.9: Evaluating [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 in a boolean context was deprecated.

Changed in version 3.14: Evaluating [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 in a boolean context now raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. It previously evaluated to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 and emitted a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 since Python 3.9.

### 3.2.3. Ellipsis[¶](https://docs.python.org/3/reference/datamodel.html#ellipsis "Link to this heading")

This type has a single value. There is a single object with this value. This object is accessed through the literal `...` or the built-in name `Ellipsis`. Its truth value is true.

### 3.2.4. [`numbers.Number`](https://docs.python.org/3/library/numbers.html#numbers.Number "numbers.Number")
[¶](https://docs.python.org/3/reference/datamodel.html#numbers-number "Link to this heading")

These are created by numeric literals and returned as results by arithmetic operators and arithmetic built-in functions. Numeric objects are immutable; once created their value never changes. Python numbers are of course strongly related to mathematical numbers, but subject to the limitations of numerical representation in computers.

The string representations of the numeric classes, computed by [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 and [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__")
, have the following properties:

*   They are valid numeric literals which, when passed to their class constructor, produce an object having the value of the original numeric.
    
*   The representation is in base 10, when possible.
    
*   Leading zeros, possibly excepting a single zero before a decimal point, are not shown.
    
*   Trailing zeros, possibly excepting a single zero after a decimal point, are not shown.
    
*   A sign is shown only when the number is negative.
    

Python distinguishes between integers, floating-point numbers, and complex numbers:

#### 3.2.4.1. [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
[¶](https://docs.python.org/3/reference/datamodel.html#numbers-integral "Link to this heading")

These represent elements from the mathematical set of integers (positive and negative).

Note

The rules for integer representation are intended to give the most meaningful interpretation of shift and mask operations involving negative integers.

There are two types of integers:

Integers ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
)

These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2’s complement which gives the illusion of an infinite string of sign bits extending to the left.

Booleans ([`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
)

These represent the truth values False and True. The two objects representing the values `False` and `True` are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings `"False"` or `"True"` are returned, respectively.

#### 3.2.4.2. [`numbers.Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real")
 ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
)[¶](https://docs.python.org/3/reference/datamodel.html#numbers-real-float "Link to this heading")

These represent machine-level double precision floating-point numbers. You are at the mercy of the underlying machine architecture (and C or Java implementation) for the accepted range and handling of overflow. Python does not support single-precision floating-point numbers; the savings in processor and memory usage that are usually the reason for using these are dwarfed by the overhead of using objects in Python, so there is no reason to complicate the language with two kinds of floating-point numbers.

#### 3.2.4.3. [`numbers.Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex")
 ([`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
)[¶](https://docs.python.org/3/reference/datamodel.html#numbers-complex-complex "Link to this heading")

These represent complex numbers as a pair of machine-level double precision floating-point numbers. The same caveats apply as for floating-point numbers. The real and imaginary parts of a complex number `z` can be retrieved through the read-only attributes `z.real` and `z.imag`.

### 3.2.5. Sequences[¶](https://docs.python.org/3/reference/datamodel.html#sequences "Link to this heading")

These represent finite ordered sets indexed by non-negative numbers. The built-in function [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 returns the number of items of a sequence. When the length of a sequence is _n_, the index set contains the numbers 0, 1, …, _n_\-1. Item _i_ of sequence _a_ is selected by `a[i]`. Some sequences, including built-in sequences, interpret negative subscripts by adding the sequence length. For example, `a[-2]` equals `a[n-2]`, the second to last item of sequence a with length `n`.

The resulting value must be a nonnegative integer less than the number of items in the sequence. If it is not, an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 is raised.

Sequences also support slicing: `a[start:stop]` selects all items with index _k_ such that _start_ `<=` _k_ `<` _stop_. When used as an expression, a slice is a sequence of the same type. The comment above about negative subscripts also applies to negative slice positions. Note that no error is raised if a slice position is less than zero or larger than the length of the sequence.

If _start_ is missing or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, slicing behaves as if _start_ was zero. If _stop_ is missing or `None`, slicing behaves as if _stop_ was equal to the length of the sequence.

Some sequences also support “extended slicing” with a third “step” parameter: `a[i:j:k]` selects all items of _a_ with index _x_ where `x = i + n*k`, _n_ `>=` `0` and _i_ `<=` _x_ `<` _j_.

Sequences are distinguished according to their mutability:

#### 3.2.5.1. Immutable sequences[¶](https://docs.python.org/3/reference/datamodel.html#immutable-sequences "Link to this heading")

An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be changed; however, the collection of objects directly referenced by an immutable object cannot change.)

The following types are immutable sequences:

Strings

A string ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) is a sequence of values that represent _characters_, or more formally, _Unicode code points_. All the code points in the range `0` to `0x10FFFF` can be represented in a string.

Python doesn’t have a dedicated _character_ type. Instead, every code point in the string is represented as a string object with length `1`.

The built-in function [`ord()`](https://docs.python.org/3/builtins/functions.html#ord "ord")
 converts a code point from its string form to an integer in the range `0` to `0x10FFFF`; [`chr()`](https://docs.python.org/3/builtins/functions.html#chr "chr")
 converts an integer in the range `0` to `0x10FFFF` to the corresponding length `1` string object. [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
 can be used to convert a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 to [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 using the given text encoding, and [`bytes.decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "bytes.decode")
 can be used to achieve the opposite.

Tuples

The items of a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). An empty tuple can be formed by an empty pair of parentheses.

Bytes

A [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object is an immutable array. The items are 8-bit bytes, represented by integers in the range 0 <= x < 256. Bytes literals (like `b'abc'`) and the built-in [`bytes()`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 constructor can be used to create bytes objects. Also, bytes objects can be decoded to strings via the [`decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "bytes.decode")
 method.

#### 3.2.5.2. Mutable sequences[¶](https://docs.python.org/3/reference/datamodel.html#mutable-sequences "Link to this heading")

Mutable sequences can be changed after they are created. The subscription and slicing notations can be used as the target of assignment and [`del`](https://docs.python.org/3/reference/simple_stmts.html#del)
 (delete) statements.

Note

The [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 and [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
 module provide additional examples of mutable sequence types.

There are currently two intrinsic mutable sequence types:

Lists

The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.)

Byte Arrays

A bytearray object is a mutable array. They are created by the built-in [`bytearray()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 constructor. Aside from being mutable (and hence unhashable), byte arrays otherwise provide the same interface and functionality as immutable [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects.

### 3.2.6. Set types[¶](https://docs.python.org/3/reference/datamodel.html#set-types "Link to this heading")

These represent unordered, finite sets of unique, immutable objects. As such, they cannot be indexed by any subscript. However, they can be iterated over, and the built-in function [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 returns the number of items in a set. Common uses for sets are fast membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

For set elements, the same immutability rules apply as for dictionary keys. Note that numeric types obey the normal rules for numeric comparison: if two numbers compare equal (e.g., `1` and `1.0`), only one of them can be contained in a set.

There are currently two intrinsic set types:

Sets

These represent a mutable set. They are created by the built-in [`set()`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 constructor and can be modified afterwards by several methods, such as [`add()`](https://docs.python.org/3/builtins/stdtypes.html#set.add "set.add")
.

Frozen sets

These represent an immutable set. They are created by the built-in [`frozenset()`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
 constructor. As a frozenset is immutable and [hashable](https://docs.python.org/3/glossary.html#term-hashable)
, it can be used again as an element of another set, or as a dictionary key.

### 3.2.7. Mappings[¶](https://docs.python.org/3/reference/datamodel.html#mappings "Link to this heading")

These represent finite sets of objects indexed by arbitrary index sets. The subscript notation `a[k]` selects the item indexed by `k` from the mapping `a`; this can be used in expressions and as the target of assignments or [`del`](https://docs.python.org/3/reference/simple_stmts.html#del)
 statements. The built-in function [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 returns the number of items in a mapping.

There are two intrinsic mapping types:

#### 3.2.7.1. Dictionaries[¶](https://docs.python.org/3/reference/datamodel.html#dictionaries "Link to this heading")

These represent finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity, the reason being that the efficient implementation of dictionaries requires a key’s hash value to remain constant. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g., `1` and `1.0`) then they can be used interchangeably to index the same dictionary entry.

Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added sequentially over the dictionary. Replacing an existing key does not change the order, however removing a key and re-inserting it will add it to the end instead of keeping its old place.

Dictionaries are mutable; they can be created by the `{}` notation (see section [Dictionary displays](https://docs.python.org/3/reference/expressions.html#dict)
).

The extension modules [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager")
 and [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")
 provide additional examples of mapping types, as does the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 module.

Changed in version 3.7: Dictionaries did not preserve insertion order in versions of Python before 3.6. In CPython 3.6, insertion order was preserved, but it was considered an implementation detail at that time rather than a language guarantee.

#### 3.2.7.2. Frozen dictionaries[¶](https://docs.python.org/3/reference/datamodel.html#frozen-dictionaries "Link to this heading")

These represent an immutable dictionary. They are created by the built-in [`frozendict()`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 constructor. A frozendict is [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 if all of its keys and values are hashable, in which case it can be used as an element of a set, or as a key in another mapping. `frozendict` is not a subclass of [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
; it inherits directly from [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
.

Added in version 3.15.

### 3.2.8. Callable types[¶](https://docs.python.org/3/reference/datamodel.html#callable-types "Link to this heading")

These are the types to which the function call operation (see section [Calls](https://docs.python.org/3/reference/expressions.html#calls)
) can be applied:

#### 3.2.8.1. User-defined functions[¶](https://docs.python.org/3/reference/datamodel.html#user-defined-functions "Link to this heading")

A user-defined function object is created by a function definition (see section [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function)
). It should be called with an argument list containing the same number of items as the function’s formal parameter list.

##### 3.2.8.1.1. Special read-only attributes[¶](https://docs.python.org/3/reference/datamodel.html#special-read-only-attributes "Link to this heading")

| Attribute | Meaning |
| --- | --- |
| function.\_\_builtins\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__builtins__ "Link to this definition") | A reference to the [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")<br> that holds the function’s builtins namespace.<br><br>Added in version 3.10. |
| function.\_\_globals\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__globals__ "Link to this definition") | A reference to the [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")<br> that holds the function’s [global variables](https://docs.python.org/3/reference/executionmodel.html#naming)<br> – the global namespace of the module in which the function was defined. |
| function.\_\_closure\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__closure__ "Link to this definition") | `None` or a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> of cells that contain bindings for the names specified in the [`co_freevars`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_freevars "codeobject.co_freevars")<br> attribute of the function’s [`code object`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__")<br>.<br><br>A cell object has the attribute `cell_contents`. This can be used to get the value of the cell, as well as set the value. |

##### 3.2.8.1.2. Special writable attributes[¶](https://docs.python.org/3/reference/datamodel.html#special-writable-attributes "Link to this heading")

Most of these attributes check the type of the assigned value:

| Attribute | Meaning |
| --- | --- |
| function.\_\_doc\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "Link to this definition") | The function’s documentation string, or `None` if unavailable. |
| function.\_\_name\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__name__ "Link to this definition") | The function’s name. See also: [`__name__ attributes`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")<br>. |
| function.\_\_qualname\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "Link to this definition") | The function’s [qualified name](https://docs.python.org/3/glossary.html#term-qualified-name)<br>. See also: [`__qualname__ attributes`](https://docs.python.org/3/builtins/stdtypes.html#definition.__qualname__ "definition.__qualname__")<br>.<br><br>Added in version 3.3. |
| function.\_\_module\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__module__ "Link to this definition") | The name of the module the function was defined in, or `None` if unavailable. |
| function.\_\_defaults\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__defaults__ "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing default [parameter](https://docs.python.org/3/glossary.html#term-parameter)<br> values for those parameters that have defaults, or `None` if no parameters have a default value. |
| function.\_\_code\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__code__ "Link to this definition") | The [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)<br> representing the compiled function body. |
| function.\_\_dict\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__dict__ "Link to this definition") | The namespace supporting arbitrary function attributes. See also: [`__dict__ attributes`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")<br>. |
| function.\_\_annotations\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__annotations__ "Link to this definition") | A [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")<br> containing annotations of [parameters](https://docs.python.org/3/glossary.html#term-parameter)<br>. The keys of the dictionary are the parameter names, and `'return'` for the return annotation, if provided. See also: [`object.__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__")<br>.<br><br>Changed in version 3.14: Annotations are now [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)<br>. See [**PEP 649**](https://peps.python.org/pep-0649/)<br>. |
| function.\_\_annotate\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__annotate__ "Link to this definition") | The [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function)<br> for this function, or `None` if the function has no annotations. See [`object.__annotate__`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__")<br>.<br><br>Added in version 3.14. |
| function.\_\_kwdefaults\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__kwdefaults__ "Link to this definition") | A [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")<br> containing defaults for keyword-only [parameters](https://docs.python.org/3/glossary.html#term-parameter)<br>. |
| function.\_\_type\_params\_\_[¶](https://docs.python.org/3/reference/datamodel.html#function.__type_params__ "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)<br> of a [generic function](https://docs.python.org/3/reference/compound_stmts.html#generic-functions)<br>.<br><br>Added in version 3.12. |

Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach metadata to functions. Regular attribute dot-notation is used to get and set such attributes.

**CPython implementation detail:** CPython’s current implementation only supports function attributes on user-defined functions. Function attributes on [built-in functions](https://docs.python.org/3/reference/datamodel.html#builtin-functions)
 may be supported in the future.

Additional information about a function’s definition can be retrieved from its [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
 (accessible via the [`__code__`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__")
 attribute).

#### 3.2.8.2. Instance methods[¶](https://docs.python.org/3/reference/datamodel.html#instance-methods "Link to this heading")

An instance method object combines a class, a class instance and any callable object (normally a user-defined function).

Special read-only attributes:

|     |     |
| --- | --- |
| method.\_\_self\_\_[¶](https://docs.python.org/3/reference/datamodel.html#method.__self__ "Link to this definition") | Refers to the class instance object to which the method is [bound](https://docs.python.org/3/reference/datamodel.html#method-binding) |
| method.\_\_func\_\_[¶](https://docs.python.org/3/reference/datamodel.html#method.__func__ "Link to this definition") | Refers to the original [function object](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs) |
| method.\_\_doc\_\_[¶](https://docs.python.org/3/reference/datamodel.html#method.__doc__ "Link to this definition") | The method’s documentation (same as [`method.__func__.__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")<br>). A [`string`](https://docs.python.org/3/builtins/stdtypes.html#str "str")<br> if the original function had a docstring, else `None`. |
| method.\_\_name\_\_[¶](https://docs.python.org/3/reference/datamodel.html#method.__name__ "Link to this definition") | The name of the method (same as [`method.__func__.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__")<br>) |
| method.\_\_module\_\_[¶](https://docs.python.org/3/reference/datamodel.html#method.__module__ "Link to this definition") | The name of the module the method was defined in, or `None` if unavailable. |

Methods also support accessing (but not setting) the arbitrary function attributes on the underlying [function object](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs)
.

User-defined method objects may be created when getting an attribute of a class (perhaps via an instance of that class), if that attribute is a user-defined [function object](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs)
 or a [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 object.

When an instance method object is created by retrieving a user-defined [function object](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs)
 from a class via one of its instances, its [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
 attribute is the instance, and the method object is said to be _bound_. The new method’s [`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")
 attribute is the original function object.

When an instance method object is created by retrieving a [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 object from a class or instance, its [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
 attribute is the class itself, and its [`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")
 attribute is the function object underlying the class method.

When an instance method object is called, the underlying function ([`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")
) is called, inserting the class instance ([`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
) in front of the argument list. For instance, when `C` is a class which contains a definition for a function `f()`, and `x` is an instance of `C`, calling `x.f(1)` is equivalent to calling `C.f(x, 1)`.

When an instance method object is derived from a [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 object, the “class instance” stored in [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
 will actually be the class itself, so that calling either `x.f(1)` or `C.f(1)` is equivalent to calling `f(C,1)` where `f` is the underlying function.

It is important to note that user-defined functions which are attributes of a class instance are not converted to bound methods; this _only_ happens when the function is an attribute of the class.

#### 3.2.8.3. Generator functions[¶](https://docs.python.org/3/reference/datamodel.html#generator-functions "Link to this heading")

A function or method which contains a [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 expression (see section [Yield expressions](https://docs.python.org/3/reference/expressions.html#yieldexpr)
) is called a _generator function_. Such a function, when called, always returns an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 object which can be used to execute the body of the function: calling the iterator’s [`iterator.__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
 method will cause the function to execute until it provides a value using the `yield` expression. When the function executes a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement or falls off the end, a [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 exception is raised and the iterator will have reached the end of the set of values to be returned.

#### 3.2.8.4. Coroutine functions[¶](https://docs.python.org/3/reference/datamodel.html#coroutine-functions "Link to this heading")

A function or method which is defined using [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 is called a _coroutine function_. Such a function, when called, returns a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 object. It may contain [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expressions, as well as [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 and [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 statements. See also the [Coroutine Objects](https://docs.python.org/3/reference/datamodel.html#coroutine-objects)
 section.

#### 3.2.8.5. Asynchronous generator functions[¶](https://docs.python.org/3/reference/datamodel.html#asynchronous-generator-functions "Link to this heading")

A function or method which is defined using [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 and which contains a [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 expression is called a _asynchronous generator function_. Such a function, when called, returns an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
 object which can be used in an [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 statement to execute the body of the function.

Calling the asynchronous iterator’s [`aiterator.__anext__`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__")
 method will return an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 which when awaited will execute until it provides a value using the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 expression. When the function executes an empty [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)
 statement or falls off the end, a [`StopAsyncIteration`](https://docs.python.org/3/builtins/exceptions.html#StopAsyncIteration "StopAsyncIteration")
 exception is raised and the asynchronous iterator will have reached the end of the set of values to be yielded.

#### 3.2.8.6. Built-in functions[¶](https://docs.python.org/3/reference/datamodel.html#built-in-functions "Link to this heading")

A built-in function object is a wrapper around a C function. Examples of built-in functions are [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 and [`math.sin()`](https://docs.python.org/3/library/math.html#math.sin "math.sin")
 ([`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 is a standard built-in module). The number and type of the arguments are determined by the C function. Special read-only attributes:

*   `__doc__` is the function’s documentation string, or `None` if unavailable. See [`function.__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")
    .
    
*   `__name__` is the function’s name. See [`function.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__")
    .
    
*   `__self__` is the module object the function was defined in or `None` if unavailable.
    
*   `__module__` is the name of the module the function was defined in or `None` if unavailable. See [`function.__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__")
    .
    

#### 3.2.8.7. Built-in methods[¶](https://docs.python.org/3/reference/datamodel.html#built-in-methods "Link to this heading")

This is really a different disguise of a built-in function, this time containing an object passed to the C function as an implicit extra argument. An example of a built-in method is `alist.append()`, assuming _alist_ is a list object. In this case, the special read-only attribute `__self__` is set to the object denoted by _alist_. (The attribute has the same semantics as it does with [`other instance methods`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
.)

#### 3.2.8.8. Classes[¶](https://docs.python.org/3/reference/datamodel.html#classes "Link to this heading")

Classes are callable. These objects normally act as factories for new instances of themselves, but variations are possible for class types that override [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
. The arguments of the call are passed to `__new__()` and, in the typical case, to [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 to initialize the new instance.

#### 3.2.8.9. Class Instances[¶](https://docs.python.org/3/reference/datamodel.html#class-instances "Link to this heading")

Instances of arbitrary classes can be made callable by defining a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method in their class.

### 3.2.9. Modules[¶](https://docs.python.org/3/reference/datamodel.html#modules "Link to this heading")

Modules are a basic organizational unit of Python code, and are created by the [import system](https://docs.python.org/3/reference/import.html#importsystem)
 as invoked either by the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statement, or by calling functions such as [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")
 and built-in [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
. A module object has a namespace implemented by a [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 object (this is the dictionary referenced by the [`__globals__`](https://docs.python.org/3/reference/datamodel.html#function.__globals__ "function.__globals__")
 attribute of functions defined in the module). Attribute references are translated to lookups in this dictionary, e.g., `m.x` is equivalent to `m.__dict__["x"]`. A module object does not contain the code object used to initialize the module (since it isn’t needed once the initialization is done).

Attribute assignment updates the module’s namespace dictionary, e.g., `m.x = 1` is equivalent to `m.__dict__["x"] = 1`.

#### 3.2.9.1. Import-related attributes on module objects[¶](https://docs.python.org/3/reference/datamodel.html#import-related-attributes-on-module-objects "Link to this heading")

Module objects have the following attributes that relate to the [import system](https://docs.python.org/3/reference/import.html#importsystem)
. When a module is created using the machinery associated with the import system, these attributes are filled in based on the module’s [spec](https://docs.python.org/3/glossary.html#term-module-spec)
, before the [loader](https://docs.python.org/3/glossary.html#term-loader)
 executes and loads the module.

To create a module dynamically rather than using the import system, it’s recommended to use [`importlib.util.module_from_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "importlib.util.module_from_spec")
, which will set the various import-controlled attributes to appropriate values. It’s also possible to use the [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
 constructor to create modules directly, but this technique is more error-prone, as most attributes must be manually set on the module object after it has been created when using this approach.

Caution

With the exception of [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
, it is **strongly** recommended that you rely on [`__spec__`](https://docs.python.org/3/reference/datamodel.html#module.__spec__ "module.__spec__")
 and its attributes instead of any of the other individual attributes listed in this subsection. Note that updating an attribute on `__spec__` will not update the corresponding attribute on the module itself:

Copy

\>>> import typing
\>>> typing.\_\_name\_\_, typing.\_\_spec\_\_.name
('typing', 'typing')
\>>> typing.\_\_spec\_\_.name \= 'spelling'
\>>> typing.\_\_name\_\_, typing.\_\_spec\_\_.name
('typing', 'spelling')
\>>> typing.\_\_name\_\_ \= 'keyboard\_smashing'
\>>> typing.\_\_name\_\_, typing.\_\_spec\_\_.name
('keyboard\_smashing', 'spelling')

module.\_\_name\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__name__ "Link to this definition")

The name used to uniquely identify the module in the import system. For a directly executed module, this will be set to `"__main__"`.

This attribute must be set to the fully qualified name of the module. It is expected to match the value of [`module.__spec__.name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name")
.

module.\_\_spec\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__spec__ "Link to this definition")

A record of the module’s import-system-related state.

Set to the [`module spec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 that was used when importing the module. See [Module specs](https://docs.python.org/3/reference/import.html#module-specs)
 for more details.

Added in version 3.4.

module.\_\_package\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__package__ "Link to this definition")

The [package](https://docs.python.org/3/glossary.html#term-package)
 a module belongs to.

If the module is top-level (that is, not a part of any specific package) then the attribute should be set to `''` (the empty string). Otherwise, it should be set to the name of the module’s package (which can be equal to [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 if the module itself is a package). See [**PEP 366**](https://peps.python.org/pep-0366/)
 for further details.

This attribute is used instead of [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 to calculate explicit relative imports for main modules. It defaults to `None` for modules created dynamically using the [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
 constructor; use [`importlib.util.module_from_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "importlib.util.module_from_spec")
 instead to ensure the attribute is set to a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
.

It is **strongly** recommended that you use [`module.__spec__.parent`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
 instead of `module.__package__`. [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 is now only used as a fallback if `__spec__.parent` is not set, and this fallback path is deprecated.

Changed in version 3.4: This attribute now defaults to `None` for modules created dynamically using the [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
 constructor. Previously the attribute was optional.

Changed in version 3.6: The value of `__package__` is expected to be the same as [`__spec__.parent`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
. [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 is now only used as a fallback during import resolution if `__spec__.parent` is not defined.

Changed in version 3.10: [`ImportWarning`](https://docs.python.org/3/builtins/exceptions.html#ImportWarning "ImportWarning")
 is raised if an import resolution falls back to `__package__` instead of [`__spec__.parent`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
.

Changed in version 3.12: Raise [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 instead of [`ImportWarning`](https://docs.python.org/3/builtins/exceptions.html#ImportWarning "ImportWarning")
 when falling back to `__package__` during import resolution.

Deprecated since version 3.13, removed in version 3.15: `__package__` will cease to be set or taken into consideration by the import system or standard library.

module.\_\_loader\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "Link to this definition")

The [loader](https://docs.python.org/3/glossary.html#term-loader)
 object that the import machinery used to load the module.

This attribute is mostly useful for introspection, but can be used for additional loader-specific functionality, for example getting data associated with a loader.

`__loader__` defaults to `None` for modules created dynamically using the [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
 constructor; use [`importlib.util.module_from_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "importlib.util.module_from_spec")
 instead to ensure the attribute is set to a [loader](https://docs.python.org/3/glossary.html#term-loader)
 object.

It is **strongly** recommended that you use [`module.__spec__.loader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader")
 instead of `module.__loader__`.

Changed in version 3.4: This attribute now defaults to `None` for modules created dynamically using the [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
 constructor. Previously the attribute was optional.

Deprecated since version 3.12, will be removed in version 3.16: Setting `__loader__` on a module while failing to set `__spec__.loader` is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.

module.\_\_path\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__path__ "Link to this definition")

A (possibly empty) [sequence](https://docs.python.org/3/glossary.html#term-sequence)
 of strings enumerating the locations where the package’s submodules will be found. Non-package modules should not have a `__path__` attribute. See [\_\_path\_\_ attributes on modules](https://docs.python.org/3/reference/import.html#package-path-rules)
 for more details.

It is **strongly** recommended that you use [`module.__spec__.submodule_search_locations`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.submodule_search_locations "importlib.machinery.ModuleSpec.submodule_search_locations")
 instead of `module.__path__`.

module.\_\_file\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__file__ "Link to this definition")

`__file__` is an optional attribute that may or may not be set. Both attributes should be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 when they are available.

An optional attribute, `__file__` indicates the pathname of the file from which the module was loaded (if loaded from a file), or the pathname of the shared library file for extension modules loaded dynamically from a shared library. It might be missing for certain types of modules, such as C modules that are statically linked into the interpreter, and the [import system](https://docs.python.org/3/reference/import.html#importsystem)
 may opt to leave it unset if it has no semantic meaning (for example, a module loaded from a database).

Changed in version 3.15: The `__cached__` attribute is no longer set on modules or taken into consideration by the import system or standard library.

#### 3.2.9.2. Other writable attributes on module objects[¶](https://docs.python.org/3/reference/datamodel.html#other-writable-attributes-on-module-objects "Link to this heading")

As well as the import-related attributes listed above, module objects also have the following writable attributes:

module.\_\_doc\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__doc__ "Link to this definition")

The module’s documentation string, or `None` if unavailable. See also: [`__doc__ attributes`](https://docs.python.org/3/builtins/stdtypes.html#definition.__doc__ "definition.__doc__")
.

module.\_\_annotations\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__annotations__ "Link to this definition")

A dictionary containing [variable annotations](https://docs.python.org/3/glossary.html#term-variable-annotation)
 collected during module body execution. For best practices on working with `__annotations__`, see [`annotationlib`](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "annotationlib: Functionality for introspecting annotations")
.

Changed in version 3.14: Annotations are now [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)
. See [**PEP 649**](https://peps.python.org/pep-0649/)
.

module.\_\_annotate\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__annotate__ "Link to this definition")

The [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function)
 for this module, or `None` if the module has no annotations. See also: [`__annotate__`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__")
 attributes.

Added in version 3.14.

module.\_\_lazy\_modules\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__lazy_modules__ "Link to this definition")

A container (an object implementing [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
) of fully qualified module name strings. When defined at module scope, any regular [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statement in that module whose target module name appears in this container is treated as a [lazy import](https://docs.python.org/3/reference/simple_stmts.html#lazy-imports)
, as if the [`lazy`](https://docs.python.org/3/reference/simple_stmts.html#lazy)
 keyword had been used. Imports inside functions, class bodies, or [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
/[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
/[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 blocks are unaffected.

See [Compatibility via \_\_lazy\_modules\_\_](https://docs.python.org/3/reference/simple_stmts.html#lazy-modules-compat)
 for details and examples.

Added in version 3.15.

#### 3.2.9.3. Module dictionaries[¶](https://docs.python.org/3/reference/datamodel.html#module-dictionaries "Link to this heading")

Module objects also have the following special read-only attribute:

module.\_\_dict\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__dict__ "Link to this definition")

The module’s namespace as a dictionary object. Uniquely among the attributes listed here, `__dict__` cannot be accessed as a global variable from within a module; it can only be accessed as an attribute on module objects.

**CPython implementation detail:** Because of the way CPython clears module dictionaries, the module dictionary will be cleared when the module falls out of scope even if the dictionary still has live references. To avoid this, copy the dictionary or keep the module around while using its dictionary directly.

### 3.2.10. Custom classes[¶](https://docs.python.org/3/reference/datamodel.html#custom-classes "Link to this heading")

Custom class types are typically created by class definitions (see section [Class definitions](https://docs.python.org/3/reference/compound_stmts.html#class)
). A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary, e.g., `C.x` is translated to `C.__dict__["x"]` (although there are a number of hooks which allow for other means of locating attributes). When the attribute name is not found there, the attribute search continues in the base classes. This search of the base classes uses the C3 method resolution order which behaves correctly even in the presence of ‘diamond’ inheritance structures where there are multiple inheritance paths leading back to a common ancestor. Additional details on the C3 MRO used by Python can be found at [The Python 2.3 Method Resolution Order](https://docs.python.org/3/howto/mro.html#python-2-3-mro)
.

When a class attribute reference (for class `C`, say) would yield a class method object, it is transformed into an instance method object whose [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
 attribute is `C`. When it would yield a [`staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 object, it is transformed into the object wrapped by the static method object. See section [Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)
 for another way in which attributes retrieved from a class may differ from those actually contained in its [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
.

Class attribute assignments update the class’s dictionary, never the dictionary of a base class.

A class object can be called (see above) to yield a class instance (see below).

#### 3.2.10.1. Special attributes[¶](https://docs.python.org/3/reference/datamodel.html#special-attributes "Link to this heading")

| Attribute | Meaning |
| --- | --- |
| type.\_\_name\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__name__ "Link to this definition") | The class’s name. See also: [`__name__ attributes`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")<br>. |
| type.\_\_qualname\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__qualname__ "Link to this definition") | The class’s [qualified name](https://docs.python.org/3/glossary.html#term-qualified-name)<br>. See also: [`__qualname__ attributes`](https://docs.python.org/3/builtins/stdtypes.html#definition.__qualname__ "definition.__qualname__")<br>. |
| type.\_\_module\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__module__ "Link to this definition") | The name of the module in which the class was defined. |
| type.\_\_dict\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "Link to this definition") | A [`mapping proxy`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")<br> providing a read-only view of the class’s namespace. See also: [`__dict__ attributes`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")<br>. |
| type.\_\_bases\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the class’s bases. In most cases, for a class defined as `class X(A, B, C)`, `X.__bases__` will be exactly equal to `(A, B, C)`. |
| type.\_\_base\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__base__ "Link to this definition") | **CPython implementation detail:** The single base class in the inheritance chain that is responsible for the memory layout of instances. This attribute corresponds to [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")<br> at the C level. |
| type.\_\_doc\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__doc__ "Link to this definition") | The class’s documentation string, or `None` if undefined. Not inherited by subclasses. |
| type.\_\_annotations\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__annotations__ "Link to this definition") | A dictionary containing [variable annotations](https://docs.python.org/3/glossary.html#term-variable-annotation)<br> collected during class body execution. See also: [`__annotations__ attributes`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__")<br>.<br><br>For best practices on working with [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__")<br>, please see [`annotationlib`](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "annotationlib: Functionality for introspecting annotations")<br>. Use [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")<br> instead of accessing this attribute directly.<br><br>Warning<br><br>Accessing the `__annotations__` attribute directly on a class object may return annotations for the wrong class, specifically in certain cases where the class, its base class, or a metaclass is defined under `from __future__ import annotations`. See [**749**](https://peps.python.org/pep-0749/#pep749-metaclasses)<br> for details.<br><br>This attribute does not exist on certain builtin classes. On user-defined classes without `__annotations__`, it is an empty dictionary.<br><br>Changed in version 3.14: Annotations are now [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)<br>. See [**PEP 649**](https://peps.python.org/pep-0649/)<br>. |
| type.\_\_annotate\_\_()[¶](https://docs.python.org/3/reference/datamodel.html#type.__annotate__ "Link to this definition") | The [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function)<br> for this class, or `None` if the class has no annotations. See also: [`__annotate__ attributes`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__")<br>.<br><br>Added in version 3.14. |
| type.\_\_type\_params\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__type_params__ "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)<br> of a [generic class](https://docs.python.org/3/reference/compound_stmts.html#generic-classes)<br>.<br><br>Added in version 3.12. |
| type.\_\_static\_attributes\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__static_attributes__ "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing names of attributes of this class which are assigned through `self.X` from any function in its body.<br><br>Added in version 3.13. |
| type.\_\_firstlineno\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__firstlineno__ "Link to this definition") | The line number of the first line of the class definition, including decorators. Setting the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")<br> attribute removes the `__firstlineno__` item from the type’s dictionary.<br><br>Added in version 3.13. |
| type.\_\_mro\_\_[¶](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "Link to this definition") | The [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> of classes that are considered when looking for base classes during method resolution. |

#### 3.2.10.2. Special methods[¶](https://docs.python.org/3/reference/datamodel.html#special-methods "Link to this heading")

In addition to the special attributes described above, all Python classes also have the following two methods available:

type.mro()[¶](https://docs.python.org/3/reference/datamodel.html#type.mro "Link to this definition")

This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called at class instantiation, and its result is stored in [`__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__")
.

type.\_\_subclasses\_\_()[¶](https://docs.python.org/3/reference/datamodel.html#type.__subclasses__ "Link to this definition")

Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. The list is in definition order. Example:

Copy

\>>> class A: pass
\>>> class B(A): pass
\>>> A.\_\_subclasses\_\_()
\[<class 'B'>\]

### 3.2.11. Class instances[¶](https://docs.python.org/3/reference/datamodel.html#id4 "Link to this heading")

A class instance is created by calling a class object (see above). A class instance has a namespace implemented as a dictionary which is the first place in which attribute references are searched. When an attribute is not found there, and the instance’s class has an attribute by that name, the search continues with the class attributes. If a class attribute is found that is a user-defined function object, it is transformed into an instance method object whose [`__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__")
 attribute is the instance. Static method and class method objects are also transformed; see above under “Classes”. See section [Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)
 for another way in which attributes of a class retrieved via its instances may differ from the objects actually stored in the class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
. If no class attribute is found, and the object’s class has a [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 method, that is called to satisfy the lookup.

Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary. If the class has a [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__")
 or [`__delattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__delattr__ "object.__delattr__")
 method, this is called instead of updating the instance dictionary directly.

Class instances can pretend to be numbers, sequences, or mappings if they have methods with certain special names. See section [Special method names](https://docs.python.org/3/reference/datamodel.html#specialnames)
.

#### 3.2.11.1. Special attributes[¶](https://docs.python.org/3/reference/datamodel.html#id5 "Link to this heading")

object.\_\_class\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__class__ "Link to this definition")

The class to which a class instance belongs.

object.\_\_dict\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "Link to this definition")

A dictionary or other mapping object used to store an object’s (writable) attributes. Not all instances have a `__dict__` attribute; see the section on [\_\_slots\_\_](https://docs.python.org/3/reference/datamodel.html#slots)
 for more details.

### 3.2.12. I/O objects (also known as file objects)[¶](https://docs.python.org/3/reference/datamodel.html#i-o-objects-also-known-as-file-objects "Link to this heading")

A [file object](https://docs.python.org/3/glossary.html#term-file-object)
 represents an open file. Various shortcuts are available to create file objects: the [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 built-in function, and also [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
, [`os.fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
, and the [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile")
 method of socket objects (and perhaps by other functions or methods provided by extension modules).

File objects implement common methods, listed below, to simplify usage in generic code. They are expected to be [With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
.

The objects `sys.stdin`, `sys.stdout` and `sys.stderr` are initialized to file objects corresponding to the interpreter’s standard input, output and error streams; they are all open in text mode and therefore follow the interface defined by the [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase")
 abstract class.

file.read(_size\=\-1_, _/_)[¶](https://docs.python.org/3/reference/datamodel.html#file.read "Link to this definition")

Retrieve up to _size_ data from the file. As a convenience if _size_ is unspecified or -1 retrieve all data available.

file.write(_data_, _/_)[¶](https://docs.python.org/3/reference/datamodel.html#file.write "Link to this definition")

Store _data_ to the file.

file.close()[¶](https://docs.python.org/3/reference/datamodel.html#file.close "Link to this definition")

Flush any buffers and close the underlying file.

### 3.2.13. Internal types[¶](https://docs.python.org/3/reference/datamodel.html#internal-types "Link to this heading")

A few types used internally by the interpreter are exposed to the user. Their definitions may change with future versions of the interpreter, but they are mentioned here for completeness.

#### 3.2.13.1. Code objects[¶](https://docs.python.org/3/reference/datamodel.html#code-objects "Link to this heading")

Code objects represent _byte-compiled_ executable Python code, or [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
. The difference between a code object and a function object is that the function object contains an explicit reference to the function’s globals (the module in which it was defined), while a code object contains no context; also the default argument values are stored in the function object, not in the code object (because they represent values calculated at run-time). Unlike function objects, code objects are immutable and contain no references (directly or indirectly) to mutable objects.

##### 3.2.13.1.1. Special read-only attributes[¶](https://docs.python.org/3/reference/datamodel.html#index-64 "Link to this heading")

|     |     |
| --- | --- |
| codeobject.co\_name[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_name "Link to this definition") | The function name |
| codeobject.co\_qualname[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_qualname "Link to this definition") | The fully qualified function name<br><br>Added in version 3.11. |
| codeobject.co\_argcount[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_argcount "Link to this definition") | The total number of positional [parameters](https://docs.python.org/3/glossary.html#term-parameter)<br> (including positional-only parameters and parameters with default values) that the function has |
| codeobject.co\_posonlyargcount[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_posonlyargcount "Link to this definition") | The number of positional-only [parameters](https://docs.python.org/3/glossary.html#term-parameter)<br> (including arguments with default values) that the function has |
| codeobject.co\_kwonlyargcount[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_kwonlyargcount "Link to this definition") | The number of keyword-only [parameters](https://docs.python.org/3/glossary.html#term-parameter)<br> (including arguments with default values) that the function has |
| codeobject.co\_nlocals[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_nlocals "Link to this definition") | The number of [local variables](https://docs.python.org/3/reference/executionmodel.html#naming)<br> used by the function (including parameters) |
| codeobject.co\_varnames[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the names of the local variables in the function (starting with the parameter names) |
| codeobject.co\_cellvars[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_cellvars "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the names of [local variables](https://docs.python.org/3/reference/executionmodel.html#naming)<br> that are referenced from at least one [nested scope](https://docs.python.org/3/glossary.html#term-nested-scope)<br> inside the function |
| codeobject.co\_freevars[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_freevars "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the names of [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable)<br> that a [nested scope](https://docs.python.org/3/glossary.html#term-nested-scope)<br> references in an outer scope. See also [`function.__closure__`](https://docs.python.org/3/reference/datamodel.html#function.__closure__ "function.__closure__")<br>.<br><br>Note: references to global and builtin names are _not_ included. |
| codeobject.co\_code[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_code "Link to this definition") | A string representing the sequence of [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)<br> instructions in the function |
| codeobject.co\_consts[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_consts "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the literals used by the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)<br> in the function |
| codeobject.co\_names[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "Link to this definition") | A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")<br> containing the names used by the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)<br> in the function |
| codeobject.co\_filename[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_filename "Link to this definition") | The name of the file from which the code was compiled |
| codeobject.co\_firstlineno[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_firstlineno "Link to this definition") | The line number of the first line of the function |
| codeobject.co\_linetable[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_linetable "Link to this definition") | A [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")<br> object containing encoded source location information. The exact format is an implementation detail and may change between Python versions. Use [`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")<br> and [`co_positions()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_positions "codeobject.co_positions")<br> for supported access to line and position information. To create a modified copy of a code object, use [`replace()`](https://docs.python.org/3/reference/datamodel.html#codeobject.replace "codeobject.replace")<br>.<br><br>Added in version 3.10. |
| codeobject.co\_stacksize[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_stacksize "Link to this definition") | The required stack size of the code object |
| codeobject.co\_flags[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "Link to this definition") | An [`integer`](https://docs.python.org/3/builtins/functions.html#int "int")<br> encoding a number of flags for the interpreter. |

The following flag bits are defined for [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
: bit `0x04` is set if the function uses the `*arguments` syntax to accept an arbitrary number of positional arguments; bit `0x08` is set if the function uses the `**keywords` syntax to accept arbitrary keyword arguments; bit `0x20` is set if the function is a generator. See [Code Objects Bit Flags](https://docs.python.org/3/library/inspect.html#inspect-module-co-flags)
 for details on the semantics of each flags that might be present.

Future feature declarations (for example, `from __future__ import division`) also use bits in [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
 to indicate whether a code object was compiled with a particular feature enabled. See [`compiler_flag`](https://docs.python.org/3/library/__future__.html#future__._Feature.compiler_flag "__future__._Feature.compiler_flag")
.

Other bits in [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
 are reserved for internal use.

If a code object represents a function and has a docstring, the [`CO_HAS_DOCSTRING`](https://docs.python.org/3/library/inspect.html#inspect.CO_HAS_DOCSTRING "inspect.CO_HAS_DOCSTRING")
 bit is set in [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
 and the first item in [`co_consts`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_consts "codeobject.co_consts")
 is the docstring of the function.

##### 3.2.13.1.2. Methods on code objects[¶](https://docs.python.org/3/reference/datamodel.html#methods-on-code-objects "Link to this heading")

codeobject.co\_positions()[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_positions "Link to this definition")

Returns an iterable over the source code positions of each [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
 instruction in the code object.

The iterator returns [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
s containing the `(start_line, end_line, start_column, end_column)`. The _i-th_ tuple corresponds to the position of the source code that compiled to the _i-th_ code unit. Column information is 0-indexed utf-8 byte offsets on the given source line.

This positional information can be missing. A non-exhaustive lists of cases where this may happen:

*   Running the interpreter with [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     `no_debug_ranges`.
    
*   Loading a pyc file compiled while using [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     `no_debug_ranges`.
    
*   Position tuples corresponding to artificial instructions.
    
*   Line and column numbers that can’t be represented due to implementation specific limitations.
    

When this occurs, some or all of the tuple elements can be [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
.

Added in version 3.11.

Note

This feature requires storing column positions in code objects which may result in a small increase of disk usage of compiled Python files or interpreter memory usage. To avoid storing the extra information and/or deactivate printing the extra traceback information, the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `no_debug_ranges` command line flag or the [`PYTHONNODEBUGRANGES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNODEBUGRANGES)
 environment variable can be used.

codeobject.co\_lines()[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "Link to this definition")

Returns an iterator that yields information about successive ranges of [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
s. Each item yielded is a `(start, end, lineno)` [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
:

*   `start` (an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
    ) represents the offset (inclusive) of the start of the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
     range
    
*   `end` (an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
    ) represents the offset (exclusive) of the end of the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
     range
    
*   `lineno` is an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     representing the line number of the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
     range, or `None` if the bytecodes in the given range have no line number
    

The items yielded will have the following properties:

*   The first range yielded will have a `start` of 0.
    
*   The `(start, end)` ranges will be non-decreasing and consecutive. That is, for any pair of [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
    s, the `start` of the second will be equal to the `end` of the first.
    
*   No range will be backwards: `end >= start` for all triples.
    
*   The last [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     yielded will have `end` equal to the size of the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
    .
    

Zero-width ranges, where `start == end`, are allowed. Zero-width ranges are used for lines that are present in the source code, but have been eliminated by the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
 compiler.

Added in version 3.10.

See also

[**PEP 626**](https://peps.python.org/pep-0626/)
 - Precise line numbers for debugging and other tools.

The PEP that introduced the `co_lines()` method.

codeobject.replace(_\*\*kwargs_)[¶](https://docs.python.org/3/reference/datamodel.html#codeobject.replace "Link to this definition")

Return a copy of the code object with new values for the specified fields.

Code objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
.

Added in version 3.8.

#### 3.2.13.2. Frame objects[¶](https://docs.python.org/3/reference/datamodel.html#frame-objects "Link to this heading")

Frame objects represent execution frames. They may occur in [traceback objects](https://docs.python.org/3/reference/datamodel.html#traceback-objects)
, and are also passed to registered trace functions.

##### 3.2.13.2.1. Special read-only attributes[¶](https://docs.python.org/3/reference/datamodel.html#index-70 "Link to this heading")

|     |     |
| --- | --- |
| frame.f\_back[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_back "Link to this definition") | Points to the previous stack frame (towards the caller), or `None` if this is the bottom stack frame |
| frame.f\_code[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_code "Link to this definition") | The [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)<br> being executed in this frame. Accessing this attribute raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)<br> `object.__getattr__` with arguments `obj` and `"f_code"`. |
| frame.f\_locals[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "Link to this definition") | The mapping used by the frame to look up [local variables](https://docs.python.org/3/reference/executionmodel.html#naming)<br>. If the frame refers to an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)<br>, this may return a write-through proxy object.<br><br>Changed in version 3.13: Return a proxy for optimized scopes. |
| frame.f\_globals[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_globals "Link to this definition") | The dictionary used by the frame to look up [global variables](https://docs.python.org/3/reference/executionmodel.html#naming) |
| frame.f\_builtins[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_builtins "Link to this definition") | The dictionary used by the frame to look up [built-in (intrinsic) names](https://docs.python.org/3/reference/executionmodel.html#naming) |
| frame.f\_lasti[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_lasti "Link to this definition") | The “precise instruction” of the frame object (this is an index into the [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)<br> string of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)<br>) |
| frame.f\_generator[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_generator "Link to this definition") | The [generator](https://docs.python.org/3/glossary.html#term-generator)<br> or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)<br> object that owns this frame, or `None` if the frame is a normal function.<br><br>Added in version 3.14. |

##### 3.2.13.2.2. Special writable attributes[¶](https://docs.python.org/3/reference/datamodel.html#index-71 "Link to this heading")

|     |     |
| --- | --- |
| frame.f\_trace[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_trace "Link to this definition") | If not `None`, this is a function called for various events during code execution (this is used by debuggers). Normally an event is triggered for each new source line (see [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines")<br>). |
| frame.f\_trace\_lines[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "Link to this definition") | Set this attribute to [`False`](https://docs.python.org/3/builtins/constants.html#False "False")<br> to disable triggering a tracing event for each source line. |
| frame.f\_trace\_opcodes[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "Link to this definition") | Set this attribute to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")<br> to allow per-opcode events to be requested. Note that this may lead to undefined interpreter behaviour if exceptions raised by the trace function escape to the function being traced. |
| frame.f\_lineno[¶](https://docs.python.org/3/reference/datamodel.html#frame.f_lineno "Link to this definition") | The current line number of the frame – writing to this from within a trace function jumps to the given line (only for the bottom-most frame). A debugger can implement a Jump command (aka Set Next Statement) by writing to this attribute. |

##### 3.2.13.2.3. Frame object methods[¶](https://docs.python.org/3/reference/datamodel.html#frame-object-methods "Link to this heading")

Frame objects support one method:

frame.clear()[¶](https://docs.python.org/3/reference/datamodel.html#frame.clear "Link to this definition")

This method clears all references to [local variables](https://docs.python.org/3/reference/executionmodel.html#naming)
 held by the frame. Also, if the frame belonged to a [generator](https://docs.python.org/3/glossary.html#term-generator)
, the generator is finalized. This helps break reference cycles involving frame objects (for example when catching an [exception](https://docs.python.org/3/builtins/exceptions.html#bltin-exceptions)
 and storing its [traceback](https://docs.python.org/3/reference/datamodel.html#traceback-objects)
 for later use).

[`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised if the frame is currently executing or suspended.

Added in version 3.4.

Changed in version 3.13: Attempting to clear a suspended frame raises [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 (as has always been the case for executing frames).

#### 3.2.13.3. Traceback objects[¶](https://docs.python.org/3/reference/datamodel.html#traceback-objects "Link to this heading")

Traceback objects represent the stack trace of an [exception](https://docs.python.org/3/tutorial/errors.html#tut-errors)
. A traceback object is implicitly created when an exception occurs, and may also be explicitly created by calling [`types.TracebackType`](https://docs.python.org/3/library/types.html#types.TracebackType "types.TracebackType")
.

Changed in version 3.7: Traceback objects can now be explicitly instantiated from Python code.

For implicitly created tracebacks, when the search for an exception handler unwinds the execution stack, at each unwound level a traceback object is inserted in front of the current traceback. When an exception handler is entered, the stack trace is made available to the program. (See section [The try statement](https://docs.python.org/3/reference/compound_stmts.html#try)
.) It is accessible as the third item of the tuple returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
, and as the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
 attribute of the caught exception.

When the program contains no suitable handler, the stack trace is written (nicely formatted) to the standard error stream; if the interpreter is interactive, it is also made available to the user as [`sys.last_traceback`](https://docs.python.org/3/library/sys.html#sys.last_traceback "sys.last_traceback")
.

For explicitly created tracebacks, it is up to the creator of the traceback to determine how the [`tb_next`](https://docs.python.org/3/reference/datamodel.html#traceback.tb_next "traceback.tb_next")
 attributes should be linked to form a full stack trace.

Special read-only attributes:

|     |     |
| --- | --- |
| traceback.tb\_frame[¶](https://docs.python.org/3/reference/datamodel.html#traceback.tb_frame "Link to this definition") | Points to the execution [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects)<br> of the current level.<br><br>Accessing this attribute raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)<br> `object.__getattr__` with arguments `obj` and `"tb_frame"`. |
| traceback.tb\_lineno[¶](https://docs.python.org/3/reference/datamodel.html#traceback.tb_lineno "Link to this definition") | Gives the line number where the exception occurred |
| traceback.tb\_lasti[¶](https://docs.python.org/3/reference/datamodel.html#traceback.tb_lasti "Link to this definition") | Indicates the “precise instruction”. |

The line number and last instruction in the traceback may differ from the line number of its [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects)
 if the exception occurred in a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement with no matching except clause or with a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause.

traceback.tb\_next[¶](https://docs.python.org/3/reference/datamodel.html#traceback.tb_next "Link to this definition")

The special writable attribute `tb_next` is the next level in the stack trace (towards the frame where the exception occurred), or `None` if there is no next level.

Changed in version 3.7: This attribute is now writable

#### 3.2.13.4. Slice objects[¶](https://docs.python.org/3/reference/datamodel.html#slice-objects "Link to this heading")

Slice objects are used to represent slices for [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 methods. They are also created by the built-in [`slice()`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 function.

Added in version 3.15: The [`slice()`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 type now supports [subscription](https://docs.python.org/3/reference/expressions.html#subscriptions)
. For example, `slice[float]` may be used in type annotations to indicate a slice containing [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 objects.

Special read-only attributes: [`start`](https://docs.python.org/3/builtins/functions.html#slice.start "slice.start")
 is the lower bound; [`stop`](https://docs.python.org/3/builtins/functions.html#slice.stop "slice.stop")
 is the upper bound; [`step`](https://docs.python.org/3/builtins/functions.html#slice.step "slice.step")
 is the step value; each is `None` if omitted. These attributes can have any type.

Slice objects support one method:

slice.indices(_self_, _length_)[¶](https://docs.python.org/3/reference/datamodel.html#slice.indices "Link to this definition")

This method takes a single integer argument _length_ and computes information about the slice that the slice object would describe if applied to a sequence of _length_ items. It returns a tuple of three integers; respectively these are the _start_ and _stop_ indices and the _step_ or stride length of the slice. Missing or out-of-bounds indices are handled in a manner consistent with regular slices.

#### 3.2.13.5. Static method objects[¶](https://docs.python.org/3/reference/datamodel.html#static-method-objects "Link to this heading")

Static method objects provide a way of defeating the transformation of function objects to method objects described above. A static method object is a wrapper around any other object, usually a user-defined method object. When a static method object is retrieved from a class or a class instance, the object actually returned is the wrapped object, which is not subject to any further transformation. Static method objects are also callable. Static method objects are created by the built-in [`staticmethod()`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 constructor.

#### 3.2.13.6. Class method objects[¶](https://docs.python.org/3/reference/datamodel.html#class-method-objects "Link to this heading")

A class method object, like a static method object, is a wrapper around another object that alters the way in which that object is retrieved from classes and class instances. The behaviour of class method objects upon such retrieval is described above, under [“instance methods”](https://docs.python.org/3/reference/datamodel.html#instance-methods)
. Class method objects are created by the built-in [`classmethod()`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 constructor.

3.3. Special method names[¶](https://docs.python.org/3/reference/datamodel.html#special-method-names "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python’s approach to _operator overloading_, allowing classes to define their own behavior with respect to language operators. For instance, if a class defines a method named [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, and `x` is an instance of this class, then `x[i]` is roughly equivalent to `type(x).__getitem__(x, i)`. Except where mentioned, attempts to execute an operation raise an exception when no appropriate method is defined (typically [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 or [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
).

Setting a special method to `None` indicates that the corresponding operation is not available. For example, if a class sets [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
 to `None`, the class is not iterable, so calling [`iter()`](https://docs.python.org/3/builtins/functions.html#iter "iter")
 on its instances will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 (without falling back to [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
). [\[2\]](https://docs.python.org/3/reference/datamodel.html#id21)

When implementing a class that emulates any built-in type, it is important that the emulation only be implemented to the degree that it makes sense for the object being modelled. For example, some sequences may work well with retrieval of individual elements, but extracting a slice may not make sense. (One example of this is the [NodeList](https://docs.python.org/3/library/xml.dom.html#dom-nodelist-objects)
 interface in the W3C’s Document Object Model.)

### 3.3.1. Basic customization[¶](https://docs.python.org/3/reference/datamodel.html#basic-customization "Link to this heading")

object.\_\_new\_\_(_cls_\[, _..._\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__new__ "Link to this definition")

Called to create a new instance of class _cls_. `__new__()` is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of `__new__()` should be the new object instance (usually an instance of _cls_).

Typical implementations create a new instance of the class by invoking the superclass’s `__new__()` method using `super().__new__(cls[, ...])` with appropriate arguments and then modifying the newly created instance as necessary before returning it.

If `__new__()` is invoked during object construction and it returns an instance of _cls_, then the new instance’s [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method will be invoked like `__init__(self[, ...])`, where _self_ is the new instance and the remaining arguments are the same as were passed to the object constructor.

If `__new__()` does not return an instance of _cls_, then the new instance’s [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method will not be invoked.

`__new__()` is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

object.\_\_init\_\_(_self_\[, _..._\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__init__ "Link to this definition")

Called after the instance has been created (by [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
), but before it is returned to the caller. The arguments are those passed to the class constructor expression. If a base class has an `__init__()` method, the derived class’s `__init__()` method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance; for example: `super().__init__([args...])`.

Because [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 and `__init__()` work together in constructing objects (`__new__()` to create it, and `__init__()` to customize it), no non-`None` value may be returned by `__init__()`; doing so will cause a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 to be raised at runtime.

object.\_\_del\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__del__ "Link to this definition")

Called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor. If a base class has a `__del__()` method, the derived class’s `__del__()` method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.

It is possible (though not recommended!) for the `__del__()` method to postpone destruction of the instance by creating a new reference to it. This is called object _resurrection_. It is implementation-dependent whether `__del__()` is called a second time when a resurrected object is about to be destroyed; the current [CPython](https://docs.python.org/3/glossary.html#term-CPython)
 implementation only calls it once.

It is not guaranteed that `__del__()` methods are called for objects that still exist when the interpreter exits. [`weakref.finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize "weakref.finalize")
 provides a straightforward way to register a cleanup function to be called when an object is garbage collected.

Note

`del x` doesn’t directly call `x.__del__()` — the former decrements the reference count for `x` by one, and the latter is only called when `x`’s reference count reaches zero.

**CPython implementation detail:** It is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the [cyclic garbage collector](https://docs.python.org/3/glossary.html#term-garbage-collection)
. A common cause of reference cycles is when an exception has been caught in a local variable. The frame’s locals then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.

See also

Documentation for the [`gc`](https://docs.python.org/3/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.")
 module.

Warning

Due to the precarious circumstances under which `__del__()` methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to `sys.stderr` instead. In particular:

*   `__del__()` can be invoked when arbitrary code is being executed, including from any arbitrary thread. If `__del__()` needs to take a lock or invoke any other blocking resource, it may deadlock as the resource may already be taken by the code that gets interrupted to execute `__del__()`.
    
*   `__del__()` can be executed during interpreter shutdown. As a consequence, the global variables it needs to access (including other modules) may already have been deleted or set to `None`. Python guarantees that globals whose name begins with a single underscore are deleted from their module before other globals are deleted; if no other references to such globals exist, this may help in assuring that imported modules are still available at the time when the `__del__()` method is called.
    

object.\_\_repr\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "Link to this definition")

Called by the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 built-in function to compute the “official” string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string of the form `<...some useful description...>` should be returned. The return value must be a string object. If a class defines `__repr__()` but not [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__")
, then `__repr__()` is also used when an “informal” string representation of instances of that class is required.

This is typically used for debugging, so it is important that the representation is information-rich and unambiguous. A default implementation is provided by the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself.

object.\_\_str\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__str__ "Link to this definition")

Called by [`str(object)`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, the default [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__")
 implementation, and the built-in function [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
, to compute the “informal” or nicely printable string representation of an object. The return value must be a [str](https://docs.python.org/3/builtins/stdtypes.html#textseq)
 object.

This method differs from [`object.__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 in that there is no expectation that `__str__()` return a valid Python expression: a more convenient or concise representation can be used.

The default implementation defined by the built-in type [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 calls [`object.__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
.

object.\_\_bytes\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__bytes__ "Link to this definition")

Called by [bytes](https://docs.python.org/3/builtins/functions.html#func-bytes)
 to compute a byte-string representation of an object. This should return a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide this method.

object.\_\_format\_\_(_self_, _format\_spec_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__format__ "Link to this definition")

Called by the [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
 built-in function, and by extension, evaluation of [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
 and the [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
 method, to produce a “formatted” string representation of an object. The _format\_spec_ argument is a string that contains a description of the formatting options desired. The interpretation of the _format\_spec_ argument is up to the type implementing `__format__()`, however most classes will either delegate formatting to one of the built-in types, or use a similar formatting option syntax.

See [Format specification mini-language](https://docs.python.org/3/library/string.html#formatspec)
 for a description of the standard formatting syntax.

The return value must be a string object.

The default implementation by the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class should be given an empty _format\_spec_ string. It delegates to [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__")
.

Changed in version 3.4: The \_\_format\_\_ method of `object` itself raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if passed any non-empty string.

Changed in version 3.7: `object.__format__(x, '')` is now equivalent to `str(x)` rather than `format(str(x), '')`.

object.\_\_lt\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "Link to this definition")

object.\_\_le\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__le__ "Link to this definition")

object.\_\_eq\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "Link to this definition")

object.\_\_ne\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ne__ "Link to this definition")

object.\_\_gt\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__gt__ "Link to this definition")

object.\_\_ge\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ge__ "Link to this definition")

These are the so-called “rich comparison” methods. The correspondence between operator symbols and method names is as follows: `x<y` calls `x.__lt__(y)`, `x<=y` calls `x.__le__(y)`, `x==y` calls `x.__eq__(y)`, `x!=y` calls `x.__ne__(y)`, `x>y` calls `x.__gt__(y)`, and `x>=y` calls `x.__ge__(y)`.

A rich comparison method may return the singleton [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 if it does not implement the operation for a given pair of arguments. By convention, `False` and `True` are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context (e.g., in the condition of an `if` statement), Python will call [`bool()`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 on the value to determine if the result is true or false.

By default, `object` implements `__eq__()` by using `is`, returning [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 in the case of a false comparison: `True if x is y else NotImplemented`. For `__ne__()`, by default it delegates to `__eq__()` and inverts the result unless it is `NotImplemented`. There are no other implied relationships among the comparison operators or default implementations; for example, the truth of `(x<y or x==y)` does not imply `x<=y`. To automatically generate ordering operations from a single root operation, see [`@functools.total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
.

By default, the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class provides implementations consistent with [Value comparisons](https://docs.python.org/3/reference/expressions.html#expressions-value-comparisons)
: equality compares according to object identity, and order comparisons raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. Each default method may generate these results directly, but may also return [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
.

See the paragraph on [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 for some important notes on creating [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 objects which support custom comparison operations and are usable as dictionary keys.

There are no swapped-argument versions of these methods (to be used when the left argument does not support the operation but the right argument does); rather, `__lt__()` and `__gt__()` are each other’s reflection, `__le__()` and `__ge__()` are each other’s reflection, and `__eq__()` and `__ne__()` are their own reflection. If the operands are of different types, and the right operand’s type is a direct or indirect subclass of the left operand’s type, the reflected method of the right operand has priority, otherwise the left operand’s method has priority. Virtual subclassing is not considered.

When no appropriate method returns any value other than [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
, the `==` and `!=` operators will fall back to `is` and `is not`, respectively.

object.\_\_hash\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "Link to this definition")

Called by built-in function [`hash()`](https://docs.python.org/3/builtins/functions.html#hash "hash")
 and for operations on members of hashed collections including [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
, [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, and [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
. The `__hash__()` method should return an integer. The only required property is that objects which compare equal have the same hash value; it is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:

Copy

def \_\_hash\_\_(self):
    return hash((self.name, self.nick, self.color))

Note

[`hash()`](https://docs.python.org/3/builtins/functions.html#hash "hash")
 truncates the value returned from an object’s custom `__hash__()` method to the size of a [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
. This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds. If an object’s `__hash__()` must interoperate on builds of different bit sizes, be sure to check the width on all supported builds. An easy way to do this is with `python -c "import sys; print(sys.hash_info.width)"`.

If a class does not define an [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 method it should not define a `__hash__()` operation either; if it defines `__eq__()` but not `__hash__()`, its instances will not be usable as items in hashable collections. If a class defines mutable objects and implements an `__eq__()` method, it should not implement `__hash__()`, since the implementation of [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 collections requires that a key’s hash value is immutable (if the object’s hash value changes, it will be in the wrong hash bucket).

User-defined classes have [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 and `__hash__()` methods by default (inherited from the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class); with them, all objects compare unequal (except with themselves) and `x.__hash__()` returns an appropriate value such that `x == y` implies both that `x is y` and `hash(x) == hash(y)`.

A class that overrides [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 and does not define `__hash__()` will have its `__hash__()` implicitly set to `None`. When the `__hash__()` method of a class is `None`, instances of the class will raise an appropriate [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 when a program attempts to retrieve their hash value, and will also be correctly identified as unhashable when checking `isinstance(obj, collections.abc.Hashable)`.

If a class that overrides [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 needs to retain the implementation of `__hash__()` from a parent class, the interpreter must be told this explicitly by setting `__hash__ = <ParentClass>.__hash__`.

If a class that does not override [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 wishes to suppress hash support, it should include `__hash__ = None` in the class definition. A class which defines its own `__hash__()` that explicitly raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 would be incorrectly identified as hashable by an `isinstance(obj, collections.abc.Hashable)` call.

Note

By default, the `__hash__()` values of str and bytes objects are “salted” with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.

This is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict insertion, _O_(_n_2) complexity. See [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html)
 for details.

Changing hash values affects the iteration order of sets. Python has never made guarantees about this ordering (and it typically varies between 32-bit and 64-bit builds).

See also [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
.

Changed in version 3.3: Hash randomization is enabled by default.

object.\_\_bool\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "Link to this definition")

Called to implement truth value testing and the built-in operation `bool()`; should return `False` or `True`. When this method is not defined, [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
 is called, if it is defined, and the object is considered true if its result is nonzero. If a class defines neither `__len__()` nor `__bool__()` (which is true of the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself), all its instances are considered true.

### 3.3.2. Customizing attribute access[¶](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access "Link to this heading")

The following methods can be defined to customize the meaning of attribute access (use of, assignment to, or deletion of `x.name`) for class instances.

object.\_\_getattr\_\_(_self_, _name_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "Link to this definition")

Called when the default attribute access fails with an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 (either [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 raises an `AttributeError` because _name_ is not an instance attribute or an attribute in the class tree for `self`; or [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 of a _name_ property raises `AttributeError`). This method should either return the (computed) attribute value or raise an `AttributeError` exception. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide this method.

Note that if the attribute is found through the normal mechanism, `__getattr__()` is not called. (This is an intentional asymmetry between `__getattr__()` and [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__")
.) This is done both for efficiency reasons and because otherwise `__getattr__()` would have no way to access other attributes of the instance. Note that at least for instance variables, you can take total control by not inserting any values in the instance attribute dictionary (but instead inserting them in another object). See the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 method below for a way to actually get total control over attribute access.

object.\_\_getattribute\_\_(_self_, _name_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "Link to this definition")

Called unconditionally to implement attribute accesses for instances of the class. If the class also defines [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
, the latter will not be called unless `__getattribute__()` either calls it explicitly or raises an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
. This method should return the (computed) attribute value or raise an `AttributeError` exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, `object.__getattribute__(self, name)`.

Note

This method may still be bypassed when looking up special methods as the result of implicit invocation via language syntax or [built-in functions](https://docs.python.org/3/reference/datamodel.html#builtin-functions)
. See [Special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)
.

For certain sensitive attribute accesses, raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `object.__getattr__` with arguments `obj` and `name`.

object.\_\_setattr\_\_(_self_, _name_, _value_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "Link to this definition")

Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). _name_ is the attribute name, _value_ is the value to be assigned to it.

If `__setattr__()` wants to assign to an instance attribute, it should call the base class method with the same name, for example, `object.__setattr__(self, name, value)`.

For certain sensitive attribute assignments, raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `object.__setattr__` with arguments `obj`, `name`, `value`.

object.\_\_delattr\_\_(_self_, _name_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__delattr__ "Link to this definition")

Like [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__")
 but for attribute deletion instead of assignment. This should only be implemented if `del obj.name` is meaningful for the object.

For certain sensitive attribute deletions, raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `object.__delattr__` with arguments `obj` and `name`.

object.\_\_dir\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "Link to this definition")

Called when [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")
 is called on the object. An iterable must be returned. `dir()` converts the returned iterable to a list and sorts it.

#### 3.3.2.1. Customizing module attribute access[¶](https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access "Link to this heading")

module.\_\_getattr\_\_()[¶](https://docs.python.org/3/reference/datamodel.html#module.__getattr__ "Link to this definition")

module.\_\_dir\_\_()[¶](https://docs.python.org/3/reference/datamodel.html#module.__dir__ "Link to this definition")

Special names `__getattr__` and `__dir__` can be also used to customize access to module attributes. The `__getattr__` function at the module level should accept one argument which is the name of an attribute and return the computed value or raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
. If an attribute is not found on a module object through the normal lookup, i.e. [`object.__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
, then `__getattr__` is searched in the module `__dict__` before raising an `AttributeError`. If found, it is called with the attribute name and the result is returned.

The `__dir__` function should accept no arguments, and return an iterable of strings that represents the names accessible on module. If present, this function overrides the standard [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")
 search on a module.

module.\_\_class\_\_[¶](https://docs.python.org/3/reference/datamodel.html#module.__class__ "Link to this definition")

For a more fine grained customization of the module behavior (setting attributes, properties, etc.), one can set the `__class__` attribute of a module object to a subclass of [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
. For example:

Copy

import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def \_\_repr\_\_(self):
        return f'Verbose {self.\_\_name\_\_}'

    def \_\_setattr\_\_(self, attr, value):
        print(f'Setting {attr}...')
        super().\_\_setattr\_\_(attr, value)

sys.modules\[\_\_name\_\_\].\_\_class\_\_ \= VerboseModule

Note

Defining module `__getattr__` and setting module `__class__` only affect lookups made using the attribute access syntax – directly accessing the module globals (whether by code within the module, or via a reference to the module’s globals dictionary) is unaffected.

Changed in version 3.5: `__class__` module attribute is now writable.

Added in version 3.7: `__getattr__` and `__dir__` module attributes.

See also

[**PEP 562**](https://peps.python.org/pep-0562/)
 - Module \_\_getattr\_\_ and \_\_dir\_\_

Describes the `__getattr__` and `__dir__` functions on modules.

#### 3.3.2.2. Implementing Descriptors[¶](https://docs.python.org/3/reference/datamodel.html#implementing-descriptors "Link to this heading")

The following methods only apply when an instance of the class containing the method (a so-called _descriptor_ class) appears in an _owner_ class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not implement any of these protocols.

object.\_\_get\_\_(_self_, _instance_, _owner\=None_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__get__ "Link to this definition")

Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). The optional _owner_ argument is the owner class, while _instance_ is the instance that the attribute was accessed through, or `None` when the attribute is accessed through the _owner_.

This method should return the computed attribute value or raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 exception.

[**PEP 252**](https://peps.python.org/pep-0252/)
 specifies that `__get__()` is callable with one or two arguments. Python’s own built-in descriptors support this specification; however, it is likely that some third-party tools have descriptors that require both arguments. Python’s own [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 implementation always passes in both arguments whether they are required or not.

object.\_\_set\_\_(_self_, _instance_, _value_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__set__ "Link to this definition")

Called to set the attribute on an instance _instance_ of the owner class to a new value, _value_.

Note, adding `__set__()` or [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
 changes the kind of descriptor to a “data descriptor”. See [Invoking Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptor-invocation)
 for more details.

object.\_\_delete\_\_(_self_, _instance_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "Link to this definition")

Called to delete the attribute on an instance _instance_ of the owner class.

Instances of descriptors may also have the `__objclass__` attribute present:

object.\_\_objclass\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__objclass__ "Link to this definition")

The attribute `__objclass__` is interpreted by the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
 module as specifying the class where this object was defined (setting this appropriately can assist in runtime introspection of dynamic class attributes). For callables, it may indicate that an instance of the given type (or a subclass) is expected or required as the first positional argument (for example, CPython sets this attribute for unbound methods that are implemented in C).

#### 3.3.2.3. Invoking Descriptors[¶](https://docs.python.org/3/reference/datamodel.html#invoking-descriptors "Link to this heading")

In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol: [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
, [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
, and [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
. If any of those methods are defined for an object, it is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete the attribute from an object’s dictionary. For instance, `a.x` has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the base classes of `type(a)` excluding metaclasses.

However, if the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined and how they were called.

The starting point for descriptor invocation is a binding, `a.x`. How the arguments are assembled depends on `a`:

Direct Call

The simplest and least common call is when user code directly invokes a descriptor method: `x.__get__(a)`.

Instance Binding

If binding to an object instance, `a.x` is transformed into the call: `type(a).__dict__['x'].__get__(a, type(a))`.

Class Binding

If binding to a class, `A.x` is transformed into the call: `A.__dict__['x'].__get__(None, A)`.

Super Binding

A dotted lookup such as `super(A, a).x` searches `a.__class__.__mro__` for a base class `B` following `A` and then returns `B.__dict__['x'].__get__(a, A)`. If not a descriptor, `x` is returned unchanged.

For instance bindings, the precedence of descriptor invocation depends on which descriptor methods are defined. A descriptor can define any combination of [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
, [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 and [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
. If it does not define `__get__()`, then accessing the attribute will return the descriptor object itself unless there is a value in the object’s instance dictionary. If the descriptor defines `__set__()` and/or `__delete__()`, it is a data descriptor; if it defines neither, it is a non-data descriptor. Normally, data descriptors define both `__get__()` and `__set__()`, while non-data descriptors have just the `__get__()` method. Data descriptors with `__get__()` and `__set__()` (and/or `__delete__()`) defined always override a redefinition in an instance dictionary. In contrast, non-data descriptors can be overridden by instances.

Python methods (including those decorated with [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 and [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.

The [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
 decorator is implemented as a data descriptor. Accordingly, instances cannot override the behavior of a property.

#### 3.3.2.4. \_\_slots\_\_[¶](https://docs.python.org/3/reference/datamodel.html#slots "Link to this heading")

_\_\_slots\_\__ allow us to explicitly declare data members (like properties) and deny the creation of [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 and _\_\_weakref\_\__ (unless explicitly declared in _\_\_slots\_\__ or available in a parent.)

The space saved over using [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 can be significant. Attribute lookup speed can be significantly improved as well.

object.\_\_slots\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "Link to this definition")

This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. _\_\_slots\_\__ reserves space for the declared variables and prevents the automatic creation of [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 and _\_\_weakref\_\__ for each instance.

Notes on using _\_\_slots\_\__:

*   When inheriting from a class without _\_\_slots\_\__, the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
     and _\_\_weakref\_\__ attribute of the instances will always be accessible.
    
*   Without a [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
     variable, instances cannot be assigned new variables not listed in the _\_\_slots\_\__ definition. Attempts to assign to an unlisted variable name raises [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    . If dynamic assignment of new variables is desired, then add `'__dict__'` to the sequence of strings in the _\_\_slots\_\__ declaration.
    
*   Without a _\_\_weakref\_\__ variable for each instance, classes defining _\_\_slots\_\__ do not support [`weak references`](https://docs.python.org/3/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.")
     to its instances. If weak reference support is needed, then add `'__weakref__'` to the sequence of strings in the _\_\_slots\_\__ declaration.
    
*   _\_\_slots\_\__ are implemented at the class level by creating [descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)
     for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by _\_\_slots\_\__; otherwise, the class attribute would overwrite the descriptor assignment.
    
*   The action of a _\_\_slots\_\__ declaration is not limited to the class where it is defined. _\_\_slots\_\__ declared in parents are available in child classes. However, instances of a child subclass will get a [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
     and _\_\_weakref\_\__ unless the subclass also defines _\_\_slots\_\__ (which should only contain names of any _additional_ slots).
    
*   If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the program undefined. In the future, a check may be added to prevent this.
    
*   [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     will be raised if _\_\_slots\_\__ other than _\_\_dict\_\__ and _\_\_weakref\_\__ are defined for a class derived from a [`"variable-length" built-in type`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
     such as [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
    , [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , and [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
    , except [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
    .
    
*   Any non-string [iterable](https://docs.python.org/3/glossary.html#term-iterable)
     may be assigned to _\_\_slots\_\__.
    
*   If a [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
     is used to assign _\_\_slots\_\__, the dictionary keys will be used as the slot names. The values of the dictionary can be used to provide per-attribute docstrings that will be recognised by [`inspect.getdoc()`](https://docs.python.org/3/library/inspect.html#inspect.getdoc "inspect.getdoc")
     and displayed in the output of [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
    .
    
*   [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__")
     assignment works only if both classes have the same _\_\_slots\_\__.
    
*   [Multiple inheritance](https://docs.python.org/3/reference/compound_stmts.html#multiple-inheritance)
     with multiple slotted parent classes can be used, but only one parent is allowed to have attributes created by slots (the other bases must have empty slot layouts) - violations raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    .
    
*   If an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
     is used for _\_\_slots\_\__ then a [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
     is created for each of the iterator’s values. However, the _\_\_slots\_\__ attribute will be an empty iterator.
    

Changed in version 3.15: Allowed defining the _\_\_dict\_\__ and _\_\_weakref\_\__ _\_\_slots\_\__ for any class. Allowed defining any _\_\_slots\_\__ for a class derived from [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
.

### 3.3.3. Customizing class creation[¶](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation "Link to this heading")

Whenever a class inherits from another class, [`__init_subclass__()`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__")
 is called on the parent class. This way, it is possible to write classes which change the behavior of subclasses. This is closely related to class decorators, but where class decorators only affect the specific class they’re applied to, `__init_subclass__` solely applies to future subclasses of the class defining the method.

classmethod object.\_\_init\_subclass\_\_(_cls_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__ "Link to this definition")

This method is called whenever the containing class is subclassed. _cls_ is then the new subclass. If defined as a normal instance method, this method is implicitly converted to a class method.

Keyword arguments which are given to a new class are passed to the parent class’s `__init_subclass__`. For compatibility with other classes using `__init_subclass__`, one should take out the needed keyword arguments and pass the others over to the base class, as in:

Copy

class Philosopher:
    def \_\_init\_subclass\_\_(cls, /, default\_name, \*\*kwargs):
        super().\_\_init\_subclass\_\_(\*\*kwargs)
        cls.default\_name \= default\_name

class AustralianPhilosopher(Philosopher, default\_name\="Bruce"):
    pass

The default implementation `object.__init_subclass__` does nothing, but raises an error if it is called with any arguments.

Note

The metaclass hint `metaclass` is consumed by the rest of the type machinery, and is never passed to `__init_subclass__` implementations. The actual metaclass (rather than the explicit hint) can be accessed as `type(cls)`.

Added in version 3.6.

When a class is created, `type.__new__()` scans the class variables and makes callbacks to those with a [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
 hook.

object.\_\_set\_name\_\_(_self_, _owner_, _name_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "Link to this definition")

Automatically called at the time the owning class _owner_ is created. The object has been assigned to _name_ in that class:

Copy

class A:
    x \= C()  \# Automatically calls: x.\_\_set\_name\_\_(A, 'x')

If the class variable is assigned after the class is created, `__set_name__()` will not be called automatically. If needed, `__set_name__()` can be called directly:

Copy

class A:
   pass

c \= C()
A.x \= c                  \# The hook is not called
c.\_\_set\_name\_\_(A, 'x')   \# Manually invoke the hook

See [Creating the class object](https://docs.python.org/3/reference/datamodel.html#class-object-creation)
 for more details.

Added in version 3.6.

#### 3.3.3.1. Metaclasses[¶](https://docs.python.org/3/reference/datamodel.html#metaclasses "Link to this heading")

By default, classes are constructed using [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
. The class body is executed in a new namespace and the class name is bound locally to the result of `type(name, bases, namespace)`.

The class creation process can be customized by passing the `metaclass` keyword argument in the class definition line, or by inheriting from an existing class that included such an argument. In the following example, both `MyClass` and `MySubclass` are instances of `Meta`:

Copy

class Meta(type):
    pass

class MyClass(metaclass\=Meta):
    pass

class MySubclass(MyClass):
    pass

Any other keyword arguments that are specified in the class definition are passed through to all metaclass operations described below.

When a class definition is executed, the following steps occur:

*   MRO entries are resolved;
    
*   the appropriate metaclass is determined;
    
*   the class namespace is prepared;
    
*   the class body is executed;
    
*   the class object is created.
    

#### 3.3.3.2. Resolving MRO entries[¶](https://docs.python.org/3/reference/datamodel.html#resolving-mro-entries "Link to this heading")

object.\_\_mro\_entries\_\_(_self_, _bases_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "Link to this definition")

If a base that appears in a class definition is not an instance of [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
, then an `__mro_entries__()` method is searched on the base. If an `__mro_entries__()` method is found, the base is substituted with the result of a call to `__mro_entries__()` when creating the class. The method is called with the original bases tuple passed to the _bases_ parameter, and must return a tuple of classes that will be used instead of the base. The returned tuple may be empty: in these cases, the original base is ignored.

See also

[`types.resolve_bases()`](https://docs.python.org/3/library/types.html#types.resolve_bases "types.resolve_bases")

Dynamically resolve bases that are not instances of [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
.

[`types.get_original_bases()`](https://docs.python.org/3/library/types.html#types.get_original_bases "types.get_original_bases")

Retrieve a class’s “original bases” prior to modifications by [`__mro_entries__()`](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__")
.

[**PEP 560**](https://peps.python.org/pep-0560/)

Core support for typing module and generic types.

#### 3.3.3.3. Determining the appropriate metaclass[¶](https://docs.python.org/3/reference/datamodel.html#determining-the-appropriate-metaclass "Link to this heading")

The appropriate metaclass for a class definition is determined as follows:

*   if no bases and no explicit metaclass are given, then [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
     is used;
    
*   if an explicit metaclass is given and it is _not_ an instance of [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
    , then it is used directly as the metaclass;
    
*   if an instance of [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
     is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used.
    

The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e. `type(cls)`) of all specified base classes. The most derived metaclass is one which is a subtype of _all_ of these candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail with `TypeError`.

#### 3.3.3.4. Preparing the class namespace[¶](https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace "Link to this heading")

Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has a `__prepare__` attribute, it is called as `namespace = metaclass.__prepare__(name, bases, **kwds)` (where the additional keyword arguments, if any, come from the class definition). The `__prepare__` method should be implemented as a [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
. The namespace returned by `__prepare__` is passed in to `__new__`, but when the final class object is created the namespace is copied into a new `dict`.

If the metaclass has no `__prepare__` attribute, then the class namespace is initialised as an empty ordered mapping.

See also

[**PEP 3115**](https://peps.python.org/pep-3115/)
 - Metaclasses in Python 3000

Introduced the `__prepare__` namespace hook

#### 3.3.3.5. Executing the class body[¶](https://docs.python.org/3/reference/datamodel.html#executing-the-class-body "Link to this heading")

The class body is executed (approximately) as `exec(body, globals(), namespace)`. The key difference from a normal call to [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 is that lexical scoping allows the class body (including any methods) to reference names from the current and outer scopes when the class definition occurs inside a function.

However, even when the class definition occurs inside the function, methods defined inside the class still cannot see names defined at the class scope. Class variables must be accessed through the first parameter of instance or class methods, or through the implicit lexically scoped `__class__` reference described in the next section.

#### 3.3.3.6. Creating the class object[¶](https://docs.python.org/3/reference/datamodel.html#creating-the-class-object "Link to this heading")

Once the class namespace has been populated by executing the class body, the class object is created by calling `metaclass(name, bases, namespace, **kwds)` (the additional keywords passed here are the same as those passed to `__prepare__`).

This class object is the one that will be referenced by the zero-argument form of [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
. `__class__` is an implicit closure reference created by the compiler if any methods in a class body refer to either `__class__` or `super`. This allows the zero argument form of `super()` to correctly identify the class being defined based on lexical scoping, while the class or instance that was used to make the current call is identified based on the first argument passed to the method.

**CPython implementation detail:** In CPython 3.6 and later, the `__class__` cell is passed to the metaclass as a `__classcell__` entry in the class namespace. If present, this must be propagated up to the `type.__new__` call in order for the class to be initialised correctly. Failing to do so will result in a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 in Python 3.8.

When using the default metaclass [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
, or any metaclass that ultimately calls `type.__new__`, the following additional customization steps are invoked after creating the class object:

1.  The `type.__new__` method collects all of the attributes in the class namespace that define a [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
     method;
    
2.  Those `__set_name__` methods are called with the class being defined and the assigned name of that particular attribute;
    
3.  The [`__init_subclass__()`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__")
     hook is called on the immediate parent of the new class in its method resolution order.
    

After the class object is created, it is passed to the class decorators included in the class definition (if any) and the resulting object is bound in the local namespace as the defined class.

When a new class is created by `type.__new__`, the object provided as the namespace parameter is copied to a new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which becomes the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
 attribute of the class object.

See also

[**PEP 3135**](https://peps.python.org/pep-3135/)
 - New super

Describes the implicit `__class__` closure reference

#### 3.3.3.7. Uses for metaclasses[¶](https://docs.python.org/3/reference/datamodel.html#uses-for-metaclasses "Link to this heading")

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization.

### 3.3.4. Customizing instance and subclass checks[¶](https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks "Link to this heading")

The following methods are used to override the default behavior of the [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 built-in functions.

In particular, the metaclass [`abc.ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
 implements these methods in order to allow the addition of Abstract Base Classes (ABCs) as “virtual base classes” to any class or type (including built-in types), including other ABCs.

type.\_\_instancecheck\_\_(_self_, _instance_)[¶](https://docs.python.org/3/reference/datamodel.html#type.__instancecheck__ "Link to this definition")

Return true if _instance_ should be considered a (direct or indirect) instance of _class_. If defined, called to implement `isinstance(instance, class)`.

type.\_\_subclasscheck\_\_(_self_, _subclass_)[¶](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__ "Link to this definition")

Return true if _subclass_ should be considered a (direct or indirect) subclass of _class_. If defined, called to implement `issubclass(subclass, class)`.

Note that these methods are looked up on the type (metaclass) of a class. They cannot be defined as class methods in the actual class. This is consistent with the lookup of special methods that are called on instances, only in this case the instance is itself a class.

See also

[**PEP 3119**](https://peps.python.org/pep-3119/)
 - Introducing Abstract Base Classes

Includes the specification for customizing [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 behavior through [`__instancecheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__instancecheck__ "type.__instancecheck__")
 and [`__subclasscheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__ "type.__subclasscheck__")
, with motivation for this functionality in the context of adding Abstract Base Classes (see the [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
 module) to the language.

### 3.3.5. Emulating generic types[¶](https://docs.python.org/3/reference/datamodel.html#emulating-generic-types "Link to this heading")

When using [type annotations](https://docs.python.org/3/glossary.html#term-annotation)
, it is often useful to _parameterize_ a [generic type](https://docs.python.org/3/glossary.html#term-generic-type)
 using Python’s square-brackets notation. For example, the annotation `list[int]` might be used to signify a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 in which all the elements are of type [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
.

See also

[**PEP 484**](https://peps.python.org/pep-0484/)
 - Type Hints

Introducing Python’s framework for type annotations

[Generic Alias Types](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)

Documentation for objects representing parameterized generic classes

[Generics](https://docs.python.org/3/library/typing.html#generics)
, [user-defined generics](https://docs.python.org/3/library/typing.html#user-defined-generics)
 and [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")

Documentation on how to implement generic classes that can be parameterized at runtime and understood by static type-checkers.

A class can _generally_ only be parameterized if it defines the special class method `__class_getitem__()`.

classmethod object.\_\_class\_getitem\_\_(_cls_, _key_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "Link to this definition")

Return an object representing the specialization of a generic class by type arguments found in _key_.

When defined on a class, `__class_getitem__()` is automatically a class method. As such, there is no need for it to be decorated with [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 when it is defined.

#### 3.3.5.1. The purpose of _\_\_class\_getitem\_\__[¶](https://docs.python.org/3/reference/datamodel.html#the-purpose-of-class-getitem "Link to this heading")

The purpose of [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 is to allow runtime parameterization of standard-library generic classes in order to more easily apply [type hints](https://docs.python.org/3/glossary.html#term-type-hint)
 to these classes.

To implement custom generic classes that can be parameterized at runtime and understood by static type-checkers, users should either inherit from a standard library class that already implements [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
, or inherit from [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")
, which has its own implementation of `__class_getitem__()`.

Custom implementations of [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 on classes defined outside of the standard library may not be understood by third-party type-checkers such as mypy. Using `__class_getitem__()` on any class for purposes other than type hinting is discouraged.

#### 3.3.5.2. _\_\_class\_getitem\_\__ versus _\_\_getitem\_\__[¶](https://docs.python.org/3/reference/datamodel.html#class-getitem-versus-getitem "Link to this heading")

Usually, the [subscription](https://docs.python.org/3/reference/expressions.html#subscriptions)
 of an object using square brackets will call the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 instance method defined on the object’s class. However, if the object being subscribed is itself a class, the class method [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 may be called instead. `__class_getitem__()` should return a [GenericAlias](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 object if it is properly defined.

Presented with the [expression](https://docs.python.org/3/glossary.html#term-expression)
 `obj[x]`, the Python interpreter follows something like the following process to decide whether [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 or [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 should be called:

Copy

from inspect import isclass

def subscribe(obj, x):
    """Return the result of the expression 'obj\[x\]'"""

    class\_of\_obj \= type(obj)

    \# If the class of obj defines \_\_getitem\_\_,
    \# call class\_of\_obj.\_\_getitem\_\_(obj, x)
    if hasattr(class\_of\_obj, '\_\_getitem\_\_'):
        return class\_of\_obj.\_\_getitem\_\_(obj, x)

    \# Else, if obj is a class and defines \_\_class\_getitem\_\_,
    \# call obj.\_\_class\_getitem\_\_(x)
    elif isclass(obj) and hasattr(obj, '\_\_class\_getitem\_\_'):
        return obj.\_\_class\_getitem\_\_(x)

    \# Else, raise an exception
    else:
        raise TypeError(
            f"'{class\_of\_obj.\_\_name\_\_}' object is not subscriptable"
        )

In Python, all classes are themselves instances of other classes. The class of a class is known as that class’s [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)
, and most classes have the [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 class as their metaclass. `type` does not define [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, meaning that expressions such as `list[int]`, `dict[str, float]` and `tuple[str, bytes]` all result in [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 being called:

Copy

\>>> \# list has class "type" as its metaclass, like most classes:
\>>> type(list)
<class 'type'>
\>>> type(dict) \== type(list) \== type(tuple) \== type(str) \== type(bytes)
True
\>>> \# "list\[int\]" calls "list.\_\_class\_getitem\_\_(int)"
\>>> list\[int\]
list\[int\]
\>>> \# list.\_\_class\_getitem\_\_ returns a GenericAlias object:
\>>> type(list\[int\])
<class 'types.GenericAlias'>

However, if a class has a custom metaclass that defines [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, subscribing the class may result in different behaviour. An example of this can be found in the [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
 module:

Copy

\>>> from enum import Enum
\>>> class Menu(Enum):
... """A breakfast menu"""
...     SPAM \= 'spam'
...     BACON \= 'bacon'
...
\>>> \# Enum classes have a custom metaclass:
\>>> type(Menu)
<class 'enum.EnumMeta'>
\>>> \# EnumMeta defines \_\_getitem\_\_,
\>>> \# so \_\_class\_getitem\_\_ is not called,
\>>> \# and the result is not a GenericAlias object:
\>>> Menu\['SPAM'\]
<Menu.SPAM: 'spam'>
\>>> type(Menu\['SPAM'\])
<enum 'Menu'>

See also

[**PEP 560**](https://peps.python.org/pep-0560/)
 - Core Support for typing module and generic types

Introducing [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
, and outlining when a [subscription](https://docs.python.org/3/reference/expressions.html#subscriptions)
 results in `__class_getitem__()` being called instead of [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")

### 3.3.6. Emulating callable objects[¶](https://docs.python.org/3/reference/datamodel.html#emulating-callable-objects "Link to this heading")

object.\_\_call\_\_(_self_\[, _args..._\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__call__ "Link to this definition")

Called when the instance is “called” as a function; if this method is defined, `x(arg1, arg2, ...)` roughly translates to `type(x).__call__(x, arg1, ...)`. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide this method.

### 3.3.7. Emulating container types[¶](https://docs.python.org/3/reference/datamodel.html#emulating-container-types "Link to this heading")

The following methods can be defined to implement container objects. None of them are provided by the [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself. Containers usually are [sequences](https://docs.python.org/3/glossary.html#term-sequence)
 (such as [`lists`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 or [`tuples`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
) or [mappings](https://docs.python.org/3/glossary.html#term-mapping)
 (like [dictionaries](https://docs.python.org/3/glossary.html#term-dictionary)
), but can represent other containers as well. The first set of methods is used either to emulate a sequence or to emulate a mapping; the difference is that for a sequence, the allowable keys should be the integers _k_ for which `0 <= k < N` where _N_ is the length of the sequence, or [`slice`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 objects, which define a range of items. It is also recommended that mappings provide the methods `keys()`, `values()`, `items()`, `get()`, `clear()`, `setdefault()`, `pop()`, `popitem()`, `copy()`, and `update()` behaving similar to those for Python’s standard [`dictionary`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 objects. The [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
 module provides a [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping")
 [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 to help create those methods from a base set of [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
, [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__")
, and `keys()`.

Mutable sequences should provide methods [`append()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.append "sequence.append")
, [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.clear "sequence.clear")
, [`count()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.count "sequence.count")
, [`extend()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.extend "sequence.extend")
, [`index()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.index "sequence.index")
, [`insert()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.insert "sequence.insert")
, [`pop()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.pop "sequence.pop")
, [`remove()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.remove "sequence.remove")
, and [`reverse()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.reverse "sequence.reverse")
, like Python standard [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 objects. Finally, sequence types should implement addition (meaning concatenation) and multiplication (meaning repetition) by defining the methods [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
, [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__")
, [`__iadd__()`](https://docs.python.org/3/reference/datamodel.html#object.__iadd__ "object.__iadd__")
, [`__mul__()`](https://docs.python.org/3/reference/datamodel.html#object.__mul__ "object.__mul__")
, [`__rmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmul__ "object.__rmul__")
 and [`__imul__()`](https://docs.python.org/3/reference/datamodel.html#object.__imul__ "object.__imul__")
 described below; they should not define other numerical operators.

It is recommended that both mappings and sequences implement the [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 method to allow efficient use of the `in` operator; for mappings, `in` should search the mapping’s keys; for sequences, it should search through the values. It is further recommended that both mappings and sequences implement the [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
 method to allow efficient iteration through the container; for mappings, `__iter__()` should iterate through the object’s keys; for sequences, it should iterate through the values.

object.\_\_len\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__len__ "Link to this definition")

Called to implement the built-in function [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
. Should return the length of the object, an integer `>=` 0. Also, an object that doesn’t define a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
 method and whose `__len__()` method returns zero is considered to be false in a Boolean context.

**CPython implementation detail:** In CPython, the length is required to be at most [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize")
. If the length is larger than `sys.maxsize` some features (such as [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
) may raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
. To prevent raising `OverflowError` by truth value testing, an object must define a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
 method.

object.\_\_length\_hint\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__ "Link to this definition")

Called to implement [`operator.length_hint()`](https://docs.python.org/3/library/operator.html#operator.length_hint "operator.length_hint")
. Should return an estimated length for the object (which may be greater or less than the actual length). The length must be an integer `>=` 0. The return value may also be [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
, which is treated the same as if the `__length_hint__` method didn’t exist at all. This method is purely an optimization and is never required for correctness.

Added in version 3.4.

object.\_\_getitem\_\_(_self_, _subscript_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "Link to this definition")

Called to implement _subscription_, that is, `self[subscript]`. See [Subscriptions and slicings](https://docs.python.org/3/reference/expressions.html#subscriptions)
 for details on the syntax.

There are two types of built-in objects that support subscription via `__getitem__()`:

*   **sequences**, where _subscript_ (also called [index](https://docs.python.org/3/glossary.html#term-index)
    ) should be an integer or a [`slice`](https://docs.python.org/3/builtins/functions.html#slice "slice")
     object. See the [sequence documentation](https://docs.python.org/3/reference/datamodel.html#datamodel-sequences)
     for the expected behavior, including handling `slice` objects and negative indices.
    
*   **mappings**, where _subscript_ is also called the [key](https://docs.python.org/3/glossary.html#term-key)
    . See [mapping documentation](https://docs.python.org/3/reference/datamodel.html#datamodel-mappings)
     for the expected behavior.
    

If _subscript_ is of an inappropriate type, `__getitem__()` should raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. If _subscript_ has an inappropriate value, `__getitem__()` should raise an [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
 or one of its subclasses ([`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 for sequences; [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 for mappings).

Note

Slicing is handled by `__getitem__()`, [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
, and [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__")
. A call like

Copy

a\[1:2\] \= b

is translated to

Copy

a\[slice(1, 2, None)\] \= b

and so forth. Missing slice items are always filled in with `None`.

Note

The sequence iteration protocol (used, for example, in [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
 loops), expects that an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 will be raised for illegal indexes to allow proper detection of the end of a sequence.

Note

When [subscripting](https://docs.python.org/3/reference/expressions.html#subscriptions)
 a _class_, the special class method [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
 may be called instead of `__getitem__()`. See [\_\_class\_getitem\_\_ versus \_\_getitem\_\_](https://docs.python.org/3/reference/datamodel.html#classgetitem-versus-getitem)
 for more details.

object.\_\_setitem\_\_(_self_, _key_, _value_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "Link to this definition")

Called to implement assignment to `self[key]`. Same note as for [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
. This should only be implemented for mappings if the objects support changes to the values for keys, or if new keys can be added, or for sequences if elements can be replaced. The same exceptions should be raised for improper _key_ values as for the `__getitem__()` method.

object.\_\_delitem\_\_(_self_, _key_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "Link to this definition")

Called to implement deletion of `self[key]`. Same note as for [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
. This should only be implemented for mappings if the objects support removal of keys, or for sequences if elements can be removed from the sequence. The same exceptions should be raised for improper _key_ values as for the `__getitem__()` method.

object.\_\_missing\_\_(_self_, _key_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__missing__ "Link to this definition")

Called by [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
.[`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 to implement `self[key]` for dict subclasses when key is not in the dictionary.

object.\_\_iter\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "Link to this definition")

This method is called when an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 is required for a container. This method should return a new iterator object that can iterate over all the objects in the container. For mappings, it should iterate over the keys of the container.

object.\_\_reversed\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__reversed__ "Link to this definition")

Called (if present) by the [`reversed()`](https://docs.python.org/3/builtins/functions.html#reversed "reversed")
 built-in to implement reverse iteration. It should return a new iterator object that iterates over all the objects in the container in reverse order.

If the `__reversed__()` method is not provided, the [`reversed()`](https://docs.python.org/3/builtins/functions.html#reversed "reversed")
 built-in will fall back to using the sequence protocol ([`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
 and [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
). Objects that support the sequence protocol should only provide `__reversed__()` if they can provide an implementation that is more efficient than the one provided by `reversed()`.

The membership test operators ([`in`](https://docs.python.org/3/reference/expressions.html#in)
 and [`not in`](https://docs.python.org/3/reference/expressions.html#not-in)
) are normally implemented as an iteration through a container. However, container objects can supply the following special method with a more efficient implementation, which also does not require the object be iterable.

object.\_\_contains\_\_(_self_, _item_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "Link to this definition")

Called to implement membership test operators. Should return true if _item_ is in _self_, false otherwise. For mapping objects, this should consider the keys of the mapping rather than the values or the key-item pairs.

For objects that don’t define `__contains__()`, the membership test first tries iteration via [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
, then the old sequence iteration protocol via [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, see [this section in the language reference](https://docs.python.org/3/reference/expressions.html#membership-test-details)
.

### 3.3.8. Emulating numeric types[¶](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types "Link to this heading")

The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

object.\_\_add\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__add__ "Link to this definition")

object.\_\_sub\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__sub__ "Link to this definition")

object.\_\_mul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__mul__ "Link to this definition")

object.\_\_matmul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__matmul__ "Link to this definition")

object.\_\_truediv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__truediv__ "Link to this definition")

object.\_\_floordiv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__floordiv__ "Link to this definition")

object.\_\_mod\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__mod__ "Link to this definition")

object.\_\_divmod\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__divmod__ "Link to this definition")

object.\_\_pow\_\_(_self_, _other_\[, _modulo_\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__pow__ "Link to this definition")

object.\_\_lshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__lshift__ "Link to this definition")

object.\_\_rshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rshift__ "Link to this definition")

object.\_\_and\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__and__ "Link to this definition")

object.\_\_xor\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__xor__ "Link to this definition")

object.\_\_or\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__or__ "Link to this definition")

These methods are called to implement the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
, [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
, `**`, `<<`, `>>`, `&`, `^`, `|`). For instance, to evaluate the expression `x + y`, where _x_ is an instance of a class that has an `__add__()` method, `type(x).__add__(x, y)` is called. The `__divmod__()` method should be the equivalent to using `__floordiv__()` and `__mod__()`; it should not be related to `__truediv__()`. Note that `__pow__()` should be defined to accept an optional third argument if the three-argument version of the built-in `pow()` function is to be supported.

If one of those methods does not support the operation with the supplied arguments, it should return [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
.

object.\_\_radd\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "Link to this definition")

object.\_\_rsub\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rsub__ "Link to this definition")

object.\_\_rmul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rmul__ "Link to this definition")

object.\_\_rmatmul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rmatmul__ "Link to this definition")

object.\_\_rtruediv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rtruediv__ "Link to this definition")

object.\_\_rfloordiv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rfloordiv__ "Link to this definition")

object.\_\_rmod\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rmod__ "Link to this definition")

object.\_\_rdivmod\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rdivmod__ "Link to this definition")

object.\_\_rpow\_\_(_self_, _other_\[, _modulo_\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__rpow__ "Link to this definition")

object.\_\_rlshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rlshift__ "Link to this definition")

object.\_\_rrshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rrshift__ "Link to this definition")

object.\_\_rand\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rand__ "Link to this definition")

object.\_\_rxor\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__rxor__ "Link to this definition")

object.\_\_ror\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ror__ "Link to this definition")

These methods are called to implement the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
, [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
, `**`, `<<`, `>>`, `&`, `^`, `|`) with reflected (swapped) operands. These functions are only called if the operands are of different types, when the left operand does not support the corresponding operation [\[3\]](https://docs.python.org/3/reference/datamodel.html#id22)
, or the right operand’s class is derived from the left operand’s class. [\[4\]](https://docs.python.org/3/reference/datamodel.html#id23)
 For instance, to evaluate the expression `x - y`, where _y_ is an instance of a class that has an `__rsub__()` method, `type(y).__rsub__(y, x)` is called if `type(x).__sub__(x, y)` returns [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 or `type(y)` is a subclass of `type(x)`. [\[5\]](https://docs.python.org/3/reference/datamodel.html#id24)

Note that `__rpow__()` should be defined to accept an optional third argument if the three-argument version of the built-in [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
 function is to be supported.

Changed in version 3.14: Three-argument [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
 now try calling `__rpow__()` if necessary. Previously it was only called in two-argument `pow()` and the binary power operator.

Note

If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different implementation of the reflected method for the operation, this method will be called before the left operand’s non-reflected method. This behavior allows subclasses to override their ancestors’ operations.

object.\_\_iadd\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__iadd__ "Link to this definition")

object.\_\_isub\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__isub__ "Link to this definition")

object.\_\_imul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__imul__ "Link to this definition")

object.\_\_imatmul\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__imatmul__ "Link to this definition")

object.\_\_itruediv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__itruediv__ "Link to this definition")

object.\_\_ifloordiv\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ifloordiv__ "Link to this definition")

object.\_\_imod\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__imod__ "Link to this definition")

object.\_\_ipow\_\_(_self_, _other_\[, _modulo_\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__ipow__ "Link to this definition")

object.\_\_ilshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ilshift__ "Link to this definition")

object.\_\_irshift\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__irshift__ "Link to this definition")

object.\_\_iand\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__iand__ "Link to this definition")

object.\_\_ixor\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ixor__ "Link to this definition")

object.\_\_ior\_\_(_self_, _other_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ior__ "Link to this definition")

These methods are called to implement the augmented arithmetic assignments (`+=`, `-=`, `*=`, `@=`, `/=`, `//=`, `%=`, `**=`, `<<=`, `>>=`, `&=`, `^=`, `|=`). These methods should attempt to do the operation in-place (modifying _self_) and return the result (which could be, but does not have to be, _self_). If a specific method is not defined, or if that method returns [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
, the augmented assignment falls back to the normal methods. For instance, if _x_ is an instance of a class with an `__iadd__()` method, `x += y` is equivalent to `x = x.__iadd__(y)` . If `__iadd__()` does not exist, or if `x.__iadd__(y)` returns `NotImplemented`, `x.__add__(y)` and `y.__radd__(x)` are considered, as with the evaluation of `x + y`. In certain situations, augmented assignment can result in unexpected errors (see [Why does a\_tuple\[i\] += \[‘item’\] raise an exception when the addition works?](https://docs.python.org/3/faq/programming.html#faq-augmented-assignment-tuple-error)
), but this behavior is in fact part of the data model.

object.\_\_neg\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__neg__ "Link to this definition")

object.\_\_pos\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__pos__ "Link to this definition")

object.\_\_abs\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__abs__ "Link to this definition")

object.\_\_invert\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__invert__ "Link to this definition")

Called to implement the unary arithmetic operations (`-`, `+`, [`abs()`](https://docs.python.org/3/builtins/functions.html#abs "abs")
 and `~`).

object.\_\_complex\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "Link to this definition")

object.\_\_int\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__int__ "Link to this definition")

object.\_\_float\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__float__ "Link to this definition")

Called to implement the built-in functions [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
, [`int()`](https://docs.python.org/3/builtins/functions.html#int "int")
 and [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
. Should return a value of the appropriate type.

object.\_\_index\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__index__ "Link to this definition")

Called to implement [`operator.index()`](https://docs.python.org/3/library/operator.html#operator.index "operator.index")
, and whenever Python needs to losslessly convert the numeric object to an integer object (such as in slicing, or in the built-in [`bin()`](https://docs.python.org/3/builtins/functions.html#bin "bin")
, [`hex()`](https://docs.python.org/3/builtins/functions.html#hex "hex")
 and [`oct()`](https://docs.python.org/3/builtins/functions.html#oct "oct")
 functions). Presence of this method indicates that the numeric object is an integer type. Must return an integer.

If [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
, [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__")
 and [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 are not defined then corresponding built-in functions [`int()`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float()`](https://docs.python.org/3/builtins/functions.html#float "float")
 and [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 fall back to `__index__()`.

object.\_\_round\_\_(_self_\[, _ndigits_\])[¶](https://docs.python.org/3/reference/datamodel.html#object.__round__ "Link to this definition")

object.\_\_trunc\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__trunc__ "Link to this definition")

object.\_\_floor\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__floor__ "Link to this definition")

object.\_\_ceil\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__ceil__ "Link to this definition")

Called to implement the built-in function [`round()`](https://docs.python.org/3/builtins/functions.html#round "round")
 and [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 functions [`trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc")
, [`floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor")
 and [`ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
. Unless _ndigits_ is passed to `__round__()` all these methods should return the value of the object truncated to an [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral")
 (typically an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
).

Changed in version 3.14: [`int()`](https://docs.python.org/3/builtins/functions.html#int "int")
 no longer delegates to the `__trunc__()` method.

### 3.3.9. With Statement Context Managers[¶](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers "Link to this heading")

A _context manager_ is an object that defines the runtime context to be established when executing a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the `with` statement (described in section [The with statement](https://docs.python.org/3/reference/compound_stmts.html#with)
), but can also be used by directly invoking their methods.

Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.

For more information on context managers, see [Context Manager Types](https://docs.python.org/3/builtins/stdtypes.html#typecontextmanager)
. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide the context manager methods.

object.\_\_enter\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "Link to this definition")

Enter the runtime context related to this object. The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement will bind this method’s return value to the target(s) specified in the `as` clause of the statement, if any.

object.\_\_exit\_\_(_self_, _exc\_type_, _exc\_value_, _traceback_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "Link to this definition")

Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
.

If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.

Note that `__exit__()` methods should not reraise the passed-in exception; this is the caller’s responsibility.

See also

[**PEP 343**](https://peps.python.org/pep-0343/)
 - The “with” statement

The specification, background, and examples for the Python [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

### 3.3.10. Customizing positional arguments in class pattern matching[¶](https://docs.python.org/3/reference/datamodel.html#customizing-positional-arguments-in-class-pattern-matching "Link to this heading")

When using a class name in a pattern, positional arguments in the pattern are not allowed by default, i.e. `case MyClass(x, y)` is typically invalid without special support in `MyClass`. To be able to use that kind of pattern, the class needs to define a _\_\_match\_args\_\__ attribute.

object.\_\_match\_args\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__match_args__ "Link to this definition")

This class variable can be assigned a tuple of strings. When this class is used in a class pattern with positional arguments, each positional argument will be converted into a keyword argument, using the corresponding value in _\_\_match\_args\_\__ as the keyword. The absence of this attribute is equivalent to setting it to `()`.

For example, if `MyClass.__match_args__` is `("left", "center", "right")` that means that `case MyClass(x, y)` is equivalent to `case MyClass(left=x, center=y)`. Note that the number of arguments in the pattern must be smaller than or equal to the number of elements in _\_\_match\_args\_\__; if it is larger, the pattern match attempt will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

Added in version 3.10.

See also

[**PEP 634**](https://peps.python.org/pep-0634/)
 - Structural Pattern Matching

The specification for the Python `match` statement.

### 3.3.11. Emulating buffer types[¶](https://docs.python.org/3/reference/datamodel.html#emulating-buffer-types "Link to this heading")

The [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 provides a way for Python objects to expose efficient access to a low-level memory array. This protocol is implemented by builtin types such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
, and third-party libraries may define additional buffer types.

While buffer types are usually implemented in C, it is also possible to implement the protocol in Python.

object.\_\_buffer\_\_(_self_, _flags_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__buffer__ "Link to this definition")

Called when a buffer is requested from _self_ (for example, by the [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 constructor). The _flags_ argument is an integer representing the kind of buffer requested, affecting for example whether the returned buffer is read-only or writable. [`inspect.BufferFlags`](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags "inspect.BufferFlags")
 provides a convenient way to interpret the flags. The method must return a `memoryview` object.

**Thread safety:** In [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 Python, implementations must manage any internal export counter using atomic operations. The method must be safe to call concurrently from multiple threads, and the returned buffer’s underlying data must remain valid until the corresponding [`__release_buffer__()`](https://docs.python.org/3/reference/datamodel.html#object.__release_buffer__ "object.__release_buffer__")
 call completes. See [Thread safety for memoryview objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-memoryview)
 for details.

object.\_\_release\_buffer\_\_(_self_, _buffer_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__release_buffer__ "Link to this definition")

Called when a buffer is no longer needed. The _buffer_ argument is a [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 object that was previously returned by [`__buffer__()`](https://docs.python.org/3/reference/datamodel.html#object.__buffer__ "object.__buffer__")
. The method must release any resources associated with the buffer. This method should return `None`.

**Thread safety:** In [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 Python, any export counter decrement must use atomic operations. Resource cleanup must be thread-safe, as the final release may race with concurrent releases from other threads.

Buffer objects that do not need to perform any cleanup are not required to implement this method.

Added in version 3.12.

See also

[**PEP 688**](https://peps.python.org/pep-0688/)
 - Making the buffer protocol accessible in Python

Introduces the Python `__buffer__` and `__release_buffer__` methods.

[`collections.abc.Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")

ABC for buffer types.

### 3.3.12. Annotations[¶](https://docs.python.org/3/reference/datamodel.html#annotations "Link to this heading")

Functions, classes, and modules may contain [annotations](https://docs.python.org/3/glossary.html#term-annotation)
, which are a way to associate information (usually [type hints](https://docs.python.org/3/glossary.html#term-type-hint)
) with a symbol.

object.\_\_annotations\_\_[¶](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "Link to this definition")

This attribute contains the annotations for an object. It is [lazily evaluated](https://docs.python.org/3/reference/executionmodel.html#lazy-evaluation)
, so accessing the attribute may execute arbitrary code and raise exceptions. If evaluation is successful, the attribute is set to a dictionary mapping from variable names to annotations.

Changed in version 3.14: Annotations are now lazily evaluated.

object.\_\_annotate\_\_(_format_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "Link to this definition")

An [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function)
. Returns a new dictionary object mapping attribute/parameter names to their annotation values.

Takes a format parameter specifying the format in which annotations values should be provided. It must be a member of the [`annotationlib.Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format")
 enum, or an integer with a value corresponding to a member of the enum.

If an annotate function doesn’t support the requested format, it must raise [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
. Annotate functions must always support [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE")
 format; they must not raise [`NotImplementedError()`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 when called with this format.

When called with [`VALUE`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.VALUE "annotationlib.Format.VALUE")
 format, an annotate function may raise [`NameError`](https://docs.python.org/3/builtins/exceptions.html#NameError "NameError")
; it must not raise `NameError` when called requesting any other format.

If an object does not have any annotations, [`__annotate__`](https://docs.python.org/3/reference/datamodel.html#object.__annotate__ "object.__annotate__")
 should preferably be set to `None` (it can’t be deleted), rather than set to a function that returns an empty dict.

Added in version 3.14.

See also

[**PEP 649**](https://peps.python.org/pep-0649/)
 — Deferred evaluation of annotation using descriptors

Introduces lazy evaluation of annotations and the `__annotate__` function.

### 3.3.13. Special method lookup[¶](https://docs.python.org/3/reference/datamodel.html#special-method-lookup "Link to this heading")

For custom classes, implicit invocations of special methods are only guaranteed to work correctly if defined on an object’s type, not in the object’s instance dictionary. That behaviour is the reason why the following code raises an exception:

Copy

\>>> class C:
...     pass
...
\>>> c \= C()
\>>> c.\_\_len\_\_ \= lambda: 5
\>>> len(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()

The rationale behind this behaviour lies with a number of special methods such as [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 that are implemented by all objects, including type objects. If the implicit lookup of these methods used the conventional lookup process, they would fail when invoked on the type object itself:

Copy

\>>> 1 .\_\_hash\_\_() \== hash(1)
True
\>>> int.\_\_hash\_\_() \== hash(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor '\_\_hash\_\_' of 'int' object needs an argument

Incorrectly attempting to invoke an unbound method of a class in this way is sometimes referred to as ‘metaclass confusion’, and is avoided by bypassing the instance when looking up special methods:

Copy

\>>> type(1).\_\_hash\_\_(1) \== hash(1)
True
\>>> type(int).\_\_hash\_\_(int) \== hash(int)
True

In addition to bypassing any instance attributes in the interest of correctness, implicit special method lookup generally also bypasses the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 method even of the object’s metaclass:

Copy

\>>> class Meta(type):
...     def \_\_getattribute\_\_(\*args):
...         print("Metaclass getattribute invoked")
...         return type.\_\_getattribute\_\_(\*args)
...
\>>> class C(object, metaclass\=Meta):
...     def \_\_len\_\_(self):
...         return 10
...     def \_\_getattribute\_\_(\*args):
...         print("Class getattribute invoked")
...         return object.\_\_getattribute\_\_(\*args)
...
\>>> c \= C()
\>>> c.\_\_len\_\_()                 \# Explicit lookup via instance
Class getattribute invoked
10
\>>> type(c).\_\_len\_\_(c)          \# Explicit lookup via type
Metaclass getattribute invoked
10
\>>> len(c)                      \# Implicit lookup
10

Bypassing the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 machinery in this fashion provides significant scope for speed optimisations within the interpreter, at the cost of some flexibility in the handling of special methods (the special method _must_ be set on the class object itself in order to be consistently invoked by the interpreter).

3.4. Coroutines[¶](https://docs.python.org/3/reference/datamodel.html#coroutines "Link to this heading")

---------------------------------------------------------------------------------------------------------

### 3.4.1. Awaitable Objects[¶](https://docs.python.org/3/reference/datamodel.html#awaitable-objects "Link to this heading")

An [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 object generally implements an [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 method. [Coroutine objects](https://docs.python.org/3/glossary.html#term-coroutine)
 returned from [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions are awaitable.

Note

The [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)
 objects returned from generators decorated with [`types.coroutine()`](https://docs.python.org/3/library/types.html#types.coroutine "types.coroutine")
 are also awaitable, but they do not implement [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
.

object.\_\_await\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__await__ "Link to this definition")

Must return an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
. Should be used to implement [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 objects. For instance, [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 implements this method to be compatible with the [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expression. The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself is not awaitable and does not provide this method.

Note

The language doesn’t place any restriction on the type or value of the objects yielded by the iterator returned by `__await__`, as this is specific to the implementation of the asynchronous execution framework (e.g. [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
) that will be managing the [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 object.

Added in version 3.5.

See also

[**PEP 492**](https://peps.python.org/pep-0492/)
 for additional information about awaitable objects.

### 3.4.2. Coroutine Objects[¶](https://docs.python.org/3/reference/datamodel.html#coroutine-objects "Link to this heading")

[Coroutine objects](https://docs.python.org/3/glossary.html#term-coroutine)
 are [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 objects. A coroutine’s execution can be controlled by calling [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 and iterating over the result. When the coroutine has finished executing and returns, the iterator raises [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, and the exception’s [`value`](https://docs.python.org/3/builtins/exceptions.html#StopIteration.value "StopIteration.value")
 attribute holds the return value. If the coroutine raises an exception, it is propagated by the iterator. Coroutines should not directly raise unhandled `StopIteration` exceptions.

Coroutines also have the methods listed below, which are analogous to those of generators (see [Generator iterators](https://docs.python.org/3/builtins/stdtypes.html#generator-methods)
). However, unlike generators, coroutines do not directly support iteration.

Coroutines are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the types of their yield, send, and return values, respectively.

Changed in version 3.5.2: It is a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 to await on a coroutine more than once.

coroutine.send(_value_)[¶](https://docs.python.org/3/reference/datamodel.html#coroutine.send "Link to this definition")

Starts or resumes execution of the coroutine. If _value_ is `None`, this is equivalent to advancing the iterator returned by [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
. If _value_ is not `None`, this method delegates to the [`send()`](https://docs.python.org/3/builtins/stdtypes.html#generator.send "generator.send")
 method of the iterator that caused the coroutine to suspend. The result (return value, [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, or other exception) is the same as when iterating over the `__await__()` return value, described above.

coroutine.throw(_value_)[¶](https://docs.python.org/3/reference/datamodel.html#coroutine.throw "Link to this definition")

coroutine.throw(_type_\[, _value_\[, _traceback_\]\])

Raises the specified exception in the coroutine. This method delegates to the [`throw()`](https://docs.python.org/3/builtins/stdtypes.html#generator.throw "generator.throw")
 method of the iterator that caused the coroutine to suspend, if it has such a method. Otherwise, the exception is raised at the suspension point. The result (return value, [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, or other exception) is the same as when iterating over the [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 return value, described above. If the exception is not caught in the coroutine, it propagates back to the caller.

Changed in version 3.12: The second signature (type\[, value\[, traceback\]\]) is deprecated and may be removed in a future version of Python.

coroutine.close()[¶](https://docs.python.org/3/reference/datamodel.html#coroutine.close "Link to this definition")

Causes the coroutine to clean itself up and exit. If the coroutine is suspended, this method first delegates to the [`close()`](https://docs.python.org/3/builtins/stdtypes.html#generator.close "generator.close")
 method of the iterator that caused the coroutine to suspend, if it has such a method. Then it raises [`GeneratorExit`](https://docs.python.org/3/builtins/exceptions.html#GeneratorExit "GeneratorExit")
 at the suspension point, causing the coroutine to immediately clean itself up. Finally, the coroutine is marked as having finished executing, even if it was never started.

Coroutine objects are automatically closed using the above process when they are about to be destroyed.

### 3.4.3. Asynchronous Iterators[¶](https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators "Link to this heading")

An _asynchronous iterator_ can call asynchronous code in its `__anext__` method.

Asynchronous iterators can be used in an [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 statement.

The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide these methods.

object.\_\_aiter\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__aiter__ "Link to this definition")

Must return an _asynchronous iterator_ object.

object.\_\_anext\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "Link to this definition")

Must return an _awaitable_ resulting in a next value of the iterator. Should raise a [`StopAsyncIteration`](https://docs.python.org/3/builtins/exceptions.html#StopAsyncIteration "StopAsyncIteration")
 error when the iteration is over.

An example of an asynchronous iterable object:

Copy

class Reader:
    async def readline(self):
        ...

    def \_\_aiter\_\_(self):
        return self

    async def \_\_anext\_\_(self):
        val \= await self.readline()
        if val \== b'':
            raise StopAsyncIteration
        return val

Added in version 3.5.

Changed in version 3.7: Prior to Python 3.7, [`__aiter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aiter__ "object.__aiter__")
 could return an _awaitable_ that would resolve to an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
.

Starting with Python 3.7, [`__aiter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aiter__ "object.__aiter__")
 must return an asynchronous iterator object. Returning anything else will result in a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 error.

### 3.4.4. Asynchronous Context Managers[¶](https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers "Link to this heading")

An _asynchronous context manager_ is a _context manager_ that is able to suspend execution in its `__aenter__` and `__aexit__` methods.

Asynchronous context managers can be used in an [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statement.

The [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 class itself does not provide these methods.

object.\_\_aenter\_\_(_self_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "Link to this definition")

Semantically similar to [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
, the only difference being that it must return an _awaitable_.

object.\_\_aexit\_\_(_self_, _exc\_type_, _exc\_value_, _traceback_)[¶](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "Link to this definition")

Semantically similar to [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
, the only difference being that it must return an _awaitable_.

An example of an asynchronous context manager class:

Copy

class AsyncContextManager:
    async def \_\_aenter\_\_(self):
        await log('entering context')

    async def \_\_aexit\_\_(self, exc\_type, exc, tb):
        await log('exiting context')

Added in version 3.5.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [3\. Data model](https://docs.python.org/3/reference/datamodel.html#)
    *   [3.1. Objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
        
    *   [3.2. The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
        *   [3.2.1. None](https://docs.python.org/3/reference/datamodel.html#none)
            
        *   [3.2.2. NotImplemented](https://docs.python.org/3/reference/datamodel.html#notimplemented)
            
        *   [3.2.3. Ellipsis](https://docs.python.org/3/reference/datamodel.html#ellipsis)
            
        *   [3.2.4. `numbers.Number`](https://docs.python.org/3/reference/datamodel.html#numbers-number)
            *   [3.2.4.1. `numbers.Integral`](https://docs.python.org/3/reference/datamodel.html#numbers-integral)
                
            *   [3.2.4.2. `numbers.Real` (`float`)](https://docs.python.org/3/reference/datamodel.html#numbers-real-float)
                
            *   [3.2.4.3. `numbers.Complex` (`complex`)](https://docs.python.org/3/reference/datamodel.html#numbers-complex-complex)
                
        *   [3.2.5. Sequences](https://docs.python.org/3/reference/datamodel.html#sequences)
            *   [3.2.5.1. Immutable sequences](https://docs.python.org/3/reference/datamodel.html#immutable-sequences)
                
            *   [3.2.5.2. Mutable sequences](https://docs.python.org/3/reference/datamodel.html#mutable-sequences)
                
        *   [3.2.6. Set types](https://docs.python.org/3/reference/datamodel.html#set-types)
            
        *   [3.2.7. Mappings](https://docs.python.org/3/reference/datamodel.html#mappings)
            *   [3.2.7.1. Dictionaries](https://docs.python.org/3/reference/datamodel.html#dictionaries)
                
            *   [3.2.7.2. Frozen dictionaries](https://docs.python.org/3/reference/datamodel.html#frozen-dictionaries)
                
        *   [3.2.8. Callable types](https://docs.python.org/3/reference/datamodel.html#callable-types)
            *   [3.2.8.1. User-defined functions](https://docs.python.org/3/reference/datamodel.html#user-defined-functions)
                *   [3.2.8.1.1. Special read-only attributes](https://docs.python.org/3/reference/datamodel.html#special-read-only-attributes)
                    
                *   [3.2.8.1.2. Special writable attributes](https://docs.python.org/3/reference/datamodel.html#special-writable-attributes)
                    
            *   [3.2.8.2. Instance methods](https://docs.python.org/3/reference/datamodel.html#instance-methods)
                
            *   [3.2.8.3. Generator functions](https://docs.python.org/3/reference/datamodel.html#generator-functions)
                
            *   [3.2.8.4. Coroutine functions](https://docs.python.org/3/reference/datamodel.html#coroutine-functions)
                
            *   [3.2.8.5. Asynchronous generator functions](https://docs.python.org/3/reference/datamodel.html#asynchronous-generator-functions)
                
            *   [3.2.8.6. Built-in functions](https://docs.python.org/3/reference/datamodel.html#built-in-functions)
                
            *   [3.2.8.7. Built-in methods](https://docs.python.org/3/reference/datamodel.html#built-in-methods)
                
            *   [3.2.8.8. Classes](https://docs.python.org/3/reference/datamodel.html#classes)
                
            *   [3.2.8.9. Class Instances](https://docs.python.org/3/reference/datamodel.html#class-instances)
                
        *   [3.2.9. Modules](https://docs.python.org/3/reference/datamodel.html#modules)
            *   [3.2.9.1. Import-related attributes on module objects](https://docs.python.org/3/reference/datamodel.html#import-related-attributes-on-module-objects)
                
            *   [3.2.9.2. Other writable attributes on module objects](https://docs.python.org/3/reference/datamodel.html#other-writable-attributes-on-module-objects)
                
            *   [3.2.9.3. Module dictionaries](https://docs.python.org/3/reference/datamodel.html#module-dictionaries)
                
        *   [3.2.10. Custom classes](https://docs.python.org/3/reference/datamodel.html#custom-classes)
            *   [3.2.10.1. Special attributes](https://docs.python.org/3/reference/datamodel.html#special-attributes)
                
            *   [3.2.10.2. Special methods](https://docs.python.org/3/reference/datamodel.html#special-methods)
                
        *   [3.2.11. Class instances](https://docs.python.org/3/reference/datamodel.html#id4)
            *   [3.2.11.1. Special attributes](https://docs.python.org/3/reference/datamodel.html#id5)
                
        *   [3.2.12. I/O objects (also known as file objects)](https://docs.python.org/3/reference/datamodel.html#i-o-objects-also-known-as-file-objects)
            
        *   [3.2.13. Internal types](https://docs.python.org/3/reference/datamodel.html#internal-types)
            *   [3.2.13.1. Code objects](https://docs.python.org/3/reference/datamodel.html#code-objects)
                *   [3.2.13.1.1. Special read-only attributes](https://docs.python.org/3/reference/datamodel.html#index-64)
                    
                *   [3.2.13.1.2. Methods on code objects](https://docs.python.org/3/reference/datamodel.html#methods-on-code-objects)
                    
            *   [3.2.13.2. Frame objects](https://docs.python.org/3/reference/datamodel.html#frame-objects)
                *   [3.2.13.2.1. Special read-only attributes](https://docs.python.org/3/reference/datamodel.html#index-70)
                    
                *   [3.2.13.2.2. Special writable attributes](https://docs.python.org/3/reference/datamodel.html#index-71)
                    
                *   [3.2.13.2.3. Frame object methods](https://docs.python.org/3/reference/datamodel.html#frame-object-methods)
                    
            *   [3.2.13.3. Traceback objects](https://docs.python.org/3/reference/datamodel.html#traceback-objects)
                
            *   [3.2.13.4. Slice objects](https://docs.python.org/3/reference/datamodel.html#slice-objects)
                
            *   [3.2.13.5. Static method objects](https://docs.python.org/3/reference/datamodel.html#static-method-objects)
                
            *   [3.2.13.6. Class method objects](https://docs.python.org/3/reference/datamodel.html#class-method-objects)
                
    *   [3.3. Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
        *   [3.3.1. Basic customization](https://docs.python.org/3/reference/datamodel.html#basic-customization)
            
        *   [3.3.2. Customizing attribute access](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access)
            *   [3.3.2.1. Customizing module attribute access](https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access)
                
            *   [3.3.2.2. Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html#implementing-descriptors)
                
            *   [3.3.2.3. Invoking Descriptors](https://docs.python.org/3/reference/datamodel.html#invoking-descriptors)
                
            *   [3.3.2.4. \_\_slots\_\_](https://docs.python.org/3/reference/datamodel.html#slots)
                
        *   [3.3.3. Customizing class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation)
            *   [3.3.3.1. Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
                
            *   [3.3.3.2. Resolving MRO entries](https://docs.python.org/3/reference/datamodel.html#resolving-mro-entries)
                
            *   [3.3.3.3. Determining the appropriate metaclass](https://docs.python.org/3/reference/datamodel.html#determining-the-appropriate-metaclass)
                
            *   [3.3.3.4. Preparing the class namespace](https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace)
                
            *   [3.3.3.5. Executing the class body](https://docs.python.org/3/reference/datamodel.html#executing-the-class-body)
                
            *   [3.3.3.6. Creating the class object](https://docs.python.org/3/reference/datamodel.html#creating-the-class-object)
                
            *   [3.3.3.7. Uses for metaclasses](https://docs.python.org/3/reference/datamodel.html#uses-for-metaclasses)
                
        *   [3.3.4. Customizing instance and subclass checks](https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks)
            
        *   [3.3.5. Emulating generic types](https://docs.python.org/3/reference/datamodel.html#emulating-generic-types)
            *   [3.3.5.1. The purpose of _\_\_class\_getitem\_\__](https://docs.python.org/3/reference/datamodel.html#the-purpose-of-class-getitem)
                
            *   [3.3.5.2. _\_\_class\_getitem\_\__ versus _\_\_getitem\_\__](https://docs.python.org/3/reference/datamodel.html#class-getitem-versus-getitem)
                
        *   [3.3.6. Emulating callable objects](https://docs.python.org/3/reference/datamodel.html#emulating-callable-objects)
            
        *   [3.3.7. Emulating container types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)
            
        *   [3.3.8. Emulating numeric types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
            
        *   [3.3.9. With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers)
            
        *   [3.3.10. Customizing positional arguments in class pattern matching](https://docs.python.org/3/reference/datamodel.html#customizing-positional-arguments-in-class-pattern-matching)
            
        *   [3.3.11. Emulating buffer types](https://docs.python.org/3/reference/datamodel.html#emulating-buffer-types)
            
        *   [3.3.12. Annotations](https://docs.python.org/3/reference/datamodel.html#annotations)
            
        *   [3.3.13. Special method lookup](https://docs.python.org/3/reference/datamodel.html#special-method-lookup)
            
    *   [3.4. Coroutines](https://docs.python.org/3/reference/datamodel.html#coroutines)
        *   [3.4.1. Awaitable Objects](https://docs.python.org/3/reference/datamodel.html#awaitable-objects)
            
        *   [3.4.2. Coroutine Objects](https://docs.python.org/3/reference/datamodel.html#coroutine-objects)
            
        *   [3.4.3. Asynchronous Iterators](https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators)
            
        *   [3.4.4. Asynchronous Context Managers](https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers)
            

#### Previous topic

[2\. Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html "previous chapter")

#### Next topic

[4\. Execution model](https://docs.python.org/3/reference/executionmodel.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=3.+Data+model&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fdatamodel.html&pagesource=reference%2Fdatamodel.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/datamodel.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/executionmodel.html "4. Execution model")
     |
*   [previous](https://docs.python.org/3/reference/lexical_analysis.html "2. Lexical analysis")
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
*   [3\. Data model](https://docs.python.org/3/reference/datamodel.html)
    
*    
    
    |
*   Theme Auto Light Dark |