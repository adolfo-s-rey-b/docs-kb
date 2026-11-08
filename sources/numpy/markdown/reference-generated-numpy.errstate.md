[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.errstate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.errstate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.errstate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.errstate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.errstate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.errstate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.errstate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.errstate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.errstate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.errstate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.errstate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.errstate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.errstate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.errstate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.errstate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.errstate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.errstate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.errstate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.errstate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.errstate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.errstate[#](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy-errstate "Link to this heading")

==============================================================================================================================

_class_ numpy.errstate(_\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L386-L515)
[#](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "Link to this definition")

Context manager for floating-point error handling.

Using an instance of [`errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 as a context manager allows statements in that context to execute with a known error handling behavior. Upon entering the context the error handling is set with [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
 and [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
, and upon exiting it is reset to what it was before.

Changed in version 1.17.0: [`errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 is also usable as a function decorator, saving a level of indentation if an entire function is wrapped.

Changed in version 2.0: [`errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 is now fully thread and asyncio safe, but may not be entered more than once. It is not safe to decorate async functions using `errstate`.

Parameters:

**kwargs**{divide, over, under, invalid}

Keyword arguments. The valid keywords are the possible floating-point exceptions. Each keyword should have a string value that defines the treatment for the particular error. Possible values are {‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}.

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.__call__.html#numpy.errstate.__call__ "numpy.errstate.__call__")<br>(func) | Call self as a function. |

See also

[`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
, [`geterr`](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "numpy.geterr")
, [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
, [`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")

Notes

For complete documentation of the types of floating-point exceptions and treatment options, see [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
.

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html#fp-error-handling)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> olderr \= np.seterr(all\='ignore')  \# Set error handling to known state.

Copy to clipboard

\>>> np.arange(3) / 0.
array(\[nan, inf, inf\])
\>>> with np.errstate(divide\='ignore'):
...     np.arange(3) / 0.
array(\[nan, inf, inf\])

Copy to clipboard

\>>> np.sqrt(\-1)
np.float64(nan)
\>>> with np.errstate(invalid\='raise'):
...     np.sqrt(\-1)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FloatingPointError: invalid value encountered in sqrt

Copy to clipboard

Outside the context the error handling behavior has not changed:

\>>> np.geterr()
{'divide': 'ignore', 'over': 'ignore', 'under': 'ignore', 'invalid': 'ignore'}
\>>> olderr \= np.seterr(\*\*olderr)  \# restore original state

Copy to clipboard

Go BackOpen In Tab

On this page