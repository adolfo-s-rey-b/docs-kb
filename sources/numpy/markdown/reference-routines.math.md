[Skip to main content](https://numpy.org/doc/stable/reference/routines.math.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.math.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.math.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.math.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.math.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.math.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.math.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.math.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.math.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.math.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.math.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.math.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.math.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.math.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.math.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.math.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.math.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.math.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.math.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.math.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.math.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.math.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Mathematical functions[#](https://numpy.org/doc/stable/reference/routines.math.html#mathematical-functions "Link to this heading")

===================================================================================================================================

Trigonometric functions[#](https://numpy.org/doc/stable/reference/routines.math.html#trigonometric-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`sin`](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric sine, element-wise. |
| [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")<br>(x, /\[, out, where, casting, order, ...\]) | Cosine element-wise. |
| [`tan`](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")<br>(x, /\[, out, where, casting, order, ...\]) | Compute tangent element-wise. |
| [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse sine, element-wise. |
| [`asin`](https://numpy.org/doc/stable/reference/generated/numpy.asin.html#numpy.asin "numpy.asin")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse sine, element-wise. |
| [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse cosine, element-wise. |
| [`acos`](https://numpy.org/doc/stable/reference/generated/numpy.acos.html#numpy.acos "numpy.acos")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse cosine, element-wise. |
| [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse tangent, element-wise. |
| [`atan`](https://numpy.org/doc/stable/reference/generated/numpy.atan.html#numpy.atan "numpy.atan")<br>(x, /\[, out, where, casting, order, ...\]) | Trigonometric inverse tangent, element-wise. |
| [`hypot`](https://numpy.org/doc/stable/reference/generated/numpy.hypot.html#numpy.hypot "numpy.hypot")<br>(x1, x2, /\[, out, where, casting, ...\]) | Given the "legs" of a right triangle, return its hypotenuse. |
| [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise arc tangent of `x1/x2` choosing the quadrant correctly. |
| [`atan2`](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#numpy.atan2 "numpy.atan2")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise arc tangent of `x1/x2` choosing the quadrant correctly. |
| [`degrees`](https://numpy.org/doc/stable/reference/generated/numpy.degrees.html#numpy.degrees "numpy.degrees")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from radians to degrees. |
| [`radians`](https://numpy.org/doc/stable/reference/generated/numpy.radians.html#numpy.radians "numpy.radians")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from degrees to radians. |
| [`unwrap`](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html#numpy.unwrap "numpy.unwrap")<br>(p\[, discont, axis, period\]) | Unwrap by taking the complement of large deltas with respect to the period. |
| [`deg2rad`](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html#numpy.deg2rad "numpy.deg2rad")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from degrees to radians. |
| [`rad2deg`](https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html#numpy.rad2deg "numpy.rad2deg")<br>(x, /\[, out, where, casting, order, ...\]) | Convert angles from radians to degrees. |

Hyperbolic functions[#](https://numpy.org/doc/stable/reference/routines.math.html#hyperbolic-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`sinh`](https://numpy.org/doc/stable/reference/generated/numpy.sinh.html#numpy.sinh "numpy.sinh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic sine, element-wise. |
| [`cosh`](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#numpy.cosh "numpy.cosh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic cosine, element-wise. |
| [`tanh`](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#numpy.tanh "numpy.tanh")<br>(x, /\[, out, where, casting, order, ...\]) | Hyperbolic tangent, element-wise. |
| [`arcsinh`](https://numpy.org/doc/stable/reference/generated/numpy.arcsinh.html#numpy.arcsinh "numpy.arcsinh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic sine, element-wise. |
| [`asinh`](https://numpy.org/doc/stable/reference/generated/numpy.asinh.html#numpy.asinh "numpy.asinh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic sine, element-wise. |
| [`arccosh`](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html#numpy.arccosh "numpy.arccosh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic cosine, element-wise. |
| [`acosh`](https://numpy.org/doc/stable/reference/generated/numpy.acosh.html#numpy.acosh "numpy.acosh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic cosine, element-wise. |
| [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic tangent, element-wise. |
| [`atanh`](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html#numpy.atanh "numpy.atanh")<br>(x, /\[, out, where, casting, order, ...\]) | Inverse hyperbolic tangent, element-wise. |

Rounding[#](https://numpy.org/doc/stable/reference/routines.math.html#rounding "Link to this heading")

-------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")<br>(a\[, decimals, out\]) | Evenly round to the given number of decimals. |
| [`around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")<br>(a\[, decimals, out\]) | Round an array to the given number of decimals. |
| [`rint`](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy.rint "numpy.rint")<br>(x, /\[, out, where, casting, order, ...\]) | Round elements of the array to the nearest integer. |
| [`fix`](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy.fix "numpy.fix")<br>(x\[, out\]) | Round to nearest integer towards zero. |
| [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")<br>(x, /\[, out, where, casting, order, ...\]) | Return the floor of the input, element-wise. |
| [`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil")<br>(x, /\[, out, where, casting, order, ...\]) | Return the ceiling of the input, element-wise. |
| [`trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")<br>(x, /\[, out, where, casting, order, ...\]) | Return the truncated value of the input, element-wise. |

Sums, products, differences[#](https://numpy.org/doc/stable/reference/routines.math.html#sums-products-differences "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")<br>(a\[, axis, dtype, out, keepdims, ...\]) | Return the product of array elements over a given axis. |
| [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")<br>(a\[, axis, dtype, out, keepdims, ...\]) | Sum of array elements over a given axis. |
| [`nanprod`](https://numpy.org/doc/stable/reference/generated/numpy.nanprod.html#numpy.nanprod "numpy.nanprod")<br>(a\[, axis, dtype, out, keepdims, ...\]) | Return the product of array elements over a given axis treating Not a Numbers (NaNs) as ones. |
| [`nansum`](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html#numpy.nansum "numpy.nansum")<br>(a\[, axis, dtype, out, keepdims, ...\]) | Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero. |
| [`cumulative_sum`](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_sum.html#numpy.cumulative_sum "numpy.cumulative_sum")<br>(x, /, \*\[, axis, dtype, out, ...\]) | Return the cumulative sum of the elements along a given axis. |
| [`cumulative_prod`](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_prod.html#numpy.cumulative_prod "numpy.cumulative_prod")<br>(x, /, \*\[, axis, dtype, out, ...\]) | Return the cumulative product of elements along a given axis. |
| [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")<br>(a\[, axis, dtype, out\]) | Return the cumulative product of elements along a given axis. |
| [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")<br>(a\[, axis, dtype, out\]) | Return the cumulative sum of the elements along a given axis. |
| [`nancumprod`](https://numpy.org/doc/stable/reference/generated/numpy.nancumprod.html#numpy.nancumprod "numpy.nancumprod")<br>(a\[, axis, dtype, out\]) | Return the cumulative product of array elements over a given axis treating Not a Numbers (NaNs) as one. |
| [`nancumsum`](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html#numpy.nancumsum "numpy.nancumsum")<br>(a\[, axis, dtype, out\]) | Return the cumulative sum of array elements over a given axis treating Not a Numbers (NaNs) as zero. |
| [`diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")<br>(a\[, n, axis, prepend, append\]) | Calculate the n-th discrete difference along the given axis. |
| [`ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "numpy.ediff1d")<br>(ary\[, to\_end, to\_begin\]) | The differences between consecutive elements of an array. |
| [`gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient "numpy.gradient")<br>(f, \*varargs\[, axis, edge\_order\]) | Return the gradient of an N-dimensional array. |
| [`cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "numpy.cross")<br>(a, b\[, axisa, axisb, axisc, axis\]) | Return the cross product of two (arrays of) vectors. |
| [`trapezoid`](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy.trapezoid "numpy.trapezoid")<br>(y\[, x, dx, axis\]) | Integrate along the given axis using the composite trapezoidal rule. |

Exponents and logarithms[#](https://numpy.org/doc/stable/reference/routines.math.html#exponents-and-logarithms "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`exp`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate the exponential of all elements in the input array. |
| [`expm1`](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate `exp(x) - 1` for all elements in the array. |
| [`exp2`](https://numpy.org/doc/stable/reference/generated/numpy.exp2.html#numpy.exp2 "numpy.exp2")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate _2\*\*p_ for all _p_ in the input array. |
| [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")<br>(x, /\[, out, where, casting, order, ...\]) | Natural logarithm, element-wise. |
| [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")<br>(x, /\[, out, where, casting, order, ...\]) | Return the base 10 logarithm of the input array, element-wise. |
| [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")<br>(x, /\[, out, where, casting, order, ...\]) | Base-2 logarithm of _x_. |
| [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")<br>(x, /\[, out, where, casting, order, ...\]) | Return the natural logarithm of one plus the input array, element-wise. |
| [`logaddexp`](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html#numpy.logaddexp "numpy.logaddexp")<br>(x1, x2, /\[, out, where, casting, ...\]) | Logarithm of the sum of exponentiations of the inputs. |
| [`logaddexp2`](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html#numpy.logaddexp2 "numpy.logaddexp2")<br>(x1, x2, /\[, out, where, casting, ...\]) | Logarithm of the sum of exponentiations of the inputs in base-2. |

Other special functions[#](https://numpy.org/doc/stable/reference/routines.math.html#other-special-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`i0`](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#numpy.i0 "numpy.i0")<br>(x) | Modified Bessel function of the first kind, order 0. |
| [`sinc`](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy.sinc "numpy.sinc")<br>(x) | Return the normalized sinc function. |

Floating point routines[#](https://numpy.org/doc/stable/reference/routines.math.html#floating-point-routines "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`signbit`](https://numpy.org/doc/stable/reference/generated/numpy.signbit.html#numpy.signbit "numpy.signbit")<br>(x, /\[, out, where, casting, order, ...\]) | Returns element-wise True where signbit is set (less than zero). |
| [`copysign`](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#numpy.copysign "numpy.copysign")<br>(x1, x2, /\[, out, where, casting, ...\]) | Change the sign of x1 to that of x2, element-wise. |
| [`frexp`](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#numpy.frexp "numpy.frexp")<br>(x\[, out1, out2\], / \[\[, out, where, ...\]) | Decompose the elements of x into mantissa and twos exponent. |\
| [`ldexp`](https://numpy.org/doc/stable/reference/generated/numpy.ldexp.html#numpy.ldexp "numpy.ldexp")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns x1 \* 2\*\*x2, element-wise. |\
| [`nextafter`](https://numpy.org/doc/stable/reference/generated/numpy.nextafter.html#numpy.nextafter "numpy.nextafter")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the next floating-point value after x1 towards x2, element-wise. |\
| [`spacing`](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy.spacing "numpy.spacing")<br>(x, /\[, out, where, casting, order, ...\]) | Return the distance between x and the nearest adjacent number. |\
\
Rational routines[#](https://numpy.org/doc/stable/reference/routines.math.html#rational-routines "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`lcm`](https://numpy.org/doc/stable/reference/generated/numpy.lcm.html#numpy.lcm "numpy.lcm")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the lowest common multiple of `\|x1\|` and `\|x2\|` |\
| [`gcd`](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html#numpy.gcd "numpy.gcd")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the greatest common divisor of `\|x1\|` and `\|x2\|` |\
\
Arithmetic operations[#](https://numpy.org/doc/stable/reference/routines.math.html#arithmetic-operations "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Add arguments element-wise. |\
| [`reciprocal`](https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html#numpy.reciprocal "numpy.reciprocal")<br>(x, /\[, out, where, casting, ...\]) | Return the reciprocal of the argument, element-wise. |\
| [`positive`](https://numpy.org/doc/stable/reference/generated/numpy.positive.html#numpy.positive "numpy.positive")<br>(x, /\[, out, where, casting, order, ...\]) | Numerical positive, element-wise. |\
| [`negative`](https://numpy.org/doc/stable/reference/generated/numpy.negative.html#numpy.negative "numpy.negative")<br>(x, /\[, out, where, casting, order, ...\]) | Numerical negation, element-wise. |\
| [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html#numpy.multiply "numpy.multiply")<br>(x1, x2, /\[, out, where, casting, ...\]) | Multiply arguments element-wise. |\
| [`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html#numpy.divide "numpy.divide")<br>(x1, x2, /\[, out, where, casting, ...\]) | Divide arguments element-wise. |\
| [`power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")<br>(x1, x2, /\[, out, where, casting, ...\]) | First array elements raised to powers from second array, element-wise. |\
| [`pow`](https://numpy.org/doc/stable/reference/generated/numpy.pow.html#numpy.pow "numpy.pow")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | First array elements raised to powers from second array, element-wise. |\
| [`subtract`](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html#numpy.subtract "numpy.subtract")<br>(x1, x2, /\[, out, where, casting, ...\]) | Subtract arguments, element-wise. |\
| [`true_divide`](https://numpy.org/doc/stable/reference/generated/numpy.true_divide.html#numpy.true_divide "numpy.true_divide")<br>(x1, x2, /\[, out, where, ...\]) | Divide arguments element-wise. |\
| [`floor_divide`](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html#numpy.floor_divide "numpy.floor_divide")<br>(x1, x2, /\[, out, where, ...\]) | Return the largest integer smaller or equal to the division of the inputs. |\
| [`float_power`](https://numpy.org/doc/stable/reference/generated/numpy.float_power.html#numpy.float_power "numpy.float_power")<br>(x1, x2, /\[, out, where, ...\]) | First array elements raised to powers from second array, element-wise. |\
| [`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns the element-wise remainder of division. |\
| [`mod`](https://numpy.org/doc/stable/reference/generated/numpy.mod.html#numpy.mod "numpy.mod")<br>(x1, x2, /\[, out, where, casting, order, ...\]) | Returns the element-wise remainder of division. |\
| [`modf`](https://numpy.org/doc/stable/reference/generated/numpy.modf.html#numpy.modf "numpy.modf")<br>(x\[, out1, out2\], / \[\[, out, where, ...\]) | Return the fractional and integral parts of an array, element-wise. |\
| [`remainder`](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy.remainder "numpy.remainder")<br>(x1, x2, /\[, out, where, casting, ...\]) | Returns the element-wise remainder of division. |\
| [`divmod`](https://numpy.org/doc/stable/reference/generated/numpy.divmod.html#numpy.divmod "numpy.divmod")<br>(x1, x2\[, out1, out2\], / \[\[, out, ...\]) | Return element-wise quotient and remainder simultaneously. |\
\
Handling complex numbers[#](https://numpy.org/doc/stable/reference/routines.math.html#handling-complex-numbers "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")<br>(z\[, deg\]) | Return the angle of the complex argument. |\
| [`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")<br>(val) | Return the real part of the complex argument. |\
| [`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")<br>(val) | Return the imaginary part of the complex argument. |\
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.conj.html#numpy.conj "numpy.conj")<br>(x, /\[, out, where, casting, order, ...\]) | Return the complex conjugate, element-wise. |\
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.conjugate.html#numpy.conjugate "numpy.conjugate")<br>(x, /\[, out, where, casting, ...\]) | Return the complex conjugate, element-wise. |\
\
Extrema finding[#](https://numpy.org/doc/stable/reference/routines.math.html#extrema-finding "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise maximum of array elements. |\
| [`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the maximum of an array or maximum along an axis. |\
| [`amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the maximum of an array or maximum along an axis. |\
| [`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise maximum of array elements. |\
| [`nanmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the maximum of an array or maximum along an axis, ignoring any NaNs. |\
| [`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise minimum of array elements. |\
| [`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the minimum of an array or minimum along an axis. |\
| [`amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the minimum of an array or minimum along an axis. |\
| [`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")<br>(x1, x2, /\[, out, where, casting, ...\]) | Element-wise minimum of array elements. |\
| [`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")<br>(a\[, axis, out, keepdims, initial, where\]) | Return minimum of an array or minimum along an axis, ignoring any NaNs. |\
\
Miscellaneous[#](https://numpy.org/doc/stable/reference/routines.math.html#miscellaneous "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")<br>(a, v\[, mode\]) | Returns the discrete, linear convolution of two one-dimensional sequences. |\
| [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")<br>(a\[, a\_min, a\_max, out, min, max\]) | Clip (limit) the values in an array. |\
| [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")<br>(x, /\[, out, where, casting, order, ...\]) | Return the non-negative square-root of an array, element-wise. |\
| [`cbrt`](https://numpy.org/doc/stable/reference/generated/numpy.cbrt.html#numpy.cbrt "numpy.cbrt")<br>(x, /\[, out, where, casting, order, ...\]) | Return the cube-root of an array, element-wise. |\
| [`square`](https://numpy.org/doc/stable/reference/generated/numpy.square.html#numpy.square "numpy.square")<br>(x, /\[, out, where, casting, order, ...\]) | Return the element-wise square of the input. |\
| [`absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "numpy.absolute")<br>(x, /\[, out, where, casting, order, ...\]) | Calculate the absolute value element-wise. |\
| [`fabs`](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#numpy.fabs "numpy.fabs")<br>(x, /\[, out, where, casting, order, ...\]) | Compute the absolute values element-wise. |\
| [`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")<br>(x, /\[, out, where, casting, order, ...\]) | Returns an element-wise indication of the sign of a number. |\
| [`heaviside`](https://numpy.org/doc/stable/reference/generated/numpy.heaviside.html#numpy.heaviside "numpy.heaviside")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the Heaviside step function. |\
| [`nan_to_num`](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#numpy.nan_to_num "numpy.nan_to_num")<br>(x\[, copy, nan, posinf, neginf\]) | Replace NaN with zero and infinity with large finite numbers (default behaviour) or with the numbers defined by the user using the [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")<br>, _posinf_ and/or _neginf_ keywords. |\
| [`real_if_close`](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html#numpy.real_if_close "numpy.real_if_close")<br>(a\[, tol\]) | If input is complex with all imaginary parts close to zero, return real parts. |\
| [`interp`](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")<br>(x, xp, fp\[, left, right, period\]) | One-dimensional linear interpolation for monotonically increasing sample points. |\
\
On this page