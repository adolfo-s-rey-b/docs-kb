### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/timerfd.html "timer file descriptor HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/annotations.html "Annotations Best Practices")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Isolating Extension Modules[¶](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extension-modules "Link to this heading")

=============================================================================================================================================

Who should read this[¶](https://docs.python.org/3/howto/isolating-extensions.html#who-should-read-this "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

This guide is written for maintainers of [C-API](https://docs.python.org/3/c-api/index.html#c-api-index)
 extensions who would like to make that extension safer to use in applications where Python itself is used as a library.

Background[¶](https://docs.python.org/3/howto/isolating-extensions.html#background "Link to this heading")

-----------------------------------------------------------------------------------------------------------

An _interpreter_ is the context in which Python code runs. It contains configuration (e.g. the import path) and runtime state (e.g. the set of imported modules).

Python supports running multiple interpreters in one process. There are two cases to think about—users may run interpreters:

*   in sequence, with several [`Py_InitializeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeEx "Py_InitializeEx")
    /[`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
     cycles, and
    
*   in parallel, managing “sub-interpreters” using [`Py_NewInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_NewInterpreter "Py_NewInterpreter")
    /[`Py_EndInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_EndInterpreter "Py_EndInterpreter")
    .
    

Both cases (and combinations of them) would be most useful when embedding Python within a library. Libraries generally shouldn’t make assumptions about the application that uses them, which include assuming a process-wide “main Python interpreter”.

Historically, Python extension modules don’t handle this use case well. Many extension modules (and even some stdlib modules) use _per-process_ global state, because C `static` variables are extremely easy to use. Thus, data that should be specific to an interpreter ends up being shared between interpreters. Unless the extension developer is careful, it is very easy to introduce edge cases that lead to crashes when a module is loaded in more than one interpreter in the same process.

Unfortunately, _per-interpreter_ state is not easy to achieve. Extension authors tend to not keep multiple interpreters in mind when developing, and it is currently cumbersome to test the behavior.

### Enter Per-Module State[¶](https://docs.python.org/3/howto/isolating-extensions.html#enter-per-module-state "Link to this heading")

Instead of focusing on per-interpreter state, Python’s C API is evolving to better support the more granular _per-module_ state. This means that C-level data should be attached to a _module object_. Each interpreter creates its own module object, keeping the data separate. For testing the isolation, multiple module objects corresponding to a single extension can even be loaded in a single interpreter.

Per-module state provides an easy way to think about lifetime and resource ownership: the extension module will initialize when a module object is created, and clean up when it’s freed. In this regard, a module is just like any other [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*; there are no “on interpreter shutdown” hooks to think—or forget—about.

Note that there are use cases for different kinds of “globals”: per-process, per-interpreter, per-thread or per-task state. With per-module state as the default, these are still possible, but you should treat them as exceptional cases: if you need them, you should give them additional care and testing. (Note that this guide does not cover them.)

### Isolated Module Objects[¶](https://docs.python.org/3/howto/isolating-extensions.html#isolated-module-objects "Link to this heading")

The key point to keep in mind when developing an extension module is that several module objects can be created from a single shared library. For example:

Copy

\>>> import sys
\>>> import binascii
\>>> old\_binascii \= binascii
\>>> del sys.modules\['binascii'\]
\>>> import binascii  \# create a new module object
\>>> old\_binascii \== binascii
False

As a rule of thumb, the two modules should be completely independent. All objects and state specific to the module should be encapsulated within the module object, not shared with other module objects, and cleaned up when the module object is deallocated. Since this just is a rule of thumb, exceptions are possible (see [Managing Global State](https://docs.python.org/3/howto/isolating-extensions.html#managing-global-state)
), but they will need more thought and attention to edge cases.

While some modules could do with less stringent restrictions, isolated modules make it easier to set clear expectations and guidelines that work across a variety of use cases.

### Surprising Edge Cases[¶](https://docs.python.org/3/howto/isolating-extensions.html#surprising-edge-cases "Link to this heading")

Note that isolated modules do create some surprising edge cases. Most notably, each module object will typically not share its classes and exceptions with other similar modules. Continuing from the [example above](https://docs.python.org/3/howto/isolating-extensions.html#isolated-module-objects)
, note that `old_binascii.Error` and `binascii.Error` are separate objects. In the following code, the exception is _not_ caught:

Copy

\>>> old\_binascii.Error \== binascii.Error
False
\>>> try:
...     old\_binascii.unhexlify(b'qwertyuiop')
... except binascii.Error:
...     print('boo')
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
binascii.Error: Non-hexadecimal digit found

This is expected. Notice that pure-Python modules behave the same way: it is a part of how Python works.

The goal is to make extension modules safe at the C level, not to make hacks behave intuitively. Mutating `sys.modules` “manually” counts as a hack.

Making Modules Safe with Multiple Interpreters[¶](https://docs.python.org/3/howto/isolating-extensions.html#making-modules-safe-with-multiple-interpreters "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Managing Global State[¶](https://docs.python.org/3/howto/isolating-extensions.html#managing-global-state "Link to this heading")

Sometimes, the state associated with a Python module is not specific to that module, but to the entire process (or something else “more global” than a module). For example:

*   The `readline` module manages _the_ terminal.
    
*   A module running on a circuit board wants to control _the_ on-board LED.
    

In these cases, the Python module should provide _access_ to the global state, rather than _own_ it. If possible, write the module so that multiple copies of it can access the state independently (along with other libraries, whether for Python or other languages). If that is not possible, consider explicit locking.

If it is necessary to use process-global state, the simplest way to avoid issues with multiple interpreters is to explicitly prevent a module from being loaded more than once per process—see [Opt-Out: Limiting to One Module Object per Process](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-optout)
.

### Managing Per-Module State[¶](https://docs.python.org/3/howto/isolating-extensions.html#managing-per-module-state "Link to this heading")

To use per-module state, use [multi-phase extension module initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
. This signals that your module supports multiple interpreters correctly.

Set `PyModuleDef.m_size` to a positive number to request that many bytes of storage local to the module. Usually, this will be set to the size of some module-specific `struct`, which can store all of the module’s C-level state. In particular, it is where you should put pointers to classes (including exceptions, but excluding static types) and settings (e.g. `csv`’s [`field_size_limit`](https://docs.python.org/3/library/csv.html#csv.field_size_limit "csv.field_size_limit")
) which the C code needs to function.

Note

Another option is to store state in the module’s `__dict__`, but you must avoid crashing when users modify `__dict__` from Python code. This usually means error- and type-checking at the C level, which is easy to get wrong and hard to test sufficiently.

However, if module state is not needed in C code, storing it in `__dict__` only is a good idea.

If the module state includes `PyObject` pointers, the module object must hold references to those objects and implement the module-level hooks `m_traverse`, `m_clear` and `m_free`. These work like `tp_traverse`, `tp_clear` and `tp_free` of a class. Adding them will require some work and make the code longer; this is the price for modules which can be unloaded cleanly.

An example of a module with per-module state is currently available as [xxlimited](https://github.com/python/cpython/blob/master/Modules/xxlimited.c)
; example module initialization shown at the bottom of the file.

### Opt-Out: Limiting to One Module Object per Process[¶](https://docs.python.org/3/howto/isolating-extensions.html#opt-out-limiting-to-one-module-object-per-process "Link to this heading")

A non-negative `PyModuleDef.m_size` signals that a module supports multiple interpreters correctly. If this is not yet the case for your module, you can explicitly make your module loadable only once per process. For example:

// A process-wide flag
static int loaded \= 0;

// Mutex to provide thread safety (only needed for free-threaded Python)
static PyMutex modinit\_mutex \= {0};

static int
exec\_module(PyObject\* module)
{
    PyMutex\_Lock(&modinit\_mutex);
    if (loaded) {
        PyMutex\_Unlock(&modinit\_mutex);
        PyErr\_SetString(PyExc\_ImportError,
                        "cannot load module more than once per process");
        return \-1;
    }
    loaded \= 1;
    PyMutex\_Unlock(&modinit\_mutex);
    // ... rest of initialization
}

If your module’s [`PyModuleDef.m_clear`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_clear "PyModuleDef.m_clear")
 function is able to prepare for future re-initialization, it should clear the `loaded` flag. In this case, your module won’t support multiple instances existing _concurrently_, but it will, for example, support being loaded after Python runtime shutdown ([`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
) and re-initialization ([`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
).

### Module State Access from Functions[¶](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-functions "Link to this heading")

Accessing the state from module-level functions is straightforward. Functions get the module object as their first argument; for extracting the state, you can use `PyModule_GetState`:

static PyObject \*
func(PyObject \*module, PyObject \*args)
{
    my\_struct \*state \= (my\_struct\*)PyModule\_GetState(module);
    if (state \== NULL) {
        return NULL;
    }
    // ... rest of logic
}

Note

`PyModule_GetState` may return `NULL` without setting an exception if there is no module state, i.e. `PyModuleDef.m_size` was zero. In your own module, you’re in control of `m_size`, so this is easy to prevent.

Heap Types[¶](https://docs.python.org/3/howto/isolating-extensions.html#heap-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Traditionally, types defined in C code are _static_; that is, `static PyTypeObject` structures defined directly in code and initialized using `PyType_Ready()`.

Such types are necessarily shared across the process. Sharing them between module objects requires paying attention to any state they own or access. To limit the possible issues, static types are immutable at the Python level: for example, you can’t set `str.myattribute = 123`.

**CPython implementation detail:** Sharing truly immutable objects between interpreters is fine, as long as they don’t provide access to mutable objects. However, in CPython, every Python object has a mutable implementation detail: the reference count. Changes to the refcount are guarded by the GIL. Thus, code that shares any Python objects across interpreters implicitly depends on CPython’s current, process-wide GIL.

Because they are immutable and process-global, static types cannot access “their” module state. If any method of such a type requires access to module state, the type must be converted to a _heap-allocated type_, or _heap type_ for short. These correspond more closely to classes created by Python’s `class` statement.

For new modules, using heap types by default is a good rule of thumb.

### Changing Static Types to Heap Types[¶](https://docs.python.org/3/howto/isolating-extensions.html#changing-static-types-to-heap-types "Link to this heading")

Static types can be converted to heap types, but note that the heap type API was not designed for “lossless” conversion from static types—that is, creating a type that works exactly like a given static type. So, when rewriting the class definition in a new API, you are likely to unintentionally change a few details (e.g. pickleability or inherited slots). Always test the details that are important to you.

Watch out for the following two points in particular (but note that this is not a comprehensive list):

*   Unlike static types, heap type objects are mutable by default. Use the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
     flag to prevent mutability.
    
*   Heap types inherit [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
     by default, so it may become possible to instantiate them from Python code. You can prevent this with the [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION "Py_TPFLAGS_DISALLOW_INSTANTIATION")
     flag.
    

### Defining Heap Types[¶](https://docs.python.org/3/howto/isolating-extensions.html#defining-heap-types "Link to this heading")

Heap types can be created by filling a [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 structure, a description or “blueprint” of a class, and calling [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
 to construct a new class object.

Note

Other functions, like [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
, can also create heap types, but [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
 associates the module with the class, allowing access to the module state from methods.

The class should generally be stored in _both_ the module state (for safe access from C) and the module’s `__dict__` (for access from Python code).

### Garbage-Collection Protocol[¶](https://docs.python.org/3/howto/isolating-extensions.html#garbage-collection-protocol "Link to this heading")

Instances of heap types hold a reference to their type. This ensures that the type isn’t destroyed before all its instances are, but may result in reference cycles that need to be broken by the garbage collector.

To avoid memory leaks, instances of heap types must implement the garbage collection protocol. That is, heap types should:

*   Have the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag.
    
*   Define a traverse function using [`Py_tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_traverse "Py_tp_traverse")
    , which visits the type (e.g. using `Py_VISIT(Py_TYPE(self))`).
    

Please refer to the documentation of [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 and [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 for additional considerations.

The API for defining heap types grew organically, leaving it somewhat awkward to use in its current state. The following sections will guide you through common issues.

#### `tp_traverse` in Python 3.8 and lower[¶](https://docs.python.org/3/howto/isolating-extensions.html#tp-traverse-in-python-3-8-and-lower "Link to this heading")

The requirement to visit the type from `tp_traverse` was added in Python 3.9. If you support Python 3.8 and lower, the traverse function must _not_ visit the type, so it must be more complicated:

static int my\_traverse(PyObject \*self, visitproc visit, void \*arg)
{
    if (Py\_Version \>= 0x03090000) {
        Py\_VISIT(Py\_TYPE(self));
    }
    return 0;
}

Unfortunately, [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version")
 was only added in Python 3.11. As a replacement, use:

*   [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
    , if not using the stable ABI, or
    
*   [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
     (via [`PySys_GetObject()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetObject "PySys_GetObject")
     and [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
    ).
    

#### Delegating `tp_traverse`[¶](https://docs.python.org/3/howto/isolating-extensions.html#delegating-tp-traverse "Link to this heading")

If your traverse function delegates to the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 of its base class (or another type), ensure that `Py_TYPE(self)` is visited only once. Note that only heap type are expected to visit the type in `tp_traverse`.

For example, if your traverse function includes:

base\->tp\_traverse(self, visit, arg)

…and `base` may be a static type, then it should also include:

if (base\->tp\_flags & Py\_TPFLAGS\_HEAPTYPE) {
    // a heap type's tp\_traverse already visited Py\_TYPE(self)
} else {
    if (Py\_Version \>= 0x03090000) {
        Py\_VISIT(Py\_TYPE(self));
    }
}

It is not necessary to handle the type’s reference count in [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
.

#### Defining `tp_dealloc`[¶](https://docs.python.org/3/howto/isolating-extensions.html#defining-tp-dealloc "Link to this heading")

If your type has a custom [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 function, it needs to:

*   call [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
     before any fields are invalidated, and
    
*   decrement the reference count of the type.
    

To keep the type valid while `tp_free` is called, the type’s refcount needs to be decremented _after_ the instance is deallocated. For example:

static void my\_dealloc(PyObject \*self)
{
    PyObject\_GC\_UnTrack(self);
    ...
    PyTypeObject \*type \= Py\_TYPE(self);
    type\->tp\_free(self);
    Py\_DECREF(type);
}

The default `tp_dealloc` function does this, so if your type does _not_ override `tp_dealloc` you don’t need to add it.

#### Not overriding `tp_free`[¶](https://docs.python.org/3/howto/isolating-extensions.html#not-overriding-tp-free "Link to this heading")

The [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot of a heap type must be set to [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
. This is the default; do not override it.

#### Avoiding `PyObject_New`[¶](https://docs.python.org/3/howto/isolating-extensions.html#avoiding-pyobject-new "Link to this heading")

GC-tracked objects need to be allocated using GC-aware functions.

If you use [`PyObject_New()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
 or [`PyObject_NewVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
:

*   Get and call type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
     slot, if possible. That is, replace `TYPE *o = PyObject_New(TYPE, typeobj)` with:
    
    TYPE \*o \= typeobj\->tp\_alloc(typeobj, 0);
    
    Replace `o = PyObject_NewVar(TYPE, typeobj, size)` with the same, but use size instead of the 0.
    
*   If the above is not possible (e.g. inside a custom `tp_alloc`), call [`PyObject_GC_New()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
     or [`PyObject_GC_NewVar()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
    :
    
    TYPE \*o \= PyObject\_GC\_New(TYPE, typeobj);
    
    TYPE \*o \= PyObject\_GC\_NewVar(TYPE, typeobj, size);
    

### Module State Access from Classes[¶](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-classes "Link to this heading")

If you have a type object defined with [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
, you can call [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
 to get the associated module, and then [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
 to get the module’s state.

To save a some tedious error-handling boilerplate code, you can combine these two steps with [`PyType_GetModuleState()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "PyType_GetModuleState")
, resulting in:

my\_struct \*state \= (my\_struct\*)PyType\_GetModuleState(type);
if (state \== NULL) {
    return NULL;
}

### Module State Access from Regular Methods[¶](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-regular-methods "Link to this heading")

Accessing the module-level state from methods of a class is somewhat more complicated, but is possible thanks to API introduced in Python 3.9. To get the state, you need to first get the _defining class_, and then get the module state from it.

The largest roadblock is getting _the class a method was defined in_, or that method’s “defining class” for short. The defining class can have a reference to the module it is part of.

Do not confuse the defining class with `Py_TYPE(self)`. If the method is called on a _subclass_ of your type, `Py_TYPE(self)` will refer to that subclass, which may be defined in different module than yours.

Note

The following Python code can illustrate the concept. `Base.get_defining_class` returns `Base` even if `type(self) == Sub`:

Copy

class Base:
    def get\_type\_of\_self(self):
        return type(self)

    def get\_defining\_class(self):
        return \_\_class\_\_

class Sub(Base):
    pass

For a method to get its “defining class”, it must use the [METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-method-meth-fastcall-meth-keywords)
 [`calling convention`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 and the corresponding [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
 signature:

PyObject \*PyCMethod(
    PyObject \*self,               // object the method was called on
    PyTypeObject \*defining\_class, // defining class
    PyObject \*const \*args,        // C array of arguments
    Py\_ssize\_t nargs,             // length of "args"
    PyObject \*kwnames)            // NULL, or tuple of keyword argument names

Once you have the defining class, call [`PyType_GetModuleState()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "PyType_GetModuleState")
 to get the state of its associated module.

For example:

static PyObject \*
example\_method(PyObject \*self,
        PyTypeObject \*defining\_class,
        PyObject \*const \*args,
        Py\_ssize\_t nargs,
        PyObject \*kwnames)
{
    my\_struct \*state \= (my\_struct\*)PyType\_GetModuleState(defining\_class);
    if (state \== NULL) {
        return NULL;
    }
    ... // rest of logic
}

PyDoc\_STRVAR(example\_method\_doc, "...");

static PyMethodDef my\_methods\[\] \= {
    {"example\_method",
      (PyCFunction)(void(\*)(void))example\_method,
      METH\_METHOD|METH\_FASTCALL|METH\_KEYWORDS,
      example\_method\_doc},
    {NULL},
};

### Module State Access from Slot Methods, Getters and Setters[¶](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-slot-methods-getters-and-setters "Link to this heading")

Note

This is new in Python 3.11.

Slot methods—the fast C equivalents for special methods, such as [`nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "PyNumberMethods.nb_add")
 for [`__add__`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
 or [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 for initialization—have a very simple API that doesn’t allow passing in the defining class, unlike with [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
. The same goes for getters and setters defined with [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
.

To access the module state in these cases, use the [`PyType_GetModuleByDef()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
 function, and pass in the module definition. Once you have the module, call [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
 to get the state:

PyObject \*module \= PyType\_GetModuleByDef(Py\_TYPE(self), &module\_def);
my\_struct \*state \= (my\_struct\*)PyModule\_GetState(module);
if (state \== NULL) {
    return NULL;
}

`PyType_GetModuleByDef()` works by searching the [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order)
 (i.e. all superclasses) for the first superclass that has a corresponding module.

Note

In very exotic cases (inheritance chains spanning multiple modules created from the same definition), `PyType_GetModuleByDef()` might not return the module of the true defining class. However, it will always return a module with the same definition, ensuring a compatible C memory layout.

### Lifetime of the Module State[¶](https://docs.python.org/3/howto/isolating-extensions.html#lifetime-of-the-module-state "Link to this heading")

When a module object is garbage-collected, its module state is freed. For each pointer to (a part of) the module state, you must hold a reference to the module object.

Usually this is not an issue, because types created with [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
, and their instances, hold a reference to the module. However, you must be careful in reference counting when you reference module state from other places, such as callbacks for external libraries.

Open Issues[¶](https://docs.python.org/3/howto/isolating-extensions.html#open-issues "Link to this heading")

-------------------------------------------------------------------------------------------------------------

Several issues around per-module state and heap types are still open.

Discussions about improving the situation are best held on the [discuss forum under c-api tag](https://discuss.python.org/c/core-dev/c-api/30)
.

### Per-Class Scope[¶](https://docs.python.org/3/howto/isolating-extensions.html#per-class-scope "Link to this heading")

It is currently (as of Python 3.11) not possible to attach state to individual _types_ without relying on CPython implementation details (which may change in the future—perhaps, ironically, to allow a proper solution for per-class scope).

### Lossless Conversion to Heap Types[¶](https://docs.python.org/3/howto/isolating-extensions.html#lossless-conversion-to-heap-types "Link to this heading")

The heap type API was not designed for “lossless” conversion from static types; that is, creating a type that works exactly like a given static type.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#)
    *   [Who should read this](https://docs.python.org/3/howto/isolating-extensions.html#who-should-read-this)
        
    *   [Background](https://docs.python.org/3/howto/isolating-extensions.html#background)
        *   [Enter Per-Module State](https://docs.python.org/3/howto/isolating-extensions.html#enter-per-module-state)
            
        *   [Isolated Module Objects](https://docs.python.org/3/howto/isolating-extensions.html#isolated-module-objects)
            
        *   [Surprising Edge Cases](https://docs.python.org/3/howto/isolating-extensions.html#surprising-edge-cases)
            
    *   [Making Modules Safe with Multiple Interpreters](https://docs.python.org/3/howto/isolating-extensions.html#making-modules-safe-with-multiple-interpreters)
        *   [Managing Global State](https://docs.python.org/3/howto/isolating-extensions.html#managing-global-state)
            
        *   [Managing Per-Module State](https://docs.python.org/3/howto/isolating-extensions.html#managing-per-module-state)
            
        *   [Opt-Out: Limiting to One Module Object per Process](https://docs.python.org/3/howto/isolating-extensions.html#opt-out-limiting-to-one-module-object-per-process)
            
        *   [Module State Access from Functions](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-functions)
            
    *   [Heap Types](https://docs.python.org/3/howto/isolating-extensions.html#heap-types)
        *   [Changing Static Types to Heap Types](https://docs.python.org/3/howto/isolating-extensions.html#changing-static-types-to-heap-types)
            
        *   [Defining Heap Types](https://docs.python.org/3/howto/isolating-extensions.html#defining-heap-types)
            
        *   [Garbage-Collection Protocol](https://docs.python.org/3/howto/isolating-extensions.html#garbage-collection-protocol)
            *   [`tp_traverse` in Python 3.8 and lower](https://docs.python.org/3/howto/isolating-extensions.html#tp-traverse-in-python-3-8-and-lower)
                
            *   [Delegating `tp_traverse`](https://docs.python.org/3/howto/isolating-extensions.html#delegating-tp-traverse)
                
            *   [Defining `tp_dealloc`](https://docs.python.org/3/howto/isolating-extensions.html#defining-tp-dealloc)
                
            *   [Not overriding `tp_free`](https://docs.python.org/3/howto/isolating-extensions.html#not-overriding-tp-free)
                
            *   [Avoiding `PyObject_New`](https://docs.python.org/3/howto/isolating-extensions.html#avoiding-pyobject-new)
                
        *   [Module State Access from Classes](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-classes)
            
        *   [Module State Access from Regular Methods](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-regular-methods)
            
        *   [Module State Access from Slot Methods, Getters and Setters](https://docs.python.org/3/howto/isolating-extensions.html#module-state-access-from-slot-methods-getters-and-setters)
            
        *   [Lifetime of the Module State](https://docs.python.org/3/howto/isolating-extensions.html#lifetime-of-the-module-state)
            
    *   [Open Issues](https://docs.python.org/3/howto/isolating-extensions.html#open-issues)
        *   [Per-Class Scope](https://docs.python.org/3/howto/isolating-extensions.html#per-class-scope)
            
        *   [Lossless Conversion to Heap Types](https://docs.python.org/3/howto/isolating-extensions.html#lossless-conversion-to-heap-types)
            

#### Previous topic

[Annotations Best Practices](https://docs.python.org/3/howto/annotations.html "previous chapter")

#### Next topic

[timer file descriptor HOWTO](https://docs.python.org/3/howto/timerfd.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Isolating+Extension+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fisolating-extensions.html&pagesource=howto%2Fisolating-extensions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/isolating-extensions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/timerfd.html "timer file descriptor HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/annotations.html "Annotations Best Practices")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html)
    
*    
    
    |
*   Theme Auto Light Dark |