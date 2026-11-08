[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.seterrcall.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.seterrcall.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.seterrcall.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.seterrcall.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.seterrcall.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.seterrcall.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.seterrcall.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.seterrcall.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.seterrcall.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.seterrcall.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.seterrcall.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.seterrcall.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.seterrcall.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.seterrcall.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.seterrcall.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.seterrcall.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.seterrcall.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.seterrcall.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.seterrcall.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.seterrcall.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.seterrcall[#](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy-seterrcall "Link to this heading")

====================================================================================================================================

numpy.seterrcall(_func_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L233-L325)
[#](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "Link to this definition")

Set the floating-point error callback function or log object.

There are two ways to capture floating-point error messages. The first is to set the error-handler to ‘call’, using [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
. Then, set the function to call using this function.

The second is to set the error-handler to ‘log’, using [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
. Floating-point errors then trigger a call to the ‘write’ method of the provided object.

Parameters:

**func**callable f(err, flag) or object with write method

Function to call upon floating-point errors (‘call’-mode) or object whose ‘write’ method is used to log such message (‘log’-mode).

The call function takes two arguments. The first is a string describing the type of error (such as “divide by zero”, “overflow”, “underflow”, or “invalid value”), and the second is the status flag. The flag is a byte, whose four least-significant bits indicate the type of error, one of “divide”, “over”, “under”, “invalid”:

\[0 0 0 0 divide over under invalid\]

Copy to clipboard

In other words, `flags = divide + 2*over + 4*under + 8*invalid`.

If an object is provided, its write method should take one argument, a string.

Returns:

**h**callable, log instance or None

The old error handler.

See also

[`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
, [`geterr`](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "numpy.geterr")
, [`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")

Notes

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html)

Examples

Try it in your browser!

Callback upon error:

\>>> def err\_handler(type, flag):
...     print("Floating point error (%s), with flag %s" % (type, flag))
...

Copy to clipboard

\>>> import numpy as np

Copy to clipboard

\>>> orig\_handler \= np.seterrcall(err\_handler)
\>>> orig\_err \= np.seterr(all\='call')

Copy to clipboard

\>>> np.array(\[1, 2, 3\]) / 0.0
Floating point error (divide by zero), with flag 1
array(\[inf, inf, inf\])

Copy to clipboard

\>>> np.seterrcall(orig\_handler)
<function err\_handler at 0x...>
\>>> np.seterr(\*\*orig\_err)
{'divide': 'call', 'over': 'call', 'under': 'call', 'invalid': 'call'}

Copy to clipboard

Log error message:

\>>> class Log:
...     def write(self, msg):
...         print("LOG: %s" % msg)
...

Copy to clipboard

\>>> log \= Log()
\>>> saved\_handler \= np.seterrcall(log)
\>>> save\_err \= np.seterr(all\='log')

Copy to clipboard

\>>> np.array(\[1, 2, 3\]) / 0.0
LOG: Warning: divide by zero encountered in divide
array(\[inf, inf, inf\])

Copy to clipboard

\>>> np.seterrcall(orig\_handler)
<numpy.Log object at 0x...>
\>>> np.seterr(\*\*orig\_err)
{'divide': 'log', 'over': 'log', 'under': 'log', 'invalid': 'log'}

Copy to clipboard

Go BackOpen In Tab

On this page