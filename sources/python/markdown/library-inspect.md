### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/annotationlib.html "annotationlib — Functionality for introspecting annotations")
     |
*   [previous](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`inspect` — Inspect live objects[¶](https://docs.python.org/3/library/inspect.html#inspect-inspect-live-objects "Link to this heading")

========================================================================================================================================

**Source code:** [Lib/inspect.py](https://github.com/python/cpython/tree/3.15/Lib/inspect.py)

* * *

The `inspect` module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects. For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function, or get all the information you need to display a detailed traceback.

There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the interpreter stack.

Types and members[¶](https://docs.python.org/3/library/inspect.html#types-and-members "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The [`getmembers()`](https://docs.python.org/3/library/inspect.html#inspect.getmembers "inspect.getmembers")
 function retrieves the members of an object such as a class or module. The functions whose names begin with “is” are mainly provided as convenient choices for the second argument to `getmembers()`. They also help you determine when you can expect to find the following special attributes (see [Import-related attributes on module objects](https://docs.python.org/3/reference/datamodel.html#import-mod-attrs)
 for module attributes):

| Type | Attribute | Description |
| --- | --- | --- |
| class | \_\_doc\_\_ | documentation string |
|     | \_\_name\_\_ | name with which this class was defined |
|     | \_\_qualname\_\_ | qualified name |
|     | \_\_module\_\_ | name of module in which this class was defined |
|     | \_\_type\_params\_\_ | A tuple containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)<br> of a generic class |
| method | \_\_doc\_\_ | documentation string |
|     | \_\_name\_\_ | name with which this method was defined |
|     | \_\_qualname\_\_ | qualified name |
|     | \_\_func\_\_ | function object containing implementation of method |
|     | \_\_self\_\_ | instance to which this method is bound, or `None` |
|     | \_\_module\_\_ | name of module in which this method was defined |
| function | \_\_doc\_\_ | documentation string |
|     | \_\_name\_\_ | name with which this function was defined |
|     | \_\_qualname\_\_ | qualified name |
|     | \_\_code\_\_ | code object containing compiled function [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) |
|     | \_\_defaults\_\_ | tuple of any default values for positional or keyword parameters |
|     | \_\_kwdefaults\_\_ | mapping of any default values for keyword-only parameters |
|     | \_\_globals\_\_ | global namespace in which this function was defined |
|     | \_\_builtins\_\_ | builtins namespace |
|     | \_\_annotations\_\_ | mapping of parameters names to annotations; `"return"` key is reserved for return annotations. |
|     | \_\_type\_params\_\_ | A tuple containing the [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params)<br> of a generic function |
|     | \_\_module\_\_ | name of module in which this function was defined |
| traceback | tb\_frame | frame object at this level |
|     | tb\_lasti | index of last attempted instruction in bytecode |
|     | tb\_lineno | current line number in Python source code |
|     | tb\_next | next inner traceback object (called by this level) |
| frame | f\_back | next outer frame object (this frame’s caller) |
|     | f\_builtins | builtins namespace seen by this frame |
|     | f\_code | code object being executed in this frame |
|     | f\_globals | global namespace seen by this frame |
|     | f\_lasti | index of last attempted instruction in bytecode |
|     | f\_lineno | current line number in Python source code |
|     | f\_locals | local namespace seen by this frame |
|     | f\_generator | returns the generator or coroutine object that owns this frame, or `None` if the frame is of a regular function |
|     | f\_trace | tracing function for this frame, or `None` |
|     | f\_trace\_lines | indicate whether a tracing event is triggered for each source source line |
|     | f\_trace\_opcodes | indicate whether per-opcode events are requested |
|     | clear() | used to clear all references to local variables |
| code | co\_argcount | number of arguments (not including keyword only arguments, \* or \*\* args) |
|     | co\_code | string of raw compiled bytecode |
|     | co\_cellvars | tuple of names of cell variables (referenced by containing scopes) |
|     | co\_consts | tuple of constants used in the bytecode |
|     | co\_filename | name of file in which this code object was created |
|     | co\_firstlineno | number of first line in Python source code |
|     | co\_flags | bitmap of `CO_*` flags, read more [here](https://docs.python.org/3/library/inspect.html#inspect-module-co-flags) |
|     | co\_freevars | tuple of names of free variables (referenced via a function’s closure) |
|     | co\_posonlyargcount | number of positional only arguments |
|     | co\_kwonlyargcount | number of keyword only arguments (not including \*\* arg) |
|     | co\_name | name with which this code object was defined |
|     | co\_qualname | fully qualified name with which this code object was defined |
|     | co\_names | tuple of names other than arguments and function locals |
|     | co\_nlocals | number of local variables |
|     | co\_stacksize | virtual machine stack space required |
|     | co\_varnames | tuple of names of arguments and local variables |
|     | co\_lines() | returns an iterator that yields successive bytecode ranges |
|     | co\_positions() | returns an iterator of source code positions for each bytecode instruction |
|     | replace() | returns a copy of the code object with new values |
| generator | \_\_name\_\_ | name |
|     | \_\_qualname\_\_ | qualified name |
|     | gi\_frame | frame |
|     | gi\_running | is the generator running? |
|     | gi\_suspended | is the generator suspended? |
|     | gi\_code | code |
|     | gi\_yieldfrom | object being iterated by `yield from`, or `None` |
|     | gi\_state | state of the generator, one of `GEN_CREATED`, `GEN_RUNNING`, `GEN_SUSPENDED`, or `GEN_CLOSED` |
| async generator | \_\_name\_\_ | name |
|     | \_\_qualname\_\_ | qualified name |
|     | ag\_await | object being awaited on, or `None` |
|     | ag\_frame | frame |
|     | ag\_running | is the generator running? |
|     | ag\_suspended | is the generator suspended? |
|     | ag\_code | code |
|     | ag\_state | state of the async generator, one of `AGEN_CREATED`, `AGEN_RUNNING`, `AGEN_SUSPENDED`, or `AGEN_CLOSED` |
| coroutine | \_\_name\_\_ | name |
|     | \_\_qualname\_\_ | qualified name |
|     | cr\_await | object being awaited on, or `None` |
|     | cr\_frame | frame |
|     | cr\_running | is the coroutine running? |
|     | cr\_suspended | is the coroutine suspended? |
|     | cr\_code | code |
|     | cr\_origin | where coroutine was created, or `None`. See [`sys.set_coroutine_origin_tracking_depth()`](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "sys.set_coroutine_origin_tracking_depth") |
|     | cr\_state | state of the coroutine, one of `CORO_CREATED`, `CORO_RUNNING`, `CORO_SUSPENDED`, or `CORO_CLOSED` |
| builtin | \_\_doc\_\_ | documentation string |
|     | \_\_name\_\_ | original name of this function or method |
|     | \_\_qualname\_\_ | qualified name |
|     | \_\_self\_\_ | instance to which a method is bound, or module object a function was defined in, or `None` |

Changed in version 3.5: Add `__qualname__` and `gi_yieldfrom` attributes to generators.

The `__name__` attribute of generators is now set from the function name, instead of the code name, and it can now be modified.

Changed in version 3.7: Add `cr_origin` attribute to coroutines.

Changed in version 3.10: Add `__builtins__` attribute to functions.

Changed in version 3.11: Add `gi_suspended` attribute to generators.

Changed in version 3.11: Add `cr_suspended` attribute to coroutines.

Changed in version 3.12: Add `ag_suspended` attribute to async generators.

Changed in version 3.14: Add `f_generator` attribute to frames.

Changed in version 3.15: Add `gi_state` attribute to generators, `cr_state` attribute to coroutines, and `ag_state` attribute to async generators.

inspect.getmembers(_object_\[, _predicate_\])[¶](https://docs.python.org/3/library/inspect.html#inspect.getmembers "Link to this definition")

Return all the members of an object in a list of `(name, value)` pairs sorted by name. If the optional _predicate_ argument—which will be called with the `value` object of each member—is supplied, only members for which the predicate returns a true value are included.

Note

`getmembers()` will only return class attributes defined in the metaclass when the argument is a class and those attributes have been listed in the metaclass’ custom [`__dir__()`](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "object.__dir__")
.

inspect.getmembers\_static(_object_\[, _predicate_\])[¶](https://docs.python.org/3/library/inspect.html#inspect.getmembers_static "Link to this definition")

Return all the members of an object in a list of `(name, value)` pairs sorted by name without triggering dynamic lookup via the descriptor protocol, \_\_getattr\_\_ or \_\_getattribute\_\_. Optionally, only return members that satisfy a given predicate.

Note

`getmembers_static()` may not be able to retrieve all members that getmembers can fetch (like dynamically created attributes) and may find members that getmembers can’t (like descriptors that raise AttributeError). It can also return descriptor objects instead of instance members in some cases.

Added in version 3.11.

inspect.getmodulename(_path_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getmodulename "Link to this definition")

Return the name of the module named by the file _path_, without including the names of enclosing packages. The file extension is checked against all of the entries in [`importlib.machinery.all_suffixes()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.all_suffixes "importlib.machinery.all_suffixes")
. If it matches, the final path component is returned with the extension removed. Otherwise, `None` is returned.

Note that this function _only_ returns a meaningful name for actual Python modules - paths that potentially refer to Python packages will still return `None`.

Changed in version 3.3: The function is based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
.

inspect.ismodule(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismodule "Link to this definition")

Return `True` if the object is a module.

inspect.isclass(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isclass "Link to this definition")

Return `True` if the object is a class, whether built-in or created in Python code.

This function returns `False` for [generic aliases](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 of classes, such as `list[int]`.

inspect.ismethod(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethod "Link to this definition")

Return `True` if the object is a bound method written in Python.

Note

For example, given this class:

Copy

\>>> class Greeter:
...     def say\_hello(self):
...         print('hello!')

A bound method (also known as an _instance method_) is created when accessing `say_hello` (a [function](https://docs.python.org/3/glossary.html#term-function)
 defined in the `Greeter` namespace) through an instance of the `Greeter` class:

Copy

\>>> instance \= Greeter()

\>>> instance.say\_hello
<bound method Greeter.say\_hello of <\_\_main\_\_.Greeter object ...>>
\>>> ismethod(instance.say\_hello)
True
\>>> isfunction(instance.say\_hello)
False

Accessing `say_hello` through the `Greeter` class will return the function itself. For this function, `ismethod()` will return `False`, but [`isfunction()`](https://docs.python.org/3/library/inspect.html#inspect.isfunction "inspect.isfunction")
 will return `True`:

Copy

\>>> Greeter.say\_hello
<function Greeter.say\_hello at 0x7f7503854a90>
\>>> ismethod(Greeter.say\_hello)
False
\>>> isfunction(Greeter.say\_hello)
True

See [Methods](https://docs.python.org/3/builtins/stdtypes.html#typesmethods)
 for details.

inspect.isfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isfunction "Link to this definition")

Return `True` if the object is a Python function, which includes functions created by a [lambda](https://docs.python.org/3/glossary.html#term-lambda)
 expression.

See the note for [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod")
 for an example.

inspect.ispackage(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ispackage "Link to this definition")

Return `True` if the object is a [package](https://docs.python.org/3/glossary.html#term-package)
.

Added in version 3.14.

inspect.isgeneratorfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgeneratorfunction "Link to this definition")

Return `True` if the object is a Python generator function.

It also returns `True` for bound methods created from Python generator functions (see [Methods](https://docs.python.org/3/builtins/stdtypes.html#typesmethods)
 for more information).

Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 now return `True` if the wrapped function is a Python generator function.

Changed in version 3.10.6: [Duck-typed](https://docs.python.org/3/glossary.html#term-duck-typing)
 function-like objects now return `True` if their code object has the [`CO_GENERATOR`](https://docs.python.org/3/library/inspect.html#inspect.CO_GENERATOR "inspect.CO_GENERATOR")
 flag.

Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod")
 now return `True` if the wrapped function is a Python generator function.

inspect.isgenerator(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgenerator "Link to this definition")

Return `True` if the object is a generator.

inspect.iscoroutinefunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "Link to this definition")

Return `True` if the object is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
 (a function defined with an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 syntax), a [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 wrapping a coroutine function, or a sync function marked with [`markcoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "inspect.markcoroutinefunction")
.

Added in version 3.5.

Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 now return `True` if the wrapped function is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
.

Changed in version 3.10.6: [Duck-typed](https://docs.python.org/3/glossary.html#term-duck-typing)
 function-like objects now return `True` if their code object has the [`CO_COROUTINE`](https://docs.python.org/3/library/inspect.html#inspect.CO_COROUTINE "inspect.CO_COROUTINE")
 flag.

Changed in version 3.12: Sync functions marked with [`markcoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "inspect.markcoroutinefunction")
 now return `True`.

Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod")
 now return `True` if the wrapped function is a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
.

inspect.markcoroutinefunction(_func_)[¶](https://docs.python.org/3/library/inspect.html#inspect.markcoroutinefunction "Link to this definition")

Decorator to mark a callable as a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
 if it would not otherwise be detected by [`iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction")
.

This may be of use for sync functions that return a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
, if the function is passed to an API that requires [`iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction")
.

When possible, using an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 function is preferred. Also acceptable is calling the function and testing the return with [`iscoroutine()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutine "inspect.iscoroutine")
.

Added in version 3.12.

inspect.iscoroutine(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscoroutine "Link to this definition")

Return `True` if the object is a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 created by an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 function.

Added in version 3.5.

inspect.isawaitable(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "Link to this definition")

Return `True` if the object can be used in [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expression.

Can also be used to distinguish generator-based coroutines from regular generators:

Copy

import types

def gen():
    yield
@types.coroutine
def gen\_coro():
    yield

assert not isawaitable(gen())
assert isawaitable(gen\_coro())

Added in version 3.5.

inspect.isasyncgenfunction(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isasyncgenfunction "Link to this definition")

Return `True` if the object is an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function, for example:

Copy

\>>> async def agen():
...     yield 1
...
\>>> inspect.isasyncgenfunction(agen)
True

Added in version 3.6.

Changed in version 3.8: Functions wrapped in [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 now return `True` if the wrapped function is an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function.

Changed in version 3.10.6: [Duck-typed](https://docs.python.org/3/glossary.html#term-duck-typing)
 function-like objects now return `True` if their code object has the [`CO_ASYNC_GENERATOR`](https://docs.python.org/3/library/inspect.html#inspect.CO_ASYNC_GENERATOR "inspect.CO_ASYNC_GENERATOR")
 flag.

Changed in version 3.13: Functions wrapped in [`functools.partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod")
 now return `True` if the wrapped function is a [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function.

inspect.isasyncgen(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isasyncgen "Link to this definition")

Return `True` if the object is an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator)
 created by an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function.

Added in version 3.6.

inspect.istraceback(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.istraceback "Link to this definition")

Return `True` if the object is a traceback.

inspect.isframe(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isframe "Link to this definition")

Return `True` if the object is a frame.

inspect.iscode(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.iscode "Link to this definition")

Return `True` if the object is a code.

inspect.isbuiltin(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isbuiltin "Link to this definition")

Return `True` if the object is a built-in function or a bound built-in method.

inspect.ismethodwrapper(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethodwrapper "Link to this definition")

Return `True` if the type of object is a [`MethodWrapperType`](https://docs.python.org/3/library/types.html#types.MethodWrapperType "types.MethodWrapperType")
.

These are instances of [`MethodWrapperType`](https://docs.python.org/3/library/types.html#types.MethodWrapperType "types.MethodWrapperType")
, such as [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__")
, [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
.

Added in version 3.11.

inspect.isroutine(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isroutine "Link to this definition")

Return `True` if the object is a user-defined or built-in function or method.

inspect.isabstract(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isabstract "Link to this definition")

Return `True` if the object is an abstract base class.

inspect.ismethoddescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismethoddescriptor "Link to this definition")

Return `True` if the object is a method descriptor, but not if [`isclass()`](https://docs.python.org/3/library/inspect.html#inspect.isclass "inspect.isclass")
, [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod")
 or [`isfunction()`](https://docs.python.org/3/library/inspect.html#inspect.isfunction "inspect.isfunction")
 is true.

This, for example, is true of `int.__add__`. An object passing this test has a [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method, but not a [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 method or a [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
 method. Beyond that, the set of attributes varies. A [`__name__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")
 attribute is usually sensible, and [`__doc__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__doc__ "definition.__doc__")
 often is.

Method descriptors that also pass any of the other tests (`isclass()`, `ismethod()` or `isfunction()`) make this function return `False`, simply because those other tests promise more – you can, for example, count on having the [`__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")
 attribute when an object passes [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod")
.

Changed in version 3.13: This function no longer incorrectly reports objects with [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 and [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
, but not [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
, as being method descriptors (such objects are data descriptors, not method descriptors).

inspect.isdatadescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isdatadescriptor "Link to this definition")

Return `True` if the object is a data descriptor, but not if [`isclass()`](https://docs.python.org/3/library/inspect.html#inspect.isclass "inspect.isclass")
, [`ismethod()`](https://docs.python.org/3/library/inspect.html#inspect.ismethod "inspect.ismethod")
 or [`isfunction()`](https://docs.python.org/3/library/inspect.html#inspect.isfunction "inspect.isfunction")
 is true.

Data descriptors always have a [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 method and/or a [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
 method. Optionally, they may also have a [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method.

Examples of data descriptors are [`properties`](https://docs.python.org/3/builtins/functions.html#property "property")
, getsets and member descriptors. Note that for the latter two (defined only in C extension modules), more specific tests are available: [`isgetsetdescriptor()`](https://docs.python.org/3/library/inspect.html#inspect.isgetsetdescriptor "inspect.isgetsetdescriptor")
 and [`ismemberdescriptor()`](https://docs.python.org/3/library/inspect.html#inspect.ismemberdescriptor "inspect.ismemberdescriptor")
, respectively.

While data descriptors may also have [`__name__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")
 and `__doc__` attributes (as properties, getsets and member descriptors do), this is not necessarily the case in general.

Changed in version 3.8: This function now reports objects with only a [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 method as being data descriptors (the presence of [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 is no longer required for that). Moreover, objects with [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
, but not `__set__()`, are now properly recognized as data descriptors as well, which was not the case previously.

inspect.isgetsetdescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.isgetsetdescriptor "Link to this definition")

Return `True` if the object is a getset descriptor.

**CPython implementation detail:** getsets are attributes defined in extension modules via [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structures. For Python implementations without such types, this method will always return `False`.

inspect.ismemberdescriptor(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.ismemberdescriptor "Link to this definition")

Return `True` if the object is a member descriptor.

**CPython implementation detail:** Member descriptors are attributes defined in extension modules via [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 structures. For Python implementations without such types, this method will always return `False`.

Retrieving source code[¶](https://docs.python.org/3/library/inspect.html#retrieving-source-code "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

inspect.getdoc(_object_, _\*_, _inherit\_class\_doc\=True_, _fallback\_to\_class\_doc\=True_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getdoc "Link to this definition")

Get the documentation string for an object, cleaned up with [`cleandoc()`](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "inspect.cleandoc")
. If the documentation string for an object is not provided:

*   if the object is a class and _inherit\_class\_doc_ is true (by default), retrieve the documentation string from the inheritance hierarchy;
    
*   if the object is a method, a property or a descriptor, retrieve the documentation string from the inheritance hierarchy;
    
*   otherwise, if _fallback\_to\_class\_doc_ is true (by default), retrieve the documentation string from the class of the object.
    

Return `None` if the documentation string is invalid or missing.

Changed in version 3.5: Documentation strings are now inherited if not overridden.

Changed in version 3.15: Added parameters _inherit\_class\_doc_ and _fallback\_to\_class\_doc_.

Documentation strings on [`cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property "functools.cached_property")
 objects are now inherited if not overridden.

inspect.getcomments(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcomments "Link to this definition")

Return in a single string any lines of comments immediately preceding the object’s source code (for a class, function, or method), or at the top of the Python source file (if the object is a module). If the object’s source code is unavailable, return `None`. This could happen if the object has been defined in C or the interactive shell.

inspect.getfile(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getfile "Link to this definition")

Return the name of the (text or binary) file in which an object was defined. An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised if the source code cannot be retrieved. This will fail with a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the object is a built-in module, class, or function.

inspect.getmodule(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getmodule "Link to this definition")

Try to guess which module an object was defined in. Return `None` if the module cannot be determined.

inspect.getsourcefile(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getsourcefile "Link to this definition")

Return the name of the Python source file in which an object was defined or `None` if no way can be identified to get the source. An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised if the source code cannot be retrieved. This will fail with a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the object is a built-in module, class, or function.

inspect.getsourcelines(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getsourcelines "Link to this definition")

Return a list of source lines and starting line number for an object. The argument may be a module, class, method, function, traceback, frame, or code object. The source code is returned as a list of the lines corresponding to the object and the line number indicates where in the original source file the first line of code was found. An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised if the source code cannot be retrieved. A [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if the object is a built-in module, class, or function.

Changed in version 3.3: [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised instead of [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
, now an alias of the former.

inspect.getsource(_object_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getsource "Link to this definition")

Return the text of the source code for an object. The argument may be a module, class, method, function, traceback, frame, or code object. The source code is returned as a single string. An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised if the source code cannot be retrieved. A [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if the object is a built-in module, class, or function.

Changed in version 3.3: [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised instead of [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
, now an alias of the former.

inspect.cleandoc(_doc_)[¶](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "Link to this definition")

Clean up indentation from docstrings that are indented to line up with blocks of code.

All leading whitespace is removed from the first line. Any leading whitespace that can be uniformly removed from the second line onwards is removed. Empty lines at the beginning and end are subsequently removed. Also, all tabs are expanded to spaces.

Introspecting callables with the Signature object[¶](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Added in version 3.3.

The [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
 object represents the call signature of a callable object and its return annotation. To retrieve a `Signature` object, use the `signature()` function.

inspect.signature(_callable_, _\*_, _follow\_wrapped\=True_, _globals\=None_, _locals\=None_, _eval\_str\=False_, _annotation\_format\=Format.VALUE_)[¶](https://docs.python.org/3/library/inspect.html#inspect.signature "Link to this definition")

Return a [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
 object for the given _callable_:

Copy

\>>> from inspect import signature
\>>> def foo(a, \*, b:int, \*\*kwargs):
...     pass

\>>> sig \= signature(foo)

\>>> str(sig)
'(a, \*, b: int, \*\*kwargs)'

\>>> str(sig.parameters\['b'\])
'b: int'

\>>> sig.parameters\['b'\].annotation
<class 'int'>

Accepts a wide range of Python callables, from plain functions and classes to [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 objects.

If some of the annotations are strings (e.g., because `from __future__ import annotations` was used), `signature()` will attempt to automatically un-stringize the annotations using [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
. The _globals_, _locals_, and _eval\_str_ parameters are passed into `annotationlib.get_annotations()` when resolving the annotations; see the documentation for `annotationlib.get_annotations()` for instructions on how to use these parameters. A member of the [`annotationlib.Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format")
 enum can be passed to the _annotation\_format_ parameter to control the format of the returned annotations. For example, use `annotation_format=annotationlib.Format.STRING` to return annotations in string format.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if no signature can be provided, and [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if that type of object is not supported. Also, if the annotations are stringized, and _eval\_str_ is not false, the `eval()` call(s) to un-stringize the annotations in [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
 could potentially raise any kind of exception.

A slash (/) in the signature of a function denotes that the parameters prior to it are positional-only. For more info, see [the FAQ entry on positional-only parameters](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments)
.

Changed in version 3.5: The _follow\_wrapped_ parameter was added. Pass `False` to get a signature of _callable_ specifically (`callable.__wrapped__` will not be used to unwrap decorated callables.)

Changed in version 3.10: The _globals_, _locals_, and _eval\_str_ parameters were added.

Changed in version 3.14: The _annotation\_format_ parameter was added.

Note

Some callables may not be introspectable in certain implementations of Python. For example, in CPython, some built-in functions defined in C provide no metadata about their arguments.

**CPython implementation detail:** If the passed object has a `__signature__` attribute, we may use it to create the signature. The exact semantics are an implementation detail and are subject to unannounced changes. Consult the source code for current semantics.

class inspect.Signature(_parameters\=None_, _\*_, _return\_annotation\=Signature.empty_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature "Link to this definition")

A `Signature` object represents the call signature of a function and its return annotation. For each parameter accepted by the function it stores a [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter")
 object in its [`parameters`](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "inspect.Signature.parameters")
 collection.

The optional _parameters_ argument is a sequence of [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter")
 objects, which is validated to check that there are no parameters with duplicate names, and that the parameters are in the right order, i.e. positional-only first, then positional-or-keyword, and that parameters with defaults follow parameters without defaults.

The optional _return\_annotation_ argument can be an arbitrary Python object. It represents the “return” annotation of the callable.

`Signature` objects are _immutable_. Use [`Signature.replace()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.replace "inspect.Signature.replace")
 or [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
 to make a modified copy.

Changed in version 3.5: `Signature` objects are now picklable and [hashable](https://docs.python.org/3/glossary.html#term-hashable)
.

empty[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "Link to this definition")

A special class-level marker to specify absence of a return annotation.

parameters[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "Link to this definition")

An ordered mapping of parameters’ names to the corresponding [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter")
 objects. Parameters appear in strict definition order, including keyword-only parameters.

Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3.

return\_annotation[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.return_annotation "Link to this definition")

The “return” annotation for the callable. If the callable has no “return” annotation, this attribute is set to [`Signature.empty`](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "inspect.Signature.empty")
.

bind(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "Link to this definition")

Create a mapping from positional and keyword arguments to parameters. Returns [`BoundArguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "inspect.BoundArguments")
 if `*args` and `**kwargs` match the signature, or raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

bind\_partial(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "Link to this definition")

Works the same way as [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind")
, but allows the omission of some required arguments (mimics [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 behavior.) Returns [`BoundArguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "inspect.BoundArguments")
, or raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the passed arguments do not match the signature.

replace(_\*\[, parameters\]\[, return\_annotation\]_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.replace "Link to this definition")

Create a new `Signature` instance based on the instance `replace()` was invoked on. It is possible to pass different _parameters_ and/or _return\_annotation_ to override the corresponding properties of the base signature. To remove `return_annotation` from the copied `Signature`, pass in [`Signature.empty`](https://docs.python.org/3/library/inspect.html#inspect.Signature.empty "inspect.Signature.empty")
.

Copy

\>>> def test(a, b):
...     pass
...
\>>> sig \= signature(test)
\>>> new\_sig \= sig.replace(return\_annotation\="new return anno")
\>>> str(new\_sig)
"(a, b) -> 'new return anno'"

`Signature` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
.

format(_\*_, _max\_width\=None_, _quote\_annotation\_strings\=True_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.format "Link to this definition")

Create a string representation of the `Signature` object.

If _max\_width_ is passed, the method will attempt to fit the signature into lines of at most _max\_width_ characters. If the signature is longer than _max\_width_, all parameters will be on separate lines.

If _quote\_annotation\_strings_ is False, [annotations](https://docs.python.org/3/glossary.html#term-annotation)
 in the signature are displayed without opening and closing quotation marks if they are strings. This is useful if the signature was created with the [`STRING`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format.STRING "annotationlib.Format.STRING")
 format or if `from __future__ import annotations` was used.

Added in version 3.13.

Changed in version 3.14: The _unquote\_annotations_ parameter was added.

classmethod from\_callable(_obj_, _\*_, _follow\_wrapped\=True_, _globals\=None_, _locals\=None_, _eval\_str\=False_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "Link to this definition")

Return a `Signature` (or its subclass) object for a given callable _obj_.

This method simplifies subclassing of `Signature`:

Copy

class MySignature(Signature):
    pass
sig \= MySignature.from\_callable(sum)
assert isinstance(sig, MySignature)

Its behavior is otherwise identical to that of [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
.

Added in version 3.5.

Changed in version 3.10: The _globals_, _locals_, and _eval\_str_ parameters were added.

class inspect.Parameter(_name_, _kind_, _\*_, _default\=Parameter.empty_, _annotation\=Parameter.empty_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter "Link to this definition")

`Parameter` objects are _immutable_. Instead of modifying a `Parameter` object, you can use [`Parameter.replace()`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.replace "inspect.Parameter.replace")
 or [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
 to create a modified copy.

Changed in version 3.5: Parameter objects are now picklable and [hashable](https://docs.python.org/3/glossary.html#term-hashable)
.

empty[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "Link to this definition")

A special class-level marker to specify absence of default values and annotations.

name[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.name "Link to this definition")

The name of the parameter as a string. The name must be a valid Python identifier.

**CPython implementation detail:** CPython generates implicit parameter names of the form `.0` on the code objects used to implement comprehensions and generator expressions.

Changed in version 3.6: These parameter names are now exposed by this module as names like `implicit0`.

default[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.default "Link to this definition")

The default value for the parameter. If the parameter has no default value, this attribute is set to [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty")
.

annotation[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.annotation "Link to this definition")

The annotation for the parameter. If the parameter has no annotation, this attribute is set to [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty")
.

kind[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind "Link to this definition")

Describes how argument values are bound to the parameter. The possible values are accessible via `Parameter` (like `Parameter.KEYWORD_ONLY`), and support comparison and ordering, in the following order:

| Name | Meaning |
| --- | --- |
| _POSITIONAL\_ONLY_ | Value must be supplied as a positional argument. Positional only parameters are those which appear before a `/` entry (if present) in a Python function definition. |
| _POSITIONAL\_OR\_KEYWORD_ | Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.) |
| _VAR\_POSITIONAL_ | A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a `*args` parameter in a Python function definition. |
| _KEYWORD\_ONLY_ | Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a `*` or `*args` entry in a Python function definition. |
| _VAR\_KEYWORD_ | A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a `**kwargs` parameter in a Python function definition. |

Example: print all keyword-only arguments without default values:

Copy

\>>> def foo(a, b, \*, c, d\=10):
...     pass

\>>> sig \= signature(foo)
\>>> for param in sig.parameters.values():
...     if (param.kind \== param.KEYWORD\_ONLY and
...                        param.default is param.empty):
...         print('Parameter:', param)
Parameter: c

kind.description[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind.description "Link to this definition")

Describes an enum value of [`Parameter.kind`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind "inspect.Parameter.kind")
.

Added in version 3.8.

Example: print all descriptions of arguments:

Copy

\>>> def foo(a, b, \*, c, d\=10):
...     pass

\>>> sig \= signature(foo)
\>>> for param in sig.parameters.values():
...     print(param.kind.description)
positional or keyword
positional or keyword
keyword-only
keyword-only

replace(_\*\[, name\]\[, kind\]\[, default\]\[, annotation\]_)[¶](https://docs.python.org/3/library/inspect.html#inspect.Parameter.replace "Link to this definition")

Create a new `Parameter` instance based on the instance replaced was invoked on. To override a `Parameter` attribute, pass the corresponding argument. To remove a default value or/and an annotation from a `Parameter`, pass [`Parameter.empty`](https://docs.python.org/3/library/inspect.html#inspect.Parameter.empty "inspect.Parameter.empty")
.

Copy

\>>> from inspect import Parameter
\>>> param \= Parameter('foo', Parameter.KEYWORD\_ONLY, default\=42)
\>>> str(param)
'foo=42'

\>>> str(param.replace()) \# Will create a shallow copy of 'param'
'foo=42'

\>>> str(param.replace(default\=Parameter.empty, annotation\='spam'))
"foo: 'spam'"

`Parameter` objects are also supported by the generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
.

Changed in version 3.4: In Python 3.3 `Parameter` objects were allowed to have `name` set to `None` if their `kind` was set to `POSITIONAL_ONLY`. This is no longer permitted.

class inspect.BoundArguments[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "Link to this definition")

Result of a [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind")
 or [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial")
 call. Holds the mapping of arguments to the function’s parameters.

arguments[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "Link to this definition")

A mutable mapping of parameters’ names to arguments’ values. Contains only explicitly bound arguments. Changes in [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments")
 will reflect in [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args")
 and [`kwargs`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "inspect.BoundArguments.kwargs")
.

Should be used in conjunction with [`Signature.parameters`](https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters "inspect.Signature.parameters")
 for any argument processing purposes.

Note

Arguments for which [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind")
 or [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial")
 relied on a default value are skipped. However, if needed, use [`BoundArguments.apply_defaults()`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults "inspect.BoundArguments.apply_defaults")
 to add them.

Changed in version 3.9: [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments")
 is now of type [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
. Formerly, it was of type [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
.

args[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "Link to this definition")

A tuple of positional arguments values. Dynamically computed from the [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments")
 attribute.

kwargs[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "Link to this definition")

A dict of keyword arguments values. Dynamically computed from the [`arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments")
 attribute. Arguments that can be passed positionally are included in [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args")
 instead.

signature[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.signature "Link to this definition")

A reference to the parent [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
 object.

apply\_defaults()[¶](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults "Link to this definition")

Set default values for missing arguments.

For variable-positional arguments (`*args`) the default is an empty tuple.

For variable-keyword arguments (`**kwargs`) the default is an empty dict.

Copy

\>>> def foo(a, b\='ham', \*args): pass
\>>> ba \= inspect.signature(foo).bind('spam')
\>>> ba.apply\_defaults()
\>>> ba.arguments
{'a': 'spam', 'b': 'ham', 'args': ()}

Added in version 3.5.

The [`args`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.args "inspect.BoundArguments.args")
 and [`kwargs`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.kwargs "inspect.BoundArguments.kwargs")
 properties can be used to invoke functions:

Copy

def test(a, \*, b):
    ...

sig \= signature(test)
ba \= sig.bind(10, b\=20)
test(\*ba.args, \*\*ba.kwargs)

See also

[**PEP 362**](https://peps.python.org/pep-0362/)
 - Function Signature Object.

The detailed specification, implementation details and examples.

Classes and functions[¶](https://docs.python.org/3/library/inspect.html#classes-and-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

inspect.getclasstree(_classes_, _unique\=False_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getclasstree "Link to this definition")

Arrange the given list of classes into a hierarchy of nested lists. Where a nested list appears, it contains classes derived from the class whose entry immediately precedes the list. Each entry is a 2-tuple containing a class and a tuple of its base classes. If the _unique_ argument is true, exactly one entry appears in the returned structure for each class in the given list. Otherwise, classes using multiple inheritance and their descendants will appear multiple times.

inspect.getfullargspec(_func_, _\*_, _annotation\_format\=Format.VALUE_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "Link to this definition")

Get the names and default values of a Python function’s parameters. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 is returned:

`FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)`

_args_ is a list of the positional parameter names. _varargs_ is the name of the `*` parameter or `None` if arbitrary positional arguments are not accepted. _varkw_ is the name of the `**` parameter or `None` if arbitrary keyword arguments are not accepted. _defaults_ is an _n_\-tuple of default argument values corresponding to the last _n_ positional parameters, or `None` if there are no such defaults defined. _kwonlyargs_ is a list of keyword-only parameter names in declaration order. _kwonlydefaults_ is a dictionary mapping parameter names from _kwonlyargs_ to the default values used if no argument is supplied. _annotations_ is a dictionary mapping parameter names to annotations. The special key `"return"` is used to report the function return value annotation (if any).

Note that [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 and [Signature Object](https://docs.python.org/3/library/inspect.html#inspect-signature-object)
 provide the recommended API for callable introspection, and support additional behaviours (like positional-only arguments) that are sometimes encountered in extension module APIs. This function is retained primarily for use in code that needs to maintain compatibility with the Python 2 `inspect` module API.

A member of the [`annotationlib.Format`](https://docs.python.org/3/library/annotationlib.html#annotationlib.Format "annotationlib.Format")
 enum can be passed to the _annotation\_format_ parameter to control the format of the returned annotations. For example, use `annotation_format=annotationlib.Format.STRING` to return annotations in string format. Note that with the default `VALUE` format, creation of some argspecs may raise an exception.

Changed in version 3.4: This function is now based on [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
, but still ignores `__wrapped__` attributes and includes the already bound first parameter in the signature output for bound methods.

Changed in version 3.6: This method was previously documented as deprecated in favour of [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 in Python 3.5, but that decision has been reversed in order to restore a clearly supported standard interface for single-source Python 2/3 code migrating away from the legacy `getargspec()` API.

Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3.

Changed in version 3.15: The _annotation\_format_ parameter was added.

inspect.getargvalues(_frame_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getargvalues "Link to this definition")

Get information about arguments passed into a particular frame. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 `ArgInfo(args, varargs, keywords, locals)` is returned. _args_ is a list of the argument names. _varargs_ and _keywords_ are the names of the `*` and `**` arguments or `None`. _locals_ is the locals dictionary of the given frame.

Note

This function was inadvertently marked as deprecated in Python 3.5.

inspect.formatargvalues(_args_\[, _varargs_, _varkw_, _locals_, _formatarg_, _formatvarargs_, _formatvarkw_, _formatvalue_\])[¶](https://docs.python.org/3/library/inspect.html#inspect.formatargvalues "Link to this definition")

Format a pretty argument spec from the four values returned by [`getargvalues()`](https://docs.python.org/3/library/inspect.html#inspect.getargvalues "inspect.getargvalues")
. The format\* arguments are the corresponding optional formatting functions that are called to turn names and values into strings.

Note

This function was inadvertently marked as deprecated in Python 3.5.

inspect.getmro(_cls_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getmro "Link to this definition")

Return a tuple of class cls’s base classes, including cls, in method resolution order. No class appears more than once in this tuple. Note that the method resolution order depends on cls’s type. Unless a very peculiar user-defined metatype is in use, cls will be the first element of the tuple.

inspect.getcallargs(_func_, _/_, _\*args_, _\*\*kwds_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcallargs "Link to this definition")

Bind the _args_ and _kwds_ to the argument names of the Python function or method _func_, as if it was called with them. For bound methods, bind also the first argument (typically named `self`) to the associated instance. A dict is returned, mapping the argument names (including the names of the `*` and `**` arguments, if any) to their values from _args_ and _kwds_. In case of invoking _func_ incorrectly, i.e. whenever `func(*args, **kwds)` would raise an exception because of incompatible signature, an exception of the same type and the same or similar message is raised. For example:

Copy

\>>> from inspect import getcallargs
\>>> def f(a, b\=1, \*pos, \*\*named):
...     pass
...
\>>> getcallargs(f, 1, 2, 3) \== {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
True
\>>> getcallargs(f, a\=2, x\=4) \== {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
True
\>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() missing 1 required positional argument: 'a'

Added in version 3.2.

Deprecated since version 3.5: Use [`Signature.bind()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind "inspect.Signature.bind")
 and [`Signature.bind_partial()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind_partial "inspect.Signature.bind_partial")
 instead.

inspect.getclosurevars(_func_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getclosurevars "Link to this definition")

Get the mapping of external name references in a Python function or method _func_ to their current values. A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 `ClosureVars(nonlocals, globals, builtins, unbound)` is returned. _nonlocals_ maps referenced names to lexical closure variables, _globals_ to the function’s module globals and _builtins_ to the builtins visible from the function body. _unbound_ is the set of names referenced in the function that could not be resolved at all given the current module globals and builtins.

[`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if _func_ is not a Python function or method.

Added in version 3.3.

inspect.unwrap(_func_, _\*_, _stop\=None_)[¶](https://docs.python.org/3/library/inspect.html#inspect.unwrap "Link to this definition")

Get the object wrapped by _func_. It follows the chain of `__wrapped__` attributes returning the last object in the chain.

_stop_ is an optional callback accepting an object in the wrapper chain as its sole argument that allows the unwrapping to be terminated early if the callback returns a true value. If the callback never returns a true value, the last object in the chain is returned as usual. For example, [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 uses this to stop unwrapping if any object in the chain has a `__signature__` attribute defined.

[`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if a cycle is encountered.

Added in version 3.4.

inspect.get\_annotations(_obj_, _\*_, _globals\=None_, _locals\=None_, _eval\_str\=False_, _format\=annotationlib.Format.VALUE_)[¶](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "Link to this definition")

Compute the annotations dict for an object.

This is an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
; see the documentation of that function for more information.

Caution

This function may execute arbitrary code contained in annotations. See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security)
 for more information.

Added in version 3.10.

Changed in version 3.14: This function is now an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
. Calling it as `inspect.get_annotations` will continue to work.

The interpreter stack[¶](https://docs.python.org/3/library/inspect.html#the-interpreter-stack "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Some of the following functions return [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects. For backwards compatibility these objects allow tuple-like operations on all attributes except `positions`. This behavior is considered deprecated and may be removed in the future.

class inspect.FrameInfo[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "Link to this definition")

frame[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.frame "Link to this definition")

The [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects)
 that the record corresponds to.

filename[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.filename "Link to this definition")

The file name associated with the code being executed by the frame this record corresponds to.

lineno[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.lineno "Link to this definition")

The line number of the current line associated with the code being executed by the frame this record corresponds to.

function[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.function "Link to this definition")

The function name that is being executed by the frame this record corresponds to.

code\_context[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.code_context "Link to this definition")

A list of lines of context from the source code that’s being executed by the frame this record corresponds to.

index[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.index "Link to this definition")

The index of the current line being executed in the [`code_context`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.code_context "inspect.FrameInfo.code_context")
 list.

positions[¶](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo.positions "Link to this definition")

A [`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions")
 object containing the start line number, end line number, start column offset, and end column offset associated with the instruction being executed by the frame this record corresponds to.

Changed in version 3.5: Return a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 instead of a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
.

Changed in version 3.11: `FrameInfo` is now a class instance (that is backwards compatible with the previous [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
).

class inspect.Traceback[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback "Link to this definition")

filename[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.filename "Link to this definition")

The file name associated with the code being executed by the frame this traceback corresponds to.

lineno[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.lineno "Link to this definition")

The line number of the current line associated with the code being executed by the frame this traceback corresponds to.

function[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.function "Link to this definition")

The function name that is being executed by the frame this traceback corresponds to.

code\_context[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.code_context "Link to this definition")

A list of lines of context from the source code that’s being executed by the frame this traceback corresponds to.

index[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.index "Link to this definition")

The index of the current line being executed in the [`code_context`](https://docs.python.org/3/library/inspect.html#inspect.Traceback.code_context "inspect.Traceback.code_context")
 list.

positions[¶](https://docs.python.org/3/library/inspect.html#inspect.Traceback.positions "Link to this definition")

A [`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions")
 object containing the start line number, end line number, start column offset, and end column offset associated with the instruction being executed by the frame this traceback corresponds to.

Changed in version 3.11: `Traceback` is now a class instance (that is backwards compatible with the previous [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
).

Note

Keeping references to frame objects, as found in the first element of the frame records these functions return, can cause your program to create reference cycles. Once a reference cycle has been created, the lifespan of all objects which can be accessed from the objects which form the cycle can become much longer even if Python’s optional cycle detector is enabled. If such cycles must be created, it is important to ensure they are explicitly broken to avoid the delayed destruction of objects and increased memory consumption which occurs.

Though the cycle detector will catch these, destruction of the frames (and local variables) can be made deterministic by removing the cycle in a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clause. This is also important if the cycle detector was disabled when Python was compiled or using [`gc.disable()`](https://docs.python.org/3/library/gc.html#gc.disable "gc.disable")
. For example:

Copy

def handle\_stackframe\_without\_leak():
    frame \= inspect.currentframe()
    try:
        \# do something with the frame
    finally:
        del frame

If you want to keep the frame around (for example to print a traceback later), you can also break reference cycles by using the [`frame.clear()`](https://docs.python.org/3/reference/datamodel.html#frame.clear "frame.clear")
 method.

The optional _context_ argument supported by most of these functions specifies the number of lines of context to return, which are centered around the current line.

inspect.getframeinfo(_frame_, _context\=1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getframeinfo "Link to this definition")

Get information about a frame or traceback object. A [`Traceback`](https://docs.python.org/3/library/inspect.html#inspect.Traceback "inspect.Traceback")
 object is returned.

Changed in version 3.11: A [`Traceback`](https://docs.python.org/3/library/inspect.html#inspect.Traceback "inspect.Traceback")
 object is returned instead of a named tuple.

inspect.getouterframes(_frame_, _context\=1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getouterframes "Link to this definition")

Get a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects for a frame and all outer frames. These frames represent the calls that lead to the creation of _frame_. The first entry in the returned list represents _frame_; the last entry represents the outermost call on _frame_’s stack.

Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple)
 `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.

Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects is returned.

inspect.getinnerframes(_traceback_, _context\=1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getinnerframes "Link to this definition")

Get a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects for a traceback’s frame and all inner frames. These frames represent calls made as a consequence of _frame_. The first entry in the list represents _traceback_; the last entry represents where the exception was raised.

Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple)
 `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.

Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects is returned.

inspect.currentframe()[¶](https://docs.python.org/3/library/inspect.html#inspect.currentframe "Link to this definition")

Return the frame object for the caller’s stack frame.

**CPython implementation detail:** This function relies on Python stack frame support in the interpreter, which isn’t guaranteed to exist in all implementations of Python. If running in an implementation without Python stack frame support this function returns `None`.

inspect.stack(_context\=1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.stack "Link to this definition")

Return a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects for the caller’s stack. The first entry in the returned list represents the caller; the last entry represents the outermost call on the stack.

Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple)
 `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.

Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects is returned.

inspect.trace(_context\=1_)[¶](https://docs.python.org/3/library/inspect.html#inspect.trace "Link to this definition")

Return a list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects for the stack between the current frame and the frame in which an exception currently being handled was raised in. The first entry in the list represents the caller; the last entry represents where the exception was raised.

Changed in version 3.5: A list of [named tuples](https://docs.python.org/3/glossary.html#term-named-tuple)
 `FrameInfo(frame, filename, lineno, function, code_context, index)` is returned.

Changed in version 3.11: A list of [`FrameInfo`](https://docs.python.org/3/library/inspect.html#inspect.FrameInfo "inspect.FrameInfo")
 objects is returned.

Fetching attributes statically[¶](https://docs.python.org/3/library/inspect.html#fetching-attributes-statically "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Both [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 and [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 can trigger code execution when fetching or checking for the existence of attributes. Descriptors, like properties, will be invoked and [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 and [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 may be called.

For cases where you want passive introspection, like documentation tools, this can be inconvenient. [`getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static")
 has a similar signature as [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 but avoids executing code when it fetches attributes.

inspect.getattr\_static(_obj_, _attr_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "Link to this definition")

inspect.getattr\_static(_obj_, _attr_, _default_)

Retrieve attributes without triggering dynamic lookup via the descriptor protocol, [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 or [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
.

Note: this function may not be able to retrieve all attributes that getattr can fetch (like dynamically created attributes) and may find attributes that getattr can’t (like descriptors that raise AttributeError). It can also return descriptors objects instead of instance members.

If the instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 is shadowed by another member (for example a property) then this function will be unable to find instance members.

Added in version 3.2.

[`getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static")
 does not resolve descriptors, for example slot descriptors or getset descriptors on objects implemented in C. The descriptor object is returned instead of the underlying attribute.

You can handle these with code like the following. Note that for arbitrary getset descriptors invoking these may trigger code execution:

Copy

\# example code for resolving the builtin descriptor types
class \_foo:
    \_\_slots\_\_ \= \['foo'\]

slot\_descriptor \= type(\_foo.foo)
getset\_descriptor \= type(type(open(\_\_file\_\_)).name)
wrapper\_descriptor \= type(str.\_\_dict\_\_\['\_\_add\_\_'\])
descriptor\_types \= (slot\_descriptor, getset\_descriptor, wrapper\_descriptor)

result \= getattr\_static(some\_object, 'foo')
if type(result) in descriptor\_types:
    try:
        result \= result.\_\_get\_\_()
    except AttributeError:
        \# descriptors can raise AttributeError to
        \# indicate there is no underlying value
        \# in which case the descriptor itself will
        \# have to do
        pass

Current State of Generators, Coroutines, and Asynchronous Generators[¶](https://docs.python.org/3/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When implementing coroutine schedulers and for other advanced uses of generators, it is useful to determine whether a generator is currently executing, is waiting to start or resume or execution, or has already terminated. [`getgeneratorstate()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorstate "inspect.getgeneratorstate")
 allows the current state of a generator to be determined easily.

inspect.getgeneratorstate(_generator_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorstate "Link to this definition")

Get current state of a generator-iterator.

Possible states are:

*   GEN\_CREATED: Waiting to start execution.
    
*   GEN\_RUNNING: Currently being executed by the interpreter.
    
*   GEN\_SUSPENDED: Currently suspended at a yield expression.
    
*   GEN\_CLOSED: Execution has completed.
    

Added in version 3.2.

inspect.getcoroutinestate(_coroutine_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinestate "Link to this definition")

Get current state of a coroutine object. The function is intended to be used with coroutine objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions, but will accept any coroutine-like object that has `cr_running` and `cr_frame` attributes.

Possible states are:

*   CORO\_CREATED: Waiting to start execution.
    
*   CORO\_RUNNING: Currently being executed by the interpreter.
    
*   CORO\_SUSPENDED: Currently suspended at an await expression.
    
*   CORO\_CLOSED: Execution has completed.
    

Added in version 3.5.

inspect.getasyncgenstate(_agen_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getasyncgenstate "Link to this definition")

Get current state of an asynchronous generator object. The function is intended to be used with asynchronous iterator objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions which use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 statement, but will accept any asynchronous generator-like object that has `ag_running` and `ag_frame` attributes.

Possible states are:

*   AGEN\_CREATED: Waiting to start execution.
    
*   AGEN\_RUNNING: Currently being executed by the interpreter.
    
*   AGEN\_SUSPENDED: Currently suspended at a yield expression.
    
*   AGEN\_CLOSED: Execution has completed.
    

Added in version 3.12.

The current internal state of the generator can also be queried. This is mostly useful for testing purposes, to ensure that internal state is being updated as expected:

inspect.getgeneratorlocals(_generator_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "Link to this definition")

Get the mapping of live local variables in _generator_ to their current values. A dictionary is returned that maps from variable names to values. This is the equivalent of calling [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 in the body of the generator, and all the same caveats apply.

If _generator_ is a [generator](https://docs.python.org/3/glossary.html#term-generator)
 with no currently associated frame, then an empty dictionary is returned. [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if _generator_ is not a Python generator object.

**CPython implementation detail:** This function relies on the generator exposing a Python stack frame for introspection, which isn’t guaranteed to be the case in all implementations of Python. In such cases, this function will always return an empty dictionary.

Added in version 3.3.

inspect.getcoroutinelocals(_coroutine_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinelocals "Link to this definition")

This function is analogous to [`getgeneratorlocals()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "inspect.getgeneratorlocals")
, but works for coroutine objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions.

Added in version 3.5.

inspect.getasyncgenlocals(_agen_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getasyncgenlocals "Link to this definition")

This function is analogous to [`getgeneratorlocals()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "inspect.getgeneratorlocals")
, but works for asynchronous generator objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions which use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 statement.

Added in version 3.12.

Code Objects Bit Flags[¶](https://docs.python.org/3/library/inspect.html#code-objects-bit-flags "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Python code objects have a [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
 attribute, which is a bitmap of the following flags:

inspect.CO\_OPTIMIZED[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_OPTIMIZED "Link to this definition")

The code object is optimized, using fast locals.

inspect.CO\_NEWLOCALS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_NEWLOCALS "Link to this definition")

If set, a new dict will be created for the frame’s [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 when the code object is executed.

inspect.CO\_VARARGS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_VARARGS "Link to this definition")

The code object has a variable positional parameter (`*args`\-like).

inspect.CO\_VARKEYWORDS[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_VARKEYWORDS "Link to this definition")

The code object has a variable keyword parameter (`**kwargs`\-like).

inspect.CO\_NESTED[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_NESTED "Link to this definition")

The flag is set when the code object is a nested function.

inspect.CO\_GENERATOR[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_GENERATOR "Link to this definition")

The flag is set when the code object is a generator function, i.e. a generator object is returned when the code object is executed.

inspect.CO\_COROUTINE[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_COROUTINE "Link to this definition")

The flag is set when the code object is a coroutine function. When the code object is executed it returns a coroutine object. See [**PEP 492**](https://peps.python.org/pep-0492/)
 for more details.

Added in version 3.5.

inspect.CO\_ITERABLE\_COROUTINE[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_ITERABLE_COROUTINE "Link to this definition")

The flag is used to transform generators into generator-based coroutines. Generator objects with this flag can be used in `await` expression, and can `yield from` coroutine objects. See [**PEP 492**](https://peps.python.org/pep-0492/)
 for more details.

Added in version 3.5.

inspect.CO\_ASYNC\_GENERATOR[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_ASYNC_GENERATOR "Link to this definition")

The flag is set when the code object is an asynchronous generator function. When the code object is executed it returns an asynchronous generator object. See [**PEP 525**](https://peps.python.org/pep-0525/)
 for more details.

Added in version 3.6.

inspect.CO\_HAS\_DOCSTRING[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_HAS_DOCSTRING "Link to this definition")

The flag is set when there is a docstring for the code object in the source code. If set, it will be the first item in [`co_consts`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_consts "codeobject.co_consts")
.

Added in version 3.14.

inspect.CO\_METHOD[¶](https://docs.python.org/3/library/inspect.html#inspect.CO_METHOD "Link to this definition")

The flag is set when the code object is a function defined in class scope.

Added in version 3.14.

Note

The flags are specific to CPython, and may not be defined in other Python implementations. Furthermore, the flags are an implementation detail, and can be removed or deprecated in future Python releases. It’s recommended to use public APIs from the `inspect` module for any introspection needs.

Buffer flags[¶](https://docs.python.org/3/library/inspect.html#buffer-flags "Link to this heading")

----------------------------------------------------------------------------------------------------

class inspect.BufferFlags[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags "Link to this definition")

This is an [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
 that represents the flags that can be passed to the [`__buffer__()`](https://docs.python.org/3/reference/datamodel.html#object.__buffer__ "object.__buffer__")
 method of objects implementing the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
.

The meaning of the flags is explained at [Buffer request types](https://docs.python.org/3/c-api/buffer.html#buffer-request-types)
.

SIMPLE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.SIMPLE "Link to this definition")

WRITABLE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.WRITABLE "Link to this definition")

FORMAT[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FORMAT "Link to this definition")

ND[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.ND "Link to this definition")

STRIDES[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDES "Link to this definition")

C\_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.C_CONTIGUOUS "Link to this definition")

F\_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.F_CONTIGUOUS "Link to this definition")

ANY\_CONTIGUOUS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.ANY_CONTIGUOUS "Link to this definition")

INDIRECT[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.INDIRECT "Link to this definition")

CONTIG[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.CONTIG "Link to this definition")

CONTIG\_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.CONTIG_RO "Link to this definition")

STRIDED[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDED "Link to this definition")

STRIDED\_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.STRIDED_RO "Link to this definition")

RECORDS[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.RECORDS "Link to this definition")

RECORDS\_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.RECORDS_RO "Link to this definition")

FULL[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FULL "Link to this definition")

FULL\_RO[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.FULL_RO "Link to this definition")

READ[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.READ "Link to this definition")

WRITE[¶](https://docs.python.org/3/library/inspect.html#inspect.BufferFlags.WRITE "Link to this definition")

Added in version 3.12.

Command-line interface[¶](https://docs.python.org/3/library/inspect.html#command-line-interface "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The `inspect` module also provides a basic introspection capability from the command line.

By default, accepts the name of a module and prints the source of that module. A class or function within the module can be printed instead by appending a colon and the qualified name of the target object.

\--details[¶](https://docs.python.org/3/library/inspect.html#cmdoption-inspect-details "Link to this definition")

Print information about the specified object rather than the source code

Changed in version 3.15: The `--details` option now supports basic introspection for modules without available source code and indicates when modules are frozen. It also indicates when the given target reference is not the canonical name of the referenced object.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html#)
    *   [Types and members](https://docs.python.org/3/library/inspect.html#types-and-members)
        
    *   [Retrieving source code](https://docs.python.org/3/library/inspect.html#retrieving-source-code)
        
    *   [Introspecting callables with the Signature object](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object)
        
    *   [Classes and functions](https://docs.python.org/3/library/inspect.html#classes-and-functions)
        
    *   [The interpreter stack](https://docs.python.org/3/library/inspect.html#the-interpreter-stack)
        
    *   [Fetching attributes statically](https://docs.python.org/3/library/inspect.html#fetching-attributes-statically)
        
    *   [Current State of Generators, Coroutines, and Asynchronous Generators](https://docs.python.org/3/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators)
        
    *   [Code Objects Bit Flags](https://docs.python.org/3/library/inspect.html#code-objects-bit-flags)
        
    *   [Buffer flags](https://docs.python.org/3/library/inspect.html#buffer-flags)
        
    *   [Command-line interface](https://docs.python.org/3/library/inspect.html#command-line-interface)
        

#### Previous topic

[`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html "previous chapter")

#### Next topic

[`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=inspect+%E2%80%94+Inspect+live+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Finspect.html&pagesource=library%2Finspect.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/inspect.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/annotationlib.html "annotationlib — Functionality for introspecting annotations")
     |
*   [previous](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
    
*    
    
    |
*   Theme Auto Light Dark |