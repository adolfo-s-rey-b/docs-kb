[Skip to main content](https://numpy.org/doc/stable/reference/routines.err.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.err.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.err.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.err.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.err.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.err.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.err.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.err.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.err.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.err.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.err.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.err.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.err.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.err.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.err.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.err.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.err.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.err.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.err.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.err.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.err.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.err.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Floating point error handling[#](https://numpy.org/doc/stable/reference/routines.err.html#floating-point-error-handling "Link to this heading")

================================================================================================================================================

Error handling settings are stored in [`contextvars`](https://docs.python.org/3/library/contextvars.html#module-contextvars "(in Python v3.14)")
 allowing different threads or async tasks to have independent configurations. For more information, see [Thread Safety](https://numpy.org/doc/stable/reference/thread_safety.html#thread-safety)
.

How numpy handles numerical exceptions[#](https://numpy.org/doc/stable/reference/routines.err.html#how-numpy-handles-numerical-exceptions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default is to `'warn'` for `invalid`, `divide`, and `overflow` and `'ignore'` for `underflow`. But this can be changed, and it can be set individually for different kinds of exceptions. The different behaviors are:

*   `'ignore'` : Take no action when the exception occurs.
    
*   `'warn'` : Print a [`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "(in Python v3.14)")
     (via the Python [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python v3.14)")
     module).
    
*   `'raise'` : Raise a [`FloatingPointError`](https://docs.python.org/3/library/exceptions.html#FloatingPointError "(in Python v3.14)")
    .
    
*   `'call'` : Call a specified function.
    
*   `'print'` : Print a warning directly to `stdout`.
    
*   `'log'` : Record error in a Log object.
    

These behaviors can be set for all kinds of errors or specific ones:

*   `all` : apply to all numeric exceptions
    
*   `invalid` : when NaNs are generated
    
*   `divide` : divide by zero (for integers as well!)
    
*   `overflow` : floating point overflows
    
*   `underflow` : floating point underflows
    

Note that integer divide-by-zero is handled by the same machinery.

The error handling mode can be configured [`numpy.errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 context manager.

Examples[#](https://numpy.org/doc/stable/reference/routines.err.html#examples "Link to this heading")

------------------------------------------------------------------------------------------------------

\>>> with np.errstate(all\='warn'):
...     np.zeros(5, dtype\=np.float32) / 0.0
<python-input-1>:2: RuntimeWarning: invalid value encountered in divide
array(\[nan, nan, nan, nan, nan\], dtype=float32)

Copy to clipboard

\>>> with np.errstate(under\='ignore'):
...     np.array(\[1.e-100\])\*\*10
array(\[0.\])

Copy to clipboard

\>>> with np.errstate(invalid\='raise'):
...     np.sqrt(np.array(\[\-1.\]))
...
Traceback (most recent call last):
  File "<python-input-1>", line 2, in <module>
    np.sqrt(np.array(\[\-1.\]))
    \~~~~~~~^^^^^^^^^^^^^^^^^
FloatingPointError: invalid value encountered in sqrt

Copy to clipboard

\>>> def errorhandler(errstr, errflag):
...     print("saw stupid error!")
\>>> with np.errstate(call\=errorhandler, all\='call'):
...     np.zeros(5, dtype\=np.int32) / 0
saw stupid error!
array(\[nan, nan, nan, nan, nan\])

Copy to clipboard

Setting and getting error handling[#](https://numpy.org/doc/stable/reference/routines.err.html#setting-and-getting-error-handling "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`seterr`](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr")<br>(\[all, divide, over, under, invalid\]) | Set how floating-point errors are handled. |
| [`geterr`](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "numpy.geterr")<br>() | Get the current way of handling floating-point errors. |
| [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")<br>(func) | Set the floating-point error callback function or log object. |
| [`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")<br>() | Return the current callback function used on floating-point errors. |
| [`errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")<br>(\*\*kwargs) | Context manager for floating-point error handling. |

On this page