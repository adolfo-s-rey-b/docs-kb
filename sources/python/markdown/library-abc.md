### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/atexit.html "atexit — Exit handlers")
     |
*   [previous](https://docs.python.org/3/library/contextlib.html "contextlib — Utilities for with-statement contexts")
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
*   [`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`abc` — Abstract Base Classes[¶](https://docs.python.org/3/library/abc.html#module-abc "Link to this heading")

===============================================================================================================

**Source code:** [Lib/abc.py](https://github.com/python/cpython/tree/3.15/Lib/abc.py)

* * *

This module provides the infrastructure for defining [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 (ABCs) in Python, as outlined in [**PEP 3119**](https://peps.python.org/pep-3119/)
; see the PEP for why this was added to Python. (See also [**PEP 3141**](https://peps.python.org/pep-3141/)
 and the [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).")
 module regarding a type hierarchy for numbers based on ABCs.)

The [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 module has some concrete classes that derive from ABCs; these can, of course, be further derived. In addition, the [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
 submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, for example, if it is [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 or if it is a [mapping](https://docs.python.org/3/glossary.html#term-mapping)
.

This module provides the metaclass [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
 for defining ABCs and a helper class [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")
 to alternatively define ABCs through inheritance:

class abc.ABC[¶](https://docs.python.org/3/library/abc.html#abc.ABC "Link to this definition")

A helper class that has [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
 as its metaclass. With this class, an abstract base class can be created by simply deriving from `ABC` avoiding sometimes confusing metaclass usage, for example:

Copy

from abc import ABC

class MyABC(ABC):
    pass

Note that the type of `ABC` is still [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
, therefore inheriting from `ABC` requires the usual precautions regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the metaclass keyword and using `ABCMeta` directly, for example:

Copy

from abc import ABCMeta

class MyABC(metaclass\=ABCMeta):
    pass

Added in version 3.4.

class abc.ABCMeta[¶](https://docs.python.org/3/library/abc.html#abc.ABCMeta "Link to this definition")

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as “virtual subclasses” – these and their descendants will be considered subclasses of the registering ABC by the built-in [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 function, but the registering ABC won’t show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
). [\[1\]](https://docs.python.org/3/library/abc.html#id2)

Classes created with a metaclass of `ABCMeta` have the following method:

register(_subclass_)[¶](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "Link to this definition")

Register _subclass_ as a “virtual subclass” of this ABC. For example:

Copy

from abc import ABC

class MyABC(ABC):
    pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

Changed in version 3.3: Returns the registered subclass, to allow usage as a class decorator.

Changed in version 3.4: To detect calls to `register()`, you can use the [`get_cache_token()`](https://docs.python.org/3/library/abc.html#abc.get_cache_token "abc.get_cache_token")
 function.

You can also override this method in an abstract base class:

\_\_subclasshook\_\_(_subclass_)[¶](https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__ "Link to this definition")

(Must be defined as a class method.)

Check whether _subclass_ is considered a subclass of this ABC. This means that you can customize the behavior of [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 further without the need to call [`register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 on every class you want to consider a subclass of the ABC. (This class method is called from the [`__subclasscheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__ "type.__subclasscheck__")
 method of the ABC.)

This method should return `True`, `False` or [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
. If it returns `True`, the _subclass_ is considered a subclass of this ABC. If it returns `False`, the _subclass_ is not considered a subclass of this ABC, even if it would normally be one. If it returns `NotImplemented`, the subclass check is continued with the usual mechanism.

For a demonstration of these concepts, look at this example ABC definition:

Copy

class Foo:
    def \_\_getitem\_\_(self, index):
        ...
    def \_\_len\_\_(self):
        ...
    def get\_iterator(self):
        return iter(self)

class MyIterable(ABC):

    @abstractmethod
    def \_\_iter\_\_(self):
        while False:
            yield None

    def get\_iterator(self):
        return self.\_\_iter\_\_()

    @classmethod
    def \_\_subclasshook\_\_(cls, C):
        if cls is MyIterable:
            if any("\_\_iter\_\_" in B.\_\_dict\_\_ for B in C.\_\_mro\_\_):
                return True
        return NotImplemented

MyIterable.register(Foo)

The ABC `MyIterable` defines the standard iterable method, [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
, as an abstract method. The implementation given here can still be called from subclasses. The `get_iterator()` method is also part of the `MyIterable` abstract base class, but it does not have to be overridden in non-abstract derived classes.

The [`__subclasshook__()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__ "abc.ABCMeta.__subclasshook__")
 class method defined here says that any class that has an [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
 method in its [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 (or in that of one of its base classes, accessed via the [`__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__")
 list) is considered a `MyIterable` too.

Finally, the last line makes `Foo` a virtual subclass of `MyIterable`, even though it does not define an [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__")
 method (it uses the old-style iterable protocol, defined in terms of [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__")
 and [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
). Note that this will not make `get_iterator` available as a method of `Foo`, so it is provided separately.

The `abc` module also provides the following decorator:

@abc.abstractmethod[¶](https://docs.python.org/3/library/abc.html#abc.abstractmethod "Link to this definition")

A decorator indicating abstract methods.

Using this decorator requires that the class’s metaclass is [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
 or is derived from it. A class that has a metaclass derived from `ABCMeta` cannot be instantiated unless all of its abstract methods and properties are overridden. The abstract methods can be called using any of the normal ‘super’ call mechanisms. `abstractmethod` may be used to declare abstract methods for properties and descriptors.

Dynamically adding abstract methods to a class, or attempting to modify the abstraction status of a method or class once it is created, are only supported using the [`update_abstractmethods()`](https://docs.python.org/3/library/abc.html#abc.update_abstractmethods "abc.update_abstractmethods")
 function. The `abstractmethod` only affects subclasses derived using regular inheritance; “virtual subclasses” registered with the ABC’s [`register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 method are not affected.

When `abstractmethod` is applied in combination with other method descriptors, it should be applied as the innermost decorator, as shown in the following usage examples:

Copy

class C(ABC):
    @abstractmethod
    def my\_abstract\_method(self, arg1):
        ...
    @classmethod
    @abstractmethod
    def my\_abstract\_classmethod(cls, arg2):
        ...
    @staticmethod
    @abstractmethod
    def my\_abstract\_staticmethod(arg3):
        ...

    @property
    @abstractmethod
    def my\_abstract\_property(self):
        ...
    @my\_abstract\_property.setter
    @abstractmethod
    def my\_abstract\_property(self, val):
        ...

    @abstractmethod
    def \_get\_x(self):
        ...
    @abstractmethod
    def \_set\_x(self, val):
        ...
    x \= property(\_get\_x, \_set\_x)

In order to correctly interoperate with the abstract base class machinery, the descriptor must identify itself as abstract using `__isabstractmethod__`. In general, this attribute should be `True` if any of the methods used to compose the descriptor are abstract. For example, Python’s built-in [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
 does the equivalent of:

Copy

class Descriptor:
    ...
    @property
    def \_\_isabstractmethod\_\_(self):
        return any(getattr(f, '\_\_isabstractmethod\_\_', False) for
                   f in (self.\_fget, self.\_fset, self.\_fdel))

Note

Unlike Java abstract methods, these abstract methods may have an implementation. This implementation can be called via the [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
 mechanism from the class that overrides it. This could be useful as an end-point for a super-call in a framework that uses cooperative multiple-inheritance.

The `abc` module also supports the following legacy decorators:

@abc.abstractclassmethod[¶](https://docs.python.org/3/library/abc.html#abc.abstractclassmethod "Link to this definition")

Added in version 3.2.

Deprecated since version 3.3: It is now possible to use [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 with [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
, making this decorator redundant.

A subclass of the built-in [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
, indicating an abstract classmethod. Otherwise it is similar to [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
.

This special case is deprecated, as the [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 decorator is now correctly identified as abstract when applied to an abstract method:

Copy

class C(ABC):
    @classmethod
    @abstractmethod
    def my\_abstract\_classmethod(cls, arg):
        ...

@abc.abstractstaticmethod[¶](https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod "Link to this definition")

Added in version 3.2.

Deprecated since version 3.3: It is now possible to use [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 with [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
, making this decorator redundant.

A subclass of the built-in [`staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
, indicating an abstract staticmethod. Otherwise it is similar to [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
.

This special case is deprecated, as the [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 decorator is now correctly identified as abstract when applied to an abstract method:

Copy

class C(ABC):
    @staticmethod
    @abstractmethod
    def my\_abstract\_staticmethod(arg):
        ...

@abc.abstractproperty[¶](https://docs.python.org/3/library/abc.html#abc.abstractproperty "Link to this definition")

Deprecated since version 3.3: It is now possible to use [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
, [`@property.getter`](https://docs.python.org/3/builtins/functions.html#property.getter "property.getter")
, [`@property.setter`](https://docs.python.org/3/builtins/functions.html#property.setter "property.setter")
 and [`@property.deleter`](https://docs.python.org/3/builtins/functions.html#property.deleter "property.deleter")
 with [`@abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
, making this decorator redundant.

A subclass of the built-in [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
, indicating an abstract property.

This special case is deprecated, as the [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
 decorator is now correctly identified as abstract when applied to an abstract method:

Copy

class C(ABC):
    @property
    @abstractmethod
    def my\_abstract\_property(self):
        ...

The above example defines a read-only property; you can also define a read-write abstract property by appropriately marking one or more of the underlying methods as abstract:

Copy

class C(ABC):
    @property
    def x(self):
        ...

    @x.setter
    @abstractmethod
    def x(self, val):
        ...

If only some components are abstract, only those components need to be updated to create a concrete property in a subclass:

Copy

class D(C):
    @C.x.setter
    def x(self, val):
        ...

The `abc` module also provides the following functions:

abc.get\_cache\_token()[¶](https://docs.python.org/3/library/abc.html#abc.get_cache_token "Link to this definition")

Returns the current abstract base class cache token.

The token is an opaque object (that supports equality testing) identifying the current version of the abstract base class cache for virtual subclasses. The token changes with every call to [`ABCMeta.register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 on any ABC.

Added in version 3.4.

abc.update\_abstractmethods(_cls_)[¶](https://docs.python.org/3/library/abc.html#abc.update_abstractmethods "Link to this definition")

A function to recalculate an abstract class’s abstraction status. This function should be called if a class’s abstract methods have been implemented or changed after it was created. Usually, this function should be called from within a class decorator.

Returns _cls_, to allow usage as a class decorator.

If _cls_ is not an instance of [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
, does nothing.

Note

This function assumes that _cls_’s superclasses are already updated. It does not update any subclasses.

Added in version 3.10.

Footnotes

#### Previous topic

[`contextlib` — Utilities for `with`\-statement contexts](https://docs.python.org/3/library/contextlib.html "previous chapter")

#### Next topic

[`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=abc+%E2%80%94+Abstract+Base+Classes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fabc.html&pagesource=library%2Fabc.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/abc.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/atexit.html "atexit — Exit handlers")
     |
*   [previous](https://docs.python.org/3/library/contextlib.html "contextlib — Utilities for with-statement contexts")
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
*   [`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
    
*    
    
    |
*   Theme Auto Light Dark |