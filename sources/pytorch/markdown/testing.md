Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/testing.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/testing.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/testing.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/testing.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/testing.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/testing.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/testing.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/testing.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/testing.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/testing.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/testing.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/testing.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/testing.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/testing.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/testing.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/testing.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/testing.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/testing.html)
[v1.13](https://docs.pytorch.org/docs/1.13/testing.html)
[v1.12](https://docs.pytorch.org/docs/1.12/testing.html)
[v1.11](https://docs.pytorch.org/docs/1.11/testing.html)
[v1.10](https://docs.pytorch.org/docs/1.10/testing.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/testing.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/testing.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/testing.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/testing.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/testing.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/testing.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/testing.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/testing.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/testing.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/testing.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/testing.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/testing.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/testing.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/testing.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/testing.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/testing.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/testing.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/testing.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/testing.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/testing.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/testing.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/testing.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.testing[#](https://docs.pytorch.org/docs/2.15/testing.html#module-torch.testing "Link to this heading")

==============================================================================================================

Created On: May 07, 2021 | Last Updated On: Aug 26, 2026

torch.testing.assert\_close(_actual_, _expected_, _\*_, _allow\_subclasses\=True_, _rtol\=None_, _atol\=None_, _equal\_nan\=False_, _check\_device\=True_, _check\_dtype\=True_, _check\_layout\=True_, _check\_stride\=False_, _msg\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/testing/_comparison.py#L1415)
[#](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_close "Link to this definition")

Asserts that `actual` and `expected` are close.

If `actual` and `expected` are strided, non-quantized, real-valued, and finite, they are considered close if

∣actual−expected∣≤atol+rtol⋅∣expected∣\\lvert \\text{actual} - \\text{expected} \\rvert \\le \\texttt{atol} + \\texttt{rtol} \\cdot \\lvert \\text{expected} \\rvert∣actual−expected∣≤atol+rtol⋅∣expected∣

Non-finite values (`-inf` and `inf`) are only considered close if and only if they are equal. `NaN`’s are only considered equal to each other if `equal_nan` is `True`.

In addition, they are only considered close if they have the same

*   [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.device.html#torch.Tensor.device "torch.Tensor.device")
     (if `check_device` is `True`),
    
*   `dtype` (if `check_dtype` is `True`),
    
*   `layout` (if `check_layout` is `True`), and
    
*   stride (if `check_stride` is `True`).
    

If either `actual` or `expected` is a meta tensor, only the attribute checks will be performed.

If `actual` and `expected` are sparse (either having COO, CSR, CSC, BSR, or BSC layout), their strided members are checked individually. Indices, namely `indices` for COO, `crow_indices` and `col_indices` for CSR and BSR, or `ccol_indices` and `row_indices` for CSC and BSC layouts, respectively, are always checked for equality whereas the values are checked for closeness according to the definition above.

If `actual` and `expected` are quantized, they are considered close if they have the same [`qscheme()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.qscheme.html#torch.Tensor.qscheme "torch.Tensor.qscheme")
 and the result of [`dequantize()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.dequantize.html#torch.Tensor.dequantize "torch.Tensor.dequantize")
 is close according to the definition above.

`actual` and `expected` can be [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
’s or any tensor-or-scalar-likes from which [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
’s can be constructed with [`torch.as_tensor()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_tensor.html#torch.as_tensor "torch.as_tensor")
. Except for Python scalars the input types have to be directly related. In addition, `actual` and `expected` can be [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
’s or [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")
’s in which case they are considered close if their structure matches and all their elements are considered close according to the above definition.

Note

Python scalars are an exception to the type relation requirement, because their `type()`, i.e. [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
, and [`complex`](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")
, is equivalent to the `dtype` of a tensor-like. Thus, Python scalars of different types can be checked, but require `check_dtype=False`.

Parameters:

*   **actual** (_Any_) – Actual input.
    
*   **expected** (_Any_) – Expected input.
    
*   **allow\_subclasses** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` (default) and except for Python scalars, inputs of directly related types are allowed. Otherwise type equality is required.
    
*   **rtol** (_Optional__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Relative tolerance. If specified `atol` must also be specified. If omitted, default values based on the `dtype` are selected with the below table.
    
*   **atol** (_Optional__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Absolute tolerance. If specified `rtol` must also be specified. If omitted, default values based on the `dtype` are selected with the below table.
    
*   **equal\_nan** (_Union__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – If `True`, two `NaN` values will be considered equal.
    
*   **check\_device** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` (default), asserts that corresponding tensors are on the same [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.device.html#torch.Tensor.device "torch.Tensor.device")
    . If this check is disabled, tensors on different [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.device.html#torch.Tensor.device "torch.Tensor.device")
    ’s are moved to the CPU before being compared.
    
*   **check\_dtype** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` (default), asserts that corresponding tensors have the same `dtype`. If this check is disabled, tensors with different `dtype`’s are promoted to a common `dtype` (according to [`torch.promote_types()`](https://docs.pytorch.org/docs/2.15/generated/torch.promote_types.html#torch.promote_types "torch.promote_types")
    ) before being compared.
    
*   **check\_layout** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` (default), asserts that corresponding tensors have the same `layout`. If this check is disabled, tensors with different `layout`’s are converted to strided tensors before being compared.
    
*   **check\_stride** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and corresponding tensors are strided, asserts that they have the same stride.
    
*   **msg** (_Optional__\[__Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Callable__\[__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__\]__\]_) – Optional error message to use in case a failure occurs during the comparison. Can also passed as callable in which case it will be called with the generated message and should return the new message.
    

Raises:

*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – If no [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     can be constructed from an input.
    
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – If only `rtol` or `atol` is specified.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If corresponding inputs are not Python scalars and are not directly related.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If `allow_subclasses` is `False`, but corresponding inputs are not Python scalars and have different types.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If the inputs are [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
    ’s, but their length does not match.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If the inputs are [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")
    ’s, but their set of keys do not match.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If corresponding tensors do not have the same [`shape`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.shape.html#torch.Tensor.shape "torch.Tensor.shape")
    .
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If `check_layout` is `True`, but corresponding tensors do not have the same `layout`.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If only one of corresponding tensors is quantized.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If corresponding tensors are quantized, but have different [`qscheme()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.qscheme.html#torch.Tensor.qscheme "torch.Tensor.qscheme")
    ’s.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If `check_device` is `True`, but corresponding tensors are not on the same [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.device.html#torch.Tensor.device "torch.Tensor.device")
    .
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If `check_dtype` is `True`, but corresponding tensors do not have the same `dtype`.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If `check_stride` is `True`, but corresponding strided tensors do not have the same stride.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If the values of corresponding tensors are not close according to the definition above.
    

The following table displays the default `rtol` and `atol` for different `dtype`’s. In case of mismatching `dtype`’s, the maximum of both tolerances is used.

| `dtype` | `rtol` | `atol` |
| --- | --- | --- |
| `float16` | `1e-3` | `1e-5` |
| `bfloat16` | `1.6e-2` | `1e-5` |
| `float32` | `1.3e-6` | `1e-5` |
| `float64` | `1e-7` | `1e-7` |
| `complex32` | `1e-3` | `1e-5` |
| `complex64` | `1.3e-6` | `1e-5` |
| `complex128` | `1e-7` | `1e-7` |
| `quint8` | `1.3e-6` | `1e-5` |
| `quint2x4` | `1.3e-6` | `1e-5` |
| `quint4x2` | `1.3e-6` | `1e-5` |
| `qint8` | `1.3e-6` | `1e-5` |
| `qint32` | `1.3e-6` | `1e-5` |
| other | `0.0` | `0.0` |

Note

[`assert_close()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_close "torch.testing.assert_close")
 is highly configurable with strict default settings. Users are encouraged to [`partial()`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.15)")
 it to fit their use case. For example, if an equality check is needed, one might define an `assert_equal` that uses zero tolerances for every `dtype` by default:

\>>> import functools
\>>> assert\_equal \= functools.partial(torch.testing.assert\_close, rtol\=0, atol\=0)
\>>> assert\_equal(1e-9, 1e-10)
Traceback (most recent call last):
...
AssertionError: Scalars are not equal!

Expected 1e-10 but got 1e-09.
Absolute difference: 9.000000000000001e-10
Relative difference: 9.0

Copy to clipboard

Examples

\>>> \# tensor to tensor comparison
\>>> expected \= torch.tensor(\[1e0, 1e-1, 1e-2\])
\>>> actual \= torch.acos(torch.cos(expected))
\>>> torch.testing.assert\_close(actual, expected)

Copy to clipboard

\>>> \# scalar to scalar comparison
\>>> import math
\>>> expected \= math.sqrt(2.0)
\>>> actual \= 2.0 / math.sqrt(2.0)
\>>> torch.testing.assert\_close(actual, expected)

Copy to clipboard

\>>> \# numpy array to numpy array comparison
\>>> import numpy as np
\>>> expected \= np.array(\[1e0, 1e-1, 1e-2\])
\>>> actual \= np.arccos(np.cos(expected))
\>>> torch.testing.assert\_close(actual, expected)

Copy to clipboard

\>>> \# sequence to sequence comparison
\>>> import numpy as np
\>>> \# The types of the sequences do not have to match. They only have to have the same
\>>> \# length and their elements have to match.
\>>> expected \= \[torch.tensor(\[1.0\]), 2.0, np.array(3.0)\]
\>>> actual \= tuple(expected)
\>>> torch.testing.assert\_close(actual, expected)

Copy to clipboard

\>>> \# mapping to mapping comparison
\>>> from collections import OrderedDict
\>>> import numpy as np
\>>> foo \= torch.tensor(1.0)
\>>> bar \= 2.0
\>>> baz \= np.array(3.0)
\>>> \# The types and a possible ordering of mappings do not have to match. They only
\>>> \# have to have the same set of keys and their elements have to match.
\>>> expected \= OrderedDict(\[("foo", foo), ("bar", bar), ("baz", baz)\])
\>>> actual \= {"baz": baz, "bar": bar, "foo": foo}
\>>> torch.testing.assert\_close(actual, expected)

Copy to clipboard

\>>> expected \= torch.tensor(\[1.0, 2.0, 3.0\])
\>>> actual \= expected.clone()
\>>> \# By default, directly related instances can be compared
\>>> torch.testing.assert\_close(torch.nn.Parameter(actual), expected)
\>>> \# This check can be made more strict with allow\_subclasses=False
\>>> torch.testing.assert\_close(
...     torch.nn.Parameter(actual), expected, allow\_subclasses\=False
... )
Traceback (most recent call last):
...
TypeError: No comparison pair was able to handle inputs of type
<class 'torch.nn.parameter.Parameter'> and <class 'torch.Tensor'>.
\>>> \# If the inputs are not directly related, they are never considered close
\>>> torch.testing.assert\_close(actual.numpy(), expected)
Traceback (most recent call last):
...
TypeError: No comparison pair was able to handle inputs of type <class 'numpy.ndarray'>
and <class 'torch.Tensor'>.
\>>> \# Exceptions to these rules are Python scalars. They can be checked regardless of
\>>> \# their type if check\_dtype=False.
\>>> torch.testing.assert\_close(1.0, 1, check\_dtype\=False)

Copy to clipboard

\>>> \# NaN != NaN by default.
\>>> expected \= torch.tensor(float("Nan"))
\>>> actual \= expected.clone()
\>>> torch.testing.assert\_close(actual, expected)
Traceback (most recent call last):
...
AssertionError: Scalars are not close!

Expected nan but got nan.
Absolute difference: nan (up to 1e-05 allowed)
Relative difference: nan (up to 1.3e-06 allowed)
\>>> torch.testing.assert\_close(actual, expected, equal\_nan\=True)

Copy to clipboard

\>>> expected \= torch.tensor(\[1.0, 2.0, 3.0\])
\>>> actual \= torch.tensor(\[1.0, 4.0, 5.0\])
\>>> \# The default error message can be overwritten.
\>>> torch.testing.assert\_close(
...     actual, expected, msg\="Argh, the tensors are not close!"
... )
Traceback (most recent call last):
...
AssertionError: Argh, the tensors are not close!
\>>> \# If msg is a callable, it can be used to augment the generated message with
\>>> \# extra information
\>>> torch.testing.assert\_close(
...     actual, expected, msg\=lambda msg: f"Header\\n\\n{msg}\\n\\nFooter"
... )
Traceback (most recent call last):
...
AssertionError: Header

Tensor-likes are not close!

Mismatched elements: 2 / 3 (66.7%)
Greatest absolute difference: 2.0 at index (1,) (up to 1e-05 allowed)
Greatest relative difference: 1.0 at index (1,) (up to 1.3e-06 allowed)

Footer

Copy to clipboard

torch.testing.make\_tensor(_\*shape_, _dtype_, _device_, _low\=None_, _high\=None_, _requires\_grad\=False_, _noncontiguous\=False_, _exclude\_zero\=False_, _memory\_format\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/testing/_creation.py#L45)
[#](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.make_tensor "Link to this definition")

Creates a tensor with the given `shape`, `device`, and `dtype`, and filled with values uniformly drawn from `[low, high)`.\
\
If `low` or `high` are specified and are outside the range of the `dtype`’s representable finite values then they are clamped to the lowest or highest representable finite value, respectively. If `None`, then the following table describes the default values for `low` and `high`, which depend on `dtype`.\
\
| `dtype` | `low` | `high` |\
| --- | --- | --- |\
| boolean type | `0` | `2` |\
| unsigned integral type | `0` | `10` |\
| signed integral types | `-9` | `10` |\
| floating types | `-9` | `9` |\
| complex types | `-9` | `9` |\
\
Parameters:\
\
*   **shape** (_Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _...__\]_) – Single integer or a sequence of integers defining the shape of the output tensor.\
    \
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
    ) – The data type of the returned tensor.\
    \
*   **device** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
    _\]_) – The device of the returned tensor.\
    \
*   **low** (_Optional__\[__Number__\]_) – Sets the lower limit (inclusive) of the given range. If a number is provided it is clamped to the least representable finite value of the given dtype. When `None` (default), this value is determined based on the `dtype` (see the table above). Default: `None`.\
    \
*   **high** (_Optional__\[__Number__\]_) –\
    \
    Sets the upper limit (exclusive) of the given range. If a number is provided it is clamped to the greatest representable finite value of the given dtype. When `None` (default) this value is determined based on the `dtype` (see the table above). Default: `None`.\
    \
    Deprecated since version 2.1: Passing `low==high` to [`make_tensor()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.make_tensor "torch.testing.make_tensor")\
     for floating or complex types is deprecated since 2.1 and will be removed in 2.3. Use [`torch.full()`](https://docs.pytorch.org/docs/2.15/generated/torch.full.html#torch.full "torch.full")\
     instead.\
    \
*   **requires\_grad** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – If autograd should record operations on the returned tensor. Default: `False`.\
    \
*   **noncontiguous** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – If True, the returned tensor will be noncontiguous. This argument is ignored if the constructed tensor has fewer than two elements. Mutually exclusive with `memory_format`.\
    \
*   **exclude\_zero** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – If `True` then zeros are replaced with the dtype’s small positive value depending on the `dtype`. For bool and integer types zero is replaced with one. For floating point types it is replaced with the dtype’s smallest positive normal number (the “tiny” value of the `dtype`’s `finfo()` object), and for complex types it is replaced with a complex number whose real and imaginary parts are both the smallest positive normal number representable by the complex type. Default `False`.\
    \
*   **memory\_format** (_Optional__\[_[_torch.memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
    _\]_) – The memory format of the returned tensor. Mutually exclusive with `noncontiguous`.\
    \
\
Raises:\
\
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")\
     – If `requires_grad=True` is passed for integral dtype\
    \
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")\
     – If `low >= high`.\
    \
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")\
     – If either `low` or `high` is `nan`.\
    \
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")\
     – If both `noncontiguous` and `memory_format` are passed.\
    \
*   [**TypeError**](https://docs.python.org/3/builtins/exceptions.html#TypeError "(in Python v3.15)")\
     – If `dtype` isn’t supported by this function.\
    \
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
Examples\
\
\>>> from torch.testing import make\_tensor\
\>>> \# Creates a float tensor with values in \[-1, 1)\
\>>> make\_tensor((3,), device\="cpu", dtype\=torch.float32, low\=-1, high\=1)\
tensor(\[ 0.1205, 0.2282, -0.6380\])\
\>>> \# Creates a bool tensor on CUDA\
\>>> make\_tensor((2, 2), device\="cuda", dtype\=torch.bool)\
tensor(\[\[False, False\],\
        \[False, True\]\], device='cuda:0')\
\
Copy to clipboard\
\
torch.testing.assert\_allclose(_actual_, _expected_, _rtol\=None_, _atol\=None_, _equal\_nan\=True_, _msg\=''_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/testing/_comparison.py#L1692)\
[#](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_allclose "Link to this definition")\
\
Warning\
\
[`torch.testing.assert_allclose()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_allclose "torch.testing.assert_allclose")\
 is deprecated since `1.12` and will be removed in a future release. Please use [`torch.testing.assert_close()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_close "torch.testing.assert_close")\
 instead. You can find detailed upgrade instructions [here](https://github.com/pytorch/pytorch/issues/61844)\
.\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/testing.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/testing.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |