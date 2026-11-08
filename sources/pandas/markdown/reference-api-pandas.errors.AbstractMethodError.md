[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.AbstractMethodError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.AbstractMethodError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.AbstractMethodError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.AbstractMethodError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.AbstractMethodError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.AbstractMethodError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.AbstractMethodError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.AbstractMethodError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.AbstractMethodError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.AbstractMethodError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.AbstractMethodError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.AbstractMethodError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.AbstractMethodError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.AbstractMethodError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.AbstractMethodError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.AbstractMethodError.html#pandas-errors-abstractmethoderror "Link to this heading")

===================================================================================================================================================================================

exception pandas.errors.AbstractMethodError(_class\_instance_, _methodtype\='method'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L487-L549)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.AbstractMethodError.html#pandas.errors.AbstractMethodError "Link to this definition")

Raise this error instead of NotImplementedError for abstract methods.

The AbstractMethodError is designed for use in classes that follow an abstract base class pattern. By raising this error in the method, it ensures that a subclass must implement the method to provide specific functionality. This is useful in a framework or library where certain methods must be implemented by the user to ensure correct behavior.

Parameters:

**class\_instance**object

The instance of the class where the abstract method is being called.

**methodtype**str, default “method”

A string indicating the type of method that is abstract. Must be one of {“method”, “classmethod”, “staticmethod”, “property”}.

See also

`api.extensions.ExtensionArray`

An example of a pandas extension mechanism that requires implementing specific abstract methods.

[`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "(in Python v3.15)")

A built-in exception that can also be used for abstract methods but lacks the specificity of AbstractMethodError in indicating the need for subclass implementation.

Examples

\>>> class Foo:
...     @classmethod
...     def classmethod(cls):
...         raise pd.errors.AbstractMethodError(cls, methodtype\="classmethod")
...
...     def method(self):
...         raise pd.errors.AbstractMethodError(self)
\>>> test \= Foo.classmethod()
Traceback (most recent call last):
AbstractMethodError: This classmethod must be defined in the concrete class Foo

Copy to clipboard

\>>> test2 \= Foo().method()
Traceback (most recent call last):
AbstractMethodError: This classmethod must be defined in the concrete class Foo

Copy to clipboard

On this page