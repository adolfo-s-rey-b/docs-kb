[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.geterr[#](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy-geterr "Link to this heading")

========================================================================================================================

numpy.geterr()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L111-L158)
[#](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "Link to this definition")

Get the current way of handling floating-point errors.

Returns:

**res**dict

A dictionary with keys “divide”, “over”, “under”, and “invalid”, whose values are from the strings “ignore”, “print”, “log”, “warn”, “raise”, and “call”. The keys represent possible floating-point exceptions, and the values define how these exceptions are handled.

See also

[`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")
, [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
, [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")

Notes

For complete documentation of the types of floating-point exceptions and treatment options, see [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
.

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.geterr()
{'divide': 'warn', 'over': 'warn', 'under': 'ignore', 'invalid': 'warn'}
\>>> np.arange(3.) / np.arange(3.)  
array(\[nan,  1.,  1.\])
RuntimeWarning: invalid value encountered in divide

Copy to clipboard

\>>> oldsettings \= np.seterr(all\='warn', invalid\='raise')
\>>> np.geterr()
{'divide': 'warn', 'over': 'warn', 'under': 'warn', 'invalid': 'raise'}
\>>> np.arange(3.) / np.arange(3.)
Traceback (most recent call last):
  ...
FloatingPointError: invalid value encountered in divide
\>>> oldsettings \= np.seterr(\*\*oldsettings)  \# restore original

Copy to clipboard

Go BackOpen In Tab

On this page