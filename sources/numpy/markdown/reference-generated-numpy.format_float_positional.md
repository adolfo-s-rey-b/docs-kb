[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.format_float_positional.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.format_float_positional.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.format_float_positional.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.format_float_positional.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.format_float_positional.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.format_float_positional.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.format_float_positional.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.format_float_positional.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.format_float_positional.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.format_float_positional.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.format_float_positional.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.format_float_positional.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.format_float_positional.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.format_float_positional.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.format_float_positional.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.format_float_positional.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.format_float_positional.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.format_float_positional.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.format_float_positional.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.format_float_positional.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.format\_float\_positional[#](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy-format-float-positional "Link to this heading")

=============================================================================================================================================================================

numpy.format\_float\_positional(_x_, _precision\=None_, _unique\=True_, _fractional\=True_, _trim\='k'_, _sign\=False_, _pad\_left\=None_, _pad\_right\=None_, _min\_digits\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L1220-L1310)
[#](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional "Link to this definition")

Format a floating-point scalar as a decimal string in positional notation.

Provides control over rounding, trimming and padding. Uses and assumes IEEE unbiased rounding. Uses the “Dragon4” algorithm.

Parameters:

**x**python float or numpy floating scalar

Value to format.

**precision**non-negative integer or None, optional

Maximum number of digits to print. May be None if [`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
 is _True_, but must be an integer if unique is _False_.

**unique**boolean, optional

If _True_, use a digit-generation strategy which gives the shortest representation which uniquely identifies the floating-point number from other values of the same type, by judicious rounding. If _precision_ is given fewer digits than necessary can be printed, or if _min\_digits_ is given more can be printed, in which cases the last digit is rounded with unbiased rounding. If _False_, digits are generated as if printing an infinite-precision value and stopping after _precision_ digits, rounding the remaining value with unbiased rounding

**fractional**boolean, optional

If _True_, the cutoffs of _precision_ and _min\_digits_ refer to the total number of digits after the decimal point, including leading zeros. If _False_, _precision_ and _min\_digits_ refer to the total number of significant digits, before or after the decimal point, ignoring leading zeros.

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

**pad\_right**non-negative integer, optional

Pad the right side of the string with whitespace until at least that many characters are to the right of the decimal point.

**min\_digits**non-negative integer or None, optional

Minimum number of digits to print. Only has an effect if _unique=True_ in which case additional digits past those necessary to uniquely identify the value may be printed, rounding the last additional digit.

New in version 1.21.0.

Returns:

**rep**string

The string representation of the floating point value

See also

[`format_float_scientific`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific "numpy.format_float_scientific")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.format\_float\_positional(np.float32(np.pi))
'3.1415927'
\>>> np.format\_float\_positional(np.float16(np.pi))
'3.14'
\>>> np.format\_float\_positional(np.float16(0.3))
'0.3'
\>>> np.format\_float\_positional(np.float16(0.3), unique\=False, precision\=10)
'0.3000488281'

Copy to clipboard

Go BackOpen In Tab

On this page