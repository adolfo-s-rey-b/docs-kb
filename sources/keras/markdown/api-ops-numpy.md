None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [The Operation class](https://keras.io/api/ops/operation/)
 [NumPy ops](https://keras.io/api/ops/numpy/)
 [NN ops](https://keras.io/api/ops/nn/)
 [Linear algebra ops](https://keras.io/api/ops/linalg/)
 [Core ops](https://keras.io/api/ops/core/)
 [Image ops](https://keras.io/api/ops/image/)
 [FFT ops](https://keras.io/api/ops/fft/)
 [Einops ops](https://keras.io/api/ops/einops/)
 [Math ops](https://keras.io/api/ops/math/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Ops API](https://keras.io/api/ops/)
 / NumPy ops

NumPy ops
=========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L184)

### `abs` function

Copied!

`keras.ops.abs(x)`

Shorthand for [`keras.ops.absolute`](https://keras.io/api/ops/numpy#absolute-function)
.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L157)

### `absolute` function

Copied!

`keras.ops.absolute(x)`

Compute the absolute value element-wise.

[`keras.ops.abs`](https://keras.io/api/ops/numpy#abs-function)
 is a shorthand for this function.

**Arguments**

*   **x**: Input tensor.

**Returns**

An array containing the absolute value of each element in `x`.

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([-1.2, 1.2]) >>> keras.ops.absolute(x) array([1.2, 1.2], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L258)

### `add` function

Copied!

`keras.ops.add(x1, x2)`

Add arguments element-wise.

**Arguments**

*   **x1**: First input tensor.
*   **x2**: Second input tensor.

**Returns**

The tensor containing the element-wise sum of `x1` and `x2`.

**Examples**

Copied!

`>>> x1 = keras.ops.convert_to_tensor([1, 4]) >>> x2 = keras.ops.convert_to_tensor([5, 6]) >>> keras.ops.add(x1, x2) array([6, 10], dtype=int32)`

[`keras.ops.add`](https://keras.io/api/ops/numpy#add-function)
 also broadcasts shapes:

Copied!

`>>> x1 = keras.ops.convert_to_tensor( ...     [[5, 4], ...      [5, 6]] ... ) >>> x2 = keras.ops.convert_to_tensor([5, 6]) >>> keras.ops.add(x1, x2) array([[10 10]        [10 12]], shape=(2, 2), dtype=int32)`

**Guides and examples using `add`**

*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L317)

### `all` function

Copied!

`keras.ops.all(x, axis=None, keepdims=False)`

Test whether all array elements along a given axis evaluate to `True`.

**Arguments**

*   **x**: Input tensor.
*   **axis**: An integer or tuple of integers that represent the axis along which a logical AND reduction is performed. The default (`axis=None`) is to perform a logical AND over all the dimensions of the input array. `axis` may be negative, in which case it counts for the last to the first axis.
*   **keepdims**: If `True`, axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array. Defaults to `False`.

**Returns**

The tensor containing the logical AND reduction over the `axis`.

**Examples**

Copied!

`>>> x = keras.ops.convert_to_tensor([True, False]) >>> keras.ops.all(x) array(False, shape=(), dtype=bool)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[True, False], [True, True]]) >>> keras.ops.all(x, axis=0) array([ True False], shape=(2,), dtype=bool)`

`keepdims=True` outputs a tensor with dimensions reduced to one.

Copied!

`>>> x = keras.ops.convert_to_tensor([[True, False], [True, True]]) >>> keras.ops.all(x, keepdims=True) array([[False]], shape=(1, 1), dtype=bool)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L374)

### `allclose` function

Copied!

`keras.ops.allclose(x1, x2, rtol=1e-05, atol=1e-08, equal_nan=False)`

Returns True if two arrays are element-wise equal within a tolerance.

The tolerance values are positive, typically very small numbers. The relative difference (`rtol * abs(b)`) and the absolute difference `atol` are added together to compare against the absolute difference between `a` and `b`.

**Arguments**

*   **x1**: First input tensor.
*   **x2**: Second input tensor.
*   **rtol**: The relative tolerance parameter (see Notes).
*   **atol**: The absolute tolerance parameter (see Notes).
*   **equal\_nan**: Whether to compare NaN's as equal. If True, NaN's in `a` will be considered equal to NaN's in `b` in the output array.

**Returns**

True if the two arrays are equal within the given tolerance; False otherwise.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L525)

### `amax` function

Copied!

`keras.ops.amax(x, axis=None, keepdims=False)`

Returns the maximum of an array or maximum value along an axis.

**Arguments**

*   **x**: Input tensor.
*   **axis**: Axis along which to compute the maximum. By default (`axis=None`), find the maximum value in all the dimensions of the input array.
*   **keepdims**: If `True`, axes which are reduced are left in the result as dimensions that are broadcast to the size of the original input tensor. Defaults to `False`.

**Returns**

An array with the maximum value. If `axis=None`, the result is a scalar value representing the maximum element in the entire array. If `axis` is given, the result is an array with the maximum values along the specified axis.

**Examples**

Copied!

`>>> x = keras.ops.convert_to_tensor([[1, 3, 5], [2, 3, 6]]) >>> keras.ops.amax(x) array(6, dtype=int32)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[1, 6, 8], [1, 5, 2]]) >>> keras.ops.amax(x, axis=0) array([1, 6, 8], dtype=int32)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[1, 6, 8], [1, 5, 2]]) >>> keras.ops.amax(x, axis=1, keepdims=True) array([[8], [5]], dtype=int32)`

**Guides and examples using `amax`**

*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L580)

### `amin` function

Copied!

`keras.ops.amin(x, axis=None, keepdims=False)`

Returns the minimum of an array or minimum value along an axis.

**Arguments**

*   **x**: Input tensor.
*   **axis**: Axis along which to compute the minimum. By default (`axis=None`), find the minimum value in all the dimensions of the input array.
*   **keepdims**: If `True`, axes which are reduced are left in the result as dimensions that are broadcast to the size of the original input tensor. Defaults to `False`.

**Returns**

An array with the minimum value. If `axis=None`, the result is a scalar value representing the minimum element in the entire array. If `axis` is given, the result is an array with the minimum values along the specified axis.

**Examples**

Copied!

`>>> x = keras.ops.convert_to_tensor([1, 3, 5, 2, 3, 6]) >>> keras.ops.amin(x) array(1, dtype=int32)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[1, 6, 8], [7, 5, 3]]) >>> keras.ops.amin(x, axis=0) array([1,5,3], dtype=int32)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[1, 6, 8], [7, 5, 3]]) >>> keras.ops.amin(x, axis=1, keepdims=True) array([[1],[3]], dtype=int32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L417)

### `angle` function

Copied!

`keras.ops.angle(x)`

Element-wise angle of a complex tensor.

**Arguments**

*   **x**: Input tensor. Can be real or complex.

**Returns**

Output tensor of same shape as x. containing the angle of each element (in radians).

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([[1 + 3j, 2 - 5j], [4 - 3j, 3 + 2j]]) >>> keras.ops.angle(x) array([[ 1.2490457, -1.19029  ],    [-0.6435011,  0.5880026]], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L466)

### `any` function

Copied!

`keras.ops.any(x, axis=None, keepdims=False)`

Test whether any array element along a given axis evaluates to `True`.

**Arguments**

*   **x**: Input tensor.
*   **axis**: An integer or tuple of integers that represent the axis along which a logical OR reduction is performed. The default (`axis=None`) is to perform a logical OR over all the dimensions of the input array. `axis` may be negative, in which case it counts for the last to the first axis.
*   **keepdims**: If `True`, axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array. Defaults to `False`.

**Returns**

The tensor containing the logical OR reduction over the `axis`.

**Examples**

Copied!

`>>> x = keras.ops.convert_to_tensor([True, False]) >>> keras.ops.any(x) array(True, shape=(), dtype=bool)`

Copied!

`>>> x = keras.ops.convert_to_tensor([[True, False], [True, True]]) >>> keras.ops.any(x, axis=0) array([ True  True], shape=(2,), dtype=bool)`

`keepdims=True` outputs a tensor with dimensions reduced to one.

Copied!

`>>> x = keras.ops.convert_to_tensor([[True, False], [True, True]]) >>> keras.ops.all(x, keepdims=True) array([[False]], shape=(1, 1), dtype=bool)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L653)

### `append` function

Copied!

`keras.ops.append(x1, x2, axis=None)`

Append tensor `x2` to the end of tensor `x1`.

**Arguments**

*   **x1**: First input tensor.
*   **x2**: Second input tensor.
*   **axis**: Axis along which tensor `x2` is appended to tensor `x1`. If `None`, both tensors are flattened before use.

**Returns**

A tensor with the values of `x2` appended to `x1`.

**Examples**

Copied!

`>>> x1 = keras.ops.convert_to_tensor([1, 2, 3]) >>> x2 = keras.ops.convert_to_tensor([[4, 5, 6], [7, 8, 9]]) >>> keras.ops.append(x1, x2) array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int32)`

When `axis` is specified, `x1` and `x2` must have compatible shapes.

Copied!

`>>> x1 = keras.ops.convert_to_tensor([[1, 2, 3], [4, 5, 6]]) >>> x2 = keras.ops.convert_to_tensor([[7, 8, 9]]) >>> keras.ops.append(x1, x2, axis=0) array([[1, 2, 3],         [4, 5, 6],         [7, 8, 9]], dtype=int32) >>> x3 = keras.ops.convert_to_tensor([7, 8, 9]) >>> keras.ops.append(x1, x3, axis=0) Traceback (most recent call last):     ... TypeError: Cannot concatenate arrays with different numbers of dimensions: got (2, 3), (3,).`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L720)

### `arange` function

Copied!

`keras.ops.arange(start, stop=None, step=None, dtype=None)`

Return evenly spaced values within a given interval.

`arange` can be called with a varying number of positional arguments: \* `arange(stop)`: Values are generated within the half-open interval `[0, stop)` (in other words, the interval including start but excluding stop). \* `arange(start, stop)`: Values are generated within the half-open interval `[start, stop)`. \* `arange(start, stop, step)`: Values are generated within the half-open interval `[start, stop)`, with spacing between values given by step.\
\
**Arguments**\
\
*   **start**: Integer or real, representing the start of the interval. The interval includes this value.\
*   **stop**: Integer or real, representing the end of the interval. The interval does not include this value, except in some cases where `step` is not an integer and floating point round-off affects the length of `out`. Defaults to `None`.\
*   **step**: Integer or real, represent the spacing between values. For any output `out`, this is the distance between two adjacent values, `out[i+1] - out[i]`. The default step size is 1. If `step` is specified as a position argument, `start` must also be given.\
*   **dtype**: The type of the output array. If `dtype` is not given, infer the data type from the other input arguments.\
\
**Returns**\
\
Tensor of evenly spaced values. For floating point arguments, the length of the result is `ceil((stop - start)/step)`. Because of floating point overflow, this rule may result in the last element of out being greater than stop.\
\
**Examples**\
\
Copied!\
\
`>>> keras.ops.arange(3) array([0, 1, 2], dtype=int32)`\
\
Copied!\
\
`>>> keras.ops.arange(3.0) array([0., 1., 2.], dtype=float32)`\
\
Copied!\
\
`>>> keras.ops.arange(3, 7) array([3, 4, 5, 6], dtype=int32)`\
\
Copied!\
\
`>>> keras.ops.arange(3, 7, 2) array([3, 5], dtype=int32)`\
\
**Guides and examples using `arange`**\
\
*   [Metric learning for image similarity search](https://keras.io/examples/vision/metric_learning/)\
    \
*   [Video Classification with Transformers](https://keras.io/examples/vision/video_transformers/)\
    \
*   [Deep Recommenders](https://keras.io/keras_rs/examples/deep_recommender/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L785)\
\
### `arccos` function\
\
Copied!\
\
`keras.ops.arccos(x)`\
\
Trigonometric inverse cosine, element-wise.\
\
The inverse of `cos` so that, if `y = cos(x)`, then `x = arccos(y)`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Tensor of the angle of the ray intersecting the unit circle at the given x-coordinate in radians `[0, pi]`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([1, -1]) >>> keras.ops.arccos(x) array([0.0, 3.1415927], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L821)\
\
### `arccosh` function\
\
Copied!\
\
`keras.ops.arccosh(x)`\
\
Inverse hyperbolic cosine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as x.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([10, 100]) >>> keras.ops.arccosh(x) array([2.993223, 5.298292], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L855)\
\
### `arcsin` function\
\
Copied!\
\
`keras.ops.arcsin(x)`\
\
Inverse sine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Tensor of the inverse sine of each element in `x`, in radians and in the closed interval `[-pi/2, pi/2]`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([1, -1, 0]) >>> keras.ops.arcsin(x) array([ 1.5707964, -1.5707964,  0.], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L890)\
\
### `arcsinh` function\
\
Copied!\
\
`keras.ops.arcsinh(x)`\
\
Inverse hyperbolic sine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([1, -1, 0]) >>> keras.ops.arcsinh(x) array([0.88137364, -0.88137364, 0.0], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L924)\
\
### `arctan` function\
\
Copied!\
\
`keras.ops.arctan(x)`\
\
Trigonometric inverse tangent, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Tensor of the inverse tangent of each element in `x`, in the interval `[-pi/2, pi/2]`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([0, 1]) >>> keras.ops.arctan(x) array([0., 0.7853982], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L963)\
\
### `arctan2` function\
\
Copied!\
\
`keras.ops.arctan2(x1, x2)`\
\
Element-wise arc tangent of `x1/x2` choosing the quadrant correctly.\
\
The quadrant (i.e., branch) is chosen so that `arctan2(x1, x2)` is the signed angle in radians between the ray ending at the origin and passing through the point `(1, 0)`, and the ray ending at the origin and passing through the point `(x2, x1)`. (Note the role reversal: the "y-coordinate" is the first function parameter, the "x-coordinate" is the second.) By IEEE convention, this function is defined for `x2 = +/-0` and for either or both of `x1` and `x2` `= +/-inf`.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Tensor of angles in radians, in the range `[-pi, pi]`.\
\
**Examples**\
\
Consider four points in different quadrants:\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([-1, +1, +1, -1]) >>> y = keras.ops.convert_to_tensor([-1, -1, +1, +1]) >>> keras.ops.arctan2(y, x) * 180 / numpy.pi array([-135., -45., 45., 135.], dtype=float32)`\
\
Note the order of the parameters. `arctan2` is defined also when x2=0 and at several other points, obtaining values in the range `[-pi, pi]`:\
\
Copied!\
\
`>>> keras.ops.arctan2( ...     keras.ops.array([1., -1.]), ...     keras.ops.array([0., 0.]), ... ) array([ 1.5707964, -1.5707964], dtype=float32) >>> keras.ops.arctan2( ...     keras.ops.array([0., 0., numpy.inf]), ...     keras.ops.array([+0., -0., numpy.inf]), ... ) array([0., 3.1415925, 0.7853982], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1021)\
\
### `arctanh` function\
\
Copied!\
\
`keras.ops.arctanh(x)`\
\
Inverse hyperbolic tangent, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([0, -0.5]) >>> keras.ops.arctanh(x) array([ 0.        , -0.54930615], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1057)\
\
### `argmax` function\
\
Copied!\
\
`keras.ops.argmax(x, axis=None, keepdims=False)`\
\
Returns the indices of the maximum values along an axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: By default, the index is into the flattened tensor, otherwise along the specified axis.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Tensor of indices. It has the same shape as `x`, with the dimension along `axis` removed.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.arange(6).reshape(2, 3) + 10 >>> x array([[10, 11, 12],        [13, 14, 15]], dtype=int32) >>> keras.ops.argmax(x) array(5, dtype=int32) >>> keras.ops.argmax(x, axis=0) array([1, 1, 1], dtype=int32) >>> keras.ops.argmax(x, axis=1) array([2, 2], dtype=int32)`\
\
**Guides and examples using `argmax`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1105)\
\
### `argmin` function\
\
Copied!\
\
`keras.ops.argmin(x, axis=None, keepdims=False)`\
\
Returns the indices of the minimum values along an axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: By default, the index is into the flattened tensor, otherwise along the specified axis.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Tensor of indices. It has the same shape as `x`, with the dimension along `axis` removed.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.arange(6).reshape(2, 3) + 10 >>> x array([[10, 11, 12],        [13, 14, 15]], dtype=int32) >>> keras.ops.argmin(x) array(0, dtype=int32) >>> keras.ops.argmin(x, axis=0) array([0, 0, 0], dtype=int32) >>> keras.ops.argmin(x, axis=1) array([0, 0], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9593)\
\
### `argpartition` function\
\
Copied!\
\
`keras.ops.argpartition(x, kth, axis=-1)`\
\
Performs an indirect partition along the given axis.\
\
It returns an array of indices of the same shape as `x` that index data along the given axis in partitioned order.\
\
**Arguments**\
\
*   **x**: Array to sort.\
*   **kth**: Element index to partition by. The k-th element will be in its final sorted position and all smaller elements will be moved before it and all larger elements behind it. The order of all elements in the partitions is undefined. If provided with a sequence of k-th it will partition all of them into their sorted position at once.\
*   **axis**: Axis along which to sort. The default is -1 (the last axis). If `None`, the flattened array is used.\
\
**Returns**\
\
Array of indices that partition `x` along the specified `axis`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1154)\
\
### `argsort` function\
\
Copied!\
\
`keras.ops.argsort(x, axis=-1)`\
\
Returns the indices that would sort a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which to sort. Defaults to `-1` (the last axis). If `None`, the flattened tensor is used.\
\
**Returns**\
\
Tensor of indices that sort `x` along the specified `axis`.\
\
**Examples**\
\
One dimensional array:\
\
Copied!\
\
`>>> x = keras.ops.array([3, 1, 2]) >>> keras.ops.argsort(x) array([1, 2, 0], dtype=int32)`\
\
Two-dimensional array:\
\
Copied!\
\
`>>> x = keras.ops.array([[0, 3], [3, 2], [4, 5]]) >>> x array([[0, 3],        [3, 2],        [4, 5]], dtype=int32) >>> keras.ops.argsort(x, axis=0) array([[0, 1],        [1, 0],        [2, 2]], dtype=int32) >>> keras.ops.argsort(x, axis=1) array([[0, 1],        [1, 0],        [0, 1]], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1209)\
\
### `array` function\
\
Copied!\
\
`keras.ops.array(x, dtype=None)`\
\
Create a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **dtype**: The desired data-type for the tensor.\
\
**Returns**\
\
A tensor.\
\
**Examples**\
\
Copied!\
\
`>>> keras.ops.array([1, 2, 3]) array([1, 2, 3], dtype=int32)`\
\
Copied!\
\
`>>> keras.ops.array([1, 2, 3], dtype="float32") array([1., 2., 3.], dtype=float32)`\
\
**Guides and examples using `array`**\
\
*   [Recommending movies: ranking](https://keras.io/keras_rs/examples/basic_ranking/)\
    \
*   [Faster retrieval with Scalable Nearest Neighbours (ScANN)](https://keras.io/keras_rs/examples/scann/)\
    \
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
*   [List-wise ranking](https://keras.io/keras_rs/examples/listwise_ranking/)\
    \
*   [Rank movies with DLRM using KerasRS](https://keras.io/keras_rs/examples/dlrm/)\
    \
*   [Context-Aware Music Retrieval with Yambda and JAX](https://keras.io/keras_rs/examples/contextual_retrieval_yambda/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9760)\
\
### `array_split` function\
\
Copied!\
\
`keras.ops.array_split(x, indices_or_sections, axis=0)`\
\
Splits an array into multiple sub-arrays (unevenly).\
\
This is similar to [`keras.ops.split`](https://keras.io/api/ops/numpy#split-function)\
, but it allows for unequal splits. `indices_or_sections` must be an integer that indicates the total number of sub-arrays to create. If the tensor cannot be divided evenly, the first `remainder` splits will have size `quotient + 1`, and the rest will have size `quotient`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **indices\_or\_sections**: An integer indicating the number of sub-arrays to create.\
*   **axis**: The axis along which to split. Defaults to 0.\
\
**Returns**\
\
A list of sub-tensors.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.arange(10) >>> keras.ops.array_split(x, 3) (array([0, 1, 2, 3], dtype=int32),  array([4, 5, 6], dtype=int32),  array([7, 8, 9], dtype=int32))`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1341)\
\
### `average` function\
\
Copied!\
\
`keras.ops.average(x, axis=None, weights=None)`\
\
Compute the weighted average along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Integer along which to average `x`. The default, `axis=None`, will average over all of the elements of the input tensor. If axis is negative it counts from the last to the first axis.\
*   **weights**: Tensor of weights associated with the values in `x`. Each value in `x` contributes to the average according to its associated weight. The weights array can either be 1-D (in which case its length must be the size of a along the given axis) or of the same shape as `x`. If `weights=None` (default), then all data in `x` are assumed to have a weight equal to one.\
*   \_\_ The 1-D calculation is\_\_: `avg = sum(a * weights) / sum(weights)`. The only constraint on weights is that `sum(weights)` must not be 0.\
\
**Returns**\
\
Return the average along the specified axis.\
\
**Examples**\
\
Copied!\
\
`>>> data = keras.ops.arange(1, 5) >>> data array([1, 2, 3, 4], dtype=int32) >>> keras.ops.average(data) array(2.5, dtype=float32) >>> keras.ops.average( ...     keras.ops.arange(1, 11), ...     weights=keras.ops.arange(10, 0, -1) ... ) array(4., dtype=float32)`\
\
Copied!\
\
`>>> data = keras.ops.arange(6).reshape((3, 2)) >>> data array([[0, 1],        [2, 3],        [4, 5]], dtype=int32) >>> keras.ops.average( ...     data, ...     axis=1, ...     weights=keras.ops.array([1./4, 3./4]) ... ) array([0.75, 2.75, 4.75], dtype=float32) >>> keras.ops.average( ...     data, ...     weights=keras.ops.array([1./4, 3./4]) ... ) Traceback (most recent call last):     ... ValueError: Axis must be specified when shapes of a and weights differ.`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1399)\
\
### `bartlett` function\
\
Copied!\
\
`keras.ops.bartlett(x)`\
\
Bartlett window function. The Bartlett window is a triangular window that rises then falls linearly.\
\
**Arguments**\
\
*   **x**: Scalar or 1D Tensor. Window length.\
\
**Returns**\
\
A 1D tensor containing the Bartlett window values.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor(5) >>> keras.ops.bartlett(x) array([0. , 0.5, 1. , 0.5, 0. ], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1573)\
\
### `bincount` function\
\
Copied!\
\
`keras.ops.bincount(x, weights=None, minlength=0, sparse=False)`\
\
Count the number of occurrences of each value in a tensor of integers.\
\
**Arguments**\
\
*   **x**: Input tensor. It must be of dimension 1, and it must only contain non-negative integer(s).\
*   **weights**: Weight tensor. It must have the same length as `x`. The default value is `None`. If specified, `x` is weighted by it, i.e. if `n = x[i]`, `out[n] += weight[i]` instead of the default behavior `out[n] += 1`.\
*   **minlength**: An integer. The default value is 0. If specified, there will be at least this number of bins in the output tensor. If greater than `max(x) + 1`, each value of the output at an index higher than `max(x)` is set to 0.\
*   **sparse**: Whether to return a sparse tensor; for backends that support sparse tensors.\
\
**Returns**\
\
1D tensor where each element gives the number of occurrence(s) of its index value in x. Its length is the maximum between `max(x) + 1` and minlength.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.array([1, 2, 2, 3], dtype="uint8") >>> keras.ops.bincount(x) array([0, 1, 2, 1], dtype=int32) >>> weights = x / 2 >>> weights array([0.5, 1., 1., 1.5], dtype=float64) >>> keras.ops.bincount(x, weights=weights) array([0., 0.5, 2., 1.5], dtype=float64) >>> minlength = (keras.ops.max(x).numpy() + 1) + 2 # 6 >>> keras.ops.bincount(x, minlength=minlength) array([0, 1, 2, 1, 0, 0], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1629)\
\
### `bitwise_and` function\
\
Copied!\
\
`keras.ops.bitwise_and(x, y)`\
\
Compute the bit-wise AND of two arrays element-wise.\
\
Computes the bit-wise AND of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `&`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1657)\
\
### `bitwise_invert` function\
\
Copied!\
\
`keras.ops.bitwise_invert(x)`\
\
Compute bit-wise inversion, or bit-wise NOT, element-wise.\
\
Computes the bit-wise NOT of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `~`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1773)\
\
### `bitwise_left_shift` function\
\
Copied!\
\
`keras.ops.bitwise_left_shift(x, y)`\
\
Shift the bits of an integer to the left.\
\
Bits are shifted to the left by appending `y` 0s at the right of `x`. Since the internal representation of numbers is in binary format, this operation is equivalent to multiplying `x` by `2**y`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1684)\
\
### `bitwise_not` function\
\
Copied!\
\
`keras.ops.bitwise_not(x)`\
\
Compute bit-wise inversion, or bit-wise NOT, element-wise.\
\
Computes the bit-wise NOT of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `~`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1712)\
\
### `bitwise_or` function\
\
Copied!\
\
`keras.ops.bitwise_or(x, y)`\
\
Compute the bit-wise OR of two arrays element-wise.\
\
Computes the bit-wise OR of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `|`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1839)\
\
### `bitwise_right_shift` function\
\
Copied!\
\
`keras.ops.bitwise_right_shift(x, y)`\
\
Shift the bits of an integer to the right.\
\
Bits are shifted to the right `y`. Because the internal representation of numbers is in binary format, this operation is equivalent to dividing `x` by `2**y`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1741)\
\
### `bitwise_xor` function\
\
Copied!\
\
`keras.ops.bitwise_xor(x, y)`\
\
Compute the bit-wise XOR of two arrays element-wise.\
\
Computes the bit-wise XOR of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `^`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1893)\
\
### `blackman` function\
\
Copied!\
\
`keras.ops.blackman(x)`\
\
Blackman window function. The Blackman window is a taper formed by using a weighted cosine.\
\
**Arguments**\
\
*   **x**: Scalar or 1D tensor. Window length.\
\
**Returns**\
\
A 1D tensor containing the Blackman window values.\
\
**Example**\
\
Copied!\
\
`>>> keras.ops.blackman(x) array([-1.4901161e-08,  3.4000003e-01,  9.9999994e-01,  3.3999997e-01,    -1.4901161e-08], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1931)\
\
### `broadcast_to` function\
\
Copied!\
\
`keras.ops.broadcast_to(x, shape)`\
\
Broadcast a tensor to a new shape.\
\
**Arguments**\
\
*   **x**: The tensor to broadcast.\
*   **shape**: The shape of the desired tensor. A single integer `i` is interpreted as `(i,)`.\
\
**Returns**\
\
A tensor with the desired shape.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.array([1, 2, 3]) >>> keras.ops.broadcast_to(x, (3, 3)) array([[1, 2, 3],        [1, 2, 3],        [1, 2, 3]])`\
\
**Guides and examples using `broadcast_to`**\
\
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)\
    \
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1982)\
\
### `cbrt` function\
\
Copied!\
\
`keras.ops.cbrt(x)`\
\
Computes the cube root of the input tensor, element-wise.\
\
This operation returns the real-valued cube root of `x`, handling negative numbers properly in the real domain.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
A tensor containing the cube root of each element in `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2013)\
\
### `ceil` function\
\
Copied!\
\
`keras.ops.ceil(x)`\
\
Return the ceiling of the input, element-wise.\
\
The ceil of the scalar `x` is the smallest integer `i`, such that `i >= x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The ceiling of each element in `x`, with float dtype.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2047)\
\
### `clip` function\
\
Copied!\
\
`keras.ops.clip(x, x_min, x_max)`\
\
Clip (limit) the values in a tensor.\
\
Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of `[0, 1]` is specified, values smaller than 0 become 0, and values larger than 1 become 1.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **x\_min**: Minimum value.\
*   **x\_max**: Maximum value.\
\
**Returns**\
\
The clipped tensor.\
\
**Guides and examples using `clip`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2105)\
\
### `concatenate` function\
\
Copied!\
\
`keras.ops.concatenate(xs, axis=0)`\
\
Join a sequence of tensors along an existing axis.\
\
**Arguments**\
\
*   **xs**: The sequence of tensors to concatenate.\
*   **axis**: The axis along which the tensors will be joined. Defaults to `0`.\
\
**Returns**\
\
The concatenated tensor.\
\
**Guides and examples using `concatenate`**\
\
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)\
    \
