### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/building.html "Building C and C++ Extensions")
     |
*   [previous](https://docs.python.org/3/extending/newtypes_tutorial.html "Defining Extension Types: Tutorial")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Defining Extension Types: Assorted Topics[¶](https://docs.python.org/3/extending/newtypes.html#defining-extension-types-assorted-topics "Link to this heading")

================================================================================================================================================================

This section aims to give a quick fly-by on the various type methods you can implement and what they do.

Here is the definition of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
, with some fields only used in [debug builds](https://docs.python.org/3/using/configure.html#debug-build)
 omitted:

typedef struct \_typeobject {
    PyObject\_VAR\_HEAD
    const char \*tp\_name; /\* For printing, in format "<module>.<name>" \*/
    Py\_ssize\_t tp\_basicsize, tp\_itemsize; /\* For allocation \*/

    /\* Methods to implement standard operations \*/

    destructor tp\_dealloc;
    Py\_ssize\_t tp\_vectorcall\_offset;
    getattrfunc tp\_getattr;
    setattrfunc tp\_setattr;
    PyAsyncMethods \*tp\_as\_async; /\* formerly known as tp\_compare (Python 2)
                                    or tp\_reserved (Python 3) \*/
    reprfunc tp\_repr;

    /\* Method suites for standard classes \*/

    PyNumberMethods \*tp\_as\_number;
    PySequenceMethods \*tp\_as\_sequence;
    PyMappingMethods \*tp\_as\_mapping;

    /\* More standard operations (here for binary compatibility) \*/

    hashfunc tp\_hash;
    ternaryfunc tp\_call;
    reprfunc tp\_str;
    getattrofunc tp\_getattro;
    setattrofunc tp\_setattro;

    /\* Functions to access object as input/output buffer \*/
    PyBufferProcs \*tp\_as\_buffer;

    /\* Flags to define presence of optional/expanded features \*/
    unsigned long tp\_flags;

    const char \*tp\_doc; /\* Documentation string \*/

    /\* Assigned meaning in release 2.0 \*/
    /\* call function for all accessible objects \*/
    traverseproc tp\_traverse;

    /\* delete references to contained objects \*/
    inquiry tp\_clear;

    /\* Assigned meaning in release 2.1 \*/
    /\* rich comparisons \*/
    richcmpfunc tp\_richcompare;

    /\* weak reference enabler \*/
    Py\_ssize\_t tp\_weaklistoffset;

    /\* Iterators \*/
    getiterfunc tp\_iter;
    iternextfunc tp\_iternext;

    /\* Attribute descriptor and subclassing stuff \*/
    PyMethodDef \*tp\_methods;
    PyMemberDef \*tp\_members;
    PyGetSetDef \*tp\_getset;
    // Strong reference on a heap type, borrowed reference on a static type
    PyTypeObject \*tp\_base;
    PyObject \*tp\_dict;
    descrgetfunc tp\_descr\_get;
    descrsetfunc tp\_descr\_set;
    Py\_ssize\_t tp\_dictoffset;
    initproc tp\_init;
    allocfunc tp\_alloc;
    newfunc tp\_new;
    freefunc tp\_free; /\* Low-level free-memory routine \*/
    inquiry tp\_is\_gc; /\* For PyObject\_IS\_GC \*/
    PyObject \*tp\_bases;
    PyObject \*tp\_mro; /\* method resolution order \*/
    PyObject \*tp\_cache; /\* no longer used \*/
    void \*tp\_subclasses;  /\* for static builtin types this is an index \*/
    PyObject \*tp\_weaklist; /\* not used for static builtin types \*/
    destructor tp\_del;

    /\* Type attribute cache version tag. Added in version 2.6.
     \* If zero, the cache is invalid and must be initialized.
     \*/
    unsigned int tp\_version\_tag;

    destructor tp\_finalize;
    vectorcallfunc tp\_vectorcall;

    /\* bitset of which type-watchers care about this type \*/
    unsigned char tp\_watched;

    /\* Number of tp\_version\_tag values used.
     \* Set to \_Py\_ATTR\_CACHE\_UNUSED if the attribute cache is
     \* disabled for this type (e.g. due to custom MRO entries).
     \* Otherwise, limited to MAX\_VERSIONS\_PER\_CLASS (defined elsewhere).
     \*/
    uint16\_t tp\_versions\_used;
} PyTypeObject;

Now that’s a _lot_ of methods. Don’t worry too much though – if you have a type you want to define, the chances are very good that you will only implement a handful of these.

As you probably expect by now, we’re going to go over this and give more information about the various handlers. We won’t go in the order they are defined in the structure, because there is a lot of historical baggage that impacts the ordering of the fields. It’s often easiest to find an example that includes the fields you need and then change the values to suit your new type.

const char \*tp\_name; /\* For printing \*/

The name of the type – as mentioned in the previous chapter, this will appear in various places, almost entirely for diagnostic purposes. Try to choose something that will be helpful in such a situation!

Py\_ssize\_t tp\_basicsize, tp\_itemsize; /\* For allocation \*/

These fields tell the runtime how much memory to allocate when new objects of this type are created. Python has some built-in support for variable length structures (think: strings, tuples) which is where the [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
 field comes in. This will be dealt with later.

const char \*tp\_doc;

Here you can put a string (or its address) that you want returned when the Python script references `obj.__doc__` to retrieve the doc string.

Now we come to the basic type methods – the ones most extension types will implement.

Finalization and De-allocation[¶](https://docs.python.org/3/extending/newtypes.html#finalization-and-de-allocation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

destructor tp\_dealloc;

This function is called when the reference count of the instance of your type is reduced to zero and the Python interpreter wants to reclaim it. If your type has memory to free or other clean-up to perform, you can put it here. The object itself needs to be freed here as well. Here is an example of this function:

static void
newdatatype\_dealloc(PyObject \*op)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    free(self\->obj\_UnderlyingDatatypePtr);
    Py\_TYPE(self)\->tp\_free(self);
}

If your type supports garbage collection, the destructor should call [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
 before clearing any member fields:

static void
newdatatype\_dealloc(PyObject \*op)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    PyObject\_GC\_UnTrack(op);
    Py\_CLEAR(self\->other\_obj);
    ...
    Py\_TYPE(self)\->tp\_free(self);
}

One important requirement of the deallocator function is that it leaves any pending exceptions alone. This is important since deallocators are frequently called as the interpreter unwinds the Python stack; when the stack is unwound due to an exception (rather than normal returns), nothing is done to protect the deallocators from seeing that an exception has already been set. Any actions which a deallocator performs which may cause additional Python code to be executed may detect that an exception has been set. This can lead to misleading errors from the interpreter. The proper way to protect against this is to save a pending exception before performing the unsafe action, and restoring it when done. This can be done using the [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
 and [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
 functions:

static void
my\_dealloc(PyObject \*obj)
{
    MyObject \*self \= (MyObject \*) obj;
    PyObject \*cbresult;

    if (self\->my\_callback != NULL) {
        PyObject \*err\_type, \*err\_value, \*err\_traceback;

        /\* This saves the current exception state \*/
        PyErr\_Fetch(&err\_type, &err\_value, &err\_traceback);

        cbresult \= PyObject\_CallNoArgs(self\->my\_callback);
        if (cbresult \== NULL) {
           PyErr\_WriteUnraisable(self\->my\_callback);
        }
        else {
            Py\_DECREF(cbresult);
        }

        /\* This restores the saved exception state \*/
        PyErr\_Restore(err\_type, err\_value, err\_traceback);

        Py\_DECREF(self\->my\_callback);
    }
    Py\_TYPE(self)\->tp\_free(self);
}

Note

There are limitations to what you can safely do in a deallocator function. First, if your type supports garbage collection (using [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 and/or [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
), some of the object’s members can have been cleared or finalized by the time [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 is called. Second, in `tp_dealloc`, your object is in an unstable state: its reference count is equal to zero. Any call to a non-trivial object or API (as in the example above) might end up calling `tp_dealloc` again, causing a double free and a crash.

Starting with Python 3.4, it is recommended not to put any complex finalization code in [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
, and instead use the new [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 type method.

See also

[**PEP 442**](https://peps.python.org/pep-0442/)
 explains the new finalization scheme.

Object Presentation[¶](https://docs.python.org/3/extending/newtypes.html#object-presentation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

In Python, there are two ways to generate a textual representation of an object: the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 function, and the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 function. (The [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function just calls `str()`.) These handlers are both optional.

reprfunc tp\_repr;
reprfunc tp\_str;

The [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 handler should return a string object containing a representation of the instance for which it is called. Here is a simple example:

static PyObject \*
newdatatype\_repr(PyObject \*op)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    return PyUnicode\_FromFormat("Repr-ified\_newdatatype{{size:%d}}",
                                self\->obj\_UnderlyingDatatypePtr\->size);
}

If no [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 handler is specified, the interpreter will supply a representation that uses the type’s [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
 and a uniquely identifying value for the object.

The [`tp_str`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_str "PyTypeObject.tp_str")
 handler is to [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 what the [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 handler described above is to [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
; that is, it is called when Python code calls `str()` on an instance of your object. Its implementation is very similar to the `tp_repr` function, but the resulting string is intended for human consumption. If `tp_str` is not specified, the `tp_repr` handler is used instead.

Here is a simple example:

static PyObject \*
newdatatype\_str(PyObject \*op)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    return PyUnicode\_FromFormat("Stringified\_newdatatype{{size:%d}}",
                                self\->obj\_UnderlyingDatatypePtr\->size);
}

Attribute Management[¶](https://docs.python.org/3/extending/newtypes.html#attribute-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

For every object which can support attributes, the corresponding type must provide the functions that control how the attributes are resolved. There needs to be a function which can retrieve attributes (if any are defined), and another to set attributes (if setting attributes is allowed). Removing an attribute is a special case, for which the new value passed to the handler is `NULL`.

Python supports two pairs of attribute handlers; a type that supports attributes only needs to implement the functions for one pair. The difference is that one pair takes the name of the attribute as a char\*, while the other accepts a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*. Each type can use whichever pair makes more sense for the implementation’s convenience.

getattrfunc  tp\_getattr;        /\* char \* version \*/
setattrfunc  tp\_setattr;
/\* ... \*/
getattrofunc tp\_getattro;       /\* PyObject \* version \*/
setattrofunc tp\_setattro;

If accessing attributes of an object is always a simple operation (this will be explained shortly), there are generic implementations which can be used to provide the [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* version of the attribute management functions. The actual need for type-specific attribute handlers almost completely disappeared starting with Python 2.2, though there are many examples which have not been updated to use some of the new generic mechanism that is available.

### Generic Attribute Management[¶](https://docs.python.org/3/extending/newtypes.html#generic-attribute-management "Link to this heading")

Most extension types only use _simple_ attributes. So, what makes the attributes simple? There are only a couple of conditions that must be met:

1.  The name of the attributes must be known when [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
     is called.
    
2.  No special processing is needed to record that an attribute was looked up or set, nor do actions need to be taken based on the value.
    

Note that this list does not place any restrictions on the values of the attributes, when the values are computed, or how relevant data is stored.

When [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 is called, it uses three tables referenced by the type object to create [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
s which are placed in the dictionary of the type object. Each descriptor controls access to one attribute of the instance object. Each of the tables is optional; if all three are `NULL`, instances of the type will only have attributes that are inherited from their base type, and should leave the [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")
 and [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
 fields `NULL` as well, allowing the base type to handle attributes.

The tables are declared as three fields of the type object:

struct PyMethodDef \*tp\_methods;
struct PyMemberDef \*tp\_members;
struct PyGetSetDef \*tp\_getset;

If [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods")
 is not `NULL`, it must refer to an array of [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 structures. Each entry in the table is an instance of this structure:

typedef struct PyMethodDef {
    const char  \*ml\_name;       /\* method name \*/
    PyCFunction  ml\_meth;       /\* implementation function \*/
    int          ml\_flags;      /\* flags \*/
    const char  \*ml\_doc;        /\* docstring \*/
} PyMethodDef;

One entry should be defined for each method provided by the type; no entries are needed for methods inherited from a base type. One additional entry is needed at the end; it is a sentinel that marks the end of the array. The [`ml_name`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_name "PyMethodDef.ml_name")
 field of the sentinel must be `NULL`.

The second table is used to define attributes which map directly to data stored in the instance. A variety of primitive C types are supported, and access may be read-only or read-write. The structures in the table are defined as:

typedef struct PyMemberDef {
    const char \*name;
    int         type;
    Py\_ssize\_t  offset;
    int         flags;
    const char \*doc;
} PyMemberDef;

For each entry in the table, a [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
 will be constructed and added to the type which will be able to extract a value from the instance structure. The [`type`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.type "PyMemberDef.type")
 field should contain a type code like [`Py_T_INT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_INT "Py_T_INT")
 or [`Py_T_DOUBLE`](https://docs.python.org/3/c-api/structures.html#c.Py_T_DOUBLE "Py_T_DOUBLE")
; the value will be used to determine how to convert Python values to and from C values. The [`flags`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.flags "PyMemberDef.flags")
 field is used to store flags which control how the attribute can be accessed: you can set it to [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
 to prevent Python code from setting it.

An interesting advantage of using the [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members")
 table to build descriptors that are used at runtime is that any attribute defined this way can have an associated doc string simply by providing the text in the table. An application can use the introspection API to retrieve the descriptor from the class object, and get the doc string using its [`__doc__`](https://docs.python.org/3/reference/datamodel.html#type.__doc__ "type.__doc__")
 attribute.

As with the [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods")
 table, a sentinel entry with a [`name`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.name "PyMemberDef.name")
 value of `NULL` is required.

### Type-specific Attribute Management[¶](https://docs.python.org/3/extending/newtypes.html#type-specific-attribute-management "Link to this heading")

For simplicity, only the char\* version will be demonstrated here; the type of the name parameter is the only difference between the char\* and [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* flavors of the interface. This example effectively does the same thing as the generic example above, but does not use the generic support added in Python 2.2. It explains how the handler functions are called, so that if you do need to extend their functionality, you’ll understand what needs to be done.

The [`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")
 handler is called when the object requires an attribute look-up. It is called in the same situations where the [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 method of a class would be called.

Here is an example:

static PyObject \*
newdatatype\_getattr(PyObject \*op, char \*name)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    if (strcmp(name, "data") \== 0) {
        return PyLong\_FromLong(self\->data);
    }

    PyErr\_Format(PyExc\_AttributeError,
                 "'%.100s' object has no attribute '%.400s'",
                 Py\_TYPE(self)\->tp\_name, name);
    return NULL;
}

The [`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")
 handler is called when the [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__")
 or [`__delattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__delattr__ "object.__delattr__")
 method of a class instance would be called. When an attribute should be deleted, the third parameter will be `NULL`. Here is an example that simply raises an exception; if this were really all you wanted, the `tp_setattr` handler should be set to `NULL`.

static int
newdatatype\_setattr(PyObject \*op, char \*name, PyObject \*v)
{
    PyErr\_Format(PyExc\_RuntimeError, "Read-only attribute: %s", name);
    return \-1;
}

Object Comparison[¶](https://docs.python.org/3/extending/newtypes.html#object-comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

richcmpfunc tp\_richcompare;

The [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
 handler is called when comparisons are needed. It is analogous to the [rich comparison methods](https://docs.python.org/3/reference/datamodel.html#richcmpfuncs)
, like `__lt__()`, and also called by [`PyObject_RichCompare()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "PyObject_RichCompare")
 and [`PyObject_RichCompareBool()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompareBool "PyObject_RichCompareBool")
.

This function is called with two Python objects and the operator as arguments, where the operator is one of `Py_EQ`, `Py_NE`, `Py_LE`, `Py_GE`, `Py_LT` or `Py_GT`. It should compare the two objects with respect to the specified operator and return `Py_True` or `Py_False` if the comparison is successful, `Py_NotImplemented` to indicate that comparison is not implemented and the other object’s comparison method should be tried, or `NULL` if an exception was set.

Here is a sample implementation, for a datatype that is considered equal if the size of an internal pointer is equal:

static PyObject \*
newdatatype\_richcmp(PyObject \*lhs, PyObject \*rhs, int op)
{
    newdatatypeobject \*obj1 \= (newdatatypeobject \*) lhs;
    newdatatypeobject \*obj2 \= (newdatatypeobject \*) rhs;
    PyObject \*result;
    int c, size1, size2;

    /\* code to make sure that both arguments are of type
       newdatatype omitted \*/

    size1 \= obj1\->obj\_UnderlyingDatatypePtr\->size;
    size2 \= obj2\->obj\_UnderlyingDatatypePtr\->size;

    switch (op) {
    case Py\_LT: c \= size1 <  size2; break;
    case Py\_LE: c \= size1 <= size2; break;
    case Py\_EQ: c \= size1 \== size2; break;
    case Py\_NE: c \= size1 != size2; break;
    case Py\_GT: c \= size1 \>  size2; break;
    case Py\_GE: c \= size1 \>= size2; break;
    }
    result \= c ? Py\_True : Py\_False;
    return Py\_NewRef(result);
 }

Abstract Protocol Support[¶](https://docs.python.org/3/extending/newtypes.html#abstract-protocol-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Python supports a variety of _abstract_ ‘protocols;’ the specific interfaces provided to use these interfaces are documented in [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html#abstract)
.

A number of these abstract interfaces were defined early in the development of the Python implementation. In particular, the number, mapping, and sequence protocols have been part of Python since the beginning. Other protocols have been added over time. For protocols which depend on several handler routines from the type implementation, the older protocols have been defined as optional blocks of handlers referenced by the type object. For newer protocols there are additional slots in the main type object, with a flag bit being set to indicate that the slots are present and should be checked by the interpreter. (The flag bit does not indicate that the slot values are non-`NULL`. The flag may be set to indicate the presence of a slot, but a slot may still be unfilled.)

PyNumberMethods   \*tp\_as\_number;
PySequenceMethods \*tp\_as\_sequence;
PyMappingMethods  \*tp\_as\_mapping;

If you wish your object to be able to act like a number, a sequence, or a mapping object, then you place the address of a structure that implements the C type [`PyNumberMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
, [`PySequenceMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
, or [`PyMappingMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
, respectively. It is up to you to fill in this structure with appropriate values. You can find examples of the use of each of these in the `Objects` directory of the Python source distribution.

hashfunc tp\_hash;

This function, if you choose to provide it, should return a hash number for an instance of your data type. Here is a simple example:

static Py\_hash\_t
newdatatype\_hash(PyObject \*op)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    Py\_hash\_t result;
    result \= self\->some\_size + 32767 \* self\->some\_number;
    if (result \== \-1) {
        result \= \-2;
    }
    return result;
}

[`Py_hash_t`](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
 is a signed integer type with a platform-varying width. Returning `-1` from [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
 indicates an error, which is why you should be careful to avoid returning it when hash computation is successful, as seen above.

ternaryfunc tp\_call;

This function is called when an instance of your data type is “called”, for example, if `obj1` is an instance of your data type and the Python script contains `obj1('hello')`, the [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 handler is invoked.

This function takes three arguments:

1.  _self_ is the instance of the data type which is the subject of the call. If the call is `obj1('hello')`, then _self_ is `obj1`.
    
2.  _args_ is a tuple containing the arguments to the call. You can use [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
     to extract the arguments.
    
3.  _kwds_ is a dictionary of keyword arguments that were passed. If this is non-`NULL` and you support keyword arguments, use [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
     to extract the arguments. If you do not want to support keyword arguments and this is non-`NULL`, raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     with a message saying that keyword arguments are not supported.
    

Here is a toy `tp_call` implementation:

static PyObject \*
newdatatype\_call(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    newdatatypeobject \*self \= (newdatatypeobject \*) op;
    PyObject \*result;
    const char \*arg1;
    const char \*arg2;
    const char \*arg3;

    if (!PyArg\_ParseTuple(args, "sss:call", &arg1, &arg2, &arg3)) {
        return NULL;
    }
    result \= PyUnicode\_FromFormat(
        "Returning -- value: \[%d\] arg1: \[%s\] arg2: \[%s\] arg3: \[%s\]\\n",
        self\->obj\_UnderlyingDatatypePtr\->size,
        arg1, arg2, arg3);
    return result;
}

/\* Iterators \*/
getiterfunc tp\_iter;
iternextfunc tp\_iternext;

These functions provide support for the iterator protocol. Both handlers take exactly one parameter, the instance for which they are being called, and return a new reference. In the case of an error, they should set an exception and return `NULL`. [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
 corresponds to the Python [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
 method, while [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext")
 corresponds to the Python [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
 method.

Any [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 object must implement the [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
 handler, which must return an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 object. Here the same guidelines apply as for Python classes:

*   For collections (such as lists and tuples) which can support multiple independent iterators, a new iterator should be created and returned by each call to [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
    .
    
*   Objects which can only be iterated over once (usually due to side effects of iteration, such as file objects) can implement [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
     by returning a new reference to themselves – and should also therefore implement the [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext")
     handler.
    

Any [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 object should implement both [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
 and [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext")
. An iterator’s `tp_iter` handler should return a new reference to the iterator. Its `tp_iternext` handler should return a new reference to the next object in the iteration, if there is one. If the iteration has reached the end, `tp_iternext` may return `NULL` without setting an exception, or it may set [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 _in addition_ to returning `NULL`; avoiding the exception can yield slightly better performance. If an actual error occurs, `tp_iternext` should always set an exception and return `NULL`.

Weak Reference Support[¶](https://docs.python.org/3/extending/newtypes.html#weak-reference-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

One of the goals of Python’s weak reference implementation is to allow any type to participate in the weak reference mechanism without incurring the overhead on performance-critical objects (such as numbers).

See also

Documentation for the [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.")
 module.

For an object to be weakly referenceable, the extension type must set the `Py_TPFLAGS_MANAGED_WEAKREF` bit of the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field. The legacy [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
 field should be left as zero.

If this flag is set, [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 should also be set.

Concretely, here is how the statically declared type object would look:

static PyTypeObject TrivialType \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    /\* ... other members omitted for brevity ... \*/
    .tp\_flags \= Py\_TPFLAGS\_MANAGED\_WEAKREF | ...,
};

The only further addition is that `tp_dealloc` needs to clear any weak references (by calling [`PyObject_ClearWeakRefs()`](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "PyObject_ClearWeakRefs")
):

static void
Trivial\_dealloc(PyObject \*op)
{
    /\* Clear weakrefs first before calling any destructors \*/
    PyObject\_ClearWeakRefs(op);
    /\* ... remainder of destruction code omitted for brevity ... \*/
    Py\_TYPE(op)\->tp\_free(op);
}

More Suggestions[¶](https://docs.python.org/3/extending/newtypes.html#more-suggestions "Link to this heading")

---------------------------------------------------------------------------------------------------------------

In order to learn how to implement any specific method for your new data type, get the [CPython](https://docs.python.org/3/glossary.html#term-CPython)
 source code. Go to the `Objects` directory, then search the C source files for `tp_` plus the function you want (for example, `tp_richcompare`). You will find examples of the function you want to implement.

When you need to verify that an object is a concrete instance of the type you are implementing, use the [`PyObject_TypeCheck()`](https://docs.python.org/3/c-api/object.html#c.PyObject_TypeCheck "PyObject_TypeCheck")
 function. A sample of its use might be something like the following:

if (!PyObject\_TypeCheck(some\_object, &MyType)) {
    PyErr\_SetString(PyExc\_TypeError, "arg #1 not a mything");
    return NULL;
}

See also

Download CPython source releases.

[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)

The CPython project on GitHub, where the CPython source code is developed.

[https://github.com/python/cpython](https://github.com/python/cpython)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html#)
    *   [Finalization and De-allocation](https://docs.python.org/3/extending/newtypes.html#finalization-and-de-allocation)
        
    *   [Object Presentation](https://docs.python.org/3/extending/newtypes.html#object-presentation)
        
    *   [Attribute Management](https://docs.python.org/3/extending/newtypes.html#attribute-management)
        *   [Generic Attribute Management](https://docs.python.org/3/extending/newtypes.html#generic-attribute-management)
            
        *   [Type-specific Attribute Management](https://docs.python.org/3/extending/newtypes.html#type-specific-attribute-management)
            
    *   [Object Comparison](https://docs.python.org/3/extending/newtypes.html#object-comparison)
        
    *   [Abstract Protocol Support](https://docs.python.org/3/extending/newtypes.html#abstract-protocol-support)
        
    *   [Weak Reference Support](https://docs.python.org/3/extending/newtypes.html#weak-reference-support)
        
    *   [More Suggestions](https://docs.python.org/3/extending/newtypes.html#more-suggestions)
        

#### Previous topic

[Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html "previous chapter")

#### Next topic

[Building C and C++ Extensions](https://docs.python.org/3/extending/building.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Defining+Extension+Types%3A+Assorted+Topics&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fextending%2Fnewtypes.html&pagesource=extending%2Fnewtypes.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/extending/newtypes.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/building.html "Building C and C++ Extensions")
     |
*   [previous](https://docs.python.org/3/extending/newtypes_tutorial.html "Defining Extension Types: Tutorial")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |