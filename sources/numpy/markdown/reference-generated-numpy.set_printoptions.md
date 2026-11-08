[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.set_printoptions.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.set_printoptions.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.set_printoptions.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.set_printoptions.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.set_printoptions.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.set_printoptions.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.set_printoptions.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.set_printoptions.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.set_printoptions.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.set_printoptions.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.set_printoptions.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.set_printoptions.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.set_printoptions.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.set_printoptions.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.set_printoptions.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.set_printoptions.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.set_printoptions.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.set_printoptions.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.set_printoptions.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.set_printoptions.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.set\_printoptions[#](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy-set-printoptions "Link to this heading")

=======================================================================================================================================================

numpy.set\_printoptions(_precision\=None_, _threshold\=None_, _edgeitems\=None_, _linewidth\=None_, _suppress\=None_, _nanstr\=None_, _infstr\=None_, _formatter\=None_, _sign\=None_, _floatmode\=None_, _\*_, _legacy\=None_, _override\_repr\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L122-L312)
[#](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "Link to this definition")

Set printing options.

These options determine the way floating point numbers, arrays and other NumPy objects are displayed.

Parameters:

**precision**int or None, optional

Number of digits of precision for floating point output (default 8). May be None if _floatmode_ is not _fixed_, to print as many digits as necessary to uniquely specify the value.

**threshold**int, optional

Total number of array elements which trigger summarization rather than full repr (default 1000). To always use the full repr without summarization, pass [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "(in Python v3.14)")
.

**edgeitems**int, optional

Number of array items in summary at beginning and end of each dimension (default 3).

**linewidth**int, optional

The number of characters per line for the purpose of inserting line breaks (default 75).

**suppress**bool, optional

If True, always print floating point numbers using fixed point notation, in which case numbers equal to zero in the current precision will print as zero. If False, then scientific notation is used when absolute value of the smallest number is < 1e-4 or the ratio of the maximum absolute value to the minimum is > 1e3. The default is False.

**nanstr**str, optional

String representation of floating point not-a-number (default nan).

**infstr**str, optional

String representation of floating point infinity (default inf).

**sign**string, either ‘-’, ‘+’, or ‘ ‘, optional

Controls printing of the sign of floating-point types. If ‘+’, always print the sign of positive values. If ‘ ‘, always prints a space (whitespace character) in the sign position of positive values. If ‘-’, omit the sign character of positive values. (default ‘-‘)

Changed in version 2.0: The sign parameter can now be an integer type, previously types were floating-point types.

**formatter**dict of callables, optional

If not None, the keys should indicate the type(s) that the respective formatting function applies to. Callables should return a string. Types that are not specified (by their corresponding keys) are handled by the default formatters. Individual types for which a formatter can be set are:

*   ‘bool’
    
*   ‘int’
    
*   ‘timedelta’ : a [`numpy.timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
    
*   ‘datetime’ : a [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
    
*   ‘float’
    
*   ‘longfloat’ : 128-bit floats
    
*   ‘complexfloat’
    
*   ‘longcomplexfloat’ : composed of two 128-bit floats
    
*   ‘numpystr’ : types [`numpy.bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
     and [`numpy.str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
    
*   ‘object’ : _np.object\__ arrays
    

Other keys that can be used to set a group of types at once are:

*   ‘all’ : sets all types
    
*   ‘int\_kind’ : sets ‘int’
    
*   ‘float\_kind’ : sets ‘float’ and ‘longfloat’
    
*   ‘complex\_kind’ : sets ‘complexfloat’ and ‘longcomplexfloat’
    
*   ‘str\_kind’ : sets ‘numpystr’
    

**floatmode**str, optional

Controls the interpretation of the _precision_ option for floating-point types. Can take the following values (default maxprec\_equal):

*   ‘fixed’: Always print exactly _precision_ fractional digits,
    
    even if this would print more or fewer digits than necessary to specify the value uniquely.
    
*   ‘unique’: Print the minimum number of fractional digits necessary
    
    to represent each value uniquely. Different elements may have a different number of digits. The value of the _precision_ option is ignored.
    
*   ‘maxprec’: Print at most _precision_ fractional digits, but if
    
    an element can be uniquely represented with fewer digits only print it with that many.
    
*   ‘maxprec\_equal’: Print at most _precision_ fractional digits,
    
    but if every element in the array can be uniquely represented with an equal number of fewer digits, use that many digits for all elements.
    

**legacy**string or _False_, optional

If set to the string `'1.13'` enables 1.13 legacy printing mode. This approximates numpy 1.13 print output by including a space in the sign position of floats and different behavior for 0d arrays. This also enables 1.21 legacy printing mode (described below).

If set to the string `'1.21'` enables 1.21 legacy printing mode. This approximates numpy 1.21 print output of complex structured dtypes by not inserting spaces after commas that separate fields and after colons.

If set to `'1.25'` approximates printing of 1.25 which mainly means that numeric scalars are printed without their type information, e.g. as `3.0` rather than `np.float64(3.0)`.

If set to `'2.1'`, shape information is not given when arrays are summarized (i.e., multiple elements replaced with `...`).

If set to `'2.2'`, the transition to use scientific notation for printing `np.float16` and `np.float32` types may happen later or not at all for larger values.

If set to _False_, disables legacy mode.

Unrecognized strings will be ignored with a warning for forward compatibility.

Changed in version 1.22.0.

Changed in version 2.2.

**override\_repr: callable, optional**

If set a passed function will be used for generating arrays’ repr. Other options will be ignored.

See also

[`get_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions")
, [`printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
, [`array2string`](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "numpy.array2string")

Notes

*   `formatter` is always reset with a call to [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
    .
    
*   Use [`printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
     as a context manager to set the values temporarily.
    
*   These print options apply only to NumPy ndarrays, not to scalars.
    

**Concurrency note:** see [Text formatting options](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options)

Examples

Try it in your browser!

Floating point precision can be set:

\>>> import numpy as np
\>>> np.set\_printoptions(precision\=4)
\>>> np.array(\[1.123456789\])
\[1.1235\]

Copy to clipboard

Long arrays can be summarised:

\>>> np.set\_printoptions(threshold\=5)
\>>> np.arange(10)
array(\[0, 1, 2, ..., 7, 8, 9\], shape=(10,))

Copy to clipboard

Small results can be suppressed:

\>>> eps \= np.finfo(float).eps
\>>> x \= np.arange(4.)
\>>> x\*\*2 \- (x + eps)\*\*2
array(\[-4.9304e-32, -4.4409e-16,  0.0000e+00,  0.0000e+00\])
\>>> np.set\_printoptions(suppress\=True)
\>>> x\*\*2 \- (x + eps)\*\*2
array(\[-0., -0.,  0.,  0.\])

Copy to clipboard

A custom formatter can be used to display array elements as desired:

\>>> np.set\_printoptions(formatter\={'all':lambda x: 'int: '+str(\-x)})
\>>> x \= np.arange(3)
\>>> x
array(\[int: 0, int: -1, int: -2\])
\>>> np.set\_printoptions()  \# formatter gets reset
\>>> x
array(\[0, 1, 2\])

Copy to clipboard

To put back the default options, you can use:

\>>> np.set\_printoptions(edgeitems\=3, infstr\='inf',
... linewidth\=75, nanstr\='nan', precision\=8,
... suppress\=False, threshold\=1000, formatter\=None)

Copy to clipboard

Also to temporarily override options, use [`printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
 as a context manager:

\>>> with np.printoptions(precision\=2, suppress\=True, threshold\=5):
...     np.linspace(0, 10, 10)
array(\[ 0.  ,  1.11,  2.22, ...,  7.78,  8.89, 10.  \], shape=(10,))

Copy to clipboard

Go BackOpen In Tab

On this page