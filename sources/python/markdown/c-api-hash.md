### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/reflection.html "Reflection")
     |
*   [previous](https://docs.python.org/3/c-api/conversion.html "String conversion and formatting")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [PyHash API](https://docs.python.org/3/c-api/hash.html)
    
*    
    
    |
*   Theme Auto Light Dark |

PyHash API[¶](https://docs.python.org/3/c-api/hash.html#pyhash-api "Link to this heading")

===========================================================================================

See also the [`PyTypeObject.tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
 member and [Hashing of numeric types](https://docs.python.org/3/builtins/stdtypes.html#numeric-hash)
.

type Py\_hash\_t[¶](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Link to this definition")
  

Hash value type: signed integer.

Added in version 3.2.

type Py\_uhash\_t[¶](https://docs.python.org/3/c-api/hash.html#c.Py_uhash_t "Link to this definition")
  

Hash value type: unsigned integer.

Added in version 3.2.

Py\_HASH\_ALGORITHM[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_ALGORITHM "Link to this definition")
  

A numerical value indicating the algorithm for hashing of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, and [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
.

The algorithm name is exposed by [`sys.hash_info.algorithm`](https://docs.python.org/3/library/sys.html#sys.hash_info.algorithm "sys.hash_info.algorithm")
.

Added in version 3.4.

Py\_HASH\_FNV[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_FNV "Link to this definition")
  

Py\_HASH\_SIPHASH24[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_SIPHASH24 "Link to this definition")
  

Py\_HASH\_SIPHASH13[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_SIPHASH13 "Link to this definition")
  

Py\_HASH\_EXTERNAL[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_EXTERNAL "Link to this definition")
  

Numerical values to compare to [`Py_HASH_ALGORITHM`](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_ALGORITHM "Py_HASH_ALGORITHM")
 to determine which algorithm is used for hashing. The built-in hash algorithm can be configured via the configure [`--with-hash-algorithm`](https://docs.python.org/3/using/configure.html#cmdoption-with-hash-algorithm)
 option.

`Py_HASH_EXTERNAL` has value `0` and indicates a hash implementation supplied by the application embedding Python; see [`PyHash_Func`](https://docs.python.org/3/c-api/hash.html#c.PyHash_Func "PyHash_Func")
.

Added in version 3.4: Add `Py_HASH_FNV`, `Py_HASH_SIPHASH24`, and `Py_HASH_EXTERNAL`.

Added in version 3.11: Add `Py_HASH_SIPHASH13`.

Py\_HASH\_CUTOFF[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_CUTOFF "Link to this definition")
  

Buffers of length in range `[1, Py_HASH_CUTOFF)` are hashed using DJBX33A instead of the algorithm described by [`Py_HASH_ALGORITHM`](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_ALGORITHM "Py_HASH_ALGORITHM")\
.\
\
*   A `Py_HASH_CUTOFF` of 0 disables the optimization.\
    \
*   `Py_HASH_CUTOFF` must be non-negative and less or equal than 7.\
    \
\
32-bit platforms should use a cutoff smaller than 64-bit platforms because it is easier to create colliding strings. A cutoff of 7 on 64-bit platforms and 5 on 32-bit platforms should provide a decent safety margin.\
\
This corresponds to the [`sys.hash_info.cutoff`](https://docs.python.org/3/library/sys.html#sys.hash_info.cutoff "sys.hash_info.cutoff")\
 constant.\
\
Added in version 3.4.\
\
PyHASH\_MODULUS[¶](https://docs.python.org/3/c-api/hash.html#c.PyHASH_MODULUS "Link to this definition")\
  \
\
The [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)\
 `P = 2**n -1`, used for numeric hash scheme.\
\
This corresponds to the [`sys.hash_info.modulus`](https://docs.python.org/3/library/sys.html#sys.hash_info.modulus "sys.hash_info.modulus")\
 constant.\
\
Added in version 3.13.\
\
PyHASH\_BITS[¶](https://docs.python.org/3/c-api/hash.html#c.PyHASH_BITS "Link to this definition")\
  \
\
The exponent `n` of `P` in [`PyHASH_MODULUS`](https://docs.python.org/3/c-api/hash.html#c.PyHASH_MODULUS "PyHASH_MODULUS")\
.\
\
Added in version 3.13.\
\
PyHASH\_MULTIPLIER[¶](https://docs.python.org/3/c-api/hash.html#c.PyHASH_MULTIPLIER "Link to this definition")\
  \
\
Prime multiplier used in string and various other hashes.\
\
Added in version 3.13.\
\
PyHASH\_INF[¶](https://docs.python.org/3/c-api/hash.html#c.PyHASH_INF "Link to this definition")\
  \
\
The hash value returned for a positive infinity.\
\
This corresponds to the [`sys.hash_info.inf`](https://docs.python.org/3/library/sys.html#sys.hash_info.inf "sys.hash_info.inf")\
 constant.\
\
Added in version 3.13.\
\
PyHASH\_IMAG[¶](https://docs.python.org/3/c-api/hash.html#c.PyHASH_IMAG "Link to this definition")\
  \
\
The multiplier used for the imaginary part of a complex number.\
\
This corresponds to the [`sys.hash_info.imag`](https://docs.python.org/3/library/sys.html#sys.hash_info.imag "sys.hash_info.imag")\
 constant.\
\
Added in version 3.13.\
\
type PyHash\_FuncDef[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef "Link to this definition")\
  \
\
Hash function definition used by [`PyHash_GetFuncDef()`](https://docs.python.org/3/c-api/hash.html#c.PyHash_GetFuncDef "PyHash_GetFuncDef")\
.\
\
[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")\
 (\*const hash)(const void\*, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
)[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef.hash "Link to this definition")\
  \
\
Hash function.\
\
const char \*name[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef.name "Link to this definition")\
  \
\
Hash function name (UTF-8 encoded string).\
\
This corresponds to the [`sys.hash_info.algorithm`](https://docs.python.org/3/library/sys.html#sys.hash_info.algorithm "sys.hash_info.algorithm")\
 constant.\
\
const int hash\_bits[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef.hash_bits "Link to this definition")\
  \
\
Internal size of the hash value in bits.\
\
This corresponds to the [`sys.hash_info.hash_bits`](https://docs.python.org/3/library/sys.html#sys.hash_info.hash_bits "sys.hash_info.hash_bits")\
 constant.\
\
const int seed\_bits[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef.seed_bits "Link to this definition")\
  \
\
Size of seed input in bits.\
\
This corresponds to the [`sys.hash_info.seed_bits`](https://docs.python.org/3/library/sys.html#sys.hash_info.seed_bits "sys.hash_info.seed_bits")\
 constant.\
\
Added in version 3.4.\
\
[PyHash\_FuncDef](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef "PyHash_FuncDef")\
 PyHash\_Func[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_Func "Link to this definition")\
  \
\
When Python is built with [`Py_HASH_ALGORITHM`](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_ALGORITHM "Py_HASH_ALGORITHM")\
 set to [`Py_HASH_EXTERNAL`](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_EXTERNAL "Py_HASH_EXTERNAL")\
, the application embedding Python must define this variable to supply a hash implementation instead of using one of Python’s built-in hash algorithms.\
\
Added in version 3.4.\
\
Deprecated since version 3.15, will be removed in version 3.19: Use one of the built-in hash algorithms instead.\
\
[PyHash\_FuncDef](https://docs.python.org/3/c-api/hash.html#c.PyHash_FuncDef "PyHash_FuncDef")\
 \*PyHash\_GetFuncDef(void)[¶](https://docs.python.org/3/c-api/hash.html#c.PyHash_GetFuncDef "Link to this definition")\
  \
\
Get the hash function definition.\
\
See also\
\
[**PEP 456**](https://peps.python.org/pep-0456/)\
 “Secure and interchangeable hash algorithm”.\
\
Added in version 3.4.\
\
[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")\
 Py\_HashPointer(const void \*ptr)[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Link to this definition")\
  \
\
Hash a pointer value: process the pointer value as an integer (cast it to `uintptr_t` internally). The pointer is not dereferenced.\
\
The function cannot fail: it cannot return `-1`.\
\
Added in version 3.13.\
\
[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")\
 Py\_HashBuffer(const void \*ptr, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
 len)[¶](https://docs.python.org/3/c-api/hash.html#c.Py_HashBuffer "Link to this definition")\
  \
\
Compute and return the hash value of a buffer of _len_ bytes starting at address _ptr_. The hash is guaranteed to match that of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")\
, [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")\
, and other built-in objects that implement the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)\
.\
\
Use this function to implement hashing for immutable objects whose [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")\
 function compares to another object’s buffer.\
\
_len_ must be greater than or equal to `0`.\
\
This function always succeeds.\
\
Added in version 3.14.\
\
[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")\
 PyObject\_GenericHash([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\
 \*obj)[¶](https://docs.python.org/3/c-api/hash.html#c.PyObject_GenericHash "Link to this definition")\
  \
\
Generic hashing function that is meant to be put into a type object’s `tp_hash` slot. Its result only depends on the object’s identity.\
\
**CPython implementation detail:** In CPython, it is equivalent to [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")\
.\
\
Added in version 3.13.\
\
#### Previous topic\
\
[String conversion and formatting](https://docs.python.org/3/c-api/conversion.html "previous chapter")\
\
#### Next topic\
\
[Reflection](https://docs.python.org/3/c-api/reflection.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=PyHash+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fhash.html&pagesource=c-api%2Fhash.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/hash.rst?plain=1)\
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
*   [next](https://docs.python.org/3/c-api/reflection.html "Reflection")\
     |\
*   [previous](https://docs.python.org/3/c-api/conversion.html "String conversion and formatting")\
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
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)\
     »\
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)\
     »\
*   [PyHash API](https://docs.python.org/3/c-api/hash.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |