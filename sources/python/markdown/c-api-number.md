### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sequence.html "Sequence Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/call.html "Call Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Number Protocol](https://docs.python.org/3/c-api/number.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Number Protocol[¶](https://docs.python.org/3/c-api/number.html#number-protocol "Link to this heading")

=======================================================================================================

int PyNumber\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns `1` if the object _o_ provides numeric protocols, and false otherwise. This function always succeeds.

Changed in version 3.8: Returns `1` if _o_ is an index integer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Add([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Add "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of adding _o1_ and _o2_, or `NULL` on failure. This is the equivalent of the Python expression `o1 + o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Subtract([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Subtract "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of subtracting _o2_ from _o1_, or `NULL` on failure. This is the equivalent of the Python expression `o1 - o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Multiply([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Multiply "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of multiplying _o1_ and _o2_, or `NULL` on failure. This is the equivalent of the Python expression `o1 * o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_MatrixMultiply([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_MatrixMultiply "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Returns the result of matrix multiplication on _o1_ and _o2_, or `NULL` on failure. This is the equivalent of the Python expression `o1 @ o2`.

Added in version 3.5.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_FloorDivide([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_FloorDivide "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the floor of _o1_ divided by _o2_, or `NULL` on failure. This is the equivalent of the Python expression `o1 // o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_TrueDivide([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_TrueDivide "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a reasonable approximation for the mathematical value of _o1_ divided by _o2_, or `NULL` on failure. The return value is “approximate” because binary floating-point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating-point value when passed two integers. This is the equivalent of the Python expression `o1 / o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Remainder([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Remainder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the remainder of dividing _o1_ by _o2_, or `NULL` on failure. This is the equivalent of the Python expression `o1 % o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Divmod([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Divmod "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See the built-in function [`divmod()`](https://docs.python.org/3/builtins/functions.html#divmod "divmod")
. Returns `NULL` on failure. This is the equivalent of the Python expression `divmod(o1, o2)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Power([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o3)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Power "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See the built-in function [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
. Returns `NULL` on failure. This is the equivalent of the Python expression `pow(o1, o2, o3)`, where _o3_ is optional. If _o3_ is to be ignored, pass [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
 in its place (passing `NULL` for _o3_ would cause an illegal memory access).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Negative([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Negative "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the negation of _o_ on success, or `NULL` on failure. This is the equivalent of the Python expression `-o`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Positive([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Positive "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns _o_ on success, or `NULL` on failure. This is the equivalent of the Python expression `+o`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Absolute([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Absolute "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the absolute value of _o_, or `NULL` on failure. This is the equivalent of the Python expression `abs(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Invert([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Invert "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the bitwise negation of _o_ on success, or `NULL` on failure. This is the equivalent of the Python expression `~o`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Lshift([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Lshift "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of left shifting _o1_ by _o2_ on success, or `NULL` on failure. This is the equivalent of the Python expression `o1 << o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Rshift([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Rshift "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of right shifting _o1_ by _o2_ on success, or `NULL` on failure. This is the equivalent of the Python expression `o1 >> o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_And([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_And "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise and” of _o1_ and _o2_ on success and `NULL` on failure. This is the equivalent of the Python expression `o1 & o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Xor([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Xor "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise exclusive or” of _o1_ by _o2_ on success, or `NULL` on failure. This is the equivalent of the Python expression `o1 ^ o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Or([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Or "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise or” of _o1_ and _o2_ on success, or `NULL` on failure. This is the equivalent of the Python expression `o1 | o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceAdd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceAdd "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of adding _o1_ and _o2_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 += o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceSubtract([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceSubtract "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of subtracting _o2_ from _o1_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 -= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceMultiply([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceMultiply "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of multiplying _o1_ and _o2_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 *= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceMatrixMultiply([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceMatrixMultiply "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Returns the result of matrix multiplication on _o1_ and _o2_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 @= o2`.

Added in version 3.5.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceFloorDivide([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceFloorDivide "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the mathematical floor of dividing _o1_ by _o2_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 //= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceTrueDivide([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceTrueDivide "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a reasonable approximation for the mathematical value of _o1_ divided by _o2_, or `NULL` on failure. The return value is “approximate” because binary floating-point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating-point value when passed two integers. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 /= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceRemainder([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceRemainder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the remainder of dividing _o1_ by _o2_, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 %= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlacePower([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o3)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlacePower "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See the built-in function [`pow()`](https://docs.python.org/3/builtins/functions.html#pow "pow")
. Returns `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 **= o2` when o3 is [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
, or an in-place variant of `pow(o1, o2, o3)` otherwise. If _o3_ is to be ignored, pass `Py_None` in its place (passing `NULL` for _o3_ would cause an illegal memory access).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceLshift([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceLshift "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of left shifting _o1_ by _o2_ on success, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 <<= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceRshift([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceRshift "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the result of right shifting _o1_ by _o2_ on success, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 >>= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceAnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceAnd "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise and” of _o1_ and _o2_ on success and `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 &= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceXor([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceXor "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise exclusive or” of _o1_ by _o2_ on success, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 ^= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_InPlaceOr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceOr "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the “bitwise or” of _o1_ and _o2_ on success, or `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python statement `o1 |= o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Long([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Long "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the _o_ converted to an integer object on success, or `NULL` on failure. This is the equivalent of the Python expression `int(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Float([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Float "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the _o_ converted to a float object on success, or `NULL` on failure. This is the equivalent of the Python expression `float(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_Index([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_Index "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the _o_ converted to a Python int on success or `NULL` with a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 exception raised on failure.

Changed in version 3.10: The result always has exact type [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. Previously, the result could have been an instance of a subclass of `int`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyNumber\_ToBase([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*n, int base)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_ToBase "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the integer _n_ converted to base _base_ as a string. The _base_ argument must be one of 2, 8, 10, or 16. For base 2, 8, or 16, the returned string is prefixed with a base marker of `'0b'`, `'0o'`, or `'0x'`, respectively. If _n_ is not a Python int, it is converted with [`PyNumber_Index()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Index "PyNumber_Index")
 first.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyNumber\_AsSsize\_t([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/number.html#c.PyNumber_AsSsize_t "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns _o_ converted to a [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 value if _o_ can be interpreted as an integer. If the call fails, an exception is raised and `-1` is returned.

If _o_ can be converted to a Python int but the attempt to convert to a [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 value would raise an [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
, then the _exc_ argument is the type of exception that will be raised (usually [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 or `OverflowError`). If _exc_ is `NULL`, then the exception is cleared and the value is clipped to `PY_SSIZE_T_MIN` for a negative integer or `PY_SSIZE_T_MAX` for a positive integer.

int PyIndex\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/number.html#c.PyIndex_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

Returns `1` if _o_ is an index integer (has the `nb_index` slot of the `tp_as_number` structure filled in), and `0` otherwise. This function always succeeds.

#### Previous topic

[Call Protocol](https://docs.python.org/3/c-api/call.html "previous chapter")

#### Next topic

[Sequence Protocol](https://docs.python.org/3/c-api/sequence.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Number+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fnumber.html&pagesource=c-api%2Fnumber.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/number.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sequence.html "Sequence Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/call.html "Call Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Number Protocol](https://docs.python.org/3/c-api/number.html)
    
*    
    
    |
*   Theme Auto Light Dark |