### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sentinel.html "Sentinel objects")
     |
*   [previous](https://docs.python.org/3/c-api/weakref.html "Weak Reference Objects")
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
*   [Capsules](https://docs.python.org/3/c-api/capsule.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Capsules[¶](https://docs.python.org/3/c-api/capsule.html#capsules "Link to this heading")

==========================================================================================

Refer to [Providing a C API for an Extension Module](https://docs.python.org/3/extending/extending.html#using-capsules)
 for more information on using these objects.

Added in version 3.1.

type PyCapsule[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents an opaque value, useful for C extension modules which need to pass an opaque value (as a void\* pointer) through Python code to other C code. It is often used to make a C function pointer defined in one module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCapsule\_Type[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object corresponding to capsule objects. This is the same object as [`types.CapsuleType`](https://docs.python.org/3/library/types.html#types.CapsuleType "types.CapsuleType")
 in the Python layer.

type PyCapsule\_Destructor[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Destructor "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type of a destructor callback for a capsule. Defined as:

typedef void (\*PyCapsule\_Destructor)(PyObject \*);

See [`PyCapsule_New()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_New "PyCapsule_New")
 for the semantics of PyCapsule\_Destructor callbacks.

int PyCapsule\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_CheckExact "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return true if its argument is a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "PyCapsule")
. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCapsule\_New(void \*pointer, const char \*name, [PyCapsule\_Destructor](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Destructor "PyCapsule_Destructor")
 destructor)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Create a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "PyCapsule")
 encapsulating the _pointer_. The _pointer_ argument may not be `NULL`.

On failure, set an exception and return `NULL`.

The _name_ string may either be `NULL` or a pointer to a valid C string. If non-`NULL`, this string must outlive the capsule. (Though it is permitted to free it inside the _destructor_.)

If the _destructor_ argument is not `NULL`, it will be called with the capsule as its argument when it is destroyed.

If this capsule will be stored as an attribute of a module, the _name_ should be specified as `modulename.attributename`. This will enable other modules to import the capsule using [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "PyCapsule_Import")
.

void \*PyCapsule\_GetPointer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, const char \*name)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetPointer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Retrieve the _pointer_ stored in the capsule. On failure, set an exception and return `NULL`.

The _name_ parameter must compare exactly to the name stored in the capsule. If the name stored in the capsule is `NULL`, the _name_ passed in must also be `NULL`. Python uses the C function `strcmp()` to compare capsule names.

[PyCapsule\_Destructor](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Destructor "PyCapsule_Destructor")
 PyCapsule\_GetDestructor([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetDestructor "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Return the current destructor stored in the capsule. On failure, set an exception and return `NULL`.

It is legal for a capsule to have a `NULL` destructor. This makes a `NULL` return code somewhat ambiguous; use [`PyCapsule_IsValid()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "PyCapsule_IsValid")
 or [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

void \*PyCapsule\_GetContext([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetContext "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Return the current context stored in the capsule. On failure, set an exception and return `NULL`.

It is legal for a capsule to have a `NULL` context. This makes a `NULL` return code somewhat ambiguous; use [`PyCapsule_IsValid()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "PyCapsule_IsValid")
 or [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

const char \*PyCapsule\_GetName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Return the current name stored in the capsule. On failure, set an exception and return `NULL`.

It is legal for a capsule to have a `NULL` name. This makes a `NULL` return code somewhat ambiguous; use [`PyCapsule_IsValid()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "PyCapsule_IsValid")
 or [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

void \*PyCapsule\_Import(const char \*name, int no\_block)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Import a pointer to a C object from a capsule attribute in a module. The _name_ parameter should specify the full name to the attribute, as in `module.attribute`. The _name_ stored in the capsule must match this string exactly.

This function splits _name_ on the `.` character, and imports the first element. It then processes further elements using attribute lookups.

Return the capsule’s internal _pointer_ on success. On failure, set an exception and return `NULL`.

Note

If _name_ points to an attribute of some submodule or subpackage, this submodule or subpackage must be previously imported using other means (for example, by using [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
) for the attribute lookups to succeed.

Changed in version 3.3: _no\_block_ has no effect anymore.

int PyCapsule\_IsValid([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, const char \*name)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Determines whether or not _capsule_ is a valid capsule. A valid capsule is non-`NULL`, passes [`PyCapsule_CheckExact()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_CheckExact "PyCapsule_CheckExact")
, has a non-`NULL` pointer stored in it, and its internal name matches the _name_ parameter. (See [`PyCapsule_GetPointer()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetPointer "PyCapsule_GetPointer")
 for information on how capsule names are compared.)

In other words, if [`PyCapsule_IsValid()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "PyCapsule_IsValid")
 returns a true value, calls to any of the accessors (any function starting with `PyCapsule_Get`) are guaranteed to succeed.

Return a nonzero value if the object is valid and matches the name passed in. Return `0` otherwise. This function will not fail.

int PyCapsule\_SetContext([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, void \*context)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetContext "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Set the context pointer inside _capsule_ to _context_.

Return `0` on success. Return nonzero and set an exception on failure.

int PyCapsule\_SetDestructor([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, [PyCapsule\_Destructor](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Destructor "PyCapsule_Destructor")
 destructor)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetDestructor "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Set the destructor inside _capsule_ to _destructor_.

Return `0` on success. Return nonzero and set an exception on failure.

int PyCapsule\_SetName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, const char \*name)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Set the name inside _capsule_ to _name_. If non-`NULL`, the name must outlive the capsule. If the previous _name_ stored in the capsule was not `NULL`, no attempt is made to free it.

Return `0` on success. Return nonzero and set an exception on failure.

int PyCapsule\_SetPointer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*capsule, void \*pointer)[¶](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetPointer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Set the void pointer inside _capsule_ to _pointer_. The pointer may not be `NULL`.

Return `0` on success. Return nonzero and set an exception on failure.

#### Previous topic

[Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html "previous chapter")

#### Next topic

[Sentinel objects](https://docs.python.org/3/c-api/sentinel.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Capsules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcapsule.html&pagesource=c-api%2Fcapsule.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/capsule.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/sentinel.html "Sentinel objects")
     |
*   [previous](https://docs.python.org/3/c-api/weakref.html "Weak Reference Objects")
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
*   [Capsules](https://docs.python.org/3/c-api/capsule.html)
    
*    
    
    |
*   Theme Auto Light Dark |