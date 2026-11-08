### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/call.html "Call Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer")
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
*   [Object Protocol](https://docs.python.org/3/c-api/object.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Object Protocol[¶](https://docs.python.org/3/c-api/object.html#object-protocol "Link to this heading")

=======================================================================================================

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_GetConstant(unsigned int constant\_id)[¶](https://docs.python.org/3/c-api/object.html#c.Py_GetConstant "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Get a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a constant.

Set an exception and return `NULL` if _constant\_id_ is invalid.

_constant\_id_ must be one of these constant identifiers:

| Constant Identifier | Value | Returned object |
| --- | --- | --- |
| Py\_CONSTANT\_NONE[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_NONE "Link to this definition") | `0` | [`None`](https://docs.python.org/3/builtins/constants.html#None "None") |
| Py\_CONSTANT\_FALSE[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_FALSE "Link to this definition") | `1` | [`False`](https://docs.python.org/3/builtins/constants.html#False "False") |
| Py\_CONSTANT\_TRUE[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_TRUE "Link to this definition") | `2` | [`True`](https://docs.python.org/3/builtins/constants.html#True "True") |
| Py\_CONSTANT\_ELLIPSIS[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_ELLIPSIS "Link to this definition") | `3` | [`Ellipsis`](https://docs.python.org/3/builtins/constants.html#Ellipsis "Ellipsis") |
| Py\_CONSTANT\_NOT\_IMPLEMENTED[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_NOT_IMPLEMENTED "Link to this definition") | `4` | [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented") |
| Py\_CONSTANT\_ZERO[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_ZERO "Link to this definition") | `5` | `0` |
| Py\_CONSTANT\_ONE[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_ONE "Link to this definition") | `6` | `1` |
| Py\_CONSTANT\_EMPTY\_STR[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_EMPTY_STR "Link to this definition") | `7` | `''` |
| Py\_CONSTANT\_EMPTY\_BYTES[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_EMPTY_BYTES "Link to this definition") | `8` | `b''` |
| Py\_CONSTANT\_EMPTY\_TUPLE[¶](https://docs.python.org/3/c-api/object.html#c.Py_CONSTANT_EMPTY_TUPLE "Link to this definition") | `9` | `()` |

Numeric values are only given for projects which cannot use the constant identifiers.

Added in version 3.13.

**CPython implementation detail:** In CPython, all of these constants are [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_GetConstantBorrowed(unsigned int constant\_id)[¶](https://docs.python.org/3/c-api/object.html#c.Py_GetConstantBorrowed "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Similar to [`Py_GetConstant()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstant "Py_GetConstant")
, but return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
.

This function is primarily intended for backwards compatibility: using [`Py_GetConstant()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstant "Py_GetConstant")
 is recommended for new code.

The reference is borrowed from the interpreter, and is valid until the interpreter finalization.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_NotImplemented[¶](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "Link to this definition")
  

The `NotImplemented` singleton, used to signal that an operation is not implemented for the given type combination.

Py\_RETURN\_NOTIMPLEMENTED[¶](https://docs.python.org/3/c-api/object.html#c.Py_RETURN_NOTIMPLEMENTED "Link to this definition")
  

Properly handle returning [`Py_NotImplemented`](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "Py_NotImplemented")
 from within a C function (that is, create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 and return it).

Py\_PRINT\_RAW[¶](https://docs.python.org/3/c-api/object.html#c.Py_PRINT_RAW "Link to this definition")
  

Flag to be used with multiple functions that print the object (like [`PyObject_Print()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Print "PyObject_Print")
 and [`PyFile_WriteObject()`](https://docs.python.org/3/c-api/file.html#c.PyFile_WriteObject "PyFile_WriteObject")
). If passed, these functions use the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of the object instead of the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
.

int PyObject\_Print([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, FILE \*fp, int flags)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Print "Link to this definition")
  

Print an object _o_, on file _fp_. Returns `-1` on error. The flags argument is used to enable certain printing options. The only option currently supported is [`Py_PRINT_RAW`](https://docs.python.org/3/c-api/object.html#c.Py_PRINT_RAW "Py_PRINT_RAW")
; if given, the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of the object is written instead of the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
.

void PyObject\_Dump([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Dump "Link to this definition")
  

Dump an object _op_ to `stderr`. This should only be used for debugging.

The output is intended to try dumping objects even after memory corruption:

*   Information is written starting with fields that are the least likely to crash when accessed.
    
*   This function can be called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
    , but it’s not recommended to do so: it can cause deadlocks.
    
*   An object that does not belong to the current interpreter may be dumped, but this may also cause crashes or unintended behavior.
    
*   Implement a heuristic to detect if the object memory has been freed. Don’t display the object contents in this case, only its memory address.
    
*   The output format may change at any time.
    

Example of output:

object address  : 0x7f80124702c0
object refcount : 2
object type     : 0x9902e0
object type name: str
object repr     : 'abcdef'

Added in version 3.15.

int PyObject\_HasAttrWithError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrWithError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Returns `1` if _o_ has the attribute _attr\_name_, and `0` otherwise. This is equivalent to the Python expression `hasattr(o, attr_name)`. On failure, return `-1`.

Added in version 3.13.

int PyObject\_HasAttrStringWithError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrStringWithError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

This is the same as [`PyObject_HasAttrWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrWithError "PyObject_HasAttrWithError")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

int PyObject\_HasAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns `1` if _o_ has the attribute _attr\_name_, and `0` otherwise. This function always succeeds.

Note

Exceptions that occur when this calls [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 and [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 methods aren’t propagated, but instead given to [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
. For proper error handling, use [`PyObject_HasAttrWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrWithError "PyObject_HasAttrWithError")
, [`PyObject_GetOptionalAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr")
 or [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
 instead.

int PyObject\_HasAttrString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_HasAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Note

Exceptions that occur when this calls [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 and [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 methods or while creating the temporary [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object are silently ignored. For proper error handling, use [`PyObject_HasAttrStringWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrStringWithError "PyObject_HasAttrStringWithError")
, [`PyObject_GetOptionalAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttrString "PyObject_GetOptionalAttrString")
 or [`PyObject_GetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString "PyObject_GetAttrString")
 instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GetAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Retrieve an attribute named _attr\_name_ from object _o_. Returns the attribute value on success, or `NULL` on failure. This is the equivalent of the Python expression `o.attr_name`.

If the missing attribute should not be treated as a failure, you can use [`PyObject_GetOptionalAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr")
 instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GetAttrString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

If the missing attribute should not be treated as a failure, you can use [`PyObject_GetOptionalAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttrString "PyObject_GetOptionalAttrString")
 instead.

int PyObject\_GetOptionalAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result);[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Variant of [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
 which doesn’t raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 if the attribute is not found.

If the attribute is found, return `1` and set _\*result_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the attribute. If the attribute is not found, return `0` and set _\*result_ to `NULL`; the [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 is silenced. If an error other than `AttributeError` is raised, return `-1` and set _\*result_ to `NULL`.

Added in version 3.13.

int PyObject\_GetOptionalAttrString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, const char \*attr\_name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result);[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

This is the same as [`PyObject_GetOptionalAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GenericGetAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetAttr "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic attribute getter function that is meant to be put into a type object’s `tp_getattro` slot. It looks for a descriptor in the dictionary of classes in the object’s MRO as well as an attribute in the object’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 (if present). As outlined in [Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html#descriptors)
, data descriptors take preference over instance attributes, while non-data descriptors don’t. Otherwise, an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 is raised.

int PyObject\_SetAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the value of the attribute named _attr\_name_, for object _o_, to the value _v_. Raise an exception and return `-1` on failure; return `0` on success. This is the equivalent of the Python statement `o.attr_name = v`.

If _v_ is `NULL`, the attribute is deleted. This behaviour is deprecated in favour of using [`PyObject_DelAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttr "PyObject_DelAttr")
, but there are currently no plans to remove it.

The function must not be called with a `NULL` _v_ and an exception set. This case can arise from forgetting `NULL` checks and would delete the attribute.

Changed in version 3.15: Must not be called with NULL value if an exception is set.

int PyObject\_SetAttrString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*attr\_name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_SetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "PyObject_SetAttr")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

If _v_ is `NULL`, the attribute is deleted, but this feature is deprecated in favour of using [`PyObject_DelAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttrString "PyObject_DelAttrString")
.

The function must not be called with a `NULL` _v_ and an exception set. This case can arise from forgetting `NULL` checks and would delete the attribute.

The number of different attribute names passed to this function should be kept small, usually by using a statically allocated string as _attr\_name_. For attribute names that aren’t known at compile time, prefer calling [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 and [`PyObject_SetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "PyObject_SetAttr")
 directly. For more details, see [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
, which may be used internally to create a key object.

Changed in version 3.15: Must not be called with NULL value if an exception is set.

int PyObject\_GenericSetAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic attribute setter and deleter function that is meant to be put into a type object’s [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
 slot. It looks for a data descriptor in the dictionary of classes in the object’s MRO, and if found it takes preference over setting or deleting the attribute in the instance dictionary. Otherwise, the attribute is set or deleted in the object’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 (if present). On success, `0` is returned, otherwise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 is raised and `-1` is returned.

int PyObject\_DelAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Delete attribute named _attr\_name_, for object _o_. Returns `-1` on failure. This is the equivalent of the Python statement `del o.attr_name`.

int PyObject\_DelAttrString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*attr\_name)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

This is the same as [`PyObject_DelAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttr "PyObject_DelAttr")
, but _attr\_name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

The number of different attribute names passed to this function should be kept small, usually by using a statically allocated string as _attr\_name_. For attribute names that aren’t known at compile time, prefer calling [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 and [`PyObject_DelAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttr "PyObject_DelAttr")
 directly. For more details, see [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
, which may be used internally to create a key object for lookup.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GenericGetDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, void \*context)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetDict "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

A generic implementation for the getter of a `__dict__` descriptor. It creates the dictionary if necessary.

This function may also be called to get the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 of the object _o_. Pass `NULL` for _context_ when calling it. Since this function may need to allocate memory for the dictionary, it may be more efficient to call [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
 when accessing an attribute on the object.

On failure, returns `NULL` with an exception set.

Added in version 3.3.

int PyObject\_GenericSetDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, void \*context)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetDict "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

A generic implementation for the setter of a `__dict__` descriptor. This implementation does not allow the dictionary to be deleted.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*\_PyObject\_GetDictPtr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c._PyObject_GetDictPtr "Link to this definition")
  

Return a pointer to [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 of the object _obj_. If there is no `__dict__`, return `NULL` without setting an exception.

This function may need to allocate memory for the dictionary, so it may be more efficient to call [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
 when accessing an attribute on the object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_RichCompare([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2, int opid)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compare the values of _o1_ and _o2_ using the operation specified by _opid_, which must be one of [`Py_LT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_LT "Py_LT")
, [`Py_LE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_LE "Py_LE")
, [`Py_EQ`](https://docs.python.org/3/c-api/typeobj.html#c.Py_EQ "Py_EQ")
, [`Py_NE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_NE "Py_NE")
, [`Py_GT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_GT "Py_GT")
, or [`Py_GE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_GE "Py_GE")
, corresponding to `<`, `<=`, `==`, `!=`, `>`, or `>=` respectively. This is the equivalent of the Python expression `o1 op o2`, where `op` is the operator corresponding to _opid_. Returns the value of the comparison on success, or `NULL` on failure.

int PyObject\_RichCompareBool([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2, int opid)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompareBool "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compare the values of _o1_ and _o2_ using the operation specified by _opid_, like [`PyObject_RichCompare()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "PyObject_RichCompare")
, but returns `-1` on error, `0` if the result is false, `1` otherwise.

Note

If _o1_ and _o2_ are the same object, [`PyObject_RichCompareBool()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompareBool "PyObject_RichCompareBool")
 will always return `1` for [`Py_EQ`](https://docs.python.org/3/c-api/typeobj.html#c.Py_EQ "Py_EQ")
 and `0` for [`Py_NE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_NE "Py_NE")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Format([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*format\_spec)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Format "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Format _obj_ using _format\_spec_. This is equivalent to the Python expression `format(obj, format_spec)`.

_format\_spec_ may be `NULL`. In this case the call is equivalent to `format(obj)`. Returns the formatted string on success, `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Repr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compute a string representation of object _o_. Returns the string representation on success, `NULL` on failure. This is the equivalent of the Python expression `repr(o)`. Called by the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 built-in function.

If argument is `NULL`, return the string `'<NULL>'`.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_ASCII([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_ASCII "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

As [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
, compute a string representation of object _o_, but escape the non-ASCII characters in the string returned by `PyObject_Repr()` with `\x`, `\u` or `\U` escapes. This generates a string similar to that returned by `PyObject_Repr()` in Python 2. Called by the [`ascii()`](https://docs.python.org/3/builtins/functions.html#ascii "ascii")
 built-in function.

If argument is `NULL`, return the string `'<NULL>'`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Str([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compute a string representation of object _o_. Returns the string representation on success, `NULL` on failure. This is the equivalent of the Python expression `str(o)`. Called by the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 built-in function and, therefore, by the [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function.

If argument is `NULL`, return the string `'<NULL>'`.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Bytes([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Bytes "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compute a bytes representation of object _o_. `NULL` is returned on failure and a bytes object on success. This is equivalent to the Python expression `bytes(o)`, when _o_ is not an integer. Unlike `bytes(o)`, a TypeError is raised when _o_ is an integer instead of a zero-initialized bytes object.

If argument is `NULL`, return the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object `b'<NULL>'`.

int PyObject\_IsSubclass([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*derived, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cls)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_IsSubclass "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if the class _derived_ is identical to or derived from the class _cls_, otherwise return `0`. In case of an error, return `-1`.

If _cls_ is a tuple, the check will be done against every entry in _cls_. The result will be `1` when at least one of the checks returns `1`, otherwise it will be `0`.

If _cls_ has a [`__subclasscheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__ "type.__subclasscheck__")
 method, it will be called to determine the subclass status as described in [**PEP 3119**](https://peps.python.org/pep-3119/)
. Otherwise, _derived_ is a subclass of _cls_ if it is a direct or indirect subclass, i.e. if _cls_ is contained in [`derived.__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__")
.

Normally only class objects, i.e. instances of [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 or a derived class, are considered classes. However, objects can override this by having a [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
 attribute (which must be a tuple of base classes).

int PyObject\_IsInstance([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*inst, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cls)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_IsInstance "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if _inst_ is an instance of the class _cls_ or a subclass of _cls_, or `0` if not. On error, returns `-1` and sets an exception.

If _cls_ is a tuple, the check will be done against every entry in _cls_. The result will be `1` when at least one of the checks returns `1`, otherwise it will be `0`.

If _cls_ has a [`__instancecheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__instancecheck__ "type.__instancecheck__")
 method, it will be called to determine the subclass status as described in [**PEP 3119**](https://peps.python.org/pep-3119/)
. Otherwise, _inst_ is an instance of _cls_ if its class is a subclass of _cls_.

An instance _inst_ can override what is considered its class by having a [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__")
 attribute.

An object _cls_ can override if it is considered a class, and what its base classes are, by having a [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
 attribute (which must be a tuple of base classes).

[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
 PyObject\_Hash([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Compute and return the hash value of an object _o_. On failure, return `-1`. This is the equivalent of the Python expression `hash(o)`.

Changed in version 3.2: The return type is now Py\_hash\_t. This is a signed integer the same size as [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
.

[Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
 PyObject\_HashNotImplemented([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 indicating that `type(o)` is not [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 and return `-1`. This function receives special treatment when stored in a `tp_hash` slot, allowing a type to explicitly indicate to the interpreter that it is not hashable.

int PyObject\_IsTrue([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_IsTrue "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns `1` if the object _o_ is considered to be true, and `0` otherwise. This is equivalent to the Python expression `not not o`. On failure, return `-1`.

int PyObject\_Not([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Not "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns `0` if the object _o_ is considered to be true, and `1` otherwise. This is equivalent to the Python expression `not o`. On failure, return `-1`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Type([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Type "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

When _o_ is non-`NULL`, returns a type object corresponding to the object type of object _o_. On failure, raises [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 and returns `NULL`. This is equivalent to the Python expression `type(o)`. This function creates a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the return value. There’s really no reason to use this function instead of the [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
 function, which returns a pointer of type [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
\*, except when a new strong reference is needed.

int PyObject\_TypeCheck([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_TypeCheck "Link to this definition")
  

Return non-zero if the object _o_ is of type _type_ or a subtype of _type_, and `0` otherwise. Both parameters must be non-`NULL`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyObject\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Size "Link to this definition")
  

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyObject\_Length([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Length "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the length of object _o_. If the object _o_ provides either the sequence and mapping protocols, the sequence length is returned. On error, `-1` is returned. This is the equivalent to the Python expression `len(o)`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyObject\_LengthHint([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 defaultvalue)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_LengthHint "Link to this definition")
  

Return an estimated length for the object _o_. First try to return its actual length, then an estimate using [`__length_hint__()`](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__ "object.__length_hint__")
, and finally return the default value. On error return `-1`. This is the equivalent to the Python expression `operator.length_hint(o, defaultvalue)`.

Added in version 3.4.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return element of _o_ corresponding to the object _key_ or `NULL` on failure. This is the equivalent of the Python expression `o[key]`.

int PyObject\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Map the object _key_ to the value _v_. Raise an exception and return `-1` on failure; return `0` on success. This is the equivalent of the Python statement `o[key] = v`. This function _does not_ steal a reference to _v_.

int PyObject\_DelItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Remove the mapping for the object _key_ from the object _o_. Return `-1` on failure. This is equivalent to the Python statement `del o[key]`.

int PyObject\_DelItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItemString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Dir([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_Dir "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is equivalent to the Python expression `dir(o)`, returning a (possibly empty) list of strings appropriate for the object argument, or `NULL` if there was an error. If the argument is `NULL`, this is like the Python `dir()`, returning the names of the current locals; in this case, if no execution frame is active then `NULL` is returned but [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 will return false.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GetIter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetIter "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is equivalent to the Python expression `iter(o)`. It returns a new iterator for the object argument, or the object itself if the object is already an iterator. Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and returns `NULL` if the object cannot be iterated.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_SelfIter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_SelfIter "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is equivalent to the Python `__iter__(self): return self` method. It is intended for [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 types, to be used in the [`PyTypeObject.tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
 slot.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_GetAIter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAIter "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

This is the equivalent to the Python expression `aiter(o)`. Takes an `AsyncIterable` object and returns an `AsyncIterator` for it. This is typically a new iterator but if the argument is an `AsyncIterator`, this returns itself. Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and returns `NULL` if the object cannot be iterated.

Added in version 3.10.

void \*PyObject\_GetTypeData([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*cls)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Get a pointer to subclass-specific data reserved for _cls_.

The object _o_ must be an instance of _cls_, and _cls_ must have been created using negative [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
. Python does not check this.

On error, set an exception and return `NULL`.

Added in version 3.12.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyType\_GetTypeDataSize([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*cls)[¶](https://docs.python.org/3/c-api/object.html#c.PyType_GetTypeDataSize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Return the size of the instance memory space reserved for _cls_, i.e. the size of the memory [`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
 returns.

This may be larger than requested using [`-PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
; it is safe to use this larger size (e.g. with `memset()`).

The type _cls_ **must** have been created using negative [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
. Python does not check this.

On error, set an exception and return a negative value.

Added in version 3.12.

void \*PyObject\_GetItemData([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItemData "Link to this definition")
  

Get a pointer to per-item data for a class with [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END "Py_TPFLAGS_ITEMS_AT_END")
.

On error, set an exception and return `NULL`. [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if _o_ does not have [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END "Py_TPFLAGS_ITEMS_AT_END")
 set.

Added in version 3.12.

int PyObject\_VisitManagedDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [visitproc](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "visitproc")
 visit, void \*arg)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "Link to this definition")
  

Visit the managed dictionary of _obj_.

This function must only be called in a traverse function of the type which has the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 flag set.

Added in version 3.13.

void PyObject\_ClearManagedDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyObject_ClearManagedDict "Link to this definition")
  

Clear the managed dictionary of _obj_.

This function must only be called in a clear function of the type which has the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 flag set.

Added in version 3.13.

int PyUnstable\_Object\_EnableDeferredRefcount([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_EnableDeferredRefcount "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Enable [deferred reference counting](https://peps.python.org/pep-0703/#deferred-reference-counting)
 on _obj_, if supported by the runtime. In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, this allows the interpreter to avoid reference count adjustments to _obj_, which may improve multi-threaded performance. The tradeoff is that _obj_ will only be deallocated by the tracing garbage collector, and not when the interpreter no longer has any references to it.

This function returns `1` if deferred reference counting is enabled on _obj_, and `0` if deferred reference counting is not supported or if the hint was ignored by the interpreter, such as when deferred reference counting is already enabled on _obj_. This function is thread-safe, and cannot fail.

This function does nothing on builds with the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 enabled, which do not support deferred reference counting. This also does nothing if _obj_ is not an object tracked by the garbage collector (see [`gc.is_tracked()`](https://docs.python.org/3/library/gc.html#gc.is_tracked "gc.is_tracked")
 and [`PyObject_GC_IsTracked()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsTracked "PyObject_GC_IsTracked")
).

This function is intended to be used soon after _obj_ is created, by the code that creates it, such as in the object’s [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 slot.

Added in version 3.14.

int PyUnstable\_Object\_IsUniqueReferencedTemporary([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniqueReferencedTemporary "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Check if _obj_ is a unique temporary object. Returns `1` if _obj_ is known to be a unique temporary object, and `0` otherwise. This function cannot fail, but the check is conservative, and may return `0` in some cases even if _obj_ is a unique temporary object.

If an object is a unique temporary, it is guaranteed that the current code has the only reference to the object. For arguments to C functions, this should be used instead of checking if the reference count is `1`. Starting with Python 3.14, the interpreter internally avoids some reference count modifications when loading objects onto the operands stack by [borrowing](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 references when possible, which means that a reference count of `1` by itself does not guarantee that a function argument uniquely referenced.

In the example below, `my_func` is called with a unique temporary object as its argument:

my\_func(\[1, 2, 3\])

In the example below, `my_func` is **not** called with a unique temporary object as its argument, even if its refcount is `1`:

my\_list \= \[1, 2, 3\]
my\_func(my\_list)

See also the function [`Py_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
.

Added in version 3.14.

int PyUnstable\_IsImmortal([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_IsImmortal "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

This function returns non-zero if _obj_ is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
, and zero otherwise. This function cannot fail.

Note

Objects that are immortal in one CPython version are not guaranteed to be immortal in another.

Added in version 3.14.

int PyUnstable\_TryIncRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_TryIncRef "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Increments the reference count of _obj_ if it is not zero. Returns `1` if the object’s reference count was successfully incremented. Otherwise, this function returns `0`.

[`PyUnstable_EnableTryIncRef()`](https://docs.python.org/3/c-api/object.html#c.PyUnstable_EnableTryIncRef "PyUnstable_EnableTryIncRef")
 must have been called earlier on _obj_ or this function may spuriously return `0` in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
.

This function is logically equivalent to the following C code, except that it behaves atomically in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
:

if (Py\_REFCNT(op) \> 0) {
   Py\_INCREF(op);
   return 1;
}
return 0;

This is intended as a building block for managing weak references without the overhead of a Python [weak reference object](https://docs.python.org/3/c-api/weakref.html#weakrefobjects)
.

Typically, correct use of this function requires support from _obj_’s deallocator ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
). For example, the following sketch could be adapted to implement a “weakmap” that works like a [`WeakValueDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary "weakref.WeakValueDictionary")
 for a specific type:

PyMutex mutex;

PyObject \*
add\_entry(weakmap\_key\_type \*key, PyObject \*value)
{
    PyUnstable\_EnableTryIncRef(value);
    weakmap\_type weakmap \= ...;
    PyMutex\_Lock(&mutex);
    weakmap\_add\_entry(weakmap, key, value);
    PyMutex\_Unlock(&mutex);
    Py\_RETURN\_NONE;
}

PyObject \*
get\_value(weakmap\_key\_type \*key)
{
    weakmap\_type weakmap \= ...;
    PyMutex\_Lock(&mutex);
    PyObject \*result \= weakmap\_find(weakmap, key);
    if (PyUnstable\_TryIncRef(result)) {
        // \`result\` is safe to use
        PyMutex\_Unlock(&mutex);
        return result;
    }
    // if we get here, \`result\` is starting to be garbage-collected,
    // but has not been removed from the weakmap yet
    PyMutex\_Unlock(&mutex);
    return NULL;
}

// tp\_dealloc function for weakmap values
void
value\_dealloc(PyObject \*value)
{
    weakmap\_type weakmap \= ...;
    PyMutex\_Lock(&mutex);
    weakmap\_remove\_value(weakmap, value);

    ...
    PyMutex\_Unlock(&mutex);
}

Added in version 3.14.

void PyUnstable\_EnableTryIncRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_EnableTryIncRef "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Enables subsequent uses of [`PyUnstable_TryIncRef()`](https://docs.python.org/3/c-api/object.html#c.PyUnstable_TryIncRef "PyUnstable_TryIncRef")
 on _obj_. The caller must hold a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to _obj_ when calling this.

Added in version 3.14.

int PyUnstable\_Object\_IsUniquelyReferenced([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Determine if _op_ only has one reference.

On GIL-enabled builds, this function is equivalent to [Py\_REFCNT](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
([op](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced "op")
) \== 1.

On a [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, this checks if _op_’s [reference count](https://docs.python.org/3/glossary.html#term-reference-count)
 is equal to one and additionally checks if _op_ is only used by this thread. [Py\_REFCNT](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
([op](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced "op")
) \== 1 is **not** thread-safe on free-threaded builds; prefer this function.

The caller must hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
, despite the fact that this function doesn’t call into the Python interpreter. This function cannot fail.

Added in version 3.14.

int PyUnstable\_SetImmortal([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/object.html#c.PyUnstable_SetImmortal "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Marks the object _op_ [immortal](https://docs.python.org/3/glossary.html#term-immortal)
. The argument should be uniquely referenced by the calling thread. This is intended to be used for reducing reference counting contention in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 for objects which are shared across threads.

This is a one-way process: objects can only be made immortal; they cannot be made mortal once again. Immortal objects do not participate in reference counting and will never be garbage collected. If the object is GC-tracked, it is untracked.

This function is intended to be used soon after _op_ is created, by the code that creates it, such as in the object’s [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 slot. Returns 1 if the object was made immortal and returns 0 if it was not. This function cannot fail.

Added in version 3.15.

#### Previous topic

[Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html "previous chapter")

#### Next topic

[Call Protocol](https://docs.python.org/3/c-api/call.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Object+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fobject.html&pagesource=c-api%2Fobject.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/object.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/call.html "Call Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer")
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
*   [Object Protocol](https://docs.python.org/3/c-api/object.html)
    
*    
    
    |
*   Theme Auto Light Dark |