*   [Electroencephalogram Signal Classification for Brain-Computer Interface](https://keras.io/examples/timeseries/eeg_bci_ssvepformer/)\
    \
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
*   [Recommending movies: ranking](https://keras.io/keras_rs/examples/basic_ranking/)\
    \
*   [Faster retrieval with Scalable Nearest Neighbours (ScANN)](https://keras.io/keras_rs/examples/scann/)\
    \
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
*   [Deep Recommenders](https://keras.io/keras_rs/examples/deep_recommender/)\
    \
*   [Ranking with Deep and Cross Networks](https://keras.io/keras_rs/examples/dcn/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2159)\
\
### `conj` function\
\
Copied!\
\
`keras.ops.conj(x)`\
\
Shorthand for [`keras.ops.conjugate`](https://keras.io/api/ops/numpy#conjugate-function)\
.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2135)\
\
### `conjugate` function\
\
Copied!\
\
`keras.ops.conjugate(x)`\
\
Returns the complex conjugate, element-wise.\
\
The complex conjugate of a complex number is obtained by changing the sign of its imaginary part.\
\
[`keras.ops.conj`](https://keras.io/api/ops/numpy#conj-function)\
 is a shorthand for this function.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The complex conjugate of each element in `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2174)\
\
### `copy` function\
\
Copied!\
\
`keras.ops.copy(x)`\
\
Returns a copy of `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
A copy of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9382)\
\
### `corrcoef` function\
\
Copied!\
\
`keras.ops.corrcoef(x)`\
\
Compute the Pearson correlation coefficient matrix.\
\
**Arguments**\
\
*   **x**: A 2D tensor of shape `(N, D)`, where N is the number of variables and D is the number of observations.\
\
**Returns**\
\
A tensor of shape `(N, N)` representing the correlation matrix.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9443)\
\
### `correlate` function\
\
Copied!\
\
`keras.ops.correlate(x1, x2, mode="valid")`\
\
Compute the cross-correlation of two 1-dimensional tensors.\
\
**Arguments**\
\
*   **x1**: First 1-dimensional input tensor of length M.\
*   **x2**: Second 1-dimensional input tensor of length N.\
*   **mode**: Either `valid`, `same` or `full`. By default the mode is set to `valid`, which returns an output of length max(M, N) - min(M, N) + 1. `same` returns an output of length max(M, N). `full` mode returns the convolution at each point of overlap, with an output length of N+M-1\
\
**Returns**\
\
Output tensor, cross-correlation of `x1` and `x2`.\
\
Notes: Complex-valued inputs are currently not fully supported on the TensorFlow and PyTorch backends. When complex tensors are passed, they are cast to floating-point types and the imaginary component is discarded.\
\
Copied!\
\
`This behavior is documented for clarity and may change in the future. See discussion in issue #21617.`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2202)\
\
### `cos` function\
\
Copied!\
\
`keras.ops.cos(x)`\
\
Cosine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The corresponding cosine values.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2230)\
\
### `cosh` function\
\
Copied!\
\
`keras.ops.cosh(x)`\
\
Hyperbolic cosine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2263)\
\
### `count_nonzero` function\
\
Copied!\
\
`keras.ops.count_nonzero(x, axis=None)`\
\
Counts the number of non-zero values in `x` along the given `axis`.\
\
If no axis is specified then all non-zeros in the tensor are counted.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or tuple of axes along which to count the number of non-zeros. Defaults to `None`.\
\
**Returns**\
\
int or tensor of ints.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.array([[0, 1, 7, 0], [3, 0, 2, 19]]) >>> keras.ops.count_nonzero(x) 5 >>> keras.ops.count_nonzero(x, axis=0) array([1, 1, 2, 1], dtype=int64) >>> keras.ops.count_nonzero(x, axis=1) array([2, 3], dtype=int64)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2346)\
\
### `cross` function\
\
Copied!\
\
`keras.ops.cross(x1, x2, axisa=-1, axisb=-1, axisc=-1, axis=None)`\
\
Returns the cross product of two (arrays of) vectors.\
\
The cross product of `x1` and `x2` in R^3 is a vector perpendicular to both `x1` and `x2`. If `x1` and `x2` are arrays of vectors, the vectors are defined by the last axis of `x1` and `x2` by default, and these axes can have dimensions 2 or 3.\
\
Where the dimension of either `x1` or `x2` is 2, the third component of the input vector is assumed to be zero and the cross product calculated accordingly.\
\
In cases where both input vectors have dimension 2, the z-component of the cross product is returned.\
\
**Arguments**\
\
*   **x1**: Components of the first vector(s).\
*   **x2**: Components of the second vector(s).\
*   **axisa**: Axis of `x1` that defines the vector(s). Defaults to `-1`.\
*   **axisb**: Axis of `x2` that defines the vector(s). Defaults to `-1`.\
*   **axisc**: Axis of the result containing the cross product vector(s). Ignored if both input vectors have dimension 2, as the return is scalar. By default, the last axis.\
*   **axis**: If defined, the axis of `x1`, `x2` and the result that defines the vector(s) and cross product(s). Overrides `axisa`, `axisb` and `axisc`.\
\
Note: Torch backend does not support two dimensional vectors, or the arguments `axisa`, `axisb` and `axisc`. Use `axis` instead.\
\
**Returns**\
\
Vector cross product(s).\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2423)\
\
### `cumprod` function\
\
Copied!\
\
`keras.ops.cumprod(x, axis=None, dtype=None)`\
\
Return the cumulative product of elements along a given axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which the cumulative product is computed. By default the input is flattened.\
*   **dtype**: dtype of returned tensor. Defaults to x.dtype.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2470)\
\
### `cumsum` function\
\
Copied!\
\
`keras.ops.cumsum(x, axis=None, dtype=None)`\
\
Returns the cumulative sum of elements along a given axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which the cumulative sum is computed. By default the input is flattened.\
*   **dtype**: dtype of returned tensor. Defaults to x.dtype.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2502)\
\
### `deg2rad` function\
\
Copied!\
\
`keras.ops.deg2rad(x)`\
\
Convert angles from degrees to radians.\
\
The conversion is defined as: `rad = deg * (π / 180)`\
\
**Arguments**\
\
*   **x**: Input tensor of angles in degrees.\
\
**Returns**\
\
A tensor containing angles converted to radians.\
\
**Examples**\
\
Copied!\
\
`>>> from keras import ops >>> ops.deg2rad(180.0) 3.141592653589793 >>> ops.deg2rad([0.0, 90.0, 180.0]) array([0., 1.57079633, 3.14159265])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2602)\
\
### `diag` function\
\
Copied!\
\
`keras.ops.diag(x, k=0)`\
\
Extract a diagonal or construct a diagonal array.\
\
**Arguments**\
\
*   **x**: Input tensor. If `x` is 2-D, returns the k-th diagonal of `x`. If `x` is 1-D, return a 2-D tensor with `x` on the k-th diagonal.\
*   **k**: The diagonal to consider. Defaults to `0`. Use `k > 0` for diagonals above the main diagonal, and `k < 0` for diagonals below the main diagonal.\
\
**Returns**\
\
The extracted diagonal or constructed diagonal tensor.\
\
**Examples**\
\
Copied!\
\
`>>> from keras.src import ops >>> x = ops.arange(9).reshape((3, 3)) >>> x array([[0, 1, 2],        [3, 4, 5],        [6, 7, 8]])`\
\
Copied!\
\
`>>> ops.diag(x) array([0, 4, 8]) >>> ops.diag(x, k=1) array([1, 5]) >>> ops.diag(x, k=-1) array([3, 7])`\
\
Copied!\
\
`>>> ops.diag(ops.diag(x))) array([[0, 0, 0],        [0, 4, 0],        [0, 0, 8]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2678)\
\
### `diagflat` function\
\
Copied!\
\
`keras.ops.diagflat(x, k=0)`\
\
Create a two-dimensional array with the flattened input on the k-th diagonal.\
\
**Arguments**\
\
*   **x**: Input tensor to be flattened and placed on the diagonal.\
*   **k**: The diagonal to place the flattened input. Defaults to `0`. Use `k > 0` for diagonals above the main diagonal, and `k < 0` for diagonals below the main diagonal.\
\
**Returns**\
\
A 2-D tensor with the flattened input on the specified diagonal.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2739)\
\
### `diagonal` function\
\
Copied!\
\
`keras.ops.diagonal(x, offset=0, axis1=0, axis2=1)`\
\
Return specified diagonals.\
\
If `x` is 2-D, returns the diagonal of `x` with the given offset, i.e., the collection of elements of the form `x[i, i+offset]`.\
\
If `x` has more than two dimensions, the axes specified by `axis1` and `axis2` are used to determine the 2-D sub-array whose diagonal is returned.\
\
The shape of the resulting array can be determined by removing `axis1` and `axis2` and appending an index to the right equal to the size of the resulting diagonals.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **offset**: Offset of the diagonal from the main diagonal. Can be positive or negative. Defaults to `0`.(main diagonal).\
*   **axis1**: Axis to be used as the first axis of the 2-D sub-arrays. Defaults to `0`.(first axis).\
*   **axis2**: Axis to be used as the second axis of the 2-D sub-arrays. Defaults to `1` (second axis).\
\
**Returns**\
\
Tensor of diagonals.\
\
**Examples**\
\
Copied!\
\
`>>> from keras.src import ops >>> x = ops.arange(4).reshape((2, 2)) >>> x array([[0, 1],        [2, 3]]) >>> x.diagonal() array([0, 3]) >>> x.diagonal(1) array([1])`\
\
Copied!\
\
`>>> x = ops.arange(8).reshape((2, 2, 2)) >>> x array([[[0, 1],         [2, 3]],        [[4, 5],         [6, 7]]]) >>> x.diagonal(0, 0, 1) array([[0, 6],        [1, 7]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2827)\
\
### `diff` function\
\
Copied!\
\
`keras.ops.diff(a, n=1, axis=-1)`\
\
Calculate the n-th discrete difference along the given axis.\
\
The first difference is given by `out[i] = a[i+1] - a[i]` along the given axis, higher differences are calculated by using `diff` recursively.\
\
**Arguments**\
\
*   **a**: Input tensor.\
*   **n**: The number of times values are differenced. Defaults to `1`.\
*   **axis**: Axis to compute discrete difference(s) along. Defaults to `-1`.(last axis).\
\
**Returns**\
\
Tensor of diagonals.\
\
**Examples**\
\
Copied!\
\
`>>> from keras.src import ops >>> x = ops.convert_to_tensor([1, 2, 4, 7, 0]) >>> ops.diff(x) array([ 1,  2,  3, -7]) >>> ops.diff(x, n=2) array([  1,   1, -10])`\
\
Copied!\
\
`>>> x = ops.convert_to_tensor([[1, 3, 6, 10], [0, 5, 6, 8]]) >>> ops.diff(x) array([[2, 3, 4],        [5, 1, 2]]) >>> ops.diff(x, axis=0) array([[-1,  2,  0, -2]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2877)\
\
### `digitize` function\
\
Copied!\
\
`keras.ops.digitize(x, bins)`\
\
Returns the indices of the bins to which each value in `x` belongs.\
\
**Arguments**\
\
*   **x**: Input array to be binned.\
*   **bins**: Array of bins. It has to be one-dimensional and monotonically increasing.\
\
**Returns**\
\
Output array of indices, of same shape as `x`.\
\
**Example**\
\
Copied!\
\
`>>> x = np.array([0.0, 1.0, 3.0, 1.6]) >>> bins = np.array([0.0, 3.0, 4.5, 7.0]) >>> keras.ops.digitize(x, bins) array([1, 1, 2, 1])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8686)\
\
### `divide` function\
\
Copied!\
\
`keras.ops.divide(x1, x2)`\
\
Divide arguments element-wise.\
\
[`keras.ops.true_divide`](https://keras.io/api/ops/numpy#truedivide-function)\
 is an alias for this function.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, the quotient `x1/x2`, element-wise.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8725)\
\
### `divide_no_nan` function\
\
Copied!\
\
`keras.ops.divide_no_nan(x1, x2)`\
\
Safe element-wise division which returns 0 where the denominator is 0.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
The quotient `x1/x2`, element-wise, with zero where x2 is zero.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2940)\
\
### `dot` function\
\
Copied!\
\
`keras.ops.dot(x1, x2)`\
\
Dot product of two tensors.\
\
*   If both `x1` and `x2` are 1-D tensors, it is inner product of vectors (without complex conjugation).\
*   If both `x1` and `x2` are 2-D tensors, it is matrix multiplication.\
*   If either `x1` or `x2` is 0-D (scalar), it is equivalent to `x1 * x2`.\
*   If `x1` is an N-D tensor and `x2` is a 1-D tensor, it is a sum product over the last axis of `x1` and `x2`.\
*   If `x1` is an N-D tensor and `x2` is an M-D tensor (where `M>=2`), it is a sum product over the last axis of `x1` and the second-to-last axis of `x2`: `dot(x1, x2)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`.\
\
**Arguments**\
\
*   **x1**: First argument.\
*   **x2**: Second argument.\
\
Note: Torch backend does not accept 0-D tensors as arguments.\
\
**Returns**\
\
Dot product of `x1` and `x2`.\
\
**Guides and examples using `dot`**\
\
*   [Rank movies with DLRM using KerasRS](https://keras.io/keras_rs/examples/dlrm/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3008)\
\
### `dstack` function\
\
Copied!\
\
`keras.ops.dstack(xs)`\
\
Stack tensors in sequence depth wise (along third axis).\
\
This is equivalent to concatenation along the third axis after 2-D tensors of shape `(M, N)` have been reshaped to `(M, N, 1)` and 1-D tensors of shape `(N,)` have been reshaped to `(1, N, 1)`.\
\
**Arguments**\
\
*   **xs**: Sequence of tensors.\
\
**Returns**\
\
The tensor formed by stacking the given tensors.\
\
**Examples**\
\
Copied!\
\
`>>> import keras >>> x = keras.ops.array([1, 2, 3]) >>> y = keras.ops.array([4, 5, 6]) >>> keras.ops.dstack([x, y]) array([[[1, 4],         [2, 5],         [3, 6]]])`\
\
Copied!\
\
`>>> x = keras.ops.array([[1], [2], [3]]) >>> y = keras.ops.array([[4], [5], [6]]) >>> keras.ops.dstack([x, y]) array([[[1, 4]],        [[2, 5]],        [[3, 6]]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3222)\
\
### `einsum` function\
\
Copied!\
\
`keras.ops.einsum(subscripts, *operands, **kwargs)`\
\
Evaluates the Einstein summation convention on the operands.\
\
**Arguments**\
\
*   **subscripts**: Specifies the subscripts for summation as comma separated list of subscript labels. An implicit (classical Einstein summation) calculation is performed unless the explicit indicator `->` is included as well as subscript labels of the precise output form.\
*   **operands**: The operands to compute the Einstein sum of.\
\
**Returns**\
\
The calculation based on the Einstein summation convention.\
\
**Example**\
\
Copied!\
\
`>>> from keras.src import ops >>> a = ops.arange(25).reshape(5, 5) >>> b = ops.arange(5) >>> c = ops.arange(6).reshape(2, 3)`\
\
Trace of a matrix:\
\
Copied!\
\
`>>> ops.einsum("ii", a) 60 >>> ops.einsum(a, [0, 0]) 60 >>> ops.trace(a) 60`\
\
Extract the diagonal:\
\
Copied!\
\
`>>> ops.einsum("ii -> i", a) array([ 0,  6, 12, 18, 24]) >>> ops.einsum(a, [0, 0], [0]) array([ 0,  6, 12, 18, 24]) >>> ops.diag(a) array([ 0,  6, 12, 18, 24])`\
\
Sum over an axis:\
\
Copied!\
\
`>>> ops.einsum("ij -> i", a) array([ 10,  35,  60,  85, 110]) >>> ops.einsum(a, [0, 1], [0]) array([ 10,  35,  60,  85, 110]) >>> ops.sum(a, axis=1) array([ 10,  35,  60,  85, 110])`\
\
For higher dimensional tensors summing a single axis can be done with ellipsis:\
\
Copied!\
\
`>>> ops.einsum("...j -> ...", a) array([ 10,  35,  60,  85, 110]) >>> np.einsum(a, [..., 1], [...]) array([ 10,  35,  60,  85, 110])`\
\
Compute a matrix transpose or reorder any number of axes:\
\
Copied!\
\
`>>> ops.einsum("ji", c) array([[0, 3],        [1, 4],        [2, 5]]) >>> ops.einsum("ij -> ji", c) array([[0, 3],        [1, 4],        [2, 5]]) >>> ops.einsum(c, [1, 0]) array([[0, 3],        [1, 4],        [2, 5]]) >>> ops.transpose(c) array([[0, 3],        [1, 4],        [2, 5]])`\
\
Matrix vector multiplication:\
\
Copied!\
\
`>>> ops.einsum("ij, j", a, b) array([ 30,  80, 130, 180, 230]) >>> ops.einsum(a, [0, 1], b, [1]) array([ 30,  80, 130, 180, 230]) >>> ops.einsum("...j, j", a, b) array([ 30,  80, 130, 180, 230])`\
\
**Guides and examples using `einsum`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Metric learning for image similarity search](https://keras.io/examples/vision/metric_learning/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3311)\
\
### `empty` function\
\
Copied!\
\
`keras.ops.empty(shape, dtype=None)`\
\
Return a tensor of given shape and type filled with uninitialized data.\
\
**Arguments**\
\
*   **shape**: Shape of the empty tensor.\
*   **dtype**: Desired data type of the empty tensor.\
\
**Returns**\
\
The empty tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3342)\
\
### `empty_like` function\
\
Copied!\
\
`keras.ops.empty_like(x, dtype=None)`\
\
Return a new uninitialized tensor with the same shape and dtype as `x`.\
\
**Arguments**\
\
*   **x**: Input tensor to mimic shape and dtype.\
*   **dtype**: Optional data type. If None, uses `x.dtype`.\
\
**Returns**\
\
A tensor with the same shape and dtype as `x`, with arbitrary contents.\
\
**Example**\
\
Copied!\
\
`>>> from keras import ops >>> x = ops.ones((2, 3), dtype="float32") >>> y = ops.empty_like(x) >>> y.shape (2, 3) >>> y.dtype dtype('float32')`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3379)\
\
### `equal` function\
\
Copied!\
\
`keras.ops.equal(x1, x2)`\
\
Returns `(x1 == x2)` element-wise.\
\
**Arguments**\
\
*   **x1**: Tensor to compare.\
*   **x2**: Tensor to compare.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
**Guides and examples using `equal`**\
\
*   [A mobile-friendly Transformer-based model for image classification](https://keras.io/examples/vision/mobilevit/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3406)\
\
### `exp` function\
\
Copied!\
\
`keras.ops.exp(x)`\
\
Calculate the exponential of all elements in the input tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise exponential of `x`.\
\
**Guides and examples using `exp`**\
\
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3432)\
\
### `exp2` function\
\
Copied!\
\
`keras.ops.exp2(x)`\
\
Calculate the base-2 exponential of all elements in the input tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise base-2 exponential of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3468)\
\
### `expand_dims` function\
\
Copied!\
\
`keras.ops.expand_dims(x, axis)`\
\
Expand the shape of a tensor.\
\
Insert a new axis at the `axis` position in the expanded tensor shape.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Position in the expanded axes where the new axis (or axes) is placed.\
\
**Returns**\
\
Output tensor with the number of dimensions increased.\
\
**Guides and examples using `expand_dims`**\
\
*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)\
    \
