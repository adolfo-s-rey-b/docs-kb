[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.clear_and_catch_warnings.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.clear_and_catch_warnings.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.clear_and_catch_warnings.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.clear\_and\_catch\_warnings[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.clear_and_catch_warnings.html#numpy-testing-clear-and-catch-warnings "Link to this heading")

=========================================================================================================================================================================================================

_class_ numpy.testing.clear\_and\_catch\_warnings(_record\=False_, _modules\=()_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2225-L2288)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.clear_and_catch_warnings.html#numpy.testing.clear_and_catch_warnings "Link to this definition")

Context manager that resets warning registry for catching warnings

Warnings can be slippery, because, whenever a warning is triggered, Python adds a `__warningregistry__` member to the _calling_ module. This makes it impossible to retrigger the warning in this module, whatever you put in the warnings filters. This context manager accepts a sequence of _modules_ as a keyword argument to its constructor and:

*   stores and removes any `__warningregistry__` entries in given _modules_ on entry;
    
*   resets `__warningregistry__` to its previous state on exit.
    

This makes it possible to trigger any warning afresh inside the context manager without disturbing the state of warnings outside.

For compatibility with Python, please consider all arguments to be keyword-only.

Parameters:

**record**bool, optional

Specifies whether warnings should be captured by a custom implementation of `warnings.showwarning()` and be appended to a list returned by the context manager. Otherwise None is returned by the context manager. The objects appended to the list are arguments whose attributes mirror the arguments to `showwarning()`.

**modules**sequence, optional

Sequence of modules for which to reset warnings registry on entry and restore on exit. To work correctly, all ‘ignore’ filters should filter by one of these modules.

Examples

Try it in your browser!

\>>> import warnings
\>>> with np.testing.clear\_and\_catch\_warnings(
...         modules\=\[np.\_core.fromnumeric\]):
...     warnings.simplefilter('always')
...     warnings.filterwarnings('ignore', module\='np.\_core.fromnumeric')
...     \# do something that raises a warning but ignore those in
...     \# np.\_core.fromnumeric

Copy to clipboard

Go BackOpen In Tab

On this page