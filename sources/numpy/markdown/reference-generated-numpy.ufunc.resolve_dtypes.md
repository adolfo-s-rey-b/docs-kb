[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.resolve_dtypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.resolve_dtypes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.resolve_dtypes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.resolve_dtypes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.resolve\_dtypes[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.resolve_dtypes.html#numpy-ufunc-resolve-dtypes "Link to this heading")

===================================================================================================================================================================

method

ufunc.resolve\_dtypes(_dtypes_, _\*_, _signature\=None_, _casting\=None_, _reduction\=False_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.resolve_dtypes.html#numpy.ufunc.resolve_dtypes "Link to this definition")

Find the dtypes NumPy will use for the operation. Both input and output dtypes are returned and may differ from those provided.

Note

This function always applies NEP 50 rules since it is not provided any actual values. The Python types `int`, `float`, and `complex` thus behave weak and should be passed for “untyped” Python input.

Parameters:

**dtypes**tuple of dtypes, None, or literal int, float, complex

The input dtypes for each operand. Output operands can be None, indicating that the dtype must be found.

**signature**tuple of DTypes or None, optional

If given, enforces exact DType (classes) of the specific operand. The ufunc `dtype` argument is equivalent to passing a tuple with only output dtypes set.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

The casting mode when casting is necessary. This is identical to the ufunc call casting modes.

**reduction**boolean

If given, the resolution assumes a reduce operation is happening which slightly changes the promotion and type resolution rules. [`dtypes`](https://numpy.org/doc/stable/reference/routines.dtypes.html#module-numpy.dtypes "numpy.dtypes")
 is usually something like `(None, np.dtype("i2"), None)` for reductions (first input is also the output).

Note

The default casting mode is “same\_kind”, however, as of NumPy 1.24, NumPy uses “unsafe” for reductions.

Returns:

**dtypes**tuple of dtypes

The dtypes which NumPy would use for the calculation. Note that dtypes may not match the passed in ones (casting is necessary).

Examples

Try it in your browser!

This API requires passing dtypes, define them for convenience:

\>>> import numpy as np
\>>> int32 \= np.dtype(np.int32)
\>>> float32 \= np.dtype(np.float32)

Copy to clipboard

The typical ufunc call does not pass an output dtype. [`numpy.add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")
 has two inputs and one output, so leave the output as `None` (not provided):

\>>> np.add.resolve\_dtypes((int32, float32, None))
(dtype('float64'), dtype('float64'), dtype('float64'))

Copy to clipboard

The loop found uses “float64” for all operands (including the output), the first input would be cast.

`resolve_dtypes` supports “weak” handling for Python scalars by passing `int`, `float`, or `complex`:

\>>> np.add.resolve\_dtypes((float32, float, None))
(dtype('float32'), dtype('float32'), dtype('float32'))

Copy to clipboard

Where the Python `float` behaves similar to a Python value `0.0` in a ufunc call. (See [NEP 50](https://numpy.org/neps/nep-0050-scalar-promotion.html#nep50 "(in NumPy Enhancement Proposals)")
 for details.)

Go BackOpen In Tab

On this page