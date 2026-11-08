### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/list.html "List Objects")
     |
*   [previous](https://docs.python.org/3/c-api/unicode.html "Unicode Objects and Codecs")
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
*   [Tuple Objects](https://docs.python.org/3/c-api/tuple.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Tuple Objects[¶](https://docs.python.org/3/c-api/tuple.html#tuple-objects "Link to this heading")

==================================================================================================

type PyTupleObject[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python tuple object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyTuple\_Type[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python tuple type; it is the same object as [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 in the Python layer.

int PyTuple\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Check "Link to this definition")
  

Return true if _p_ is a tuple object or an instance of a subtype of the tuple type. This function always succeeds.

int PyTuple\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_CheckExact "Link to this definition")
  

Return true if _p_ is a tuple object, but not an instance of a subtype of the tuple type. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_New([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new tuple object of size _len_, or `NULL` with an exception set on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_FromArray([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*array, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_FromArray "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Create a tuple of _size_ items and copy references from _array_ to the new tuple.

_array_ can be NULL if _size_ is `0`.

On success, return a new reference. On error, set an exception and return `NULL`.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_Pack([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 n, ...)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Pack "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new tuple object of size _n_, or `NULL` with an exception set on failure. The tuple values are initialized to the subsequent _n_ C arguments pointing to Python objects. `PyTuple_Pack(2, a, b)` is equivalent to `Py_BuildValue("(OO)", a, b)`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyTuple\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Take a pointer to a tuple object, and return the size of that tuple. On error, return `-1` with an exception set.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyTuple\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GET_SIZE "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Like [`PyTuple_Size()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Size "PyTuple_Size")
, but without error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return the object at position _pos_ in the tuple pointed to by _p_. If _pos_ is negative or out of bounds, return `NULL` and set an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 exception.

The returned reference is borrowed from the tuple _p_ (that is: it is only valid as long as you hold a reference to _p_). To get a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
, use [`Py_NewRef(PyTuple_GetItem(...))`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef")
 or [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_GET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GET_ITEM "Link to this definition")
  

_Return value: Borrowed reference._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Like [`PyTuple_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem "PyTuple_GetItem")
, but does no checking of its arguments.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTuple\_GetSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 low, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 high)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetSlice "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the slice of the tuple pointed to by _p_ between _low_ and _high_, or `NULL` with an exception set on failure.

This is the equivalent of the Python expression `p[low:high]`. Indexing from the end of the tuple is not supported.

int PyTuple\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Insert a reference to object _o_ at position _pos_ of the tuple pointed to by _p_. Return `0` on success. If _pos_ is out of bounds, return `-1` and set an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 exception. This function should only be used to fill in brand new tuples; using it on an existing tuple is thread-unsafe.

Note

This function “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _o_ and discards a reference to an item already in the tuple at the affected position (unless it was NULL).

void PyTuple\_SET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SET_ITEM "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Like [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
, but does no error checking, and should _only_ be used to fill in brand new tuples, using it on an existing tuple is thread-unsafe.

Bounds checking is performed as an assertion if Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 or [`with assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
.

Note

This function “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _o_, and, unlike [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
, does _not_ discard a reference to any item that is being replaced; any reference in the tuple at position _pos_ will be leaked.

Warning

This macro should _only_ be used on tuples that are newly created. Using this macro on a tuple that is already in use (or in other words, has a refcount > 1) could lead to undefined behavior.

int \_PyTuple\_Resize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 newsize)[¶](https://docs.python.org/3/c-api/tuple.html#c._PyTuple_Resize "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Can be used to resize a tuple. _newsize_ will be the new length of the tuple. Because tuples are _supposed_ to be immutable, this should only be used if there is only one reference to the object. Do _not_ use this if the tuple may already be known to some other part of the code. The tuple will always grow or shrink at the end. Think of this as destroying the old tuple and creating a new one, only more efficiently. Returns `0` on success. Client code should never assume that the resulting value of `*p` will be the same as before calling this function. If the object referenced by `*p` is replaced, the original `*p` is destroyed. On failure, returns `-1` and sets `*p` to `NULL`, and raises [`MemoryError`](https://docs.python.org/3/builtins/exceptions.html#MemoryError "MemoryError")
 or [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
.

Struct Sequence Objects[¶](https://docs.python.org/3/c-api/tuple.html#struct-sequence-objects "Link to this heading")

======================================================================================================================

A struct sequence object is a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
, that is, a sequence whose items can also be accessed through attributes. It is similar to [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
, but provides a slightly different interface.

To create a struct sequence, you first have to create a specific struct sequence type.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*PyStructSequence\_NewType([PyStructSequence\_Desc](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "PyStructSequence_Desc")
 \*desc)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_NewType "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Create a new struct sequence type from the data in _desc_, described below. Instances of the resulting type can be created with [`PyStructSequence_New()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_New "PyStructSequence_New")
.

Return `NULL` with an exception set on failure.

void PyStructSequence\_InitType([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [PyStructSequence\_Desc](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "PyStructSequence_Desc")
 \*desc)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_InitType "Link to this definition")
  

_Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Initializes a struct sequence type _type_ from _desc_ in place.

int PyStructSequence\_InitType2([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [PyStructSequence\_Desc](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "PyStructSequence_Desc")
 \*desc)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_InitType2 "Link to this definition")
  

_Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Like [`PyStructSequence_InitType()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_InitType "PyStructSequence_InitType")
, but returns `0` on success and `-1` with an exception set on failure.

Added in version 3.4.

type PyStructSequence\_Desc[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Contains the meta information of a struct sequence type to create.

const char \*name[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc.name "Link to this definition")
  

Fully qualified name of the type; null-terminated UTF-8 encoded. The name must contain the module name.

const char \*doc[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc.doc "Link to this definition")
  

Pointer to docstring for the type or `NULL` to omit.

[PyStructSequence\_Field](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Field "PyStructSequence_Field")
 \*fields[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc.fields "Link to this definition")
  

Pointer to `NULL`\-terminated array with field names of the new type.

int n\_in\_sequence[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc.n_in_sequence "Link to this definition")
  

Number of fields visible to the Python side (if used as tuple).

type PyStructSequence\_Field[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Field "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Describes a field of a struct sequence. As a struct sequence is modeled as a tuple, all fields are typed as [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*. The index in the [`fields`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc.fields "PyStructSequence_Desc.fields")
 array of the [`PyStructSequence_Desc`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "PyStructSequence_Desc")
 determines which field of the struct sequence is described.

const char \*name[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Field.name "Link to this definition")
  

Name for the field or `NULL` to end the list of named fields, set to [`PyStructSequence_UnnamedField`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_UnnamedField "PyStructSequence_UnnamedField")
 to leave unnamed.

const char \*doc[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Field.doc "Link to this definition")
  

Field docstring or `NULL` to omit.

const char \*const PyStructSequence\_UnnamedField[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_UnnamedField "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Special value for a field name to leave it unnamed.

Changed in version 3.9: The type was changed from `char *`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyStructSequence\_New([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Creates an instance of _type_, which must have been created with [`PyStructSequence_NewType()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_NewType "PyStructSequence_NewType")
.

Return `NULL` with an exception set on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyStructSequence\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_GetItem "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return the object at position _pos_ in the struct sequence pointed to by _p_. The returned reference is borrowed from the struct sequence _p_ (that is: it is only valid as long as you hold a reference to _p_).

Bounds checking is performed as an assertion if Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 or [`with assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyStructSequence\_GET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_GET_ITEM "Link to this definition")
  

_Return value: Borrowed reference._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Alias to [`PyStructSequence_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_GetItem "PyStructSequence_GetItem")
.

Changed in version 3.13: Now implemented as an alias to [`PyStructSequence_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_GetItem "PyStructSequence_GetItem")
.

void PyStructSequence\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 pos, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Sets the field at index _pos_ of the struct sequence _p_ to value _o_. Like [`PyTuple_SET_ITEM()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SET_ITEM "PyTuple_SET_ITEM")
, this should only be used to fill in brand new instances.

Bounds checking is performed as an assertion if Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 or [`with assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
.

Note

This function “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _o_.

void PyStructSequence\_SET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*pos, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_SET_ITEM "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Alias to [`PyStructSequence_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_SetItem "PyStructSequence_SetItem")
.

Changed in version 3.13: Now implemented as an alias to [`PyStructSequence_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_SetItem "PyStructSequence_SetItem")
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Tuple Objects](https://docs.python.org/3/c-api/tuple.html#)
    
*   [Struct Sequence Objects](https://docs.python.org/3/c-api/tuple.html#struct-sequence-objects)
    

#### Previous topic

[Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html "previous chapter")

#### Next topic

[List Objects](https://docs.python.org/3/c-api/list.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Tuple+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftuple.html&pagesource=c-api%2Ftuple.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/tuple.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/list.html "List Objects")
     |
*   [previous](https://docs.python.org/3/c-api/unicode.html "Unicode Objects and Codecs")
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
*   [Tuple Objects](https://docs.python.org/3/c-api/tuple.html)
    
*    
    
    |
*   Theme Auto Light Dark |