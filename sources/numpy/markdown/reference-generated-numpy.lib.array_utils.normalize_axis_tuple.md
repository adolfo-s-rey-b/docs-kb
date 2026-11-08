[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.array\_utils.normalize\_axis\_tuple[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html#numpy-lib-array-utils-normalize-axis-tuple "Link to this heading")

=====================================================================================================================================================================================================================

lib.array\_utils.normalize\_axis\_tuple(_axis_, _ndim_, _argname\=None_, _allow\_duplicate\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1426-L1481)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_tuple.html#numpy.lib.array_utils.normalize_axis_tuple "Link to this definition")

Normalizes an axis argument into a tuple of non-negative integer axes.

This handles shorthands such as `1` and converts them to `(1,)`, as well as performing the handling of negative indices covered by [`normalize_axis_index`](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html#numpy.lib.array_utils.normalize_axis_index "numpy.lib.array_utils.normalize_axis_index")
.

By default, this forbids axes from being specified multiple times.

Used internally by multi-axis-checking logic.

Parameters:

**axis**int, iterable of int

The un-normalized index or indices of the axis.

**ndim**int

The number of dimensions of the array that _axis_ should be normalized against.

**argname**str, optional

A prefix to put before the error message, typically the name of the argument.

**allow\_duplicate**bool, optional

If False, the default, disallow an axis from being specified twice.

Returns:

**normalized\_axes**tuple of int

The normalized axis index, such that _0 <= normalized\_axis < ndim_

Raises:

AxisError

If any axis provided is out of range

ValueError

If an axis is repeated

See also

[`normalize_axis_index`](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html#numpy.lib.array_utils.normalize_axis_index "numpy.lib.array_utils.normalize_axis_index")

normalizing a single scalar axis

On this page