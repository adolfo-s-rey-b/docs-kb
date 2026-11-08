[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.geterrcall.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.geterrcall.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.geterrcall.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.geterrcall.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.geterrcall.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.geterrcall.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.geterrcall.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.geterrcall.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.geterrcall.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.geterrcall.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.geterrcall.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.geterrcall.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.geterrcall.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.geterrcall.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.geterrcall.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.geterrcall.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.geterrcall.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.geterrcall.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.geterrcall.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.geterrcall.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.geterrcall[#](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy-geterrcall "Link to this heading")

====================================================================================================================================

numpy.geterrcall()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L328-L376)
[#](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "Link to this definition")

Return the current callback function used on floating-point errors.

When the error handling for a floating-point error (one of “divide”, “over”, “under”, or “invalid”) is set to ‘call’ or ‘log’, the function that is called or the log instance that is written to is returned by [`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")
. This function or log instance has been set with [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
.

Returns:

**errobj**callable, log instance or None

The current error handler. If no handler was set through [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
, `None` is returned.

See also

[`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
, [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
, [`geterr`](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "numpy.geterr")

Notes

For complete documentation of the types of floating-point exceptions and treatment options, see [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")
.

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html#fp-error-handling)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.geterrcall()  \# we did not yet set a handler, returns None

Copy to clipboard

\>>> orig\_settings \= np.seterr(all\='call')
\>>> def err\_handler(type, flag):
...     print("Floating point error (%s), with flag %s" % (type, flag))
\>>> old\_handler \= np.seterrcall(err\_handler)
\>>> np.array(\[1, 2, 3\]) / 0.0
Floating point error (divide by zero), with flag 1
array(\[inf, inf, inf\])

Copy to clipboard

\>>> cur\_handler \= np.geterrcall()
\>>> cur\_handler is err\_handler
True
\>>> old\_settings \= np.seterr(\*\*orig\_settings)  \# restore original
\>>> old\_handler \= np.seterrcall(None)  \# restore original

Copy to clipboard

Go BackOpen In Tab

On this page