*   [Object Detection Fine-tuning with KerasHub](https://keras.io/keras_hub/guides/object_detection_retinanet/)\
    \
*   [Image classification from scratch](https://keras.io/examples/vision/image_classification_from_scratch/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Structured data learning with Wide, Deep, and Cross networks](https://keras.io/examples/structured_data/wide_deep_cross_networks/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
*   [Classification with Neural Decision Forests](https://keras.io/examples/structured_data/deep_neural_decision_forests/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3504)\
\
### `expm1` function\
\
Copied!\
\
`keras.ops.expm1(x)`\
\
Calculate `exp(x) - 1` for all elements in the tensor.\
\
**Arguments**\
\
*   **x**: Input values.\
\
**Returns**\
\
Output tensor, element-wise exponential minus one.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9280)\
\
### `eye` function\
\
Copied!\
\
`keras.ops.eye(N, M=None, k=0, dtype=None)`\
\
Return a 2-D tensor with ones on the diagonal and zeros elsewhere.\
\
**Arguments**\
\
*   **N**: Number of rows in the output.\
*   **M**: Number of columns in the output. If `None`, defaults to `N`.\
*   **k**: Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.\
*   **dtype**: Data type of the returned tensor.\
\
**Returns**\
\
Tensor with ones on the k-th diagonal and zeros elsewhere.\
\
**Guides and examples using `eye`**\
\
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
*   [Sequential retrieval \[GRU4Rec\]](https://keras.io/keras_rs/examples/sequential_retrieval/)\
    \
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
*   [Context-Aware Music Retrieval with Yambda and JAX](https://keras.io/keras_rs/examples/contextual_retrieval_yambda/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L206)\
\
### `fabs` function\
\
Copied!\
\
`keras.ops.fabs(x)`\
\
Compute the absolute values element-wise.\
\
Integer or boolean inputs are automatically promoted to the default floating-point type. Complex values are not supported.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
An array containing the absolute value of each element in `x`.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([-1, 2], dtype="int32") >>> keras.ops.fabs(x) array([1., 2.], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3533)\
\
### `flip` function\
\
Copied!\
\
`keras.ops.flip(x, axis=None)`\
\
Reverse the order of elements in the tensor along the given axis.\
\
The shape of the tensor is preserved, but the elements are reordered.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which to flip the tensor. The default, `axis=None`, will flip over all of the axes of the input tensor.\
\
**Returns**\
\
Output tensor with entries of `axis` reversed.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3565)\
\
### `fliplr` function\
\
Copied!\
\
`keras.ops.fliplr(x)`\
\
Reverse the order of elements along axis 1 (left/right).\
\
For a 2-D tensor, this flips the entries in each row in the left/right direction. Columns are preserved, but appear in a different order than before.\
\
**Arguments**\
\
*   **x**: Input tensor, must be at least 2-D.\
\
**Returns**\
\
Output tensor with columns reversed.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3597)\
\
### `flipud` function\
\
Copied!\
\
`keras.ops.flipud(x)`\
\
Reverse the order of elements along axis 0 (up/down).\
\
For a 2-D tensor, this flips the entries in each column in the up/down direction. Rows are preserved, but appear in a different order than before.\
\
**Arguments**\
\
*   **x**: Input tensor, must be at least 1-D.\
\
**Returns**\
\
Output tensor with rows reversed.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3630)\
\
### `floor` function\
\
Copied!\
\
`keras.ops.floor(x)`\
\
Return the floor of the input, element-wise.\
\
The floor of the scalar `x` is the largest integer `i`, such that `i <= x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise floor of `x`.\
\
**Guides and examples using `floor`**\
\
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9326)\
\
### `floor_divide` function\
\
Copied!\
\
`keras.ops.floor_divide(x1, x2)`\
\
Returns the largest integer smaller or equal to the division of inputs.\
\
**Arguments**\
\
*   **x1**: Numerator.\
*   **x2**: Denominator.\
\
**Returns**\
\
Output tensor, `y = floor(x1/x2)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5217)\
\
### `fmax` function\
\
Copied!\
\
`keras.ops.fmax(x1, x2)`\
\
Element-wise maximum of tensor elements, ignoring NaNs.\
\
Compare two tensors element-wise and return the maximum. If one of the elements being compared is a NaN, the non-NaN element is returned. If both elements are NaNs, the NaN is returned.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise maximum of `x1` and `x2`.\
\
**Examples**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([2.0, float("nan")]) >>> x2 = keras.ops.convert_to_tensor([1.0, 4.0]) >>> keras.ops.fmax(x1, x2) array([2.0, 4.0], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5456)\
\
### `fmin` function\
\
Copied!\
\
`keras.ops.fmin(x1, x2)`\
\
Element-wise minimum of tensor elements, ignoring NaNs.\
\
Compare two tensors element-wise and return the minimum. If one of the elements being compared is a NaN, the non-NaN element is returned. If both elements are NaNs, the NaN is returned.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise minimum of `x1` and `x2`.\
\
**Examples**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([2.0, float("nan")]) >>> x2 = keras.ops.convert_to_tensor([1.0, 4.0]) >>> keras.ops.fmin(x1, x2) array([1.0, 4.0], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5532)\
\
### `fmod` function\
\
Copied!\
\
`keras.ops.fmod(x1, x2)`\
\
Returns the element-wise remainder of division with truncation.\
\
Computes the remainder complementary to the `floor_divide` function, equivalent to the C library function `fmod`. The result has the same sign as the dividend `x1`. This is different from [`keras.ops.mod`](https://keras.io/api/ops/numpy#mod-function)\
 which has the same sign as the divisor `x2`.\
\
**Arguments**\
\
*   **x1**: First tensor, the dividend.\
*   **x2**: Second tensor, the divisor.\
\
**Returns**\
\
Output tensor, element-wise remainder with truncation.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3661)\
\
### `full` function\
\
Copied!\
\
`keras.ops.full(shape, fill_value, dtype=None)`\
\
Return a new tensor of given shape and type, filled with `fill_value`.\
\
**Arguments**\
\
*   **shape**: Shape of the new tensor.\
*   **fill\_value**: Fill value.\
*   **dtype**: Desired data type of the tensor.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3696)\
\
### `full_like` function\
\
Copied!\
\
`keras.ops.full_like(x, fill_value, dtype=None)`\
\
Return a full tensor with the same shape and type as the given tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **fill\_value**: Fill value.\
*   **dtype**: Overrides data type of the result.\
\
**Returns**\
\
Tensor of `fill_value` with the same shape and type as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3729)\
\
### `gcd` function\
\
Copied!\
\
`keras.ops.gcd(x1, x2)`\
\
Greatest common divisor of `x1` and `x2`, element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor (integer type).\
*   **x2**: Second input tensor (integer type).\
\
**Returns**\
\
Output tensor, element-wise greatest common divisor of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3860)\
\
### `geomspace` function\
\
Copied!\
\
`keras.ops.geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)`\
\
Returns numbers spaced evenly on a log scale (a geometric progression).\
\
This is similar to `logspace`, but with endpoints specified directly instead of as logarithms. Each output sample is a constant multiple of the previous.\
\
**Arguments**\
\
*   **start**: The starting value of the sequence.\
*   **stop**: The final value of the sequence, unless `endpoint` is `False`. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length `num`) are returned.\
*   **num**: Number of samples to generate. Defaults to `50`.\
*   **endpoint**: If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`.\
*   **dtype**: The type of the output tensor.\
*   **axis**: The axis in the result to store the samples. Relevant only if start or stop are array-like.\
\
Note: Torch backend does not support `axis` argument.\
\
**Returns**\
\
A tensor of `num` samples, evenly spaced on a log scale.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3818)\
\
### `get_item` function\
\
Copied!\
\
`keras.ops.get_item(x, key)`\
\
Return `x[key]`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3911)\
\
### `greater` function\
\
Copied!\
\
`keras.ops.greater(x1, x2)`\
\
Return the truth value of `x1 > x2` element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
**Guides and examples using `greater`**\
\
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
*   [Deep Recommenders](https://keras.io/keras_rs/examples/deep_recommender/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3938)\
\
### `greater_equal` function\
\
Copied!\
\
`keras.ops.greater_equal(x1, x2)`\
\
Return the truth value of `x1 >= x2` element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1423)\
\
### `hamming` function\
\
Copied!\
\
`keras.ops.hamming(x)`\
\
Hamming window function.\
\
The Hamming window is defined as: `w[n] = 0.54 - 0.46 * cos(2 * pi * n / (N - 1))` for `0 <= n <= N - 1`.\
\
**Arguments**\
\
*   **x**: Scalar or 1D Tensor. The window length.\
\
**Returns**\
\
A 1D tensor containing the Hamming window values.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor(5) >>> keras.ops.hamming(x) array([0.08, 0.54, 1.  , 0.54, 0.08], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1449)\
\
### `hanning` function\
\
Copied!\
\
`keras.ops.hanning(x)`\
\
Hanning window function.\
\
The Hanning window is defined as: `w[n] = 0.5 - 0.5 * cos(2 * pi * n / (N - 1))` for `0 <= n <= N - 1`.\
\
**Arguments**\
\
*   **x**: Scalar or 1D Tensor. The window length.\
\
**Returns**\
\
A 1D tensor containing the Hanning window values.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor(5) >>> keras.ops.hanning(x) array([0. , 0.5, 1. , 0.5, 0. ], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1488)\
\
### `heaviside` function\
\
Copied!\
\
`keras.ops.heaviside(x1, x2)`\
\
Heaviside step function.\
\
The Heaviside step function is defined as: `heaviside(x1, x2) = 0 if x1 < 0, 1 if x1 > 0, x2 if x1 == 0`\
\
**Arguments**\
\
*   **x1**: A tensor input.\
*   **x2**: A scalar or tensor, the value to return when `x1 == 0`.\
\
**Returns**\
\
A tensor with a shape determined by broadcasting `x1` and `x2`.\
\
**Example**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([-2.0, 0.0, 3.0]) >>> x2 = 0.5 >>> keras.ops.heaviside(x1, x2) array([0. , 0.5, 1. ], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9654)\
\
### `histogram` function\
\
Copied!\
\
`keras.ops.histogram(x, bins=10, range=None)`\
\
Computes a histogram of the data tensor `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **bins**: An integer representing the number of histogram bins. Defaults to 10.\
*   **range**: A tuple representing the lower and upper range of the bins. If not specified, it will use the min and max of `x`.\
\
**Returns**\
\
*   **A tuple containing**:\
*   A tensor representing the counts of elements in each bin.\
*   A tensor representing the bin edges.\
\
**Example**\
\
Copied!\
\
`>>> input_tensor = np.random.rand(8) >>> keras.ops.histogram(input_tensor) (array([1, 1, 1, 0, 0, 1, 2, 1, 0, 1], dtype=int32), array([0.0189519 , 0.10294958, 0.18694726, 0.27094494, 0.35494262,     0.43894029, 0.52293797, 0.60693565, 0.69093333, 0.77493101,     0.85892869]))`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4025)\
\
### `hsplit` function\
\
Copied!\
\
`keras.ops.hsplit(x, indices_or_sections)`\
\
Split an array into multiple sub-arrays horizontally (column-wise).\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **indices\_or\_sections**: If an integer, N, the tensor will be split into N equal sections along axis 1 (if ndim >= 2) or axis 0 (if ndim == 1). If a 1-D array of sorted integers, the entries indicate indices at which the tensor will be split along the axis.\
\
**Returns**\
\
A list of sub-arrays.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.arange(16.0).reshape((4, 4)) >>> keras.ops.hsplit(x, 2) [array([[ 0.,  1.],        [ 4.,  5.],        [ 8.,  9.],        [12., 13.]]),  array([[ 2.,  3.],        [ 6.,  7.],        [10., 11.],        [14., 15.]])] >>> keras.ops.hsplit(x, [1, 3]) [array([[0.],     [4.],     [8.],     [12.]]), array([[1., 2.],     [5., 6.],     [9., 10.],     [13., 14.]]), array([[3.],     [7.],     [11.],     [15.]])]`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3986)\
\
### `hstack` function\
\
Copied!\
\
`keras.ops.hstack(xs)`\
\
Stack tensors in sequence horizontally (column wise).\
\
This is equivalent to concatenation along the first axis for 1-D tensors, and along the second axis for all other tensors.\
\
**Arguments**\
\
*   **xs**: Sequence of tensors.\
\
**Returns**\
\
The tensor formed by stacking the given tensors.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4083)\
\
### `hypot` function\
\
Copied!\
\
`keras.ops.hypot(x1, x2)`\
\
Element-wise hypotenuse of right triangles with legs `x1` and `x2`.\
\
This is equivalent to computing `sqrt(x1**2 + x2**2)` element-wise, with shape determined by broadcasting.\
\
**Arguments**\
\
*   **x1**: A tensor, representing the first leg of the right triangle.\
*   **x2**: A tensor, representing the second leg of the right triangle.\
\
**Returns**\
\
A tensor with a shape determined by broadcasting `x1` and `x2`.\
\
**Example**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([3.0, 4.0, 5.0]) >>> x2 = keras.ops.convert_to_tensor([4.0, 3.0, 12.0]) >>> keras.ops.hypot(x1, x2) array([5., 5., 13.], dtype=float32)`\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([[1, 2], [3, 4]]) >>> x2 = keras.ops.convert_to_tensor([1, 1]) >>> keras.ops.hypot(x1, x2) array([[1.41421356 2.23606798],       [3.16227766 4.12310563]], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4168)\
\
### `i0` function\
\
Copied!\
\
`keras.ops.i0(x)`\
\
Modified Bessel function of the first kind, order 0.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise modified Bessel function of the first kind, order 0 of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4114)\
\
### `identity` function\
\
Copied!\
\
`keras.ops.identity(n, dtype=None)`\
\
Return the identity tensor.\
\
The identity tensor is a square tensor with ones on the main diagonal and zeros elsewhere.\
\
**Arguments**\
\
*   **n**: Number of rows (and columns) in the `n x n` output tensor.\
*   **dtype**: Data type of the output tensor.\
\
**Returns**\
\
The identity tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4140)\
\
### `imag` function\
\
Copied!\
\
`keras.ops.imag(x)`\
\
Return the imaginary part of the complex argument.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The imaginary component of the complex argument.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8394)\
\
### `inner` function\
\
Copied!\
\
`keras.ops.inner(x1, x2)`\
\
Return the inner product of two tensors.\
\
Ordinary inner product of vectors for 1-D tensors (without complex conjugation), in higher dimensions a sum product over the last axes.\
\
Multidimensional arrays are treated as vectors by flattening all but their last axes. The resulting dot product is performed over their last axes.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor. The last dimension of `x1` and `x2` must match.\
\
**Returns**\
\
Output tensor. The shape of the output is determined by broadcasting the shapes of `x1` and `x2` after removing their last axes.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4199)\
\
### `isclose` function\
\
Copied!\
\
`keras.ops.isclose(x1, x2, rtol=1e-05, atol=1e-08, equal_nan=False)`\
\
Return whether two tensors are element-wise almost equal.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
*   **rtol**: Relative tolerance.\
*   **atol**: Absolute tolerance.\
*   **equal\_nan**: If `True`, element-wise NaNs are considered equal.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4226)\
\
### `isfinite` function\
\
Copied!\
\
`keras.ops.isfinite(x)`\
\
Return whether a tensor is finite, element-wise.\
\
Real values are finite when they are not NaN, not positive infinity, and not negative infinity. Complex values are finite when both their real and imaginary parts are finite.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4315)\
\
### `isinf` function\
\
Copied!\
\
`keras.ops.isinf(x)`\
\
Test element-wise for positive or negative infinity.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4266)\
\
### `isin` function\
\
Copied!\
\
`keras.ops.isin(x1, x2, assume_unique=False, invert=False)`\
\
Test whether each element of `x1` is present in `x2`.\
\
This operation performs element-wise checks to determine if each value in `x1` is contained within `x2`. The result is a boolean tensor with the same shape as `x1`, where each entry is `True` if the corresponding element in `x1` is in `x2`, and `False` otherwise.\
\
**Arguments**\
\
*   **x1**: Input tensor or array-like structure to test.\
*   **x2**: Values against which each element of `x1` is tested. Can be a tensor, list, or scalar.\
*   **assume\_unique**: Boolean (default: False). If True, assumes both `x1` and `x2` contain only unique elements. This can speed up the computation. If False, duplicates will be handled correctly but may impact performance.\
*   **invert**: A boolean (default: False). If True, inverts the result. Entries will be `True` where `x1` elements are not in `x2`.\
\
**Returns**\
\
A boolean tensor of the same shape as `x1` indicating element-wise membership in `x2`.\
\
**Example**\
\
Copied!\
\
`>>> from keras import ops >>> x1 = ops.array([0, 1, 2, 5]) >>> x2 = ops.array([0, 2]) >>> result = ops.isin(x1, x2) array([ True, False,  True, False])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4338)\
\
### `isnan` function\
\
Copied!\
\
`keras.ops.isnan(x)`\
\
Test element-wise for NaN and return result as a boolean tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4361)\
\
### `isneginf` function\
\
Copied!\
\
`keras.ops.isneginf(x)`\
\
Test element-wise for negative infinity.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4384)\
\
### `isposinf` function\
\
Copied!\
\
`keras.ops.isposinf(x)`\
\
Test element-wise for positive infinity.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4407)\
\
### `isreal` function\
\
Copied!\
\
`keras.ops.isreal(x)`\
\
Test element-wise for real numbers.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
**Example**\
\
Copied!\
\
`>>> from keras import ops >>> x = ops.array([1+1j, 1+0j, 4.5, 3, 2, 2j], dtype="complex64") >>> ops.isreal(x) array([False,  True,  True,  True,  True, False])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1513)\
\
### `kaiser` function\
\
Copied!\
\
`keras.ops.kaiser(x, beta)`\
\
Kaiser window function.\
\
The Kaiser window is defined as: `w[n] = I0(beta * sqrt(1 - (2n / (N - 1) - 1)^2)) / I0(beta)` where I0 is the modified zeroth-order Bessel function of the first kind.\
\
**Arguments**\
\
*   **x**: Scalar or 1D Tensor. The window length.\
*   **beta**: Float. Shape parameter for the Kaiser window.\
\
**Returns**\
\
A 1D tensor containing the Kaiser window values.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor(5) >>> keras.ops.kaiser(x, beta=14.0) array([7.7268669e-06, 1.6493219e-01, 1.0000000e+00, 1.6493219e-01,    7.7268669e-06], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4451)\
\
### `kron` function\
\
Copied!\
\
`keras.ops.kron(x1, x2)`\
\
Kronecker product of `x1` and `x2`.\
\
Computes the Kronecker product of two input tensors. If `x1` has shape `(a0, a1, ..., an)` and `x2` has shape `(b0, b1, ..., bn)`, then the output will have shape `(a0*b0, a1*b1, ..., an*bn)`.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
A tensor representing the Kronecker product of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4486)\
\
### `lcm` function\
\
Copied!\
\
`keras.ops.lcm(x1, x2)`\
\
Least common multiple of `x1` and `x2`, element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor (integer type).\
*   **x2**: Second input tensor (integer type).\
\
**Returns**\
\
Output tensor, element-wise least common multiple of `x1` and `x2`.\
\
**Example**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([2, 3, 4]) >>> x2 = keras.ops.convert_to_tensor([5, 6, 7]) >>> keras.ops.lcm(x1, x2) array([10,  6, 28], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4523)\
\
### `ldexp` function\
\
Copied!\
\
`keras.ops.ldexp(x1, x2)`\
\
Multiply `x1` by 2 raised to the power of `x2`, element-wise.\
\
This function computes: ldexp(x1, x2) = x1 \* 2\*\*x2\
\
**Arguments**\
\
*   **x1**: Float input tensor.\
*   **x2**: Integer exponent tensor.\
\
**Returns**\
\
Output tensor\
\
**Example**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([0.75, 1.5]) >>> x2 = keras.ops.convert_to_tensor([1, 2]) >>> keras.ops.ldexp(x1, x2) array([1.5, 6. ], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1807)\
\
### `left_shift` function\
\
Copied!\
\
`keras.ops.left_shift(x, y)`\
\
Shift the bits of an integer to the left.\
\
Bits are shifted to the left by appending `y` 0s at the right of `x`. Since the internal representation of numbers is in binary format, this operation is equivalent to multiplying `x` by `2**y`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4559)\
\
### `less` function\
\
Copied!\
\
`keras.ops.less(x1, x2)`\
\
Return the truth value of `x1 < x2` element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4586)\
\
### `less_equal` function\
\
Copied!\
\
`keras.ops.less_equal(x1, x2)`\
\
Return the truth value of `x1 <= x2` element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4655)\
\
### `linspace` function\
\
Copied!\
\
`keras.ops.linspace(     start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0 )`\
\
Return evenly spaced numbers over a specified interval.\
\
Returns `num` evenly spaced samples, calculated over the interval `[start, stop]`.\
\
The endpoint of the interval can optionally be excluded.\
\
**Arguments**\
\
*   **start**: The starting value of the sequence.\
*   **stop**: The end value of the sequence, unless `endpoint` is set to `False`. In that case, the sequence consists of all but the last of `num + 1` evenly spaced samples, so that `stop` is excluded. Note that the step size changes when `endpoint` is `False`.\
*   **num**: Number of samples to generate. Defaults to `50`. Must be non-negative.\
*   **endpoint**: If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`.\
*   **retstep**: If `True`, return `(samples, step)`, where `step` is the spacing between samples.\
*   **dtype**: The type of the output tensor.\
*   **axis**: The axis in the result to store the samples. Relevant only if start or stop are array-like. Defaults to `0`.\
\
Note: Torch backend does not support `axis` argument.\
\
**Returns**\
\
A tensor of evenly spaced numbers. If `retstep` is `True`, returns `(samples, step)`\
\
**Guides and examples using `linspace`**\
\
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4715)\
\
### `log` function\
\
Copied!\
\
`keras.ops.log(x)`\
\
Natural logarithm, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise natural logarithm of `x`.\
\
**Guides and examples using `log`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4743)\
\
### `log10` function\
\
Copied!\
\
`keras.ops.log10(x)`\
\
Return the base 10 logarithm of the input tensor, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise base 10 logarithm of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4772)\
\
### `log1p` function\
\
Copied!\
\
`keras.ops.log1p(x)`\
\
Returns the natural logarithm of one plus the `x`, element-wise.\
\
Calculates `log(1 + x)`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise natural logarithm of `1 + x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4802)\
\
### `log2` function\
\
Copied!\
\
`keras.ops.log2(x)`\
\
Base-2 logarithm of `x`, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise base-2 logarithm of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4833)\
\
### `logaddexp` function\
\
Copied!\
\
`keras.ops.logaddexp(x1, x2)`\
\
Logarithm of the sum of exponentiations of the inputs.\
\
Calculates `log(exp(x1) + exp(x2))`.\
\
**Arguments**\
\
*   **x1**: Input tensor.\
*   **x2**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise logarithm of the sum of exponentiations of the inputs.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4868)\
\
### `logaddexp2` function\
\
Copied!\
\
`keras.ops.logaddexp2(x1, x2)`\
\
Base-2 logarithm of the sum of exponentiations of the inputs.\
\
Calculates `log2(2**x1 + 2**x2)`.\
\
**Arguments**\
\
*   **x1**: Input tensor.\
*   **x2**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise log base 2 of the sum of 2**x1 and 2**x2.\
\
**Example**\
\
Copied!\
\
`>>> from keras import ops >>> x1 = ops.array([1, 2, 3]) >>> x2 = ops.array([1, 2, 3]) >>> ops.logaddexp2(x1, x2) array([2., 3., 4.], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4904)\
\
### `logical_and` function\
\
Copied!\
\
`keras.ops.logical_and(x1, x2)`\
\
Computes the element-wise logical AND of the given input tensors.\
\
Zeros are treated as `False` and non-zeros are treated as `True`.\
\
**Arguments**\
\
*   **x1**: Input tensor.\
*   **x2**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise logical AND of the inputs.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4935)\
\
### `logical_not` function\
\
Copied!\
\
`keras.ops.logical_not(x)`\
\
Computes the element-wise NOT of the given input tensor.\
\
Zeros are treated as `False` and non-zeros are treated as `True`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise logical NOT of the input.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4968)\
\
### `logical_or` function\
\
Copied!\
\
`keras.ops.logical_or(x1, x2)`\
\
Computes the element-wise logical OR of the given input tensors.\
\
Zeros are treated as `False` and non-zeros are treated as `True`.\
\
**Arguments**\
\
*   **x1**: Input tensor.\
*   **x2**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise logical OR of the inputs.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9353)\
\
### `logical_xor` function\
\
Copied!\
\
`keras.ops.logical_xor(x1, x2)`\
\
Compute the truth value of `x1 XOR x2`, element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output boolean tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5029)\
\
### `logspace` function\
\
Copied!\
\
`keras.ops.logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0)`\
\
Returns numbers spaced evenly on a log scale.\
\
In linear space, the sequence starts at `base ** start` and ends with `base ** stop` (see `endpoint` below).\
\
**Arguments**\
\
*   **start**: The starting value of the sequence.\
*   **stop**: The final value of the sequence, unless `endpoint` is `False`. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length `num`) are returned.\
*   **num**: Number of samples to generate. Defaults to `50`.\
*   **endpoint**: If `True`, `stop` is the last sample. Otherwise, it is not included. Defaults to `True`.\
*   **base**: The base of the log space. Defaults to `10`.\
*   **dtype**: The type of the output tensor.\
*   **axis**: The axis in the result to store the samples. Relevant only if start or stop are array-like.\
\
Note: Torch backend does not support `axis` argument.\
\
**Returns**\
\
A tensor of evenly spaced samples on a log scale.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5092)\
\
### `matmul` function\
\
Copied!\
\
`keras.ops.matmul(x1, x2)`\
\
Matrix product of two tensors.\
\
*   If both tensors are 1-dimensional, the dot product (scalar) is returned.\
*   If either tensor is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly.\
*   If the first tensor is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed.\
*   If the second tensor is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed.\
\
**Arguments**\
\
*   **x1**: First tensor.\
*   **x2**: Second tensor.\
\
**Returns**\
\
Output tensor, matrix product of the inputs.\
\
**Guides and examples using `matmul`**\
\
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)\
    \
*   [Migrating Keras 2 code to Keras 3](https://keras.io/guides/migrating_to_keras_3/)\
    \
*   [Define a Custom TPU/GPU Kernel](https://keras.io/guides/define_custom_kernel/)\
    \
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)\
    \
*   [Sequential retrieval \[GRU4Rec\]](https://keras.io/keras_rs/examples/sequential_retrieval/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5139)\
\
### `max` function\
\
Copied!\
\
`keras.ops.max(x, axis=None, keepdims=False, initial=None)`\
\
Return the maximum of a tensor or maximum along an axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which to operate. By default, flattened input is used.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
*   **initial**: The minimum value of an output element. Defaults to `None`.\
\
**Returns**\
\
Maximum of `x`.\
\
**Guides and examples using `max`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5181)\
\
### `maximum` function\
\
Copied!\
\
`keras.ops.maximum(x1, x2)`\
\
Element-wise maximum of `x1` and `x2`.\
\
**Arguments**\
\
*   **x1**: First tensor.\
*   **x2**: Second tensor.\
\
**Returns**\
\
Output tensor, element-wise maximum of `x1` and `x2`.\
\
**Guides and examples using `maximum`**\
\
*   [Semantic Similarity with KerasHub](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9076)\
\
### `mean` function\
\
Copied!\
\
`keras.ops.mean(x, axis=None, keepdims=False)`\
\
Compute the arithmetic mean along the specified axes.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the means are computed. The default is to compute the mean of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the mean values.\
\
**Guides and examples using `mean`**\
\
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)\
    \
*   [8-bit integer quantization in Keras](https://keras.io/guides/int8_quantization_in_keras/)\
    \
*   [4-bit integer quantization in Keras](https://keras.io/guides/int4_quantization_in_keras/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
*   [Deep Deterministic Policy Gradient (DDPG)](https://keras.io/examples/rl/ddpg_pendulum/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5265)\
\
### `median` function\
\
Copied!\
\
`keras.ops.median(x, axis=None, keepdims=False)`\
\
Compute the median along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the medians are computed. Defaults to `axis=None` which is to compute the median(s) along a flattened version of the array.\
*   **keepdims**: If this is set to `True`, the axes which are reduce are left in the result as dimensions with size one.\
\
**Returns**\
\
The output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5319)\
\
### `meshgrid` function\
\
Copied!\
\
`keras.ops.meshgrid(*x, indexing="xy")`\
\
Creates grids of coordinates from coordinate vectors.\
\
Given `N` 1-D tensors `T0, T1, ..., TN-1` as inputs with corresponding lengths `S0, S1, ..., SN-1`, this creates an `N` N-dimensional tensors `G0, G1, ..., GN-1` each with shape `(S0, ..., SN-1)` where the output `Gi` is constructed by expanding `Ti` to the result shape.\
\
**Arguments**\
\
*   **x**: 1-D tensors representing the coordinates of a grid.\
*   **indexing**: `"xy"` or `"ij"`. "xy" is cartesian; `"ij"` is matrix indexing of output. Defaults to `"xy"`.\
\
**Returns**\
\
Sequence of N tensors.\
\
**Example**\
\
Copied!\
\
`>>> from keras.src import ops >>> x = ops.array([1, 2, 3]) >>> y = ops.array([4, 5, 6])`\
\
Copied!\
\
`>>> grid_x, grid_y = ops.meshgrid(x, y, indexing="ij") >>> grid_x array([[1, 1, 1],        [2, 2, 2],        [3, 3, 3]]) >>> grid_y array([[4, 5, 6],        [4, 5, 6],        [4, 5, 6]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5378)\
\
### `min` function\
\
Copied!\
\
`keras.ops.min(x, axis=None, keepdims=False, initial=None)`\
\
Return the minimum of a tensor or minimum along an axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which to operate. By default, flattened input is used.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
*   **initial**: The maximum value of an output element. Defaults to `None`.\
\
**Returns**\
\
Minimum of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5420)\
\
### `minimum` function\
\
Copied!\
\
`keras.ops.minimum(x1, x2)`\
\
Element-wise minimum of `x1` and `x2`.\
\
**Arguments**\
\
*   **x1**: First tensor.\
*   **x2**: Second tensor.\
\
**Returns**\
\
Output tensor, element-wise minimum of `x1` and `x2`.\
\
**Guides and examples using `minimum`**\
\
*   [Semantic Similarity with KerasHub](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/)\
    \
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5499)\
\
### `mod` function\
\
Copied!\
\
`keras.ops.mod(x1, x2)`\
\
Returns the element-wise remainder of division.\
\
**Arguments**\
\
*   **x1**: First tensor.\
*   **x2**: Second tensor.\
\
**Returns**\
\
Output tensor, element-wise remainder of division.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5600)\
\
### `moveaxis` function\
\
Copied!\
\
`keras.ops.moveaxis(x, source, destination)`\
\
Move axes of a tensor to new positions.\
\
Other axes remain in their original order.\
\
**Arguments**\
\
*   **x**: Tensor whose axes should be reordered.\
*   **source**: Original positions of the axes to move. These must be unique.\
*   **destination**: Destinations positions for each of the original axes. These must also be unique.\
\
**Returns**\
\
Tensor with moved axes.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8649)\
\
### `multiply` function\
\
Copied!\
\
`keras.ops.multiply(x1, x2)`\
\
Multiply arguments element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise product of `x1` and `x2`.\
\
**Guides and examples using `multiply`**\
\
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)\
    \
