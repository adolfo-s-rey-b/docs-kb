[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.decorate_methods.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.decorate_methods.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.decorate_methods.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.decorate_methods.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.decorate_methods.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.decorate_methods.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.decorate_methods.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.decorate_methods.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.decorate_methods.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.decorate_methods.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.decorate_methods.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.decorate_methods.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.decorate_methods.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.decorate_methods.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.decorate_methods.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.decorate_methods.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.decorate_methods.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.decorate_methods.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.decorate_methods.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.decorate_methods.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.decorate_methods.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.decorate_methods.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.decorate\_methods[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.decorate_methods.html#numpy-testing-decorate-methods "Link to this heading")

===============================================================================================================================================================================

testing.decorate\_methods(_cls_, _decorator_, _testmatch\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1553-L1596)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.decorate_methods.html#numpy.testing.decorate_methods "Link to this definition")

Apply a decorator to all methods in a class matching a regular expression.

The given decorator is applied to all public methods of _cls_ that are matched by the regular expression _testmatch_ (`testmatch.search(methodname)`). Methods that are private, i.e. start with an underscore, are ignored.

Parameters:

**cls**class

Class whose methods to decorate.

**decorator**function

Decorator to apply to methods

**testmatch**compiled regexp or str, optional

The regular expression. Default value is None, in which case the nose default (`re.compile(r'(?:^|[\b_\.%s-])[Tt]est' % os.sep)`) is used. If _testmatch_ is a string, it is compiled to a regular expression first.

On this page