### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/gdb_helpers.html "Debugging C API extensions and CPython Internals with GDB")
     |
*   [previous](https://docs.python.org/3/howto/curses.html "Curses Programming with Python")
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
*   [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html)
    
*    
    
    |
*   Theme Auto Light Dark |

[Descriptor Guide](https://docs.python.org/3/howto/descriptor.html#id1)
[¶](https://docs.python.org/3/howto/descriptor.html#descriptor-guide "Link to this heading")

=====================================================================================================================================================================

[Descriptors](https://docs.python.org/3/glossary.html#term-descriptor)
 let objects customize attribute lookup, storage, and deletion.

This guide has four major sections:

1.  The “primer” gives a basic overview, moving gently from simple examples, adding one feature at a time. Start here if you’re new to descriptors.
    
2.  The second section shows a complete, practical descriptor example. If you already know the basics, start there.
    
3.  The third section provides a more technical tutorial that goes into the detailed mechanics of how descriptors work. Most people don’t need this level of detail.
    
4.  The last section has pure Python equivalents for built-in descriptors that are written in C. Read this if you’re curious about how functions turn into bound methods or about the implementation of common tools like [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
    , [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
    , [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
    , and [\_\_slots\_\_](https://docs.python.org/3/glossary.html#term-__slots__)
    .
    

[Primer](https://docs.python.org/3/howto/descriptor.html#id2)
[¶](https://docs.python.org/3/howto/descriptor.html#primer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

In this primer, we start with the most basic possible example and then we’ll add new capabilities one by one.

### [Simple example: A descriptor that returns a constant](https://docs.python.org/3/howto/descriptor.html#id3)
[¶](https://docs.python.org/3/howto/descriptor.html#simple-example-a-descriptor-that-returns-a-constant "Link to this heading")

The `Ten` class is a descriptor whose [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method always returns the constant `10`:

Copy

class Ten:
    def \_\_get\_\_(self, obj, objtype\=None):
        return 10

To use the descriptor, it must be stored as a class variable in another class:

Copy

class A:
    x \= 5                       \# Regular class attribute
    y \= Ten()                   \# Descriptor instance

An interactive session shows the difference between normal attribute lookup and descriptor lookup:

Copy

\>>> a \= A()                     \# Make an instance of class A
\>>> a.x                         \# Normal attribute lookup
5
\>>> a.y                         \# Descriptor lookup
10

In the `a.x` attribute lookup, the dot operator finds `'x': 5` in the class dictionary. In the `a.y` lookup, the dot operator finds a descriptor instance, recognized by its `__get__` method. Calling that method returns `10`.

Note that the value `10` is not stored in either the class dictionary or the instance dictionary. Instead, the value `10` is computed on demand.

This example shows how a simple descriptor works, but it isn’t very useful. For retrieving constants, normal attribute lookup would be better.

In the next section, we’ll create something more useful, a dynamic lookup.

### [Dynamic lookups](https://docs.python.org/3/howto/descriptor.html#id4)
[¶](https://docs.python.org/3/howto/descriptor.html#dynamic-lookups "Link to this heading")

Interesting descriptors typically run computations instead of returning constants:

Copy

import os

class DirectorySize:

    def \_\_get\_\_(self, obj, objtype\=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size \= DirectorySize()              \# Descriptor instance

    def \_\_init\_\_(self, dirname):
        self.dirname \= dirname          \# Regular instance attribute

An interactive session shows that the lookup is dynamic — it computes different, updated answers each time:

Copy

\>>> s \= Directory('songs')
\>>> g \= Directory('games')
\>>> s.size                              \# The songs directory has twenty files
20
\>>> g.size                              \# The games directory has three files
3
\>>> os.remove('games/chess')            \# Delete a game
\>>> g.size                              \# File count is automatically updated
2

Besides showing how descriptors can run computations, this example also reveals the purpose of the parameters to [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
. The _self_ parameter is _size_, an instance of _DirectorySize_. The _obj_ parameter is either _g_ or _s_, an instance of _Directory_. It is the _obj_ parameter that lets the `__get__()` method learn the target directory. The _objtype_ parameter is the class _Directory_.

### [Managed attributes](https://docs.python.org/3/howto/descriptor.html#id5)
[¶](https://docs.python.org/3/howto/descriptor.html#managed-attributes "Link to this heading")

A popular use for descriptors is managing access to instance data. The descriptor is assigned to a public attribute in the class dictionary while the actual data is stored as a private attribute in the instance dictionary. The descriptor’s [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 and [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 methods are triggered when the public attribute is accessed.

In the following example, _age_ is the public attribute and _\_age_ is the private attribute. When the public attribute is accessed, the descriptor logs the lookup or update:

Copy

import logging

logging.basicConfig(level\=logging.INFO)

class LoggedAgeAccess:

    def \_\_get\_\_(self, obj, objtype\=None):
        value \= obj.\_age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def \_\_set\_\_(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj.\_age \= value

class Person:

    age \= LoggedAgeAccess()             \# Descriptor instance

    def \_\_init\_\_(self, name, age):
        self.name \= name                \# Regular instance attribute
        self.age \= age                  \# Calls \_\_set\_\_()

    def birthday(self):
        self.age += 1                   \# Calls both \_\_get\_\_() and \_\_set\_\_()

An interactive session shows that all access to the managed attribute _age_ is logged, but that the regular attribute _name_ is not logged:

Copy

\>>> mary \= Person('Mary M', 30)         \# The initial age update is logged
INFO:root:Updating 'age' to 30
\>>> dave \= Person('David D', 40)
INFO:root:Updating 'age' to 40

\>>> vars(mary)                          \# The actual data is in a private attribute
{'name': 'Mary M', '\_age': 30}
\>>> vars(dave)
{'name': 'David D', '\_age': 40}

\>>> mary.age                            \# Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
30
\>>> mary.birthday()                     \# Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

\>>> dave.name                           \# Regular attribute lookup isn't logged
'David D'
\>>> dave.age                            \# Only the managed attribute is logged
INFO:root:Accessing 'age' giving 40
40

One major issue with this example is that the private name _\_age_ is hardwired in the _LoggedAgeAccess_ class. That means that each instance can only have one logged attribute and that its name is unchangeable. In the next example, we’ll fix that problem.

### [Customized names](https://docs.python.org/3/howto/descriptor.html#id6)
[¶](https://docs.python.org/3/howto/descriptor.html#customized-names "Link to this heading")

When a class uses descriptors, it can inform each descriptor about which variable name was used.

In this example, the `Person` class has two descriptor instances, _name_ and _age_. When the `Person` class is defined, it makes a callback to [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
 in _LoggedAccess_ so that the field names can be recorded, giving each descriptor its own _public\_name_ and _private\_name_:

Copy

import logging

logging.basicConfig(level\=logging.INFO)

class LoggedAccess:

    def \_\_set\_name\_\_(self, owner, name):
        self.public\_name \= name
        self.private\_name \= '\_' + name

    def \_\_get\_\_(self, obj, objtype\=None):
        value \= getattr(obj, self.private\_name)
        logging.info('Accessing %r giving %r', self.public\_name, value)
        return value

    def \_\_set\_\_(self, obj, value):
        logging.info('Updating %r to %r', self.public\_name, value)
        setattr(obj, self.private\_name, value)

class Person:

    name \= LoggedAccess()                \# First descriptor instance
    age \= LoggedAccess()                 \# Second descriptor instance

    def \_\_init\_\_(self, name, age):
        self.name \= name                 \# Calls the first descriptor
        self.age \= age                   \# Calls the second descriptor

    def birthday(self):
        self.age += 1

An interactive session shows that the `Person` class has called [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
 so that the field names would be recorded. Here we call [`vars()`](https://docs.python.org/3/builtins/functions.html#vars "vars")
 to look up the descriptor without triggering it:

Copy

\>>> vars(vars(Person)\['name'\])
{'public\_name': 'name', 'private\_name': '\_name'}
\>>> vars(vars(Person)\['age'\])
{'public\_name': 'age', 'private\_name': '\_age'}

The new class now logs access to both _name_ and _age_:

Copy

\>>> pete \= Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10
\>>> kate \= Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20

The two _Person_ instances contain only the private names:

Copy

\>>> vars(pete)
{'\_name': 'Peter P', '\_age': 10}
\>>> vars(kate)
{'\_name': 'Catherine C', '\_age': 20}

### [Closing thoughts](https://docs.python.org/3/howto/descriptor.html#id7)
[¶](https://docs.python.org/3/howto/descriptor.html#closing-thoughts "Link to this heading")

A [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
 is what we call any object that defines [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
, [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
, or [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
.

Optionally, descriptors can have a [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
 method. This is only used in cases where a descriptor needs to know either the class where it was created or the name of class variable it was assigned to. (This method, if present, is called even if the class is not a descriptor.)

Descriptors get invoked by the dot operator during attribute lookup. If a descriptor is accessed indirectly with `vars(some_class)[descriptor_name]`, the descriptor instance is returned without invoking it.

Descriptors only work when used as class variables. When put in instances, they have no effect.

The main motivation for descriptors is to provide a hook allowing objects stored in class variables to control what happens during attribute lookup.

Traditionally, the calling class controls what happens during lookup. Descriptors invert that relationship and allow the data being looked-up to have a say in the matter.

Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
, [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
, [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
, and [`@functools.cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property "functools.cached_property")
 are all implemented as descriptors.

[Complete Practical Example](https://docs.python.org/3/howto/descriptor.html#id8)
[¶](https://docs.python.org/3/howto/descriptor.html#complete-practical-example "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this example, we create a practical and powerful tool for locating notoriously hard to find data corruption bugs.

### [Validator class](https://docs.python.org/3/howto/descriptor.html#id9)
[¶](https://docs.python.org/3/howto/descriptor.html#validator-class "Link to this heading")

A validator is a descriptor for managed attribute access. Prior to storing any data, it verifies that the new value meets various type and range restrictions. If those restrictions aren’t met, it raises an exception to prevent data corruption at its source.

This `Validator` class is both an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 and a managed attribute descriptor:

Copy

from abc import ABC, abstractmethod

class Validator(ABC):

    def \_\_set\_name\_\_(self, owner, name):
        self.private\_name \= '\_' + name

    def \_\_get\_\_(self, obj, objtype\=None):
        return getattr(obj, self.private\_name)

    def \_\_set\_\_(self, obj, value):
        self.validate(value)
        setattr(obj, self.private\_name, value)

    @abstractmethod
    def validate(self, value):
        pass

Custom validators need to inherit from `Validator` and must supply a `validate()` method to test various restrictions as needed.

### [Custom validators](https://docs.python.org/3/howto/descriptor.html#id10)
[¶](https://docs.python.org/3/howto/descriptor.html#custom-validators "Link to this heading")

Here are three practical data validation utilities:

1.  `OneOf` verifies that a value is one of a restricted set of options.
    
2.  `Number` verifies that a value is either an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     or [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
    . Optionally, it verifies that a value is between a given minimum or maximum.
    
3.  `String` verifies that a value is a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    . Optionally, it validates a given minimum or maximum length. It can validate a user-defined [predicate](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic))
     as well.
    

Copy

class OneOf(Validator):

    def \_\_init\_\_(self, \*options):
        self.options \= set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(
                f'Expected {value!r} to be one of {self.options!r}'
            )

class Number(Validator):

    def \_\_init\_\_(self, minvalue\=None, maxvalue\=None):
        self.minvalue \= minvalue
        self.maxvalue \= maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value \> self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )

class String(Validator):

    def \_\_init\_\_(self, minsize\=None, maxsize\=None, predicate\=None):
        self.minsize \= minsize
        self.maxsize \= maxsize
        self.predicate \= predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be a str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) \> self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )

### [Practical application](https://docs.python.org/3/howto/descriptor.html#id11)
[¶](https://docs.python.org/3/howto/descriptor.html#practical-application "Link to this heading")

Here’s how the data validators can be used in a real class:

Copy

class Component:

    name \= String(minsize\=3, maxsize\=10, predicate\=str.isupper)
    kind \= OneOf('wood', 'metal', 'plastic')
    quantity \= Number(minvalue\=0)

    def \_\_init\_\_(self, name, kind, quantity):
        self.name \= name
        self.kind \= kind
        self.quantity \= quantity

The descriptors prevent invalid instances from being created:

Copy

\>>> Component('Widget', 'metal', 5)      \# Blocked: 'Widget' is not all uppercase
Traceback (most recent call last):
    ...
ValueError: Expected <method 'isupper' of 'str' objects> to be true for 'Widget'

\>>> Component('WIDGET', 'metle', 5)      \# Blocked: 'metle' is misspelled
Traceback (most recent call last):
    ...
ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}

\>>> Component('WIDGET', 'metal', \-5)     \# Blocked: -5 is negative
Traceback (most recent call last):
    ...
ValueError: Expected -5 to be at least 0

\>>> Component('WIDGET', 'metal', 'V')    \# Blocked: 'V' isn't a number
Traceback (most recent call last):
    ...
TypeError: Expected 'V' to be an int or float

\>>> c \= Component('WIDGET', 'metal', 5)  \# Allowed:  The inputs are valid

[Technical Tutorial](https://docs.python.org/3/howto/descriptor.html#id12)
[¶](https://docs.python.org/3/howto/descriptor.html#technical-tutorial "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

What follows is a more technical tutorial for the mechanics and details of how descriptors work.

### [Abstract](https://docs.python.org/3/howto/descriptor.html#id13)
[¶](https://docs.python.org/3/howto/descriptor.html#abstract "Link to this heading")

Defines descriptors, summarizes the protocol, and shows how descriptors are called. Provides an example showing how object relational mappings work.

Learning about descriptors not only provides access to a larger toolset, it creates a deeper understanding of how Python works.

### [Definition and introduction](https://docs.python.org/3/howto/descriptor.html#id14)
[¶](https://docs.python.org/3/howto/descriptor.html#definition-and-introduction "Link to this heading")

In general, a descriptor is an attribute value that has one of the methods in the descriptor protocol. Those methods are [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
, [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
, and [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
. If any of those methods are defined for an attribute, it is said to be a [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
.

The default behavior for attribute access is to get, set, or delete the attribute from an object’s dictionary. For instance, `a.x` has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the method resolution order of `type(a)`. If the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined.

Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
. They are used throughout Python itself. Descriptors simplify the underlying C code and offer a flexible set of new tools for everyday Python programs.

### [Descriptor protocol](https://docs.python.org/3/howto/descriptor.html#id15)
[¶](https://docs.python.org/3/howto/descriptor.html#descriptor-protocol "Link to this heading")

`descr.__get__(self, obj, type=None)`

`descr.__set__(self, obj, value)`

`descr.__delete__(self, obj)`

That is all there is to it. Define any of these methods and an object is considered a descriptor and can override default behavior upon being looked up as an attribute.

If an object defines [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 or [`__delete__()`](https://docs.python.org/3/reference/datamodel.html#object.__delete__ "object.__delete__")
, it is considered a data descriptor. Descriptors that only define [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 are called non-data descriptors (they are often used for methods but other uses are possible).

Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary. If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence. If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

To make a read-only data descriptor, define both [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 and [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 with the `__set__()` raising an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 when called. Defining the `__set__()` method with an exception raising placeholder is enough to make it a data descriptor.

### [Overview of descriptor invocation](https://docs.python.org/3/howto/descriptor.html#id16)
[¶](https://docs.python.org/3/howto/descriptor.html#overview-of-descriptor-invocation "Link to this heading")

A descriptor can be called directly with `desc.__get__(obj)` or `desc.__get__(None, cls)`.

But it is more common for a descriptor to be invoked automatically from attribute access.

The expression `obj.x` looks up the attribute `x` in the chain of namespaces for `obj`. If the search finds a descriptor outside of the instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
, its [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method is invoked according to the precedence rules listed below.

The details of invocation depend on whether `obj` is an object, class, or instance of super.

### [Invocation from an instance](https://docs.python.org/3/howto/descriptor.html#id17)
[¶](https://docs.python.org/3/howto/descriptor.html#invocation-from-an-instance "Link to this heading")

Instance lookup scans through a chain of namespaces giving data descriptors the highest priority, followed by instance variables, then non-data descriptors, then class variables, and lastly [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 if it is provided.

If a descriptor is found for `a.x`, then it is invoked with: `desc.__get__(a, type(a))`.

The logic for a dotted lookup is in [`object.__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
. Here is a pure Python equivalent:

Copy

def find\_name\_in\_mro(cls, name, default):
    "Emulate \_PyType\_Lookup() in Objects/typeobject.c"
    for base in cls.\_\_mro\_\_:
        if name in vars(base):
            return vars(base)\[name\]
    return default

def object\_getattribute(obj, name):
    "Emulate PyObject\_GenericGetAttr() in Objects/object.c"
    null \= sentinel('null')
    objtype \= type(obj)
    cls\_var \= find\_name\_in\_mro(objtype, name, null)
    descr\_get \= getattr(type(cls\_var), '\_\_get\_\_', null)
    if descr\_get is not null:
        if (hasattr(type(cls\_var), '\_\_set\_\_')
            or hasattr(type(cls\_var), '\_\_delete\_\_')):
            return descr\_get(cls\_var, obj, objtype)     \# data descriptor
    if hasattr(obj, '\_\_dict\_\_') and name in vars(obj):
        return vars(obj)\[name\]                          \# instance variable
    if descr\_get is not null:
        return descr\_get(cls\_var, obj, objtype)         \# non-data descriptor
    if cls\_var is not null:
        return cls\_var                                  \# class variable
    raise AttributeError(name)

Note, there is no [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 hook in the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 code. That is why calling `__getattribute__()` directly or with `super().__getattribute__` will bypass `__getattr__()` entirely.

Instead, it is the dot operator and the [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 function that are responsible for invoking [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 whenever [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 raises an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
. Their logic is encapsulated in a helper function:

Copy

def getattr\_hook(obj, name):
    "Emulate slot\_tp\_getattr\_hook() in Objects/typeobject.c"
    try:
        return obj.\_\_getattribute\_\_(name)
    except AttributeError:
        if not hasattr(type(obj), '\_\_getattr\_\_'):
            raise
    return type(obj).\_\_getattr\_\_(obj, name)             \# \_\_getattr\_\_

### [Invocation from a class](https://docs.python.org/3/howto/descriptor.html#id18)
[¶](https://docs.python.org/3/howto/descriptor.html#invocation-from-a-class "Link to this heading")

The logic for a dotted lookup such as `A.x` is in `type.__getattribute__()`. The steps are similar to those for `object.__getattribute__()` but the instance dictionary lookup is replaced by a search through the class’s [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order)
.

If a descriptor is found, it is invoked with `desc.__get__(None, A)`.

The full C implementation can be found in `type_getattro()` and `_PyType_Lookup()` in [Objects/typeobject.c](https://github.com/python/cpython/tree/3.15/Objects/typeobject.c)
.

### [Invocation from super](https://docs.python.org/3/howto/descriptor.html#id19)
[¶](https://docs.python.org/3/howto/descriptor.html#invocation-from-super "Link to this heading")

The logic for super’s dotted lookup is in the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 method for object returned by [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
.

A dotted lookup such as `super(A, obj).m` searches `obj.__class__.__mro__` for the base class `B` immediately following `A` and then returns `B.__dict__['m'].__get__(obj, A)`. If not a descriptor, `m` is returned unchanged.

The full C implementation can be found in `super_getattro()` in [Objects/typeobject.c](https://github.com/python/cpython/tree/3.15/Objects/typeobject.c)
. A pure Python equivalent can be found in [Guido’s Tutorial](https://www.python.org/download/releases/2.2.3/descrintro/#cooperation)
.

### [Summary of invocation logic](https://docs.python.org/3/howto/descriptor.html#id20)
[¶](https://docs.python.org/3/howto/descriptor.html#summary-of-invocation-logic "Link to this heading")

The mechanism for descriptors is embedded in the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
 methods for [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
, and [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
.

The important points to remember are:

*   Descriptors are invoked by the [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
     method.
    
*   Classes inherit this machinery from [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
    , [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
    , or [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
    .
    
*   Overriding [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
     prevents automatic descriptor calls because all the descriptor logic is in that method.
    
*   `object.__getattribute__()` and `type.__getattribute__()` make different calls to [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
    . The first includes the instance and may include the class. The second puts in `None` for the instance and always includes the class.
    
*   Data descriptors always override instance dictionaries.
    
*   Non-data descriptors may be overridden by instance dictionaries.
    

### [Automatic name notification](https://docs.python.org/3/howto/descriptor.html#id21)
[¶](https://docs.python.org/3/howto/descriptor.html#automatic-name-notification "Link to this heading")

Sometimes it is desirable for a descriptor to know what class variable name it was assigned to. When a new class is created, the [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 metaclass scans the dictionary of the new class. If any of the entries are descriptors and if they define [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
, that method is called with two arguments. The _owner_ is the class where the descriptor is used, and the _name_ is the class variable the descriptor was assigned to.

The implementation details are in `type_new()` and `set_names()` in [Objects/typeobject.c](https://github.com/python/cpython/tree/3.15/Objects/typeobject.c)
.

Since the update logic is in `type.__new__()`, notifications only take place at the time of class creation. If descriptors are added to the class afterwards, [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
 will need to be called manually.

### [ORM example](https://docs.python.org/3/howto/descriptor.html#id22)
[¶](https://docs.python.org/3/howto/descriptor.html#orm-example "Link to this heading")

The following code is a simplified skeleton showing how data descriptors could be used to implement an [object relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
.

The essential idea is that the data is stored in an external database. The Python instances only hold keys to the database’s tables. Descriptors take care of lookups or updates:

Copy

class Field:

    def \_\_set\_name\_\_(self, owner, name):
        self.fetch \= f'SELECT {name} FROM {owner.table} WHERE {owner.key}\=?;'
        self.store \= f'UPDATE {owner.table} SET {name}\=? WHERE {owner.key}\=?;'

    def \_\_get\_\_(self, obj, objtype\=None):
        return conn.execute(self.fetch, \[obj.key\]).fetchone()\[0\]

    def \_\_set\_\_(self, obj, value):
        conn.execute(self.store, \[value, obj.key\])
        conn.commit()

We can use the `Field` class to define [models](https://en.wikipedia.org/wiki/Database_model)
 that describe the schema for each table in a database:

Copy

class Movie:
    table \= 'Movies'                    \# Table name
    key \= 'title'                       \# Primary key
    director \= Field()
    year \= Field()

    def \_\_init\_\_(self, key):
        self.key \= key

class Song:
    table \= 'Music'
    key \= 'title'
    artist \= Field()
    year \= Field()
    genre \= Field()

    def \_\_init\_\_(self, key):
        self.key \= key

To use the models, first connect to the database:

Copy

\>>> import sqlite3
\>>> conn \= sqlite3.connect('entertainment.db')

An interactive session shows how data is retrieved from the database and how it can be updated:

Copy

\>>> Movie('Star Wars').director
'George Lucas'
\>>> jaws \= Movie('Jaws')
\>>> f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

\>>> Song('Country Roads').artist
'John Denver'

\>>> Movie('Star Wars').director \= 'J.J. Abrams'
\>>> Movie('Star Wars').director
'J.J. Abrams'

[Pure Python Equivalents](https://docs.python.org/3/howto/descriptor.html#id23)
[¶](https://docs.python.org/3/howto/descriptor.html#pure-python-equivalents "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The descriptor protocol is simple and offers exciting possibilities. Several use cases are so common that they have been prepackaged into built-in tools. Properties, bound methods, static methods, class methods, and \_\_slots\_\_ are all based on the descriptor protocol.

### [Properties](https://docs.python.org/3/howto/descriptor.html#id24)
[¶](https://docs.python.org/3/howto/descriptor.html#properties "Link to this heading")

Calling [`property()`](https://docs.python.org/3/builtins/functions.html#property "property")
 is a succinct way of building a data descriptor that triggers a function call upon access to an attribute. Its signature is:

Copy

property(fget\=None, fset\=None, fdel\=None, doc\=None) \-> property

The documentation shows a typical use to define a managed attribute `x`:

Copy

class C:
    def getx(self): return self.\_\_x
    def setx(self, value): self.\_\_x \= value
    def delx(self): del self.\_\_x
    x \= property(getx, setx, delx, "I'm the 'x' property.")

To see how [`property()`](https://docs.python.org/3/builtins/functions.html#property "property")
 is implemented in terms of the descriptor protocol, here is a pure Python equivalent that implements most of the core functionality:

Copy

class Property:
    "Emulate PyProperty\_Type() in Objects/descrobject.c"

    def \_\_init\_\_(self, fget\=None, fset\=None, fdel\=None, doc\=None):
        self.fget \= fget
        self.fset \= fset
        self.fdel \= fdel
        if doc is None and fget is not None:
            doc \= fget.\_\_doc\_\_
        self.\_\_doc\_\_ \= doc

    def \_\_set\_name\_\_(self, owner, name):
        self.\_\_name\_\_ \= name

    def \_\_get\_\_(self, obj, objtype\=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def \_\_set\_\_(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def \_\_delete\_\_(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.\_\_doc\_\_)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.\_\_doc\_\_)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.\_\_doc\_\_)

The [`property()`](https://docs.python.org/3/builtins/functions.html#property "property")
 builtin helps whenever a user interface has granted attribute access and then subsequent changes require the intervention of a method.

For instance, a spreadsheet class may grant access to a cell value through `Cell('b10').value`. Subsequent improvements to the program require the cell to be recalculated on every access; however, the programmer does not want to affect existing client code accessing the attribute directly. The solution is to wrap access to the value attribute in a property data descriptor:

Copy

class Cell:
    ...

    @property
    def value(self):
        "Recalculate the cell before returning value"
        self.recalc()
        return self.\_value

Either the built-in [`property()`](https://docs.python.org/3/builtins/functions.html#property "property")
 or our `Property()` equivalent would work in this example.

### [Functions and methods](https://docs.python.org/3/howto/descriptor.html#id25)
[¶](https://docs.python.org/3/howto/descriptor.html#functions-and-methods "Link to this heading")

Python’s object oriented features are built upon a function based environment. Using non-data descriptors, the two are merged seamlessly.

Functions stored in class dictionaries get turned into methods when invoked. Methods only differ from regular functions in that the object instance is prepended to the other arguments. By convention, the instance is called _self_ but could be called _this_ or any other variable name.

Methods can be created manually with [`types.MethodType`](https://docs.python.org/3/library/types.html#types.MethodType "types.MethodType")
 which is roughly equivalent to:

Copy

class MethodType:
    "Emulate PyMethod\_Type in Objects/classobject.c"

    def \_\_init\_\_(self, func, obj):
        self.\_\_func\_\_ \= func
        self.\_\_self\_\_ \= obj

    def \_\_call\_\_(self, \*args, \*\*kwargs):
        func \= self.\_\_func\_\_
        obj \= self.\_\_self\_\_
        return func(obj, \*args, \*\*kwargs)

    def \_\_getattribute\_\_(self, name):
        "Emulate method\_getset() in Objects/classobject.c"
        if name \== '\_\_doc\_\_':
            return self.\_\_func\_\_.\_\_doc\_\_
        return object.\_\_getattribute\_\_(self, name)

    def \_\_getattr\_\_(self, name):
        "Emulate method\_getattro() in Objects/classobject.c"
        return getattr(self.\_\_func\_\_, name)

    def \_\_get\_\_(self, obj, objtype\=None):
        "Emulate method\_descr\_get() in Objects/classobject.c"
        return self

To support automatic creation of methods, functions include the [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method for binding methods during attribute access. This means that functions are non-data descriptors that return bound methods during dotted lookup from an instance. Here’s how it works:

Copy

class Function:
    ...

    def \_\_get\_\_(self, obj, objtype\=None):
        "Simulate func\_descr\_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return MethodType(self, obj)

Running the following class in the interpreter shows how the function descriptor works in practice:

Copy

class D:
    def f(self):
         return self

class D2:
    pass

The function has a [qualified name](https://docs.python.org/3/glossary.html#term-qualified-name)
 attribute to support introspection:

Copy

\>>> D.f.\_\_qualname\_\_
'D.f'

Accessing the function through the class dictionary does not invoke [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
. Instead, it just returns the underlying function object:

Copy

\>>> D.\_\_dict\_\_\['f'\]
<function D.f at 0x00C45070>

Dotted access from a class calls [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 which just returns the underlying function unchanged:

Copy

\>>> D.f
<function D.f at 0x00C45070>

The interesting behavior occurs during dotted access from an instance. The dotted lookup calls [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 which returns a bound method object:

Copy

\>>> d \= D()
\>>> d.f
<bound method D.f of <\_\_main\_\_.D object at 0x00B18C90>>

Internally, the bound method stores the underlying function and the bound instance:

Copy

\>>> d.f.\_\_func\_\_
<function D.f at 0x00C45070>

\>>> d.f.\_\_self\_\_
<\_\_main\_\_.D object at 0x00B18C90>

If you have ever wondered where _self_ comes from in regular methods or where _cls_ comes from in class methods, this is it!

### [Kinds of methods](https://docs.python.org/3/howto/descriptor.html#id26)
[¶](https://docs.python.org/3/howto/descriptor.html#kinds-of-methods "Link to this heading")

Non-data descriptors provide a simple mechanism for variations on the usual patterns of binding functions into methods.

To recap, functions have a [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 method so that they can be converted to a method when accessed as attributes. The non-data descriptor transforms an `obj.f(*args)` call into `f(obj, *args)`. Calling `cls.f(*args)` becomes `f(*args)`.

This chart summarizes the binding and its two most useful variants:

> | Transformation | Called from an object | Called from a class |
> | --- | --- | --- |
> | function | f(obj, \*args) | f(\*args) |
> | staticmethod | f(\*args) | f(\*args) |
> | classmethod | f(type(obj), \*args) | f(cls, \*args) |

### [Static methods](https://docs.python.org/3/howto/descriptor.html#id27)
[¶](https://docs.python.org/3/howto/descriptor.html#static-methods "Link to this heading")

Static methods return the underlying function without changes. Calling either `c.f` or `C.f` is the equivalent of a direct lookup into `object.__getattribute__(c, "f")` or `object.__getattribute__(C, "f")`. As a result, the function becomes identically accessible from either an object or a class.

Good candidates for static methods are methods that do not reference the `self` variable.

For instance, a statistics package may include a container class for experimental data. The class provides normal methods for computing the average, mean, median, and other descriptive statistics that depend on the data. However, there may be useful functions which are conceptually related but do not depend on the data. For instance, `erf(x)` is handy conversion routine that comes up in statistical work but does not directly depend on a particular dataset. It can be called either from an object or the class: `s.erf(1.5) --> 0.9332` or `Sample.erf(1.5) --> 0.9332`.

Since static methods return the underlying function with no changes, the example calls are unexciting:

Copy

class E:
    @staticmethod
    def f(x):
        return x \* 10

Copy

\>>> E.f(3)
30
\>>> E().f(3)
30

Using the non-data descriptor protocol, a pure Python version of [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 would look like this:

Copy

import functools

class StaticMethod:
    "Emulate PyStaticMethod\_Type() in Objects/funcobject.c"

    def \_\_init\_\_(self, f):
        self.f \= f
        functools.update\_wrapper(self, f)

    def \_\_get\_\_(self, obj, objtype\=None):
        return self.f

    def \_\_call\_\_(self, \*args, \*\*kwds):
        return self.f(\*args, \*\*kwds)

    @property
    def \_\_annotations\_\_(self):
        return self.f.\_\_annotations\_\_

The [`functools.update_wrapper()`](https://docs.python.org/3/library/functools.html#functools.update_wrapper "functools.update_wrapper")
 call adds a `__wrapped__` attribute that refers to the underlying function. Also it carries forward the attributes necessary to make the wrapper look like the wrapped function, including [`__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__")
, [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__")
, and [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")
.

### [Class methods](https://docs.python.org/3/howto/descriptor.html#id28)
[¶](https://docs.python.org/3/howto/descriptor.html#class-methods "Link to this heading")

Unlike static methods, class methods prepend the class reference to the argument list before calling the function. This format is the same for whether the caller is an object or a class:

Copy

class F:
    @classmethod
    def f(cls, x):
        return cls.\_\_name\_\_, x

Copy

\>>> F.f(3)
('F', 3)
\>>> F().f(3)
('F', 3)

This behavior is useful whenever the method only needs to have a class reference and does not rely on data stored in a specific instance. One use for class methods is to create alternate class constructors. For example, the classmethod [`dict.fromkeys()`](https://docs.python.org/3/builtins/stdtypes.html#dict.fromkeys "dict.fromkeys")
 creates a new dictionary from a list of keys. The pure Python equivalent is:

Copy

class Dict(dict):
    @classmethod
    def fromkeys(cls, iterable, value\=None):
        "Emulate dict\_fromkeys() in Objects/dictobject.c"
        d \= cls()
        for key in iterable:
            d\[key\] \= value
        return d

Now a new dictionary of unique keys can be constructed like this:

Copy

\>>> d \= Dict.fromkeys('abracadabra')
\>>> type(d) is Dict
True
\>>> d
{'a': None, 'b': None, 'r': None, 'c': None, 'd': None}

Using the non-data descriptor protocol, a pure Python version of [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 would look like this:

Copy

import functools

class ClassMethod:
    "Emulate PyClassMethod\_Type() in Objects/funcobject.c"

    def \_\_init\_\_(self, f):
        self.f \= f
        functools.update\_wrapper(self, f)

    def \_\_get\_\_(self, obj, cls\=None):
        if cls is None:
            cls \= type(obj)
        return MethodType(self.f, cls)

The [`functools.update_wrapper()`](https://docs.python.org/3/library/functools.html#functools.update_wrapper "functools.update_wrapper")
 call in `ClassMethod` adds a `__wrapped__` attribute that refers to the underlying function. Also it carries forward the attributes necessary to make the wrapper look like the wrapped function: [`__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__")
, [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__")
, [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")
, and [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#function.__annotations__ "function.__annotations__")
.

### [Member objects and \_\_slots\_\_](https://docs.python.org/3/howto/descriptor.html#id29)
[¶](https://docs.python.org/3/howto/descriptor.html#member-objects-and-slots "Link to this heading")

When a class defines `__slots__`, it replaces instance dictionaries with a fixed-length array of slot values. From a user point of view that has several effects:

1\. Provides immediate detection of bugs due to misspelled attribute assignments. Only attribute names specified in `__slots__` are allowed:

Copy

class Vehicle:
    \_\_slots\_\_ \= ('id\_number', 'make', 'model')

Copy

\>>> auto \= Vehicle()
\>>> auto.id\_nubmer \= 'VYE483814LQEX'
Traceback (most recent call last):
    ...
AttributeError: 'Vehicle' object has no attribute 'id\_nubmer'

2\. Helps create immutable objects where descriptors manage access to private attributes stored in `__slots__`:

Copy

class Immutable:

    \_\_slots\_\_ \= ('\_dept', '\_name')          \# Replace the instance dictionary

    def \_\_init\_\_(self, dept, name):
        self.\_dept \= dept                   \# Store to private attribute
        self.\_name \= name                   \# Store to private attribute

    @property                               \# Read-only descriptor
    def dept(self):
        return self.\_dept

    @property
    def name(self):                         \# Read-only descriptor
        return self.\_name

Copy

\>>> mark \= Immutable('Botany', 'Mark Watney')
\>>> mark.dept
'Botany'
\>>> mark.dept \= 'Space Pirate'
Traceback (most recent call last):
    ...
AttributeError: property 'dept' of 'Immutable' object has no setter
\>>> mark.location \= 'Mars'
Traceback (most recent call last):
    ...
AttributeError: 'Immutable' object has no attribute 'location'

3\. Saves memory. On a 64-bit Linux build, an instance with two attributes takes 48 bytes with `__slots__` and 152 bytes without. This [flyweight design pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
 likely only matters when a large number of instances are going to be created.

4\. Improves speed. Reading instance variables is 35% faster with `__slots__` (as measured with Python 3.10 on an Apple M1 processor).

5\. Blocks tools like [`@functools.cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property "functools.cached_property")
 which require an instance dictionary to function correctly:

Copy

from functools import cached\_property

class CP:
    \_\_slots\_\_ \= ()                          \# Eliminates the instance dict

    @cached\_property                        \# Requires an instance dict
    def pi(self):
        return 4 \* sum((\-1.0)\*\*n / (2.0\*n + 1.0)
                       for n in reversed(range(100\_000)))

Copy

\>>> CP().pi
Traceback (most recent call last):
  ...
TypeError: No '\_\_dict\_\_' attribute on 'CP' instance to cache 'pi' property.

It is not possible to create an exact drop-in pure Python version of `__slots__` because it requires direct access to C structures and control over object memory allocation. However, we can build a mostly faithful simulation where the actual C structure for slots is emulated by a private `_slotvalues` list. Reads and writes to that private structure are managed by member descriptors:

Copy

null \= sentinel('null')

class Member:

    def \_\_init\_\_(self, name, clsname, offset):
        'Emulate PyMemberDef in Include/descrobject.h'
        \# Also see descr\_new() in Objects/descrobject.c
        self.name \= name
        self.clsname \= clsname
        self.offset \= offset

    def \_\_get\_\_(self, obj, objtype\=None):
        'Emulate member\_get() in Objects/descrobject.c'
        \# Also see PyMember\_GetOne() in Python/structmember.c
        if obj is None:
            return self
        value \= obj.\_slotvalues\[self.offset\]
        if value is null:
            raise AttributeError(self.name)
        return value

    def \_\_set\_\_(self, obj, value):
        'Emulate member\_set() in Objects/descrobject.c'
        obj.\_slotvalues\[self.offset\] \= value

    def \_\_delete\_\_(self, obj):
        'Emulate member\_delete() in Objects/descrobject.c'
        value \= obj.\_slotvalues\[self.offset\]
        if value is null:
            raise AttributeError(self.name)
        obj.\_slotvalues\[self.offset\] \= null

    def \_\_repr\_\_(self):
        'Emulate member\_repr() in Objects/descrobject.c'
        return f'<Member {self.name!r} of {self.clsname!r}\>'

The `type.__new__()` method takes care of adding member objects to class variables:

Copy

class Type(type):
    'Simulate how the type metaclass adds member objects for slots'

    def \_\_new\_\_(mcls, clsname, bases, mapping, \*\*kwargs):
        'Emulate type\_new() in Objects/typeobject.c'
        \# type\_new() calls PyType\_Ready() which calls add\_methods()
        slot\_names \= mapping.get('slot\_names', \[\])
        for offset, name in enumerate(slot\_names):
            mapping\[name\] \= Member(name, clsname, offset)
        return type.\_\_new\_\_(mcls, clsname, bases, mapping, \*\*kwargs)

The [`object.__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 method takes care of creating instances that have slots instead of an instance dictionary. Here is a rough simulation in pure Python:

Copy

class Object:
    'Simulate how object.\_\_new\_\_() allocates memory for \_\_slots\_\_'

    def \_\_new\_\_(cls, \*args, \*\*kwargs):
        'Emulate object\_new() in Objects/typeobject.c'
        inst \= super().\_\_new\_\_(cls)
        if hasattr(cls, 'slot\_names'):
            empty\_slots \= \[null\] \* len(cls.slot\_names)
            object.\_\_setattr\_\_(inst, '\_slotvalues', empty\_slots)
        return inst

    def \_\_setattr\_\_(self, name, value):
        'Emulate \_PyObject\_GenericSetAttrWithDict() Objects/object.c'
        cls \= type(self)
        if hasattr(cls, 'slot\_names') and name not in cls.slot\_names:
            raise AttributeError(
                f'{cls.\_\_name\_\_!r} object has no attribute {name!r}'
            )
        super().\_\_setattr\_\_(name, value)

    def \_\_delattr\_\_(self, name):
        'Emulate \_PyObject\_GenericSetAttrWithDict() Objects/object.c'
        cls \= type(self)
        if hasattr(cls, 'slot\_names') and name not in cls.slot\_names:
            raise AttributeError(
                f'{cls.\_\_name\_\_!r} object has no attribute {name!r}'
            )
        super().\_\_delattr\_\_(name)

To use the simulation in a real class, just inherit from `Object` and set the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)
 to `Type`:

Copy

class H(Object, metaclass\=Type):
    'Instance variables stored in slots'

    slot\_names \= \['x', 'y'\]

    def \_\_init\_\_(self, x, y):
        self.x \= x
        self.y \= y

At this point, the metaclass has loaded member objects for _x_ and _y_:

Copy

\>>> from pprint import pp
\>>> pp(dict(vars(H)))
{'\_\_module\_\_': '\_\_main\_\_',
 '\_\_doc\_\_': 'Instance variables stored in slots',
 'slot\_names': \['x', 'y'\],
 '\_\_init\_\_': <function H.\_\_init\_\_ at 0x7fb5d302f9d0>,
 'x': <Member 'x' of 'H'>,
 'y': <Member 'y' of 'H'>}

When instances are created, they have a `_slotvalues` list where the attributes are stored:

Copy

\>>> h \= H(10, 20)
\>>> vars(h)
{'\_slotvalues': \[10, 20\]}
\>>> h.x \= 55
\>>> vars(h)
{'\_slotvalues': \[55, 20\]}

Misspelled or unassigned attributes will raise an exception:

Copy

\>>> h.xz
Traceback (most recent call last):
    ...
AttributeError: 'H' object has no attribute 'xz'

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html#)
    *   [Primer](https://docs.python.org/3/howto/descriptor.html#primer)
        *   [Simple example: A descriptor that returns a constant](https://docs.python.org/3/howto/descriptor.html#simple-example-a-descriptor-that-returns-a-constant)
            
        *   [Dynamic lookups](https://docs.python.org/3/howto/descriptor.html#dynamic-lookups)
            
        *   [Managed attributes](https://docs.python.org/3/howto/descriptor.html#managed-attributes)
            
        *   [Customized names](https://docs.python.org/3/howto/descriptor.html#customized-names)
            
        *   [Closing thoughts](https://docs.python.org/3/howto/descriptor.html#closing-thoughts)
            
    *   [Complete Practical Example](https://docs.python.org/3/howto/descriptor.html#complete-practical-example)
        *   [Validator class](https://docs.python.org/3/howto/descriptor.html#validator-class)
            
        *   [Custom validators](https://docs.python.org/3/howto/descriptor.html#custom-validators)
            
        *   [Practical application](https://docs.python.org/3/howto/descriptor.html#practical-application)
            
    *   [Technical Tutorial](https://docs.python.org/3/howto/descriptor.html#technical-tutorial)
        *   [Abstract](https://docs.python.org/3/howto/descriptor.html#abstract)
            
        *   [Definition and introduction](https://docs.python.org/3/howto/descriptor.html#definition-and-introduction)
            
        *   [Descriptor protocol](https://docs.python.org/3/howto/descriptor.html#descriptor-protocol)
            
        *   [Overview of descriptor invocation](https://docs.python.org/3/howto/descriptor.html#overview-of-descriptor-invocation)
            
        *   [Invocation from an instance](https://docs.python.org/3/howto/descriptor.html#invocation-from-an-instance)
            
        *   [Invocation from a class](https://docs.python.org/3/howto/descriptor.html#invocation-from-a-class)
            
        *   [Invocation from super](https://docs.python.org/3/howto/descriptor.html#invocation-from-super)
            
        *   [Summary of invocation logic](https://docs.python.org/3/howto/descriptor.html#summary-of-invocation-logic)
            
        *   [Automatic name notification](https://docs.python.org/3/howto/descriptor.html#automatic-name-notification)
            
        *   [ORM example](https://docs.python.org/3/howto/descriptor.html#orm-example)
            
    *   [Pure Python Equivalents](https://docs.python.org/3/howto/descriptor.html#pure-python-equivalents)
        *   [Properties](https://docs.python.org/3/howto/descriptor.html#properties)
            
        *   [Functions and methods](https://docs.python.org/3/howto/descriptor.html#functions-and-methods)
            
        *   [Kinds of methods](https://docs.python.org/3/howto/descriptor.html#kinds-of-methods)
            
        *   [Static methods](https://docs.python.org/3/howto/descriptor.html#static-methods)
            
        *   [Class methods](https://docs.python.org/3/howto/descriptor.html#class-methods)
            
        *   [Member objects and \_\_slots\_\_](https://docs.python.org/3/howto/descriptor.html#member-objects-and-slots)
            

#### Previous topic

[Curses Programming with Python](https://docs.python.org/3/howto/curses.html "previous chapter")

#### Next topic

[Debugging C API extensions and CPython Internals with GDB](https://docs.python.org/3/howto/gdb_helpers.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Descriptor+Guide&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fdescriptor.html&pagesource=howto%2Fdescriptor.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/descriptor.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/gdb_helpers.html "Debugging C API extensions and CPython Internals with GDB")
     |
*   [previous](https://docs.python.org/3/howto/curses.html "Curses Programming with Python")
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
*   [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html)
    
*    
    
    |
*   Theme Auto Light Dark |