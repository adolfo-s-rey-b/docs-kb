[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.astype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.astype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.astype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.astype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.astype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.astype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.astype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.astype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.astype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.astype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.astype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.astype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.astype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.astype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.astype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.astype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.astype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.astype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.astype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.astype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.astype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.astype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.astype[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.astype.html#numpy-char-chararray-astype "Link to this heading")

=====================================================================================================================================================================

method

char.chararray.astype(_dtype_, _order\='K'_, _casting\='unsafe'_, _subok\=True_, _copy\=True_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.astype.html#numpy.char.chararray.astype "Link to this definition")

Copy of the array, cast to a specified type.

Parameters:

**dtype**str or dtype

Typecode or data-type to which the array is cast.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Controls the memory layout order of the result. ‘C’ means C order, ‘F’ means Fortran order, ‘A’ means ‘F’ order if all the arrays are Fortran contiguous, ‘C’ order otherwise, and ‘K’ means as close to the order the array elements appear in memory as possible. Default is ‘K’.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘same\_value’, ‘unsafe’}, optional

Controls what kind of data casting may occur. Defaults to ‘unsafe’ for backwards compatibility.

*   ‘no’ means the data types should not be cast at all.
    
*   ‘equiv’ means only byte-order changes are allowed.
    
*   ‘safe’ means only casts which can preserve values are allowed.
    
*   ‘same\_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
    
*   ‘unsafe’ means any data conversions may be done.
    
*   ‘same\_value’ means any data conversions may be done, but the values must not change, including rounding of floats or overflow of ints
    

New in version 2.4: Support for `'same_value'` was added.

**subok**bool, optional

If True, then sub-classes will be passed-through (default), otherwise the returned array will be forced to be a base-class array.

**copy**bool, optional

By default, astype always returns a newly allocated array. If this is set to false, and the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, _order_, and _subok_ requirements are satisfied, the input array is returned instead of a copy.

Returns:

**arr\_t**ndarray

Unless [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 is False and the other conditions for returning the input array are satisfied (see description for [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 input parameter), _arr\_t_ is a new array of the same shape as the input array, with dtype, order given by [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, _order_.

Raises:

ComplexWarning

When casting from complex to float or int. To avoid this, one should use `a.real.astype(t)`.

ValueError

When casting using `'same_value'` and the values change or would overflow

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 2.5\])
\>>> x
array(\[1. ,  2. ,  2.5\])

Copy to clipboard

\>>> x.astype(np.int\_)
array(\[1, 2, 2\])

Copy to clipboard

\>>> x.astype(np.int\_, casting\="same\_value")
Traceback (most recent call last):
...
ValueError: could not cast 'same\_value' double to long

Copy to clipboard

\>>> x\[:2\].astype(np.int\_, casting\="same\_value")
array(\[1, 2\])

Copy to clipboard

Go BackOpen In Tab

On this page