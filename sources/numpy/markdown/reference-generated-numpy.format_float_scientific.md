[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.format_float_scientific.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.format_float_scientific.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.format_float_scientific.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.format_float_scientific.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.format_float_scientific.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.format_float_scientific.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.format_float_scientific.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.format_float_scientific.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.format_float_scientific.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.format_float_scientific.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.format_float_scientific.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.format_float_scientific.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.format_float_scientific.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.format_float_scientific.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.format_float_scientific.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.format_float_scientific.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.format_float_scientific.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.format_float_scientific.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.format_float_scientific.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.format_float_scientific.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.format\_float\_scientific[#](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy-format-float-scientific "Link to this heading")

=============================================================================================================================================================================

numpy.format\_float\_scientific(_x_, _precision\=None_, _unique\=True_, _trim\='k'_, _sign\=False_, _pad\_left\=None_, _exp\_digits\=None_, _min\_digits\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L1139-L1217)
[#](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific "Link to this definition")

Format a floating-point scalar as a decimal string in scientific notation.

Provides control over rounding, trimming and padding. Uses and assumes IEEE unbiased rounding. Uses the “Dragon4” algorithm.

Parameters:

**x**python float or numpy floating scalar

Value to format.

**precision**non-negative integer or None, optional

Maximum number of digits to print. May be None if [`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
 is _True_, but must be an integer if unique is _False_.

**unique**boolean, optional

If _True_, use a digit-generation strategy which gives the shortest representation which uniquely identifies the floating-point number from other values of the same type, by judicious rounding. If _precision_ is given fewer digits than necessary can be printed. If _min\_digits_ is given more can be printed, in which cases the last digit is rounded with unbiased rounding. If _False_, digits are generated as if printing an infinite-precision value and stopping after _precision_ digits, rounding the remaining value with unbiased rounding

**trim**one of ‘k’, ‘.’, ‘0’, ‘-’, optional

Controls post-processing trimming of trailing digits, as follows:

*   ‘k’ : keep trailing zeros, keep decimal point (no trimming)
    
*   ‘.’ : trim all trailing zeros, leave decimal point
    
*   ‘0’ : trim all but the zero before the decimal point. Insert the zero if it is missing.
    
*   ‘-’ : trim trailing zeros and any trailing decimal point
    

**sign**boolean, optional

Whether to show the sign for positive values.

**pad\_left**non-negative integer, optional

Pad the left side of the string with whitespace until at least that many characters are to the left of the decimal point.

**exp\_digits**non-negative integer, optional

Pad the exponent with zeros until it contains at least this many digits. If omitted, the exponent will be at least 2 digits.

**min\_digits**non-negative integer or None, optional

Minimum number of digits to print. This only has an effect for _unique=True_. In that case more digits than necessary to uniquely identify the value may be printed and rounded unbiased.

New in version 1.21.0.

Returns:

**rep**string

The string representation of the floating point value

See also

[`format_float_positional`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional "numpy.format_float_positional")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.format\_float\_scientific(np.float32(np.pi))
'3.1415927e+00'
\>>> s \= np.float32(1.23e24)
\>>> np.format\_float\_scientific(s, unique\=False, precision\=15)
'1.230000071797338e+24'
\>>> np.format\_float\_scientific(s, exp\_digits\=4)
'1.23e+0024'

Copy to clipboard

Go BackOpen In Tab

On this page