[Skip to main content](https://numpy.org/doc/stable/user/basics.ufuncs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.ufuncs.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.ufuncs.html)
[2.4](https://numpy.org/doc/2.4/user/basics.ufuncs.html)
[2.3](https://numpy.org/doc/2.3/user/basics.ufuncs.html)
[2.2](https://numpy.org/doc/2.2/user/basics.ufuncs.html)
[2.1](https://numpy.org/doc/2.1/user/basics.ufuncs.html)
[2.0](https://numpy.org/doc/2.0/user/basics.ufuncs.html)
[1.26](https://numpy.org/doc/1.26/user/basics.ufuncs.html)
[1.25](https://numpy.org/doc/1.25/user/basics.ufuncs.html)
[1.24](https://numpy.org/doc/1.24/user/basics.ufuncs.html)
[1.23](https://numpy.org/doc/1.23/user/basics.ufuncs.html)
[1.22](https://numpy.org/doc/1.22/user/basics.ufuncs.html)
[1.21](https://numpy.org/doc/1.21/user/basics.ufuncs.html)
[1.20](https://numpy.org/doc/1.20/user/basics.ufuncs.html)
[1.19](https://numpy.org/doc/1.19/user/basics.ufuncs.html)
[1.18](https://numpy.org/doc/1.18/user/basics.ufuncs.html)
[1.17](https://numpy.org/doc/1.17/user/basics.ufuncs.html)
[1.16](https://numpy.org/doc/1.16/user/basics.ufuncs.html)
[1.15](https://numpy.org/doc/1.15/user/basics.ufuncs.html)
[1.14](https://numpy.org/doc/1.14/user/basics.ufuncs.html)
[1.13](https://numpy.org/doc/1.13/user/basics.ufuncs.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Universal functions ([`ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
) basics[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#universal-functions-ufunc-basics "Link to this heading")

======================================================================================================================================================================================================================================================

See also

[Universal functions (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs)

A universal function (or [ufunc](https://numpy.org/doc/stable/glossary.html#term-ufunc)
 for short) is a function that operates on [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in an element-by-element fashion, supporting [array broadcasting](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-broadcasting)
, [type casting](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-casting)
, and several other standard features. That is, a ufunc is a “[vectorized](https://numpy.org/doc/stable/glossary.html#term-vectorization)
” wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs.

There are also [generalized ufuncs](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#c-api-generalized-ufuncs)
 which are functions over vectors (or arrays) instead of single-element scalars. For example, [`numpy.add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")
 is a ufunc that operates element-by-element, while [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
 is a gufunc that operates on vectors/matrices:

\>>> a \= np.arange(6).reshape(3, 2)
\>>> a
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\]\])
\>>> np.add(a, a)  \# element-wise addition
array(\[\[ 0,  2\],\
       \[ 4,  6\],\
       \[ 8, 10\]\])
\>>> np.matmul(a, a.T)  \# matrix multiplication (3x2) @ (2x3) -> (3x3)
array(\[\[ 1,  3,  5\],\
       \[ 3, 13, 23\],\
       \[ 5, 23, 41\]\])

Copy to clipboard

In NumPy, universal functions are instances of the [`numpy.ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
 class. Many of the built-in functions are implemented in compiled C code. The basic ufuncs operate on scalars, but there is also a generalized kind for which the basic elements are sub-arrays (vectors, matrices, etc.), and broadcasting is done over other dimensions. The simplest example is the addition operator:

\>>> np.array(\[0,2,3,4\]) + np.array(\[1,1,\-1,2\])
array(\[1, 3, 2, 6\])

Copy to clipboard

One can also produce custom [`numpy.ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
 instances using the [`numpy.frompyfunc`](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#numpy.frompyfunc "numpy.frompyfunc")
 factory function.

Ufunc methods[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufunc-methods "Link to this heading")

------------------------------------------------------------------------------------------------------------

All ufuncs have 5 methods. 4 reduce-like methods ([`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
, [`accumulate`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#numpy.ufunc.accumulate "numpy.ufunc.accumulate")
, [`reduceat`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "numpy.ufunc.reduceat")
, [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "numpy.ufunc.outer")
) and one for inplace operations ([`at`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at")
). See [Methods](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-methods)
 for more. However, these methods only make sense on ufuncs that take two input arguments and return one output argument (so-called “scalar” ufuncs since the inner loop operates on a single scalar value). Attempting to call these methods on other ufuncs will cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

For example, [`numpy.add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")
 takes two inputs and returns one output, so its methods work:

\>>> np.add.reduce(\[1, 2, 3\])
6

Copy to clipboard

But [`numpy.divmod`](https://numpy.org/doc/stable/reference/generated/numpy.divmod.html#numpy.divmod "numpy.divmod")
 returns two outputs (quotient and remainder), so calling its methods raises an error:

\>>> np.divmod.reduce(\[1, 2, 3\])
Traceback (most recent call last):
    ...
ValueError: reduce only supported for functions returning a single value

Copy to clipboard

The reduce-like methods all take an _axis_ keyword, a _dtype_ keyword, and an _out_ keyword, and the arrays must all have dimension >= 1. The _axis_ keyword specifies the axis of the array over which the reduction will take place (with negative values counting backwards). Generally, it is an integer, though for [`numpy.ufunc.reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
, it can also be a tuple of `int` to reduce over several axes at once, or `None`, to reduce over all axes. For example:

\>>> x \= np.arange(9).reshape(3,3)
\>>> x
array(\[\[0, 1, 2\],\
      \[3, 4, 5\],\
      \[6, 7, 8\]\])
\>>> np.add.reduce(x, 1)
array(\[ 3, 12, 21\])
\>>> np.add.reduce(x, (0, 1))
36

Copy to clipboard

The _dtype_ keyword allows you to manage a very common problem that arises when naively using [`ufunc.reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
. Sometimes you may have an array of a certain data type and wish to add up all of its elements, but the result does not fit into the data type of the array. This commonly happens if you have an array of single-byte integers. The _dtype_ keyword allows you to alter the data type over which the reduction takes place (and therefore the type of the output). Thus, you can ensure that the output is a data type with precision large enough to handle your output. The responsibility of altering the reduce type is mostly up to you. There is one exception: if no _dtype_ is given for a reduction on the “add” or “multiply” operations, then if the input type is an integer (or Boolean) data-type and smaller than the size of the [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 data type, it will be internally upcast to the [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 (or [`numpy.uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint")
) data-type. In the previous example:

\>>> x.dtype
dtype('int64')
\>>> np.multiply.reduce(x, dtype\=np.float64)
array(\[ 0., 28., 80.\])

Copy to clipboard

Finally, the _out_ keyword allows you to provide an output array (or a tuple of output arrays for multi-output ufuncs). If _out_ is given, the _dtype_ argument is only used for the internal computations. Considering `x` from the previous example:

\>>> y \= np.zeros(3, dtype\=np.int\_)
\>>> y
array(\[0, 0, 0\])
\>>> np.multiply.reduce(x, dtype\=np.float64, out\=y)
array(\[ 0, 28, 80\])

Copy to clipboard

Ufuncs also have a fifth method, [`numpy.ufunc.at`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at")
, that allows in place operations to be performed using advanced indexing. No [buffering](https://numpy.org/doc/stable/user/basics.ufuncs.html#use-of-internal-buffers)
 is used on the dimensions where advanced indexing is used, so the advanced index can list an item more than once and the operation will be performed on the result of the previous operation for that item.

Output type determination[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#output-type-determination "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

If the input arguments of the ufunc (or its methods) are [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, then the output will be as well. The exception is when the result is zero-dimensional, in which case the output will be converted to an _array scalar_. This can be avoided by passing in `out=...` or `out=Ellipsis`.

If some or all of the input arguments are not [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, then the output may not be an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 either. Indeed, if any input defines an [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
 method, control will be passed completely to that function, i.e., the ufunc is [overridden](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-overrides)
.

If none of the inputs overrides the ufunc, then all output arrays will be passed to the [`__array_wrap__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__")
 method of the input (besides [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, and scalars) that defines it **and** has the highest [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 of any other input to the universal function. The default [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 of the ndarray is 0.0, and the default [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 of a subtype is 0.0. Matrices have [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 equal to 10.0.

All ufuncs can also take output arguments which must be arrays or subclasses. If necessary, the result will be cast to the data-type(s) of the provided output array(s). If the output has an [`__array_wrap__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__")
 method it is called instead of the one found on the inputs.

Broadcasting[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#broadcasting "Link to this heading")

----------------------------------------------------------------------------------------------------------

See also

[Broadcasting basics](https://numpy.org/doc/stable/user/basics.broadcasting.html)

Each universal function takes array inputs and produces array outputs by performing the core function element-wise on the inputs (where an element is generally a scalar, but can be a vector or higher-order sub-array for generalized ufuncs). Standard [broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules)
 are applied so that inputs not sharing exactly the same shapes can still be usefully operated on.

By these rules, if an input has a dimension size of 1 in its shape, the first data entry in that dimension will be used for all calculations along that dimension. In other words, the stepping machinery of the [ufunc](https://numpy.org/doc/stable/glossary.html#term-ufunc)
 will simply not step along that dimension (the [stride](https://numpy.org/doc/stable/reference/arrays.ndarray.html#memory-layout)
 will be 0 for that dimension).

Type casting rules[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#type-casting-rules "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Note

In NumPy 1.6.0, a type promotion API was created to encapsulate the mechanism for determining output types. See the functions [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
, [`numpy.promote_types`](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types")
, and [`numpy.min_scalar_type`](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#numpy.min_scalar_type "numpy.min_scalar_type")
 for more details.

At the core of every ufunc is a one-dimensional strided loop that implements the actual function for a specific type combination. When a ufunc is created, it is given a static list of inner loops and a corresponding list of type signatures over which the ufunc operates. The ufunc machinery uses this list to determine which inner loop to use for a particular case. You can inspect the [`.types`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#numpy.ufunc.types "numpy.ufunc.types")
 attribute for a particular ufunc to see which type combinations have a defined inner loop and which output type they produce ([character codes](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars-character-codes)
 are used in said output for brevity).

Casting must be done on one or more of the inputs whenever the ufunc does not have a core loop implementation for the input types provided. If an implementation for the input types cannot be found, then the algorithm searches for an implementation with a type signature to which all of the inputs can be cast “safely.” The first one it finds in its internal list of loops is selected and performed, after all necessary type casting. Recall that internal copies during ufuncs (even for casting) are limited to the size of an internal buffer (which is user settable).

Note

Universal functions in NumPy are flexible enough to have mixed type signatures. Thus, for example, a universal function could be defined that works with floating-point and integer values. See [`numpy.ldexp`](https://numpy.org/doc/stable/reference/generated/numpy.ldexp.html#numpy.ldexp "numpy.ldexp")
 for an example.

By the above description, the casting rules are essentially implemented by the question of when a data type can be cast “safely” to another data type. The answer to this question can be determined in Python with a function call: [`can_cast(fromtype, totype)`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")
. The example below shows the results of this call for the 24 internally supported types on the author’s 64-bit system. You can generate this table for your system with the code given in the example.

Example

Code segment showing the “can cast safely” table for a 64-bit system. Generally the output depends on the system; your system might result in a different table.

\>>> mark \= {False: ' -', True: ' Y'}
\>>> def print\_table(ntypes):
...     print('X ' + ' '.join(ntypes))
...     for row in ntypes:
...         print(row, end\='')
...         for col in ntypes:
...             print(mark\[np.can\_cast(row, col)\], end\='')
...         print()
...
\>>> print\_table(np.typecodes\['All'\])
X ? b h i l q n p B H I L Q N P e f d g F D G S U V O M m
? Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
b - Y Y Y Y Y Y Y - - - - - - - Y Y Y Y Y Y Y Y Y Y Y - Y
h - - Y Y Y Y Y Y - - - - - - - - Y Y Y Y Y Y Y Y Y Y - Y
i - - - Y Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
l - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
q - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
n - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
p - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
B - - Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
H - - - Y Y Y Y Y - Y Y Y Y Y Y - Y Y Y Y Y Y Y Y Y Y - Y
I - - - - Y Y Y Y - - Y Y Y Y Y - - Y Y - Y Y Y Y Y Y - Y
L - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
Q - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
N - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
P - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
e - - - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y Y - -
f - - - - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y - -
d - - - - - - - - - - - - - - - - - Y Y - Y Y Y Y Y Y - -
g - - - - - - - - - - - - - - - - - - Y - - Y Y Y Y Y - -
F - - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y Y - -
D - - - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y - -
G - - - - - - - - - - - - - - - - - - - - - Y Y Y Y Y - -
S - - - - - - - - - - - - - - - - - - - - - - Y Y Y Y - -
U - - - - - - - - - - - - - - - - - - - - - - - Y Y Y - -
V - - - - - - - - - - - - - - - - - - - - - - - - Y Y - -
O - - - - - - - - - - - - - - - - - - - - - - - - - Y - -
M - - - - - - - - - - - - - - - - - - - - - - - - Y Y Y -
m - - - - - - - - - - - - - - - - - - - - - - - - Y Y - Y

Copy to clipboard

You should note that, while included in the table for completeness, the ‘S’, ‘U’, and ‘V’ types cannot be operated on by ufuncs. Also, note that on a 32-bit system the integer types may have different sizes, resulting in a slightly altered table.

Mixed scalar-array operations use a different set of casting rules that ensure that a scalar cannot “upcast” an array unless the scalar is of a fundamentally different kind of data (i.e., under a different hierarchy in the data-type hierarchy) than the array. This rule enables you to use scalar constants in your code (which, as Python types, are interpreted accordingly in ufuncs) without worrying about whether the precision of the scalar constant will cause upcasting on your large (small precision) array.

Use of internal buffers[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#use-of-internal-buffers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Internally, buffers are used for misaligned data, swapped data, and data that has to be converted from one data type to another. The size of internal buffers is settable on a per-thread basis. There can be up to \\(2 (n\_{\\mathrm{inputs}} + n\_{\\mathrm{outputs}})\\) buffers of the specified size created to handle the data from all the inputs and outputs of a ufunc. The default size of a buffer is 10,000 elements. Whenever buffer-based calculation would be needed, but all input arrays are smaller than the buffer size, those misbehaved or incorrectly-typed arrays will be copied before the calculation proceeds. Adjusting the size of the buffer may therefore alter the speed at which ufunc calculations of various sorts are completed. A simple interface for setting this variable is accessible using the function [`numpy.setbufsize`](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html#numpy.setbufsize "numpy.setbufsize")
.

Error handling[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#error-handling "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Universal functions can trip special floating-point status registers in your hardware (such as divide-by-zero). If available on your platform, these registers will be regularly checked during calculation. Error handling is controlled on a per-thread basis, and can be configured using the functions [`numpy.seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
 and [`numpy.seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
.

Overriding ufunc behavior[#](https://numpy.org/doc/stable/user/basics.ufuncs.html#overriding-ufunc-behavior "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Classes (including ndarray subclasses) can override how ufuncs act on them by defining certain special methods. For details, see [Standard array subclasses](https://numpy.org/doc/stable/reference/arrays.classes.html#arrays-classes)
.

On this page