*   [Recommending movies: retrieval](https://keras.io/keras_rs/examples/basic_retrieval/)\
    \
*   [Retrieval with data parallel training](https://keras.io/keras_rs/examples/data_parallel_retrieval/)\
    \
*   [Faster retrieval with Scalable Nearest Neighbours (ScANN)](https://keras.io/keras_rs/examples/scann/)\
    \
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
*   [Deep Recommenders](https://keras.io/keras_rs/examples/deep_recommender/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6504)\
\
### `nan_to_num` function\
\
Copied!\
\
`keras.ops.nan_to_num(x, nan=0.0, posinf=None, neginf=None)`\
\
Replace NaN with zero and infinity with large finite numbers.\
\
**Arguments**\
\
*   **x**: Input data.\
*   **nan**: Optional float or int. Value to replace `NaN` entries with.\
*   **posinf**: Optional float or int. Value to replace positive infinity with.\
*   **neginf**: Optional float or int. Value to replace negative infinity with.\
\
**Returns**\
\
`x`, with non-finite values replaced.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5639)\
\
### `nanargmax` function\
\
Copied!\
\
`keras.ops.nanargmax(x, axis=None, keepdims=False)`\
\
Returns the indices of the maximum values along an axis, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: By default, the index is into the flattened tensor, otherwise along the specified axis.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Tensor of indices. It has the same shape as `x`, with the dimension along `axis` removed. NaN values are ignored when computing the maximum.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 0.0]])`\
\
Copied!\
\
`>>> ops.nanargmax(x) array(2, dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmax(x, axis=0) array([0, 1, 0], dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmax(x, axis=1) array([2, 1], dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmax(x, axis=1, keepdims=True) array([[2],        [1]], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5698)\
\
### `nanargmin` function\
\
Copied!\
\
`keras.ops.nanargmin(x, axis=None, keepdims=False)`\
\
Returns the indices of the minimum values along an axis, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: By default, the index is into the flattened tensor, otherwise along the specified axis.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Tensor of indices. It has the same shape as `x`, with the dimension along `axis` removed. NaN values are ignored when computing the minimum.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 0.0]])`\
\
Copied!\
\
`>>> ops.nanargmin(x) array(5, dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmin(x, axis=0) array([0, 1, 1], dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmin(x, axis=1) array([0, 2], dtype=int32)`\
\
Copied!\
\
`>>> ops.nanargmin(x, axis=1, keepdims=True) array([[0],        [2]], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5829)\
\
### `nancumprod` function\
\
Copied!\
\
`keras.ops.nancumprod(x, axis=None, dtype=None)`\
\
Returns the cumulative product of elements along a given axis, treating NaNs as one.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which the cumulative product is computed. By default the input is flattened.\
*   **dtype**: dtype of returned tensor. Defaults to x.dtype.\
\
**Returns**\
\
Output tensor.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nancumprod(x) array([1., 1., 3., 3., 6., 6.])`\
\
Copied!\
\
`>>> ops.nancumprod(x, axis=1) array([[1., 1., 3.],        [1., 2., 2.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5768)\
\
### `nancumsum` function\
\
Copied!\
\
`keras.ops.nancumsum(x, axis=None, dtype=None)`\
\
Returns the cumulative sum of elements along a given axis, treating NaNs as zero.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which the cumulative sum is computed. By default the input is flattened.\
*   **dtype**: dtype of returned tensor. Defaults to x.dtype.\
\
**Returns**\
\
Output tensor.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nancumsum(x) array([1., 1., 4., 4., 6., 7.])`\
\
Copied!\
\
`>>> ops.nancumsum(x, axis=1) array([[1., 1., 4.],        [0., 2., 3.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5881)\
\
### `nanmax` function\
\
Copied!\
\
`keras.ops.nanmax(x, axis=None, keepdims=False)`\
\
Maximum of a tensor over the given axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the maximum is computed. The default is to compute the maximum of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Output tensor containing the maximum, with NaN values ignored. If all values along a reduced axis are NaN, the result is NaN.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nanmax(x) 3.0`\
\
Copied!\
\
`>>> ops.nanmax(x, axis=1) array([3., 2.])`\
\
Copied!\
\
`>>> ops.nanmax(x, axis=1, keepdims=True) array([[3.],        [2.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5934)\
\
### `nanmean` function\
\
Copied!\
\
`keras.ops.nanmean(x, axis=None, keepdims=False)`\
\
Mean of a tensor over the given axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the mean is computed. The default is to compute the mean of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Output tensor containing the mean, with NaN values ignored. If all values along a reduced axis are NaN, the result is NaN.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nanmean(x) 1.75`\
\
Copied!\
\
`>>> ops.nanmean(x, axis=1) array([2., 1.5])`\
\
Copied!\
\
`>>> ops.nanmean(x, axis=1, keepdims=True) array([[2. ],        [1.5]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5990)\
\
### `nanmedian` function\
\
Copied!\
\
`keras.ops.nanmedian(x, axis=None, keepdims=False)`\
\
Median of a tensor over the given axes, ignoring NaNs.\
\
This function computes the median along the specified axis or axes, skipping any NaN values. If all values along a reduced axis are NaN, the result is NaN.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the median is computed. If None (default), the median of the flattened tensor is returned.\
*   **keepdims**: If True, the reduced axes are retained as dimensions with size one. Defaults to False.\
\
**Returns**\
\
Tensor with the median values, ignoring NaNs.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nanmedian(x) 1.5`\
\
Copied!\
\
`>>> ops.nanmedian(x, axis=1) array([2., 1.5])`\
\
Copied!\
\
`>>> ops.nanmedian(x, axis=1, keepdims=True) array([[2. ],        [1.5]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6050)\
\
### `nanmin` function\
\
Copied!\
\
`keras.ops.nanmin(x, axis=None, keepdims=False)`\
\
Minimum of a tensor over the given axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the minimum is computed. The default is to compute the minimum of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the minimum, with NaN values ignored. If all values along a reduced axis are NaN, the result is NaN.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nanmin(x) 1.0`\
\
Copied!\
\
`>>> ops.nanmin(x, axis=1) array([1., 1.])`\
\
Copied!\
\
`>>> ops.nanmin(x, axis=1, keepdims=True) array([[1.],        [1.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6118)\
\
### `nanpercentile` function\
\
Copied!\
\
`keras.ops.nanpercentile(x, q, axis=None, method="linear", keepdims=False)`\
\
Compute the q-th percentile(s) of the data along the specified axis, while ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **q**: Percentile or sequence of percentiles to compute. Values must be between 0 and 100 inclusive.\
*   **axis**: Axis or axes along which the percentiles are computed.\
*   **method**: A string specifies the method to use for estimating the percentile. Available methods are `"linear"`, `"lower"`, `"higher"`, `"midpoint"`, and `"nearest"`. Defaults to `"linear"`. If the desired percentile lies between two data points `i < j`:\
    *   `"linear"`: `i + (j - i) * fraction`, where fraction is the fractional part of the index surrounded by `i` and `j`.\
    *   `"lower"`: `i`.\
    *   `"higher"`: `j`.\
    *   `"midpoint"`: `(i + j) / 2`\
    *   `"nearest"`: `i` or `j`, whichever is nearest.\
*   **keepdims**: If True, reduced axes are kept with size 1.\
\
**Returns**\
\
The percentile(s) ignoring NaNs.\
\
**Examples**\
\
Copied!\
\
`>>> import keras >>> from keras import ops >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.nanpercentile(x, 50) 2.5 >>> x = keras.ops.array([1., 2., float("nan"), 4.]) >>> keras.ops.nanpercentile(x, 50) 2.0 >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.nanpercentile(x, [25, 75]) array([1.75, 3.25]) >>> x = keras.ops.array([[1., 2., float("nan")], ...                      [4., 5., 6.]]) >>> keras.ops.nanpercentile(x, 50, axis=1) array([1.5, 5.0])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6202)\
\
### `nanprod` function\
\
Copied!\
\
`keras.ops.nanprod(x, axis=None, keepdims=False)`\
\
Product of a tensor over the given axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the product is computed. The default is to compute the product of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the product, with NaN values ignored.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nanprod(x) 6.0`\
\
Copied!\
\
`>>> ops.nanprod(x, axis=1) array([3., 2.])`\
\
Copied!\
\
`>>> ops.nanprod(x, axis=1, keepdims=True) array([[3.],        [2.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6268)\
\
### `nanquantile` function\
\
Copied!\
\
`keras.ops.nanquantile(x, q, axis=None, method="linear", keepdims=False)`\
\
Compute the q-th quantile(s) of the data along the specified axis, while ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **q**: Probability or sequence of probabilities for the quantiles to compute. Values must be between 0 and 1 inclusive.\
*   **axis**: Axis or axes along which the quantiles are computed. Defaults to `axis=None` which is to compute the quantile(s) along a flattened version of the array.\
*   **method**: A string specifies the method to use for estimating the quantile. Available methods are `"linear"`, `"lower"`, `"higher"`, `"midpoint"`, and `"nearest"`. Defaults to `"linear"`. If the desired quantile lies between two data points `i < j`:\
    *   `"linear"`: `i + (j - i) * fraction`, where fraction is the fractional part of the index surrounded by `i` and `j`.\
    *   `"lower"`: `i`.\
    *   `"higher"`: `j`.\
    *   `"midpoint"`: `(i + j) / 2`\
    *   `"nearest"`: `i` or `j`, whichever is nearest.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
The quantile(s) ignoring NaNs.\
\
**Examples**\
\
Copied!\
\
`>>> import keras >>> from keras import ops >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.nanquantile(x, 0.5) 2.5 >>> x = keras.ops.array([1., 2., float("nan"), 4.]) >>> keras.ops.nanquantile(x, 0.5) 2.0 >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.nanquantile(x, [0.25, 0.75]) array([1.75, 3.25]) >>> x = keras.ops.array([[1., 2., float("nan")], ...                      [4., 5., 6.]]) >>> keras.ops.nanquantile(x, 0.5, axis=1) array([1.5, 5.0])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6340)\
\
### `nanstd` function\
\
Copied!\
\
`keras.ops.nanstd(x, axis=None, keepdims=False)`\
\
Compute the standard deviation along the specified axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the standard deviation is computed. The default is to compute the std of the flattened tensor.\
*   **keepdims**: If `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Output tensor containing the standard deviation ignoring NaNs.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]])`\
\
Copied!\
\
`>>> ops.nanstd(x) 0.8291562`\
\
Copied!\
\
`>>> ops.nanstd(x, axis=1) array([1. , 0.5])`\
\
Copied!\
\
`>>> ops.nanstd(x, axis=1, keepdims=True) array([[1. ],        [0.5]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6402)\
\
### `nansum` function\
\
Copied!\
\
`keras.ops.nansum(x, axis=None, keepdims=False)`\
\
Sum of a tensor over the given axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the sum is computed. The default is to compute the sum of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the sum, with NaN values ignored.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]]) >>> ops.nansum(x) 7.0`\
\
Copied!\
\
`>>> ops.nansum(x, axis=1) array([4., 3.])`\
\
Copied!\
\
`>>> ops.nansum(x, axis=1, keepdims=True) array([[4.],        [3.]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6453)\
\
### `nanvar` function\
\
Copied!\
\
`keras.ops.nanvar(x, axis=None, keepdims=False)`\
\
Compute the variance along the specified axes, ignoring NaNs.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the variance is computed. The default is to compute the variance of the flattened tensor.\
*   **keepdims**: If `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`.\
\
**Returns**\
\
Output tensor containing the variance ignoring NaNs.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> x = np.array([[1.0, np.nan, 3.0], ...               [np.nan, 2.0, 1.0]])`\
\
Copied!\
\
`>>> ops.nanvar(x) 0.6875`\
\
Copied!\
\
`>>> ops.nanvar(x, axis=1) array([1.  , 0.25])`\
\
Copied!\
\
`>>> ops.nanvar(x, axis=1, keepdims=True) array([[1.  ],        [0.25]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6539)\
\
### `ndim` function\
\
Copied!\
\
`keras.ops.ndim(x)`\
\
Return the number of dimensions of a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The number of dimensions in `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8814)\
\
### `negative` function\
\
Copied!\
\
`keras.ops.negative(x)`\
\
Numerical negative, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, `y = -x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8844)\
\
### `nextafter` function\
\
Copied!\
\
`keras.ops.nextafter(x1, x2)`\
\
Return the next representable floating-point value after `x1` towards `x2`.\
\
This function computes the next floating-point value following `x1` in the direction of `x2`, element-wise.\
\
**Arguments**\
\
*   **x1**: Input tensor whose values will be moved to the next representable floating-point value.\
*   **x2**: Input tensor indicating the direction toward which `x1` is moved.\
\
**Returns**\
\
Output tensor\
\
**Example**\
\
Copied!\
\
`>>> x1 = keras.ops.convert_to_tensor([1.0, 1.0]) >>> x2 = keras.ops.convert_to_tensor([2.0, 0.0]) >>> keras.ops.nextafter(x1, x2) array([1.0000001, 0.99999994], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6564)\
\
### `nonzero` function\
\
Copied!\
\
`keras.ops.nonzero(x)`\
\
Return the indices of the elements that are non-zero.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Indices of elements that are non-zero.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6590)\
\
### `not_equal` function\
\
Copied!\
\
`keras.ops.not_equal(x1, x2)`\
\
Return `(x1 != x2)` element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise comparison of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9266)\
\
### `ones` function\
\
Copied!\
\
`keras.ops.ones(shape, dtype=None)`\
\
Return a new tensor of given shape and type, filled with ones.\
\
**Arguments**\
\
*   **shape**: Shape of the new tensor.\
*   **dtype**: Desired data type of the tensor.\
\
**Returns**\
\
Tensor of ones with the given shape and dtype.\
\
**Guides and examples using `ones`**\
\
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6624)\
\
### `ones_like` function\
\
Copied!\
\
`keras.ops.ones_like(x, dtype=None)`\
\
Return a tensor of ones with the same shape and type of `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **dtype**: Overrides the data type of the result.\
\
**Returns**\
\
A tensor of ones with the same shape and type as `x`.\
\
**Guides and examples using `ones_like`**\
\
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6704)\
\
### `outer` function\
\
Copied!\
\
`keras.ops.outer(x1, x2)`\
\
Compute the outer product of two vectors.\
\
Given two vectors `x1` and `x2`, the outer product is:\
\
Copied!\
\
`out[i, j] = x1[i] * x2[j]`\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Outer product of `x1` and `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6787)\
\
### `pad` function\
\
Copied!\
\
`keras.ops.pad(x, pad_width, mode="constant", constant_values=None)`\
\
Pad a tensor.\
\
**Arguments**\
\
*   **x**: Tensor to pad.\
*   **pad\_width**: Number of values padded to the edges of each axis. `((before_1, after_1), ...(before_N, after_N))` unique pad widths for each axis. `((before, after),)` yields same before and after pad for each axis. `(pad,)` or `int` is a shortcut for `before = after = pad` width for all axes.\
*   **mode**: One of `"constant"`, `"edge"`, `"linear_ramp"`, `"maximum"`, `"mean"`, `"median"`, `"minimum"`, `"reflect"`, `"symmetric"`, `"wrap"`, `"empty"`, `"circular"`. Defaults to `"constant"`.\
*   **constant\_values**: value to pad with if `mode == "constant"`. Defaults to `0`. A `ValueError` is raised if not None and `mode != "constant"`.\
\
Note: Torch backend only supports modes `"constant"`, `"reflect"`, `"symmetric"` and `"circular"`. Only Torch backend supports `"circular"` mode.\
\
Note: Tensorflow backend only supports modes `"constant"`, `"reflect"` and `"symmetric"`.\
\
**Returns**\
\
Padded tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6855)\
\
### `percentile` function\
\
Copied!\
\
`keras.ops.percentile(x, q, axis=None, method="linear", keepdims=False)`\
\
Compute the q-th percentile(s) of the data along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **q**: Percentile or sequence of percentiles to compute. Values must be between 0 and 100 inclusive.\
*   **axis**: Axis or axes along which the percentiles are computed.\
*   **method**: A string specifies the method to use for estimating the percentile. Available methods are `"linear"`, `"lower"`, `"higher"`, `"midpoint"`, and `"nearest"`. Defaults to `"linear"`. If the desired percentile lies between two data points `i < j`:\
    *   `"linear"`: `i + (j - i) * fraction`, where fraction is the fractional part of the index surrounded by `i` and `j`.\
    *   `"lower"`: `i`.\
    *   `"higher"`: `j`.\
    *   `"midpoint"`: `(i + j) / 2`\
    *   `"nearest"`: `i` or `j`, whichever is nearest.\
*   **keepdims**: If True, reduced axes are kept with size 1.\
\
**Returns**\
\
The percentile(s). If `q` is a single percentile and `axis=None`, then the result is a scalar. If multiple percentile levels are given, the first axis of the result corresponds to the percentiles. The other axes are the axes that remain after the reduction of `x`.\
\
**Examples**\
\
Copied!\
\
`>>> import keras >>> from keras import ops >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.percentile(x, 50) 2.5 >>> x = keras.ops.array([1., 2., 3., 4.]) >>> keras.ops.percentile(x, [25, 75]) array([1.75, 3.25]) >>> x = keras.ops.array([[1., 2., 3.], ...                      [4., 5., 6.]]) >>> keras.ops.percentile(x, 50, axis=1) array([2., 5.])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8789)\
\
### `power` function\
\
Copied!\
\
`keras.ops.power(x1, x2)`\
\
First tensor elements raised to powers from second tensor, element-wise.\
\
**Arguments**\
\
*   **x1**: The bases.\
*   **x2**: The exponents.\
\
**Returns**\
\
Output tensor, the bases in `x1` raised to the exponents in `x2`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6945)\
\
### `prod` function\
\
Copied!\
\
`keras.ops.prod(x, axis=None, keepdims=False, dtype=None)`\
\
Return the product of tensor elements over a given axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which a product is performed. The default, `axis=None`, will compute the product of all elements in the input tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduce are left in the result as dimensions with size one.\
*   **dtype**: Data type of the returned tensor.\
\
**Returns**\
\
Product of elements of `x` over the given axis or axes.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6988)\
\
### `ptp` function\
\
Copied!\
\
`keras.ops.ptp(x, axis=None, keepdims=False)`\
\
Return the peak-to-peak (max - min) value of tensor elements over a given axis.\
\
The peak-to-peak value is defined as the difference between the maximum and minimum values along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the peak-to-peak value is computed. The default, `axis=None`, will compute the peak-to-peak value over all elements in the input tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
A tensor containing the peak-to-peak values of `x` over the given axis or axes.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.array([[1., 3., 2.], ...                      [4., 0., 5.]])`\
\
Copied!\
\
`>>> # Peak-to-peak over all elements >>> keras.ops.ptp(x) 5.0`\
\
Copied!\
\
`>>> # Peak-to-peak along axis 1 >>> keras.ops.ptp(x, axis=1) array([2., 5.], dtype=float32)`\
\
Copied!\
\
`>>> # Peak-to-peak over multiple axes >>> x = keras.ops.reshape(x, (1, 2, 3)) >>> keras.ops.ptp(x, axis=(1, 2)) array([5.], dtype=float32)`\
\
Copied!\
\
`>>> # Keep reduced dimensions >>> keras.ops.ptp(x, axis=2, keepdims=True) array([[[2.],         [5.]]], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7067)\
\
### `quantile` function\
\
Copied!\
\
`keras.ops.quantile(x, q, axis=None, method="linear", keepdims=False)`\
\
Compute the q-th quantile(s) of the data along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **q**: Probability or sequence of probabilities for the quantiles to compute. Values must be between 0 and 1 inclusive.\
*   **axis**: Axis or axes along which the quantiles are computed. Defaults to `axis=None` which is to compute the quantile(s) along a flattened version of the array.\
*   **method**: A string specifies the method to use for estimating the quantile. Available methods are `"linear"`, `"lower"`, `"higher"`, `"midpoint"`, and `"nearest"`. Defaults to `"linear"`. If the desired quantile lies between two data points `i < j`:\
    *   `"linear"`: `i + (j - i) * fraction`, where fraction is the fractional part of the index surrounded by `i` and `j`.\
    *   `"lower"`: `i`.\
    *   `"higher"`: `j`.\
    *   `"midpoint"`: `(i + j) / 2`\
    *   `"nearest"`: `i` or `j`, whichever is nearest.\
*   **keepdims**: If this is set to `True`, the axes which are reduce are left in the result as dimensions with size one.\
\
**Returns**\
\
The quantile(s). If `q` is a single probability and `axis=None`, then the result is a scalar. If multiple probabilities levels are given, first axis of the result corresponds to the quantiles. The other axes are the axes that remain after the reduction of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2540)\
\
### `rad2deg` function\
\
Copied!\
\
`keras.ops.rad2deg(x)`\
\
Convert angles from radians to degrees.\
\
The conversion is defined as: `deg = rad * (180 / π)`\
\
**Arguments**\
\
*   **x**: Input tensor of angles in radians.\
\
**Returns**\
\
A tensor containing angles converted to degrees.\
\
**Examples**\
\
Copied!\
\
`>>> from keras import ops >>> ops.rad2deg(3.141592653589793) 180.0 >>> ops.rad2deg([0.0, 1.57079633, 3.14159265]) array([0., 90., 180.])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7118)\
\
### `ravel` function\
\
Copied!\
\
`keras.ops.ravel(x)`\
\
Return a contiguous flattened tensor.\
\
A 1-D tensor, containing the elements of the input, is returned.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7195)\
\
### `real` function\
\
Copied!\
\
`keras.ops.real(x)`\
\
Return the real part of the complex argument.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The real component of the complex argument.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7218)\
\
### `reciprocal` function\
\
Copied!\
\
`keras.ops.reciprocal(x)`\
\
Return the reciprocal of the argument, element-wise.\
\
Calculates `1/x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, element-wise reciprocal of `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7292)\
\
### `repeat` function\
\
Copied!\
\
`keras.ops.repeat(x, repeats, axis=None)`\
\
Repeat each element of a tensor after themselves.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **repeats**: The number of repetitions for each element.\
*   **axis**: The axis along which to repeat values. By default, use the flattened input array, and return a flat output array.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7326)\
\
### `reshape` function\
\
Copied!\
\
`keras.ops.reshape(x, newshape)`\
\
Gives a new shape to a tensor without changing its data.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **newshape**: The new shape should be compatible with the original shape. One shape dimension can be -1 in which case the value is inferred from the length of the array and remaining dimensions.\
\
**Returns**\
\
The reshaped tensor.\
\
**Guides and examples using `reshape`**\
\
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)\
    \
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
*   [MixUp augmentation for image classification](https://keras.io/examples/vision/mixup/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Multimodal entailment](https://keras.io/examples/nlp/multimodal_entailment/)\
    \
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
*   [Rank movies with DLRM using KerasRS](https://keras.io/keras_rs/examples/dlrm/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1873)\
\
### `right_shift` function\
\
Copied!\
\
`keras.ops.right_shift(x, y)`\
\
Shift the bits of an integer to the right.\
\
Bits are shifted to the right `y`. Because the internal representation of numbers is in binary format, this operation is equivalent to dividing `x` by `2**y`.\
\
**Arguments**\
\
*   **x**: Input integer tensor.\
*   **y**: Input integer tensor.\
\
**Returns**\
\
Result tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7367)\
\
### `roll` function\
\
Copied!\
\
`keras.ops.roll(x, shift, axis=None)`\
\
Roll tensor elements along a given axis.\
\
Elements that roll beyond the last position are re-introduced at the first.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **shift**: The number of places by which elements are shifted.\
*   **axis**: The axis along which elements are shifted. By default, the array is flattened before shifting, after which the original shape is restored.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L50)\
\
### `rot90` function\
\
Copied!\
\
`keras.ops.rot90(array, k=1, axes=(0, 1))`\
\
Rotate an array by 90 degrees in the plane specified by axes.\
\
This function rotates an array counterclockwise by 90 degrees `k` times in the plane specified by `axes`. Supports arrays of two or more dimensions.\
\
**Arguments**\
\
*   **array**: Input array to rotate.\
*   **k**: Number of times the array is rotated by 90 degrees.\
*   **axes**: A tuple of two integers specifying the plane of rotation (defaults to `(0, 1)`).\
\
**Returns**\
\
Rotated array.\
\
**Examples**\
\
Copied!\
\
`>>> import numpy as np >>> from keras import ops >>> m = np.array([[1, 2], [3, 4]]) >>> rotated = ops.rot90(m) >>> rotated array([[2, 4],        [1, 3]])`\
\
Copied!\
\
`>>> m = np.arange(8).reshape((2, 2, 2)) >>> rotated = ops.rot90(m, k=1, axes=(1, 2)) >>> rotated array([[[1, 3],         [0, 2]],        [[5, 7],         [4, 6]]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7401)\
\
### `round` function\
\
Copied!\
\
`keras.ops.round(x, decimals=0)`\
\
Evenly round to the given number of decimals.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **decimals**: Number of decimal places to round to. Defaults to `0`.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7445)\
\
### `searchsorted` function\
\
Copied!\
\
`keras.ops.searchsorted(sorted_sequence, values, side="left")`\
\
Perform a binary search, returning indices for insertion of `values` into `sorted_sequence` that maintain the sorting order.\
\
**Arguments**\
\
*   **sorted\_sequence**: 1-D input tensor, sorted along the innermost dimension.\
*   **values**: N-D tensor of query insertion values.\
*   **side**: 'left' or 'right', specifying the direction in which to insert for the equality case (tie-breaker).\
\
**Returns**\
\
Tensor of insertion indices of same shape as `values`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9483)\
\
### `select` function\
\
Copied!\
\
`keras.ops.select(condlist, choicelist, default=0)`\
\
Return elements from `choicelist`, based on conditions in `condlist`.\
\
**Arguments**\
\
*   **condlist**: List of boolean tensors. The list of conditions which determine from which array in choicelist the output elements are taken. When multiple conditions are satisfied, the first one encountered in condlist is used.\
*   **choicelist**: List of tensors. The list of tensors from which the output elements are taken. This list has to be of the same length as `condlist`.\
*   **default**: Optional scalar value. The element inserted in the output when all conditions evaluate to `False`.\
\
**Returns**\
\
Tensor where the output at position `m` is the `m`\-th element of the tensor in `choicelist` where the `m`\-th element of the corresponding tensor in `condlist` is `True`.\
\
**Example**\
\
Copied!\
\
`from keras import ops  x = ops.arange(6) condlist = [x<3, x>3] choicelist = [x, x**2] ops.select(condlist, choicelist, 42) # # Returns tensor([0,  1,  2, 42, 16, 25])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7477)\
\
### `sign` function\
\
Copied!\
\
`keras.ops.sign(x)`\
\
Returns a tensor with the signs of the elements of `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7501)\
\
### `signbit` function\
\
Copied!\
\
`keras.ops.signbit(x)`\
\
Return the sign bit of the elements of `x`.\
\
The output boolean tensor contains `True` where the sign of `x` is negative, and `False` otherwise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output boolean tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7533)\
\
### `sin` function\
\
Copied!\
\
`keras.ops.sin(x)`\
\
Trigonometric sine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7561)\
\
### `sinc` function\
\
Copied!\
\
`keras.ops.sinc(x)`\
\
Return the normalized sinc function.\
\
The sinc function is equal to `sin(pi*x) / (pi*x)` for any argument `x != 0`, and `sinc(0)` takes the limit value 1, making `sinc` not just everywhere continuous but also infinitely differentiable.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0]) >>> keras.ops.sinc(x) array([1., 0., 0.], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7599)\
\
### `sinh` function\
\
Copied!\
\
`keras.ops.sinh(x)`\
\
Hyperbolic sine, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7622)\
\
### `size` function\
\
Copied!\
\
`keras.ops.size(x)`\
\
Return the number of elements in a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Number of elements in `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9548)\
\
### `slogdet` function\
\
Copied!\
\
`keras.ops.slogdet(x)`\
\
Compute the sign and natural logarithm of the determinant of a matrix.\
\
**Arguments**\
\
*   **x**: Input matrix. It must 2D and square.\
\
**Returns**\
\
A tuple `(sign, logabsdet)`. `sign` is a number representing the sign of the determinant. For a real matrix, this is 1, 0, or -1. For a complex matrix, this is a complex number with absolute value 1 (i.e., it is on the unit circle), or else 0. `logabsdet` is the natural log of the absolute value of the determinant.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7656)\
\
### `sort` function\
\
Copied!\
\
`keras.ops.sort(x, axis=-1)`\
\
Sorts the elements of `x` along a given axis in ascending order.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which to sort. If `None`, the tensor is flattened before sorting. Defaults to `-1`; the last axis.\
\
**Returns**\
\
Sorted tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7734)\
\
### `split` function\
\
Copied!\
\
`keras.ops.split(x, indices_or_sections, axis=0)`\
\
Split a tensor into chunks.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **indices\_or\_sections**: If an integer, N, the tensor will be split into N equal sections along `axis`. If a 1-D array of sorted integers, the entries indicate indices at which the tensor will be split along `axis`.\
*   **axis**: Axis along which to split. Defaults to `0`.\
\
Note: A split does not have to result in equal division when using Torch backend.\
\
**Returns**\
\
A list of tensors.\
\
**Guides and examples using `split`**\
\
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8914)\
\
### `sqrt` function\
\
Copied!\
\
`keras.ops.sqrt(x)`\
\
Return the non-negative square root of a tensor, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, the non-negative square root of `x`.\
\
**Guides and examples using `sqrt`**\
\
*   [CutMix data augmentation for image classification](https://keras.io/examples/vision/cutmix/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [Neural Style Transfer with AdaIN](https://keras.io/examples/generative/adain/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8884)\
\
### `square` function\
\
Copied!\
\
`keras.ops.square(x)`\
\
Return the element-wise square of the input.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor, the square of `x`.\
\
**Guides and examples using `square`**\
\
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)\
    \
