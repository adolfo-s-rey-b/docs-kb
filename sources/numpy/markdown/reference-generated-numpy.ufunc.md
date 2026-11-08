[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy-ufunc "Link to this heading")

=====================================================================================================================

_class_ numpy.ufunc[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "Link to this definition")

Functions that operate element by element on whole arrays.

To see the documentation for a specific ufunc, use [`info`](https://numpy.org/doc/stable/reference/generated/numpy.info.html#numpy.info "numpy.info")
. For example, `np.info(np.sin)`. Because ufuncs are written in C (for speed) and linked into Python with NumPy’s ufunc facility, Python’s help() function finds this page whenever help() is called on a ufunc.

A detailed explanation of ufuncs can be found in the docs for [Universal functions (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs)
.

**Calling ufuncs:** `op(*x[, out], where=True, **kwargs)`

Apply _op_ to the arguments _\*x_ elementwise, broadcasting the arguments.

The broadcasting rules are:

*   Dimensions of length 1 may be prepended to either array.
    
*   Arrays may be repeated along dimensions of length 1.
    

Parameters:

**\*x**array\_like

Input arrays.

**out**ndarray, None, …, or tuple of ndarray and None, optional

Location(s) into which the result(s) are stored. If not provided or None, new array(s) are created by the ufunc. If passed as a keyword argument, can be Ellipses (`out=...`) to ensure an array is returned even if the result is 0-dimensional, or a tuple with length equal to the number of outputs (where None can be used for allocation by the ufunc).

New in version 2.3: Support for `out=...` was added.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Attributes:

[`identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity")

The identity value.

[`nargs`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nargs.html#numpy.ufunc.nargs "numpy.ufunc.nargs")

The number of arguments.

[`nin`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nin.html#numpy.ufunc.nin "numpy.ufunc.nin")

The number of inputs.

[`nout`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nout.html#numpy.ufunc.nout "numpy.ufunc.nout")

The number of outputs.

[`ntypes`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.ntypes.html#numpy.ufunc.ntypes "numpy.ufunc.ntypes")

The number of types.

[`signature`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html#numpy.ufunc.signature "numpy.ufunc.signature")

Definition of the core elements a generalized ufunc operates on.

[`types`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#numpy.ufunc.types "numpy.ufunc.types")

Returns a list with types grouped input->output.

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.__call__.html#numpy.ufunc.__call__ "numpy.ufunc.__call__")<br>(\*args, \*\*kwargs) | Call self as a function. |
| [`accumulate`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#numpy.ufunc.accumulate "numpy.ufunc.accumulate")<br>(array\[, axis, dtype, out\]) | Accumulate the result of applying the operator to all elements. |
| [`at`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at")<br>(a, indices\[, b\]) | Performs unbuffered in place operation on operand 'a' for elements specified by 'indices'. |
| [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "numpy.ufunc.outer")<br>(A, B, /, \*\*kwargs) | Apply the ufunc _op_ to all pairs (a, b) with a in _A_ and b in _B_. |
| [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")<br>(array\[, axis, dtype, out, keepdims, ...\]) | Reduces [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")<br>'s dimension by one, by applying ufunc along one axis. |
| [`reduceat`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "numpy.ufunc.reduceat")<br>(array, indices\[, axis, dtype, out\]) | Performs a (local) reduce with specified slices over a single axis. |
| [`resolve_dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.resolve_dtypes.html#numpy.ufunc.resolve_dtypes "numpy.ufunc.resolve_dtypes")<br>(dtypes, \*\[, signature, ...\]) | Find the dtypes NumPy will use for the operation. |

Returns:

**r**ndarray or tuple of ndarray

_r_ will have the shape that the arrays in _x_ broadcast to; if _out_ is provided, it will be returned. If not, _r_ will be allocated and may contain uninitialized values. If the function has more than one output, then the result will be a tuple of arrays.

On this page