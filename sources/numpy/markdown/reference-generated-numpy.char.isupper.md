[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.isupper.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.isupper.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.isupper.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.isupper.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.isupper.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.isupper.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.isupper.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.isupper.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.isupper.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.isupper.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.isupper.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.isupper.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.isupper.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.isupper.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.isupper.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.isupper.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.isupper.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.isupper.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.isupper.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.isupper.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.isupper[#](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html#numpy-char-isupper "Link to this heading")

==========================================================================================================================================

char.isupper(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'isupper'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.char.isupper.html#numpy.char.isupper "Link to this definition")

Return true for each element if all cased characters in the string are uppercase and there is at least one character, false otherwise.

Parameters:

**x**array\_like, with `StringDType`, `bytes_` or `str_` dtype

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray

Output array of bools This is a scalar if _x_ is a scalar.

See also

[`str.isupper`](https://docs.python.org/3/library/stdtypes.html#str.isupper "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.strings.isupper("GHC")
array(True)
\>>> a \= np.array(\["hello", "HELLO", "Hello"\])
\>>> np.strings.isupper(a)
array(\[False,  True, False\])

Copy to clipboard

Go BackOpen In Tab

On this page