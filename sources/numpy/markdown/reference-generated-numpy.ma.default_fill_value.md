[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.default_fill_value.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.default_fill_value.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.default_fill_value.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.default_fill_value.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.default_fill_value.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.default_fill_value.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.default_fill_value.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.default_fill_value.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.default_fill_value.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.default_fill_value.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.default_fill_value.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.default_fill_value.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.default_fill_value.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.default_fill_value.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.default_fill_value.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.default_fill_value.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.default_fill_value.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.default_fill_value.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.default_fill_value.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.default_fill_value.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.default_fill_value.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.default_fill_value.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.default\_fill\_value[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.default_fill_value.html#numpy-ma-default-fill-value "Link to this heading")

=======================================================================================================================================================================

ma.default\_fill\_value(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L260-L314)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.default_fill_value.html#numpy.ma.default_fill_value "Link to this definition")

Return the default fill value for the argument object.

The default filling value depends on the datatype of the input array or the type of the input scalar:

> | datatype | default |
> | --- | --- |
> | bool | True |
> | int | 999999 |
> | float | 1.e20 |
> | complex | 1.e20+0j |
> | object | ‘?’ |
> | string | ‘N/A’ |
> | StringDType | ‘N/A’ |

For structured types, a structured scalar is returned, with each field the default fill value for its type.

For subarray types, the fill value is an array of the same size containing the default scalar fill value.

Parameters:

**obj**ndarray, dtype or scalar

The array data-type or scalar for which the default fill value is returned.

Returns:

**fill\_value**scalar

The default fill value.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.ma.default\_fill\_value(1)
999999
\>>> np.ma.default\_fill\_value(np.array(\[1.1, 2., np.pi\]))
1e+20
\>>> np.ma.default\_fill\_value(np.dtype(complex))
(1e+20+0j)

Copy to clipboard

Go BackOpen In Tab

On this page