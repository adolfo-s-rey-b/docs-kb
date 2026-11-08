### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bytes.html "Bytes Objects")
     |
*   [previous](https://docs.python.org/3/c-api/float.html "Floating-Point Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Complex Number Objects](https://docs.python.org/3/c-api/complex.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Complex Number Objects[¶](https://docs.python.org/3/c-api/complex.html#complex-number-objects "Link to this heading")

======================================================================================================================

type PyComplexObject[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python complex number object.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 cval[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject.cval "Link to this definition")
  

The complex number value, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

Deprecated since version 3.15, will be removed in version 3.20: Use [`PyComplex_AsCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "PyComplex_AsCComplex")
 and [`PyComplex_FromCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromCComplex "PyComplex_FromCComplex")
 to convert a Python complex number to/from the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyComplex\_Type[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python complex number type. It is the same object as [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 in the Python layer.

int PyComplex\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_Check "Link to this definition")
  

Return true if its argument is a [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")
 or a subtype of `PyComplexObject`. This function always succeeds.

int PyComplex\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_CheckExact "Link to this definition")
  

Return true if its argument is a [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")
, but not a subtype of `PyComplexObject`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyComplex\_FromDoubles(double real, double imag)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromDoubles "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")
 object from _real_ and _imag_. Return `NULL` with an exception set on error.

double PyComplex\_RealAsDouble([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_RealAsDouble "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the real part of _op_ as a C double.

If _op_ is not a Python complex number object but has a [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 method, this method will first be called to convert _op_ to a Python complex number object. If `__complex__()` is not defined then it falls back to call [`PyFloat_AsDouble()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_AsDouble "PyFloat_AsDouble")
 and returns its result.

Upon failure, this method returns `-1.0` with an exception set, so one should call [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for errors.

Changed in version 3.13: Use [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 if available.

double PyComplex\_ImagAsDouble([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_ImagAsDouble "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the imaginary part of _op_ as a C double.

If _op_ is not a Python complex number object but has a [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 method, this method will first be called to convert _op_ to a Python complex number object. If `__complex__()` is not defined then it falls back to call [`PyFloat_AsDouble()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_AsDouble "PyFloat_AsDouble")
 and returns `0.0` on success.

Upon failure, this method returns `-1.0` with an exception set, so one should call [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for errors.

Changed in version 3.13: Use [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 if available.

type Py\_complex[¶](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Link to this definition")
  

This C structure defines an export format for a Python complex number object.

double real[¶](https://docs.python.org/3/c-api/complex.html#c.Py_complex.real "Link to this definition")
  

double imag[¶](https://docs.python.org/3/c-api/complex.html#c.Py_complex.imag "Link to this definition")
  

The structure is defined as:

typedef struct {
    double real;
    double imag;
} Py\_complex;

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyComplex\_FromCComplex([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 v)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromCComplex "Link to this definition")
  

_Return value: New reference._

Create a new Python complex number object from a C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 value. Return `NULL` with an exception set on error.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 PyComplex\_AsCComplex([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "Link to this definition")
  

Return the [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 value of the complex number _op_.

If _op_ is not a Python complex number object but has a [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 method, this method will first be called to convert _op_ to a Python complex number object. If `__complex__()` is not defined then it falls back to [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__")
. If `__float__()` is not defined then it falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
.

Upon failure, this method returns [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 with [`real`](https://docs.python.org/3/c-api/complex.html#c.Py_complex.real "Py_complex.real")
 set to `-1.0` and with an exception set, so one should call [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for errors.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Complex Numbers as C Structures[¶](https://docs.python.org/3/c-api/complex.html#complex-numbers-as-c-structures "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The API also provides functions for working with complex numbers, using the [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation. Note that the functions which accept these structures as parameters and return them as results do so _by value_ rather than dereferencing them through pointers.

Please note, that these functions are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since Python 3.15. Avoid using this API in a new code to do complex arithmetic: either use the [Number Protocol](https://docs.python.org/3/c-api/number.html#number)
 API or use native complex types, like double complex.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_sum([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 left, [Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 right)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_sum "Link to this definition")
  

Return the sum of two complex numbers, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

Deprecated since version 3.15.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_diff([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 left, [Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 right)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_diff "Link to this definition")
  

Return the difference between two complex numbers, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

Deprecated since version 3.15.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_neg([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 num)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_neg "Link to this definition")
  

Return the negation of the complex number _num_, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

Deprecated since version 3.15.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_prod([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 left, [Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 right)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_prod "Link to this definition")
  

Return the product of two complex numbers, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

Deprecated since version 3.15.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_quot([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 dividend, [Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 divisor)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_quot "Link to this definition")
  

Return the quotient of two complex numbers, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

If _divisor_ is null, this method returns zero and sets `errno` to `EDOM`.

Deprecated since version 3.15.

[Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 \_Py\_c\_pow([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 num, [Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 exp)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_pow "Link to this definition")
  

Return the exponentiation of _num_ by _exp_, using the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 representation.

If _num_ is null and _exp_ is not a positive real number, this method returns zero and sets `errno` to `EDOM`.

Set `errno` to `ERANGE` on overflows.

Deprecated since version 3.15.

double \_Py\_c\_abs([Py\_complex](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 num)[¶](https://docs.python.org/3/c-api/complex.html#c._Py_c_abs "Link to this definition")
  

Return the absolute value of the complex number _num_.

Set `errno` to `ERANGE` on overflows.

Deprecated since version 3.15.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Complex Number Objects](https://docs.python.org/3/c-api/complex.html#)
    *   [Complex Numbers as C Structures](https://docs.python.org/3/c-api/complex.html#complex-numbers-as-c-structures)
        

#### Previous topic

[Floating-Point Objects](https://docs.python.org/3/c-api/float.html "previous chapter")

#### Next topic

[Bytes Objects](https://docs.python.org/3/c-api/bytes.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Complex+Number+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcomplex.html&pagesource=c-api%2Fcomplex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/complex.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bytes.html "Bytes Objects")
     |
*   [previous](https://docs.python.org/3/c-api/float.html "Floating-Point Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Complex Number Objects](https://docs.python.org/3/c-api/complex.html)
    
*    
    
    |
*   Theme Auto Light Dark |