### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/heapq.html "heapq — Heap queue algorithm")
     |
*   [previous](https://docs.python.org/3/library/collections.html "collections — Container datatypes")
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
*   [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`collections.abc` — Abstract Base Classes for Containers[¶](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "Link to this heading")

==================================================================================================================================================================

Added in version 3.3: Formerly, this module was part of the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 module.

**Source code:** [Lib/\_collections\_abc.py](https://github.com/python/cpython/tree/3.15/Lib/_collections_abc.py)

* * *

This module provides [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 that can be used to test whether a class provides a particular interface; for example, whether it is [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 or whether it is a [mapping](https://docs.python.org/3/glossary.html#term-mapping)
.

An [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 or [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 test for an interface works in one of three ways.

1.  A newly written class can inherit directly from one of the abstract base classes. The class must supply the required abstract methods. The remaining mixin methods come from inheritance and can be overridden if desired. Other methods may be added as needed:
    
    Copy
    
    class C(Sequence):                      \# Direct inheritance
        def \_\_init\_\_(self): ...             \# Extra method not required by the ABC
        def \_\_getitem\_\_(self, index):  ...  \# Required abstract method
        def \_\_len\_\_(self):  ...             \# Required abstract method
        def count(self, value): ...         \# Optionally override a mixin method
    
    Copy
    
    \>>> issubclass(C, Sequence)
    True
    \>>> isinstance(C(), Sequence)
    True
    
2.  Existing classes and built-in classes can be registered as “virtual subclasses” of the ABCs. Those classes should define the full API including all of the abstract methods and all of the mixin methods. This lets users rely on [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
     or [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
     tests to determine whether the full interface is supported. The exception to this rule is for methods that are automatically inferred from the rest of the API:
    
    Copy
    
    class D:                                 \# No inheritance
        def \_\_init\_\_(self): ...              \# Extra method not required by the ABC
        def \_\_getitem\_\_(self, index):  ...   \# Abstract method
        def \_\_len\_\_(self):  ...              \# Abstract method
        def count(self, value): ...          \# Mixin method
        def index(self, value): ...          \# Mixin method
    
    Sequence.register(D)                     \# Register instead of inherit
    
    Copy
    
    \>>> issubclass(D, Sequence)
    True
    \>>> isinstance(D(), Sequence)
    True
    
    In this example, class `D` does not need to define `__contains__`, `__iter__`, and `__reversed__` because the [in-operator](https://docs.python.org/3/reference/expressions.html#comparisons)
    , the [iteration](https://docs.python.org/3/glossary.html#term-iterable)
     logic, and the [`reversed()`](https://docs.python.org/3/builtins/functions.html#reversed "reversed")
     function automatically fall back to using `__getitem__` and `__len__`.
    
3.  Some simple interfaces are directly recognizable by the presence of the required methods (unless those methods have been set to [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
    ):
    
    Copy
    
    class E:
        def \_\_iter\_\_(self): ...
        def \_\_next\_\_(self): ...
    
    Copy
    
    \>>> issubclass(E, Iterable)
    True
    \>>> isinstance(E(), Iterable)
    True
    
    Complex interfaces do not support this last technique because an interface is more than just the presence of method names. Interfaces specify semantics and relationships between methods that cannot be inferred solely from the presence of specific method names. For example, knowing that a class supplies `__getitem__`, `__len__`, and `__iter__` is insufficient for distinguishing a [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
     from a [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")
    .
    

Added in version 3.9: These abstract classes now support `[]`. See [Generic Alias Type](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 and [**PEP 585**](https://peps.python.org/pep-0585/)
.

Collections Abstract Base Classes[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

The collections module offers the following [ABCs](https://docs.python.org/3/glossary.html#term-abstract-base-class)
, where the “Abstract Methods” column lists all required abstract methods, including those inherited from parent classes:

| ABC | Inherits from | Abstract Methods | Mixin Methods |
| --- | --- | --- | --- |
| [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__contains__` |     |
| [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__hash__` |     |
| [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18)<br> [\[2\]](https://docs.python.org/3/library/collections.abc.html#id19) |     | `__iter__` |     |
| [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") | `__next__` | `__iter__` |
| [`Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") | `__iter__`, `__reversed__` |     |
| [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator") | `send`, `throw` | `close`, `__iter__`, `__next__` |
| [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__len__` |     |
| [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__call__` |     |
| [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized")<br>, [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable")<br>, [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container") | `__contains__`, `__iter__`, `__len__` |     |
| [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") | [`Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible")<br>, [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") | `__getitem__`, `__len__` | `__contains__`, `__iter__`, `__reversed__`, `index`, and `count` |
| [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") | [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") | `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert` | Inherited [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")<br> methods and `append`, `clear`, `reverse`, `extend`, `pop`, `remove`, and `__iadd__` |
| [`ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString") | [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") | `__getitem__`, `__len__` | Inherited [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")<br> methods |
| [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") | [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") | `__contains__`, `__iter__`, `__len__` | `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__rsub__`, `__xor__`, `__rxor__` and `isdisjoint` |
| [`MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet") | [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") | `__contains__`, `__iter__`, `__len__`, `add`, `discard` | Inherited [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set")<br> methods and `clear`, `pop`, `remove`, `__ior__`, `__iand__`, `__ixor__`, and `__isub__` |
| [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") | [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") | `__getitem__`, `__iter__`, `__len__` | `__contains__`, `keys`, `items`, `values`, `get`, `__eq__`, and `__ne__` |
| [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") | [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") | `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__` | Inherited [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")<br> methods and `pop`, `popitem`, `clear`, `update`, and `setdefault` |
| [`MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView") | [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized") |     | `__init__`, `__len__` and `__repr__` |
| [`ItemsView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView") | [`MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView")<br>, [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") |     | `__contains__`, `__iter__` |
| [`KeysView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView "collections.abc.KeysView") | [`MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView")<br>, [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") |     | `__contains__`, `__iter__` |
| [`ValuesView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView") | [`MappingView`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView")<br>, [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") |     | `__contains__`, `__iter__` |
| [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__await__` |     |
| [`Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable") | `__await__`, `send`, `throw` | `close` |
| [`AsyncIterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__aiter__` |     |
| [`AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`AsyncIterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable") | `__anext__` | `__aiter__` |
| [`AsyncGenerator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) | [`AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator") | `asend`, `athrow` | `aclose`, `__aiter__`, `__anext__` |
| [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")<br> [\[1\]](https://docs.python.org/3/library/collections.abc.html#id18) |     | `__buffer__` |     |

Footnotes

Collections Abstract Base Classes – Detailed Descriptions[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class collections.abc.Container[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "Link to this definition")

ABC for classes that provide the [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 method.

class collections.abc.Hashable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "Link to this definition")

ABC for classes that provide the [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 method.

class collections.abc.Sized[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "Link to this definition")

ABC for classes that provide the [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
 method.

class collections.abc.Callable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "Link to this definition")

ABC for classes that provide the [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method.

See [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callables)
 for details on how to use `Callable` in type annotations.

class collections.abc.Iterable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "Link to this definition")

ABC for classes that provide the [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
 method.

Checking `isinstance(obj, Iterable)` detects classes that are registered as `Iterable` or that have an [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
 method, but it does not detect classes that iterate with the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method. The only reliable way to determine whether an object is [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 is to call `iter(obj)`.

class collections.abc.Collection[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "Link to this definition")

ABC for sized iterable container classes.

Added in version 3.6.

class collections.abc.Iterator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "Link to this definition")

ABC for classes that provide the [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__iter__ "iterator.__iter__")
 and [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
 methods. See also the definition of [iterator](https://docs.python.org/3/glossary.html#term-iterator)
.

class collections.abc.Reversible[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "Link to this definition")

ABC for iterable classes that also provide the [`__reversed__()`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__ "object.__reversed__")
 method.

Added in version 3.6.

class collections.abc.Generator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "Link to this definition")

ABC for [generator](https://docs.python.org/3/glossary.html#term-generator)
 classes that implement the protocol defined in [**PEP 342**](https://peps.python.org/pep-0342/)
 that extends [iterators](https://docs.python.org/3/glossary.html#term-iterator)
 with the [`send()`](https://docs.python.org/3/builtins/stdtypes.html#generator.send "generator.send")
, [`throw()`](https://docs.python.org/3/builtins/stdtypes.html#generator.throw "generator.throw")
 and [`close()`](https://docs.python.org/3/builtins/stdtypes.html#generator.close "generator.close")
 methods.

See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
 for details on using `Generator` in type annotations.

Added in version 3.5.

class collections.abc.Sequence[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "Link to this definition")

class collections.abc.MutableSequence[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "Link to this definition")

class collections.abc.ByteString[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "Link to this definition")

ABCs for read-only and mutable [sequences](https://docs.python.org/3/glossary.html#term-sequence)
.

Implementation note: Some of the mixin methods, such as [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
, [`__reversed__()`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__ "object.__reversed__")
, and [`index()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.index "sequence.index")
 make repeated calls to the underlying [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method. Consequently, if `__getitem__()` is implemented with constant access speed, the mixin methods will have linear performance; however, if the underlying method is linear (as it would be with a linked list), the mixins will have quadratic performance and will likely need to be overridden.

index(_value_, _start\=0_, _stop\=None_)[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString.index "Link to this definition")

Return first index of _value_.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if the value is not present.

Supporting the _start_ and _stop_ arguments is optional, but recommended.

Changed in version 3.5: The [`index()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.index "sequence.index")
 method gained support for the _stop_ and _start_ arguments.

Deprecated since version 3.12, will be removed in version 3.17: The `ByteString` ABC has been deprecated.

Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
 or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).

`ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
. However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).

See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)
 for more details.

class collections.abc.Set[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "Link to this definition")

class collections.abc.MutableSet[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "Link to this definition")

ABCs for read-only and mutable [sets](https://docs.python.org/3/builtins/stdtypes.html#types-set)
.

class collections.abc.Mapping[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "Link to this definition")

class collections.abc.MutableMapping[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "Link to this definition")

ABCs for read-only and mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping)
.

class collections.abc.MappingView[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView "Link to this definition")

class collections.abc.ItemsView[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView "Link to this definition")

class collections.abc.KeysView[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView "Link to this definition")

class collections.abc.ValuesView[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView "Link to this definition")

ABCs for mapping, items, keys, and values [views](https://docs.python.org/3/glossary.html#term-dictionary-view)
.

class collections.abc.Awaitable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "Link to this definition")

ABC for [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 objects, which can be used in [`await`](https://docs.python.org/3/reference/expressions.html#await)
 expressions. Custom implementations must provide the [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 method.

[Coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 objects and instances of the [`Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine")
 ABC are all instances of this ABC.

Note

In CPython, generator-based coroutines ([generators](https://docs.python.org/3/glossary.html#term-generator)
 decorated with [`@types.coroutine`](https://docs.python.org/3/library/types.html#types.coroutine "types.coroutine")
) are _awaitables_, even though they do not have an [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 method. Using `isinstance(gencoro, Awaitable)` for them will return `False`. Use [`inspect.isawaitable()`](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "inspect.isawaitable")
 to detect them.

Added in version 3.5.

class collections.abc.Coroutine[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "Link to this definition")

ABC for [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 compatible classes. These implement the following methods, defined in [Coroutine Objects](https://docs.python.org/3/reference/datamodel.html#coroutine-objects)
: [`send()`](https://docs.python.org/3/reference/datamodel.html#coroutine.send "coroutine.send")
, [`throw()`](https://docs.python.org/3/reference/datamodel.html#coroutine.throw "coroutine.throw")
, and [`close()`](https://docs.python.org/3/reference/datamodel.html#coroutine.close "coroutine.close")
. Custom implementations must also implement [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
. All `Coroutine` instances are also instances of [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")
.

Note

In CPython, generator-based coroutines ([generators](https://docs.python.org/3/glossary.html#term-generator)
 decorated with [`@types.coroutine`](https://docs.python.org/3/library/types.html#types.coroutine "types.coroutine")
) are _awaitables_, even though they do not have an [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__")
 method. Using `isinstance(gencoro, Coroutine)` for them will return `False`. Use [`inspect.isawaitable()`](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "inspect.isawaitable")
 to detect them.

See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
 for details on using `Coroutine` in type annotations. The variance and order of type parameters correspond to those of [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator")
.

Added in version 3.5.

class collections.abc.AsyncIterable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "Link to this definition")

ABC for classes that provide an `__aiter__` method. See also the definition of [asynchronous iterable](https://docs.python.org/3/glossary.html#term-asynchronous-iterable)
.

Added in version 3.5.

class collections.abc.AsyncIterator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "Link to this definition")

ABC for classes that provide `__aiter__` and `__anext__` methods. See also the definition of [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
.

Added in version 3.5.

class collections.abc.AsyncGenerator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "Link to this definition")

ABC for [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 classes that implement the protocol defined in [**PEP 525**](https://peps.python.org/pep-0525/)
 and [**PEP 492**](https://peps.python.org/pep-0492/)
.

See [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
 for details on using `AsyncGenerator` in type annotations.

Added in version 3.6.

class collections.abc.Buffer[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "Link to this definition")

ABC for classes that provide the [`__buffer__()`](https://docs.python.org/3/reference/datamodel.html#object.__buffer__ "object.__buffer__")
 method, implementing the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
. See [**PEP 688**](https://peps.python.org/pep-0688/)
.

Added in version 3.12.

Examples and Recipes[¶](https://docs.python.org/3/library/collections.abc.html#examples-and-recipes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

ABCs allow us to ask classes or instances if they provide particular functionality, for example:

Copy

size \= None
if isinstance(myvar, collections.abc.Sized):
    size \= len(myvar)

Several of the ABCs are also useful as mixins that make it easier to develop classes supporting container APIs. For example, to write a class supporting the full [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set")
 API, it is only necessary to supply the three underlying abstract methods: [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
, [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
, and [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
. The ABC supplies the remaining methods such as `__and__()` and [`isdisjoint()`](https://docs.python.org/3/builtins/stdtypes.html#frozenset.isdisjoint "frozenset.isdisjoint")
:

Copy

class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def \_\_init\_\_(self, iterable):
        self.elements \= lst \= \[\]
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def \_\_iter\_\_(self):
        return iter(self.elements)

    def \_\_contains\_\_(self, value):
        return value in self.elements

    def \_\_len\_\_(self):
        return len(self.elements)

s1 \= ListBasedSet('abcdef')
s2 \= ListBasedSet('defghi')
overlap \= s1 & s2            \# The \_\_and\_\_() method is supported automatically

Notes on using [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set")
 and [`MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet")
 as a mixin:

1.  Since some set operations create new sets, the default mixin methods need a way to create new instances from an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
    . The class constructor is assumed to have a signature in the form `ClassName(iterable)`. That assumption is factored-out to an internal [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
     called `_from_iterable()` which calls `cls(iterable)` to produce a new set. If the [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set")
     mixin is being used in a class with a different constructor signature, you will need to override `_from_iterable()` with a classmethod or regular method that can construct new instances from an iterable argument.
    
2.  To override the comparisons (presumably for speed, as the semantics are fixed), redefine [`__le__()`](https://docs.python.org/3/reference/datamodel.html#object.__le__ "object.__le__")
     and [`__ge__()`](https://docs.python.org/3/reference/datamodel.html#object.__ge__ "object.__ge__")
    , then the other operations will automatically follow suit.
    
3.  The [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set")
     mixin provides a `_hash()` method to compute a hash value for the set; however, [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
     is not defined because not all sets are [hashable](https://docs.python.org/3/glossary.html#term-hashable)
     or immutable. To add set hashability using mixins, inherit from both `Set` and [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable")
    , then define `__hash__ = Set._hash`.
    

See also

*   [OrderedSet recipe](https://code.activestate.com/recipes/576694/)
     for an example built on [`MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet")
    .
    
*   For more about ABCs, see the [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
     module and [**PEP 3119**](https://peps.python.org/pep-3119/)
    .
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html#)
    *   [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes)
        
    *   [Collections Abstract Base Classes – Detailed Descriptions](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions)
        
    *   [Examples and Recipes](https://docs.python.org/3/library/collections.abc.html#examples-and-recipes)
        

#### Previous topic

[`collections` — Container datatypes](https://docs.python.org/3/library/collections.html "previous chapter")

#### Next topic

[`heapq` — Heap queue algorithm](https://docs.python.org/3/library/heapq.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=collections.abc+%E2%80%94+Abstract+Base+Classes+for+Containers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcollections.abc.html&pagesource=library%2Fcollections.abc.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/collections.abc.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/heapq.html "heapq — Heap queue algorithm")
     |
*   [previous](https://docs.python.org/3/library/collections.html "collections — Container datatypes")
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
*   [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
    
*    
    
    |
*   Theme Auto Light Dark |