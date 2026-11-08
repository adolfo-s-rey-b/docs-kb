[Skip to main content](https://numpy.org/doc/stable/reference/ufuncs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/ufuncs.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/ufuncs.html)
[2.4](https://numpy.org/doc/2.4/reference/ufuncs.html)
[2.3](https://numpy.org/doc/2.3/reference/ufuncs.html)
[2.2](https://numpy.org/doc/2.2/reference/ufuncs.html)
[2.1](https://numpy.org/doc/2.1/reference/ufuncs.html)
[2.0](https://numpy.org/doc/2.0/reference/ufuncs.html)
[1.26](https://numpy.org/doc/1.26/reference/ufuncs.html)
[1.25](https://numpy.org/doc/1.25/reference/ufuncs.html)
[1.24](https://numpy.org/doc/1.24/reference/ufuncs.html)
[1.23](https://numpy.org/doc/1.23/reference/ufuncs.html)
[1.22](https://numpy.org/doc/1.22/reference/ufuncs.html)
[1.21](https://numpy.org/doc/1.21/reference/ufuncs.html)
[1.20](https://numpy.org/doc/1.20/reference/ufuncs.html)
[1.19](https://numpy.org/doc/1.19/reference/ufuncs.html)
[1.18](https://numpy.org/doc/1.18/reference/ufuncs.html)
[1.17](https://numpy.org/doc/1.17/reference/ufuncs.html)
[1.16](https://numpy.org/doc/1.16/reference/ufuncs.html)
[1.15](https://numpy.org/doc/1.15/reference/ufuncs.html)
[1.14](https://numpy.org/doc/1.14/reference/ufuncs.html)
[1.13](https://numpy.org/doc/1.13/reference/ufuncs.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Universal functions ([`ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
)[#](https://numpy.org/doc/stable/reference/ufuncs.html#universal-functions-ufunc "Link to this heading")

======================================================================================================================================================================================================================================

See also

[Universal functions (ufunc) basics](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)

A universal function (or [ufunc](https://numpy.org/doc/stable/glossary.html#term-ufunc)
 for short) is a function that operates on [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in an element-by-element fashion, supporting [array broadcasting](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-broadcasting)
, [type casting](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-casting)
, and several other standard features. That is, a ufunc is a “[vectorized](https://numpy.org/doc/stable/glossary.html#term-vectorization)
” wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs. For detailed information on universal functions, see [Universal functions (ufunc) basics](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)
.

There are also [generalized ufuncs](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#c-api-generalized-ufuncs)
 which are functions over vectors (or arrays) instead of only single-element scalars.

[`ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
[#](https://numpy.org/doc/stable/reference/ufuncs.html#ufunc "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`numpy.ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")<br>() | Functions that operate element by element on whole arrays. |

### Optional keyword arguments[#](https://numpy.org/doc/stable/reference/ufuncs.html#optional-keyword-arguments "Link to this heading")

All ufuncs take optional keyword arguments. Most of these represent advanced usage and will not typically be used.

_out_

The first output can be provided as either a positional or a keyword parameter. Keyword ‘out’ arguments are incompatible with positional ones.

The ‘out’ keyword argument is expected to be a tuple with one entry per output (which can be None for arrays to be allocated by the ufunc). For ufuncs with a single output, passing a single array (instead of a tuple holding a single array) is also valid.

If ‘out’ is None (the default), a uninitialized output array is created, which will be filled in the ufunc. At the end, this array is returned unless it is zero-dimensional, in which case it is converted to a scalar; this conversion can be avoided by passing in `out=...`. This can also be spelled _out=Ellipsis_ if you think that is clearer.

Note that the output is filled only in the places that the broadcast ‘where’ is True. If ‘where’ is the scalar True (the default), then this corresponds to all elements of the output, but in other cases, the elements not explicitly filled are left with their uninitialized values.

Operations where ufunc input and output operands have memory overlap are defined to be the same as for equivalent operations where there is no memory overlap. Operations affected make temporary copies as needed to eliminate data dependency. As detecting these cases is computationally expensive, a heuristic is used, which may in rare cases result in needless temporary copies. For operations where the data dependency is simple enough for the heuristic to analyze, temporary copies will not be made even if the arrays overlap, if it can be deduced copies are not necessary. As an example, `np.add(a, b, out=a)` will not involve copies.

_where_

Accepts a boolean array which is broadcast together with the operands. Values of True indicate to calculate the ufunc at that position, values of False indicate to leave the value in the output alone. This argument cannot be used for generalized ufuncs as those take non-scalar input.

Note that if an uninitialized return array is created, values of False will leave those values **uninitialized**.

_axes_

A list of tuples with indices of axes a generalized ufunc should operate on. For instance, for a signature of `(i,j),(j,k)->(i,k)` appropriate for matrix multiplication, the base elements are two-dimensional matrices and these are taken to be stored in the two last axes of each argument. The corresponding axes keyword would be `[(-2, -1), (-2, -1), (-2, -1)]`. For simplicity, for generalized ufuncs that operate on 1-dimensional arrays (vectors), a single integer is accepted instead of a single-element tuple, and for generalized ufuncs for which all outputs are scalars, the output tuples can be omitted.

_axis_

A single axis over which a generalized ufunc should operate. This is a short-cut for ufuncs that operate over a single, shared core dimension, equivalent to passing in `axes` with entries of `(axis,)` for each single-core-dimension argument and `()` for all others. For instance, for a signature `(i),(i)->()`, it is equivalent to passing in `axes=[(axis,), (axis,), ()]`.

_keepdims_

If this is set to _True_, axes which are reduced over will be left in the result as a dimension with size one, so that the result will broadcast correctly against the inputs. This option can only be used for generalized ufuncs that operate on inputs that all have the same number of core dimensions and with outputs that have no core dimensions, i.e., with signatures like `(i),(i)->()` or `(m,m)->()`. If used, the location of the dimensions in the output can be controlled with `axes` and `axis`.

_casting_

May be ‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, or ‘unsafe’. See [`can_cast`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")
 for explanations of the parameter values.

Provides a policy for what kind of casting is permitted. For compatibility with previous versions of NumPy, this defaults to ‘unsafe’ for numpy < 1.7. In numpy 1.7 a transition to ‘same\_kind’ was begun where ufuncs produce a DeprecationWarning for calls which are allowed under the ‘unsafe’ rules, but not under the ‘same\_kind’ rules. From numpy 1.10 and onwards, the default is ‘same\_kind’.

_order_

Specifies the calculation iteration order/memory layout of the output array. Defaults to ‘K’. ‘C’ means the output should be C-contiguous, ‘F’ means F-contiguous, ‘A’ means F-contiguous if the inputs are F-contiguous and not also not C-contiguous, C-contiguous otherwise, and ‘K’ means to match the element ordering of the inputs as closely as possible.

_dtype_

Overrides the DType of the output arrays the same way as the _signature_. This should ensure a matching precision of the calculation. The exact calculation DTypes chosen may depend on the ufunc and the inputs may be cast to this DType to perform the calculation.

_subok_

Defaults to true. If set to false, the output will always be a strict array, not a subtype.

_signature_

Either a Dtype, a tuple of DTypes, or a special signature string indicating the input and output types of a ufunc.

This argument allows the user to specify exact DTypes to be used for the calculation. Casting will be used as necessary. The actual DType of the input arrays is not considered unless `signature` is `None` for that array.

When all DTypes are fixed, a specific loop is chosen or an error raised if no matching loop exists. If some DTypes are not specified and left `None`, the behaviour may depend on the ufunc. At this time, a list of available signatures is provided by the **types** attribute of the ufunc. (This list may be missing DTypes not defined by NumPy.)

The `signature` only specifies the DType class/type. For example, it can specify that the operation should be `datetime64` or `float64` operation. It does not specify the `datetime64` time-unit or the `float64` byte-order.

For backwards compatibility this argument can also be provided as _sig_, although the long form is preferred. Note that this should not be confused with the generalized ufunc [signature](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#details-of-signature)
 that is stored in the **signature** attribute of the of the ufunc object.

### Attributes[#](https://numpy.org/doc/stable/reference/ufuncs.html#attributes "Link to this heading")

There are some informational attributes that universal functions possess. None of the attributes can be set.

|     |     |
| --- | --- |
| **\_\_doc\_\_** | A docstring for each ufunc. The first part of the docstring is dynamically generated from the number of outputs, the name, and the number of inputs. The second part of the docstring is provided at creation time and stored with the ufunc. |
| **\_\_name\_\_** | The name of the ufunc. |
| **\_\_signature\_\_** | The call signature of the ufunc, as an [`inspect.Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "(in Python v3.14)")<br> object. |

|     |     |
| --- | --- |
| [`ufunc.nin`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nin.html#numpy.ufunc.nin "numpy.ufunc.nin") | The number of inputs. |
| [`ufunc.nout`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nout.html#numpy.ufunc.nout "numpy.ufunc.nout") | The number of outputs. |
| [`ufunc.nargs`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.nargs.html#numpy.ufunc.nargs "numpy.ufunc.nargs") | The number of arguments. |
| [`ufunc.ntypes`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.ntypes.html#numpy.ufunc.ntypes "numpy.ufunc.ntypes") | The number of types. |
| [`ufunc.types`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#numpy.ufunc.types "numpy.ufunc.types") | Returns a list with types grouped input->output. |
| [`ufunc.identity`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html#numpy.ufunc.identity "numpy.ufunc.identity") | The identity value. |
| [`ufunc.signature`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.signature.html#numpy.ufunc.signature "numpy.ufunc.signature") | Definition of the core elements a generalized ufunc operates on. |

### Methods[#](https://numpy.org/doc/stable/reference/ufuncs.html#methods "Link to this heading")

|     |     |
| --- | --- |
| [`ufunc.reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")<br>(array\[, axis, dtype, out, ...\]) | Reduces [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")<br>'s dimension by one, by applying ufunc along one axis. |
| [`ufunc.accumulate`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#numpy.ufunc.accumulate "numpy.ufunc.accumulate")<br>(array\[, axis, dtype, out\]) | Accumulate the result of applying the operator to all elements. |
| [`ufunc.reduceat`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "numpy.ufunc.reduceat")<br>(array, indices\[, axis, ...\]) | Performs a (local) reduce with specified slices over a single axis. |
| [`ufunc.outer`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "numpy.ufunc.outer")<br>(A, B, /, \*\*kwargs) | Apply the ufunc _op_ to all pairs (a, b) with a in _A_ and b in _B_. |
| [`ufunc.at`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at")<br>(a, indices\[, b\]) | Performs unbuffered in place operation on operand 'a' for elements specified by 'indices'. |

Warning

A reduce-like operation on an array with a data-type that has a range “too small” to handle the result will silently wrap. One should use [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 to increase the size of the data-type over which reduction takes place.

Available ufuncs[#](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs "Link to this heading")

----------------------------------------------------------------------------------------------------------------

There are currently more than 60 universal functions defined in [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
 on one or more types, covering a wide variety of operations. Some of these ufuncs are called automatically on arrays when the relevant infix notation is used (_e.g._, [`add(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")
 is called internally when `a + b` is written and _a_ or _b_ is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
). Nevertheless, you may still want to use the ufunc call in order to use the optional output argument(s) to place the output(s) in an object (or objects) of your choice.

Recall that each ufunc operates element-by-element. Therefore, each scalar ufunc will be described as if acting on a set of scalar inputs to return a set of scalar outputs.

Note

The ufunc still returns its output(s) even if you use the optional output argument(s).

### Math operations[#](https://numpy.org/doc/stable/reference/ufuncs.html#math-operations "Link to this heading")

|     |     |
| --- | --- |
| [`add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Add arguments element-wise. |
| [`subtract`](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html#numpy.subtract "numpy.subtract")<br>(x1, x2, /\[, out, where, casting, ...\]) | Subtract arguments, element-wise. |
| [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html#numpy.multiply "numpy.multiply")<br>(x1, x2, /\[, out, where, casting, ...\]) | Multiply arguments element-wise. |
| [`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")<br>(x1, x2, /\[, out, casting, order, ...\]) | Matrix product of two arrays. |
| [`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html#numpy.divide "numpy.divide")<br>(x1, x2, /\[, out, where, casting, ...\]) | Divide arguments element-wise. |
| [`logaddexp`](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html#numpy.logaddexp "numpy.logaddexp")<br>(x1, x2, /\[, out, where, casting, ...\]) | Logarithm of the sum of exponentiations of the inputs. |
| [`logaddexp2`](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html#numpy.logaddexp2 "numpy.logaddexp2")<br>(x1, x2, /\[, out, where, casting, ...\]) | Logarithm of the sum of exponentiations of the inputs in base-2. |
| [`true_divide`](https://numpy.org/doc/stable/reference/generated/numpy.true_divide.html#numpy.true_divide "numpy.true_divide")<br>(x1, x2, /\[, out, where, ...\]) | Divide arguments element-wise. |
| [`floor_divide`](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html#numpy.floor_divide "numpy.floor_divide")<br>(x1, x2, /\[, out, where, ...\]) | Return the largest integer smaller or equal to the division of the inputs. |
| [`negative`](https://numpy.org/doc/stable/reference/generated/numpy.negative.html#numpy.negative "numpy.negative")<br>(x, /\[, out, where, casting, order, ...\]) | Numerical negation, element-wise. |
| [`positive`](https://numpy.org/doc/stable/reference/generated/numpy.positive.html#numpy.positive "numpy.positive")<br>(x, /\[, out, where, casting, order, ...\]) | Numerical positive, element-wise. |
| [`power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")<br>(x1, x2, /\[, out, where, casting, ...\]) | First array elements raised to powers from second array, element-wise. |
| [`float_power`](https://numpy.org/doc/stable/reference/generated/numpy.float_power.html#numpy.float_power "numpy.float_power")<br>(x1, x2, /\[, out, where, ...\]) | First array elements raised to powers from second array, element-wise. |
| [`remainder`](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy.remainder "numpy.remainder")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns the element-wise remainder of division. |
| [`mod`](https://numpy.org/doc/stable/reference/generated/numpy.mod.html#numpy.mod "numpy.mod")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the element-wise remainder of division. |
| [`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns the element-wise remainder of division. |
| [`divmod`](https://numpy.org/doc/stable/reference/generated/numpy.divmod.html#numpy.divmod "numpy.divmod")<br>(x1, x2\[, out1, out2\], / \[\[, out, ...\]) | Return element-wise quotient and remainder simultaneously. |\
| [`absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "numpy.absolute")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate the absolute value element-wise. |\
| [`fabs`](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#numpy.fabs "numpy.fabs")<br>(x, /\[, out, where, casting, order, ...\]) | Compute the absolute values element-wise. |\
| [`rint`](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy.rint "numpy.rint")<br>(x, /\[, out, where, casting, order, ...\]) | Round elements of the array to the nearest integer. |\
| [`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")<br>(x, /\[, out, where, casting, order, ...\]) | Returns an element-wise indication of the sign of a number. |\
| [`heaviside`](https://numpy.org/doc/stable/reference/generated/numpy.heaviside.html#numpy.heaviside "numpy.heaviside")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the Heaviside step function. |\
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.conj.html#numpy.conj "numpy.conj")<br>(x, /\[, out, where, casting, order, ...\]) | Return the complex conjugate, element-wise. |\
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.conjugate.html#numpy.conjugate "numpy.conjugate")<br>(x, /\[, out, where, casting, ...\]) | Return the complex conjugate, element-wise. |\
| [`exp`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate the exponential of all elements in the input array. |\
| [`exp2`](https://numpy.org/doc/stable/reference/generated/numpy.exp2.html#numpy.exp2 "numpy.exp2")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate _2\*\*p_ for all _p_ in the input array. |\
| [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")<br>(x, /\[, out, where, casting, order, ...\]) | Natural logarithm, element-wise. |\
| [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")<br>(x, /\[, out, where, casting, order, ...\]) | Base-2 logarithm of _x_. |\
| [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")<br>(x, /\[, out, where, casting, order, ...\]) | Return the base 10 logarithm of the input array, element-wise. |\
| [`expm1`](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate `exp(x) - 1` for all elements in the array. |\
| [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")<br>(x, /\[, out, where, casting, order, ...\]) | Return the natural logarithm of one plus the input array, element-wise. |\
| [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")<br>(x, /\[, out, where, casting, order, ...\]) | Return the non-negative square-root of an array, element-wise. |\
| [`square`](https://numpy.org/doc/stable/reference/generated/numpy.square.html#numpy.square "numpy.square")<br>(x, /\[, out, where, casting, order, ...\]) | Return the element-wise square of the input. |\
| [`cbrt`](https://numpy.org/doc/stable/reference/generated/numpy.cbrt.html#numpy.cbrt "numpy.cbrt")<br>(x, /\[, out, where, casting, order, ...\]) | Return the cube-root of an array, element-wise. |\
| [`reciprocal`](https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html#numpy.reciprocal "numpy.reciprocal")<br>(x, /\[, out, where, casting, ...\]) | Return the reciprocal of the argument, element-wise. |\
| [`gcd`](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html#numpy.gcd "numpy.gcd")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the greatest common divisor of `\|x1\|` and `\|x2\|` |\
| [`lcm`](https://numpy.org/doc/stable/reference/generated/numpy.lcm.html#numpy.lcm "numpy.lcm")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the lowest common multiple of `\|x1\|` and `\|x2\|` |\
\
Tip\
\
The optional output arguments can be used to help you save memory for large calculations. If your arrays are large, complicated expressions can take longer than absolutely necessary due to the creation and (later) destruction of temporary calculation spaces. For example, the expression `G = A * B + C` is equivalent to `T1 = A * B; G = T1 + C; del T1`. It will be more quickly executed as `G = A * B; add(G, C, G)` which is the same as `G = A * B; G += C`.\
\
### Trigonometric functions[#](https://numpy.org/doc/stable/reference/ufuncs.html#trigonometric-functions "Link to this heading")\
\
All trigonometric functions use radians when an angle is called for. The ratio of degrees to radians is \\(180^{\\circ}/\\pi.\\)\
\
|     |     |\
| --- | --- |\
| [`sin`](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric sine, element-wise. |\
| [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")<br>(x, /\[, out, where, casting, order, ...\]) | Cosine element-wise. |\
| [`tan`](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")<br>(x, /\[, out, where, casting, order, ...\]) | Compute tangent element-wise. |\
| [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse sine, element-wise. |\
| [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse cosine, element-wise. |\
| [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse tangent, element-wise. |\
| [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise arc tangent of `x1/x2` choosing the quadrant correctly. |\
| [`hypot`](https://numpy.org/doc/stable/reference/generated/numpy.hypot.html#numpy.hypot "numpy.hypot")<br>(x1, x2, /\[, out, where, casting, ...\]) | Given the "legs" of a right triangle, return its hypotenuse. |\
| [`sinh`](https://numpy.org/doc/stable/reference/generated/numpy.sinh.html#numpy.sinh "numpy.sinh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic sine, element-wise. |\
| [`cosh`](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#numpy.cosh "numpy.cosh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic cosine, element-wise. |\
| [`tanh`](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#numpy.tanh "numpy.tanh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic tangent, element-wise. |\
| [`arcsinh`](https://numpy.org/doc/stable/reference/generated/numpy.arcsinh.html#numpy.arcsinh "numpy.arcsinh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic sine, element-wise. |\
| [`arccosh`](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html#numpy.arccosh "numpy.arccosh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic cosine, element-wise. |\
| [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic tangent, element-wise. |\
| [`degrees`](https://numpy.org/doc/stable/reference/generated/numpy.degrees.html#numpy.degrees "numpy.degrees")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from radians to degrees. |\
| [`radians`](https://numpy.org/doc/stable/reference/generated/numpy.radians.html#numpy.radians "numpy.radians")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from degrees to radians. |\
| [`deg2rad`](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html#numpy.deg2rad "numpy.deg2rad")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from degrees to radians. |\
| [`rad2deg`](https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html#numpy.rad2deg "numpy.rad2deg")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from radians to degrees. |\
\
### Bit-twiddling functions[#](https://numpy.org/doc/stable/reference/ufuncs.html#bit-twiddling-functions "Link to this heading")\
\
These function all require integer arguments and they manipulate the bit-pattern of those arguments.\
\
|     |     |\
| --- | --- |\
| [`bitwise_and`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html#numpy.bitwise_and "numpy.bitwise_and")<br>(x1, x2, /\[, out, where, ...\]) | Compute the bit-wise AND of two arrays element-wise. |\
| [`bitwise_or`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html#numpy.bitwise_or "numpy.bitwise_or")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the bit-wise OR of two arrays element-wise. |\
| [`bitwise_xor`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy.bitwise_xor "numpy.bitwise_xor")<br>(x1, x2, /\[, out, where, ...\]) | Compute the bit-wise XOR of two arrays element-wise. |\
| [`invert`](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "numpy.invert")<br>(x, /\[, out, where, casting, order, ...\]) | Compute bit-wise inversion, or bit-wise NOT, element-wise. |\
| [`left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy.left_shift "numpy.left_shift")<br>(x1, x2, /\[, out, where, casting, ...\]) | Shift the bits of an integer to the left. |\
| [`right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.right_shift.html#numpy.right_shift "numpy.right_shift")<br>(x1, x2, /\[, out, where, ...\]) | Shift the bits of an integer to the right. |\
\
### Comparison functions[#](https://numpy.org/doc/stable/reference/ufuncs.html#comparison-functions "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`greater`](https://numpy.org/doc/stable/reference/generated/numpy.greater.html#numpy.greater "numpy.greater")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 > x2) element-wise. |\
| [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater_equal "numpy.greater_equal")<br>(x1, x2, /\[, out, where, ...\]) | Return the truth value of (x1 >= x2) element-wise. |\
| [`less`](https://numpy.org/doc/stable/reference/generated/numpy.less.html#numpy.less "numpy.less")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 < x2) element-wise. |\
| [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html#numpy.less_equal "numpy.less_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 <= x2) element-wise. |\
| [`not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy.not_equal "numpy.not_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 != x2) element-wise. |\
| [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 == x2) element-wise. |\
\
Warning\
\
Do not use the Python keywords `and` and `or` to combine logical array expressions. These keywords will test the truth value of the entire array (not element-by-element as you might expect). Use the bitwise operators & and | instead.\
\
|     |     |\
| --- | --- |\
| [`logical_and`](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")<br>(x1, x2, /\[, out, where, ...\]) | Compute the truth value of x1 AND x2 element-wise. |\
| [`logical_or`](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the truth value of x1 OR x2 element-wise. |\
| [`logical_xor`](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")<br>(x1, x2, /\[, out, where, ...\]) | Compute the truth value of x1 XOR x2, element-wise. |\
| [`logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")<br>(x, /\[, out, where, casting, ...\]) | Compute the truth value of NOT x element-wise. |\
\
Warning\
\
The bit-wise operators & and | are the proper way to perform element-by-element array comparisons. Be sure you understand the operator precedence: `(a > 2) & (a < 5)` is the proper syntax because `a > 2 & a < 5` will result in an error due to the fact that `2 & a` is evaluated first.\
\
|     |     |\
| --- | --- |\
| [`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise maximum of array elements. |\
\
Tip\
\
The Python function `max()` will find the maximum over a one-dimensional array, but it will do so using a slower sequence interface. The reduce method of the maximum ufunc is much faster. Also, the `max()` method will not give answers you might expect for arrays with greater than one dimension. The reduce method of minimum also allows you to compute a total minimum over an array.\
\
|     |     |\
| --- | --- |\
| [`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise minimum of array elements. |\
\
Warning\
\
the behavior of `maximum(a, b)` is different than that of `max(a, b)`. As a ufunc, `maximum(a, b)` performs an element-by-element comparison of _a_ and _b_ and chooses each element of the result according to which element in the two arrays is larger. In contrast, `max(a, b)` treats the objects _a_ and _b_ as a whole, looks at the (total) truth value of `a > b` and uses it to return either _a_ or _b_ (as a whole). A similar difference exists between `minimum(a, b)` and `min(a, b)`.\
\
|     |     |\
| --- | --- |\
| [`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise maximum of array elements. |\
| [`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise minimum of array elements. |\
\
### Floating functions[#](https://numpy.org/doc/stable/reference/ufuncs.html#floating-functions "Link to this heading")\
\
Recall that all of these functions work element-by-element over an array, returning an array output. The description details only a single operation.\
\
|     |     |\
| --- | --- |\
| [`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for finiteness (not infinity and not Not a Number). |\
| [`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for positive or negative infinity. |\
| [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for NaN and return result as a boolean array. |\
| [`isnat`](https://numpy.org/doc/stable/reference/generated/numpy.isnat.html#numpy.isnat "numpy.isnat")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for NaT (not a time) and return result as a boolean array. |\
| [`fabs`](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#numpy.fabs "numpy.fabs")<br>(x, /\[, out, where, casting, order, ...\]) | Compute the absolute values element-wise. |\
| [`signbit`](https://numpy.org/doc/stable/reference/generated/numpy.signbit.html#numpy.signbit "numpy.signbit")<br>(x, /\[, out, where, casting, order, ...\]) | Returns element-wise True where signbit is set (less than zero). |\
| [`copysign`](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#numpy.copysign "numpy.copysign")<br>(x1, x2, /\[, out, where, casting, ...\]) | Change the sign of x1 to that of x2, element-wise. |\
| [`nextafter`](https://numpy.org/doc/stable/reference/generated/numpy.nextafter.html#numpy.nextafter "numpy.nextafter")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the next floating-point value after x1 towards x2, element-wise. |\
| [`spacing`](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy.spacing "numpy.spacing")<br>(x, /\[, out, where, casting, order, ...\]) | Return the distance between x and the nearest adjacent number. |\
| [`modf`](https://numpy.org/doc/stable/reference/generated/numpy.modf.html#numpy.modf "numpy.modf")<br>(x\[, out1, out2\], / \[\[, out, where, ...\]) | Return the fractional and integral parts of an array, element-wise. |\
| [`ldexp`](https://numpy.org/doc/stable/reference/generated/numpy.ldexp.html#numpy.ldexp "numpy.ldexp")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns x1 \* 2\*\*x2, element-wise. |\
| [`frexp`](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#numpy.frexp "numpy.frexp")<br>(x\[, out1, out2\], / \[\[, out, where, ...\]) | Decompose the elements of x into mantissa and twos exponent. |\
| [`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns the element-wise remainder of division. |\
| [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")<br>(x, /\[, out, where, casting, order, ...\]) | Return the floor of the input, element-wise. |\
| [`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil")<br>(x, /\[, out, where, casting, order, ...\]) | Return the ceiling of the input, element-wise. |\
| [`trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")<br>(x, /\[, out, where, casting, order, ...\]) | Return the truncated value of the input, element-wise. |\
\
On this page