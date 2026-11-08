[Skip to main content](https://numpy.org/doc/stable/reference/arrays.dtypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.dtypes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.dtypes.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.dtypes.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.dtypes.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.dtypes.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.dtypes.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.dtypes.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.dtypes.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.dtypes.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.dtypes.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.dtypes.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.dtypes.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.dtypes.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.dtypes.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.dtypes.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.dtypes.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.dtypes.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.dtypes.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.dtypes.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.dtypes.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.dtypes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Data type objects ([`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
)[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#data-type-objects-dtype "Link to this heading")

=========================================================================================================================================================================================================================================

A data type object (an instance of [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 class) describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted. It describes the following aspects of the data:

1.  Type of the data (integer, float, Python object, etc.)
    
2.  Size of the data (how many bytes is in _e.g._ the integer)
    
3.  Byte order of the data ([little-endian](https://numpy.org/doc/stable/glossary.html#term-little-endian)
     or [big-endian](https://numpy.org/doc/stable/glossary.html#term-big-endian)
    )
    
4.  If the data type is [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)
    , an aggregate of other data types, (_e.g._, describing an array item consisting of an integer and a float),
    
    1.  what are the names of the “[fields](https://numpy.org/doc/stable/glossary.html#term-field)
        ” of the structure, by which they can be [accessed](https://numpy.org/doc/stable/user/basics.indexing.html#arrays-indexing-fields)
        ,
        
    2.  what is the data-type of each [field](https://numpy.org/doc/stable/glossary.html#term-field)
        , and
        
    3.  which part of the memory block each field takes.
        
5.  If the data type is a sub-array, what is its shape and data type.
    

To describe the type of scalar data, there are several [built-in scalar types](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars-built-in)
 in NumPy for various precision of integers, floating-point numbers, _etc_. An item extracted from an array, _e.g._, by indexing, will be a Python object whose type is the scalar type associated with the data type of the array.

Note that the scalar types are not [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 objects, even though they can be used in place of one whenever a data type specification is needed in NumPy.

Structured data types are formed by creating a data type whose [field](https://numpy.org/doc/stable/glossary.html#term-field)
 contain other data types. Each field has a name by which it can be [accessed](https://numpy.org/doc/stable/user/basics.indexing.html#arrays-indexing-fields)
. The parent data type should be of sufficient size to contain all its fields; the parent is nearly always based on the [`void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")
 type which allows an arbitrary item size. Structured data types may also contain nested structured sub-array data types in their fields.

Finally, a data type can describe items that are themselves arrays of items of another data type. These sub-arrays must, however, be of a fixed size.

If an array is created using a data-type describing a sub-array, the dimensions of the sub-array are appended to the shape of the array when the array is created. Sub-arrays in a field of a structured type behave differently, see [Field access](https://numpy.org/doc/stable/user/basics.indexing.html#arrays-indexing-fields)
.

Sub-arrays always have a C-contiguous memory layout.

Example

A simple data type containing a 32-bit big-endian integer: (see [Specifying and constructing data types](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing)
 for details on construction)

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype('>i4')
\>>> dt.byteorder
'>'
\>>> dt.itemsize
4
\>>> dt.name
'int32'
\>>> dt.type is np.int32
True

Copy to clipboard

Go BackOpen In Tab

The corresponding array scalar type is [`int32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
.

Example

A structured data type containing a 16-character string (in field ‘name’) and a sub-array of two 64-bit floating-point number (in field ‘grades’):

> Try it in your browser!
> 
> \>>> import numpy as np
> 
> Copy to clipboard
> 
> \>>> dt \= np.dtype(\[('name', np.str\_, 16), ('grades', np.float64, (2,))\])
> \>>> dt\['name'\]
> dtype('<U16')
> \>>> dt\['grades'\]
> dtype(('<f8', (2,)))
> 
> Copy to clipboard
> 
> Go BackOpen In Tab

Items of an array of this data type are wrapped in an [array scalar](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars)
 type that also has two fields:

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> x \= np.array(\[('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))\], dtype\=dt)
\>>> x\[1\]
('John', \[6., 7.\])
\>>> x\[1\]\['grades'\]
array(\[6.,  7.\])
\>>> type(x\[1\])
<class 'numpy.void'>
\>>> type(x\[1\]\['grades'\])
<class 'numpy.ndarray'>

Copy to clipboard

Go BackOpen In Tab

Specifying and constructing data types[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#specifying-and-constructing-data-types "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Whenever a data-type is required in a NumPy function or method, either a [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 object or something that can be converted to one can be supplied. Such conversions are done by the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 constructor:

|     |     |
| --- | --- |
| [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")<br>(dtype\[, align, copy\]) | \-- |

What can be converted to a data-type object is described below:

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 object

Used as-is.

None

The default data type: [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

Array-scalar types

The 24 built-in [array scalar type objects](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars-built-in)
 all convert to an associated data-type object. This is true for their sub-classes as well.

Note that not all data-type information can be supplied with a type-object: for example, [`flexible`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.flexible "numpy.flexible")
 data-types have a default _itemsize_ of 0, and require an explicitly given size to be useful.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype(np.int32)      \# 32-bit integer
\>>> dt \= np.dtype(np.complex128) \# 128-bit complex floating-point number

Copy to clipboard

Go BackOpen In Tab

Generic types

The generic hierarchical type objects convert to corresponding type objects according to the associations:

|     |     |
| --- | --- |
| [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")<br>, [`inexact`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.inexact "numpy.inexact")<br>, [`floating`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.floating "numpy.floating") | [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64") |
| [`complexfloating`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complexfloating "numpy.complexfloating") | [`complex128`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex128 "numpy.complex128") |
| [`integer`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.integer "numpy.integer")<br>, [`signedinteger`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.signedinteger "numpy.signedinteger") | [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_") |
| [`unsignedinteger`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.unsignedinteger "numpy.unsignedinteger") | [`uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint") |
| [`generic`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.generic "numpy.generic")<br>, [`flexible`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.flexible "numpy.flexible") | [`void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void") |

Deprecated since version 1.19: This conversion of generic scalar types is deprecated. This is because it can be unexpected in a context such as `arr.astype(dtype=np.floating)`, which casts an array of `float32` to an array of `float64`, even though `float32` is a subdtype of `np.floating`.

Built-in Python types

Several Python types are equivalent to a corresponding array scalar when used to generate a [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 object:

| Python type | NumPy type |
| --- | --- |
| [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_") |
| [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool") | [`bool_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_") |
| [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64") |
| [`complex`](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)") | [`complex128`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex128 "numpy.complex128") |
| [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_") |
| [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_") |
| [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)") | [`void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void") |
| (all others) | [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_") |

Note that `str_` corresponds to UCS4 encoded unicode strings.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype(float)   \# Python-compatible floating-point number
\>>> dt \= np.dtype(int)     \# Python-compatible integer
\>>> dt \= np.dtype(object)  \# Python object

Copy to clipboard

Go BackOpen In Tab

Note

All other types map to `object_` for convenience. Code should expect that such types may map to a specific (new) dtype in the future.

Types with `.dtype`

Any type object with a `dtype` attribute: The attribute will be accessed and used directly. The attribute must return something that is convertible into a dtype object.

Several kinds of strings can be converted. Recognized strings can be prepended with `'>'` ([big-endian](https://numpy.org/doc/stable/glossary.html#term-big-endian)
), `'<'` ([little-endian](https://numpy.org/doc/stable/glossary.html#term-little-endian)
), or `'='` (hardware-native, the default), to specify the byte order.

One-character strings

Each built-in data-type has a character code (the updated Numeric typecodes), that uniquely identifies it.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype('b')  \# byte, native byte order
\>>> dt \= np.dtype('>H') \# big-endian unsigned short
\>>> dt \= np.dtype('<f') \# little-endian single-precision float
\>>> dt \= np.dtype('d')  \# double-precision floating-point number

Copy to clipboard

Go BackOpen In Tab

Array-protocol type strings (see [The array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
)

The first character specifies the kind of data and the remaining characters specify the number of bytes per item, except for Unicode, where it is interpreted as the number of characters, and except `b1` which represents boolean. The item size must correspond to an existing type, or an error will be raised. The supported kinds are

|     |     |
| --- | --- |
| `'?'` | boolean |
| `'b'` | (signed) byte |
| `'B'` | unsigned byte |
| `'h'` | (signed) short |
| `'H'` | unsigned short |
| `'i'` | (signed) integer |
| `'I'` | unsigned integer |
| `'l'` | (signed) long integer |
| `'L'` | unsigned long integer |
| `'q'` | (signed) long long integer |
| `'Q'` | unsigned long long integer |
| `'f'` | single precision |
| `'F'` | complex single precision |
| `'d'` | double precision |
| `'D'` | complex double precision |
| `'g'` | long precision |
| `'G'` | complex long double precision |
| `'O'` | (Python) objects |
| `'S'` | zero-terminated bytes (not recommended) |
| `'U'` | Unicode string |
| `'V'` | raw data ([`void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")<br>) |

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype('i4')   \# 32-bit signed integer
\>>> dt \= np.dtype('f8')   \# 64-bit floating-point number
\>>> dt \= np.dtype('c16')  \# 128-bit complex floating-point number
\>>> dt \= np.dtype('S25')  \# 25-length zero-terminated bytes
\>>> dt \= np.dtype('U25')  \# 25-character string

Copy to clipboard

Go BackOpen In Tab

String with comma-separated fields

A short-hand notation for specifying the format of a structured data type is a comma-separated string of basic formats.

A basic format in this context is an optional shape specifier followed by an array-protocol type string. Parenthesis are required on the shape if it has more than one dimension. NumPy allows a modification on the format in that any string that can uniquely identify the type can be used to specify the data-type in a field. The generated data-type fields are named `'f0'`, `'f1'`, …, `'f<N-1>'` where N (>1) is the number of comma-separated basic formats in the string. If the optional shape specifier is provided, then the data-type for the corresponding field describes a sub-array.

Example

Try it in your browser!

Go BackOpen In Tab

*   field named `f0` containing a 32-bit integer
    
*   field named `f1` containing a 2 x 3 sub-array of 64-bit floating-point numbers
    
*   field named `f2` containing a 32-bit floating-point number
    
    \>>> import numpy as np
    \>>> dt \= np.dtype("i4, (2,3)f8, f4")
    
    Copy to clipboard
    
*   field named `f0` containing a 3-character string
    
*   field named `f1` containing a sub-array of shape (3,) containing 64-bit unsigned integers
    
*   field named `f2` containing a 3 x 4 sub-array containing 10-character strings
    
    \>>> import numpy as np
    \>>> dt \= np.dtype("S3, 3u8, (3,4)S10")
    
    Copy to clipboard
    

Type strings

Any string name of a NumPy dtype, e.g.:

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype('uint32')   \# 32-bit unsigned integer
\>>> dt \= np.dtype('float64')  \# 64-bit floating-point number

Copy to clipboard

Go BackOpen In Tab

`(flexible_dtype, itemsize)`

The first argument must be an object that is converted to a zero-sized flexible data-type object, the second argument is an integer providing the desired itemsize.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype((np.void, 10))  \# 10-byte wide data block
\>>> dt \= np.dtype(('U', 10))   \# 10-character unicode string

Copy to clipboard

Go BackOpen In Tab

`(fixed_dtype, shape)`

The first argument is any object that can be converted into a fixed-size data-type object. The second argument is the desired shape of this type. If the shape parameter is 1, then the data-type object used to be equivalent to fixed dtype. This behaviour is deprecated since NumPy 1.17 and will raise an error in the future. If _shape_ is a tuple, then the new dtype defines a sub-array of the given shape.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype((np.int32, (2,2)))          \# 2 x 2 integer sub-array
\>>> dt \= np.dtype(('i4, (2,3)f8, f4', (2,3))) \# 2 x 3 structured sub-array

Copy to clipboard

Go BackOpen In Tab

`[(field_name, field_dtype, field_shape), ...]`

_obj_ should be a list of fields where each field is described by a tuple of length 2 or 3. (Equivalent to the `descr` item in the [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__")
 attribute.)

The first element, _field\_name_, is the field name (if this is `''` then a standard field name, `'f#'`, is assigned). The field name may also be a 2-tuple of strings where the first string is either a “title” (which may be any string or unicode string) or meta-data for the field which can be any object, and the second string is the “name” which must be a valid Python identifier.

The second element, _field\_dtype_, can be anything that can be interpreted as a data-type.

The optional third element _field\_shape_ contains the shape if this field represents an array of the data-type in the second element. Note that a 3-tuple with a third argument equal to 1 is equivalent to a 2-tuple.

This style does not accept _align_ in the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 constructor as it is assumed that all of the memory is accounted for by the array interface description.

Example

Try it in your browser!

Data-type with fields `big` (big-endian 32-bit integer) and `little` (little-endian 32-bit integer):

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype(\[('big', '>i4'), ('little', '<i4')\])

Copy to clipboard

Data-type with fields `R`, `G`, `B`, `A`, each being an unsigned 8-bit integer:

\>>> dt \= np.dtype(\[('R','u1'), ('G','u1'), ('B','u1'), ('A','u1')\])

Copy to clipboard

Go BackOpen In Tab

`{'names': ..., 'formats': ..., 'offsets': ..., 'titles': ..., 'itemsize': ...}`

This style has two required and three optional keys. The _names_ and _formats_ keys are required. Their respective values are equal-length lists with the field names and the field formats. The field names must be strings and the field formats can be any object accepted by [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 constructor.

When the optional keys _offsets_ and _titles_ are provided, their values must each be lists of the same length as the _names_ and _formats_ lists. The _offsets_ value is a list of byte offsets (limited to [`ctypes.c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "(in Python v3.14)")
) for each field, while the _titles_ value is a list of titles for each field (`None` can be used if no title is desired for that field). The _titles_ can be any object, but when a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 object will add another entry to the fields dictionary keyed by the title and referencing the same field tuple which will contain the title as an additional tuple member.

The _itemsize_ key allows the total size of the dtype to be set, and must be an integer large enough so all the fields are within the dtype. If the dtype being constructed is aligned, the _itemsize_ must also be divisible by the struct alignment. Total dtype _itemsize_ is limited to [`ctypes.c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "(in Python v3.14)")
.

Example

Try it in your browser!

Data type with fields `r`, `g`, `b`, `a`, each being an 8-bit unsigned integer:

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype({'names': \['r','g','b','a'\],
...                'formats': \[np.uint8, np.uint8, np.uint8, np.uint8\]})

Copy to clipboard

Data type with fields `r` and `b` (with the given titles), both being 8-bit unsigned integers, the first at byte position 0 from the start of the field and the second at position 2:

\>>> dt \= np.dtype({'names': \['r','b'\], 'formats': \['u1', 'u1'\],
...                'offsets': \[0, 2\],
...                'titles': \['Red pixel', 'Blue pixel'\]})

Copy to clipboard

Go BackOpen In Tab

`{'field1': ..., 'field2': ..., ...}`

This usage is discouraged, because it is ambiguous with the other dict-based construction method. If you have a field called ‘names’ and a field called ‘formats’ there will be a conflict.

This style allows passing in the [`fields`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#numpy.dtype.fields "numpy.dtype.fields")
 attribute of a data-type object.

_obj_ should contain string or unicode keys that refer to `(data-type, offset)` or `(data-type, offset, title)` tuples.

Example

Try it in your browser!

Data type containing field `col1` (10-character string at byte position 0), `col2` (32-bit float at byte position 10), and `col3` (integers at byte position 14):

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype({'col1': ('U10', 0), 'col2': (np.float32, 10),
...                'col3': (int, 14)})

Copy to clipboard

Go BackOpen In Tab

`(base_dtype, new_dtype)`

In NumPy 1.7 and later, this form allows _base\_dtype_ to be interpreted as a structured dtype. Arrays created with this dtype will have underlying dtype _base\_dtype_ but will have fields and flags taken from _new\_dtype_. This is useful for creating custom structured dtypes, as done in [record arrays](https://numpy.org/doc/stable/reference/arrays.classes.html#arrays-classes-rec)
.

This form also makes it possible to specify struct dtypes with overlapping fields, functioning like the ‘union’ type in C. This usage is discouraged, however, and the union mechanism is preferred.

Both arguments must be convertible to data-type objects with the same total size.

Example

Try it in your browser!

32-bit integer, whose first two bytes are interpreted as an integer via field `real`, and the following two bytes via field `imag`.

\>>> import numpy as np

Copy to clipboard

\>>> dt \= np.dtype((np.int32,{'real':(np.int16, 0),'imag':(np.int16, 2)}))

Copy to clipboard

32-bit integer, which is interpreted as consisting of a sub-array of shape `(4,)` containing 8-bit integers:

\>>> dt \= np.dtype((np.int32, (np.int8, 4)))

Copy to clipboard

32-bit integer, containing fields `r`, `g`, `b`, `a` that interpret the 4 bytes in the integer as four unsigned integers:

\>>> dt \= np.dtype(('i4', \[('r','u1'),('g','u1'),('b','u1'),('a','u1')\]))

Copy to clipboard

Go BackOpen In Tab

Checking the data type[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#checking-the-data-type "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

When checking for a specific data type, use `==` comparison.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.array(\[1, 2\], dtype\=np.float32)
\>>> a.dtype \== np.float32
True

Copy to clipboard

Go BackOpen In Tab

As opposed to Python types, a comparison using `is` should not be used.

First, NumPy treats data type specifications (everything that can be passed to the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 constructor) as equivalent to the data type object itself. This equivalence can only be handled through `==`, not through `is`.

Example

Try it in your browser!

A [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 object is equal to all data type specifications that are equivalent to it.

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.array(\[1, 2\], dtype\=np.float64)
\>>> a.dtype \== np.dtype(np.float64)
True
\>>> a.dtype \== np.float64
True
\>>> a.dtype \== float
True
\>>> a.dtype \== "float64"
True
\>>> a.dtype \== "d"
True

Copy to clipboard

Go BackOpen In Tab

Second, there is no guarantee that data type objects are singletons.

Example

Try it in your browser!

Do not use `is` because data type objects may or may not be singletons.

\>>> import numpy as np

Copy to clipboard

\>>> np.dtype(float) is np.dtype(float)
True
\>>> np.dtype(\[('a', float)\]) is np.dtype(\[('a', float)\])
False

Copy to clipboard

Go BackOpen In Tab

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#dtype "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy data type descriptions are instances of the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 class.

### Attributes[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#attributes "Link to this heading")

The type of the data is described by the following [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 attributes:

|     |     |
| --- | --- |
| [`dtype.type`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.type.html#numpy.dtype.type "numpy.dtype.type") |     |
| [`dtype.kind`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy.dtype.kind "numpy.dtype.kind") | A character code (one of 'biufcmMOSTUV') identifying the general kind of data. |
| [`dtype.char`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.char.html#numpy.dtype.char "numpy.dtype.char") | A unique character code for each of the 21 different built-in types. |
| [`dtype.num`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.num.html#numpy.dtype.num "numpy.dtype.num") | A unique number for each of the 21 different built-in types. |
| [`dtype.str`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.str.html#numpy.dtype.str "numpy.dtype.str") | The array-protocol typestring of this data-type object. |

Size of the data is in turn described by:

|     |     |
| --- | --- |
| [`dtype.name`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.name.html#numpy.dtype.name "numpy.dtype.name") | A bit-width name for this data-type. |
| [`dtype.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.itemsize.html#numpy.dtype.itemsize "numpy.dtype.itemsize") | The element size of this data-type object. |

Endianness of this data:

|     |     |
| --- | --- |
| [`dtype.byteorder`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#numpy.dtype.byteorder "numpy.dtype.byteorder") | A character indicating the byte-order of this data-type object. |

Information about sub-data-types in a [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)
:

|     |     |
| --- | --- |
| [`dtype.fields`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#numpy.dtype.fields "numpy.dtype.fields") | Dictionary of named fields defined for this data type, or `None`. |
| [`dtype.names`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.names.html#numpy.dtype.names "numpy.dtype.names") | Ordered list of field names, or `None` if there are no fields. |

For data types that describe sub-arrays:

|     |     |
| --- | --- |
| [`dtype.subdtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html#numpy.dtype.subdtype "numpy.dtype.subdtype") | Tuple `(item_dtype, shape)` if this [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")<br> describes a sub-array, and None otherwise. |
| [`dtype.shape`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.shape.html#numpy.dtype.shape "numpy.dtype.shape") | Shape tuple of the sub-array if this data type describes a sub-array, and `()` otherwise. |

Attributes providing additional information:

|     |     |
| --- | --- |
| [`dtype.hasobject`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.hasobject.html#numpy.dtype.hasobject "numpy.dtype.hasobject") | Boolean indicating whether this dtype contains any reference-counted objects in any fields or sub-dtypes. |
| [`dtype.flags`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html#numpy.dtype.flags "numpy.dtype.flags") | Bit-flags describing how this data type is to be interpreted. |
| [`dtype.isbuiltin`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.isbuiltin.html#numpy.dtype.isbuiltin "numpy.dtype.isbuiltin") | Integer indicating how this dtype relates to the built-in dtypes. |
| [`dtype.isnative`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.isnative.html#numpy.dtype.isnative "numpy.dtype.isnative") | Boolean indicating whether the byte order of this dtype is native to the platform. |
| [`dtype.descr`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.descr.html#numpy.dtype.descr "numpy.dtype.descr") | _\_\_array\_interface\_\__ description of the data-type. |
| [`dtype.alignment`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.alignment.html#numpy.dtype.alignment "numpy.dtype.alignment") | The required alignment (bytes) of this data-type according to the compiler. |
| [`dtype.base`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.base.html#numpy.dtype.base "numpy.dtype.base") | Returns dtype for the base element of the subarrays, regardless of their dimension or shape. |

Metadata attached by the user:

|     |     |
| --- | --- |
| [`dtype.metadata`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html#numpy.dtype.metadata "numpy.dtype.metadata") | Either `None` or a readonly dictionary of metadata (mappingproxy). |

### Methods[#](https://numpy.org/doc/stable/reference/arrays.dtypes.html#methods "Link to this heading")

Data types have the following method for changing the byte order:

|     |     |
| --- | --- |
| [`dtype.newbyteorder`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html#numpy.dtype.newbyteorder "numpy.dtype.newbyteorder")<br>(\[new\_order\]) | Return a new dtype with a different byte order. |

The following methods implement the pickle protocol:

|     |     |
| --- | --- |
| [`dtype.__reduce__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__reduce__.html#numpy.dtype.__reduce__ "numpy.dtype.__reduce__") | Helper for pickle. |
| [`dtype.__setstate__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__setstate__.html#numpy.dtype.__setstate__ "numpy.dtype.__setstate__") |     |

Utility method for typing:

|     |     |
| --- | --- |
| [`dtype.__class_getitem__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__class_getitem__.html#numpy.dtype.__class_getitem__ "numpy.dtype.__class_getitem__")<br>(item, /) | Return a parametrized wrapper around the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")<br> type. |

Comparison operations:

|     |     |
| --- | --- |
| [`dtype.__ge__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__ge__.html#numpy.dtype.__ge__ "numpy.dtype.__ge__")<br>(value, /) | Return self>=value. |
| [`dtype.__gt__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__gt__.html#numpy.dtype.__gt__ "numpy.dtype.__gt__")<br>(value, /) | Return self>value. |
| [`dtype.__le__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__le__.html#numpy.dtype.__le__ "numpy.dtype.__le__")<br>(value, /) | Return self<=value. |
| [`dtype.__lt__`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__lt__.html#numpy.dtype.__lt__ "numpy.dtype.__lt__")<br>(value, /) | Return self<value. |

On this page