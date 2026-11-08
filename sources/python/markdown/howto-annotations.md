### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/isolating-extensions.html "Isolating Extension Modules")
     |
*   [previous](https://docs.python.org/3/howto/perf_profiling.html "Python support for the perf map compatible profilers")
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
*   [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Annotations Best Practices[¶](https://docs.python.org/3/howto/annotations.html#annotations-best-practices "Link to this heading")

==================================================================================================================================

Accessing The Annotations Dict Of An Object In Python 3.10 And Newer[¶](https://docs.python.org/3/howto/annotations.html#accessing-the-annotations-dict-of-an-object-in-python-3-10-and-newer "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python 3.10 adds a new function to the standard library: [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
. In Python versions 3.10 through 3.13, calling this function is the best practice for accessing the annotations dict of any object that supports annotations. This function can also “un-stringize” stringized annotations for you.

In Python 3.14, there is a new [`annotationlib`](https://docs.python.org/3/library/annotationlib.html#module-annotationlib "annotationlib: Functionality for introspecting annotations")
 module with functionality for working with annotations. This includes a [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
 function, which supersedes [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
.

If for some reason [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
 isn’t viable for your use case, you may access the `__annotations__` data member manually. Best practice for this changed in Python 3.10 as well: as of Python 3.10, `o.__annotations__` is guaranteed to _always_ work on Python functions, classes, and modules. If you’re certain the object you’re examining is one of these three _specific_ objects, you may simply use `o.__annotations__` to get at the object’s annotations dict.

However, other types of callables–for example, callables created by [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
–may not have an `__annotations__` attribute defined. When accessing the `__annotations__` of a possibly unknown object, best practice in Python versions 3.10 and newer is to call [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 with three arguments, for example `getattr(o, '__annotations__', None)`.

Before Python 3.10, accessing `__annotations__` on a class that defines no annotations but that has a parent class with annotations would return the parent’s `__annotations__`. In Python 3.10 and newer, the child class’s annotations will be an empty dict instead.

Accessing The Annotations Dict Of An Object In Python 3.9 And Older[¶](https://docs.python.org/3/howto/annotations.html#accessing-the-annotations-dict-of-an-object-in-python-3-9-and-older "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Python 3.9 and older, accessing the annotations dict of an object is much more complicated than in newer versions. The problem is a design flaw in these older versions of Python, specifically to do with class annotations.

Best practice for accessing the annotations dict of other objects–functions, other callables, and modules–is the same as best practice for 3.10, assuming you aren’t calling [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
: you should use three-argument [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 to access the object’s `__annotations__` attribute.

Unfortunately, this isn’t best practice for classes. The problem is that, since `__annotations__` is optional on classes, and because classes can inherit attributes from their base classes, accessing the `__annotations__` attribute of a class may inadvertently return the annotations dict of a _base class._ As an example:

Copy

class Base:
    a: int \= 3
    b: str \= 'abc'

class Derived(Base):
    pass

print(Derived.\_\_annotations\_\_)

This will print the annotations dict from `Base`, not `Derived`.

Your code will have to have a separate code path if the object you’re examining is a class (`isinstance(o, type)`). In that case, best practice relies on an implementation detail of Python 3.9 and before: if a class has annotations defined, they are stored in the class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
 dictionary. Since the class may or may not have annotations defined, best practice is to call the [`get()`](https://docs.python.org/3/builtins/stdtypes.html#dict.get "dict.get")
 method on the class dict.

To put it all together, here is some sample code that safely accesses the `__annotations__` attribute on an arbitrary object in Python 3.9 and before:

Copy

if isinstance(o, type):
    ann \= o.\_\_dict\_\_.get('\_\_annotations\_\_', None)
else:
    ann \= getattr(o, '\_\_annotations\_\_', None)

After running this code, `ann` should be either a dictionary or `None`. You’re encouraged to double-check the type of `ann` using [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 before further examination.

Note that some exotic or malformed type objects may not have a [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
 attribute, so for extra safety you may also wish to use [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 to access `__dict__`.

Manually Un-Stringizing Stringized Annotations[¶](https://docs.python.org/3/howto/annotations.html#manually-un-stringizing-stringized-annotations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In situations where some annotations may be “stringized”, and you wish to evaluate those strings to produce the Python values they represent, it really is best to call [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
 to do this work for you.

If you’re using Python 3.9 or older, or if for some reason you can’t use [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
, you’ll need to duplicate its logic. You’re encouraged to examine the implementation of `inspect.get_annotations()` in the current Python version and follow a similar approach.

In a nutshell, if you wish to evaluate a stringized annotation on an arbitrary object `o`:

*   If `o` is a module, use `o.__dict__` as the `globals` when calling [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
    .
    
*   If `o` is a class, use `sys.modules[o.__module__].__dict__` as the `globals`, and `dict(vars(o))` as the `locals`, when calling [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
    .
    
*   If `o` is a wrapped callable using [`functools.update_wrapper()`](https://docs.python.org/3/library/functools.html#functools.update_wrapper "functools.update_wrapper")
    , [`@functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps "functools.wraps")
    , or [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
    , iteratively unwrap it by accessing either `o.__wrapped__` or `o.func` as appropriate, until you have found the root unwrapped function.
    
*   If `o` is a callable (but not a class), use [`o.__globals__`](https://docs.python.org/3/reference/datamodel.html#function.__globals__ "function.__globals__")
     as the globals when calling [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
    .
    

However, not all string values used as annotations can be successfully turned into Python values by [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
. String values could theoretically contain any valid string, and in practice there are valid use cases for type hints that require annotating with string values that specifically _can’t_ be evaluated. For example:

*   [**PEP 604**](https://peps.python.org/pep-0604/)
     union types using `|`, before support for this was added to Python 3.10.
    
*   Definitions that aren’t needed at runtime, only imported when [`typing.TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING "typing.TYPE_CHECKING")
     is true.
    

If [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 attempts to evaluate such values, it will fail and raise an exception. So, when designing a library API that works with annotations, it’s recommended to only attempt to evaluate string values when explicitly requested to by the caller.

Best Practices For `__annotations__` In Any Python Version[¶](https://docs.python.org/3/howto/annotations.html#best-practices-for-annotations-in-any-python-version "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   You should avoid assigning to the `__annotations__` member of objects directly. Let Python manage setting `__annotations__`.
    
*   If you do assign directly to the `__annotations__` member of an object, you should always set it to a `dict` object.
    
*   You should avoid accessing `__annotations__` directly on any object. Instead, use [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
     (Python 3.14+) or [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
     (Python 3.10+).
    
*   If you do directly access the `__annotations__` member of an object, you should ensure that it’s a dictionary before attempting to examine its contents.
    
*   You should avoid modifying `__annotations__` dicts.
    
*   You should avoid deleting the `__annotations__` attribute of an object.
    

`__annotations__` Quirks[¶](https://docs.python.org/3/howto/annotations.html#annotations-quirks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

In all versions of Python 3, function objects lazy-create an annotations dict if no annotations are defined on that object. You can delete the `__annotations__` attribute using `del fn.__annotations__`, but if you then access `fn.__annotations__` the object will create a new empty dict that it will store and return as its annotations. Deleting the annotations on a function before it has lazily created its annotations dict will throw an `AttributeError`; using `del fn.__annotations__` twice in a row is guaranteed to always throw an `AttributeError`.

Everything in the above paragraph also applies to class and module objects in Python 3.10 and newer.

In all versions of Python 3, you can set `__annotations__` on a function object to `None`. However, subsequently accessing the annotations on that object using `fn.__annotations__` will lazy-create an empty dictionary as per the first paragraph of this section. This is _not_ true of modules and classes, in any Python version; those objects permit setting `__annotations__` to any Python value, and will retain whatever value is set.

If Python stringizes your annotations for you (using `from __future__ import annotations`), and you specify a string as an annotation, the string will itself be quoted. In effect the annotation is quoted _twice._ For example:

Copy

from \_\_future\_\_ import annotations
def foo(a: "str"): pass

print(foo.\_\_annotations\_\_)

This prints `{'a': "'str'"}`. This shouldn’t really be considered a “quirk”; it’s mentioned here simply because it might be surprising.

If you use a class with a custom metaclass and access `__annotations__` on the class, you may observe unexpected behavior; see [**749**](https://peps.python.org/pep-0749/#pep749-metaclasses)
 for some examples. You can avoid these quirks by using [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
 on Python 3.14+ or [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
 on Python 3.10+.

Note

On Python 3.14 and later, annotations are evaluated lazily (see [**PEP 649**](https://peps.python.org/pep-0649/)
 and [**PEP 749**](https://peps.python.org/pep-0749/)
), and how the annotations dict is stored in the class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
 is a private implementation detail. Reading `cls.__dict__.get('__annotations__', None)` may therefore return `None` even when the class has annotations. On these versions, always use [`annotationlib.get_annotations()`](https://docs.python.org/3/library/annotationlib.html#annotationlib.get_annotations "annotationlib.get_annotations")
 (or [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations")
) rather than accessing `__dict__` directly.

Only on Python 3.9 and earlier, where neither function is available, can you avoid these bugs by reading the annotations from the class’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
 (for example, `cls.__dict__.get('__annotations__', None)`).

In some versions of Python, instances of classes may have an `__annotations__` attribute. However, this is not supported functionality. If you need the annotations of an instance, you can use [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
 to access its class (for example, `annotationlib.get_annotations(type(myinstance))` on Python 3.14+).

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#)
    *   [Accessing The Annotations Dict Of An Object In Python 3.10 And Newer](https://docs.python.org/3/howto/annotations.html#accessing-the-annotations-dict-of-an-object-in-python-3-10-and-newer)
        
    *   [Accessing The Annotations Dict Of An Object In Python 3.9 And Older](https://docs.python.org/3/howto/annotations.html#accessing-the-annotations-dict-of-an-object-in-python-3-9-and-older)
        
    *   [Manually Un-Stringizing Stringized Annotations](https://docs.python.org/3/howto/annotations.html#manually-un-stringizing-stringized-annotations)
        
    *   [Best Practices For `__annotations__` In Any Python Version](https://docs.python.org/3/howto/annotations.html#best-practices-for-annotations-in-any-python-version)
        
    *   [`__annotations__` Quirks](https://docs.python.org/3/howto/annotations.html#annotations-quirks)
        

#### Previous topic

[Python support for the `perf map` compatible profilers](https://docs.python.org/3/howto/perf_profiling.html "previous chapter")

#### Next topic

[Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Annotations+Best+Practices&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fannotations.html&pagesource=howto%2Fannotations.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/annotations.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/isolating-extensions.html "Isolating Extension Modules")
     |
*   [previous](https://docs.python.org/3/howto/perf_profiling.html "Python support for the perf map compatible profilers")
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
*   [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html)
    
*    
    
    |
*   Theme Auto Light Dark |