*   [8-bit integer quantization in Keras](https://keras.io/guides/int8_quantization_in_keras/)\
    \
*   [4-bit integer quantization in Keras](https://keras.io/guides/int4_quantization_in_keras/)\
    \
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
*   [Deep Deterministic Policy Gradient (DDPG)](https://keras.io/examples/rl/ddpg_pendulum/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8958)\
\
### `squeeze` function\
\
Copied!\
\
`keras.ops.squeeze(x, axis=None)`\
\
Remove axes of length one from `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Select a subset of the entries of length one in the shape.\
\
**Returns**\
\
The input tensor with all or a subset of the dimensions of length 1 removed.\
\
**Guides and examples using `squeeze`**\
\
*   [Migrating Keras 2 code to Keras 3](https://keras.io/guides/migrating_to_keras_3/)\
    \
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Video Classification with Transformers](https://keras.io/examples/vision/video_transformers/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)\
    \
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
*   [Deep Deterministic Policy Gradient (DDPG)](https://keras.io/examples/rl/ddpg_pendulum/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7788)\
\
### `stack` function\
\
Copied!\
\
`keras.ops.stack(x, axis=0)`\
\
Join a sequence of tensors along a new axis.\
\
The `axis` parameter specifies the index of the new axis in the dimensions of the result.\
\
**Arguments**\
\
*   **x**: A sequence of tensors.\
*   **axis**: Axis along which to stack. Defaults to `0`.\
\
**Returns**\
\
The stacked tensor.\
\
**Guides and examples using `stack`**\
\
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7829)\
\
### `std` function\
\
Copied!\
\
`keras.ops.std(x, axis=None, keepdims=False)`\
\
Compute the standard deviation along the specified axis.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis along which to compute standard deviation. Default is to compute the standard deviation of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the standard deviation values.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8615)\
\
### `subtract` function\
\
Copied!\
\
`keras.ops.subtract(x1, x2)`\
\
Subtract arguments element-wise.\
\
**Arguments**\
\
*   **x1**: First input tensor.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor, element-wise difference of `x1` and `x2`.\
\
**Guides and examples using `subtract`**\
\
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9233)\
\
### `sum` function\
\
Copied!\
\
`keras.ops.sum(x, axis=None, keepdims=False)`\
\
Sum of a tensor over the given axes.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the sum is computed. The default is to compute the sum of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the sum.\
\
**Guides and examples using `sum`**\
\
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)\
    \
*   [Migrating Keras 2 code to Keras 3](https://keras.io/guides/migrating_to_keras_3/)\
    \
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [End-to-end Masked Language Modeling with BERT](https://keras.io/examples/nlp/masked_language_modeling/)\
    \
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7868)\
\
### `swapaxes` function\
\
Copied!\
\
`keras.ops.swapaxes(x, axis1, axis2)`\
\
Interchange two axes of a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis1**: First axis.\
*   **axis2**: Second axis.\
\
**Returns**\
\
A tensor with the axes swapped.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7909)\
\
### `take` function\
\
Copied!\
\
`keras.ops.take(x, indices, axis=None)`\
\
Take elements from a tensor along an axis.\
\
**Arguments**\
\
*   **x**: Source tensor.\
*   **indices**: The indices of the values to extract.\
*   **axis**: The axis over which to select values. By default, the flattened input tensor is used.\
\
**Returns**\
\
The corresponding tensor of values.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7942)\
\
### `take_along_axis` function\
\
Copied!\
\
`keras.ops.take_along_axis(x, indices, axis=None)`\
\
Select values from `x` at the 1-D `indices` along the given axis.\
\
**Arguments**\
\
*   **x**: Source tensor.\
*   **indices**: The indices of the values to extract.\
*   **axis**: The axis over which to select values. By default, the flattened input tensor is used.\
\
**Returns**\
\
The corresponding tensor of values.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7979)\
\
### `tan` function\
\
Copied!\
\
`keras.ops.tan(x)`\
\
Compute tangent, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8008)\
\
### `tanh` function\
\
Copied!\
\
`keras.ops.tanh(x)`\
\
Hyperbolic tangent, element-wise.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
Output tensor of same shape as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8068)\
\
### `tensordot` function\
\
Copied!\
\
`keras.ops.tensordot(x1, x2, axes=2)`\
\
Compute the tensor dot product along specified axes.\
\
**Arguments**\
\
*   **x1**: First tensor.\
*   **x2**: Second tensor.\
*   **axes**: - If an integer, N, sum over the last N axes of `x1` and the first N axes of `x2` in order. The sizes of the corresponding axes must match. - Or, a list of axes to be summed over, first sequence applying to `x1`, second to `x2`. Both sequences must be of the same length.\
\
**Returns**\
\
The tensor dot product of the inputs.\
\
**Guides and examples using `tensordot`**\
\
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8120)\
\
### `tile` function\
\
Copied!\
\
`keras.ops.tile(x, repeats)`\
\
Repeat `x` the number of times given by `repeats`.\
\
If `repeats` has length `d`, the result will have dimension of `max(d, x.ndim)`.\
\
If `x.ndim < d`, `x` is promoted to be d-dimensional by prepending new axes.\
\
If `x.ndim > d`, `repeats` is promoted to `x.ndim` by prepending 1's to it.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **repeats**: The number of repetitions of `x` along each axis.\
\
**Returns**\
\
The tiled output tensor.\
\
**Guides and examples using `tile`**\
\
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)\
    \
*   [Semantic Image Clustering](https://keras.io/examples/vision/semantic_image_clustering/)\
    \
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8181)\
\
### `trace` function\
\
Copied!\
\
`keras.ops.trace(x, offset=0, axis1=0, axis2=1)`\
\
Return the sum along diagonals of the tensor.\
\
If `x` is 2-D, the sum along its diagonal with the given offset is returned, i.e., the sum of elements `x[i, i+offset]` for all `i`.\
\
If a has more than two dimensions, then the axes specified by `axis1` and `axis2` are used to determine the 2-D sub-arrays whose traces are returned.\
\
The shape of the resulting tensor is the same as that of `x` with `axis1` and `axis2` removed.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **offset**: Offset of the diagonal from the main diagonal. Can be both positive and negative. Defaults to `0`.\
*   **axis1**: Axis to be used as the first axis of the 2-D sub-arrays. Defaults to `0`.(first axis).\
*   **axis2**: Axis to be used as the second axis of the 2-D sub-arrays. Defaults to `1` (second axis).\
\
**Returns**\
\
If `x` is 2-D, the sum of the diagonal is returned. If `x` has larger dimensions, then a tensor of sums along diagonals is returned.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9026)\
\
### `trapezoid` function\
\
Copied!\
\
`keras.ops.trapezoid(y, x=None, dx=1.0, axis=-1)`\
\
Integrate along the given axis using the composite trapezoidal rule.\
\
**Arguments**\
\
*   **y**: Input tensor.\
*   **x**: Optional tensor specifying sample points corresponding to `y`. If `None`, spacing is assumed to be `dx`.\
*   **dx**: Spacing between sample points when `x` is `None`.\
*   **axis**: Axis along which to integrate. Default is the last axis.\
\
**Returns**\
\
The approximate integral of `y` along the given axis.\
\
**Example**\
\
Copied!\
\
`>>> y = keras.ops.convert_to_tensor([[1, 2, 3], [4, 5, 6]]) >>> keras.ops.trapezoid(y, axis=1) array([ 4., 10.], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8991)\
\
### `transpose` function\
\
Copied!\
\
`keras.ops.transpose(x, axes=None)`\
\
Returns a tensor with `axes` transposed.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axes**: Sequence of integers. Permutation of the dimensions of `x`. By default, the order of the axes are reversed.\
\
**Returns**\
\
`x` with its axes permuted.\
\
**Guides and examples using `transpose`**\
\
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)\
    \
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)\
    \
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)\
    \
