### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/copy.html "copy — Shallow and deep copy operations")
     |
*   [previous](https://docs.python.org/3/library/weakref.html "weakref — Weak references")
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
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`types` — Dynamic type creation and names for built-in types[¶](https://docs.python.org/3/library/types.html#module-types "Link to this heading")

==================================================================================================================================================

**Source code:** [Lib/types.py](https://github.com/python/cpython/tree/3.15/Lib/types.py)

* * *

This module defines utility functions to assist in dynamic creation of new types.

It also defines names for some object types that are used by the standard Python interpreter, but not exposed as builtins like [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 or [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 are.

Finally, it provides some additional type-related utility classes and functions that are not fundamental enough to be builtins.

Dynamic Type Creation[¶](https://docs.python.org/3/library/types.html#dynamic-type-creation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

types.new\_class(_name_, _bases\=()_, _kwds\=None_, _exec\_body\=None_)[¶](https://docs.python.org/3/library/types.html#types.new_class "Link to this definition")

Creates a class object dynamically using the appropriate metaclass.

The first three arguments are the components that make up a class definition header: the class name, the base classes (in order), the keyword arguments (such as `metaclass`).

The _exec\_body_ argument is a callback that is used to populate the freshly created class namespace. It should accept the class namespace as its sole argument and update the namespace directly with the class contents. If no callback is provided, it has the same effect as passing in `lambda ns: None`.

Added in version 3.3.

types.prepare\_class(_name_, _bases\=()_, _kwds\=None_)[¶](https://docs.python.org/3/library/types.html#types.prepare_class "Link to this definition")

Calculates the appropriate metaclass and creates the class namespace.

The arguments are the components that make up a class definition header: the class name, the base classes (in order) and the keyword arguments (such as `metaclass`).

The return value is a 3-tuple: `metaclass, namespace, kwds`

_metaclass_ is the appropriate metaclass, _namespace_ is the prepared class namespace and _kwds_ is an updated copy of the passed in _kwds_ argument with any `'metaclass'` entry removed. If no _kwds_ argument is passed in, this will be an empty dict.

Added in version 3.3.

Changed in version 3.6: The default value for the `namespace` element of the returned tuple has changed. Now an insertion-order-preserving mapping is used when the metaclass does not have a `__prepare__` method.

See also

[Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)

Full details of the class creation process supported by these functions

[**PEP 3115**](https://peps.python.org/pep-3115/)
 - Metaclasses in Python 3000

Introduced the `__prepare__` namespace hook

types.resolve\_bases(_bases_)[¶](https://docs.python.org/3/library/types.html#types.resolve_bases "Link to this definition")

Resolve MRO entries dynamically as specified by [**PEP 560**](https://peps.python.org/pep-0560/)
.

This function looks for items in _bases_ that are not instances of [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
, and returns a tuple where each such object that has an [`__mro_entries__()`](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__")
 method is replaced with an unpacked result of calling this method. If a _bases_ item is an instance of `type`, or it doesn’t have an `__mro_entries__()` method, then it is included in the return tuple unchanged.

Added in version 3.7.

types.get\_original\_bases(_cls_, _/_)[¶](https://docs.python.org/3/library/types.html#types.get_original_bases "Link to this definition")

Return the tuple of objects originally given as the bases of _cls_ before the [`__mro_entries__()`](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__")
 method has been called on any bases (following the mechanisms laid out in [**PEP 560**](https://peps.python.org/pep-0560/)
). This is useful for introspecting [Generics](https://docs.python.org/3/library/typing.html#user-defined-generics)
.

For classes that have an `__orig_bases__` attribute, this function returns the value of `cls.__orig_bases__`. For classes without the `__orig_bases__` attribute, [`cls.__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
 is returned.

Examples:

Copy

from typing import TypeVar, Generic, NamedTuple, TypedDict

T \= TypeVar("T")
class Foo(Generic\[T\]): ...
class Bar(Foo\[int\], float): ...
class Baz(list\[str\]): ...
Eggs \= NamedTuple("Eggs", \[("a", int), ("b", str)\])
Spam \= TypedDict("Spam", {"a": int, "b": str})

assert Bar.\_\_bases\_\_ \== (Foo, float)
assert get\_original\_bases(Bar) \== (Foo\[int\], float)

assert Baz.\_\_bases\_\_ \== (list,)
assert get\_original\_bases(Baz) \== (list\[str\],)

assert Eggs.\_\_bases\_\_ \== (tuple,)
assert get\_original\_bases(Eggs) \== (NamedTuple,)

assert Spam.\_\_bases\_\_ \== (dict,)
assert get\_original\_bases(Spam) \== (TypedDict,)

assert int.\_\_bases\_\_ \== (object,)
assert get\_original\_bases(int) \== (object,)

Added in version 3.12.

See also

[**PEP 560**](https://peps.python.org/pep-0560/)
 - Core support for typing module and generic types

Standard Interpreter Types[¶](https://docs.python.org/3/library/types.html#standard-interpreter-types "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

This module provides names for many of the types that are required to implement a Python interpreter. It deliberately avoids including some of the types that arise only incidentally during processing such as the `listiterator` type.

Typical use of these names is for [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 or [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 checks.

If you instantiate any of these types, note that signatures may vary between Python versions.

Standard names are defined for the following types:

class types.NoneType[¶](https://docs.python.org/3/library/types.html#types.NoneType "Link to this definition")

The type of [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
.

Added in version 3.10.

class types.FunctionType[¶](https://docs.python.org/3/library/types.html#types.FunctionType "Link to this definition")

class types.LambdaType[¶](https://docs.python.org/3/library/types.html#types.LambdaType "Link to this definition")

The type of user-defined functions and functions created by [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda)
 expressions.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `function.__new__` with argument `code`.

The audit event only occurs for direct instantiation of function objects, and is not raised for normal compilation.

class types.GeneratorType[¶](https://docs.python.org/3/library/types.html#types.GeneratorType "Link to this definition")

The type of [generator](https://docs.python.org/3/glossary.html#term-generator)
\-iterator objects, created by generator functions.

class types.CoroutineType[¶](https://docs.python.org/3/library/types.html#types.CoroutineType "Link to this definition")

The type of [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 objects, created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def)
 functions.

Added in version 3.5.

class types.AsyncGeneratorType[¶](https://docs.python.org/3/library/types.html#types.AsyncGeneratorType "Link to this definition")

The type of [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
\-iterator objects, created by asynchronous generator functions.

Added in version 3.6.

class types.CodeType(_\*\*kwargs_)[¶](https://docs.python.org/3/library/types.html#types.CodeType "Link to this definition")

The type of [code objects](https://docs.python.org/3/reference/datamodel.html#code-objects)
 such as returned by [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `code.__new__` with arguments `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags`.

Note that the audited arguments may not match the names or positions required by the initializer. The audit event only occurs for direct instantiation of code objects, and is not raised for normal compilation.

class types.CellType[¶](https://docs.python.org/3/library/types.html#types.CellType "Link to this definition")

The type for cell objects: such objects are used as containers for a function’s [closure variables](https://docs.python.org/3/glossary.html#term-closure-variable)
.

Added in version 3.8.

class types.MethodType[¶](https://docs.python.org/3/library/types.html#types.MethodType "Link to this definition")

The type of methods of user-defined class instances.

class types.BuiltinFunctionType[¶](https://docs.python.org/3/library/types.html#types.BuiltinFunctionType "Link to this definition")

class types.BuiltinMethodType[¶](https://docs.python.org/3/library/types.html#types.BuiltinMethodType "Link to this definition")

The type of built-in functions like [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 or [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
, and methods of built-in classes. (Here, the term “built-in” means “written in C”.)

class types.WrapperDescriptorType[¶](https://docs.python.org/3/library/types.html#types.WrapperDescriptorType "Link to this definition")

The type of methods of some built-in data types and base classes such as [`object.__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 or [`object.__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
.

Added in version 3.7.

class types.MethodWrapperType[¶](https://docs.python.org/3/library/types.html#types.MethodWrapperType "Link to this definition")

The type of _bound_ methods of some built-in data types and base classes. For example it is the type of `object().__str__`.

Added in version 3.7.

class types.NotImplementedType[¶](https://docs.python.org/3/library/types.html#types.NotImplementedType "Link to this definition")

The type of [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
.

Added in version 3.10.

class types.MethodDescriptorType[¶](https://docs.python.org/3/library/types.html#types.MethodDescriptorType "Link to this definition")

The type of methods of some built-in data types such as [`str.join()`](https://docs.python.org/3/builtins/stdtypes.html#str.join "str.join")
.

Added in version 3.7.

class types.ClassMethodDescriptorType[¶](https://docs.python.org/3/library/types.html#types.ClassMethodDescriptorType "Link to this definition")

The type of _unbound_ class methods of some built-in data types such as `dict.__dict__['fromkeys']`.

Added in version 3.7.

class types.ModuleType(_name_, _doc\=None_)[¶](https://docs.python.org/3/library/types.html#types.ModuleType "Link to this definition")

The type of [modules](https://docs.python.org/3/glossary.html#term-module)
. The constructor takes the name of the module to be created and optionally its [docstring](https://docs.python.org/3/glossary.html#term-docstring)
.

See also

[Documentation on module objects](https://docs.python.org/3/reference/datamodel.html#module-objects)

Provides details on the special attributes that can be found on instances of `ModuleType`.

[`importlib.util.module_from_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "importlib.util.module_from_spec")

Modules created using the `ModuleType` constructor are created with many of their special attributes unset or set to default values. `module_from_spec()` provides a more robust way of creating `ModuleType` instances which ensures the various attributes are set appropriately.

class types.EllipsisType[¶](https://docs.python.org/3/library/types.html#types.EllipsisType "Link to this definition")

The type of [`Ellipsis`](https://docs.python.org/3/builtins/constants.html#Ellipsis "Ellipsis")
.

Added in version 3.10.

class types.GenericAlias(_t\_origin_, _t\_args_)[¶](https://docs.python.org/3/library/types.html#types.GenericAlias "Link to this definition")

The type of [parameterized generics](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 such as `list[int]`.

`t_origin` should be a non-parameterized generic class, such as `list`, `tuple` or `dict`. `t_args` should be a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 (possibly of length 1) of types which parameterize `t_origin`:

Copy

\>>> from types import GenericAlias

\>>> list\[int\] \== GenericAlias(list, (int,))
True
\>>> dict\[str, int\] \== GenericAlias(dict, (str, int))
True

Added in version 3.9.

Changed in version 3.9.2: This type can now be subclassed.

See also

[Generic Alias Types](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)

In-depth documentation on instances of `types.GenericAlias`

[**PEP 585**](https://peps.python.org/pep-0585/)
 - Type Hinting Generics In Standard Collections

Introducing the `types.GenericAlias` class

class types.UnionType[¶](https://docs.python.org/3/library/types.html#types.UnionType "Link to this definition")

The type of [union type expressions](https://docs.python.org/3/builtins/stdtypes.html#types-union)
.

Added in version 3.10.

Changed in version 3.14: This is now an alias for [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")
.

class types.TracebackType(_tb\_next_, _tb\_frame_, _tb\_lasti_, _tb\_lineno_)[¶](https://docs.python.org/3/library/types.html#types.TracebackType "Link to this definition")

The type of traceback objects such as found in `sys.exception().__traceback__`.

See [the language reference](https://docs.python.org/3/reference/datamodel.html#traceback-objects)
 for details of the available attributes and operations, and guidance on creating tracebacks dynamically.

class types.FrameType[¶](https://docs.python.org/3/library/types.html#types.FrameType "Link to this definition")

The type of [frame objects](https://docs.python.org/3/reference/datamodel.html#frame-objects)
 such as found in [`tb.tb_frame`](https://docs.python.org/3/reference/datamodel.html#traceback.tb_frame "traceback.tb_frame")
 if `tb` is a traceback object.

class types.FrameLocalsProxyType[¶](https://docs.python.org/3/library/types.html#types.FrameLocalsProxyType "Link to this definition")

The type of frame locals proxy objects, as found on the [`frame.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute.

Added in version 3.15.

See also

[**PEP 667**](https://peps.python.org/pep-0667/)

class types.LazyImportType[¶](https://docs.python.org/3/library/types.html#types.LazyImportType "Link to this definition")

The type of lazy import proxy objects. These objects are created when a module is lazily imported and serve as placeholders until the module is actually accessed. This type can be used to detect lazy imports programmatically.

Added in version 3.15.

See also

[**PEP 810**](https://peps.python.org/pep-0810/)

resolve()[¶](https://docs.python.org/3/library/types.html#types.LazyImportType.resolve "Link to this definition")

Reify the lazy import and return the “real” object being imported.

class types.GetSetDescriptorType[¶](https://docs.python.org/3/library/types.html#types.GetSetDescriptorType "Link to this definition")

The type of objects defined in extension modules with `PyGetSetDef`, such as [`FrameType.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 or `array.array.typecode`. This type is used as descriptor for object attributes; it has the same purpose as the [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
 type, but for classes defined in extension modules.

class types.MemberDescriptorType[¶](https://docs.python.org/3/library/types.html#types.MemberDescriptorType "Link to this definition")

The type of objects defined in extension modules with `PyMemberDef`, such as `datetime.timedelta.days`. This type is used as descriptor for simple C data members which use standard conversion functions; it has the same purpose as the [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
 type, but for classes defined in extension modules.

In addition, when a class is defined with a [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__")
 attribute, then for each slot, an instance of `MemberDescriptorType` will be added as an attribute on the class. This allows the slot to appear in the class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
.

**CPython implementation detail:** In other implementations of Python, this type may be identical to `GetSetDescriptorType`.

class types.MappingProxyType(_mapping_)[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType "Link to this definition")

Read-only proxy of a mapping. It provides a dynamic view on the mapping’s entries, which means that when the mapping changes, the view reflects these changes.

`MappingProxyType`s are [generic](https://docs.python.org/3/library/typing.html#generics)
 over two types, signifying (respectively) the types of the underlying mapping’s keys and values.

Added in version 3.3.

Changed in version 3.9: Updated to support the new union (`|`) operator from [**PEP 584**](https://peps.python.org/pep-0584/)
, which simply delegates to the underlying mapping.

key in proxy

Return `True` if the underlying mapping has a key _key_, else `False`.

proxy\[key\]

Return the item of the underlying mapping with key _key_. Raises a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if _key_ is not in the underlying mapping.

iter(proxy)

Return an iterator over the keys of the underlying mapping. This is a shortcut for `iter(proxy.keys())`.

len(proxy)

Return the number of items in the underlying mapping.

copy()[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType.copy "Link to this definition")

Return a shallow copy of the underlying mapping.

get(_key_\[, _default_\])[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType.get "Link to this definition")

Return the value for _key_ if _key_ is in the underlying mapping, else _default_. If _default_ is not given, it defaults to `None`, so that this method never raises a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
.

items()[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType.items "Link to this definition")

Return a new view of the underlying mapping’s items (`(key, value)` pairs).

keys()[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType.keys "Link to this definition")

Return a new view of the underlying mapping’s keys.

values()[¶](https://docs.python.org/3/library/types.html#types.MappingProxyType.values "Link to this definition")

Return a new view of the underlying mapping’s values.

reversed(proxy)

Return a reverse iterator over the keys of the underlying mapping.

Added in version 3.9.

hash(proxy)

Return a hash of the underlying mapping.

Added in version 3.12.

class types.CapsuleType[¶](https://docs.python.org/3/library/types.html#types.CapsuleType "Link to this definition")

The type of [capsule objects](https://docs.python.org/3/c-api/capsule.html#capsules)
.

Added in version 3.13.

Additional Utility Classes and Functions[¶](https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

class types.SimpleNamespace[¶](https://docs.python.org/3/library/types.html#types.SimpleNamespace "Link to this definition")

A simple [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 subclass that provides attribute access to its namespace, as well as a meaningful repr.

Unlike [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, with `SimpleNamespace` you can add and remove attributes.

`SimpleNamespace` objects may be initialized in the same way as [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
: either with keyword arguments, with a single positional argument, or with both. When initialized with keyword arguments, those are directly added to the underlying namespace. Alternatively, when initialized with a positional argument, the underlying namespace will be updated with key-value pairs from that argument (either a mapping object or an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 object producing key-value pairs). All such keys must be strings.

The type is roughly equivalent to the following code:

Copy

class SimpleNamespace:
    def \_\_init\_\_(self, mapping\_or\_iterable\=(), /, \*\*kwargs):
        self.\_\_dict\_\_.update(mapping\_or\_iterable)
        self.\_\_dict\_\_.update(kwargs)

    def \_\_repr\_\_(self):
        items \= (f"{k}\={v!r}" for k, v in self.\_\_dict\_\_.items())
        return "{}({})".format(type(self).\_\_name\_\_, ", ".join(items))

    def \_\_eq\_\_(self, other):
        if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
           return self.\_\_dict\_\_ \== other.\_\_dict\_\_
        return NotImplemented

`SimpleNamespace` may be useful as a replacement for `class NS: pass`. However, for a structured record type use [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
 instead.

`SimpleNamespace` objects are supported by [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
.

Added in version 3.3.

Changed in version 3.9: Attribute order in the repr changed from alphabetical to insertion (like `dict`).

Changed in version 3.13: Added support for an optional positional argument.

types.DynamicClassAttribute(_fget\=None_, _fset\=None_, _fdel\=None_, _doc\=None_)[¶](https://docs.python.org/3/library/types.html#types.DynamicClassAttribute "Link to this definition")

Route attribute access on a class to \_\_getattr\_\_.

This is a descriptor, used to define attributes that act differently when accessed through an instance and through a class. Instance access remains normal, but access to an attribute through a class will be routed to the class’s \_\_getattr\_\_ method; this is done by raising AttributeError.

This allows one to have properties active on an instance, and have virtual attributes on the class with the same name (see [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")
 for an example).

Added in version 3.4.

Coroutine Utility Functions[¶](https://docs.python.org/3/library/types.html#coroutine-utility-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

types.coroutine(_gen\_func_)[¶](https://docs.python.org/3/library/types.html#types.coroutine "Link to this definition")

This function transforms a [generator](https://docs.python.org/3/glossary.html#term-generator)
 function into a [coroutine function](https://docs.python.org/3/glossary.html#term-coroutine-function)
 which returns a generator-based coroutine. The generator-based coroutine is still a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)
, but is also considered to be a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 object and is [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
. However, it may not necessarily implement the [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 method.

If _gen\_func_ is a generator function, it will be modified in-place.

If _gen\_func_ is not a generator function, it will be wrapped. If it returns an instance of [`collections.abc.Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator")
, the instance will be wrapped in an _awaitable_ proxy object. All other types of objects will be returned as is.

Added in version 3.5.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html#)
    *   [Dynamic Type Creation](https://docs.python.org/3/library/types.html#dynamic-type-creation)
        
    *   [Standard Interpreter Types](https://docs.python.org/3/library/types.html#standard-interpreter-types)
        
    *   [Additional Utility Classes and Functions](https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions)
        
    *   [Coroutine Utility Functions](https://docs.python.org/3/library/types.html#coroutine-utility-functions)
        

#### Previous topic

[`weakref` — Weak references](https://docs.python.org/3/library/weakref.html "previous chapter")

#### Next topic

[`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=types+%E2%80%94+Dynamic+type+creation+and+names+for+built-in+types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftypes.html&pagesource=library%2Ftypes.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/types.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/copy.html "copy — Shallow and deep copy operations")
     |
*   [previous](https://docs.python.org/3/library/weakref.html "weakref — Weak references")
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
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html)
    
*    
    
    |
*   Theme Auto Light Dark |