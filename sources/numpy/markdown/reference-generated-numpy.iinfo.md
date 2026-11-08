[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.iinfo.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.iinfo.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.iinfo.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.iinfo.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.iinfo.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.iinfo.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.iinfo.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.iinfo.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.iinfo.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.iinfo.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.iinfo.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.iinfo.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.iinfo.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.iinfo.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.iinfo.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.iinfo.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.iinfo.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.iinfo.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.iinfo.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.iinfo.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.iinfo[#](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy-iinfo "Link to this heading")

=====================================================================================================================

_class_ numpy.iinfo(_type_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/getlimits.py#L345-L453)
[#](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy.iinfo "Link to this definition")

Machine limits for integer types.

Parameters:

**int\_type**integer type, dtype, or instance

The kind of integer data type to get information about.

Attributes:

**bits**int

The number of bits occupied by the type.

**dtype**dtype

Returns the dtype for which [`iinfo`](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy.iinfo "numpy.iinfo")
 returns information.

[`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
int

Minimum value of given dtype.

[`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
int

Maximum value of given dtype.

See also

[`finfo`](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo")

The equivalent for floating point data types.

Examples

Try it in your browser!

With types:

\>>> import numpy as np
\>>> ii16 \= np.iinfo(np.int16)
\>>> ii16.min
\-32768
\>>> ii16.max
32767
\>>> ii32 \= np.iinfo(np.int32)
\>>> ii32.min
\-2147483648
\>>> ii32.max
2147483647

Copy to clipboard

With instances:

\>>> ii32 \= np.iinfo(np.int32(10))
\>>> ii32.min
\-2147483648
\>>> ii32.max
2147483647

Copy to clipboard

Go BackOpen In Tab

On this page