*   [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)\
    \
*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)\
    \
*   [Sequential retrieval \[GRU4Rec\]](https://keras.io/keras_rs/examples/sequential_retrieval/)\
    \
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8214)\
\
### `tri` function\
\
Copied!\
\
`keras.ops.tri(N, M=None, k=0, dtype=None)`\
\
Return a tensor with ones at and below a diagonal and zeros elsewhere.\
\
**Arguments**\
\
*   **N**: Number of rows in the tensor.\
*   **M**: Number of columns in the tensor.\
*   **k**: The sub-diagonal at and below which the array is filled. `k = 0` is the main diagonal, while `k < 0` is below it, and `k > 0` is above. The default is 0.\
*   **dtype**: Data type of the returned tensor. The default is "float32".\
\
**Returns**\
\
Tensor with its lower triangle filled with ones and zeros elsewhere. `T[i, j] == 1` for `j <= i + k`, 0 otherwise.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8245)\
\
### `tril` function\
\
Copied!\
\
`keras.ops.tril(x, k=0)`\
\
Return lower triangle of a tensor.\
\
For tensors with `ndim` exceeding 2, `tril` will apply to the final two axes.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **k**: Diagonal above which to zero elements. Defaults to `0`. the main diagonal. `k < 0` is below it, and `k > 0` is above it.\
\
**Returns**\
\
Lower triangle of `x`, of same shape and data type as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8277)\
\
### `triu` function\
\
Copied!\
\
`keras.ops.triu(x, k=0)`\
\
Return upper triangle of a tensor.\
\
For tensors with `ndim` exceeding 2, `triu` will apply to the final two axes.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **k**: Diagonal below which to zero elements. Defaults to `0`. the main diagonal. `k < 0` is below it, and `k > 0` is above it.\
\
**Returns**\
\
Upper triangle of `x`, of same shape and data type as `x`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8762)\
\
### `true_divide` function\
\
Copied!\
\
`keras.ops.true_divide(x1, x2)`\
\
Alias for [`keras.ops.divide`](https://keras.io/api/ops/numpy#divide-function)\
.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8305)\
\
### `trunc` function\
\
Copied!\
\
`keras.ops.trunc(x)`\
\
Return the truncated value of the input, element-wise.\
\
The truncated value of the scalar `x` is the nearest integer `i` which is closer to zero than `x` is. In short, the fractional part of the signed number `x` is discarded.\
\
**Arguments**\
\
*   **x**: Input tensor.\
\
**Returns**\
\
The truncated value of each element in `x`.\
\
**Example**\
\
Copied!\
\
`>>> x = ops.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]) >>> ops.trunc(x) array([-1.0, -1.0, -0.0, 0.0, 1.0, 1.0, 2.0])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9886)\
\
### `unique` function\
\
Copied!\
\
`keras.ops.unique(     x,     sorted=True,     return_index=False,     return_inverse=False,     return_counts=False,     axis=None,     size=None,     fill_value=None, )`\
\
Finds the unique elements of a tensor.\
\
This function returns the unique elements of an array, optionally sorted. When `size` is provided, the output shape is fixed, making it compatible with JIT compilation (e.g., JAX, TensorFlow Graph Mode).\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **sorted**: Whether to sort the unique elements in ascending order. Defaults to `True`.\
*   **return\_index**: If `True`, also return the indices of the first occurrence of each unique element in `x`. Defaults to `False`.\
*   **return\_inverse**: If `True`, also return the indices of the unique tensor (for the specified axis, if provided) that can be used to reconstruct `x`. Defaults to `False`.\
*   **return\_counts**: If `True`, also return the number of times each unique item appears in `x`. Defaults to `False`.\
*   **axis**: The axis to operate on. If `None`, `x` will be flattened. If an integer, the subarrays indexed by the given axis will be treated as the elements. Defaults to `None`.\
*   **size**: Optional integer. If provided, the output will always have this fixed size. If the number of unique elements is less than `size`, the output will be padded with `fill_value`. If greater, the output will be truncated.\
*   **fill\_value**: The value used to pad the output when `size` is specified and there are fewer unique elements than `size`. Defaults to `0`.\
\
**Returns**\
\
A tensor or a tuple of tensors. - **\- `unique_values`**: The unique values. Shape is `(size,)` if `size` is provided and `axis=None`. - **\- `unique_index` (optional)**: The indices of the first occurrence of each unique element in `x`. Only provided if `return_index` is `True`. - **\- `unique_inverse` (optional)**: The indices to reconstruct the original array. Only provided if `return_inverse` is `True`. - **\- `unique_counts` (optional)**: The number of occurrences of each unique value. Only provided if `return_counts` is `True`.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([3, 1, 2, 1, 3, 2]) >>> keras.ops.unique(x) array([1, 2, 3], dtype=int32)`\
\
Fixed size output with padding (JIT-compatible):\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([3, 1, 2, 1]) >>> values, counts = keras.ops.unique(x, size=5, fill_value=0, ...                                   return_counts=True) >>> values array([1, 2, 3, 0, 0], dtype=int32) >>> counts array([2, 1, 1, 0, 0], dtype=int32)`\
\
Fixed size output with truncation:\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([3, 1, 2, 1]) >>> keras.ops.unique(x, size=2) array([1, 2], dtype=int32)`\
\
Return unique rows of a 2D array:\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([[1, 0, 0], [0, 1, 0], [1, 0, 0]]) >>> keras.ops.unique(x, axis=0) array([[0, 1, 0],        [1, 0, 0]], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7163)\
\
### `unravel_index` function\
\
Copied!\
\
`keras.ops.unravel_index(indices, shape)`\
\
Convert flat indices to coordinate arrays in a given array shape.\
\
**Arguments**\
\
*   **indices**: An integer or array of integers representing flat indices.\
*   **shape**: The shape of the array to unravel into.\
\
**Returns**\
\
Tuple of arrays for each dimension with unraveled indices.\
\
**Example**\
\
Copied!\
\
`>>> indices = 5 >>> shape = (3, 3) >>> unravel_index(indices, shape) (1, 2)  # 5 is at row 1, column 2 in a 3x3 array`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9114)\
\
### `vander` function\
\
Copied!\
\
`keras.ops.vander(x, N=None, increasing=False)`\
\
Generate a Vandermonde matrix.\
\
**Arguments**\
\
*   **x**: 1D input tensor.\
*   **N**: Number of columns. If `None`, `N` = `len(x)`.\
*   **increasing**: Order of powers. If True, powers increase left to right.\
\
**Returns**\
\
Output tensor, Vandermonde matrix of shape `(len(x), N)`.\
\
**Example**\
\
Copied!\
\
`>>> import numpy as np >>> import keras >>> x = np.array([1, 2, 3, 5]) >>> keras.ops.vander(x) array([[  1,   1,   1,   1],        [  8,   4,   2,   1],        [ 27,   9,   3,   1],        [125,  25,   5,   1]])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9185)\
\
### `var` function\
\
Copied!\
\
`keras.ops.var(x, axis=None, keepdims=False)`\
\
Compute the variance along the specified axes.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **axis**: Axis or axes along which the variance is computed. The default is to compute the variance of the flattened tensor.\
*   **keepdims**: If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one.\
\
**Returns**\
\
Output tensor containing the variance.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8341)\
\
### `vdot` function\
\
Copied!\
\
`keras.ops.vdot(x1, x2)`\
\
Return the dot product of two vectors.\
\
If the first argument is complex, the complex conjugate of the first argument is used for the calculation of the dot product.\
\
Multidimensional tensors are flattened before the dot product is taken.\
\
**Arguments**\
\
*   **x1**: First input tensor. If complex, its complex conjugate is taken before calculation of the dot product.\
*   **x2**: Second input tensor.\
\
**Returns**\
\
Output tensor.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8421)\
\
### `vectorize` function\
\
Copied!\
\
`keras.ops.vectorize(pyfunc, excluded=None, signature=None)`\
\
Turn a function into a vectorized function.\
\
**Example**\
\
Copied!\
\
`def myfunc(a, b):     return a + b  vfunc = keras.ops.vectorize(myfunc) y = vfunc([1, 2, 3, 4], 2)  # Returns Tensor([3, 4, 5, 6])`\
\
**Arguments**\
\
*   **pyfunc**: Callable of a single tensor argument.\
*   **excluded**: Optional set of integers representing positional arguments for which the function will not be vectorized. These will be passed directly to `pyfunc` unmodified.\
*   **signature**: Optional generalized universal function signature, e.g., `"(m,n),(n)->(m)"` for vectorized matrix-vector multiplication. If provided, `pyfunc` will be called with (and expected to return) arrays with shapes given by the size of corresponding core dimensions. By default, `pyfunc` is assumed to take scalars tensors as input and output.\
\
**Returns**\
\
A new function that applies `pyfunc` to every element of its input along axis 0 (the batch axis).\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1271)\
\
### `view` function\
\
Copied!\
\
`keras.ops.view(x, dtype=None)`\
\
Create a new bitwise view of the same data with the specified dtype.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **dtype**: Data-type descriptor of the returned view, e.g., float32 or int16.\
\
**Returns**\
\
View of a tensor with data type dtype.\
\
**Examples**\
\
Copied!\
\
`>>> x = keras.ops.array([1, 2, 3]) >>> x array([1, 2, 3], dtype=int32) >>> keras.ops.view(x, dtype="float32") array([1.0e-45, 3.0e-45, 4.0e-45], dtype=float32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8524)\
\
### `vsplit` function\
\
Copied!\
\
`keras.ops.vsplit(x, indices_or_sections)`\
\
Split an array into multiple sub-arrays vertically (row-wise).\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **indices\_or\_sections**: If an integer, N, the tensor will be split into N equal sections along axis 0. If a 1-D array of sorted integers, the entries indicate indices at which the tensor will be split along axis 0.\
\
**Returns**\
\
A list of sub-arrays.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.arange(12).reshape((4, 3)) >>> keras.ops.vsplit(x, 2) [array([[0, 1, 2],        [3, 4, 5]]),  array([[ 6,  7,  8],        [ 9, 10, 11]])] >>> keras.ops.vsplit(x, [1, 3]) [array([[0, 1, 2]]),  array([[3, 4, 5],        [6, 7, 8]]),  array([[ 9, 10, 11]])]`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8490)\
\
### `vstack` function\
\
Copied!\
\
`keras.ops.vstack(xs)`\
\
Stack tensors in sequence vertically (row wise).\
\
**Arguments**\
\
*   **xs**: Sequence of tensors.\
\
**Returns**\
\
Tensor formed by stacking the given tensors.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8574)\
\
### `where` function\
\
Copied!\
\
`keras.ops.where(condition, x1=None, x2=None)`\
\
Return elements chosen from `x1` or `x2` depending on `condition`.\
\
**Arguments**\
\
*   **condition**: Where `True`, yield `x1`, otherwise yield `x2`.\
*   **x1**: Values from which to choose when `condition` is `True`.\
*   **x2**: Values from which to choose when `condition` is `False`.\
\
**Returns**\
\
A tensor with elements from `x1` where `condition` is `True`, and elements from `x2` where `condition` is `False`.\
\
**Guides and examples using `where`**\
\
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9252)\
\
### `zeros` function\
\
Copied!\
\
`keras.ops.zeros(shape, dtype=None)`\
\
Return a new tensor of given shape and type, filled with zeros.\
\
**Arguments**\
\
*   **shape**: Shape of the new tensor.\
*   **dtype**: Desired data type of the tensor.\
\
**Returns**\
\
Tensor of zeros with the given shape and dtype.\
\
**Guides and examples using `zeros`**\
\
*   [Rank movies with DLRM using KerasRS](https://keras.io/keras_rs/examples/dlrm/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6659)\
\
### `zeros_like` function\
\
Copied!\
\
`keras.ops.zeros_like(x, dtype=None)`\
\
Return a tensor of zeros with the same shape and type as `x`.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **dtype**: Overrides the data type of the result.\
\
**Returns**\
\
A tensor of zeros with the same shape and type as `x`.\
\
**Guides and examples using `zeros_like`**\
\
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)\
    \
