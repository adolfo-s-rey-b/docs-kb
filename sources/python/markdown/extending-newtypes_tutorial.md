### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/newtypes.html "Defining Extension Types: Assorted Topics")
     |
*   [previous](https://docs.python.org/3/extending/extending.html "Using the C API: Assorted topics")
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
*   [Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Defining Extension Types: Tutorial[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#defining-extension-types-tutorial "Link to this heading")

===========================================================================================================================================================

Python allows the writer of a C extension module to define new types that can be manipulated from Python code, much like the built-in [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 and [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 types. The code for all extension types follows a pattern, but there are some details that you need to understand before you can get started. This document is a gentle introduction to the topic.

The Basics[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#the-basics "Link to this heading")

------------------------------------------------------------------------------------------------------------

The [CPython](https://docs.python.org/3/glossary.html#term-CPython)
 runtime sees all Python objects as variables of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, which serves as a “base type” for all Python objects. The [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 structure itself only contains the object’s [reference count](https://docs.python.org/3/glossary.html#term-reference-count)
 and a pointer to the object’s “type object”. This is where the action is; the type object determines which (C) functions get called by the interpreter when, for instance, an attribute gets looked up on an object, a method called, or it is multiplied by another object. These C functions are called “type methods”.

So, if you want to define a new extension type, you need to create a new type object.

This sort of thing can only be explained by example, so here’s a minimal, but complete, module that defines a new type named `Custom` inside a C extension module `custom`:

Note

What we’re showing here is the traditional way of defining _static_ extension types. It should be adequate for most uses. The C API also allows defining heap-allocated extension types using the [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
 function, which isn’t covered in this tutorial.

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>

typedef struct {
    PyObject\_HEAD
    /\* Type-specific fields go here. \*/
} CustomObject;

static PyTypeObject CustomType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "custom.Custom",
    .tp\_doc \= PyDoc\_STR("Custom objects"),
    .tp\_basicsize \= sizeof(CustomObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT,
    .tp\_new \= PyType\_GenericNew,
};

static int
custom\_module\_exec(PyObject \*m)
{
    if (PyType\_Ready(&CustomType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "Custom", (PyObject \*) &CustomType) < 0) {
        return \-1;
    }

    return 0;
}

static PyModuleDef\_Slot custom\_module\_slots\[\] \= {
    {Py\_mod\_exec, custom\_module\_exec},
    // Just use this while using static types
    {Py\_mod\_multiple\_interpreters, Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED},
    {0, NULL}
};

static PyModuleDef custom\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "custom",
    .m\_doc \= "Example module that creates an extension type.",
    .m\_size \= 0,
    .m\_slots \= custom\_module\_slots,
};

PyMODINIT\_FUNC
PyInit\_custom(void)
{
    return PyModuleDef\_Init(&custom\_module);
}

Now that’s quite a bit to take in at once, but hopefully bits will seem familiar from the previous chapter. This file defines three things:

1.  What a `Custom` **object** contains: this is the `CustomObject` struct, which is allocated once for each `Custom` instance.
    
2.  How the `Custom` **type** behaves: this is the `CustomType` struct, which defines a set of flags and function pointers that the interpreter inspects when specific operations are requested.
    
3.  How to define and execute the `custom` module: this is the `PyInit_custom` function and the associated `custom_module` struct for defining the module, and the `custom_module_exec` function to set up a fresh module object.
    

The first bit is:

typedef struct {
    PyObject\_HEAD
} CustomObject;

This is what a Custom object will contain. `PyObject_HEAD` is mandatory at the start of each object struct and defines a field called `ob_base` of type [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
, containing a pointer to a type object and a reference count (these can be accessed using the macros [`Py_TYPE`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
 and [`Py_REFCNT`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
 respectively). The reason for the macro is to abstract away the layout and to enable additional fields in [debug builds](https://docs.python.org/3/using/configure.html#debug-build)
.

Note

There is no semicolon above after the [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
 macro. Be wary of adding one by accident: some compilers will complain.

Of course, objects generally store additional data besides the standard `PyObject_HEAD` boilerplate; for example, here is the definition for standard Python floats:

typedef struct {
    PyObject\_HEAD
    double ob\_fval;
} PyFloatObject;

The second bit is the definition of the type object.

static PyTypeObject CustomType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "custom.Custom",
    .tp\_doc \= PyDoc\_STR("Custom objects"),
    .tp\_basicsize \= sizeof(CustomObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT,
    .tp\_new \= PyType\_GenericNew,
};

Note

We recommend using C99-style designated initializers as above, to avoid listing all the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 fields that you don’t care about and also to avoid caring about the fields’ declaration order.

The actual definition of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 in `object.h` has many more [fields](https://docs.python.org/3/c-api/typeobj.html#type-structs)
 than the definition above. The remaining fields will be filled with zeros by the C compiler, and it’s common practice to not specify them explicitly unless you need them.

We’re going to pick it apart, one field at a time:

.ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)

This line is mandatory boilerplate to initialize the `ob_base` field mentioned above.

.tp\_name \= "custom.Custom",

The name of our type. This will appear in the default textual representation of our objects and in some error messages, for example:

Copy

\>>> "" + custom.Custom()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "custom.Custom") to str

Note that the name is a dotted name that includes both the module name and the name of the type within the module. The module in this case is `custom` and the type is `Custom`, so we set the type name to `custom.Custom`. Using the real dotted import path is important to make your type compatible with the [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 modules.

.tp\_basicsize \= sizeof(CustomObject),
.tp\_itemsize \= 0,

This is so that Python knows how much memory to allocate when creating new `Custom` instances. [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
 is only used for variable-sized objects and should otherwise be zero.

Note

If you want your type to be subclassable from Python, and your type has the same [`tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
 as its base type, you may have problems with multiple inheritance. A Python subclass of your type will have to list your type first in its [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
, or else it will not be able to call your type’s [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 method without getting an error. You can avoid this problem by ensuring that your type has a larger value for `tp_basicsize` than its base type does. Most of the time, this will be true anyway, because either your base type will be [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, or else you will be adding data members to your base type, and therefore increasing its size.

We set the class flags to [`Py_TPFLAGS_DEFAULT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DEFAULT "Py_TPFLAGS_DEFAULT")
.

.tp\_flags \= Py\_TPFLAGS\_DEFAULT,

All types should include this constant in their flags. It enables all of the members defined until at least Python 3.3. If you need further members, you will need to OR the corresponding flags.

We provide a doc string for the type in [`tp_doc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_doc "PyTypeObject.tp_doc")
.

.tp\_doc \= PyDoc\_STR("Custom objects"),

To enable object creation, we have to provide a [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 handler. This is the equivalent of the Python method [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
, but has to be specified explicitly. In this case, we can just use the default implementation provided by the API function [`PyType_GenericNew()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericNew "PyType_GenericNew")
.

.tp\_new \= PyType\_GenericNew,

Everything else in the file should be familiar, except for some code in `custom_module_exec()`:

if (PyType\_Ready(&CustomType) < 0) {
    return \-1;
}

This initializes the `Custom` type, filling in a number of members to the appropriate default values, including [`ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
 that we initially set to `NULL`.

if (PyModule\_AddObjectRef(m, "Custom", (PyObject \*) &CustomType) < 0) {
    return \-1;
}

This adds the type to the module dictionary. This allows us to create `Custom` instances by calling the `Custom` class:

Copy

\>>> import custom
\>>> mycustom \= custom.Custom()

That’s it! All that remains is to build it; put the above code in a file called `custom.c`,

\[build\-system\]
requires \= \["setuptools"\]
build\-backend \= "setuptools.build\_meta"

\[project\]
name \= "custom"
version \= "1"

in a file called `pyproject.toml`, and

Copy

from setuptools import Extension, setup
setup(ext\_modules\=\[Extension("custom", \["custom.c"\])\])

in a file called `setup.py`; then typing

Copy

$ python \-m pip install .

in a shell should produce a file `custom.so` in a subdirectory and install it; now fire up Python — you should be able to `import custom` and play around with `Custom` objects.

That wasn’t so hard, was it?

Of course, the current Custom type is pretty uninteresting. It has no data and doesn’t do anything. It can’t even be subclassed.

Adding data and methods to the Basic example[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#adding-data-and-methods-to-the-basic-example "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s extend the basic example to add some data and methods. Let’s also make the type usable as a base class. We’ll create a new module, `custom2` that adds these capabilities:

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>
#include <stddef.h> /\* for offsetof() \*/

typedef struct {
    PyObject\_HEAD
    PyObject \*first; /\* first name \*/
    PyObject \*last;  /\* last name \*/
    int number;
} CustomObject;

static void
Custom\_dealloc(PyObject \*op)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_XDECREF(self\->first);
    Py\_XDECREF(self\->last);
    Py\_TYPE(self)\->tp\_free(self);
}

static PyObject \*
Custom\_new(PyTypeObject \*type, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self;
    self \= (CustomObject \*) type\->tp\_alloc(type, 0);
    if (self != NULL) {
        self\->first \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->first \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->last \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->last \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->number \= 0;
    }
    return (PyObject \*) self;
}

static int
Custom\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self \= (CustomObject \*) op;
    static char \*kwlist\[\] \= {"first", "last", "number", NULL};
    PyObject \*first \= NULL, \*last \= NULL;

    if (!PyArg\_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self\->number))
        return \-1;

    if (first) {
        Py\_XSETREF(self\->first, Py\_NewRef(first));
    }
    if (last) {
        Py\_XSETREF(self\->last, Py\_NewRef(last));
    }
    return 0;
}

static PyMemberDef Custom\_members\[\] \= {
    {"first", Py\_T\_OBJECT\_EX, offsetof(CustomObject, first), 0,
     "first name"},
    {"last", Py\_T\_OBJECT\_EX, offsetof(CustomObject, last), 0,
     "last name"},
    {"number", Py\_T\_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /\* Sentinel \*/
};

static PyObject \*
Custom\_name(PyObject \*op, PyObject \*Py\_UNUSED(dummy))
{
    CustomObject \*self \= (CustomObject \*) op;
    if (self\->first \== NULL) {
        PyErr\_SetString(PyExc\_AttributeError, "first");
        return NULL;
    }
    if (self\->last \== NULL) {
        PyErr\_SetString(PyExc\_AttributeError, "last");
        return NULL;
    }
    return PyUnicode\_FromFormat("%S %S", self\->first, self\->last);
}

static PyMethodDef Custom\_methods\[\] \= {
    {"name", Custom\_name, METH\_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /\* Sentinel \*/
};

static PyTypeObject CustomType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "custom2.Custom",
    .tp\_doc \= PyDoc\_STR("Custom objects"),
    .tp\_basicsize \= sizeof(CustomObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE,
    .tp\_new \= Custom\_new,
    .tp\_init \= Custom\_init,
    .tp\_dealloc \= Custom\_dealloc,
    .tp\_members \= Custom\_members,
    .tp\_methods \= Custom\_methods,
};

static int
custom\_module\_exec(PyObject \*m)
{
    if (PyType\_Ready(&CustomType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "Custom", (PyObject \*) &CustomType) < 0) {
        return \-1;
    }

    return 0;
}

static PyModuleDef\_Slot custom\_module\_slots\[\] \= {
    {Py\_mod\_exec, custom\_module\_exec},
    {Py\_mod\_multiple\_interpreters, Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED},
    {0, NULL}
};

static PyModuleDef custom\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "custom2",
    .m\_doc \= "Example module that creates an extension type.",
    .m\_size \= 0,
    .m\_slots \= custom\_module\_slots,
};

PyMODINIT\_FUNC
PyInit\_custom2(void)
{
    return PyModuleDef\_Init(&custom\_module);
}

This version of the module has a number of changes.

The `Custom` type now has three data attributes in its C struct, _first_, _last_, and _number_. The _first_ and _last_ variables are Python strings containing first and last names. The _number_ attribute is a C integer.

The object structure is updated accordingly:

typedef struct {
    PyObject\_HEAD
    PyObject \*first; /\* first name \*/
    PyObject \*last;  /\* last name \*/
    int number;
} CustomObject;

Because we now have data to manage, we have to be more careful about object allocation and deallocation. At a minimum, we need a deallocation method:

static void
Custom\_dealloc(PyObject \*op)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_XDECREF(self\->first);
    Py\_XDECREF(self\->last);
    Py\_TYPE(self)\->tp\_free(self);
}

which is assigned to the [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 member:

.tp\_dealloc \= Custom\_dealloc,

This method first clears the reference counts of the two Python attributes. [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 correctly handles the case where its argument is `NULL` (which might happen here if `tp_new` failed midway). It then calls the [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 member of the object’s type (computed by `Py_TYPE(self)`) to free the object’s memory. Note that the object’s type might not be `CustomType`, because the object may be an instance of a subclass.

Note

The explicit cast to `CustomObject *` above is needed because we defined `Custom_dealloc` to take a `PyObject *` argument, as the `tp_dealloc` function pointer expects to receive a `PyObject *` argument. By assigning to the `tp_dealloc` slot of a type, we declare that it can only be called with instances of our `CustomObject` class, so the cast to `(CustomObject *)` is safe. This is object-oriented polymorphism, in C!

In existing code, or in previous versions of this tutorial, you might see similar functions take a pointer to the subtype object structure (`CustomObject*`) directly, like this:

Custom\_dealloc(CustomObject \*self)
{
    Py\_XDECREF(self\->first);
    Py\_XDECREF(self\->last);
    Py\_TYPE(self)\->tp\_free((PyObject \*) self);
}
...
.tp\_dealloc \= (destructor) Custom\_dealloc,

This does the same thing on all architectures that CPython supports, but according to the C standard, it invokes undefined behavior.

We want to make sure that the first and last names are initialized to empty strings, so we provide a `tp_new` implementation:

static PyObject \*
Custom\_new(PyTypeObject \*type, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self;
    self \= (CustomObject \*) type\->tp\_alloc(type, 0);
    if (self != NULL) {
        self\->first \= PyUnicode\_FromString("");
        if (self\->first \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->last \= PyUnicode\_FromString("");
        if (self\->last \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->number \= 0;
    }
    return (PyObject \*) self;
}

and install it in the [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 member:

.tp\_new \= Custom\_new,

The `tp_new` handler is responsible for creating (as opposed to initializing) objects of the type. It is exposed in Python as the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 method. It is not required to define a `tp_new` member, and indeed many extension types will simply reuse [`PyType_GenericNew()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericNew "PyType_GenericNew")
 as done in the first version of the `Custom` type above. In this case, we use the `tp_new` handler to initialize the `first` and `last` attributes to non-`NULL` default values.

`tp_new` is passed the type being instantiated (not necessarily `CustomType`, if a subclass is instantiated) and any arguments passed when the type was called, and is expected to return the instance created. `tp_new` handlers always accept positional and keyword arguments, but they often ignore the arguments, leaving the argument handling to initializer (a.k.a. `tp_init` in C or `__init__` in Python) methods.

Note

`tp_new` shouldn’t call `tp_init` explicitly, as the interpreter will do it itself.

The `tp_new` implementation calls the [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot to allocate memory:

self \= (CustomObject \*) type\->tp\_alloc(type, 0);

Since memory allocation may fail, we must check the [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 result against `NULL` before proceeding.

Note

We didn’t fill the [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot ourselves. Rather [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 fills it for us by inheriting it from our base class, which is [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 by default. Most types use the default allocation strategy.

Note

If you are creating a co-operative [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 (one that calls a base type’s `tp_new` or [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
), you must _not_ try to determine what method to call using method resolution order at runtime. Always statically determine what type you are going to call, and call its `tp_new` directly, or via `type->tp_base->tp_new`. If you do not do this, Python subclasses of your type that also inherit from other Python-defined classes may not work correctly. (Specifically, you may not be able to create instances of such subclasses without getting a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.)

We also define an initialization function which accepts arguments to provide initial values for our instance:

static int
Custom\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self \= (CustomObject \*) op;
    static char \*kwlist\[\] \= {"first", "last", "number", NULL};
    PyObject \*first \= NULL, \*last \= NULL, \*tmp;

    if (!PyArg\_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self\->number))
        return \-1;

    if (first) {
        tmp \= self\->first;
        Py\_INCREF(first);
        self\->first \= first;
        Py\_XDECREF(tmp);
    }
    if (last) {
        tmp \= self\->last;
        Py\_INCREF(last);
        self\->last \= last;
        Py\_XDECREF(tmp);
    }
    return 0;
}

by filling the [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 slot.

.tp\_init \= Custom\_init,

The [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 slot is exposed in Python as the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method. It is used to initialize an object after it’s created. Initializers always accept positional and keyword arguments, and they should return either `0` on success or `-1` on error.

Unlike the `tp_new` handler, there is no guarantee that `tp_init` is called at all (for example, the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 module by default doesn’t call [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 on unpickled instances). It can also be called multiple times. Anyone can call the `__init__()` method on our objects. For this reason, we have to be extra careful when assigning the new attribute values. We might be tempted, for example to assign the `first` member like this:

if (first) {
    Py\_XDECREF(self\->first);
    Py\_INCREF(first);
    self\->first \= first;
}

But this would be risky. Our type doesn’t restrict the type of the `first` member, so it could be any kind of object. It could have a destructor that causes code to be executed that tries to access the `first` member; or that destructor could detach the [thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 and let arbitrary code run in other threads that accesses and modifies our object.

To be paranoid and protect ourselves against this possibility, we almost always reassign members before decrementing their reference counts. When don’t we have to do this?

*   when we absolutely know that the reference count is greater than 1;
    
*   when we know that deallocation of the object [\[1\]](https://docs.python.org/3/extending/newtypes_tutorial.html#id5)
     will neither detach the [thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
     nor cause any calls back into our type’s code;
    
*   when decrementing a reference count in a [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
     handler on a type which doesn’t support cyclic garbage collection [\[2\]](https://docs.python.org/3/extending/newtypes_tutorial.html#id6)
    .
    

We want to expose our instance variables as attributes. There are a number of ways to do that. The simplest way is to define member definitions:

static PyMemberDef Custom\_members\[\] \= {
    {"first", Py\_T\_OBJECT\_EX, offsetof(CustomObject, first), 0,
     "first name"},
    {"last", Py\_T\_OBJECT\_EX, offsetof(CustomObject, last), 0,
     "last name"},
    {"number", Py\_T\_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /\* Sentinel \*/
};

and put the definitions in the [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members")
 slot:

.tp\_members \= Custom\_members,

Each member definition has a member name, type, offset, access flags and documentation string. See the [Generic Attribute Management](https://docs.python.org/3/extending/newtypes.html#generic-attribute-management)
 section below for details.

A disadvantage of this approach is that it doesn’t provide a way to restrict the types of objects that can be assigned to the Python attributes. We expect the first and last names to be strings, but any Python objects can be assigned. Further, the attributes can be deleted, setting the C pointers to `NULL`. Even though we can make sure the members are initialized to non-`NULL` values, the members can be set to `NULL` if the attributes are deleted.

We define a single method, `Custom.name()`, that outputs the objects name as the concatenation of the first and last names.

static PyObject \*
Custom\_name(PyObject \*op, PyObject \*Py\_UNUSED(dummy))
{
    CustomObject \*self \= (CustomObject \*) op;
    if (self\->first \== NULL) {
        PyErr\_SetString(PyExc\_AttributeError, "first");
        return NULL;
    }
    if (self\->last \== NULL) {
        PyErr\_SetString(PyExc\_AttributeError, "last");
        return NULL;
    }
    return PyUnicode\_FromFormat("%S %S", self\->first, self\->last);
}

The method is implemented as a C function that takes a `Custom` (or `Custom` subclass) instance as the first argument. Methods always take an instance as the first argument. Methods often take positional and keyword arguments as well, but in this case we don’t take any and don’t need to accept a positional argument tuple or keyword argument dictionary. This method is equivalent to the Python method:

Copy

def name(self):
    return "%s %s" % (self.first, self.last)

Note that we have to check for the possibility that our `first` and `last` members are `NULL`. This is because they can be deleted, in which case they are set to `NULL`. It would be better to prevent deletion of these attributes and to restrict the attribute values to be strings. We’ll see how to do that in the next section.

Now that we’ve defined the method, we need to create an array of method definitions:

static PyMethodDef Custom\_methods\[\] \= {
    {"name", Custom\_name, METH\_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /\* Sentinel \*/
};

(note that we used the [`METH_NOARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "METH_NOARGS")
 flag to indicate that the method is expecting no arguments other than _self_)

and assign it to the [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods")
 slot:

.tp\_methods \= Custom\_methods,

Finally, we’ll make our type usable as a base class for subclassing. We’ve written our methods carefully so far so that they don’t make any assumptions about the type of the object being created or used, so all we need to do is to add the [`Py_TPFLAGS_BASETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BASETYPE "Py_TPFLAGS_BASETYPE")
 to our class flag definition:

.tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE,

We rename `PyInit_custom()` to `PyInit_custom2()`, update the module name in the [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 struct, and update the full class name in the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 struct.

Finally, we update our `setup.py` file to include the new module,

Copy

from setuptools import Extension, setup
setup(ext\_modules\=\[\
    Extension("custom", \["custom.c"\]),\
    Extension("custom2", \["custom2.c"\]),\
\])

and then we re-install so that we can `import custom2`:

Copy

$ python \-m pip install .

Providing finer control over data attributes[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#providing-finer-control-over-data-attributes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we’ll provide finer control over how the `first` and `last` attributes are set in the `Custom` example. In the previous version of our module, the instance variables `first` and `last` could be set to non-string values or even deleted. We want to make sure that these attributes always contain strings.

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>
#include <stddef.h> /\* for offsetof() \*/

typedef struct {
    PyObject\_HEAD
    PyObject \*first; /\* first name \*/
    PyObject \*last;  /\* last name \*/
    int number;
} CustomObject;

static void
Custom\_dealloc(PyObject \*op)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_XDECREF(self\->first);
    Py\_XDECREF(self\->last);
    Py\_TYPE(self)\->tp\_free(self);
}

static PyObject \*
Custom\_new(PyTypeObject \*type, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self;
    self \= (CustomObject \*) type\->tp\_alloc(type, 0);
    if (self != NULL) {
        self\->first \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->first \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->last \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->last \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->number \= 0;
    }
    return (PyObject \*) self;
}

static int
Custom\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self \= (CustomObject \*) op;
    static char \*kwlist\[\] \= {"first", "last", "number", NULL};
    PyObject \*first \= NULL, \*last \= NULL;

    if (!PyArg\_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self\->number))
        return \-1;

    if (first) {
        Py\_SETREF(self\->first, Py\_NewRef(first));
    }
    if (last) {
        Py\_SETREF(self\->last, Py\_NewRef(last));
    }
    return 0;
}

static PyMemberDef Custom\_members\[\] \= {
    {"number", Py\_T\_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /\* Sentinel \*/
};

static PyObject \*
Custom\_getfirst(PyObject \*op, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    return Py\_NewRef(self\->first);
}

static int
Custom\_setfirst(PyObject \*op, PyObject \*value, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    if (value \== NULL) {
        PyErr\_SetString(PyExc\_TypeError, "Cannot delete the first attribute");
        return \-1;
    }
    if (!PyUnicode\_Check(value)) {
        PyErr\_SetString(PyExc\_TypeError,
                        "The first attribute value must be a string");
        return \-1;
    }
    Py\_SETREF(self\->first, Py\_NewRef(value));
    return 0;
}

static PyObject \*
Custom\_getlast(PyObject \*op, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    return Py\_NewRef(self\->last);
}

static int
Custom\_setlast(PyObject \*op, PyObject \*value, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    if (value \== NULL) {
        PyErr\_SetString(PyExc\_TypeError, "Cannot delete the last attribute");
        return \-1;
    }
    if (!PyUnicode\_Check(value)) {
        PyErr\_SetString(PyExc\_TypeError,
                        "The last attribute value must be a string");
        return \-1;
    }
    Py\_SETREF(self\->last, Py\_NewRef(value));
    return 0;
}

static PyGetSetDef Custom\_getsetters\[\] \= {
    {"first", Custom\_getfirst, Custom\_setfirst,
     "first name", NULL},
    {"last", Custom\_getlast, Custom\_setlast,
     "last name", NULL},
    {NULL}  /\* Sentinel \*/
};

static PyObject \*
Custom\_name(PyObject \*op, PyObject \*Py\_UNUSED(dummy))
{
    CustomObject \*self \= (CustomObject \*) op;
    return PyUnicode\_FromFormat("%S %S", self\->first, self\->last);
}

static PyMethodDef Custom\_methods\[\] \= {
    {"name", Custom\_name, METH\_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /\* Sentinel \*/
};

static PyTypeObject CustomType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "custom3.Custom",
    .tp\_doc \= PyDoc\_STR("Custom objects"),
    .tp\_basicsize \= sizeof(CustomObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE,
    .tp\_new \= Custom\_new,
    .tp\_init \= Custom\_init,
    .tp\_dealloc \= Custom\_dealloc,
    .tp\_members \= Custom\_members,
    .tp\_methods \= Custom\_methods,
    .tp\_getset \= Custom\_getsetters,
};

static int
custom\_module\_exec(PyObject \*m)
{
    if (PyType\_Ready(&CustomType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "Custom", (PyObject \*) &CustomType) < 0) {
        return \-1;
    }

    return 0;
}

static PyModuleDef\_Slot custom\_module\_slots\[\] \= {
    {Py\_mod\_exec, custom\_module\_exec},
    {Py\_mod\_multiple\_interpreters, Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED},
    {0, NULL}
};

static PyModuleDef custom\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "custom3",
    .m\_doc \= "Example module that creates an extension type.",
    .m\_size \= 0,
    .m\_slots \= custom\_module\_slots,
};

PyMODINIT\_FUNC
PyInit\_custom3(void)
{
    return PyModuleDef\_Init(&custom\_module);
}

To provide greater control, over the `first` and `last` attributes, we’ll use custom getter and setter functions. Here are the functions for getting and setting the `first` attribute:

static PyObject \*
Custom\_getfirst(PyObject \*op, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_INCREF(self\->first);
    return self\->first;
}

static int
Custom\_setfirst(PyObject \*op, PyObject \*value, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    PyObject \*tmp;
    if (value \== NULL) {
        PyErr\_SetString(PyExc\_TypeError, "Cannot delete the first attribute");
        return \-1;
    }
    if (!PyUnicode\_Check(value)) {
        PyErr\_SetString(PyExc\_TypeError,
                        "The first attribute value must be a string");
        return \-1;
    }
    tmp \= self\->first;
    Py\_INCREF(value);
    self\->first \= value;
    Py\_DECREF(tmp);
    return 0;
}

The getter function is passed a `Custom` object and a “closure”, which is a void pointer. In this case, the closure is ignored. (The closure supports an advanced usage in which definition data is passed to the getter and setter. This could, for example, be used to allow a single set of getter and setter functions that decide the attribute to get or set based on data in the closure.)

The setter function is passed the `Custom` object, the new value, and the closure. The new value may be `NULL`, in which case the attribute is being deleted. In our setter, we raise an error if the attribute is deleted or if its new value is not a string.

We create an array of [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structures:

static PyGetSetDef Custom\_getsetters\[\] \= {
    {"first", Custom\_getfirst, Custom\_setfirst,
     "first name", NULL},
    {"last", Custom\_getlast, Custom\_setlast,
     "last name", NULL},
    {NULL}  /\* Sentinel \*/
};

and register it in the [`tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "PyTypeObject.tp_getset")
 slot:

.tp\_getset \= Custom\_getsetters,

The last item in a [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structure is the “closure” mentioned above. In this case, we aren’t using a closure, so we just pass `NULL`.

We also remove the member definitions for these attributes:

static PyMemberDef Custom\_members\[\] \= {
    {"number", Py\_T\_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /\* Sentinel \*/
};

We also need to update the [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 handler to only allow strings [\[3\]](https://docs.python.org/3/extending/newtypes_tutorial.html#id7)
 to be passed:

static int
Custom\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self \= (CustomObject \*) op;
    static char \*kwlist\[\] \= {"first", "last", "number", NULL};
    PyObject \*first \= NULL, \*last \= NULL, \*tmp;

    if (!PyArg\_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self\->number))
        return \-1;

    if (first) {
        tmp \= self\->first;
        Py\_INCREF(first);
        self\->first \= first;
        Py\_DECREF(tmp);
    }
    if (last) {
        tmp \= self\->last;
        Py\_INCREF(last);
        self\->last \= last;
        Py\_DECREF(tmp);
    }
    return 0;
}

With these changes, we can assure that the `first` and `last` members are never `NULL` so we can remove checks for `NULL` values in almost all cases. This means that most of the [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 calls can be converted to [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 calls. The only place we can’t change these calls is in the `tp_dealloc` implementation, where there is the possibility that the initialization of these members failed in `tp_new`.

We also rename the module initialization function and module name in the initialization function, as we did before, and we add an extra definition to the `setup.py` file.

Supporting cyclic garbage collection[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#supporting-cyclic-garbage-collection "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Python has a [cyclic garbage collector (GC)](https://docs.python.org/3/glossary.html#term-garbage-collection)
 that can identify unneeded objects even when their reference counts are not zero. This can happen when objects are involved in cycles. For example, consider:

Copy

\>>> l \= \[\]
\>>> l.append(l)
\>>> del l

In this example, we create a list that contains itself. When we delete it, it still has a reference from itself. Its reference count doesn’t drop to zero. Fortunately, Python’s cyclic garbage collector will eventually figure out that the list is garbage and free it.

In the second version of the `Custom` example, we allowed any kind of object to be stored in the `first` or `last` attributes [\[4\]](https://docs.python.org/3/extending/newtypes_tutorial.html#id8)
. Besides, in the second and third versions, we allowed subclassing `Custom`, and subclasses may add arbitrary attributes. For any of those two reasons, `Custom` objects can participate in cycles:

Copy

\>>> import custom3
\>>> class Derived(custom3.Custom): pass
...
\>>> n \= Derived()
\>>> n.some\_attribute \= n

To allow a `Custom` instance participating in a reference cycle to be properly detected and collected by the cyclic GC, our `Custom` type needs to fill two additional slots and to enable a flag that enables these slots:

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>
#include <stddef.h> /\* for offsetof() \*/

typedef struct {
    PyObject\_HEAD
    PyObject \*first; /\* first name \*/
    PyObject \*last;  /\* last name \*/
    int number;
} CustomObject;

static int
Custom\_traverse(PyObject \*op, visitproc visit, void \*arg)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_VISIT(self\->first);
    Py\_VISIT(self\->last);
    return 0;
}

static int
Custom\_clear(PyObject \*op)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_CLEAR(self\->first);
    Py\_CLEAR(self\->last);
    return 0;
}

static void
Custom\_dealloc(PyObject \*op)
{
    PyObject\_GC\_UnTrack(op);
    (void)Custom\_clear(op);
    Py\_TYPE(op)\->tp\_free(op);
}

static PyObject \*
Custom\_new(PyTypeObject \*type, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self;
    self \= (CustomObject \*) type\->tp\_alloc(type, 0);
    if (self != NULL) {
        self\->first \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->first \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->last \= Py\_GetConstant(Py\_CONSTANT\_EMPTY\_STR);
        if (self\->last \== NULL) {
            Py\_DECREF(self);
            return NULL;
        }
        self\->number \= 0;
    }
    return (PyObject \*) self;
}

static int
Custom\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    CustomObject \*self \= (CustomObject \*) op;
    static char \*kwlist\[\] \= {"first", "last", "number", NULL};
    PyObject \*first \= NULL, \*last \= NULL;

    if (!PyArg\_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self\->number))
        return \-1;

    if (first) {
        Py\_SETREF(self\->first, Py\_NewRef(first));
    }
    if (last) {
        Py\_SETREF(self\->last, Py\_NewRef(last));
    }
    return 0;
}

static PyMemberDef Custom\_members\[\] \= {
    {"number", Py\_T\_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /\* Sentinel \*/
};

static PyObject \*
Custom\_getfirst(PyObject \*op, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    return Py\_NewRef(self\->first);
}

static int
Custom\_setfirst(PyObject \*op, PyObject \*value, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    if (value \== NULL) {
        PyErr\_SetString(PyExc\_TypeError, "Cannot delete the first attribute");
        return \-1;
    }
    if (!PyUnicode\_Check(value)) {
        PyErr\_SetString(PyExc\_TypeError,
                        "The first attribute value must be a string");
        return \-1;
    }
    Py\_XSETREF(self\->first, Py\_NewRef(value));
    return 0;
}

static PyObject \*
Custom\_getlast(PyObject \*op, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    return Py\_NewRef(self\->last);
}

static int
Custom\_setlast(PyObject \*op, PyObject \*value, void \*closure)
{
    CustomObject \*self \= (CustomObject \*) op;
    if (value \== NULL) {
        PyErr\_SetString(PyExc\_TypeError, "Cannot delete the last attribute");
        return \-1;
    }
    if (!PyUnicode\_Check(value)) {
        PyErr\_SetString(PyExc\_TypeError,
                        "The last attribute value must be a string");
        return \-1;
    }
    Py\_XSETREF(self\->last, Py\_NewRef(value));
    return 0;
}

static PyGetSetDef Custom\_getsetters\[\] \= {
    {"first", Custom\_getfirst, Custom\_setfirst,
     "first name", NULL},
    {"last", Custom\_getlast, Custom\_setlast,
     "last name", NULL},
    {NULL}  /\* Sentinel \*/
};

static PyObject \*
Custom\_name(PyObject \*op, PyObject \*Py\_UNUSED(dummy))
{
    CustomObject \*self \= (CustomObject \*) op;
    return PyUnicode\_FromFormat("%S %S", self\->first, self\->last);
}

static PyMethodDef Custom\_methods\[\] \= {
    {"name", Custom\_name, METH\_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /\* Sentinel \*/
};

static PyTypeObject CustomType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "custom4.Custom",
    .tp\_doc \= PyDoc\_STR("Custom objects"),
    .tp\_basicsize \= sizeof(CustomObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE | Py\_TPFLAGS\_HAVE\_GC,
    .tp\_new \= Custom\_new,
    .tp\_init \= Custom\_init,
    .tp\_dealloc \= Custom\_dealloc,
    .tp\_traverse \= Custom\_traverse,
    .tp\_clear \= Custom\_clear,
    .tp\_members \= Custom\_members,
    .tp\_methods \= Custom\_methods,
    .tp\_getset \= Custom\_getsetters,
};

static int
custom\_module\_exec(PyObject \*m)
{
    if (PyType\_Ready(&CustomType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "Custom", (PyObject \*) &CustomType) < 0) {
        return \-1;
    }

    return 0;
}

static PyModuleDef\_Slot custom\_module\_slots\[\] \= {
    {Py\_mod\_exec, custom\_module\_exec},
    {Py\_mod\_multiple\_interpreters, Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED},
    {0, NULL}
};

static PyModuleDef custom\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "custom4",
    .m\_doc \= "Example module that creates an extension type.",
    .m\_size \= 0,
    .m\_slots \= custom\_module\_slots,
};

PyMODINIT\_FUNC
PyInit\_custom4(void)
{
    return PyModuleDef\_Init(&custom\_module);
}

First, the traversal method lets the cyclic GC know about subobjects that could participate in cycles:

static int
Custom\_traverse(PyObject \*op, visitproc visit, void \*arg)
{
    CustomObject \*self \= (CustomObject \*) op;
    int vret;
    if (self\->first) {
        vret \= visit(self\->first, arg);
        if (vret != 0)
            return vret;
    }
    if (self\->last) {
        vret \= visit(self\->last, arg);
        if (vret != 0)
            return vret;
    }
    return 0;
}

For each subobject that can participate in cycles, we need to call the `visit()` function, which is passed to the traversal method. The `visit()` function takes as arguments the subobject and the extra argument _arg_ passed to the traversal method. It returns an integer value that must be returned if it is non-zero.

Python provides a [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
 macro that automates calling visit functions. With `Py_VISIT()`, we can minimize the amount of boilerplate in `Custom_traverse`:

static int
Custom\_traverse(PyObject \*op, visitproc visit, void \*arg)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_VISIT(self\->first);
    Py\_VISIT(self\->last);
    return 0;
}

Note

The [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 implementation must name its arguments exactly _visit_ and _arg_ in order to use [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
.

Second, we need to provide a method for clearing any subobjects that can participate in cycles:

static int
Custom\_clear(PyObject \*op)
{
    CustomObject \*self \= (CustomObject \*) op;
    Py\_CLEAR(self\->first);
    Py\_CLEAR(self\->last);
    return 0;
}

Notice the use of the [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
 macro. It is the recommended and safe way to clear data attributes of arbitrary types while decrementing their reference counts. If you were to call [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 instead on the attribute before setting it to `NULL`, there is a possibility that the attribute’s destructor would call back into code that reads the attribute again (_especially_ if there is a reference cycle).

Note

You could emulate [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
 by writing:

PyObject \*tmp;
tmp \= self\->first;
self\->first \= NULL;
Py\_XDECREF(tmp);

Nevertheless, it is much easier and less error-prone to always use [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
 when deleting an attribute. Don’t try to micro-optimize at the expense of robustness!

The deallocator `Custom_dealloc` may call arbitrary code when clearing attributes. It means the circular GC can be triggered inside the function. Since the GC assumes reference count is not zero, we need to untrack the object from the GC by calling [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
 before clearing members. Here is our reimplemented deallocator using `PyObject_GC_UnTrack()` and `Custom_clear`:

static void
Custom\_dealloc(PyObject \*op)
{
    PyObject\_GC\_UnTrack(op);
    (void)Custom\_clear(op);
    Py\_TYPE(op)\->tp\_free(op);
}

Finally, we add the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag to the class flags:

.tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE | Py\_TPFLAGS\_HAVE\_GC,

That’s pretty much it. If we had written custom [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 or [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 handlers, we’d need to modify them for cyclic garbage collection. Most extensions will use the versions automatically provided.

Subclassing other types[¶](https://docs.python.org/3/extending/newtypes_tutorial.html#subclassing-other-types "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

It is possible to create new extension types that are derived from existing types. It is easiest to inherit from the built in types, since an extension can easily use the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 it needs. It can be difficult to share these `PyTypeObject` structures between extension modules.

In this example we will create a `SubList` type that inherits from the built-in [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 type. The new type will be completely compatible with regular lists, but will have an additional `increment()` method that increases an internal counter:

Copy

\>>> import sublist
\>>> s \= sublist.SubList(range(3))
\>>> s.extend(s)
\>>> print(len(s))
6
\>>> print(s.increment())
1
\>>> print(s.increment())
2

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>

typedef struct {
    PyListObject list;
    int state;
} SubListObject;

static PyObject \*
SubList\_increment(PyObject \*op, PyObject \*Py\_UNUSED(dummy))
{
    SubListObject \*self \= (SubListObject \*) op;
    self\->state++;
    return PyLong\_FromLong(self\->state);
}

static PyMethodDef SubList\_methods\[\] \= {
    {"increment", SubList\_increment, METH\_NOARGS,
     PyDoc\_STR("increment state counter")},
    {NULL},
};

static int
SubList\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    SubListObject \*self \= (SubListObject \*) op;
    if (PyList\_Type.tp\_init(op, args, kwds) < 0)
        return \-1;
    self\->state \= 0;
    return 0;
}

static PyTypeObject SubListType \= {
    .ob\_base \= PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "sublist.SubList",
    .tp\_doc \= PyDoc\_STR("SubList objects"),
    .tp\_basicsize \= sizeof(SubListObject),
    .tp\_itemsize \= 0,
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE,
    .tp\_init \= SubList\_init,
    .tp\_methods \= SubList\_methods,
};

static int
sublist\_module\_exec(PyObject \*m)
{
    SubListType.tp\_base \= &PyList\_Type;
    if (PyType\_Ready(&SubListType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "SubList", (PyObject \*) &SubListType) < 0) {
        return \-1;
    }

    return 0;
}

static PyModuleDef\_Slot sublist\_module\_slots\[\] \= {
    {Py\_mod\_exec, sublist\_module\_exec},
    {Py\_mod\_multiple\_interpreters, Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED},
    {0, NULL}
};

static PyModuleDef sublist\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "sublist",
    .m\_doc \= "Example module that creates an extension type.",
    .m\_size \= 0,
    .m\_slots \= sublist\_module\_slots,
};

PyMODINIT\_FUNC
PyInit\_sublist(void)
{
    return PyModuleDef\_Init(&sublist\_module);
}

As you can see, the source code closely resembles the `Custom` examples in previous sections. We will break down the main differences between them.

typedef struct {
    PyListObject list;
    int state;
} SubListObject;

The primary difference for derived type objects is that the base type’s object structure must be the first value. The base type will already include the [`PyObject_HEAD()`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
 at the beginning of its structure.

When a Python object is a `SubList` instance, its `PyObject *` pointer can be safely cast to both `PyListObject *` and `SubListObject *`:

static int
SubList\_init(PyObject \*op, PyObject \*args, PyObject \*kwds)
{
    SubListObject \*self \= (SubListObject \*) op;
    if (PyList\_Type.tp\_init(op, args, kwds) < 0)
        return \-1;
    self\->state \= 0;
    return 0;
}

We see above how to call through to the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method of the base type.

This pattern is important when writing a type with custom [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 and [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 members. The `tp_new` handler should not actually create the memory for the object with its [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
, but let the base class handle it by calling its own `tp_new`.

The [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 struct supports a [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
 specifying the type’s concrete base class. Due to cross-platform compiler issues, you can’t fill that field directly with a reference to [`PyList_Type`](https://docs.python.org/3/c-api/list.html#c.PyList_Type "PyList_Type")
; it should be done in the [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 function:

static int
sublist\_module\_exec(PyObject \*m)
{
    SubListType.tp\_base \= &PyList\_Type;
    if (PyType\_Ready(&SubListType) < 0) {
        return \-1;
    }

    if (PyModule\_AddObjectRef(m, "SubList", (PyObject \*) &SubListType) < 0) {
        return \-1;
    }

    return 0;
}

Before calling [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
, the type structure must have the [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
 slot filled in. When we are deriving an existing type, it is not necessary to fill out the [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot with [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 – the allocation function from the base type will be inherited.

After that, calling [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 and adding the type object to the module is the same as with the basic `Custom` examples.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html#)
    *   [The Basics](https://docs.python.org/3/extending/newtypes_tutorial.html#the-basics)
        
    *   [Adding data and methods to the Basic example](https://docs.python.org/3/extending/newtypes_tutorial.html#adding-data-and-methods-to-the-basic-example)
        
    *   [Providing finer control over data attributes](https://docs.python.org/3/extending/newtypes_tutorial.html#providing-finer-control-over-data-attributes)
        
    *   [Supporting cyclic garbage collection](https://docs.python.org/3/extending/newtypes_tutorial.html#supporting-cyclic-garbage-collection)
        
    *   [Subclassing other types](https://docs.python.org/3/extending/newtypes_tutorial.html#subclassing-other-types)
        

#### Previous topic

[Using the C API: Assorted topics](https://docs.python.org/3/extending/extending.html "previous chapter")

#### Next topic

[Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Defining+Extension+Types%3A+Tutorial&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fextending%2Fnewtypes_tutorial.html&pagesource=extending%2Fnewtypes_tutorial.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/extending/newtypes_tutorial.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/newtypes.html "Defining Extension Types: Assorted Topics")
     |
*   [previous](https://docs.python.org/3/extending/extending.html "Using the C API: Assorted topics")
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
*   [Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html)
    
*    
    
    |
*   Theme Auto Light Dark |