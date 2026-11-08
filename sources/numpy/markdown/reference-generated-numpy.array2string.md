[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array2string.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array2string.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array2string.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array2string.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array2string.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array2string.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array2string.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array2string.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array2string.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array2string.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array2string.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array2string.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array2string.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array2string.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array2string.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array2string.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array2string.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array2string.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array2string.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array2string.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array2string[#](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy-array2string "Link to this heading")

==========================================================================================================================================

numpy.array2string(_a_, _max\_line\_width\=None_, _precision\=None_, _suppress\_small\=None_, _separator\=' '_, _prefix\=''_, _\*_, _formatter\=None_, _threshold\=None_, _edgeitems\=None_, _sign\=None_, _floatmode\=None_, _suffix\=''_, _legacy\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L643-L810)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "Link to this definition")

Return a string representation of an array.

Parameters:

**a**ndarray

Input array.

**max\_line\_width**int, optional

Inserts newlines if text is longer than _max\_line\_width_. Defaults to `numpy.get_printoptions()['linewidth']`.

**precision**int or None, optional

Floating point precision. Defaults to `numpy.get_printoptions()['precision']`.

**suppress\_small**bool, optional

Represent numbers “very close” to zero as zero; default is False. Very close is defined by precision: if the precision is 8, e.g., numbers smaller (in absolute value) than 5e-9 are represented as zero. Defaults to `numpy.get_printoptions()['suppress']`.

**separator**str, optional

Inserted between elements.

**prefix**str, optional

**suffix**str, optional

The length of the prefix and suffix strings are used to respectively align and wrap the output. An array is typically printed as:

prefix + array2string(a) + suffix

Copy to clipboard

The output is left-padded by the length of the prefix string, and wrapping is forced at the column `max_line_width - len(suffix)`. It should be noted that the content of prefix and suffix strings are not included in the output.

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
    
*   ‘void’ : type [`numpy.void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")
    
*   ‘numpystr’ : types [`numpy.bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
     and [`numpy.str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
    

Other keys that can be used to set a group of types at once are:

*   ‘all’ : sets all types
    
*   ‘int\_kind’ : sets ‘int’
    
*   ‘float\_kind’ : sets ‘float’ and ‘longfloat’
    
*   ‘complex\_kind’ : sets ‘complexfloat’ and ‘longcomplexfloat’
    
*   ‘str\_kind’ : sets ‘numpystr’
    

**threshold**int, optional

Total number of array elements which trigger summarization rather than full repr. Defaults to `numpy.get_printoptions()['threshold']`.

**edgeitems**int, optional

Number of array items in summary at beginning and end of each dimension. Defaults to `numpy.get_printoptions()['edgeitems']`.

**sign**string, either ‘-’, ‘+’, or ‘ ‘, optional

Controls printing of the sign of floating-point types. If ‘+’, always print the sign of positive values. If ‘ ‘, always prints a space (whitespace character) in the sign position of positive values. If ‘-’, omit the sign character of positive values. Defaults to `numpy.get_printoptions()['sign']`.

Changed in version 2.0: The sign parameter can now be an integer type, previously types were floating-point types.

**floatmode**str, optional

Controls the interpretation of the _precision_ option for floating-point types. Defaults to `numpy.get_printoptions()['floatmode']`. Can take the following values:

*   ‘fixed’: Always print exactly _precision_ fractional digits, even if this would print more or fewer digits than necessary to specify the value uniquely.
    
*   ‘unique’: Print the minimum number of fractional digits necessary to represent each value uniquely. Different elements may have a different number of digits. The value of the _precision_ option is ignored.
    
*   ‘maxprec’: Print at most _precision_ fractional digits, but if an element can be uniquely represented with fewer digits only print it with that many.
    
*   ‘maxprec\_equal’: Print at most _precision_ fractional digits, but if every element in the array can be uniquely represented with an equal number of fewer digits, use that many digits for all elements.
    

**legacy**string or _False_, optional

If set to the string `'1.13'` enables 1.13 legacy printing mode. This approximates numpy 1.13 print output by including a space in the sign position of floats and different behavior for 0d arrays. If set to _False_, disables legacy mode. Unrecognized strings will be ignored with a warning for forward compatibility.

Returns:

**array\_str**str

String representation of the array.

Raises:

TypeError

if a callable in _formatter_ does not return a string.

See also

[`array_str`](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str "numpy.array_str")
, [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")
, [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
, [`get_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions")

Notes

If a formatter is specified for a certain type, the _precision_ keyword is ignored for that type.

This is a very flexible function; [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")
 and [`array_str`](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str "numpy.array_str")
 are using [`array2string`](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "numpy.array2string")
 internally so keywords with the same name should work identically in all three functions.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1e-16,1,2,3\])
\>>> np.array2string(x, precision\=2, separator\=',',
...                       suppress\_small\=True)
'\[0.,1.,2.,3.\]'

Copy to clipboard

\>>> x  \= np.arange(3.)
\>>> np.array2string(x, formatter\={'float\_kind':lambda x: "%.2f" % x})
'\[0.00 1.00 2.00\]'

Copy to clipboard

\>>> x  \= np.arange(3)
\>>> np.array2string(x, formatter\={'int':lambda x: hex(x)})
'\[0x0 0x1 0x2\]'

Copy to clipboard

Go BackOpen In Tab

On this page