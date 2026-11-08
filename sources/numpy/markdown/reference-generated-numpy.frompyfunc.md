[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.frompyfunc.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.frompyfunc.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.frompyfunc.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.frompyfunc.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.frompyfunc.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.frompyfunc.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.frompyfunc.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.frompyfunc.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.frompyfunc.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.frompyfunc.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.frompyfunc.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.frompyfunc.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.frompyfunc.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.frompyfunc.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.frompyfunc.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.frompyfunc.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.frompyfunc.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.frompyfunc.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.frompyfunc.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.frompyfunc.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.frompyfunc[#](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#numpy-frompyfunc "Link to this heading")

====================================================================================================================================

numpy.frompyfunc(_func_, _/_, _nin_, _nout_, _\*_\[, _identity_\])[#](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#numpy.frompyfunc "Link to this definition")

Takes an arbitrary Python function and returns a NumPy ufunc.

Can be used, for example, to add broadcasting to a built-in Python function (see Examples section).

Parameters:

**func**Python function object

An arbitrary Python function.

**nin**int

The number of input arguments.

**nout**int

The number of objects returned by _func_.

**identity**object, optional

The value to use for the [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html#numpy.ufunc.identity "numpy.ufunc.identity")
 attribute of the resulting object. If specified, this is equivalent to setting the underlying C `identity` field to `PyUFunc_IdentityValue`. If omitted, the identity is set to `PyUFunc_None`. Note that this is \_not\_ equivalent to setting the identity to `None`, which implies the operation is reorderable.

Returns:

**out**ufunc

Returns a NumPy universal function (`ufunc`) object.

See also

[`vectorize`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")

Evaluates pyfunc over input arrays using broadcasting rules of numpy.

Notes

The returned ufunc always returns PyObject arrays.

Examples

Try it in your browser!

Use frompyfunc to add broadcasting to the Python function `oct`:

\>>> import numpy as np
\>>> oct\_array \= np.frompyfunc(oct, 1, 1)
\>>> oct\_array(np.array((10, 30, 100)))
array(\['0o12', '0o36', '0o144'\], dtype=object)
\>>> np.array((oct(10), oct(30), oct(100))) \# for comparison
array(\['0o12', '0o36', '0o144'\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page