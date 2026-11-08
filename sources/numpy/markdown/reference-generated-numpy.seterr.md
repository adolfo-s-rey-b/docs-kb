[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.seterr[#](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy-seterr "Link to this heading")

========================================================================================================================

numpy.seterr(_all\=None_, _divide\=None_, _over\=None_, _under\=None_, _invalid\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L19-L108)
[#](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#numpy.seterr "Link to this definition")

Set how floating-point errors are handled.

Note that operations on integer scalar types (such as [`int16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int16 "numpy.int16")
) are handled like floating point, and are affected by these settings.

Parameters:

**all**{‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}, optional

Set treatment for all types of floating-point errors at once:

*   ignore: Take no action when the exception occurs.
    
*   warn: Print a [`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "(in Python v3.14)")
     (via the Python [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python v3.14)")
     module).
    
*   raise: Raise a [`FloatingPointError`](https://docs.python.org/3/library/exceptions.html#FloatingPointError "(in Python v3.14)")
    .
    
*   call: Call a function specified using the [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
     function.
    
*   print: Print a warning directly to `stdout`.
    
*   log: Record error in a Log object specified by [`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")
    .
    

The default is not to change the current behavior.

**divide**{‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}, optional

Treatment for division by zero.

**over**{‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}, optional

Treatment for floating-point overflow.

**under**{‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}, optional

Treatment for floating-point underflow.

**invalid**{‘ignore’, ‘warn’, ‘raise’, ‘call’, ‘print’, ‘log’}, optional

Treatment for invalid floating-point operation.

Returns:

**old\_settings**dict

Dictionary containing the old settings.

See also

[`seterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall")

Set a callback function for the ‘call’ mode.

[`geterr`](https://numpy.org/doc/stable/reference/generated/numpy.geterr.html#numpy.geterr "numpy.geterr")
, [`geterrcall`](https://numpy.org/doc/stable/reference/generated/numpy.geterrcall.html#numpy.geterrcall "numpy.geterrcall")
, [`errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")

Notes

The floating-point exceptions are defined in the IEEE 754 standard [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#r4cab4292821f-1)
:

*   Division by zero: infinite result obtained from finite numbers.
    
*   Overflow: result too large to be expressed.
    
*   Underflow: result so close to zero that some precision was lost.
    
*   Invalid operation: result is not an expressible number, typically indicates that a NaN was produced.
    

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html#fp-error-handling)

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.seterr.html#id1)\
\]

[https://en.wikipedia.org/wiki/IEEE\_754](https://en.wikipedia.org/wiki/IEEE_754)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> orig\_settings \= np.seterr(all\='ignore')  \# seterr to known value
\>>> np.int16(32000) \* np.int16(3)
np.int16(30464)
\>>> np.seterr(over\='raise')
{'divide': 'ignore', 'over': 'ignore', 'under': 'ignore', 'invalid': 'ignore'}
\>>> old\_settings \= np.seterr(all\='warn', over\='raise')
\>>> np.int16(32000) \* np.int16(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FloatingPointError: overflow encountered in scalar multiply

Copy to clipboard

\>>> old\_settings \= np.seterr(all\='print')
\>>> np.geterr()
{'divide': 'print', 'over': 'print', 'under': 'print', 'invalid': 'print'}
\>>> np.int16(32000) \* np.int16(3)
np.int16(30464)
\>>> np.seterr(\*\*orig\_settings)  \# restore original
{'divide': 'print', 'over': 'print', 'under': 'print', 'invalid': 'print'}

Copy to clipboard

Go BackOpen In Tab

On this page