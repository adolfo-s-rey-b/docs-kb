### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/unittest.mock-examples.html "unittest.mock — getting started")
     |
*   [previous](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework")
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
*   [Development Tools](https://docs.python.org/3/library/development.html)
     »
*   [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`unittest.mock` — mock object library[¶](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock "Link to this heading")

===========================================================================================================================================

Added in version 3.3.

**Source code:** [Lib/unittest/mock.py](https://github.com/python/cpython/tree/3.15/Lib/unittest/mock.py)

* * *

`unittest.mock` is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

`unittest.mock` provides a core [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Additionally, mock provides a [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 decorator that handles patching module and class level attributes within the scope of a test, along with [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 for creating unique objects. See the [quick guide](https://docs.python.org/3/library/unittest.mock.html#quick-guide)
 for some examples of how to use [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
, [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 and `patch()`.

Mock is designed for use with [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
 and is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks.

There is a backport of `unittest.mock` for earlier versions of Python, available as [mock](https://pypi.org/project/mock/)
 on PyPI.

Quick Guide[¶](https://docs.python.org/3/library/unittest.mock.html#quick-guide "Link to this heading")

--------------------------------------------------------------------------------------------------------

[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 and [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 objects create all attributes and methods as you access them and store details of how they have been used. You can configure them, to specify return values or limit what attributes are available, and then make assertions about how they have been used:

Copy

\>>> from unittest.mock import MagicMock
\>>> thing \= ProductionClass()
\>>> thing.method \= MagicMock(return\_value\=3)
\>>> thing.method(3, 4, 5, key\='value')
3
\>>> thing.method.assert\_called\_with(3, 4, 5, key\='value')

[`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 allows you to perform side effects, including raising an exception when a mock is called:

Copy

\>>> from unittest.mock import Mock
\>>> mock \= Mock(side\_effect\=KeyError('foo'))
\>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'

Copy

\>>> values \= {'a': 1, 'b': 2, 'c': 3}
\>>> def side\_effect(arg):
...     return values\[arg\]
...
\>>> mock.side\_effect \= side\_effect
\>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
\>>> mock.side\_effect \= \[5, 4, 3, 2, 1\]
\>>> mock(), mock(), mock()
(5, 4, 3)

Mock has many other ways you can configure it and control its behaviour. For example the _spec_ argument configures the mock to take its specification from another object. Attempting to access attributes or methods on the mock that don’t exist on the spec will fail with an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

The [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 decorator / context manager makes it easy to mock classes or objects in a module under test. The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends:

Copy

\>>> from unittest.mock import patch
\>>> @patch('module.ClassName2')
... @patch('module.ClassName1')
... def test(MockClass1, MockClass2):
...     module.ClassName1()
...     module.ClassName2()
...     assert MockClass1 is module.ClassName1
...     assert MockClass2 is module.ClassName2
...     assert MockClass1.called
...     assert MockClass2.called
...
\>>> test()

Note

When you nest patch decorators the mocks are passed in to the decorated function in the same order they applied (the normal _Python_ order that decorators are applied). This means from the bottom up, so in the example above the mock for `module.ClassName1` is passed in first.

With [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 it matters that you patch objects in the namespace where they are looked up. This is normally straightforward, but for a quick guide read [where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
.

As well as a decorator [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 can be used as a context manager in a with statement:

Copy

\>>> with patch.object(ProductionClass, 'method', return\_value\=None) as mock\_method:
...     thing \= ProductionClass()
...     thing.method(1, 2, 3)
...
\>>> mock\_method.assert\_called\_once\_with(1, 2, 3)

There is also [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 for setting values in a dictionary just during a scope and restoring the dictionary to its original state when the test ends:

Copy

\>>> foo \= {'key': 'value'}
\>>> original \= foo.copy()
\>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear\=True):
...     assert foo \== {'newkey': 'newvalue'}
...
\>>> assert foo \== original

Mock supports the mocking of Python [magic methods](https://docs.python.org/3/library/unittest.mock.html#magic-methods)
. The easiest way of using magic methods is with the [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 class. It allows you to do things like:

Copy

\>>> mock \= MagicMock()
\>>> mock.\_\_str\_\_.return\_value \= 'foobarbaz'
\>>> str(mock)
'foobarbaz'
\>>> mock.\_\_str\_\_.assert\_called\_with()

Mock allows you to assign functions (or other Mock instances) to magic methods and they will be called appropriately. The [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 class is just a Mock variant that has all of the magic methods pre-created for you (well, all the useful ones anyway).

The following is an example of using magic methods with the ordinary Mock class:

Copy

\>>> mock \= Mock()
\>>> mock.\_\_str\_\_ \= Mock(return\_value\='wheeeeee')
\>>> str(mock)
'wheeeeee'

For ensuring that the mock objects in your tests have the same api as the objects they are replacing, you can use [auto-speccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
. Auto-speccing can be done through the _autospec_ argument to patch, or the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")
 function. Auto-speccing creates mock objects that have the same attributes and methods as the objects they are replacing, and any functions and methods (including constructors) have the same call signature as the real object.

This ensures that your mocks will fail in the same way as your production code if they are used incorrectly:

Copy

\>>> from unittest.mock import create\_autospec
\>>> def function(a, b, c):
...     pass
...
\>>> mock\_function \= create\_autospec(function, return\_value\='fishy')
\>>> mock\_function(1, 2, 3)
'fishy'
\>>> mock\_function.assert\_called\_once\_with(1, 2, 3)
\>>> mock\_function('wrong arguments')
Traceback (most recent call last):
 ...
TypeError: missing a required argument: 'b'

[`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")
 can also be used on classes, where it copies the signature of the `__init__` method, and on callable objects where it copies the signature of the `__call__` method.

The Mock Class[¶](https://docs.python.org/3/library/unittest.mock.html#the-mock-class "Link to this heading")

--------------------------------------------------------------------------------------------------------------

[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 is a flexible mock object intended to replace the use of stubs and test doubles throughout your code. Mocks are callable and create attributes as new mocks when you access them [\[1\]](https://docs.python.org/3/library/unittest.mock.html#id3)
. Accessing the same attribute will always return the same mock. Mocks record how you use them, allowing you to make assertions about what your code has done to them.

[`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 is a subclass of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 with all the magic methods pre-created and ready to use. There are also non-callable variants, useful when you are mocking out objects that aren’t callable: [`NonCallableMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "unittest.mock.NonCallableMock")
 and [`NonCallableMagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "unittest.mock.NonCallableMagicMock")

The [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 decorators makes it easy to temporarily replace classes in a particular module with a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 object. By default `patch()` will create a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 for you. You can specify an alternative class of `Mock` using the _new\_callable_ argument to `patch()`.

class unittest.mock.Mock(_spec\=None_, _side\_effect\=None_, _return\_value\=DEFAULT_, _wraps\=None_, _name\=None_, _spec\_set\=None_, _unsafe\=False_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "Link to this definition")

Create a new `Mock` object. `Mock` takes several optional arguments that specify the behaviour of the Mock object:

*   _spec_: This can be either a list of strings or an existing object (a class or instance) that acts as the specification for the mock object. If you pass in an object then a list of strings is formed by calling dir on the object (excluding unsupported magic attributes and methods). Accessing any attribute not in this list will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    .
    
    If _spec_ is an object (rather than a list of strings) then [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__")
     returns the class of the spec object. This allows mocks to pass [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
     tests.
    
*   _spec\_set_: A stricter variant of _spec_. If used, attempting to _set_ or get an attribute on the mock that isn’t on the object passed as _spec\_set_ will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    .
    
*   _side\_effect_: A function to be called whenever the Mock is called. See the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
     attribute. Useful for raising exceptions or dynamically changing return values. The function is called with the same arguments as the mock, and unless it returns [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
    , the return value of this function is used as the return value.
    
    Alternatively _side\_effect_ can be an exception class or instance. In this case the exception will be raised when the mock is called.
    
    If _side\_effect_ is an iterable then each call to the mock will return the next value from the iterable.
    
    A _side\_effect_ can be cleared by setting it to `None`.
    
*   _return\_value_: The value returned when the mock is called. By default this is a new Mock (created on first access). See the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
     attribute.
    
*   _unsafe_: By default, accessing any attribute whose name starts with _assert_, _assret_, _asert_, _aseert_ or _assrt_ will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    . Passing `unsafe=True` will allow access to these attributes.
    
    Added in version 3.5.
    
*   _wraps_: Item for the mock object to wrap. If _wraps_ is not `None` then calling the Mock will pass the call through to the wrapped object (returning the real result). Attribute access on the mock will return a Mock object that wraps the corresponding attribute of the wrapped object (so attempting to access an attribute that doesn’t exist will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    ).
    
    If the mock has an explicit _return\_value_ set then calls are not passed to the wrapped object and the _return\_value_ is returned instead.
    
*   _name_: If the mock has a name then it will be used in the repr of the mock. This can be useful for debugging. The name is propagated to child mocks.
    

Mocks can also be called with arbitrary keyword arguments. These will be used to set attributes on the mock after it is created. See the [`configure_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "unittest.mock.Mock.configure_mock")
 method for details.

assert\_called()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called "Link to this definition")

Assert that the mock was called at least once.

Copy

\>>> mock \= Mock()
\>>> mock.method()
<Mock name='mock.method()' id='...'>
\>>> mock.method.assert\_called()

Added in version 3.6.

assert\_called\_once()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once "Link to this definition")

Assert that the mock was called exactly once.

Copy

\>>> mock \= Mock()
\>>> mock.method()
<Mock name='mock.method()' id='...'>
\>>> mock.method.assert\_called\_once()
\>>> mock.method()
<Mock name='mock.method()' id='...'>
\>>> mock.method.assert\_called\_once()
Traceback (most recent call last):
...
AssertionError: Expected 'method' to have been called once. Called 2 times.
Calls: \[call(), call()\].

Added in version 3.6.

assert\_called\_with(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "Link to this definition")

This method is a convenient way of asserting that the last call has been made in a particular way:

Copy

\>>> mock \= Mock()
\>>> mock.method(1, 2, 3, test\='wow')
<Mock name='mock.method()' id='...'>
\>>> mock.method.assert\_called\_with(1, 2, 3, test\='wow')

assert\_called\_once\_with(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "Link to this definition")

Assert that the mock was called exactly once and that call was with the specified arguments.

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock('foo', bar\='baz')
\>>> mock.assert\_called\_once\_with('foo', bar\='baz')
\>>> mock('other', bar\='values')
\>>> mock.assert\_called\_once\_with('other', bar\='values')
Traceback (most recent call last):
  ...
AssertionError: Expected 'mock' to be called once. Called 2 times.
Calls: \[call('foo', bar='baz'), call('other', bar='values')\].

assert\_any\_call(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_any_call "Link to this definition")

Assert the mock has been called with the specified arguments.

The assert passes if the mock has _ever_ been called, unlike [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
 and [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with")
 that only pass if the call is the most recent one, and in the case of `assert_called_once_with()` it must also be the only call.

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock(1, 2, arg\='thing')
\>>> mock('some', 'thing', 'else')
\>>> mock.assert\_any\_call(1, 2, arg\='thing')

assert\_has\_calls(_calls_, _any\_order\=False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "Link to this definition")

Assert the mock has been called with the specified calls. The [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 list is checked for the calls.

If _any\_order_ is false then the calls must be sequential. There can be extra calls before or after the specified calls.

If _any\_order_ is true then the calls can be in any order, but they must all appear in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
.

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock(1)
\>>> mock(2)
\>>> mock(3)
\>>> mock(4)
\>>> calls \= \[call(2), call(3)\]
\>>> mock.assert\_has\_calls(calls)
\>>> calls \= \[call(4), call(2), call(3)\]
\>>> mock.assert\_has\_calls(calls, any\_order\=True)

assert\_not\_called()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_not_called "Link to this definition")

Assert the mock was never called.

Copy

\>>> m \= Mock()
\>>> m.hello.assert\_not\_called()
\>>> obj \= m.hello()
\>>> m.hello.assert\_not\_called()
Traceback (most recent call last):
  ...
AssertionError: Expected 'hello' to not have been called. Called 1 times.
Calls: \[call()\].

Added in version 3.5.

reset\_mock(_\*_, _return\_value\=False_, _side\_effect\=False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock "Link to this definition")

The reset\_mock method resets all the call attributes on a mock object:

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock('hello')
\>>> mock.called
True
\>>> mock.reset\_mock()
\>>> mock.called
False

This can be useful where you want to make a series of assertions that reuse the same object.

_return\_value_ parameter when set to `True` resets [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
:

Copy

\>>> mock \= Mock(return\_value\=5)
\>>> mock('hello')
5
\>>> mock.reset\_mock(return\_value\=True)
\>>> mock('hello')
<Mock name='mock()' id='...'>

_side\_effect_ parameter when set to `True` resets [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
:

Copy

\>>> mock \= Mock(side\_effect\=ValueError)
\>>> mock('hello')
Traceback (most recent call last):
  ...
ValueError
\>>> mock.reset\_mock(side\_effect\=True)
\>>> mock('hello')
<Mock name='mock()' id='...'>

Note that `reset_mock()` _doesn’t_ clear the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
, [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 or any child attributes you have set using normal assignment by default.

Child mocks are reset as well.

Changed in version 3.6: Added two keyword-only arguments to the reset\_mock function.

mock\_add\_spec(_spec_, _spec\_set\=False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_add_spec "Link to this definition")

Add a spec to a mock. _spec_ can either be an object or a list of strings. Only attributes on the _spec_ can be fetched as attributes from the mock.

If _spec\_set_ is true then only attributes on the spec can be set.

attach\_mock(_mock_, _attribute_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.attach_mock "Link to this definition")

Attach a mock as an attribute of this one, replacing its name and parent. Calls to the attached mock will be recorded in the [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
 and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 attributes of this one.

configure\_mock(_\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "Link to this definition")

Set attributes on the mock through keyword arguments.

Attributes plus return values and side effects can be set on child mocks using standard dot notation and unpacking a dictionary in the method call:

Copy

\>>> mock \= Mock()
\>>> attrs \= {'method.return\_value': 3, 'other.side\_effect': KeyError}
\>>> mock.configure\_mock(\*\*attrs)
\>>> mock.method()
3
\>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

The same thing can be achieved in the constructor call to mocks:

Copy

\>>> attrs \= {'method.return\_value': 3, 'other.side\_effect': KeyError}
\>>> mock \= Mock(some\_attribute\='eggs', \*\*attrs)
\>>> mock.some\_attribute
'eggs'
\>>> mock.method()
3
\>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

`configure_mock()` exists to make it easier to do configuration after the mock has been created.

\_\_dir\_\_()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.__dir__ "Link to this definition")

`Mock` objects limit the results of `dir(some_mock)` to useful results. For mocks with a _spec_ this includes all the permitted attributes for the mock.

See [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR")
 for what this filtering does, and how to switch it off.

\_get\_child\_mock(_\*\*kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock._get_child_mock "Link to this definition")

Create the child mocks for attributes and return value. By default child mocks will be the same type as the parent. Subclasses of Mock may want to override this to customize the way child mocks are made.

For non-callable mocks the callable variant will be used (rather than any custom subclass).

called[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.called "Link to this definition")

A boolean representing whether or not the mock object has been called:

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock.called
False
\>>> mock()
\>>> mock.called
True

call\_count[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count "Link to this definition")

An integer telling you how many times the mock object has been called:

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock.call\_count
0
\>>> mock()
\>>> mock()
\>>> mock.call\_count
2

return\_value[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "Link to this definition")

Set this to configure the value returned by calling the mock:

Copy

\>>> mock \= Mock()
\>>> mock.return\_value \= 'fish'
\>>> mock()
'fish'

The default return value is a mock object and you can configure it in the normal way:

Copy

\>>> mock \= Mock()
\>>> mock.return\_value.attribute \= sentinel.Attribute
\>>> mock.return\_value()
<Mock name='mock()()' id='...'>
\>>> mock.return\_value.assert\_called\_with()

[`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 can also be set in the constructor:

Copy

\>>> mock \= Mock(return\_value\=3)
\>>> mock.return\_value
3
\>>> mock()
3

side\_effect[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "Link to this definition")

This can either be a function to be called when the mock is called, an iterable or an exception (class or instance) to be raised.

If you pass in a function it will be called with same arguments as the mock and unless the function returns the [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
 singleton the call to the mock will then return whatever the function returns. If the function returns `DEFAULT` then the mock will return its normal value (from the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
).

If you pass in an iterable, it is used to retrieve an iterator which must yield a value on every call. This value can either be an exception instance to be raised, or a value to be returned from the call to the mock ([`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
 handling is identical to the function case).

An example of a mock that raises an exception (to test exception handling of an API):

Copy

\>>> mock \= Mock()
\>>> mock.side\_effect \= Exception('Boom!')
\>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

Using [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 to return a sequence of values:

Copy

\>>> mock \= Mock()
\>>> mock.side\_effect \= \[3, 2, 1\]
\>>> mock(), mock(), mock()
(3, 2, 1)

Using a callable:

Copy

\>>> mock \= Mock(return\_value\=3)
\>>> def side\_effect(\*args, \*\*kwargs):
...     return DEFAULT
...
\>>> mock.side\_effect \= side\_effect
\>>> mock()
3

[`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 can be set in the constructor. Here’s an example that adds one to the value the mock is called with and returns it:

Copy

\>>> side\_effect \= lambda value: value + 1
\>>> mock \= Mock(side\_effect\=side\_effect)
\>>> mock(3)
4
\>>> mock(\-8)
\-7

Setting [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 to `None` clears it:

Copy

\>>> m \= Mock(side\_effect\=KeyError, return\_value\=3)
\>>> m()
Traceback (most recent call last):
 ...
KeyError
\>>> m.side\_effect \= None
\>>> m()
3

call\_args[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "Link to this definition")

This is either `None` (if the mock hasn’t been called), or the arguments that the mock was last called with. This will be in the form of a tuple: the first member, which can also be accessed through the `args` property, is any positional arguments the mock was called with (or an empty tuple) and the second member, which can also be accessed through the `kwargs` property, is any keyword arguments (or an empty dictionary).

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> print(mock.call\_args)
None
\>>> mock()
\>>> mock.call\_args
call()
\>>> mock.call\_args \== ()
True
\>>> mock(3, 4)
\>>> mock.call\_args
call(3, 4)
\>>> mock.call\_args \== ((3, 4),)
True
\>>> mock.call\_args.args
(3, 4)
\>>> mock.call\_args.kwargs
{}
\>>> mock(3, 4, 5, key\='fish', next\='w00t!')
\>>> mock.call\_args
call(3, 4, 5, key='fish', next='w00t!')
\>>> mock.call\_args.args
(3, 4, 5)
\>>> mock.call\_args.kwargs
{'key': 'fish', 'next': 'w00t!'}

[`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
, along with members of the lists [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
, [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
 and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 objects. These are tuples, so they can be unpacked to get at the individual arguments and make more complex assertions. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples)
.

Changed in version 3.8: Added `args` and `kwargs` properties.

call\_args\_list[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "Link to this definition")

This is a list of all the calls made to the mock object in sequence (so the length of the list is the number of times it has been called). Before any calls have been made it is an empty list. The [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 object can be used for conveniently constructing lists of calls to compare with [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
.

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock()
\>>> mock(3, 4)
\>>> mock(key\='fish', next\='w00t!')
\>>> mock.call\_args\_list
\[call(), call(3, 4), call(key='fish', next='w00t!')\]
\>>> expected \= \[(), ((3, 4),), ({'key': 'fish', 'next': 'w00t!'},)\]
\>>> mock.call\_args\_list \== expected
True

Members of [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
 are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples)
.

method\_calls[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "Link to this definition")

As well as tracking calls to themselves, mocks also track calls to methods and attributes, and _their_ methods and attributes:

Copy

\>>> mock \= Mock()
\>>> mock.method()
<Mock name='mock.method()' id='...'>
\>>> mock.property.method.attribute()
<Mock name='mock.property.method.attribute()' id='...'>
\>>> mock.method\_calls
\[call.method(), call.property.method.attribute()\]

Members of [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
 are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples)
.

mock\_calls[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "Link to this definition")

[`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 records _all_ calls to the mock object, its methods, magic methods _and_ return value mocks.

Copy

\>>> mock \= MagicMock()
\>>> result \= mock(1, 2, 3)
\>>> mock.first(a\=3)
<MagicMock name='mock.first()' id='...'>
\>>> mock.second()
<MagicMock name='mock.second()' id='...'>
\>>> int(mock)
1
\>>> result(1)
<MagicMock name='mock()()' id='...'>
\>>> expected \= \[call(1, 2, 3), call.first(a\=3), call.second(),\
... call.\_\_int\_\_(), call()(1)\]
\>>> mock.mock\_calls \== expected
True

Members of [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples)
.

Note

The way [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 are recorded means that where nested calls are made, the parameters of ancestor calls are not recorded and so will always compare equal:

Copy

\>>> mock \= MagicMock()
\>>> mock.top(a\=3).bottom()
<MagicMock name='mock.top().bottom()' id='...'>
\>>> mock.mock\_calls
\[call.top(a=3), call.top().bottom()\]
\>>> mock.mock\_calls\[\-1\] \== call.top(a\=-1).bottom()
True

\_\_class\_\_[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.__class__ "Link to this definition")

Normally the `__class__` attribute of an object will return its type. For a mock object with a `spec`, `__class__` returns the spec class instead. This allows mock objects to pass [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 tests for the object they are replacing / masquerading as:

Copy

\>>> mock \= Mock(spec\=3)
\>>> isinstance(mock, int)
True

`__class__` is assignable to, this allows a mock to pass an [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 check without forcing you to use a spec:

Copy

\>>> mock \= Mock()
\>>> mock.\_\_class\_\_ \= dict
\>>> isinstance(mock, dict)
True

class unittest.mock.NonCallableMock(_spec\=None_, _wraps\=None_, _name\=None_, _spec\_set\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "Link to this definition")

A non-callable version of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
. The constructor parameters have the same meaning of `Mock`, with the exception of _return\_value_ and _side\_effect_ which have no meaning on a non-callable mock.

Mock objects that use a class or an instance as a `spec` or `spec_set` are able to pass [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
 tests:

Copy

\>>> mock \= Mock(spec\=SomeClass)
\>>> isinstance(mock, SomeClass)
True
\>>> mock \= Mock(spec\_set\=SomeClass())
\>>> isinstance(mock, SomeClass)
True

The [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 classes have support for mocking magic methods. See [magic methods](https://docs.python.org/3/library/unittest.mock.html#magic-methods)
 for the full details.

The mock classes and the [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 decorators all take arbitrary keyword arguments for configuration. For the `patch()` decorators the keywords are passed to the constructor of the mock being created. The keyword arguments are for configuring attributes of the mock:

Copy

\>>> m \= MagicMock(attribute\=3, other\='fish')
\>>> m.attribute
3
\>>> m.other
'fish'

The return value and side effect of child mocks can be set in the same way, using dotted notation. As you can’t use dotted names directly in a call you have to create a dictionary and unpack it using `**`:

Copy

\>>> attrs \= {'method.return\_value': 3, 'other.side\_effect': KeyError}
\>>> mock \= Mock(some\_attribute\='eggs', \*\*attrs)
\>>> mock.some\_attribute
'eggs'
\>>> mock.method()
3
\>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

A callable mock which was created with a _spec_ (or a _spec\_set_) will introspect the specification object’s signature when matching calls to the mock. Therefore, it can match the actual call’s arguments regardless of whether they were passed positionally or by name:

Copy

\>>> def f(a, b, c): pass
...
\>>> mock \= Mock(spec\=f)
\>>> mock(1, 2, c\=3)
<Mock name='mock()' id='140161580456576'>
\>>> mock.assert\_called\_with(1, 2, 3)
\>>> mock.assert\_called\_with(a\=1, b\=2, c\=3)

This applies to [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
, [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with")
, [`assert_has_calls()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "unittest.mock.Mock.assert_has_calls")
 and [`assert_any_call()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_any_call "unittest.mock.Mock.assert_any_call")
. When [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
, it will also apply to method calls on the mock object.

Changed in version 3.4: Added signature introspection on specced and autospecced mock objects.

class unittest.mock.PropertyMock(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "Link to this definition")

A mock intended to be used as a [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
, or other [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
, on a class. `PropertyMock` provides [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__")
 and [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__")
 methods so you can specify a return value when it is fetched.

Fetching a `PropertyMock` instance from an object calls the mock, with no args. Setting it calls the mock with the value being set.

Copy

\>>> class Foo:
...     @property
...     def foo(self):
...         return 'something'
...     @foo.setter
...     def foo(self, value):
...         pass
...
\>>> with patch('\_\_main\_\_.Foo.foo', new\_callable\=PropertyMock) as mock\_foo:
...     mock\_foo.return\_value \= 'mockity-mock'
...     this\_foo \= Foo()
...     print(this\_foo.foo)
...     this\_foo.foo \= 6
...
mockity-mock
\>>> mock\_foo.mock\_calls
\[call(), call(6)\]

Because of the way mock attributes are stored you can’t directly attach a [`PropertyMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "unittest.mock.PropertyMock")
 to a mock object. Instead you can attach it to the mock type object:

Copy

\>>> m \= MagicMock()
\>>> p \= PropertyMock(return\_value\=3)
\>>> type(m).foo \= p
\>>> m.foo
3
\>>> p.assert\_called\_once\_with()

Caution

If an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 is raised by [`PropertyMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "unittest.mock.PropertyMock")
, it will be interpreted as a missing descriptor and [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 will be called on the parent mock:

Copy

\>>> m \= MagicMock()
\>>> no\_attribute \= PropertyMock(side\_effect\=AttributeError)
\>>> type(m).my\_property \= no\_attribute
\>>> m.my\_property
<MagicMock name='mock.my\_property' id='140165240345424'>

See [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 for details.

class unittest.mock.AsyncMock(_spec\=None_, _side\_effect\=None_, _return\_value\=DEFAULT_, _wraps\=None_, _name\=None_, _spec\_set\=None_, _unsafe\=False_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "Link to this definition")

An asynchronous version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
. The `AsyncMock` object will behave so the object is recognized as an async function, and the result of a call is an awaitable.

Copy

\>>> mock \= AsyncMock()
\>>> inspect.iscoroutinefunction(mock)
True
\>>> inspect.isawaitable(mock())
True

The result of `mock()` is an async function which will have the outcome of `side_effect` or `return_value` after it has been awaited:

*   if `side_effect` is a function, the async function will return the result of that function,
    
*   if `side_effect` is an exception, the async function will raise the exception,
    
*   if `side_effect` is an iterable, the async function will return the next value of the iterable, however, if the sequence of result is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
    , `StopAsyncIteration` is raised immediately,
    
*   if `side_effect` is not defined, the async function will return the value defined by `return_value`, hence, by default, the async function returns a new `AsyncMock` object.
    

Setting the _spec_ of a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 or [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 to an async function will result in a coroutine object being returned after calling.

Copy

\>>> async def async\_func(): pass
...
\>>> mock \= MagicMock(async\_func)
\>>> mock
<MagicMock spec='function' id='...'>
\>>> mock()
<coroutine object AsyncMockMixin.\_mock\_call at ...>

Setting the _spec_ of a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
, [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
, or `AsyncMock` to a class with asynchronous and synchronous functions will automatically detect the synchronous functions and set them as `MagicMock` (if the parent mock is `AsyncMock` or `MagicMock`) or `Mock` (if the parent mock is `Mock`). All asynchronous functions will be `AsyncMock`.

Copy

\>>> class ExampleClass:
...     def sync\_foo():
...         pass
...     async def async\_foo():
...         pass
...
\>>> a\_mock \= AsyncMock(ExampleClass)
\>>> a\_mock.sync\_foo
<MagicMock name='mock.sync\_foo' id='...'>
\>>> a\_mock.async\_foo
<AsyncMock name='mock.async\_foo' id='...'>
\>>> mock \= Mock(ExampleClass)
\>>> mock.sync\_foo
<Mock name='mock.sync\_foo' id='...'>
\>>> mock.async\_foo
<AsyncMock name='mock.async\_foo' id='...'>

Added in version 3.8.

assert\_awaited()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited "Link to this definition")

Assert that the mock was awaited at least once. Note that this is separate from the object having been called, the `await` keyword must be used:

Copy

\>>> mock \= AsyncMock()
\>>> async def main(coroutine\_mock):
...     await coroutine\_mock
...
\>>> coroutine\_mock \= mock()
\>>> mock.called
True
\>>> mock.assert\_awaited()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited.
\>>> asyncio.run(main(coroutine\_mock))
\>>> mock.assert\_awaited()

assert\_awaited\_once()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_once "Link to this definition")

Assert that the mock was awaited exactly once.

Copy

\>>> mock \= AsyncMock()
\>>> async def main():
...     await mock()
...
\>>> asyncio.run(main())
\>>> mock.assert\_awaited\_once()
\>>> asyncio.run(main())
\>>> mock.assert\_awaited\_once()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

assert\_awaited\_with(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_with "Link to this definition")

Assert that the last await was with the specified arguments.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args, \*\*kwargs):
...     await mock(\*args, \*\*kwargs)
...
\>>> asyncio.run(main('foo', bar\='bar'))
\>>> mock.assert\_awaited\_with('foo', bar\='bar')
\>>> mock.assert\_awaited\_with('other')
Traceback (most recent call last):
...
AssertionError: expected await not found.
Expected: mock('other')
Actual: mock('foo', bar='bar')

assert\_awaited\_once\_with(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_once_with "Link to this definition")

Assert that the mock was awaited exactly once and with the specified arguments.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args, \*\*kwargs):
...     await mock(\*args, \*\*kwargs)
...
\>>> asyncio.run(main('foo', bar\='bar'))
\>>> mock.assert\_awaited\_once\_with('foo', bar\='bar')
\>>> asyncio.run(main('foo', bar\='bar'))
\>>> mock.assert\_awaited\_once\_with('foo', bar\='bar')
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

assert\_any\_await(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_any_await "Link to this definition")

Assert the mock has ever been awaited with the specified arguments.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args, \*\*kwargs):
...     await mock(\*args, \*\*kwargs)
...
\>>> asyncio.run(main('foo', bar\='bar'))
\>>> asyncio.run(main('hello'))
\>>> mock.assert\_any\_await('foo', bar\='bar')
\>>> mock.assert\_any\_await('other')
Traceback (most recent call last):
...
AssertionError: mock('other') await not found

assert\_has\_awaits(_calls_, _any\_order\=False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_has_awaits "Link to this definition")

Assert the mock has been awaited with the specified calls. The [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list")
 list is checked for the awaits.

If _any\_order_ is false then the awaits must be sequential. There can be extra calls before or after the specified awaits.

If _any\_order_ is true then the awaits can be in any order, but they must all appear in [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list")
.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args, \*\*kwargs):
...     await mock(\*args, \*\*kwargs)
...
\>>> calls \= \[call("foo"), call("bar")\]
\>>> mock.assert\_has\_awaits(calls)
Traceback (most recent call last):
...
AssertionError: Awaits not found.
Expected: \[call('foo'), call('bar')\]
Actual: \[\]
\>>> asyncio.run(main('foo'))
\>>> asyncio.run(main('bar'))
\>>> mock.assert\_has\_awaits(calls)

assert\_not\_awaited()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_not_awaited "Link to this definition")

Assert that the mock was never awaited.

Copy

\>>> mock \= AsyncMock()
\>>> mock.assert\_not\_awaited()

reset\_mock(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.reset_mock "Link to this definition")

See [`Mock.reset_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock "unittest.mock.Mock.reset_mock")
. Also sets [`await_count`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_count "unittest.mock.AsyncMock.await_count")
 to 0, [`await_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args "unittest.mock.AsyncMock.await_args")
 to None, and clears the [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list")
.

await\_count[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_count "Link to this definition")

An integer keeping track of how many times the mock object has been awaited.

Copy

\>>> mock \= AsyncMock()
\>>> async def main():
...     await mock()
...
\>>> asyncio.run(main())
\>>> mock.await\_count
1
\>>> asyncio.run(main())
\>>> mock.await\_count
2

await\_args[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args "Link to this definition")

This is either `None` (if the mock hasn’t been awaited), or the arguments that the mock was last awaited with. Functions the same as [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args):
...     await mock(\*args)
...
\>>> mock.await\_args
\>>> asyncio.run(main('foo'))
\>>> mock.await\_args
call('foo')
\>>> asyncio.run(main('bar'))
\>>> mock.await\_args
call('bar')

await\_args\_list[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "Link to this definition")

This is a list of all the awaits made to the mock object in sequence (so the length of the list is the number of times it has been awaited). Before any awaits have been made it is an empty list.

Copy

\>>> mock \= AsyncMock()
\>>> async def main(\*args):
...     await mock(\*args)
...
\>>> mock.await\_args\_list
\[\]
\>>> asyncio.run(main('foo'))
\>>> mock.await\_args\_list
\[call('foo')\]
\>>> asyncio.run(main('bar'))
\>>> mock.await\_args\_list
\[call('foo'), call('bar')\]

class unittest.mock.ThreadingMock(_spec\=None_, _side\_effect\=None_, _return\_value\=DEFAULT_, _wraps\=None_, _name\=None_, _spec\_set\=None_, _unsafe\=False_, _\*_, _timeout\=UNSET_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock "Link to this definition")

A version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 for multithreading tests. The `ThreadingMock` object provides extra methods to wait for a call to be invoked, rather than assert on it immediately.

The default timeout is specified by the `timeout` argument, or if unset by the [`ThreadingMock.DEFAULT_TIMEOUT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "unittest.mock.ThreadingMock.DEFAULT_TIMEOUT")
 attribute, which defaults to blocking (`None`).

You can configure the global default timeout by setting [`ThreadingMock.DEFAULT_TIMEOUT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "unittest.mock.ThreadingMock.DEFAULT_TIMEOUT")
.

wait\_until\_called(_\*_, _timeout\=UNSET_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.wait_until_called "Link to this definition")

Waits until the mock is called.

If a timeout was passed at the creation of the mock or if a timeout argument is passed to this function, the function raises an [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
 if the call is not performed in time.

Copy

\>>> mock \= ThreadingMock()
\>>> thread \= threading.Thread(target\=mock)
\>>> thread.start()
\>>> mock.wait\_until\_called(timeout\=1)
\>>> thread.join()

wait\_until\_any\_call\_with(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.wait_until_any_call_with "Link to this definition")

Waits until the mock is called with the specified arguments.

If a timeout was passed at the creation of the mock the function raises an [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
 if the call is not performed in time.

Copy

\>>> mock \= ThreadingMock()
\>>> thread \= threading.Thread(target\=mock, args\=("arg1", "arg2",), kwargs\={"arg": "thing"})
\>>> thread.start()
\>>> mock.wait\_until\_any\_call\_with("arg1", "arg2", arg\="thing")
\>>> thread.join()

DEFAULT\_TIMEOUT[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "Link to this definition")

Global default timeout in seconds to create instances of `ThreadingMock`.

Added in version 3.13.

### Calling[¶](https://docs.python.org/3/library/unittest.mock.html#calling "Link to this heading")

Mock objects are callable. The call will return the value set as the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 attribute. The default return value is a new Mock object; it is created the first time the return value is accessed (either explicitly or by calling the Mock) - but it is stored and the same one returned each time.

Calls made to the object will be recorded in the attributes like [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
 and [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
.

If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 is set then it will be called after the call has been recorded, so if `side_effect` raises an exception the call is still recorded.

The simplest way to make a mock raise an exception when called is to make [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 an exception class or instance:

Copy

\>>> m \= MagicMock(side\_effect\=IndexError)
\>>> m(1, 2, 3)
Traceback (most recent call last):
  ...
IndexError
\>>> m.mock\_calls
\[call(1, 2, 3)\]
\>>> m.side\_effect \= KeyError('Bang!')
\>>> m('two', 'three', 'four')
Traceback (most recent call last):
  ...
KeyError: 'Bang!'
\>>> m.mock\_calls
\[call(1, 2, 3), call('two', 'three', 'four')\]

If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 is a function then whatever that function returns is what calls to the mock return. The `side_effect` function is called with the same arguments as the mock. This allows you to vary the return value of the call dynamically, based on the input:

Copy

\>>> def side\_effect(value):
...     return value + 1
...
\>>> m \= MagicMock(side\_effect\=side\_effect)
\>>> m(1)
2
\>>> m(2)
3
\>>> m.mock\_calls
\[call(1), call(2)\]

If you want the mock to still return the default return value (a new mock), or any set return value, then there are two ways of doing this. Either return [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 from inside [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
, or return [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
:

Copy

\>>> m \= MagicMock()
\>>> def side\_effect(\*args, \*\*kwargs):
...     return m.return\_value
...
\>>> m.side\_effect \= side\_effect
\>>> m.return\_value \= 3
\>>> m()
3
\>>> def side\_effect(\*args, \*\*kwargs):
...     return DEFAULT
...
\>>> m.side\_effect \= side\_effect
\>>> m()
3

To remove a [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
, and return to the default behaviour, set the `side_effect` to `None`:

Copy

\>>> m \= MagicMock(return\_value\=6)
\>>> def side\_effect(\*args, \*\*kwargs):
...     return 3
...
\>>> m.side\_effect \= side\_effect
\>>> m()
3
\>>> m.side\_effect \= None
\>>> m()
6

The [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 can also be any iterable object. Repeated calls to the mock will return values from the iterable (until the iterable is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
 and a [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 is raised):

Copy

\>>> m \= MagicMock(side\_effect\=\[1, 2, 3\])
\>>> m()
1
\>>> m()
2
\>>> m()
3
\>>> m()
Traceback (most recent call last):
  ...
StopIteration

If any members of the iterable are exceptions they will be raised instead of returned:

Copy

\>>> iterable \= (33, ValueError, 66)
\>>> m \= MagicMock(side\_effect\=iterable)
\>>> m()
33
\>>> m()
Traceback (most recent call last):
 ...
ValueError
\>>> m()
66

### Deleting Attributes[¶](https://docs.python.org/3/library/unittest.mock.html#deleting-attributes "Link to this heading")

Mock objects create attributes on demand. This allows them to pretend to be objects of any type.

You may want a mock object to return `False` to a [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
 call, or raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 when an attribute is fetched. You can do this by providing an object as a `spec` for a mock, but that isn’t always convenient.

You “block” attributes by deleting them. Once deleted, accessing an attribute will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

Copy

\>>> mock \= MagicMock()
\>>> hasattr(mock, 'm')
True
\>>> del mock.m
\>>> hasattr(mock, 'm')
False
\>>> del mock.f
\>>> mock.f
Traceback (most recent call last):
    ...
AttributeError: f

### Mock names and the name attribute[¶](https://docs.python.org/3/library/unittest.mock.html#mock-names-and-the-name-attribute "Link to this heading")

Since “name” is an argument to the [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 constructor, if you want your mock object to have a “name” attribute you can’t just pass it in at creation time. There are two alternatives. One option is to use [`configure_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "unittest.mock.Mock.configure_mock")
:

Copy

\>>> mock \= MagicMock()
\>>> mock.configure\_mock(name\='my\_name')
\>>> mock.name
'my\_name'

A simpler option is to simply set the “name” attribute after mock creation:

Copy

\>>> mock \= MagicMock()
\>>> mock.name \= "foo"

### Attaching Mocks as Attributes[¶](https://docs.python.org/3/library/unittest.mock.html#attaching-mocks-as-attributes "Link to this heading")

When you attach a mock as an attribute of another mock (or as the return value) it becomes a “child” of that mock. Calls to the child are recorded in the [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
 and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 attributes of the parent. This is useful for configuring child mocks and then attaching them to the parent, or for attaching mocks to a parent that records all calls to the children and allows you to make assertions about the order of calls between mocks:

Copy

\>>> parent \= MagicMock()
\>>> child1 \= MagicMock(return\_value\=None)
\>>> child2 \= MagicMock(return\_value\=None)
\>>> parent.child1 \= child1
\>>> parent.child2 \= child2
\>>> child1(1)
\>>> child2(2)
\>>> parent.mock\_calls
\[call.child1(1), call.child2(2)\]

The exception to this is if the mock has a name. This allows you to prevent the “parenting” if for some reason you don’t want it to happen.

Copy

\>>> mock \= MagicMock()
\>>> not\_a\_child \= MagicMock(name\='not-a-child')
\>>> mock.attribute \= not\_a\_child
\>>> mock.attribute()
<MagicMock name='not-a-child()' id='...'>
\>>> mock.mock\_calls
\[\]

Mocks created for you by [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 are automatically given names. To attach mocks that have names to a parent you use the [`attach_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.attach_mock "unittest.mock.Mock.attach_mock")
 method:

Copy

\>>> thing1 \= object()
\>>> thing2 \= object()
\>>> parent \= MagicMock()
\>>> with patch('\_\_main\_\_.thing1', return\_value\=None) as child1:
...     with patch('\_\_main\_\_.thing2', return\_value\=None) as child2:
...         parent.attach\_mock(child1, 'child1')
...         parent.attach\_mock(child2, 'child2')
...         child1('one')
...         child2('two')
...
\>>> parent.mock\_calls
\[call.child1('one'), call.child2('two')\]

The patchers[¶](https://docs.python.org/3/library/unittest.mock.html#the-patchers "Link to this heading")

----------------------------------------------------------------------------------------------------------

The patch decorators are used for patching objects only within the scope of the function they decorate. They automatically handle the unpatching for you, even if exceptions are raised. All of these functions can also be used in with statements or as class decorators.

### patch[¶](https://docs.python.org/3/library/unittest.mock.html#patch "Link to this heading")

Note

The key is to do the patching in the right namespace. See the section [where to patch](https://docs.python.org/3/library/unittest.mock.html#id6)
.

unittest.mock.patch(_target_, _new\=DEFAULT_, _spec\=None_, _create\=False_, _spec\_set\=None_, _autospec\=None_, _new\_callable\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "Link to this definition")

`patch()` acts as a function decorator, class decorator or a context manager. Inside the body of the function or with statement, the _target_ is patched with a _new_ object. When the function/with statement exits the patch is undone.

If _new_ is omitted, then the target is replaced with an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock")
 if the patched object is an async function or a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 otherwise. If `patch()` is used as a decorator and _new_ is omitted, the created mock is passed in as an extra argument to the decorated function. If `patch()` is used as a context manager the created mock is returned by the context manager.

_target_ should be a string in the form `'package.module.ClassName'`. The _target_ is imported and the specified object replaced with the _new_ object, so the _target_ must be importable from the environment you are calling `patch()` from. The target is imported when the decorated function is executed, not at decoration time.

The _spec_ and _spec\_set_ keyword arguments are passed to the [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 if patch is creating one for you.

In addition you can pass `spec=True` or `spec_set=True`, which causes patch to pass in the object being mocked as the spec/spec\_set object.

_new\_callable_ allows you to specify a different class, or callable object, that will be called to create the _new_ object. By default [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock")
 is used for async functions and [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 for the rest.

A more powerful form of _spec_ is _autospec_. If you set `autospec=True` then the mock will be created with a spec from the object being replaced. All attributes of the mock will also have the spec of the corresponding attribute of the object being replaced. Methods and functions being mocked will have their arguments checked and will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if they are called with the wrong signature. For mocks replacing a class, their return value (the ‘instance’) will have the same spec as the class. See the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")
 function and [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
.

Instead of `autospec=True` you can pass `autospec=some_object` to use an arbitrary object as the spec instead of the one being replaced.

By default `patch()` will fail to replace attributes that don’t exist. If you pass in `create=True`, and the attribute doesn’t exist, patch will create the attribute for you when the patched function is called, and delete it again after the patched function has exited. This is useful for writing tests against attributes that your production code creates at runtime. It is off by default because it can be dangerous. With it switched on you can write passing tests against APIs that don’t actually exist!

Note

Changed in version 3.5: If you are patching builtins in a module then you don’t need to pass `create=True`, it will be added by default.

Patch can be used as a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")
 class decorator. It works by decorating each test method in the class. This reduces the boilerplate code when your test methods share a common patchings set. `patch()` finds tests by looking for method names that start with `patch.TEST_PREFIX`. By default this is `'test'`, which matches the way [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
 finds tests. You can specify an alternative prefix by setting `patch.TEST_PREFIX`.

Patch can be used as a context manager, with the with statement. Here the patching applies to the indented block after the with statement. If you use “as” then the patched object will be bound to the name after the “as”; very useful if `patch()` is creating a mock object for you.

`patch()` takes arbitrary keyword arguments. These will be passed to [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock")
 if the patched object is asynchronous, to [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 otherwise or to _new\_callable_ if specified.

`patch.dict(...)`, `patch.multiple(...)` and `patch.object(...)` are available for alternate use-cases.

[`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 as function decorator, creating the mock for you and passing it into the decorated function:

Copy

\>>> @patch('\_\_main\_\_.SomeClass')
... def function(normal\_argument, mock\_class):
...     print(mock\_class is SomeClass)
...
\>>> function(None)
True

Patching a class replaces the class with a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 _instance_. If the class is instantiated in the code under test then it will be the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 of the mock that will be used.

If the class is instantiated multiple times you could use [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 to return a new mock each time. Alternatively you can set the _return\_value_ to be anything you want.

To configure return values on methods of _instances_ on the patched class you must do this on the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
. For example:

Copy

\>>> class Class:
...     def method(self):
...         pass
...
\>>> with patch('\_\_main\_\_.Class') as MockClass:
...     instance \= MockClass.return\_value
...     instance.method.return\_value \= 'foo'
...     assert Class() is instance
...     assert Class().method() \== 'foo'
...

If you use _spec_ or _spec\_set_ and [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 is replacing a _class_, then the return value of the created mock will have the same spec.

Copy

\>>> Original \= Class
\>>> patcher \= patch('\_\_main\_\_.Class', spec\=True)
\>>> MockClass \= patcher.start()
\>>> instance \= MockClass()
\>>> assert isinstance(instance, Original)
\>>> patcher.stop()

The _new\_callable_ argument is useful where you want to use an alternative class to the default [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 for the created mock. For example, if you wanted a [`NonCallableMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "unittest.mock.NonCallableMock")
 to be used:

Copy

\>>> thing \= object()
\>>> with patch('\_\_main\_\_.thing', new\_callable\=NonCallableMock) as mock\_thing:
...     assert thing is mock\_thing
...     thing()
...
Traceback (most recent call last):
  ...
TypeError: 'NonCallableMock' object is not callable

Another use case might be to replace an object with an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
 instance:

Copy

\>>> from io import StringIO
\>>> def foo():
...     print('Something')
...
\>>> @patch('sys.stdout', new\_callable\=StringIO)
... def test(mock\_stdout):
...     foo()
...     assert mock\_stdout.getvalue() \== 'Something\\n'
...
\>>> test()

When [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 is creating a mock for you, it is common that the first thing you need to do is to configure the mock. Some of that configuration can be done in the call to patch. Any arbitrary keywords you pass into the call will be used to set attributes on the created mock:

Copy

\>>> patcher \= patch('\_\_main\_\_.thing', first\='one', second\='two')
\>>> mock\_thing \= patcher.start()
\>>> mock\_thing.first
'one'
\>>> mock\_thing.second
'two'

As well as attributes on the created mock attributes, like the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 and [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
, of child mocks can also be configured. These aren’t syntactically valid to pass in directly as keyword arguments, but a dictionary with these as keys can still be expanded into a [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 call using `**`:

Copy

\>>> config \= {'method.return\_value': 3, 'other.side\_effect': KeyError}
\>>> patcher \= patch('\_\_main\_\_.thing', \*\*config)
\>>> mock\_thing \= patcher.start()
\>>> mock\_thing.method()
3
\>>> mock\_thing.other()
Traceback (most recent call last):
  ...
KeyError

By default, attempting to patch a function in a module (or a method or an attribute in a class) that does not exist will fail with [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
:

Copy

\>>> @patch('sys.non\_existing\_attribute', 42)
... def test():
...     assert sys.non\_existing\_attribute \== 42
...
\>>> test()
Traceback (most recent call last):
  ...
AttributeError: <module 'sys' (built-in)> does not have the attribute 'non\_existing\_attribute'

but adding `create=True` in the call to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 will make the previous example work as expected:

Copy

\>>> @patch('sys.non\_existing\_attribute', 42, create\=True)
... def test(mock\_stdout):
...     assert sys.non\_existing\_attribute \== 42
...
\>>> test()

Changed in version 3.8: [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 now returns an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock")
 if the target is an async function.

### patch.object[¶](https://docs.python.org/3/library/unittest.mock.html#patch-object "Link to this heading")

patch.object(_target_, _attribute_, _new\=DEFAULT_, _spec\=None_, _create\=False_, _spec\_set\=None_, _autospec\=None_, _new\_callable\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "Link to this definition")

patch the named member (_attribute_) on an object (_target_) with a mock object.

`patch.object()` can be used as a decorator, class decorator or a context manager. Arguments _new_, _spec_, _create_, _spec\_set_, _autospec_ and _new\_callable_ have the same meaning as for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
. Like `patch()`, `patch.object()` takes arbitrary keyword arguments for configuring the mock object it creates.

When used as a class decorator `patch.object()` honours `patch.TEST_PREFIX` for choosing which methods to wrap.

You can either call [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
 with three arguments or two arguments. The three argument form takes the object to be patched, the attribute name and the object to replace the attribute with.

When calling with the two argument form you omit the replacement object, and a mock is created for you and passed in as an extra argument to the decorated function:

Copy

\>>> @patch.object(SomeClass, 'class\_method')
... def test(mock\_method):
...     SomeClass.class\_method(3)
...     mock\_method.assert\_called\_with(3)
...
\>>> test()

_spec_, _create_ and the other arguments to [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
 have the same meaning as they do for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
.

### patch.dict[¶](https://docs.python.org/3/library/unittest.mock.html#patch-dict "Link to this heading")

patch.dict(_in\_dict_, _values\=()_, _clear\=False_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "Link to this definition")

Patch a dictionary, or dictionary like object, and restore the dictionary to its original state after the test, where the restored dictionary is a copy of the dictionary as it was before the test.

_in\_dict_ can be a dictionary or a mapping like container. If it is a mapping then it must at least support getting, setting and deleting items plus iterating over keys.

_in\_dict_ can also be a string specifying the name of the dictionary, which will then be fetched by importing it.

_values_ can be a dictionary of values to set in the dictionary. _values_ can also be an iterable of `(key, value)` pairs.

If _clear_ is true then the dictionary will be cleared before the new values are set.

`patch.dict()` can also be called with arbitrary keyword arguments to set values in the dictionary.

Changed in version 3.8: `patch.dict()` now returns the patched dictionary when used as a context manager.

[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 can be used as a context manager, decorator or class decorator:

Copy

\>>> foo \= {}
\>>> @patch.dict(foo, {'newkey': 'newvalue'})
... def test():
...     assert foo \== {'newkey': 'newvalue'}
...
\>>> test()
\>>> assert foo \== {}

When used as a class decorator [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 honours `patch.TEST_PREFIX` (default to `'test'`) for choosing which methods to wrap:

Copy

\>>> import os
\>>> import unittest
\>>> from unittest.mock import patch
\>>> @patch.dict('os.environ', {'newkey': 'newvalue'})
... class TestSample(unittest.TestCase):
...     def test\_sample(self):
...         self.assertEqual(os.environ\['newkey'\], 'newvalue')

If you want to use a different prefix for your test, you can inform the patchers of the different prefix by setting `patch.TEST_PREFIX`. For more details about how to change the value of see [TEST\_PREFIX](https://docs.python.org/3/library/unittest.mock.html#test-prefix)
.

[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 can be used to add members to a dictionary, or simply let a test change a dictionary, and ensure the dictionary is restored when the test ends.

Copy

\>>> foo \= {}
\>>> with patch.dict(foo, {'newkey': 'newvalue'}) as patched\_foo:
...     assert foo \== {'newkey': 'newvalue'}
...     assert patched\_foo \== {'newkey': 'newvalue'}
...     \# You can add, update or delete keys of foo (or patched\_foo, it's the same dict)
...     patched\_foo\['spam'\] \= 'eggs'
...
\>>> assert foo \== {}
\>>> assert patched\_foo \== {}

Copy

\>>> import os
\>>> with patch.dict('os.environ', {'newkey': 'newvalue'}):
...     print(os.environ\['newkey'\])
...
newvalue
\>>> assert 'newkey' not in os.environ

Keywords can be used in the [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 call to set values in the dictionary:

Copy

\>>> mymodule \= MagicMock()
\>>> mymodule.function.return\_value \= 'fish'
\>>> with patch.dict('sys.modules', mymodule\=mymodule):
...     import mymodule
...     mymodule.function('some', 'args')
...
'fish'

[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 can be used with dictionary like objects that aren’t actually dictionaries. At the very minimum they must support item getting, setting, deleting and either iteration or membership test. This corresponds to the magic methods [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
, [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
, [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__")
 and either [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
 or [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
.

Copy

\>>> class Container:
...     def \_\_init\_\_(self):
...         self.values \= {}
...     def \_\_getitem\_\_(self, name):
...         return self.values\[name\]
...     def \_\_setitem\_\_(self, name, value):
...         self.values\[name\] \= value
...     def \_\_delitem\_\_(self, name):
...         del self.values\[name\]
...     def \_\_iter\_\_(self):
...         return iter(self.values)
...
\>>> thing \= Container()
\>>> thing\['one'\] \= 1
\>>> with patch.dict(thing, one\=2, two\=3):
...     assert thing\['one'\] \== 2
...     assert thing\['two'\] \== 3
...
\>>> assert thing\['one'\] \== 1
\>>> assert list(thing) \== \['one'\]

### patch.multiple[¶](https://docs.python.org/3/library/unittest.mock.html#patch-multiple "Link to this heading")

patch.multiple(_target_, _spec\=None_, _create\=False_, _spec\_set\=None_, _autospec\=None_, _new\_callable\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "Link to this definition")

Perform multiple patches in a single call. It takes the object to be patched (either as an object or a string to fetch the object by importing) and keyword arguments for the patches:

Copy

with patch.multiple(settings, FIRST\_PATCH\='one', SECOND\_PATCH\='two'):
    ...

Use [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
 as the value if you want `patch.multiple()` to create mocks for you. In this case the created mocks are passed into a decorated function by keyword, and a dictionary is returned when `patch.multiple()` is used as a context manager.

`patch.multiple()` can be used as a decorator, class decorator or a context manager. The arguments _spec_, _spec\_set_, _create_, _autospec_ and _new\_callable_ have the same meaning as for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
. These arguments will be applied to _all_ patches done by `patch.multiple()`.

When used as a class decorator `patch.multiple()` honours `patch.TEST_PREFIX` for choosing which methods to wrap.

If you want [`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple")
 to create mocks for you, then you can use [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")
 as the value. If you use `patch.multiple()` as a decorator then the created mocks are passed into the decorated function by keyword.

Copy

\>>> thing \= object()
\>>> other \= object()

\>>> @patch.multiple('\_\_main\_\_', thing\=DEFAULT, other\=DEFAULT)
... def test\_function(thing, other):
...     assert isinstance(thing, MagicMock)
...     assert isinstance(other, MagicMock)
...
\>>> test\_function()

[`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple")
 can be nested with other `patch` decorators, but put arguments passed by keyword _after_ any of the standard arguments created by [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
:

Copy

\>>> @patch('sys.exit')
... @patch.multiple('\_\_main\_\_', thing\=DEFAULT, other\=DEFAULT)
... def test\_function(mock\_exit, other, thing):
...     assert 'other' in repr(other)
...     assert 'thing' in repr(thing)
...     assert 'exit' in repr(mock\_exit)
...
\>>> test\_function()

If [`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple")
 is used as a context manager, the value returned by the context manager is a dictionary where created mocks are keyed by name:

Copy

\>>> with patch.multiple('\_\_main\_\_', thing\=DEFAULT, other\=DEFAULT) as values:
...     assert 'other' in repr(values\['other'\])
...     assert 'thing' in repr(values\['thing'\])
...     assert values\['thing'\] is thing
...     assert values\['other'\] is other
...

### patch methods: start and stop[¶](https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop "Link to this heading")

All the patchers have `start()` and `stop()` methods. These make it simpler to do patching in `setUp` methods or where you want to do multiple patches without nesting decorators or with statements.

To use them call [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
, [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
 or [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 as normal and keep a reference to the returned `patcher` object. You can then call `start()` to put the patch in place and `stop()` to undo it.

If you are using [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 to create a mock for you then it will be returned by the call to `patcher.start`.

Copy

\>>> patcher \= patch('package.module.ClassName')
\>>> from package import module
\>>> original \= module.ClassName
\>>> new\_mock \= patcher.start()
\>>> assert module.ClassName is not original
\>>> assert module.ClassName is new\_mock
\>>> patcher.stop()
\>>> assert module.ClassName is original
\>>> assert module.ClassName is not new\_mock

A typical use case for this might be for doing multiple patches in the `setUp` method of a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")
:

Copy

\>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         self.patcher1 \= patch('package.module.Class1')
...         self.patcher2 \= patch('package.module.Class2')
...         self.MockClass1 \= self.patcher1.start()
...         self.MockClass2 \= self.patcher2.start()
...
...     def tearDown(self):
...         self.patcher1.stop()
...         self.patcher2.stop()
...
...     def test\_something(self):
...         assert package.module.Class1 is self.MockClass1
...         assert package.module.Class2 is self.MockClass2
...
\>>> MyTest('test\_something').run()

Caution

If you use this technique you must ensure that the patching is “undone” by calling `stop`. This can be fiddlier than you might think, because if an exception is raised in the `setUp` then `tearDown` is not called. [`unittest.TestCase.addCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup")
 makes this easier:

Copy

\>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         patcher \= patch('package.module.Class')
...         self.MockClass \= patcher.start()
...         self.addCleanup(patcher.stop)
...
...     def test\_something(self):
...         assert package.module.Class is self.MockClass
...

As an added bonus you no longer need to keep a reference to the `patcher` object.

It is also possible to stop all patches which have been started by using [`patch.stopall()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.stopall "unittest.mock.patch.stopall")
.

patch.stopall()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.stopall "Link to this definition")

Stop all active patches. Only stops patches started with `start`.

### patch builtins[¶](https://docs.python.org/3/library/unittest.mock.html#patch-builtins "Link to this heading")

You can patch any builtins within a module. The following example patches builtin [`ord()`](https://docs.python.org/3/builtins/functions.html#ord "ord")
:

Copy

\>>> @patch('\_\_main\_\_.ord')
... def test(mock\_ord):
...     mock\_ord.return\_value \= 101
...     print(ord('c'))
...
\>>> test()
101

### TEST\_PREFIX[¶](https://docs.python.org/3/library/unittest.mock.html#test-prefix "Link to this heading")

All of the patchers can be used as class decorators. When used in this way they wrap every test method on the class. The patchers recognise methods that start with `'test'` as being test methods. This is the same way that the [`unittest.TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader")
 finds test methods by default.

It is possible that you want to use a different prefix for your tests. You can inform the patchers of the different prefix by setting `patch.TEST_PREFIX`:

Copy

\>>> patch.TEST\_PREFIX \= 'foo'
\>>> value \= 3
\>>>
\>>> @patch('\_\_main\_\_.value', 'not three')
... class Thing:
...     def foo\_one(self):
...         print(value)
...     def foo\_two(self):
...         print(value)
...
\>>>
\>>> Thing().foo\_one()
not three
\>>> Thing().foo\_two()
not three
\>>> value
3

### Nesting Patch Decorators[¶](https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators "Link to this heading")

If you want to perform multiple patches then you can simply stack up the decorators.

You can stack up multiple patch decorators using this pattern:

Copy

\>>> @patch.object(SomeClass, 'class\_method')
... @patch.object(SomeClass, 'static\_method')
... def test(mock1, mock2):
...     assert SomeClass.static\_method is mock1
...     assert SomeClass.class\_method is mock2
...     SomeClass.static\_method('foo')
...     SomeClass.class\_method('bar')
...     return mock1, mock2
...
\>>> mock1, mock2 \= test()
\>>> mock1.assert\_called\_once\_with('foo')
\>>> mock2.assert\_called\_once\_with('bar')

Note that the decorators are applied from the bottom upwards. This is the standard way that Python applies decorators. The order of the created mocks passed into your test function matches this order.

### Where to patch[¶](https://docs.python.org/3/library/unittest.mock.html#where-to-patch "Link to this heading")

[`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 works by (temporarily) changing the object that a _name_ points to with another one. There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.

The basic principle is that you patch where an object is _looked up_, which is not necessarily the same place as where it is defined. A couple of examples will help to clarify this.

Imagine we have a project that we want to test with the following structure:

Copy

a.py
    \-> Defines SomeClass

b.py
    \-> from a import SomeClass
    \-> some\_function instantiates SomeClass

Now we want to test `some_function` but we want to mock out `SomeClass` using [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
. The problem is that when we import module b, which we will have to do when it imports `SomeClass` from module a. If we use `patch()` to mock out `a.SomeClass` then it will have no effect on our test; module b already has a reference to the _real_ `SomeClass` and it looks like our patching had no effect.

The key is to patch out `SomeClass` where it is used (or where it is looked up). In this case `some_function` will actually look up `SomeClass` in module b, where we have imported it. The patching should look like:

Copy

@patch('b.SomeClass')

However, consider the alternative scenario where instead of `from a import SomeClass` module b does `import a` and `some_function` uses `a.SomeClass`. Both of these import forms are common. In this case the class we want to patch is being looked up in the module and so we have to patch `a.SomeClass` instead:

Copy

@patch('a.SomeClass')

### Patching Descriptors and Proxy Objects[¶](https://docs.python.org/3/library/unittest.mock.html#patching-descriptors-and-proxy-objects "Link to this heading")

Both [patch](https://docs.python.org/3/library/unittest.mock.html#patch)
 and [patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object)
 correctly patch and restore descriptors: class methods, static methods and properties. You should patch these on the _class_ rather than an instance. They also work with _some_ objects that proxy attribute access, like the [django settings object](https://web.archive.org/web/20200603181648/http://www.voidspace.org.uk/python/weblog/arch_d7_2010_12_04.shtml#e1198)
.

MagicMock and magic method support[¶](https://docs.python.org/3/library/unittest.mock.html#magicmock-and-magic-method-support "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

### Mocking Magic Methods[¶](https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods "Link to this heading")

[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 supports mocking the Python protocol methods, also known as [“magic methods”](https://docs.python.org/3/glossary.html#term-magic-method)
. This allows mock objects to replace containers or other objects that implement Python protocols.

Because magic methods are looked up differently from normal methods [\[2\]](https://docs.python.org/3/library/unittest.mock.html#id9)
, this support has been specially implemented. This means that only specific magic methods are supported. The supported list includes _almost_ all of them. If there are any missing that you need please let us know.

You mock magic methods by setting the method you are interested in to a function or a mock instance. If you are using a function then it _must_ take `self` as the first argument [\[3\]](https://docs.python.org/3/library/unittest.mock.html#id10)
.

Copy

\>>> def \_\_str\_\_(self):
...     return 'fooble'
...
\>>> mock \= Mock()
\>>> mock.\_\_str\_\_ \= \_\_str\_\_
\>>> str(mock)
'fooble'

Copy

\>>> mock \= Mock()
\>>> mock.\_\_str\_\_ \= Mock()
\>>> mock.\_\_str\_\_.return\_value \= 'fooble'
\>>> str(mock)
'fooble'

Copy

\>>> mock \= Mock()
\>>> mock.\_\_iter\_\_ \= Mock(return\_value\=iter(\[\]))
\>>> list(mock)
\[\]

One use case for this is for mocking objects used as context managers in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement:

Copy

\>>> mock \= Mock()
\>>> mock.\_\_enter\_\_ \= Mock(return\_value\='foo')
\>>> mock.\_\_exit\_\_ \= Mock(return\_value\=False)
\>>> with mock as m:
...     assert m \== 'foo'
...
\>>> mock.\_\_enter\_\_.assert\_called\_with()
\>>> mock.\_\_exit\_\_.assert\_called\_with(None, None, None)

Calls to magic methods do not appear in [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
, but they are recorded in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
.

Note

If you use the _spec_ keyword argument to create a mock then attempting to set a magic method that isn’t in the spec will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

The full list of supported magic methods is:

*   `__hash__`, `__sizeof__`, `__repr__` and `__str__`
    
*   `__dir__`, `__format__` and `__subclasses__`
    
*   `__round__`, `__floor__`, `__trunc__` and `__ceil__`
    
*   Comparisons: `__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__` and `__ne__`
    
*   Container methods: `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__len__`, `__iter__`, `__reversed__` and `__missing__`
    
*   Context manager: `__enter__`, `__exit__`, `__aenter__` and `__aexit__`
    
*   Unary numeric methods: `__neg__`, `__pos__` and `__invert__`
    
*   The numeric methods (including right hand and in-place variants): `__add__`, `__sub__`, `__mul__`, `__matmul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__divmod__`, `__lshift__`, `__rshift__`, `__and__`, `__xor__`, `__or__`, and `__pow__`
    
*   Numeric conversion methods: `__complex__`, `__int__`, `__float__` and `__index__`
    
*   Descriptor methods: `__get__`, `__set__` and `__delete__`
    
*   Pickling: `__reduce__`, `__reduce_ex__`, `__getinitargs__`, `__getnewargs__`, `__getstate__` and `__setstate__`
    
*   File system path representation: `__fspath__`
    
*   Asynchronous iteration methods: `__aiter__` and `__anext__`
    

Changed in version 3.8: Added support for [`os.PathLike.__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__")
.

Changed in version 3.8: Added support for `__aenter__`, `__aexit__`, `__aiter__` and `__anext__`.

The following methods exist but are _not_ supported as they are either in use by mock, can’t be set dynamically, or can cause problems:

*   `__getattr__`, `__setattr__`, `__init__` and `__new__`
    
*   `__prepare__`, `__instancecheck__`, `__subclasscheck__`, `__del__`
    

### Magic Mock[¶](https://docs.python.org/3/library/unittest.mock.html#magic-mock "Link to this heading")

There are two `MagicMock` variants: [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 and [`NonCallableMagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "unittest.mock.NonCallableMagicMock")
.

class unittest.mock.MagicMock(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "Link to this definition")

`MagicMock` is a subclass of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 with default implementations of most of the [magic methods](https://docs.python.org/3/glossary.html#term-magic-method)
. You can use `MagicMock` without having to configure the magic methods yourself.

The constructor parameters have the same meaning as for [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
.

If you use the _spec_ or _spec\_set_ arguments then _only_ magic methods that exist in the spec will be created.

class unittest.mock.NonCallableMagicMock(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "Link to this definition")

A non-callable version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
.

The constructor parameters have the same meaning as for [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
, with the exception of _return\_value_ and _side\_effect_ which have no meaning on a non-callable mock.

The magic methods are setup with [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 objects, so you can configure them and use them in the usual way:

Copy

\>>> mock \= MagicMock()
\>>> mock\[3\] \= 'fish'
\>>> mock.\_\_setitem\_\_.assert\_called\_with(3, 'fish')
\>>> mock.\_\_getitem\_\_.return\_value \= 'result'
\>>> mock\[2\]
'result'

By default many of the protocol methods are required to return objects of a specific type. These methods are preconfigured with a default return value, so that they can be used without you having to do anything if you aren’t interested in the return value. You can still _set_ the return value manually if you want to change the default.

Methods and their defaults:

*   `__lt__`: [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
    
*   `__gt__`: `NotImplemented`
    
*   `__le__`: `NotImplemented`
    
*   `__ge__`: `NotImplemented`
    
*   `__int__`: `1`
    
*   `__contains__`: `False`
    
*   `__len__`: `0`
    
*   `__iter__`: `iter([])`
    
*   `__exit__`: `False`
    
*   `__aexit__`: `False`
    
*   `__complex__`: `1j`
    
*   `__float__`: `1.0`
    
*   `__bool__`: `True`
    
*   `__index__`: `1`
    
*   `__hash__`: default hash for the mock
    
*   `__str__`: default str for the mock
    
*   `__sizeof__`: default sizeof for the mock
    

For example:

Copy

\>>> mock \= MagicMock()
\>>> int(mock)
1
\>>> len(mock)
0
\>>> list(mock)
\[\]
\>>> object() in mock
False

The two equality methods, `__eq__()` and `__ne__()`, are special. They do the default equality comparison on identity, using the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 attribute, unless you change their return value to return something else:

Copy

\>>> MagicMock() \== 3
False
\>>> MagicMock() != 3
True
\>>> mock \= MagicMock()
\>>> mock.\_\_eq\_\_.return\_value \= True
\>>> mock \== 3
True

The return value of `__iter__()` can be any iterable object and isn’t required to be an iterator:

Copy

\>>> mock \= MagicMock()
\>>> mock.\_\_iter\_\_.return\_value \= \['a', 'b', 'c'\]
\>>> list(mock)
\['a', 'b', 'c'\]
\>>> list(mock)
\['a', 'b', 'c'\]

If the return value _is_ an iterator, then iterating over it once will consume it and subsequent iterations will result in an empty list:

Copy

\>>> mock.\_\_iter\_\_.return\_value \= iter(\['a', 'b', 'c'\])
\>>> list(mock)
\['a', 'b', 'c'\]
\>>> list(mock)
\[\]

`MagicMock` has all of the supported magic methods configured except for some of the obscure and obsolete ones. You can still set these up if you want.

Magic methods that are supported but not setup by default in `MagicMock` are:

*   `__subclasses__`
    
*   `__dir__`
    
*   `__format__`
    
*   `__get__`, `__set__` and `__delete__`
    
*   `__reversed__` and `__missing__`
    
*   `__reduce__`, `__reduce_ex__`, `__getinitargs__`, `__getnewargs__`, `__getstate__` and `__setstate__`
    
*   `__getformat__`
    

Helpers[¶](https://docs.python.org/3/library/unittest.mock.html#helpers "Link to this heading")

------------------------------------------------------------------------------------------------

### sentinel[¶](https://docs.python.org/3/library/unittest.mock.html#sentinel "Link to this heading")

unittest.mock.sentinel[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.sentinel "Link to this definition")

The `sentinel` object provides a convenient way of providing unique objects for your tests.

Attributes are created on demand when you access them by name. Accessing the same attribute will always return the same object. The objects returned have a sensible repr so that test failure messages are readable.

Changed in version 3.7: The `sentinel` attributes now preserve their identity when they are [`copied`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
 or [`pickled`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
.

Sometimes when testing you need to test that a specific object is passed as an argument to another method, or returned. It can be common to create named sentinel objects to test this. [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 provides a convenient way of creating and testing the identity of objects like this.

In this example we monkey patch `method` to return `sentinel.some_object`:

Copy

\>>> real \= ProductionClass()
\>>> real.method \= Mock(name\="method")
\>>> real.method.return\_value \= sentinel.some\_object
\>>> result \= real.method()
\>>> assert result is sentinel.some\_object
\>>> result
sentinel.some\_object

### DEFAULT[¶](https://docs.python.org/3/library/unittest.mock.html#default "Link to this heading")

unittest.mock.DEFAULT[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "Link to this definition")

The `DEFAULT` object is a pre-created sentinel (actually `sentinel.DEFAULT`). It can be used by [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 functions to indicate that the normal return value should be used.

### call[¶](https://docs.python.org/3/library/unittest.mock.html#call "Link to this heading")

unittest.mock.call(_\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "Link to this definition")

`call()` is a helper object for making simpler assertions, for comparing with [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
, [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
, [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 and [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
. `call()` can also be used with [`assert_has_calls()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "unittest.mock.Mock.assert_has_calls")
.

Copy

\>>> m \= MagicMock(return\_value\=None)
\>>> m(1, 2, a\='foo', b\='bar')
\>>> m()
\>>> m.call\_args\_list \== \[call(1, 2, a\='foo', b\='bar'), call()\]
True

call.call\_list()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call.call_list "Link to this definition")

For a call object that represents multiple calls, `call_list()` returns a list of all the intermediate calls as well as the final call.

`call_list` is particularly useful for making assertions on “chained calls”. A chained call is multiple calls on a single line of code. This results in multiple entries in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 on a mock. Manually constructing the sequence of calls can be tedious.

[`call_list()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call.call_list "unittest.mock.call.call_list")
 can construct the sequence of calls from the same chained call:

Copy

\>>> m \= MagicMock()
\>>> m(1).method(arg\='foo').other('bar')(2.0)
<MagicMock name='mock().method().other()()' id='...'>
\>>> kall \= call(1).method(arg\='foo').other('bar')(2.0)
\>>> kall.call\_list()
\[call(1),\
 call().method(arg='foo'),\
 call().method().other('bar'),\
 call().method().other()(2.0)\]
\>>> m.mock\_calls \== kall.call\_list()
True

A `call` object is either a tuple of (positional args, keyword args) or (name, positional args, keyword args) depending on how it was constructed. When you construct them yourself this isn’t particularly interesting, but the `call` objects that are in the [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
, [`Mock.call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
 and [`Mock.mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 attributes can be introspected to get at the individual arguments they contain.

The `call` objects in [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
 and [`Mock.call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
 are two-tuples of (positional args, keyword args) whereas the `call` objects in [`Mock.mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
, along with ones you construct yourself, are three-tuples of (name, positional args, keyword args).

You can use their “tupleness” to pull out the individual arguments for more complex introspection and assertions. The positional arguments are a tuple (an empty tuple if there are no positional arguments) and the keyword arguments are a dictionary:

Copy

\>>> m \= MagicMock(return\_value\=None)
\>>> m(1, 2, 3, arg\='one', arg2\='two')
\>>> kall \= m.call\_args
\>>> kall.args
(1, 2, 3)
\>>> kall.kwargs
{'arg': 'one', 'arg2': 'two'}
\>>> kall.args is kall\[0\]
True
\>>> kall.kwargs is kall\[1\]
True

Copy

\>>> m \= MagicMock()
\>>> m.foo(4, 5, 6, arg\='two', arg2\='three')
<MagicMock name='mock.foo()' id='...'>
\>>> kall \= m.mock\_calls\[0\]
\>>> name, args, kwargs \= kall
\>>> name
'foo'
\>>> args
(4, 5, 6)
\>>> kwargs
{'arg': 'two', 'arg2': 'three'}
\>>> name is m.mock\_calls\[0\]\[0\]
True

### create\_autospec[¶](https://docs.python.org/3/library/unittest.mock.html#create-autospec "Link to this heading")

unittest.mock.create\_autospec(_spec_, _spec\_set\=False_, _instance\=False_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "Link to this definition")

Create a mock object using another object as a spec. Attributes on the mock will use the corresponding attribute on the _spec_ object as their spec.

Functions or methods being mocked will have their arguments checked to ensure that they are called with the correct signature.

If _spec\_set_ is `True` then attempting to set attributes that don’t exist on the spec object will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

If a class is used as a spec then the return value of the mock (the instance of the class) will have the same spec. You can use a class as the spec for an instance object by passing `instance=True`. The returned mock will only be callable if instances of the mock are callable.

`create_autospec()` also takes arbitrary keyword arguments that are passed to the constructor of the created mock.

See [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
 for examples of how to use auto-speccing with [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")
 and the _autospec_ argument to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
.

Changed in version 3.8: [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")
 now returns an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock")
 if the target is an async function.

### ANY[¶](https://docs.python.org/3/library/unittest.mock.html#any "Link to this heading")

unittest.mock.ANY[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "Link to this definition")

Sometimes you may need to make assertions about _some_ of the arguments in a call to mock, but either not care about some of the arguments or want to pull them individually out of [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args")
 and make more complex assertions on them.

To ignore certain arguments you can pass in objects that compare equal to _everything_. Calls to [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
 and [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with")
 will then succeed no matter what was passed in.

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock('foo', bar\=object())
\>>> mock.assert\_called\_once\_with('foo', bar\=ANY)

[`ANY`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "unittest.mock.ANY")
 can also be used in comparisons with call lists like [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
:

Copy

\>>> m \= MagicMock(return\_value\=None)
\>>> m(1)
\>>> m(1, 2)
\>>> m(object())
\>>> m.mock\_calls \== \[call(1), call(1, 2), ANY\]
True

[`ANY`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "unittest.mock.ANY")
 is not limited to comparisons with call objects and so can also be used in test assertions:

Copy

class TestStringMethods(unittest.TestCase):

    def test\_split(self):
        s \= 'hello world'
        self.assertEqual(s.split(), \['hello', ANY\])

### FILTER\_DIR[¶](https://docs.python.org/3/library/unittest.mock.html#filter-dir "Link to this heading")

unittest.mock.FILTER\_DIR[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "Link to this definition")

[`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR")
 is a module level variable that controls the way mock objects respond to [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")
. The default is `True`, which uses the filtering described below, to only show useful members. If you dislike this filtering, or need to switch it off for diagnostic purposes, then set `mock.FILTER_DIR = False`.

With filtering on, `dir(some_mock)` shows only useful attributes and will include any dynamically created attributes that wouldn’t normally be shown. If the mock was created with a _spec_ (or _autospec_ of course) then all the attributes from the original are shown, even if they haven’t been accessed yet:

Copy

\>>> dir(Mock())
\['assert\_any\_call',\
 'assert\_called',\
 'assert\_called\_once',\
 'assert\_called\_once\_with',\
 'assert\_called\_with',\
 'assert\_has\_calls',\
 'assert\_not\_called',\
 'attach\_mock',\
 ...\
\>>> from urllib import request\
\>>> dir(Mock(spec\=request))\
\['AbstractBasicAuthHandler',\
 'AbstractDigestAuthHandler',\
 'AbstractHTTPHandler',\
 'BaseHandler',\
 ...\
\
Many of the not-very-useful (private to [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")\
 rather than the thing being mocked) underscore and double underscore prefixed attributes have been filtered from the result of calling [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")\
 on a `Mock`. If you dislike this behaviour you can switch it off by setting the module level switch [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR")\
:\
\
Copy\
\
\>>> from unittest import mock\
\>>> mock.FILTER\_DIR \= False\
\>>> dir(mock.Mock())\
\['\_NonCallableMock\_\_get\_return\_value',\
 '\_NonCallableMock\_\_get\_side\_effect',\
 '\_NonCallableMock\_\_return\_value\_doc',\
 '\_NonCallableMock\_\_set\_return\_value',\
 '\_NonCallableMock\_\_set\_side\_effect',\
 '\_\_call\_\_',\
 '\_\_class\_\_',\
 ...\
\
Alternatively you can just use `vars(my_mock)` (instance members) and `dir(type(my_mock))` (type members) to bypass the filtering irrespective of [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR")\
.\
\
### mock\_open[¶](https://docs.python.org/3/library/unittest.mock.html#mock-open "Link to this heading")\
\
unittest.mock.mock\_open(_mock\=None_, _read\_data\=''_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open "Link to this definition")\
\
A helper function to create a mock to replace the use of [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")\
. It works for `open()` called directly or used as a context manager.\
\
The _mock_ argument is the mock object to configure. If `None` (the default) then a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")\
 will be created for you, with the API limited to methods or attributes available on standard file handles.\
\
_read\_data_ is a string for the [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read")\
, [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")\
, and [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines")\
 methods of the file handle to return. Calls to those methods will take data from _read\_data_ until it is depleted. The mock of these methods is pretty simplistic: every time the _mock_ is called, the _read\_data_ is rewound to the start. If you need more control over the data that you are feeding to the tested code you will need to customize this mock for yourself. When that is insufficient, one of the in-memory filesystem packages on [PyPI](https://pypi.org/)\
 can offer a realistic filesystem for testing.\
\
Changed in version 3.4: Added [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")\
 and [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines")\
 support. The mock of [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read")\
 changed to consume _read\_data_ rather than returning it on each call.\
\
Changed in version 3.5: _read\_data_ is now reset on each call to the _mock_.\
\
Changed in version 3.8: Added [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")\
 to implementation so that iteration (such as in for loops) correctly consumes _read\_data_.\
\
Using [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")\
 as a context manager is a great way to ensure your file handles are closed properly and is becoming common:\
\
Copy\
\
with open('/some/path', 'w') as f:\
    f.write('something')\
\
The issue is that even if you mock out the call to [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")\
 it is the _returned object_ that is used as a context manager (and has [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")\
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")\
 called).\
\
Mocking context managers with a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")\
 is common enough and fiddly enough that a helper function is useful.\
\
Copy\
\
\>>> m \= mock\_open()\
\>>> with patch('\_\_main\_\_.open', m):\
...     with open('foo', 'w') as h:\
...         h.write('some stuff')\
...\
\>>> m.mock\_calls\
\[call('foo', 'w'),\
 call().\_\_enter\_\_(),\
 call().write('some stuff'),\
 call().\_\_exit\_\_(None, None, None)\]\
\>>> m.assert\_called\_once\_with('foo', 'w')\
\>>> handle \= m()\
\>>> handle.write.assert\_called\_once\_with('some stuff')\
\
And for reading files:\
\
Copy\
\
\>>> with patch('\_\_main\_\_.open', mock\_open(read\_data\='bibble')) as m:\
...     with open('foo') as h:\
...         result \= h.read()\
...\
\>>> m.assert\_called\_once\_with('foo')\
\>>> assert result \== 'bibble'\
\
### Autospeccing[¶](https://docs.python.org/3/library/unittest.mock.html#autospeccing "Link to this heading")\
\
Autospeccing is based on the existing `spec` feature of mock. It limits the api of mocks to the api of an original object (the spec), but it is recursive (implemented lazily) so that attributes of mocks only have the same api as the attributes of the spec. In addition mocked functions / methods have the same call signature as the original so they raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")\
 if they are called incorrectly.\
\
Before I explain how auto-speccing works, here’s why it is needed.\
\
[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")\
 is a very powerful and flexible object, but it suffers from a flaw which is general to mocking. If you refactor some of your code, rename members and so on, any tests for code that is still using the _old api_ but uses mocks instead of the real objects will still pass. This means your tests can all pass even though your code is broken.\
\
Changed in version 3.5: Before 3.5, tests with a typo in the word assert would silently pass when they should raise an error. You can still achieve this behavior by passing `unsafe=True` to Mock.\
\
Note that this is another reason why you need integration tests as well as unit tests. Testing everything in isolation is all fine and dandy, but if you don’t test how your units are “wired together” there is still lots of room for bugs that tests might have caught.\
\
`unittest.mock` already provides a feature to help with this, called speccing. If you use a class or instance as the `spec` for a mock then you can only access attributes on the mock that exist on the real class:\
\
Copy\
\
\>>> from urllib import request\
\>>> mock \= Mock(spec\=request.Request)\
\>>> mock.assret\_called\_with  \# Intentional typo!\
Traceback (most recent call last):\
 ...\
AttributeError: Mock object has no attribute 'assret\_called\_with'\
\
The spec only applies to the mock itself, so we still have the same issue with any methods on the mock:\
\
Copy\
\
\>>> mock.header\_items()\
<mock.Mock object at 0x...>\
\>>> mock.header\_items.assret\_called\_with()  \# Intentional typo!\
\
Auto-speccing solves this problem. You can either pass `autospec=True` to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")\
 / [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")\
 or use the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")\
 function to create a mock with a spec. If you use the `autospec=True` argument to `patch()` then the object that is being replaced will be used as the spec object. Because the speccing is done “lazily” (the spec is created as attributes on the mock are accessed) you can use it with very complex or deeply nested objects (like modules that import modules that import modules) without a big performance hit.\
\
Here’s an example of it in use:\
\
Copy\
\
\>>> from urllib import request\
\>>> patcher \= patch('\_\_main\_\_.request', autospec\=True)\
\>>> mock\_request \= patcher.start()\
\>>> request is mock\_request\
True\
\>>> mock\_request.Request\
<MagicMock name='request.Request' spec='Request' id='...'>\
\
You can see that `request.Request` has a spec. `request.Request` takes two arguments in the constructor (one of which is _self_). Here’s what happens if we try to call it incorrectly:\
\
Copy\
\
\>>> req \= request.Request()\
Traceback (most recent call last):\
 ...\
TypeError: <lambda>() takes at least 2 arguments (1 given)\
\
The spec also applies to instantiated classes (i.e. the return value of specced mocks):\
\
Copy\
\
\>>> req \= request.Request('foo')\
\>>> req\
<NonCallableMagicMock name='request.Request()' spec='Request' id='...'>\
\
`Request` objects are not callable, so the return value of instantiating our mocked out `request.Request` is a non-callable mock. With the spec in place any typos in our asserts will raise the correct error:\
\
Copy\
\
\>>> req.add\_header('spam', 'eggs')\
<MagicMock name='request.Request().add\_header()' id='...'>\
\>>> req.add\_header.assret\_called\_with  \# Intentional typo!\
Traceback (most recent call last):\
 ...\
AttributeError: Mock object has no attribute 'assret\_called\_with'\
\>>> req.add\_header.assert\_called\_with('spam', 'eggs')\
\
In many cases you will just be able to add `autospec=True` to your existing [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")\
 calls and then be protected against bugs due to typos and api changes.\
\
As well as using _autospec_ through [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")\
 there is a [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec")\
 for creating autospecced mocks directly:\
\
Copy\
\
\>>> from urllib import request\
\>>> mock\_request \= create\_autospec(request)\
\>>> mock\_request.Request('foo', 'bar')\
<NonCallableMagicMock name='mock.Request()' spec='Request' id='...'>\
\
This isn’t without caveats and limitations however, which is why it is not the default behaviour. In order to know what attributes are available on the spec object, autospec has to introspect (access attributes) the spec. As you traverse attributes on the mock a corresponding traversal of the original object is happening under the hood. If any of your specced objects have properties or descriptors that can trigger code execution then you may not be able to use autospec. On the other hand it is much better to design your objects so that introspection is safe [\[4\]](https://docs.python.org/3/library/unittest.mock.html#id12)\
.\
\
A more serious problem is that it is common for instance attributes to be created in the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")\
 method and not to exist on the class at all. _autospec_ can’t know about any dynamically created attributes and restricts the api to visible attributes.\
\
Copy\
\
\>>> class Something:\
...   def \_\_init\_\_(self):\
...     self.a \= 33\
...\
\>>> with patch('\_\_main\_\_.Something', autospec\=True):\
...   thing \= Something()\
...   thing.a\
...\
Traceback (most recent call last):\
  ...\
AttributeError: Mock object has no attribute 'a'\
\
There are a few different ways of resolving this problem. The easiest, but not necessarily the least annoying, way is to simply set the required attributes on the mock after creation. Just because _autospec_ doesn’t allow you to fetch attributes that don’t exist on the spec it doesn’t prevent you setting them:\
\
Copy\
\
\>>> with patch('\_\_main\_\_.Something', autospec\=True):\
...   thing \= Something()\
...   thing.a \= 33\
...\
\
There is a more aggressive version of both _spec_ and _autospec_ that _does_ prevent you setting non-existent attributes. This is useful if you want to ensure your code only _sets_ valid attributes too, but obviously it prevents this particular scenario:\
\
Copy\
\
\>>> with patch('\_\_main\_\_.Something', autospec\=True, spec\_set\=True):\
...   thing \= Something()\
...   thing.a \= 33\
...\
Traceback (most recent call last):\
 ...\
AttributeError: Mock object has no attribute 'a'\
\
Probably the best way of solving the problem is to add class attributes as default values for instance members initialised in [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")\
. Note that if you are only setting default attributes in `__init__()` then providing them via class attributes (shared between instances of course) is faster too. e.g.\
\
Copy\
\
class Something:\
    a \= 33\
\
This brings up another issue. It is relatively common to provide a default value of `None` for members that will later be an object of a different type. `None` would be useless as a spec because it wouldn’t let you access _any_ attributes or methods on it. As `None` is _never_ going to be useful as a spec, and probably indicates a member that will normally of some other type, autospec doesn’t use a spec for members that are set to `None`. These will just be ordinary mocks (well - MagicMocks):\
\
Copy\
\
\>>> class Something:\
...     member \= None\
...\
\>>> mock \= create\_autospec(Something)\
\>>> mock.member.foo.bar.baz()\
<MagicMock name='mock.member.foo.bar.baz()' id='...'>\
\
If modifying your production classes to add defaults isn’t to your liking then there are more options. One of these is simply to use an instance as the spec rather than the class. The other is to create a subclass of the production class and add the defaults to the subclass without affecting the production class. Both of these require you to use an alternative object as the spec. Thankfully [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")\
 supports this - you can simply pass the alternative object as the _autospec_ argument:\
\
Copy\
\
\>>> class Something:\
...   def \_\_init\_\_(self):\
...     self.a \= 33\
...\
\>>> class SomethingForTest(Something):\
...   a \= 33\
...\
\>>> p \= patch('\_\_main\_\_.Something', autospec\=SomethingForTest)\
\>>> mock \= p.start()\
\>>> mock.a\
<NonCallableMagicMock name='Something.a' spec='int' id='...'>\
\
### Sealing mocks[¶](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks "Link to this heading")\
\
unittest.mock.seal(_mock_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.seal "Link to this definition")\
\
Seal will disable the automatic creation of mocks when accessing an attribute of the mock being sealed or any of its attributes that are already mocks recursively.\
\
If a mock instance with a name or a spec is assigned to an attribute it won’t be considered in the sealing chain. This allows one to prevent seal from fixing part of the mock object.\
\
Copy\
\
\>>> mock \= Mock()\
\>>> mock.submock.attribute1 \= 2\
\>>> mock.not\_submock \= mock.Mock(name\="sample\_name")\
\>>> seal(mock)\
\>>> mock.new\_attribute  \# This will raise AttributeError.\
\>>> mock.submock.attribute2  \# This will raise AttributeError.\
\>>> mock.not\_submock.attribute2  \# This won't raise.\
\
Added in version 3.7.\
\
Order of precedence of `side_effect`, `return_value` and _wraps_[¶](https://docs.python.org/3/library/unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The order of their precedence is:\
\
1.  [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")\
    \
2.  [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")\
    \
3.  _wraps_\
    \
\
If all three are set, mock will return the value from [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")\
, ignoring [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")\
 and the wrapped object altogether. If any two are set, the one with the higher precedence will return the value. Regardless of the order of which was set first, the order of precedence remains unchanged.\
\
Copy\
\
\>>> from unittest.mock import Mock\
\>>> class Order:\
...     @staticmethod\
...     def get\_value():\
...         return "third"\
...\
\>>> order\_mock \= Mock(spec\=Order, wraps\=Order)\
\>>> order\_mock.get\_value.side\_effect \= \["first"\]\
\>>> order\_mock.get\_value.return\_value \= "second"\
\>>> order\_mock.get\_value()\
'first'\
\
As `None` is the default value of [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")\
, if you reassign its value back to `None`, the order of precedence will be checked between [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")\
 and the wrapped object, ignoring `side_effect`.\
\
Copy\
\
\>>> order\_mock.get\_value.side\_effect \= None\
\>>> order\_mock.get\_value()\
'second'\
\
If the value being returned by [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")\
 is [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")\
, it is ignored and the order of precedence moves to the successor to obtain the value to return.\
\
Copy\
\
\>>> from unittest.mock import DEFAULT\
\>>> order\_mock.get\_value.side\_effect \= \[DEFAULT\]\
\>>> order\_mock.get\_value()\
'second'\
\
When [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")\
 wraps an object, the default value of [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")\
 will be [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT")\
.\
\
Copy\
\
\>>> order\_mock \= Mock(spec\=Order, wraps\=Order)\
\>>> order\_mock.return\_value\
sentinel.DEFAULT\
\>>> order\_mock.get\_value.return\_value\
sentinel.DEFAULT\
\
The order of precedence will ignore this value and it will move to the last successor which is the wrapped object.\
\
As the real call is being made to the wrapped object, creating an instance of this mock will return the real instance of the class. The positional arguments, if any, required by the wrapped object must be passed.\
\
Copy\
\
\>>> order\_mock\_instance \= order\_mock()\
\>>> isinstance(order\_mock\_instance, Order)\
True\
\>>> order\_mock\_instance.get\_value()\
'third'\
\
Copy\
\
\>>> order\_mock.get\_value.return\_value \= DEFAULT\
\>>> order\_mock.get\_value()\
'third'\
\
Copy\
\
\>>> order\_mock.get\_value.return\_value \= "second"\
\>>> order\_mock.get\_value()\
'second'\
\
But if you assign `None` to it, this will not be ignored as it is an explicit assignment. So, the order of precedence will not move to the wrapped object.\
\
Copy\
\
\>>> order\_mock.get\_value.return\_value \= None\
\>>> order\_mock.get\_value() is None\
True\
\
Even if you set all three at once when initializing the mock, the order of precedence remains the same:\
\
Copy\
\
\>>> order\_mock \= Mock(spec\=Order, wraps\=Order,\
...                   \*\*{"get\_value.side\_effect": \["first"\],\
...                      "get\_value.return\_value": "second"}\
...                   )\
...\
\>>> order\_mock.get\_value()\
'first'\
\>>> order\_mock.get\_value.side\_effect \= None\
\>>> order\_mock.get\_value()\
'second'\
\>>> order\_mock.get\_value.return\_value \= DEFAULT\
\>>> order\_mock.get\_value()\
'third'\
\
If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")\
 is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)\
, the order of precedence will not cause a value to be obtained from the successors. Instead, `StopIteration` exception is raised.\
\
Copy\
\
\>>> order\_mock \= Mock(spec\=Order, wraps\=Order)\
\>>> order\_mock.get\_value.side\_effect \= \["first side effect value",\
...                                     "another side effect value"\]\
\>>> order\_mock.get\_value.return\_value \= "second"\
\
Copy\
\
\>>> order\_mock.get\_value()\
'first side effect value'\
\>>> order\_mock.get\_value()\
'another side effect value'\
\
Copy\
\
\>>> order\_mock.get\_value()\
Traceback (most recent call last):\
 ...\
StopIteration\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html#)\
    *   [Quick Guide](https://docs.python.org/3/library/unittest.mock.html#quick-guide)\
        \
    *   [The Mock Class](https://docs.python.org/3/library/unittest.mock.html#the-mock-class)\
        *   [Calling](https://docs.python.org/3/library/unittest.mock.html#calling)\
            \
        *   [Deleting Attributes](https://docs.python.org/3/library/unittest.mock.html#deleting-attributes)\
            \
        *   [Mock names and the name attribute](https://docs.python.org/3/library/unittest.mock.html#mock-names-and-the-name-attribute)\
            \
        *   [Attaching Mocks as Attributes](https://docs.python.org/3/library/unittest.mock.html#attaching-mocks-as-attributes)\
            \
    *   [The patchers](https://docs.python.org/3/library/unittest.mock.html#the-patchers)\
        *   [patch](https://docs.python.org/3/library/unittest.mock.html#patch)\
            \
        *   [patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object)\
            \
        *   [patch.dict](https://docs.python.org/3/library/unittest.mock.html#patch-dict)\
            \
        *   [patch.multiple](https://docs.python.org/3/library/unittest.mock.html#patch-multiple)\
            \
        *   [patch methods: start and stop](https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop)\
            \
        *   [patch builtins](https://docs.python.org/3/library/unittest.mock.html#patch-builtins)\
            \
        *   [TEST\_PREFIX](https://docs.python.org/3/library/unittest.mock.html#test-prefix)\
            \
        *   [Nesting Patch Decorators](https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators)\
            \
        *   [Where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)\
            \
        *   [Patching Descriptors and Proxy Objects](https://docs.python.org/3/library/unittest.mock.html#patching-descriptors-and-proxy-objects)\
            \
    *   [MagicMock and magic method support](https://docs.python.org/3/library/unittest.mock.html#magicmock-and-magic-method-support)\
        *   [Mocking Magic Methods](https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods)\
            \
        *   [Magic Mock](https://docs.python.org/3/library/unittest.mock.html#magic-mock)\
            \
    *   [Helpers](https://docs.python.org/3/library/unittest.mock.html#helpers)\
        *   [sentinel](https://docs.python.org/3/library/unittest.mock.html#sentinel)\
            \
        *   [DEFAULT](https://docs.python.org/3/library/unittest.mock.html#default)\
            \
        *   [call](https://docs.python.org/3/library/unittest.mock.html#call)\
            \
        *   [create\_autospec](https://docs.python.org/3/library/unittest.mock.html#create-autospec)\
            \
        *   [ANY](https://docs.python.org/3/library/unittest.mock.html#any)\
            \
        *   [FILTER\_DIR](https://docs.python.org/3/library/unittest.mock.html#filter-dir)\
            \
        *   [mock\_open](https://docs.python.org/3/library/unittest.mock.html#mock-open)\
            \
        *   [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#autospeccing)\
            \
        *   [Sealing mocks](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks)\
            \
    *   [Order of precedence of `side_effect`, `return_value` and _wraps_](https://docs.python.org/3/library/unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps)\
        \
\
#### Previous topic\
\
[`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html "previous chapter")\
\
#### Next topic\
\
[`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest.mock+%E2%80%94+mock+object+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.mock.html&pagesource=library%2Funittest.mock.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/unittest.mock.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/library/unittest.mock-examples.html "unittest.mock — getting started")\
     |\
*   [previous](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [Development Tools](https://docs.python.org/3/library/development.html)\
     »\
*   [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |