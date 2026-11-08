[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.piecewise.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.piecewise.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.piecewise.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.piecewise.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.piecewise.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.piecewise.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.piecewise.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.piecewise.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.piecewise.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.piecewise.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.piecewise.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.piecewise.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.piecewise.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.piecewise.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.piecewise.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.piecewise.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.piecewise.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.piecewise.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.piecewise.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.piecewise.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.piecewise[#](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html#numpy-piecewise "Link to this heading")

=================================================================================================================================

numpy.piecewise(_x_, _condlist_, _funclist_, _\*args_, _\*\*kw_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L696-L815)
[#](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html#numpy.piecewise "Link to this definition")

Evaluate a piecewise-defined function.

Given a set of conditions and corresponding functions, evaluate each function on the input data wherever its condition is true.

Parameters:

**x**ndarray or scalar

The input domain.

**condlist**list of bool arrays or bool scalars

Each boolean array corresponds to a function in _funclist_. Wherever _condlist\[i\]_ is True, _funclist\[i\](x)_ is used as the output value.

Each boolean array in _condlist_ selects a piece of _x_, and should therefore be of the same shape as _x_.

The length of _condlist_ must correspond to that of _funclist_. If one extra function is given, i.e. if `len(funclist) == len(condlist) + 1`, then that extra function is the default value, used wherever all conditions are false.

**funclist**list of callables, f(x,\*args,\*\*kw), or scalars

Each function is evaluated over _x_ wherever its corresponding condition is True. It should take a 1d array as input and give a 1d array or a scalar value as output. If, instead of a callable, a scalar is provided then a constant function (`lambda x: scalar`) is assumed.

**args**tuple, optional

Any further arguments given to [`piecewise`](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html#numpy.piecewise "numpy.piecewise")
 are passed to the functions upon execution, i.e., if called `piecewise(..., ..., 1, 'a')`, then each function is called as `f(x, 1, 'a')`.

**kw**dict, optional

Keyword arguments used in calling [`piecewise`](https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html#numpy.piecewise "numpy.piecewise")
 are passed to the functions upon execution, i.e., if called `piecewise(..., ..., alpha=1)`, then each function is called as `f(x, alpha=1)`.

Returns:

**out**ndarray

The output is the same shape and type as x and is found by calling the functions in _funclist_ on the appropriate portions of _x_, as defined by the boolean arrays in _condlist_. Portions not covered by any condition have a default value of 0.

See also

[`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")
, [`select`](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select "numpy.select")
, [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")

Notes

This is similar to choose or select, except that functions are evaluated on elements of _x_ that satisfy the corresponding condition from _condlist_.

The result is:

      |--
      |funclist\[0\](x\[condlist\[0\]\])
out \= |funclist\[1\](x\[condlist\[1\]\])
      |...
      |funclist\[n2\](x\[condlist\[n2\]\])
      |--

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Define the signum function, which is -1 for `x < 0` and +1 for `x >= 0`.

\>>> x \= np.linspace(\-2.5, 2.5, 6)
\>>> np.piecewise(x, \[x < 0, x \>= 0\], \[\-1, 1\])
array(\[-1., -1., -1.,  1.,  1.,  1.\])

Copy to clipboard

Define the absolute value, which is `-x` for `x <0` and `x` for `x >= 0`.

\>>> np.piecewise(x, \[x < 0, x \>= 0\], \[lambda x: \-x, lambda x: x\])
array(\[2.5,  1.5,  0.5,  0.5,  1.5,  2.5\])

Copy to clipboard

Apply the same function to a scalar value.

\>>> y \= \-2
\>>> np.piecewise(y, \[y < 0, y \>= 0\], \[lambda x: \-x, lambda x: x\])
array(2)

Copy to clipboard

Go BackOpen In Tab

On this page