\
* * *\
\
[NumPy ops](https://keras.io/api/ops/numpy/#numpy-ops)\
\
[`abs` function](https://keras.io/api/ops/numpy/#abs-function)\
\
[`absolute` function](https://keras.io/api/ops/numpy/#absolute-function)\
\
[`add` function](https://keras.io/api/ops/numpy/#add-function)\
\
[`all` function](https://keras.io/api/ops/numpy/#all-function)\
\
[`allclose` function](https://keras.io/api/ops/numpy/#allclose-function)\
\
[`amax` function](https://keras.io/api/ops/numpy/#amax-function)\
\
[`amin` function](https://keras.io/api/ops/numpy/#amin-function)\
\
[`angle` function](https://keras.io/api/ops/numpy/#angle-function)\
\
[`any` function](https://keras.io/api/ops/numpy/#any-function)\
\
[`append` function](https://keras.io/api/ops/numpy/#append-function)\
\
[`arange` function](https://keras.io/api/ops/numpy/#arange-function)\
\
[`arccos` function](https://keras.io/api/ops/numpy/#arccos-function)\
\
[`arccosh` function](https://keras.io/api/ops/numpy/#arccosh-function)\
\
[`arcsin` function](https://keras.io/api/ops/numpy/#arcsin-function)\
\
[`arcsinh` function](https://keras.io/api/ops/numpy/#arcsinh-function)\
\
[`arctan` function](https://keras.io/api/ops/numpy/#arctan-function)\
\
[`arctan2` function](https://keras.io/api/ops/numpy/#arctan2-function)\
\
[`arctanh` function](https://keras.io/api/ops/numpy/#arctanh-function)\
\
[`argmax` function](https://keras.io/api/ops/numpy/#argmax-function)\
\
[`argmin` function](https://keras.io/api/ops/numpy/#argmin-function)\
\
[`argpartition` function](https://keras.io/api/ops/numpy/#argpartition-function)\
\
[`argsort` function](https://keras.io/api/ops/numpy/#argsort-function)\
\
[`array` function](https://keras.io/api/ops/numpy/#array-function)\
\
[`array_split` function](https://keras.io/api/ops/numpy/#arraysplit-function)\
\
[`average` function](https://keras.io/api/ops/numpy/#average-function)\
\
[`bartlett` function](https://keras.io/api/ops/numpy/#bartlett-function)\
\
[`bincount` function](https://keras.io/api/ops/numpy/#bincount-function)\
\
[`bitwise_and` function](https://keras.io/api/ops/numpy/#bitwiseand-function)\
\
[`bitwise_invert` function](https://keras.io/api/ops/numpy/#bitwiseinvert-function)\
\
[`bitwise_left_shift` function](https://keras.io/api/ops/numpy/#bitwiseleftshift-function)\
\
[`bitwise_not` function](https://keras.io/api/ops/numpy/#bitwisenot-function)\
\
[`bitwise_or` function](https://keras.io/api/ops/numpy/#bitwiseor-function)\
\
[`bitwise_right_shift` function](https://keras.io/api/ops/numpy/#bitwiserightshift-function)\
\
[`bitwise_xor` function](https://keras.io/api/ops/numpy/#bitwisexor-function)\
\
[`blackman` function](https://keras.io/api/ops/numpy/#blackman-function)\
\
[`broadcast_to` function](https://keras.io/api/ops/numpy/#broadcastto-function)\
\
[`cbrt` function](https://keras.io/api/ops/numpy/#cbrt-function)\
\
[`ceil` function](https://keras.io/api/ops/numpy/#ceil-function)\
\
[`clip` function](https://keras.io/api/ops/numpy/#clip-function)\
\
[`concatenate` function](https://keras.io/api/ops/numpy/#concatenate-function)\
\
[`conj` function](https://keras.io/api/ops/numpy/#conj-function)\
\
[`conjugate` function](https://keras.io/api/ops/numpy/#conjugate-function)\
\
[`copy` function](https://keras.io/api/ops/numpy/#copy-function)\
\
[`corrcoef` function](https://keras.io/api/ops/numpy/#corrcoef-function)\
\
[`correlate` function](https://keras.io/api/ops/numpy/#correlate-function)\
\
[`cos` function](https://keras.io/api/ops/numpy/#cos-function)\
\
[`cosh` function](https://keras.io/api/ops/numpy/#cosh-function)\
\
[`count_nonzero` function](https://keras.io/api/ops/numpy/#countnonzero-function)\
\
[`cross` function](https://keras.io/api/ops/numpy/#cross-function)\
\
[`cumprod` function](https://keras.io/api/ops/numpy/#cumprod-function)\
\
[`cumsum` function](https://keras.io/api/ops/numpy/#cumsum-function)\
\
[`deg2rad` function](https://keras.io/api/ops/numpy/#deg2rad-function)\
\
[`diag` function](https://keras.io/api/ops/numpy/#diag-function)\
\
[`diagflat` function](https://keras.io/api/ops/numpy/#diagflat-function)\
\
[`diagonal` function](https://keras.io/api/ops/numpy/#diagonal-function)\
\
[`diff` function](https://keras.io/api/ops/numpy/#diff-function)\
\
[`digitize` function](https://keras.io/api/ops/numpy/#digitize-function)\
\
[`divide` function](https://keras.io/api/ops/numpy/#divide-function)\
\
[`divide_no_nan` function](https://keras.io/api/ops/numpy/#dividenonan-function)\
\
[`dot` function](https://keras.io/api/ops/numpy/#dot-function)\
\
[`dstack` function](https://keras.io/api/ops/numpy/#dstack-function)\
\
[`einsum` function](https://keras.io/api/ops/numpy/#einsum-function)\
\
[`empty` function](https://keras.io/api/ops/numpy/#empty-function)\
\
[`empty_like` function](https://keras.io/api/ops/numpy/#emptylike-function)\
\
[`equal` function](https://keras.io/api/ops/numpy/#equal-function)\
\
[`exp` function](https://keras.io/api/ops/numpy/#exp-function)\
\
[`exp2` function](https://keras.io/api/ops/numpy/#exp2-function)\
\
[`expand_dims` function](https://keras.io/api/ops/numpy/#expanddims-function)\
\
[`expm1` function](https://keras.io/api/ops/numpy/#expm1-function)\
\
[`eye` function](https://keras.io/api/ops/numpy/#eye-function)\
\
[`fabs` function](https://keras.io/api/ops/numpy/#fabs-function)\
\
[`flip` function](https://keras.io/api/ops/numpy/#flip-function)\
\
[`fliplr` function](https://keras.io/api/ops/numpy/#fliplr-function)\
\
[`flipud` function](https://keras.io/api/ops/numpy/#flipud-function)\
\
[`floor` function](https://keras.io/api/ops/numpy/#floor-function)\
\
[`floor_divide` function](https://keras.io/api/ops/numpy/#floordivide-function)\
\
[`fmax` function](https://keras.io/api/ops/numpy/#fmax-function)\
\
[`fmin` function](https://keras.io/api/ops/numpy/#fmin-function)\
\
[`fmod` function](https://keras.io/api/ops/numpy/#fmod-function)\
\
[`full` function](https://keras.io/api/ops/numpy/#full-function)\
\
[`full_like` function](https://keras.io/api/ops/numpy/#fulllike-function)\
\
[`gcd` function](https://keras.io/api/ops/numpy/#gcd-function)\
\
[`geomspace` function](https://keras.io/api/ops/numpy/#geomspace-function)\
\
[`get_item` function](https://keras.io/api/ops/numpy/#getitem-function)\
\
[`greater` function](https://keras.io/api/ops/numpy/#greater-function)\
\
[`greater_equal` function](https://keras.io/api/ops/numpy/#greaterequal-function)\
\
[`hamming` function](https://keras.io/api/ops/numpy/#hamming-function)\
\
[`hanning` function](https://keras.io/api/ops/numpy/#hanning-function)\
\
[`heaviside` function](https://keras.io/api/ops/numpy/#heaviside-function)\
\
[`histogram` function](https://keras.io/api/ops/numpy/#histogram-function)\
\
[`hsplit` function](https://keras.io/api/ops/numpy/#hsplit-function)\
\
[`hstack` function](https://keras.io/api/ops/numpy/#hstack-function)\
\
[`hypot` function](https://keras.io/api/ops/numpy/#hypot-function)\
\
[`i0` function](https://keras.io/api/ops/numpy/#i0-function)\
\
[`identity` function](https://keras.io/api/ops/numpy/#identity-function)\
\
[`imag` function](https://keras.io/api/ops/numpy/#imag-function)\
\
[`inner` function](https://keras.io/api/ops/numpy/#inner-function)\
\
[`isclose` function](https://keras.io/api/ops/numpy/#isclose-function)\
\
[`isfinite` function](https://keras.io/api/ops/numpy/#isfinite-function)\
\
[`isinf` function](https://keras.io/api/ops/numpy/#isinf-function)\
\
[`isin` function](https://keras.io/api/ops/numpy/#isin-function)\
\
[`isnan` function](https://keras.io/api/ops/numpy/#isnan-function)\
\
[`isneginf` function](https://keras.io/api/ops/numpy/#isneginf-function)\
\
[`isposinf` function](https://keras.io/api/ops/numpy/#isposinf-function)\
\
[`isreal` function](https://keras.io/api/ops/numpy/#isreal-function)\
\
[`kaiser` function](https://keras.io/api/ops/numpy/#kaiser-function)\
\
[`kron` function](https://keras.io/api/ops/numpy/#kron-function)\
\
[`lcm` function](https://keras.io/api/ops/numpy/#lcm-function)\
\
[`ldexp` function](https://keras.io/api/ops/numpy/#ldexp-function)\
\
[`left_shift` function](https://keras.io/api/ops/numpy/#leftshift-function)\
\
[`less` function](https://keras.io/api/ops/numpy/#less-function)\
\
[`less_equal` function](https://keras.io/api/ops/numpy/#lessequal-function)\
\
[`linspace` function](https://keras.io/api/ops/numpy/#linspace-function)\
\
[`log` function](https://keras.io/api/ops/numpy/#log-function)\
\
[`log10` function](https://keras.io/api/ops/numpy/#log10-function)\
\
[`log1p` function](https://keras.io/api/ops/numpy/#log1p-function)\
\
[`log2` function](https://keras.io/api/ops/numpy/#log2-function)\
\
[`logaddexp` function](https://keras.io/api/ops/numpy/#logaddexp-function)\
\
[`logaddexp2` function](https://keras.io/api/ops/numpy/#logaddexp2-function)\
\
[`logical_and` function](https://keras.io/api/ops/numpy/#logicaland-function)\
\
[`logical_not` function](https://keras.io/api/ops/numpy/#logicalnot-function)\
\
[`logical_or` function](https://keras.io/api/ops/numpy/#logicalor-function)\
\
[`logical_xor` function](https://keras.io/api/ops/numpy/#logicalxor-function)\
\
[`logspace` function](https://keras.io/api/ops/numpy/#logspace-function)\
\
[`matmul` function](https://keras.io/api/ops/numpy/#matmul-function)\
\
[`max` function](https://keras.io/api/ops/numpy/#max-function)\
\
[`maximum` function](https://keras.io/api/ops/numpy/#maximum-function)\
\
[`mean` function](https://keras.io/api/ops/numpy/#mean-function)\
\
[`median` function](https://keras.io/api/ops/numpy/#median-function)\
\
[`meshgrid` function](https://keras.io/api/ops/numpy/#meshgrid-function)\
\
[`min` function](https://keras.io/api/ops/numpy/#min-function)\
\
[`minimum` function](https://keras.io/api/ops/numpy/#minimum-function)\
\
[`mod` function](https://keras.io/api/ops/numpy/#mod-function)\
\
[`moveaxis` function](https://keras.io/api/ops/numpy/#moveaxis-function)\
\
[`multiply` function](https://keras.io/api/ops/numpy/#multiply-function)\
\
[`nan_to_num` function](https://keras.io/api/ops/numpy/#nantonum-function)\
\
[`nanargmax` function](https://keras.io/api/ops/numpy/#nanargmax-function)\
\
[`nanargmin` function](https://keras.io/api/ops/numpy/#nanargmin-function)\
\
[`nancumprod` function](https://keras.io/api/ops/numpy/#nancumprod-function)\
\
[`nancumsum` function](https://keras.io/api/ops/numpy/#nancumsum-function)\
\
[`nanmax` function](https://keras.io/api/ops/numpy/#nanmax-function)\
\
[`nanmean` function](https://keras.io/api/ops/numpy/#nanmean-function)\
\
[`nanmedian` function](https://keras.io/api/ops/numpy/#nanmedian-function)\
\
[`nanmin` function](https://keras.io/api/ops/numpy/#nanmin-function)\
\
[`nanpercentile` function](https://keras.io/api/ops/numpy/#nanpercentile-function)\
\
[`nanprod` function](https://keras.io/api/ops/numpy/#nanprod-function)\
\
[`nanquantile` function](https://keras.io/api/ops/numpy/#nanquantile-function)\
\
[`nanstd` function](https://keras.io/api/ops/numpy/#nanstd-function)\
\
[`nansum` function](https://keras.io/api/ops/numpy/#nansum-function)\
\
[`nanvar` function](https://keras.io/api/ops/numpy/#nanvar-function)\
\
[`ndim` function](https://keras.io/api/ops/numpy/#ndim-function)\
\
[`negative` function](https://keras.io/api/ops/numpy/#negative-function)\
\
[`nextafter` function](https://keras.io/api/ops/numpy/#nextafter-function)\
\
[`nonzero` function](https://keras.io/api/ops/numpy/#nonzero-function)\
\
[`not_equal` function](https://keras.io/api/ops/numpy/#notequal-function)\
\
[`ones` function](https://keras.io/api/ops/numpy/#ones-function)\
\
[`ones_like` function](https://keras.io/api/ops/numpy/#oneslike-function)\
\
[`outer` function](https://keras.io/api/ops/numpy/#outer-function)\
\
[`pad` function](https://keras.io/api/ops/numpy/#pad-function)\
\
[`percentile` function](https://keras.io/api/ops/numpy/#percentile-function)\
\
[`power` function](https://keras.io/api/ops/numpy/#power-function)\
\
[`prod` function](https://keras.io/api/ops/numpy/#prod-function)\
\
[`ptp` function](https://keras.io/api/ops/numpy/#ptp-function)\
\
[`quantile` function](https://keras.io/api/ops/numpy/#quantile-function)\
\
[`rad2deg` function](https://keras.io/api/ops/numpy/#rad2deg-function)\
\
[`ravel` function](https://keras.io/api/ops/numpy/#ravel-function)\
\
[`real` function](https://keras.io/api/ops/numpy/#real-function)\
\
[`reciprocal` function](https://keras.io/api/ops/numpy/#reciprocal-function)\
\
[`repeat` function](https://keras.io/api/ops/numpy/#repeat-function)\
\
[`reshape` function](https://keras.io/api/ops/numpy/#reshape-function)\
\
[`right_shift` function](https://keras.io/api/ops/numpy/#rightshift-function)\
\
[`roll` function](https://keras.io/api/ops/numpy/#roll-function)\
\
[`rot90` function](https://keras.io/api/ops/numpy/#rot90-function)\
\
[`round` function](https://keras.io/api/ops/numpy/#round-function)\
\
[`searchsorted` function](https://keras.io/api/ops/numpy/#searchsorted-function)\
\
[`select` function](https://keras.io/api/ops/numpy/#select-function)\
\
[`sign` function](https://keras.io/api/ops/numpy/#sign-function)\
\
[`signbit` function](https://keras.io/api/ops/numpy/#signbit-function)\
\
[`sin` function](https://keras.io/api/ops/numpy/#sin-function)\
\
[`sinc` function](https://keras.io/api/ops/numpy/#sinc-function)\
\
[`sinh` function](https://keras.io/api/ops/numpy/#sinh-function)\
\
[`size` function](https://keras.io/api/ops/numpy/#size-function)\
\
[`slogdet` function](https://keras.io/api/ops/numpy/#slogdet-function)\
\
[`sort` function](https://keras.io/api/ops/numpy/#sort-function)\
\
[`split` function](https://keras.io/api/ops/numpy/#split-function)\
\
[`sqrt` function](https://keras.io/api/ops/numpy/#sqrt-function)\
\
[`square` function](https://keras.io/api/ops/numpy/#square-function)\
\
[`squeeze` function](https://keras.io/api/ops/numpy/#squeeze-function)\
\
[`stack` function](https://keras.io/api/ops/numpy/#stack-function)\
\
[`std` function](https://keras.io/api/ops/numpy/#std-function)\
\
[`subtract` function](https://keras.io/api/ops/numpy/#subtract-function)\
\
[`sum` function](https://keras.io/api/ops/numpy/#sum-function)\
\
[`swapaxes` function](https://keras.io/api/ops/numpy/#swapaxes-function)\
\
[`take` function](https://keras.io/api/ops/numpy/#take-function)\
\
[`take_along_axis` function](https://keras.io/api/ops/numpy/#takealongaxis-function)\
\
[`tan` function](https://keras.io/api/ops/numpy/#tan-function)\
\
[`tanh` function](https://keras.io/api/ops/numpy/#tanh-function)\
\
[`tensordot` function](https://keras.io/api/ops/numpy/#tensordot-function)\
\
[`tile` function](https://keras.io/api/ops/numpy/#tile-function)\
\
[`trace` function](https://keras.io/api/ops/numpy/#trace-function)\
\
[`trapezoid` function](https://keras.io/api/ops/numpy/#trapezoid-function)\
\
[`transpose` function](https://keras.io/api/ops/numpy/#transpose-function)\
\
[`tri` function](https://keras.io/api/ops/numpy/#tri-function)\
\
[`tril` function](https://keras.io/api/ops/numpy/#tril-function)\
\
[`triu` function](https://keras.io/api/ops/numpy/#triu-function)\
\
[`true_divide` function](https://keras.io/api/ops/numpy/#truedivide-function)\
\
[`trunc` function](https://keras.io/api/ops/numpy/#trunc-function)\
\
[`unique` function](https://keras.io/api/ops/numpy/#unique-function)\
\
[`unravel_index` function](https://keras.io/api/ops/numpy/#unravelindex-function)\
\
[`vander` function](https://keras.io/api/ops/numpy/#vander-function)\
\
[`var` function](https://keras.io/api/ops/numpy/#var-function)\
\
[`vdot` function](https://keras.io/api/ops/numpy/#vdot-function)\
\
[`vectorize` function](https://keras.io/api/ops/numpy/#vectorize-function)\
\
[`view` function](https://keras.io/api/ops/numpy/#view-function)\
\
[`vsplit` function](https://keras.io/api/ops/numpy/#vsplit-function)\
\
[`vstack` function](https://keras.io/api/ops/numpy/#vstack-function)\
\
[`where` function](https://keras.io/api/ops/numpy/#where-function)\
\
[`zeros` function](https://keras.io/api/ops/numpy/#zeros-function)\
\
[`zeros_like` function](https://keras.io/api/ops/numpy/#zeroslike-function)