### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/slice.html "Slice Objects")
     |
*   [previous](https://docs.python.org/3/c-api/iterator.html "Iterator Objects")
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
*   [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Descriptor Objects[¶](https://docs.python.org/3/c-api/descriptor.html#descriptor-objects "Link to this heading")

=================================================================================================================

“Descriptors” are objects that describe some attribute of an object. They are found in the dictionary of type objects.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDescr\_NewGetSet([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, struct [PyGetSetDef](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 \*getset)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewGetSet "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new get-set descriptor for extension type _type_ from the [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structure _getset_.

Get-set descriptors expose attributes implemented by C getter and setter functions rather than stored directly in the instance. This is the same kind of descriptor created for entries in [`tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "PyTypeObject.tp_getset")
, and it appears in Python as a [`types.GetSetDescriptorType`](https://docs.python.org/3/library/types.html#types.GetSetDescriptorType "types.GetSetDescriptorType")
 object.

On success, return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the descriptor. Return `NULL` with an exception set on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDescr\_NewMember([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, struct [PyMemberDef](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 \*member)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMember "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new member descriptor for extension type _type_ from the [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 structure _member_.

Member descriptors expose fields in the type’s C struct as Python attributes. This is the same kind of descriptor created for entries in [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members")
, and it appears in Python as a [`types.MemberDescriptorType`](https://docs.python.org/3/library/types.html#types.MemberDescriptorType "types.MemberDescriptorType")
 object.

On success, return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the descriptor. Return `NULL` with an exception set on failure.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyMemberDescr\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyMemberDescr_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for member descriptor objects created from [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 structures. These descriptors expose fields of a C struct as attributes on a type, and correspond to [`types.MemberDescriptorType`](https://docs.python.org/3/library/types.html#types.MemberDescriptorType "types.MemberDescriptorType")
 objects in Python.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyGetSetDescr\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyGetSetDescr_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for get/set descriptor objects created from [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structures. These descriptors implement attributes whose value is computed by C getter and setter functions, and are used for many built-in type attributes. They correspond to [`types.GetSetDescriptorType`](https://docs.python.org/3/library/types.html#types.GetSetDescriptorType "types.GetSetDescriptorType")
 objects in Python.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDescr\_NewMethod([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, struct [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*meth)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMethod "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new method descriptor for extension type _type_ from the [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 structure _meth_.

Method descriptors expose C functions as methods on a type. This is the same kind of descriptor created for entries in [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods")
, and it appears in Python as a [`types.MethodDescriptorType`](https://docs.python.org/3/library/types.html#types.MethodDescriptorType "types.MethodDescriptorType")
 object.

On success, return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the descriptor. Return `NULL` with an exception set on failure.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyMethodDescr\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyMethodDescr_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for method descriptor objects created from [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 structures. These descriptors expose C functions as methods on a type, and correspond to [`types.MethodDescriptorType`](https://docs.python.org/3/library/types.html#types.MethodDescriptorType "types.MethodDescriptorType")
 objects in Python.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyWrapperDescr\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapperDescr_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for wrapper descriptor objects created by [`PyDescr_NewWrapper()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewWrapper "PyDescr_NewWrapper")
 and [`PyWrapper_New()`](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapper_New "PyWrapper_New")
.

Wrapper descriptors are used internally to expose special methods such as `__repr__` or `__add__`, which are implemented by type slots. The type is exposed in Python as [`types.WrapperDescriptorType`](https://docs.python.org/3/library/types.html#types.WrapperDescriptorType "types.WrapperDescriptorType")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDescr\_NewWrapper([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, struct [wrapperbase](https://docs.python.org/3/c-api/descriptor.html#c.wrapperbase "wrapperbase")
 \*base, void \*wrapped)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewWrapper "Link to this definition")
  

_Return value: New reference._

Create a new wrapper descriptor of type [`PyWrapperDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapperDescr_Type "PyWrapperDescr_Type")
.

This function is meant for internal use only; it and related API (`struct wrapperbase` and the `PyWrapperFlag_KEYWORDS` flag) are exposed publicly for backwards compatibility reasons.

See [`PyCMethod_New()`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_New "PyCMethod_New")
 for wrapping a C function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDescr\_NewClassMethod([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*method)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewClassMethod "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new class method descriptor for extension type _type_ from the [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 structure _method_.

Class method descriptors expose C methods that receive the class rather than an instance when accessed. This is the same kind of descriptor created for `METH_CLASS` entries in [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods")
, and it appears in Python as a [`types.ClassMethodDescriptorType`](https://docs.python.org/3/library/types.html#types.ClassMethodDescriptorType "types.ClassMethodDescriptorType")
 object.

On success, return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the descriptor. Return `NULL` with an exception set on failure.

int PyDescr\_IsData([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*descr)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_IsData "Link to this definition")
  

Return non-zero if the descriptor object _descr_ describes a data attribute, or `0` if it describes a method. _descr_ must be a descriptor object; there is no error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyWrapper\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*d, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapper_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new bound wrapper object from the wrapper descriptor _d_ and the instance _self_.

This is the bound form of a wrapper descriptor created by [`PyDescr_NewWrapper()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewWrapper "PyDescr_NewWrapper")
. CPython creates these objects when a slot wrapper is accessed through an instance, and they appear in Python as [`types.MethodWrapperType`](https://docs.python.org/3/library/types.html#types.MethodWrapperType "types.MethodWrapperType")
 objects.

On success, return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the wrapper object. Return `NULL` with an exception set on failure.

PyDescr\_TYPE(descr)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_TYPE "Link to this definition")
  

Return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the type that the descriptor _descr_ belongs to. This is accessible as [`__objclass__`](https://docs.python.org/3/reference/datamodel.html#object.__objclass__ "object.__objclass__")
 in Python.

_descr_ must be a descriptor object created by one of the `PyDescr_New*` functions (an instance of [`PyMethodDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyMethodDescr_Type "PyMethodDescr_Type")
, [`PyClassMethodDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethodDescr_Type "PyClassMethodDescr_Type")
, [`PyMemberDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyMemberDescr_Type "PyMemberDescr_Type")
, [`PyGetSetDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyGetSetDescr_Type "PyGetSetDescr_Type")
, or [`PyWrapperDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapperDescr_Type "PyWrapperDescr_Type")
). If the passed descriptor is not an instance of one of these types, the behavior is undefined.

PyDescr\_NAME(descr)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NAME "Link to this definition")
  

Return the name of the descriptor _descr_ as a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object. This is available as [`__name__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")
 in Python.

_descr_ must be a descriptor object created by one of the `PyDescr_New*` functions. If not, the behavior is undefined.

PyDescr\_COMMON[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_COMMON "Link to this definition")
  

This is a macro including the common fields for a descriptor object.

This was included in Python’s C API by mistake; do not use it in extensions. For creating custom descriptor objects, create a class implementing the descriptor protocol ([`tp_descr_get`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_get "PyTypeObject.tp_descr_get")
 and [`tp_descr_set`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_set "PyTypeObject.tp_descr_set")
).

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Built-in descriptors[¶](https://docs.python.org/3/c-api/descriptor.html#built-in-descriptors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyProperty\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyProperty_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for property objects. This is the same object as [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PySuper\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PySuper_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for super objects. This is the same object as [`super`](https://docs.python.org/3/builtins/functions.html#super "super")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyClassMethod\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethod_Type "Link to this definition")
  

The type of class method objects. This is the same object as [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyClassMethodDescr\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethodDescr_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for C-level class method descriptor objects. This is the type of the descriptors created for [`classmethod()`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 defined in C extension types, and corresponds to [`types.ClassMethodDescriptorType`](https://docs.python.org/3/library/types.html#types.ClassMethodDescriptorType "types.ClassMethodDescriptorType")
 objects in Python.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyClassMethod\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethod_New "Link to this definition")
  

Create a new [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 object wrapping _callable_. _callable_ must be a callable object and must not be `NULL`.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a new class method descriptor. On failure, this function returns `NULL` with an exception set.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyStaticMethod\_Type[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyStaticMethod_Type "Link to this definition")
  

The type of static method objects. This is the same object as [`staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 in the Python layer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyStaticMethod\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable)[¶](https://docs.python.org/3/c-api/descriptor.html#c.PyStaticMethod_New "Link to this definition")
  

Create a new [`staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 object wrapping _callable_. _callable_ must be a callable object and must not be `NULL`.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a new static method descriptor. On failure, this function returns `NULL` with an exception set.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html#)
    *   [Built-in descriptors](https://docs.python.org/3/c-api/descriptor.html#built-in-descriptors)
        

#### Previous topic

[Iterator Objects](https://docs.python.org/3/c-api/iterator.html "previous chapter")

#### Next topic

[Slice Objects](https://docs.python.org/3/c-api/slice.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Descriptor+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fdescriptor.html&pagesource=c-api%2Fdescriptor.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/descriptor.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/slice.html "Slice Objects")
     |
*   [previous](https://docs.python.org/3/c-api/iterator.html "Iterator Objects")
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
*   [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html)
    
*    
    
    |
*   Theme Auto Light Dark |