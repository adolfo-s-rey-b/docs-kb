### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/test.html "test — Regression tests package for Python")
     |
*   [previous](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library")
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
*   [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`unittest.mock` — getting started[¶](https://docs.python.org/3/library/unittest.mock-examples.html#unittest-mock-getting-started "Link to this heading")

=========================================================================================================================================================

Added in version 3.3.

Using Mock[¶](https://docs.python.org/3/library/unittest.mock-examples.html#using-mock "Link to this heading")

---------------------------------------------------------------------------------------------------------------

### Mock patching methods[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mock-patching-methods "Link to this heading")

Common uses for [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 objects include:

*   Patching methods
    
*   Recording method calls on objects
    

You might want to replace a method on an object to check that it is called with the correct arguments by another part of the system:

Copy

\>>> real \= SomeClass()
\>>> real.method \= MagicMock(name\='method')
\>>> real.method(3, 4, 5, key\='value')
<MagicMock name='method()' id='...'>

Once our mock has been used (`real.method` in this example) it has methods and attributes that allow you to make assertions about how it has been used.

Note

In most of these examples the [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 and [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 classes are interchangeable. As the `MagicMock` is the more capable class it makes a sensible one to use by default.

Once the mock has been called its [`called`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.called "unittest.mock.Mock.called")
 attribute is set to `True`. More importantly we can use the [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
 or [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with")
 method to check that it was called with the correct arguments.

This example tests that calling `ProductionClass().method` results in a call to the `something` method:

Copy

\>>> class ProductionClass:
...     def method(self):
...         self.something(1, 2, 3)
...     def something(self, a, b, c):
...         pass
...
\>>> real \= ProductionClass()
\>>> real.something \= MagicMock()
\>>> real.method()
\>>> real.something.assert\_called\_once\_with(1, 2, 3)

### Mock for method calls on an object[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mock-for-method-calls-on-an-object "Link to this heading")

In the last example we patched a method directly on an object to check that it was called correctly. Another common use case is to pass an object into a method (or some part of the system under test) and then check that it is used in the correct way.

The simple `ProductionClass` below has a `closer` method. If it is called with an object then it calls `close` on it.

Copy

\>>> class ProductionClass:
...     def closer(self, something):
...         something.close()
...

So to test it we need to pass in an object with a `close` method and check that it was called correctly.

Copy

\>>> real \= ProductionClass()
\>>> mock \= Mock()
\>>> real.closer(mock)
\>>> mock.close.assert\_called\_with()

We don’t have to do any work to provide the ‘close’ method on our mock. Accessing close creates it. So, if ‘close’ hasn’t already been called then accessing it in the test will create it, but [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
 will raise a failure exception.

### Mocking classes[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-classes "Link to this heading")

A common use case is to mock out classes instantiated by your code under test. When you patch a class, then that class is replaced with a mock. Instances are created by _calling the class_. This means you access the “mock instance” by looking at the return value of the mocked class.

In the example below we have a function `some_function` that instantiates `Foo` and calls a method on it. The call to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 replaces the class `Foo` with a mock. The `Foo` instance is the result of calling the mock, so it is configured by modifying the mock [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
.

Copy

\>>> def some\_function():
...     instance \= module.Foo()
...     return instance.method()
...
\>>> with patch('module.Foo') as mock:
...     instance \= mock.return\_value
...     instance.method.return\_value \= 'the result'
...     result \= some\_function()
...     assert result \== 'the result'

### Naming your mocks[¶](https://docs.python.org/3/library/unittest.mock-examples.html#naming-your-mocks "Link to this heading")

It can be useful to give your mocks a name. The name is shown in the repr of the mock and can be helpful when the mock appears in test failure messages. The name is also propagated to attributes or methods of the mock:

Copy

\>>> mock \= MagicMock(name\='foo')
\>>> mock
<MagicMock name='foo' id='...'>
\>>> mock.method
<MagicMock name='foo.method' id='...'>

### Tracking all calls[¶](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-all-calls "Link to this heading")

Often you want to track more than a single call to a method. The [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 attribute records all calls to child attributes of the mock - and also to their children.

Copy

\>>> mock \= MagicMock()
\>>> mock.method()
<MagicMock name='mock.method()' id='...'>
\>>> mock.attribute.method(10, x\=53)
<MagicMock name='mock.attribute.method()' id='...'>
\>>> mock.mock\_calls
\[call.method(), call.attribute.method(10, x=53)\]

If you make an assertion about `mock_calls` and any unexpected methods have been called, then the assertion will fail. This is useful because as well as asserting that the calls you expected have been made, you are also checking that they were made in the right order and with no additional calls:

You use the [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 object to construct lists for comparing with `mock_calls`:

Copy

\>>> expected \= \[call.method(), call.attribute.method(10, x\=53)\]
\>>> mock.mock\_calls \== expected
True

However, parameters to calls that return mocks are not recorded, which means it is not possible to track nested calls where the parameters used to create ancestors are important:

Copy

\>>> m \= Mock()
\>>> m.factory(important\=True).deliver()
<Mock name='mock.factory().deliver()' id='...'>
\>>> m.mock\_calls\[\-1\] \== call.factory(important\=False).deliver()
True

### Setting return values and attributes[¶](https://docs.python.org/3/library/unittest.mock-examples.html#setting-return-values-and-attributes "Link to this heading")

Setting the return values on a mock object is trivially easy:

Copy

\>>> mock \= Mock()
\>>> mock.return\_value \= 3
\>>> mock()
3

Of course you can do the same for methods on the mock:

Copy

\>>> mock \= Mock()
\>>> mock.method.return\_value \= 3
\>>> mock.method()
3

The return value can also be set in the constructor:

Copy

\>>> mock \= Mock(return\_value\=3)
\>>> mock()
3

If you need an attribute setting on your mock, just do it:

Copy

\>>> mock \= Mock()
\>>> mock.x \= 3
\>>> mock.x
3

Sometimes you want to mock up a more complex situation, like for example `mock.connection.cursor().execute("SELECT 1")`. If we wanted this call to return a list, then we have to configure the result of the nested call.

We can use [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 to construct the set of calls in a “chained call” like this for easy assertion afterwards:

Copy

\>>> mock \= Mock()
\>>> cursor \= mock.connection.cursor.return\_value
\>>> cursor.execute.return\_value \= \['foo'\]
\>>> mock.connection.cursor().execute("SELECT 1")
\['foo'\]
\>>> expected \= call.connection.cursor().execute("SELECT 1").call\_list()
\>>> mock.mock\_calls
\[call.connection.cursor(), call.connection.cursor().execute('SELECT 1')\]
\>>> mock.mock\_calls \== expected
True

It is the call to `.call_list()` that turns our call object into a list of calls representing the chained calls.

### Raising exceptions with mocks[¶](https://docs.python.org/3/library/unittest.mock-examples.html#raising-exceptions-with-mocks "Link to this heading")

A useful attribute is [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
. If you set this to an exception class or instance then the exception will be raised when the mock is called.

Copy

\>>> mock \= Mock(side\_effect\=Exception('Boom!'))
\>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

### Side effect functions and iterables[¶](https://docs.python.org/3/library/unittest.mock-examples.html#side-effect-functions-and-iterables "Link to this heading")

`side_effect` can also be set to a function or an iterable. The use case for `side_effect` as an iterable is where your mock is going to be called several times, and you want each call to return a different value. When you set `side_effect` to an iterable every call to the mock returns the next value from the iterable:

Copy

\>>> mock \= MagicMock(side\_effect\=\[4, 5, 6\])
\>>> mock()
4
\>>> mock()
5
\>>> mock()
6

For more advanced use cases, like dynamically varying the return values depending on what the mock is called with, `side_effect` can be a function. The function will be called with the same arguments as the mock. Whatever the function returns is what the call returns:

Copy

\>>> vals \= {(1, 2): 1, (2, 3): 2}
\>>> def side\_effect(\*args):
...     return vals\[args\]
...
\>>> mock \= MagicMock(side\_effect\=side\_effect)
\>>> mock(1, 2)
1
\>>> mock(2, 3)
2

### Mocking asynchronous iterators[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-iterators "Link to this heading")

Since Python 3.8, `AsyncMock` and `MagicMock` have support to mock [Asynchronous Iterators](https://docs.python.org/3/reference/datamodel.html#async-iterators)
 through `__aiter__`. The [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 attribute of `__aiter__` can be used to set the return values to be used for iteration.

Copy

\>>> mock \= MagicMock()  \# AsyncMock also works here
\>>> mock.\_\_aiter\_\_.return\_value \= \[1, 2, 3\]
\>>> async def main():
...     return \[i async for i in mock\]
...
\>>> asyncio.run(main())
\[1, 2, 3\]

### Mocking asynchronous context manager[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-context-manager "Link to this heading")

Since Python 3.8, `AsyncMock` and `MagicMock` have support to mock [Asynchronous Context Managers](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
 through `__aenter__` and `__aexit__`. By default, `__aenter__` and `__aexit__` are `AsyncMock` instances that return an async function.

Copy

\>>> class AsyncContextManager:
...     async def \_\_aenter\_\_(self):
...         return self
...     async def \_\_aexit\_\_(self, exc\_type, exc, tb):
...         pass
...
\>>> mock\_instance \= MagicMock(AsyncContextManager())  \# AsyncMock also works here
\>>> async def main():
...     async with mock\_instance as result:
...         pass
...
\>>> asyncio.run(main())
\>>> mock\_instance.\_\_aenter\_\_.assert\_awaited\_once()
\>>> mock\_instance.\_\_aexit\_\_.assert\_awaited\_once()

### Creating a mock from an existing object[¶](https://docs.python.org/3/library/unittest.mock-examples.html#creating-a-mock-from-an-existing-object "Link to this heading")

One problem with over use of mocking is that it couples your tests to the implementation of your mocks rather than your real code. Suppose you have a class that implements `some_method`. In a test for another class, you provide a mock of this object that _also_ provides `some_method`. If later you refactor the first class, so that it no longer has `some_method` - then your tests will continue to pass even though your code is now broken!

[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 allows you to provide an object as a specification for the mock, using the _spec_ keyword argument. Accessing methods / attributes on the mock that don’t exist on your specification object will immediately raise an attribute error. If you change the implementation of your specification, then tests that use that class will start failing immediately without you having to instantiate the class in those tests.

Copy

\>>> mock \= Mock(spec\=SomeClass)
\>>> mock.old\_method()
Traceback (most recent call last):
   ...
AttributeError: Mock object has no attribute 'old\_method'. Did you mean: 'class\_method'?

Using a specification also enables a smarter matching of calls made to the mock, regardless of whether some parameters were passed as positional or named arguments:

Copy

\>>> def f(a, b, c): pass
...
\>>> mock \= Mock(spec\=f)
\>>> mock(1, 2, 3)
<Mock name='mock()' id='140161580456576'>
\>>> mock.assert\_called\_with(a\=1, b\=2, c\=3)

If you want this smarter matching to also work with method calls on the mock, you can use [auto-speccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing)
.

If you want a stronger form of specification that prevents the setting of arbitrary attributes as well as the getting of them then you can use _spec\_set_ instead of _spec_.

### Using side\_effect to return per file content[¶](https://docs.python.org/3/library/unittest.mock-examples.html#using-side-effect-to-return-per-file-content "Link to this heading")

[`mock_open()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open "unittest.mock.mock_open")
 is used to patch [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 method. [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 can be used to return a new Mock object per call. This can be used to return different contents per file stored in a dictionary:

Copy

DEFAULT \= "default"
data\_dict \= {"file1": "data1",
             "file2": "data2"}

def open\_side\_effect(name):
    return mock\_open(read\_data\=data\_dict.get(name, DEFAULT))()

with patch("builtins.open", side\_effect\=open\_side\_effect):
    with open("file1") as file1:
        assert file1.read() \== "data1"

    with open("file2") as file2:
        assert file2.read() \== "data2"

    with open("file3") as file2:
        assert file2.read() \== "default"

Patch decorators[¶](https://docs.python.org/3/library/unittest.mock-examples.html#patch-decorators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Note

With [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 it matters that you patch objects in the namespace where they are looked up. This is normally straightforward, but for a quick guide read [where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
.

A common need in tests is to patch a class attribute or a module attribute, for example patching a builtin or patching a class in a module to test that it is instantiated. Modules and classes are effectively global, so patching on them has to be undone after the test or the patch will persist into other tests and cause hard to diagnose problems.

mock provides three convenient decorators for this: [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
, [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
 and [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
. `patch` takes a single string, of the form `package.module.Class.attribute` to specify the attribute you are patching. It also optionally takes a value that you want the attribute (or class or whatever) to be replaced with. ‘patch.object’ takes an object and the name of the attribute you would like patched, plus optionally the value to patch it with.

`patch.object`:

Copy

\>>> original \= SomeClass.attribute
\>>> @patch.object(SomeClass, 'attribute', sentinel.attribute)
... def test():
...     assert SomeClass.attribute \== sentinel.attribute
...
\>>> test()
\>>> assert SomeClass.attribute \== original

\>>> @patch('package.module.attribute', sentinel.attribute)
... def test():
...     from package.module import attribute
...     assert attribute is sentinel.attribute
...
\>>> test()

If you are patching a module (including [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
) then use [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 instead of [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
:

Copy

\>>> mock \= MagicMock(return\_value\=sentinel.file\_handle)
\>>> with patch('builtins.open', mock):
...     handle \= open('filename', 'r')
...
\>>> mock.assert\_called\_with('filename', 'r')
\>>> assert handle \== sentinel.file\_handle, "incorrect file handle returned"

The module name can be ‘dotted’, in the form `package.module` if needed:

Copy

\>>> @patch('package.module.ClassName.attribute', sentinel.attribute)
... def test():
...     from package.module import ClassName
...     assert ClassName.attribute \== sentinel.attribute
...
\>>> test()

A nice pattern is to actually decorate test methods themselves:

Copy

\>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'attribute', sentinel.attribute)
...     def test\_something(self):
...         self.assertEqual(SomeClass.attribute, sentinel.attribute)
...
\>>> original \= SomeClass.attribute
\>>> MyTest('test\_something').test\_something()
\>>> assert SomeClass.attribute \== original

If you want to patch with a Mock, you can use [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 with only one argument (or [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object")
 with two arguments). The mock will be created for you and passed into the test function / method:

Copy

\>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'static\_method')
...     def test\_something(self, mock\_method):
...         SomeClass.static\_method()
...         mock\_method.assert\_called\_with()
...
\>>> MyTest('test\_something').test\_something()

You can stack up multiple patch decorators using this pattern:

Copy

\>>> class MyTest(unittest.TestCase):
...     @patch('package.module.ClassName1')
...     @patch('package.module.ClassName2')
...     def test\_something(self, MockClass2, MockClass1):
...         self.assertIs(package.module.ClassName1, MockClass1)
...         self.assertIs(package.module.ClassName2, MockClass2)
...
\>>> MyTest('test\_something').test\_something()

When you nest patch decorators the mocks are passed in to the decorated function in the same order they applied (the normal _Python_ order that decorators are applied). This means from the bottom up, so in the example above the mock for `package.module.ClassName2` is passed in first.

There is also [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 for setting values in a dictionary just during a scope and restoring the dictionary to its original state when the test ends:

Copy

\>>> foo \= {'key': 'value'}
\>>> original \= foo.copy()
\>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear\=True):
...     assert foo \== {'newkey': 'newvalue'}
...
\>>> assert foo \== original

`patch`, `patch.object` and `patch.dict` can all be used as context managers.

Where you use [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 to create a mock for you, you can get a reference to the mock using the “as” form of the with statement:

Copy

\>>> class ProductionClass:
...     def method(self):
...         pass
...
\>>> with patch.object(ProductionClass, 'method') as mock\_method:
...     mock\_method.return\_value \= None
...     real \= ProductionClass()
...     real.method(1, 2, 3)
...
\>>> mock\_method.assert\_called\_with(1, 2, 3)

As an alternative `patch`, `patch.object` and `patch.dict` can be used as class decorators. When used in this way it is the same as applying the decorator individually to every method whose name starts with “test”.

Further examples[¶](https://docs.python.org/3/library/unittest.mock-examples.html#further-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Here are some more examples for some slightly more advanced scenarios.

### Mocking chained calls[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls "Link to this heading")

Mocking chained calls is actually straightforward with mock once you understand the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
 attribute. When a mock is called for the first time, or you fetch its `return_value` before it has been called, a new [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 is created.

This means that you can see how the object returned from a call to a mocked object has been used by interrogating the `return_value` mock:

Copy

\>>> mock \= Mock()
\>>> mock().foo(a\=2, b\=3)
<Mock name='mock().foo()' id='...'>
\>>> mock.return\_value.foo.assert\_called\_with(a\=2, b\=3)

From here it is a simple step to configure and then make assertions about chained calls. Of course another alternative is writing your code in a more testable way in the first place…

So, suppose we have some code that looks a little bit like this:

Copy

\>>> class Something:
...     def \_\_init\_\_(self):
...         self.backend \= BackendProvider()
...     def method(self):
...         response \= self.backend.get\_endpoint('foobar').create\_call('spam', 'eggs').start\_call()
...         \# more code

Assuming that `BackendProvider` is already well tested, how do we test `method()`? Specifically, we want to test that the code section `# more code` uses the response object in the correct way.

As this chain of calls is made from an instance attribute we can monkey patch the `backend` attribute on a `Something` instance. In this particular case we are only interested in the return value from the final call to `start_call` so we don’t have much configuration to do. Let’s assume the object it returns is ‘file-like’, so we’ll ensure that our response object uses the builtin [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 as its `spec`.

To do this we create a mock instance as our mock backend and create a mock response object for it. To set the response as the return value for that final `start_call` we could do this:

Copy

mock\_backend.get\_endpoint.return\_value.create\_call.return\_value.start\_call.return\_value \= mock\_response

We can do that in a slightly nicer way using the [`configure_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "unittest.mock.Mock.configure_mock")
 method to directly set the return value for us:

Copy

\>>> something \= Something()
\>>> mock\_response \= Mock(spec\=open)
\>>> mock\_backend \= Mock()
\>>> config \= {'get\_endpoint.return\_value.create\_call.return\_value.start\_call.return\_value': mock\_response}
\>>> mock\_backend.configure\_mock(\*\*config)

With these we monkey patch the “mock backend” in place and can make the real call:

Copy

\>>> something.backend \= mock\_backend
\>>> something.method()

Using [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 we can check the chained call with a single assert. A chained call is several calls in one line of code, so there will be several entries in `mock_calls`. We can use [`call.call_list()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call.call_list "unittest.mock.call.call_list")
 to create this list of calls for us:

Copy

\>>> chained \= call.get\_endpoint('foobar').create\_call('spam', 'eggs').start\_call()
\>>> call\_list \= chained.call\_list()
\>>> assert mock\_backend.mock\_calls \== call\_list

### Partial mocking[¶](https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking "Link to this heading")

For some tests, you may want to mock out a call to [`datetime.date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today "datetime.date.today")
 to return a known date, but don’t want to prevent the code under test from creating new date objects. Unfortunately [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 is written in C, so you cannot just monkey-patch out the static `datetime.date.today()` method.

Instead, you can effectively wrap the date class with a mock, while passing through calls to the constructor to the real class (and returning real instances).

The [`patch decorator`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 is used here to mock out the `date` class in the module under test. The [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 attribute on the mock date class is then set to a lambda function that returns a real date. When the mock date class is called a real date will be constructed and returned by `side_effect`.

Copy

\>>> import datetime as dt
\>>> with patch('mymodule.date') as mock\_date:
...     mock\_date.today.return\_value \= dt.date(2010, 10, 8)
...     mock\_date.side\_effect \= lambda \*args, \*\*kw: dt.date(\*args, \*\*kw)
...
...     assert mymodule.date.today() \== dt.date(2010, 10, 8)
...     assert mymodule.date(2009, 6, 8) \== dt.date(2009, 6, 8)

Note that we don’t patch [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 globally, we patch `date` in the module that _uses_ it. See [where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
.

When `date.today()` is called a known date is returned, but calls to the `date(...)` constructor still return normal dates. Without this you can find yourself having to calculate an expected result using exactly the same algorithm as the code under test, which is a classic testing anti-pattern.

Calls to the date constructor are recorded in the `mock_date` attributes (`call_count` and friends) which may also be useful for your tests.

An alternative way of dealing with mocking dates, or other builtin classes, is discussed in [this blog entry](https://williambert.online/2011/07/how-to-unit-testing-in-django-with-mocking-and-patching/)
.

### Mocking a generator method[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-generator-method "Link to this heading")

A Python generator is a function or method that uses the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 statement to return a series of values when iterated over [\[1\]](https://docs.python.org/3/library/unittest.mock-examples.html#id3)
.

A generator method / function is called to return the generator object. It is the generator object that is then iterated over. The protocol method for iteration is [`__iter__()`](https://docs.python.org/3/builtins/stdtypes.html#container.__iter__ "container.__iter__")
, so we can mock this using a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
.

Here’s an example class with an “iter” method implemented as a generator:

Copy

\>>> class Foo:
...     def iter(self):
...         for i in \[1, 2, 3\]:
...             yield i
...
\>>> foo \= Foo()
\>>> list(foo.iter())
\[1, 2, 3\]

How would we mock this class, and in particular its “iter” method?

To configure the values returned from the iteration (implicit in the call to [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
), we need to configure the object returned by the call to `foo.iter()`.

Copy

\>>> mock\_foo \= MagicMock()
\>>> mock\_foo.iter.return\_value \= iter(\[1, 2, 3\])
\>>> list(mock\_foo.iter())
\[1, 2, 3\]

### Applying the same patch to every test method[¶](https://docs.python.org/3/library/unittest.mock-examples.html#applying-the-same-patch-to-every-test-method "Link to this heading")

If you want several patches in place for multiple test methods the obvious way is to apply the patch decorators to every method. This can feel like unnecessary repetition. Instead, you can use [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 (in all its various forms) as a class decorator. This applies the patches to all test methods on the class. A test method is identified by methods whose names start with `test`:

Copy

\>>> @patch('mymodule.SomeClass')
... class MyTest(unittest.TestCase):
...
...     def test\_one(self, MockSomeClass):
...         self.assertIs(mymodule.SomeClass, MockSomeClass)
...
...     def test\_two(self, MockSomeClass):
...         self.assertIs(mymodule.SomeClass, MockSomeClass)
...
...     def not\_a\_test(self):
...         return 'something'
...
\>>> MyTest('test\_one').test\_one()
\>>> MyTest('test\_two').test\_two()
\>>> MyTest('test\_two').not\_a\_test()
'something'

An alternative way of managing patches is to use the [patch methods: start and stop](https://docs.python.org/3/library/unittest.mock.html#start-and-stop)
. These allow you to move the patching into your `setUp` and `tearDown` methods.

Copy

\>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         self.patcher \= patch('mymodule.foo')
...         self.mock\_foo \= self.patcher.start()
...
...     def test\_foo(self):
...         self.assertIs(mymodule.foo, self.mock\_foo)
...
...     def tearDown(self):
...         self.patcher.stop()
...
\>>> MyTest('test\_foo').run()

If you use this technique you must ensure that the patching is “undone” by calling `stop`. This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called. [`unittest.TestCase.addCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup")
 makes this easier:

Copy

\>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         patcher \= patch('mymodule.foo')
...         self.addCleanup(patcher.stop)
...         self.mock\_foo \= patcher.start()
...
...     def test\_foo(self):
...         self.assertIs(mymodule.foo, self.mock\_foo)
...
\>>> MyTest('test\_foo').run()

### Mocking unbound methods[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-unbound-methods "Link to this heading")

Sometimes a test needs to patch an _unbound method_, which means patching the method on the class rather than on the instance. In order to make assertions about which objects were calling this particular method, you need to pass `self` as the first argument. The issue is that you can’t patch with a mock for this, because if you replace an unbound method with a mock it doesn’t become a bound method when fetched from the instance, and so it doesn’t get `self` passed in. The workaround is to patch the unbound method with a real function instead. The [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch")
 decorator makes it so simple to patch out methods with a mock that having to create a real function becomes a nuisance.

If you pass `autospec=True` to patch then it does the patching with a _real_ function object. This function object has the same signature as the one it is replacing, but delegates to a mock under the hood. You still get your mock auto-created in exactly the same way as before. What it means though, is that if you use it to patch out an unbound method on a class the mocked function will be turned into a bound method if it is fetched from an instance. It will have `self` passed in as the first argument, which is exactly what was needed:

Copy

\>>> class Foo:
...   def foo(self):
...     pass
...
\>>> with patch.object(Foo, 'foo', autospec\=True) as mock\_foo:
...   mock\_foo.return\_value \= 'foo'
...   foo \= Foo()
...   foo.foo()
...
'foo'
\>>> mock\_foo.assert\_called\_once\_with(foo)

If we don’t use `autospec=True` then the unbound method is patched out with a Mock instance instead, and isn’t called with `self`.

### Checking multiple calls with mock[¶](https://docs.python.org/3/library/unittest.mock-examples.html#checking-multiple-calls-with-mock "Link to this heading")

mock has a nice API for making assertions about how your mock objects are used.

Copy

\>>> mock \= Mock()
\>>> mock.foo\_bar.return\_value \= None
\>>> mock.foo\_bar('baz', spam\='eggs')
\>>> mock.foo\_bar.assert\_called\_with('baz', spam\='eggs')

If your mock is only being called once you can use the [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with")
 method that also asserts that the [`call_count`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count "unittest.mock.Mock.call_count")
 is one.

Copy

\>>> mock.foo\_bar.assert\_called\_once\_with('baz', spam\='eggs')
\>>> mock.foo\_bar()
\>>> mock.foo\_bar.assert\_called\_once\_with('baz', spam\='eggs')
Traceback (most recent call last):
    ...
AssertionError: Expected 'foo\_bar' to be called once. Called 2 times.
Calls: \[call('baz', spam='eggs'), call()\].

Both `assert_called_with` and `assert_called_once_with` make assertions about the _most recent_ call. If your mock is going to be called several times, and you want to make assertions about _all_ those calls you can use [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
:

Copy

\>>> mock \= Mock(return\_value\=None)
\>>> mock(1, 2, 3)
\>>> mock(4, 5, 6)
\>>> mock()
\>>> mock.call\_args\_list
\[call(1, 2, 3), call(4, 5, 6), call()\]

The [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 helper makes it easy to make assertions about these calls. You can build up a list of expected calls and compare it to `call_args_list`. This looks remarkably similar to the repr of the `call_args_list`:

Copy

\>>> expected \= \[call(1, 2, 3), call(4, 5, 6), call()\]
\>>> mock.call\_args\_list \== expected
True

### Coping with mutable arguments[¶](https://docs.python.org/3/library/unittest.mock-examples.html#coping-with-mutable-arguments "Link to this heading")

Another situation is rare, but can bite you, is when your mock is called with mutable arguments. `call_args` and `call_args_list` store _references_ to the arguments. If the arguments are mutated by the code under test then you can no longer make assertions about what the values were when the mock was called.

Here’s some example code that shows the problem. Imagine the following functions defined in ‘mymodule’:

Copy

def frob(val):
    pass

def grob(val):
    "First frob and then clear val"
    frob(val)
    val.clear()

When we try to test that `grob` calls `frob` with the correct argument look what happens:

Copy

\>>> with patch('mymodule.frob') as mock\_frob:
...     val \= {6}
...     mymodule.grob(val)
...
\>>> val
set()
\>>> mock\_frob.assert\_called\_with({6})
Traceback (most recent call last):
    ...
AssertionError: Expected: (({6},), {})
Called with: ((set(),), {})

One possibility would be for mock to copy the arguments you pass in. This could then cause problems if you do assertions that rely on object identity for equality.

Here’s one solution that uses the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 functionality. If you provide a `side_effect` function for a mock then `side_effect` will be called with the same args as the mock. This gives us an opportunity to copy the arguments and store them for later assertions. In this example we’re using _another_ mock to store the arguments so that we can use the mock methods for doing the assertion. Again a helper function sets this up for us.

Copy

\>>> from copy import deepcopy
\>>> from unittest.mock import Mock, patch, DEFAULT
\>>> def copy\_call\_args(mock):
...     new\_mock \= Mock()
...     def side\_effect(\*args, \*\*kwargs):
...         args \= deepcopy(args)
...         kwargs \= deepcopy(kwargs)
...         new\_mock(\*args, \*\*kwargs)
...         return DEFAULT
...     mock.side\_effect \= side\_effect
...     return new\_mock
...
\>>> with patch('mymodule.frob') as mock\_frob:
...     new\_mock \= copy\_call\_args(mock\_frob)
...     val \= {6}
...     mymodule.grob(val)
...
\>>> new\_mock.assert\_called\_with({6})
\>>> new\_mock.call\_args
call({6})

`copy_call_args` is called with the mock that will be called. It returns a new mock that we do the assertion on. The `side_effect` function makes a copy of the args and calls our `new_mock` with the copy.

Note

If your mock is only going to be used once there is an easier way of checking arguments at the point they are called. You can simply do the checking inside a `side_effect` function.

Copy

\>>> def side\_effect(arg):
...     assert arg \== {6}
...
\>>> mock \= Mock(side\_effect\=side\_effect)
\>>> mock({6})
\>>> mock(set())
Traceback (most recent call last):
    ...
AssertionError

An alternative approach is to create a subclass of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 or [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
 that copies (using [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy")
) the arguments. Here’s an example implementation:

Copy

\>>> from copy import deepcopy
\>>> class CopyingMock(MagicMock):
...     def \_\_call\_\_(self, /, \*args, \*\*kwargs):
...         args \= deepcopy(args)
...         kwargs \= deepcopy(kwargs)
...         return super().\_\_call\_\_(\*args, \*\*kwargs)
...
\>>> c \= CopyingMock(return\_value\=None)
\>>> arg \= set()
\>>> c(arg)
\>>> arg.add(1)
\>>> c.assert\_called\_with(set())
\>>> c.assert\_called\_with(arg)
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock({1})
Actual: mock(set())
\>>> c.foo
<CopyingMock name='mock.foo' id='...'>

When you subclass `Mock` or `MagicMock` all dynamically created attributes, and the `return_value` will use your subclass automatically. That means all children of a `CopyingMock` will also have the type `CopyingMock`.

### Nesting patches[¶](https://docs.python.org/3/library/unittest.mock-examples.html#nesting-patches "Link to this heading")

Using patch as a context manager is nice, but if you do multiple patches you can end up with nested with statements indenting further and further to the right:

Copy

\>>> class MyTest(unittest.TestCase):
...
...     def test\_foo(self):
...         with patch('mymodule.Foo') as mock\_foo:
...             with patch('mymodule.Bar') as mock\_bar:
...                 with patch('mymodule.Spam') as mock\_spam:
...                     assert mymodule.Foo is mock\_foo
...                     assert mymodule.Bar is mock\_bar
...                     assert mymodule.Spam is mock\_spam
...
\>>> original \= mymodule.Foo
\>>> MyTest('test\_foo').test\_foo()
\>>> assert mymodule.Foo is original

With unittest `cleanup` functions and the [patch methods: start and stop](https://docs.python.org/3/library/unittest.mock.html#start-and-stop)
 we can achieve the same effect without the nested indentation. A simple helper method, `create_patch`, puts the patch in place and returns the created mock for us:

Copy

\>>> class MyTest(unittest.TestCase):
...
...     def create\_patch(self, name):
...         patcher \= patch(name)
...         thing \= patcher.start()
...         self.addCleanup(patcher.stop)
...         return thing
...
...     def test\_foo(self):
...         mock\_foo \= self.create\_patch('mymodule.Foo')
...         mock\_bar \= self.create\_patch('mymodule.Bar')
...         mock\_spam \= self.create\_patch('mymodule.Spam')
...
...         assert mymodule.Foo is mock\_foo
...         assert mymodule.Bar is mock\_bar
...         assert mymodule.Spam is mock\_spam
...
\>>> original \= mymodule.Foo
\>>> MyTest('test\_foo').run()
\>>> assert mymodule.Foo is original

### Mocking a dictionary with MagicMock[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-dictionary-with-magicmock "Link to this heading")

You may want to mock a dictionary, or other container object, recording all access to it whilst having it still behave like a dictionary.

We can do this with [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock")
, which will behave like a dictionary, and using [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
 to delegate dictionary access to a real underlying dictionary that is under our control.

When the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 and [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
 methods of our `MagicMock` are called (normal dictionary access) then `side_effect` is called with the key (and in the case of `__setitem__` the value too). We can also control what is returned.

After the `MagicMock` has been used we can use attributes like [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list")
 to assert about how the dictionary was used:

Copy

\>>> my\_dict \= {'a': 1, 'b': 2, 'c': 3}
\>>> def getitem(name):
...      return my\_dict\[name\]
...
\>>> def setitem(name, val):
...     my\_dict\[name\] \= val
...
\>>> mock \= MagicMock()
\>>> mock.\_\_getitem\_\_.side\_effect \= getitem
\>>> mock.\_\_setitem\_\_.side\_effect \= setitem

Note

An alternative to using `MagicMock` is to use `Mock` and _only_ provide the magic methods you specifically want:

Copy

\>>> mock \= Mock()
\>>> mock.\_\_getitem\_\_ \= Mock(side\_effect\=getitem)
\>>> mock.\_\_setitem\_\_ \= Mock(side\_effect\=setitem)

A _third_ option is to use `MagicMock` but passing in `dict` as the _spec_ (or _spec\_set_) argument so that the `MagicMock` created only has dictionary magic methods available:

Copy

\>>> mock \= MagicMock(spec\_set\=dict)
\>>> mock.\_\_getitem\_\_.side\_effect \= getitem
\>>> mock.\_\_setitem\_\_.side\_effect \= setitem

With these side effect functions in place, the `mock` will behave like a normal dictionary but recording the access. It even raises a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if you try to access a key that doesn’t exist.

Copy

\>>> mock\['a'\]
1
\>>> mock\['c'\]
3
\>>> mock\['d'\]
Traceback (most recent call last):
    ...
KeyError: 'd'
\>>> mock\['b'\] \= 'fish'
\>>> mock\['d'\] \= 'eggs'
\>>> mock\['b'\]
'fish'
\>>> mock\['d'\]
'eggs'

After it has been used you can make assertions about the access using the normal mock methods and attributes:

Copy

\>>> mock.\_\_getitem\_\_.call\_args\_list
\[call('a'), call('c'), call('d'), call('b'), call('d')\]
\>>> mock.\_\_setitem\_\_.call\_args\_list
\[call('b', 'fish'), call('d', 'eggs')\]
\>>> my\_dict
{'a': 1, 'b': 'fish', 'c': 3, 'd': 'eggs'}

### Mock subclasses and their attributes[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mock-subclasses-and-their-attributes "Link to this heading")

There are various reasons why you might want to subclass [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
. One reason might be to add helper methods. Here’s a silly example:

Copy

\>>> class MyMock(MagicMock):
...     def has\_been\_called(self):
...         return self.called
...
\>>> mymock \= MyMock(return\_value\=None)
\>>> mymock
<MyMock id='...'>
\>>> mymock.has\_been\_called()
False
\>>> mymock()
\>>> mymock.has\_been\_called()
True

The standard behaviour for `Mock` instances is that attributes and the return value mocks are of the same type as the mock they are accessed on. This ensures that `Mock` attributes are `Mocks` and `MagicMock` attributes are `MagicMocks` [\[2\]](https://docs.python.org/3/library/unittest.mock-examples.html#id5)
. So if you’re subclassing to add helper methods then they’ll also be available on the attributes and return value mock of instances of your subclass.

Copy

\>>> mymock.foo
<MyMock name='mock.foo' id='...'>
\>>> mymock.foo.has\_been\_called()
False
\>>> mymock.foo()
<MyMock name='mock.foo()' id='...'>
\>>> mymock.foo.has\_been\_called()
True

Sometimes this is inconvenient. For example, [one user](https://code.google.com/archive/p/mock/issues/105)
 is subclassing mock to created a [Twisted adaptor](https://twisted.org/documents/11.0.0/api/twisted.python.components.html)
. Having this applied to attributes too actually causes errors.

`Mock` (in all its flavours) uses a method called `_get_child_mock` to create these “sub-mocks” for attributes and return values. You can prevent your subclass being used for attributes by overriding this method. The signature is that it takes arbitrary keyword arguments (`**kwargs`) which are then passed onto the mock constructor:

Copy

\>>> class Subclass(MagicMock):
...     def \_get\_child\_mock(self, /, \*\*kwargs):
...         return MagicMock(\*\*kwargs)
...
\>>> mymock \= Subclass()
\>>> mymock.foo
<MagicMock name='mock.foo' id='...'>
\>>> assert isinstance(mymock, Subclass)
\>>> assert not isinstance(mymock.foo, Subclass)
\>>> assert not isinstance(mymock(), Subclass)

### Mocking imports with patch.dict[¶](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-imports-with-patch-dict "Link to this heading")

One situation where mocking can be hard is where you have a local import inside a function. These are harder to mock because they aren’t using an object from the module namespace that we can patch out.

Generally local imports are to be avoided. They are sometimes done to prevent circular dependencies, for which there is _usually_ a much better way to solve the problem (refactor the code) or to prevent “up front costs” by delaying the import. This can also be solved in better ways than an unconditional local import (store the module as a class or module attribute and only do the import on first use).

That aside there is a way to use `mock` to affect the results of an import. Importing fetches an _object_ from the [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
 dictionary. Note that it fetches an _object_, which need not be a module. Importing a module for the first time results in a module object being put in `sys.modules`, so usually when you import something you get a module back. This need not be the case however.

This means you can use [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict")
 to _temporarily_ put a mock in place in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
. Any imports whilst this patch is active will fetch the mock. When the patch is complete (the decorated function exits, the with statement body is complete or `patcher.stop()` is called) then whatever was there previously will be restored safely.

Here’s an example that mocks out the ‘fooble’ module.

Copy

\>>> import sys
\>>> mock \= Mock()
\>>> with patch.dict('sys.modules', {'fooble': mock}):
...    import fooble
...    fooble.blob()
...
<Mock name='mock.blob()' id='...'>
\>>> assert 'fooble' not in sys.modules
\>>> mock.blob.assert\_called\_once\_with()

As you can see the `import fooble` succeeds, but on exit there is no ‘fooble’ left in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
.

This also works for the `from module import name` form:

Copy

\>>> mock \= Mock()
\>>> with patch.dict('sys.modules', {'fooble': mock}):
...    from fooble import blob
...    blob.blip()
...
<Mock name='mock.blob.blip()' id='...'>
\>>> mock.blob.blip.assert\_called\_once\_with()

With slightly more work you can also mock package imports:

Copy

\>>> mock \= Mock()
\>>> modules \= {'package': mock, 'package.module': mock.module}
\>>> with patch.dict('sys.modules', modules):
...    from package.module import fooble
...    fooble()
...
<Mock name='mock.module.fooble()' id='...'>
\>>> mock.module.fooble.assert\_called\_once\_with()

### Tracking order of calls and less verbose call assertions[¶](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-order-of-calls-and-less-verbose-call-assertions "Link to this heading")

The [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock")
 class allows you to track the _order_ of method calls on your mock objects through the [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls")
 attribute. This doesn’t allow you to track the order of calls between separate mock objects, however we can use [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 to achieve the same effect.

Because mocks track calls to child mocks in `mock_calls`, and accessing an arbitrary attribute of a mock creates a child mock, we can create our separate mocks from a parent one. Calls to those child mock will then all be recorded, in order, in the `mock_calls` of the parent:

Copy

\>>> manager \= Mock()
\>>> mock\_foo \= manager.foo
\>>> mock\_bar \= manager.bar

Copy

\>>> mock\_foo.something()
<Mock name='mock.foo.something()' id='...'>
\>>> mock\_bar.other.thing()
<Mock name='mock.bar.other.thing()' id='...'>

Copy

\>>> manager.mock\_calls
\[call.foo.something(), call.bar.other.thing()\]

We can then assert about the calls, including the order, by comparing with the `mock_calls` attribute on the manager mock:

Copy

\>>> expected\_calls \= \[call.foo.something(), call.bar.other.thing()\]
\>>> manager.mock\_calls \== expected\_calls
True

If `patch` is creating, and putting in place, your mocks then you can attach them to a manager mock using the [`attach_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.attach_mock "unittest.mock.Mock.attach_mock")
 method. After attaching calls will be recorded in `mock_calls` of the manager.

Copy

\>>> manager \= MagicMock()
\>>> with patch('mymodule.Class1') as MockClass1:
...     with patch('mymodule.Class2') as MockClass2:
...         manager.attach\_mock(MockClass1, 'MockClass1')
...         manager.attach\_mock(MockClass2, 'MockClass2')
...         MockClass1().foo()
...         MockClass2().bar()
<MagicMock name='mock.MockClass1().foo()' id='...'>
<MagicMock name='mock.MockClass2().bar()' id='...'>
\>>> manager.mock\_calls
\[call.MockClass1(),\
call.MockClass1().foo(),\
call.MockClass2(),\
call.MockClass2().bar()\]

If many calls have been made, but you’re only interested in a particular sequence of them then an alternative is to use the [`assert_has_calls()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "unittest.mock.Mock.assert_has_calls")
 method. This takes a list of calls (constructed with the [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call")
 object). If that sequence of calls are in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls")
 then the assert succeeds.

Copy

\>>> m \= MagicMock()
\>>> m().foo().bar().baz()
<MagicMock name='mock().foo().bar().baz()' id='...'>
\>>> m.one().two().three()
<MagicMock name='mock.one().two().three()' id='...'>
\>>> calls \= call.one().two().three().call\_list()
\>>> m.assert\_has\_calls(calls)

Even though the chained call `m.one().two().three()` aren’t the only calls that have been made to the mock, the assert still succeeds.

Sometimes a mock may have several calls made to it, and you are only interested in asserting about _some_ of those calls. You may not even care about the order. In this case you can pass `any_order=True` to `assert_has_calls`:

Copy

\>>> m \= MagicMock()
\>>> m(1), m.two(2, 3), m.seven(7), m.fifty('50')
(...)
\>>> calls \= \[call.fifty('50'), call(1), call.seven(7)\]
\>>> m.assert\_has\_calls(calls, any\_order\=True)

### More complex argument matching[¶](https://docs.python.org/3/library/unittest.mock-examples.html#more-complex-argument-matching "Link to this heading")

Using the same basic concept as [`ANY`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "unittest.mock.ANY")
 we can implement matchers to do more complex assertions on objects used as arguments to mocks.

Suppose we expect some object to be passed to a mock that by default compares equal based on object identity (which is the Python default for user defined classes). To use [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with")
 we would need to pass in the exact same object. If we are only interested in some of the attributes of this object then we can create a matcher that will check these attributes for us.

You can see in this example how a ‘standard’ call to `assert_called_with` isn’t sufficient:

Copy

\>>> class Foo:
...     def \_\_init\_\_(self, a, b):
...         self.a, self.b \= a, b
...
\>>> mock \= Mock(return\_value\=None)
\>>> mock(Foo(1, 2))
\>>> mock.assert\_called\_with(Foo(1, 2))
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock(<\_\_main\_\_.Foo object at 0x...>)
Actual: mock(<\_\_main\_\_.Foo object at 0x...>)

A comparison function for our `Foo` class might look something like this:

Copy

\>>> def compare(self, other):
...     if not type(self) \== type(other):
...         return False
...     if self.a != other.a:
...         return False
...     if self.b != other.b:
...         return False
...     return True
...

And a matcher object that can use comparison functions like this for its equality operation would look something like this:

Copy

\>>> class Matcher:
...     def \_\_init\_\_(self, compare, some\_obj):
...         self.compare \= compare
...         self.some\_obj \= some\_obj
...     def \_\_eq\_\_(self, other):
...         return self.compare(self.some\_obj, other)
...

Putting all this together:

Copy

\>>> match\_foo \= Matcher(compare, Foo(1, 2))
\>>> mock.assert\_called\_with(match\_foo)

The `Matcher` is instantiated with our compare function and the `Foo` object we want to compare against. In `assert_called_with` the `Matcher` equality method will be called, which compares the object the mock was called with against the one we created our matcher with. If they match then `assert_called_with` passes, and if they don’t an [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
 is raised:

Copy

\>>> match\_wrong \= Matcher(compare, Foo(3, 4))
\>>> mock.assert\_called\_with(match\_wrong)
Traceback (most recent call last):
    ...
AssertionError: Expected: ((<Matcher object at 0x...>,), {})
Called with: ((<Foo object at 0x...>,), {})

With a bit of tweaking you could have the comparison function raise the [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
 directly and provide a more useful failure message.

As of version 1.5, the Python testing library [PyHamcrest](https://pyhamcrest.readthedocs.io/)
 provides similar functionality, that may be useful here, in the form of its equality matcher ([hamcrest.library.integration.match\_equality](https://pyhamcrest.readthedocs.io/en/release-1.8/integration/#module-hamcrest.library.integration.match_equality)
).

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html#)
    *   [Using Mock](https://docs.python.org/3/library/unittest.mock-examples.html#using-mock)
        *   [Mock patching methods](https://docs.python.org/3/library/unittest.mock-examples.html#mock-patching-methods)
            
        *   [Mock for method calls on an object](https://docs.python.org/3/library/unittest.mock-examples.html#mock-for-method-calls-on-an-object)
            
        *   [Mocking classes](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-classes)
            
        *   [Naming your mocks](https://docs.python.org/3/library/unittest.mock-examples.html#naming-your-mocks)
            
        *   [Tracking all calls](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-all-calls)
            
        *   [Setting return values and attributes](https://docs.python.org/3/library/unittest.mock-examples.html#setting-return-values-and-attributes)
            
        *   [Raising exceptions with mocks](https://docs.python.org/3/library/unittest.mock-examples.html#raising-exceptions-with-mocks)
            
        *   [Side effect functions and iterables](https://docs.python.org/3/library/unittest.mock-examples.html#side-effect-functions-and-iterables)
            
        *   [Mocking asynchronous iterators](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-iterators)
            
        *   [Mocking asynchronous context manager](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-context-manager)
            
        *   [Creating a mock from an existing object](https://docs.python.org/3/library/unittest.mock-examples.html#creating-a-mock-from-an-existing-object)
            
        *   [Using side\_effect to return per file content](https://docs.python.org/3/library/unittest.mock-examples.html#using-side-effect-to-return-per-file-content)
            
    *   [Patch decorators](https://docs.python.org/3/library/unittest.mock-examples.html#patch-decorators)
        
    *   [Further examples](https://docs.python.org/3/library/unittest.mock-examples.html#further-examples)
        *   [Mocking chained calls](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls)
            
        *   [Partial mocking](https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking)
            
        *   [Mocking a generator method](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-generator-method)
            
        *   [Applying the same patch to every test method](https://docs.python.org/3/library/unittest.mock-examples.html#applying-the-same-patch-to-every-test-method)
            
        *   [Mocking unbound methods](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-unbound-methods)
            
        *   [Checking multiple calls with mock](https://docs.python.org/3/library/unittest.mock-examples.html#checking-multiple-calls-with-mock)
            
        *   [Coping with mutable arguments](https://docs.python.org/3/library/unittest.mock-examples.html#coping-with-mutable-arguments)
            
        *   [Nesting patches](https://docs.python.org/3/library/unittest.mock-examples.html#nesting-patches)
            
        *   [Mocking a dictionary with MagicMock](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-dictionary-with-magicmock)
            
        *   [Mock subclasses and their attributes](https://docs.python.org/3/library/unittest.mock-examples.html#mock-subclasses-and-their-attributes)
            
        *   [Mocking imports with patch.dict](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-imports-with-patch-dict)
            
        *   [Tracking order of calls and less verbose call assertions](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-order-of-calls-and-less-verbose-call-assertions)
            
        *   [More complex argument matching](https://docs.python.org/3/library/unittest.mock-examples.html#more-complex-argument-matching)
            

#### Previous topic

[`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html "previous chapter")

#### Next topic

[`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest.mock+%E2%80%94+getting+started&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.mock-examples.html&pagesource=library%2Funittest.mock-examples.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/unittest.mock-examples.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/test.html "test — Regression tests package for Python")
     |
*   [previous](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library")
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
*   [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
    
*    
    
    |
*   Theme Auto Light Dark |