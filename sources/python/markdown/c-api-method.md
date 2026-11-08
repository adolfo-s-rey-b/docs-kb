### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/cell.html "Cell Objects")
     |
*   [previous](https://docs.python.org/3/c-api/function.html "Function Objects")
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
*   [Instance Method Objects](https://docs.python.org/3/c-api/method.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Instance Method Objects[¶](https://docs.python.org/3/c-api/method.html#instance-method-objects "Link to this heading")

=======================================================================================================================

An instance method is a wrapper for a [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
 and the new way to bind a `PyCFunction` to a class object. It replaces the former call `PyMethod_New(func, NULL, class)`.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyInstanceMethod\_Type[¶](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Type "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python instance method type. It is not exposed to Python programs.

int PyInstanceMethod\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Check "Link to this definition")
  

Return true if _o_ is an instance method object (has type [`PyInstanceMethod_Type`](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Type "PyInstanceMethod_Type")
). The parameter must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyInstanceMethod\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_New "Link to this definition")
  

_Return value: New reference._

Return a new instance method object, with _func_ being any callable object. _func_ is the function that will be called when the instance method is called.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyInstanceMethod\_Function([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*im)[¶](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Function "Link to this definition")
  

_Return value: Borrowed reference._

Return the function object associated with the instance method _im_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyInstanceMethod\_GET\_FUNCTION([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*im)[¶](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_GET_FUNCTION "Link to this definition")
  

_Return value: Borrowed reference._

Macro version of [`PyInstanceMethod_Function()`](https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Function "PyInstanceMethod_Function")
 which avoids error checking.

Method Objects[¶](https://docs.python.org/3/c-api/method.html#method-objects "Link to this heading")

=====================================================================================================

Methods are bound function objects. Methods are always bound to an instance of a user-defined class. Unbound methods (methods bound to a class object) are no longer available.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyMethod\_Type[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_Type "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python method type. This is exposed to Python programs as `types.MethodType`.

int PyMethod\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_Check "Link to this definition")
  

Return true if _o_ is a method object (has type [`PyMethod_Type`](https://docs.python.org/3/c-api/method.html#c.PyMethod_Type "PyMethod_Type")
). The parameter must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMethod\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_New "Link to this definition")
  

_Return value: New reference._

Return a new method object, with _func_ being any callable object and _self_ the instance the method should be bound. _func_ is the function that will be called when the method is called. _self_ must not be `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMethod\_Function([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*meth)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_Function "Link to this definition")
  

_Return value: Borrowed reference._

Return the function object associated with the method _meth_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMethod\_GET\_FUNCTION([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*meth)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_GET_FUNCTION "Link to this definition")
  

_Return value: Borrowed reference._

Macro version of [`PyMethod_Function()`](https://docs.python.org/3/c-api/method.html#c.PyMethod_Function "PyMethod_Function")
 which avoids error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMethod\_Self([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*meth)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_Self "Link to this definition")
  

_Return value: Borrowed reference._

Return the instance associated with the method _meth_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMethod\_GET\_SELF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*meth)[¶](https://docs.python.org/3/c-api/method.html#c.PyMethod_GET_SELF "Link to this definition")
  

_Return value: Borrowed reference._

Macro version of [`PyMethod_Self()`](https://docs.python.org/3/c-api/method.html#c.PyMethod_Self "PyMethod_Self")
 which avoids error checking.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Instance Method Objects](https://docs.python.org/3/c-api/method.html#)
    
*   [Method Objects](https://docs.python.org/3/c-api/method.html#method-objects)
    

#### Previous topic

[Function Objects](https://docs.python.org/3/c-api/function.html "previous chapter")

#### Next topic

[Cell Objects](https://docs.python.org/3/c-api/cell.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Instance+Method+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmethod.html&pagesource=c-api%2Fmethod.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/method.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/cell.html "Cell Objects")
     |
*   [previous](https://docs.python.org/3/c-api/function.html "Function Objects")
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
*   [Instance Method Objects](https://docs.python.org/3/c-api/method.html)
    
*    
    
    |
*   Theme Auto Light Dark |