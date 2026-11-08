[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.finfo[#](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy-finfo "Link to this heading")

=====================================================================================================================

_class_ numpy.finfo(_dtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/getlimits.py#L57-L342)
[#](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "Link to this definition")

Machine limits for floating point types.

Parameters:

**dtype**float, dtype, or instance

Kind of floating point or complex floating point data-type about which to get information.

Attributes:

**bits**int

The number of bits occupied by the type.

**dtype**dtype

Returns the dtype for which [`finfo`](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo")
 returns information. For complex input, the returned dtype is the associated `float*` dtype for its real and complex components.

**eps**float

The difference between 1.0 and the next smallest representable float larger than 1.0. For example, for 64-bit binary floats in the IEEE-754 standard, `eps = 2**-52`, approximately 2.22e-16.

**epsneg**float

The difference between 1.0 and the next smallest representable float less than 1.0. For example, for 64-bit binary floats in the IEEE-754 standard, `epsneg = 2**-53`, approximately 1.11e-16.

**iexp**int

The number of bits in the exponent portion of the floating point representation.

**machep**int

The exponent that yields _eps_.

**max**floating point number of the appropriate type

The largest representable number.

**maxexp**int

The smallest positive power of the base (2) that causes overflow. Corresponds to the C standard MAX\_EXP.

**min**floating point number of the appropriate type

The smallest representable number, typically `-max`.

**minexp**int

The most negative power of the base (2) consistent with there being no leading 0’s in the mantissa. Corresponds to the C standard MIN\_EXP - 1.

**negep**int

The exponent that yields [`epsneg`](https://numpy.org/doc/stable/reference/generated/numpy.finfo.epsneg.html#numpy.finfo.epsneg "numpy.finfo.epsneg")
.

**nexp**int

The number of bits in the exponent including its sign and bias.

**nmant**int

The number of explicit bits in the mantissa (excluding the implicit leading bit for normalized numbers).

**precision**int

The approximate number of decimal digits to which this kind of float is precise.

**resolution**floating point number of the appropriate type

The approximate decimal resolution of this type, i.e., `10**-precision`.

**tiny**float

An alias for _smallest\_normal_, kept for backwards compatibility.

**smallest\_normal**float

The smallest positive floating point number with 1 as leading bit in the mantissa following IEEE-754 (see Notes).

**smallest\_subnormal**float

The smallest positive floating point number with 0 as leading bit in the mantissa following IEEE-754.

See also

[`iinfo`](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy.iinfo "numpy.iinfo")

The equivalent for integer data types.

[`spacing`](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy.spacing "numpy.spacing")

The distance between a value and the nearest adjacent number

[`nextafter`](https://numpy.org/doc/stable/reference/generated/numpy.nextafter.html#numpy.nextafter "numpy.nextafter")

The next floating point value after x1 towards x2

Notes

For developers of NumPy: do not instantiate this at the module level. The initial calculation of these parameters is expensive and negatively impacts import times. These objects are cached, so calling `finfo()` repeatedly inside your functions is not a problem.

Note that `smallest_normal` is not actually the smallest positive representable value in a NumPy floating point type. As in the IEEE-754 standard [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#r2ee89c7f792a-1)
, NumPy floating point types make use of subnormal numbers to fill the gap between 0 and `smallest_normal`. However, subnormal numbers may have significantly reduced precision [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#r2ee89c7f792a-2)
.

For `longdouble`, the representation varies across platforms. On most platforms it is IEEE 754 binary128 (quad precision) or binary64-extended (80-bit extended precision). On PowerPC systems, it may use the IBM double-double format (a pair of float64 values), which has special characteristics for precision and range.

This function can also be used for complex data types as well. If used, the output will be the same as the corresponding real float type (e.g. numpy.finfo(numpy.csingle) is the same as numpy.finfo(numpy.single)). However, the output is true for the real and imaginary components.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#id1)\
\]

IEEE Standard for Floating-Point Arithmetic, IEEE Std 754-2008, pp.1-70, 2008, [https://doi.org/10.1109/IEEESTD.2008.4610935](https://doi.org/10.1109/IEEESTD.2008.4610935)

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#id2)\
\]

Wikipedia, “Denormal Numbers”, [https://en.wikipedia.org/wiki/Denormal\_number](https://en.wikipedia.org/wiki/Denormal_number)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.finfo(np.float64).dtype
dtype('float64')
\>>> np.finfo(np.complex64).dtype
dtype('float32')

Copy to clipboard

Go BackOpen In Tab

On this page