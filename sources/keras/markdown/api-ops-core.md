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
 / Core ops

Core ops
========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L232)

### `associative_scan` function

Copied!

`keras.ops.associative_scan(f, elems, reverse=False, axis=0)`

Performs a scan with an associative binary operation, in parallel.

This operation his similar to `scan`, with the key difference that `associative_scan` is a parallel implementation with potentially significant performance benefits, especially when jit compiled. The catch is that it can only be used when `f` is a binary associative operation (i.e. it must verify `f(a, f(b, c)) == f(f(a, b), c)`).

For an introduction to associative scans, refer to this paper: Blelloch, Guy E. 1990. [Prefix Sums and Their Applications](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf)
.

**Arguments**

*   **f**: A Python callable implementing an associative binary operation with signature `r = f(a, b)`. Function `f` must be associative, i.e., it must satisfy the equation `f(a, f(b, c)) == f(f(a, b), c)`. The inputs and result are (possibly nested Python tree structures of) array(s) matching `elems`. Each array has a dimension in place of the `axis` dimension. `f` should be applied elementwise over the `axis` dimension. The result `r` has the same shape (and structure) as the two inputs `a` and `b`.
*   **elems**: A (possibly nested Python tree structure of) array(s), each with an `axis` dimension of size `num_elems`.
*   **reverse**: A boolean stating if the scan should be reversed with respect to the `axis` dimension.
*   **axis**: an integer identifying the axis over which the scan should occur.

**Returns**

A (possibly nested Python tree structure of) array(s) of the same shape and structure as `elems`, in which the `k`'th element of `axis` is the result of recursively applying `f` to combine the first `k` elements of `elems` along `axis`. For example, given `elems = [a, b, c, ...]`, the result would be `[a, f(a, b), f(f(a, b), c), ...]`.

**Examples**

Copied!

`>>> sum_fn = lambda x, y: x + y >>> xs = keras.ops.arange(5) >>> ys = keras.ops.associative_scan(sum_fn, xs, axis=0) >>> ys [0, 1, 3, 6, 10]`

Copied!

`>>> sum_fn = lambda x, y: [x[0] + y[0], x[1] + y[1], x[2] + y[2]] >>> xs = [keras.ops.array([1, 2]) for _ in range(3)] >>> ys = keras.ops.associative_scan(sum_fn, xs, axis=0) >>> ys [[1, 3], [1, 3], [1, 3]]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L863)

### `cast` function

Copied!

`keras.ops.cast(x, dtype)`

Cast a tensor to the desired dtype.

**Arguments**

*   **x**: A tensor or variable.
*   **dtype**: The target type.

**Returns**

A tensor of the specified `dtype`.

**Example**

Copied!

`>>> x = keras.ops.arange(4) >>> x = keras.ops.cast(x, dtype="float16")`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1118)

### `cond` function

Copied!

`keras.ops.cond(pred, true_fn, false_fn)`

Conditionally applies `true_fn` or `false_fn`.

**Arguments**

*   **pred**: Boolean scalar type
*   **true\_fn**: Callable returning the output for the `pred == True` case.
*   **false\_fn**: Callable returning the output for the `pred == False` case.

**Returns**

The output of either `true_fn` or `false_fn` depending on pred.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1052)

### `convert_to_numpy` function

Copied!

`keras.ops.convert_to_numpy(x)`

Convert a tensor to a NumPy array.

**Arguments**

*   **x**: A tensor.

**Returns**

A NumPy array.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1019)

### `convert_to_tensor` function

Copied!

`keras.ops.convert_to_tensor(x, dtype=None, sparse=None, ragged=None)`

Convert a NumPy array or Python array to a tensor.

Native tensors for the current backend or left unchanged unless the `dtype`, `sparse` or `ragged` arguments are set.

**Arguments**

*   **x**: A NumPy array, Python array (can be nested) or a backend tensor.
*   **dtype**: The target type. If `None`, the type of `x` is used.
*   **sparse**: Whether to keep sparse tensors. `False` will cause sparse tensors to be densified. The default value of `None` means that sparse tensors are kept only if the backend supports them.
*   **ragged**: Whether to keep ragged tensors. `False` will cause ragged tensors to be densified. The default value of `None` means that ragged tensors are kept only if the backend supports them.

**Returns**

A backend tensor of the specified `dtype` and sparseness.

**Example**

Copied!

`>>> x = np.array([1, 2, 3]) >>> y = keras.ops.convert_to_tensor(x)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1222)

### `custom_gradient` function

Copied!

`keras.ops.custom_gradient(f)`

Decorator to define a function with a custom gradient.

This decorator allows fine grained control over the gradients of a sequence for operations. This may be useful for multiple reasons, including providing a more efficient or numerically stable gradient for a sequence of operations.

**Arguments**

*   **f**: Function `f(*args)` that returns a tuple `(output, grad_fn)`, where:
    *   `args` is a sequence of (nested structures of) tensor inputs to the function.
    *   `output` is a (nested structure of) tensor outputs of applying operations in `forward_fn` to `args`.
    *   `grad_fn` is a function with the signature `grad_fn(*args, upstream)` which returns a tuple of tensors the same size as (flattened) `args`: the derivatives of tensors in `output` with respect to the tensors in `args`. `upstream` is a tensor or sequence of tensors holding the initial value gradients for each tensor in `output`.

**Returns**

A function `h(*args)` which returns the same value as `f(*args)[0]` and whose gradient is determined by `f(*args)[1]`.

**Examples**

1.  Backend-agnostic example.

Copied!

`@ops.custom_gradient def log1pexp(x):     e = ops.exp(x)      def grad(*args, upstream=None):         if upstream is None:             (upstream,) = args         return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))      return ops.log(1 + e), grad`

Note that the grad function that returns gradient computation requires `args` as well as an `upstream` keyword argument, depending on the backend being set. With the JAX and TensorFlow backends, it requires only one argument, whereas it might use the `upstream` argument in the case of the PyTorch backend.

When working with TensorFlow/JAX backend, `grad(upstream)` is sufficient. With PyTorch, the `grad` function requires `*args` as well as `upstream`, e.g. `def grad(*args, upstream)`. Follow the previous example to use `@ops.custom_gradient` in a way that is compatible with all backends.

1.  Here's JAX & TensorFlow-specific example:

Copied!

`@ops.custom_gradient def log1pexp(x):     e = ops.exp(x)     def grad(upstream):         return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))     return ops.log(1 + e), grad`

1.  Lastly, here's a PyTorch-specific example, using `*args` & `upstream`:

Copied!

`@ops.custom_gradient def log1pexp(x):     e = ops.exp(x)     def grad(*args, upstream):         return ops.multiply(upstream, 1.0 - 1.0 / ops.add(1, e))     return ops.log(1 + e), grad`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L827)

### `dtype` function

Copied!

`keras.ops.dtype(x)`

Return the dtype of the tensor input as a standardized string.

Note that due to the standardization, the dtype will not compare equal to the backend-specific version of the dtype.

**Arguments**

*   **x**: A tensor. This function will try to access the `dtype` attribute of the input tensor.

**Returns**

A string indicating the dtype of the input tensor, e.g. `"float32"`.

**Example**

Copied!

`>>> x = keras.ops.zeros((8, 12)) >>> keras.ops.dtype(x) 'float32'`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1138)

### `erf` function

Copied!

`keras.ops.erf(x)`

Computes the error function of `x`, element-wise.

**Arguments**

*   **x**: Input tensor.

**Returns**

A tensor with the same dtype as `x`.

**Example**

Copied!

`>>> x = np.array([-3.0, -2.0, -1.0, 0.0, 1.0]) >>> keras.ops.erf(x) array([-0.99998 , -0.99532, -0.842701,  0.,  0.842701], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1168)

### `erfc` function

Copied!

`keras.ops.erfc(x)`

Computes the complementary error function of `x`, element-wise.

**Arguments**

*   **x**: Input tensor.

**Returns**

A tensor with the same dtype as `x`.

**Example**

Copied!

`>>> x = np.array([-3.0, -2.0, -1.0, 0.0, 1.0]) >>> keras.ops.erfc(x) array([1.999978 , 1.9953222, 1.8427008, 1. , 0.1572992],   dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1197)

### `erfinv` function

Copied!

`keras.ops.erfinv(x)`

Computes the inverse error function of `x`, element-wise.

**Arguments**

*   **x**: Input tensor.

**Returns**

A tensor with the same dtype as `x`.

**Example**

Copied!

`>>> x = np.array([-0.5, -0.2, -0.1, 0.0, 0.3]) >>> keras.ops.erfinv(x) array([-0.47694, -0.17914, -0.08886,  0. ,  0.27246], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L456)

### `extract_sequences` function

Copied!

`keras.ops.extract_sequences(x, sequence_length, sequence_stride)`

Expands the dimension of last axis into sequences of `sequence_length`.

Slides a window of size `sequence_length` over the last axis of the input with a stride of `sequence_stride`, replacing the last axis with `[num_sequences, sequence_length]` sequences.

If the dimension along the last axis is N, the number of sequences can be computed by:

`num_sequences = 1 + (N - sequence_length) // sequence_stride`

**Arguments**

*   **x**: Input tensor.
*   **sequence\_length**: An integer representing the sequences length.
*   **sequence\_stride**: An integer representing the sequences hop size.

**Returns**

A tensor of sequences with shape \[..., num\_sequences, sequence\_length\].

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([1, 2, 3, 4, 5, 6]) >>> extract_sequences(x, 3, 2) array([[1, 2, 3],    [3, 4, 5]])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L719)

### `fori_loop` function

Copied!

`keras.ops.fori_loop(lower, upper, body_fun, init_val)`

For loop implementation.

**Arguments**

*   **lower**: The initial value of the loop variable.
*   **upper**: The upper bound of the loop variable.
*   **body\_fun**: A callable that represents the loop body. Must take two arguments: the loop variable and the loop state. The loop state should be updated and returned by this function.
*   **init\_val**: The initial value of the loop state.

**Returns**

The final state after the loop.

**Example**

Copied!

`>>> lower = 0 >>> upper = 10 >>> body_fun = lambda i, s: (i + 1, s + i) >>> init_val = 0 >>> keras.ops.fori_loop(lower, upper, body_fun, init_val) 45`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L293)

### `in_top_k` function

Copied!

`keras.ops.in_top_k(targets, predictions, k)`

Checks if the targets are in the top-k predictions.

**Arguments**

*   **targets**: A tensor of true labels.
*   **predictions**: A tensor of predicted labels.
*   **k**: An integer representing the number of predictions to consider.

**Returns**

A boolean tensor of the same shape as `targets`, where each element indicates whether the corresponding target is in the top-k predictions.

**Example**

Copied!

`>>> targets = keras.ops.convert_to_tensor([2, 5, 3]) >>> predictions = keras.ops.convert_to_tensor( ... [[0.1, 0.4, 0.6, 0.9, 0.5], ...  [0.1, 0.7, 0.9, 0.8, 0.3], ...  [0.1, 0.6, 0.9, 0.9, 0.5]]) >>> in_top_k(targets, predictions, k=3) array([ True False  True], shape=(3,), dtype=bool)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1206)

### `is_tensor` function

Copied!

`keras.ops.is_tensor(x)`

Check whether the given object is a tensor.

Note: This checks for backend specific tensors so passing a TensorFlow tensor would return `False` if your backend is PyTorch or JAX.

**Arguments**

*   **x**: A variable.

**Returns**

`True` if `x` is a tensor, otherwise `False`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L335)

### `logsumexp` function

Copied!

`keras.ops.logsumexp(x, axis=None, keepdims=False)`

Computes the logarithm of sum of exponentials of elements in a tensor.

**Arguments**

*   **x**: Input tensor.
*   **axis**: An integer or a tuple of integers specifying the axis/axes along which to compute the sum. If `None`, the sum is computed over all elements. Defaults to `None`.
*   **keepdims**: A boolean indicating whether to keep the dimensions of the input tensor when computing the sum. Defaults to `False`.

**Returns**

A tensor containing the logarithm of the sum of exponentials of elements in `x`.

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([1., 2., 3.]) >>> logsumexp(x) 3.407606`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L37)

### `map` function

Copied!

`keras.ops.map(f, xs)`

Map a function over leading array axes.

Like Python’s builtin map, except inputs and outputs are in the form of stacked arrays. Consider using the `vectorized_map()` transform instead, unless you need to apply a function element by element for reduced memory usage or heterogeneous computation with other control flow primitives.

When `xs` is an array type, the semantics of `map()` are given by this Python implementation:

Copied!

`def map(f, xs):     return np.stack([f(x) for x in xs])`

**Arguments**

*   **f**: Callable defines the function to apply element-wise over the first axis or axes of `xs`.
*   **xs**: Values over which to map along the leading axis.

**Returns**

Mapped values.

**Examples**

Copied!

`>>> f = lambda x: x**2 >>> xs = keras.ops.arange(10) >>> ys = keras.ops.map(f, xs) >>> ys [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

Copied!

`>>> f = lambda x: {"y1": x**2, "y2": x * 10}  # Can have nested outputs >>> ys = keras.ops.map(f, xs) >>> ys["y1"] [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] >>> ys["y2"] [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1109)

### `rsqrt` function

Copied!

`keras.ops.rsqrt(x)`

Computes reciprocal of square root of x element-wise.

**Arguments**

*   **x**: input tensor

**Returns**

A tensor with the same dtype as `x`.

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([1.0, 10.0, 100.0]) >>> keras.ops.rsqrt(x) array([1.0, 0.31622776, 0.1], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L897)

### `saturate_cast` function

Copied!

`keras.ops.saturate_cast(x, dtype)`

Performs a safe saturating cast to the desired dtype.

Saturating cast prevents data type overflow when casting to `dtype` with smaller values range. E.g. `ops.cast(ops.cast([-1, 256], "float32"), "uint8")` returns `[255, 0]`, but `ops.saturate_cast(ops.cast([-1, 256], "float32"), "uint8")` returns `[0, 255]`.

**Arguments**

*   **x**: A tensor or variable.
*   **dtype**: The target type.

**Returns**

A safely casted tensor of the specified `dtype`.

**Example**

Image resizing with bicubic interpolation may produce values outside original range.

Copied!

`>>> image2x2 = np.array([0, 1, 254, 255], dtype="uint8").reshape(1, 2, 2, 1) >>> image4x4 = tf.image.resize(image2x2, (4, 4), method="bicubic") >>> print(image4x4.numpy().squeeze()) >>> # [[-22.500004 -22.204624 -21.618908 -21.32353 ] >>> #  [ 52.526054  52.82143   53.407146  53.70253 ] >>> #  [201.29752  201.59288  202.17859  202.47395 ] >>> #  [276.32355  276.61893  277.20465  277.50006 ]]`

Casting this resized image back to `uint8` will cause overflow.

Copied!

`>>> image4x4_casted = ops.cast(image4x4, "uint8") >>> print(image4x4_casted.numpy().squeeze()) >>> # [[234 234 235 235] >>> #  [ 52  52  53  53] >>> #  [201 201 202 202] >>> #  [ 20  20  21  21]]`

Saturate casting to `uint8` will clip values to `uint8` range before casting and will not cause overflow.

Copied!

`>>> image4x4_saturate_casted = ops.saturate_cast(image4x4, "uint8") >>> print(image4x4_saturate_casted.numpy().squeeze()) >>> # [[  0   0   0   0] >>> #  [ 52  52  53  53] >>> #  [201 201 202 202] >>> #  [255 255 255 255]]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L116)

### `scan` function

Copied!

`keras.ops.scan(f, init, xs=None, length=None, reverse=False, unroll=1)`

Scan a function over leading array axes while carrying along state.

When the type of `xs` is an array type or `None`, and the type of `ys` is an array type, the semantics of `scan()` are given roughly by this Python implementation:

Copied!

`def scan(f, init, xs, length=None):     if xs is None:         xs = [None] * length     carry = init     ys = []     for x in xs:         carry, y = f(carry, x)         ys.append(y)     return carry, np.stack(ys)`

The loop-carried value `carry` (`init`) must hold a fixed shape and dtype across all iterations.

In TensorFlow, `y` must match `carry` in shape and dtype. This is not required in other backends.

**Arguments**

*   **f**: Callable defines the logic for each loop iteration. This accepts two arguments where the first is a value of the loop carry and the second is a slice of `xs` along its leading axis. This callable returns a pair where the first represents a new value for the loop carry and the second represents a slice of the output.
*   **init**: The initial loop carry value. This can be a scalar, tensor, or any nested structure. It must match the structure of the first element returned by `f`.
*   **xs**: Optional value to scan along its leading axis. This can be a tensor or any nested structure. If `xs` is not provided, you must specify `length` to define the number of loop iterations. Defaults to `None`.
*   **length**: Optional integer specifying the number of loop iterations. If `length` is not provided, it defaults to the sizes of leading axis of the arrays in `xs`. Defaults to `None`.
*   **reverse**: Optional boolean specifying whether to run the scan iteration forward or in reverse, equivalent to reversing the leading axes of the arrays in both `xs` and in `ys`.
*   **unroll**: Optional positive integer or boolean specifying how many scan iterations to unroll within a single iteration of a loop. If an integer is provided, it determines how many unrolled loop iterations to run within a single rolled iteration of the loop. If a boolean is provided, it will determine if the loop is completely unrolled (`unroll=True`) or left completely unrolled (`unroll=False`). Note that unrolling is only supported by JAX and TensorFlow backends.

**Returns**

A pair where the first element represents the final loop carry value and the second element represents the stacked outputs of `f` when scanned over the leading axis of the inputs.

**Examples**

Copied!

`>>> sum_fn = lambda c, x: (c + x, c + x) >>> init = keras.ops.array(0) >>> xs = keras.ops.array([1, 2, 3, 4, 5]) >>> carry, result = keras.ops.scan(sum_fn, init, xs) >>> carry 15 >>> result [1, 3, 6, 10, 15]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L305)

### `scatter` function

Copied!

`keras.ops.scatter(indices, values, shape)`

Returns a tensor of shape `shape` where `indices` are set to `values`.

At a high level, this operation does `zeros[indices] = updates` and returns the output. It is equivalent to:

Copied!

`zeros = keras.ops.zeros(shape) output = keras.ops.scatter_update(zeros, indices, values)`

**Arguments**

*   **indices**: A tensor or list/tuple specifying indices for the values in `values`.
*   **values**: A tensor, the values to be set at `indices`.
*   **shape**: Shape of the output tensor.

**Example**

Copied!

`>>> indices = [[0, 1], [1, 1]] >>> values = np.array([1., 1.]) >>> keras.ops.scatter(indices, values, shape=(2, 2)) array([[0., 1.],        [0., 1.]])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L350)

### `scatter_update` function

Copied!

`keras.ops.scatter_update(inputs, indices, updates, reduction=None)`

Update inputs via updates at scattered (sparse) indices.

At a high level, this operation does `inputs[indices] = updates`. Assume `inputs` is a tensor of shape `(D0, D1, ..., Dn)`, there are 2 main usages of `scatter_update`.

1.  `indices` is a 2D tensor of shape `(num_updates, n)`, where `num_updates` is the number of updates to perform, and `updates` is a 1D tensor of shape `(num_updates,)`. For example, if `inputs` is `zeros((4, 4, 4))`, and we want to update `inputs[1, 2, 3]` and `inputs[0, 1, 3]` as 1, then we can use:

Copied!

`inputs = np.zeros((4, 4, 4)) indices = [[1, 2, 3], [0, 1, 3]] updates = np.array([1., 1.]) inputs = keras.ops.scatter_update(inputs, indices, updates)`

2 `indices` is a 2D tensor of shape `(num_updates, k)`, where `num_updates` is the number of updates to perform, and `k` (`k < n`) is the size of each index in `indices`. `updates` is a `n - k`\-D tensor of shape `(num_updates, inputs.shape[k:])`. For example, if `inputs = np.zeros((4, 4, 4))`, and we want to update `inputs[1, 2, :]` and `inputs[2, 3, :]` as `[1, 1, 1, 1]`, then `indices` would have shape `(num_updates, 2)` (`k = 2`), and `updates` would have shape `(num_updates, 4)` (`inputs.shape[2:] = 4`). See the code below:

Copied!

`inputs = np.zeros((4, 4, 4)) indices = [[1, 2], [2, 3]] updates = np.array([[1., 1., 1, 1,], [1., 1., 1, 1,]) inputs = keras.ops.scatter_update(inputs, indices, updates)`\
\
**Arguments**\
\
*   **inputs**: A tensor, the tensor to be updated.\
*   **indices**: A tensor or list/tuple of shape `(N, inputs.ndim)`, specifying indices to update. `N` is the number of indices to update, must be equal to the first dimension of `updates`.\
*   **updates**: A tensor, the new values to be put to `inputs` at `indices`.\
*   **reduction**: A string specifying the reduction operation to apply when multiple updates target the same index. Supported values are: `None` (default): Updates replace existing values (last write wins). `"add"`: Updates are added to existing values. `"max"`: The maximum of updates and existing values is kept. `"min"`: The minimum of updates and existing values is kept. `"mul"`: Updates are multiplied with existing values.\
\
**Returns**\
\
A tensor, has the same shape and dtype as `inputs`.\
\
**Example**\
\
Using `reduction="add"` to accumulate values at the same index:\
\
Copied!\
\
`>>> inputs = np.zeros((4,)) >>> indices = [[0], [0], [1]] >>> updates = np.array([1., 1., 1.]) >>> keras.ops.scatter_update(inputs, indices, updates, reduction="add") array([2., 1., 0., 0.])`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L104)\
\
### `segment_max` function\
\
Copied!\
\
`keras.ops.segment_max(data, segment_ids, num_segments=None, sorted=False)`\
\
Computes the max of segments in a tensor.\
\
**Arguments**\
\
*   **data**: Input tensor.\
*   **segment\_ids**: A N-D tensor containing segment indices for each element in `data`. data.shape\[:len(segment\_ids.shape)\] should match.\
*   **num\_segments**: An integer representing the total number of segments. If not specified, it is inferred from the maximum value in `segment_ids`.\
*   **sorted**: A boolean indicating whether `segment_ids` is sorted. Defaults to `False`.\
\
**Returns**\
\
A tensor containing the max of segments, where each element represents the max of the corresponding segment in `data`.\
\
**Example**\
\
Copied!\
\
`>>> data = keras.ops.convert_to_tensor([1, 2, 10, 20, 100, 200]) >>> segment_ids = keras.ops.convert_to_tensor([0, 0, 1, 1, 2, 2]) >>> num_segments = 3 >>> keras.ops.segment_max(data, segment_ids, num_segments) array([2, 20, 200], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L149)\
\
### `segment_min` function\
\
Copied!\
\
`keras.ops.segment_min(data, segment_ids, num_segments=None, sorted=False)`\
\
Computes the min of segments in a tensor.\
\
**Arguments**\
\
*   **data**: Input tensor.\
*   **segment\_ids**: A N-D tensor containing segment indices for each element in `data`. data.shape\[:len(segment\_ids.shape)\] should match.\
*   **num\_segments**: An integer representing the total number of segments. If not specified, it is inferred from the maximum value in `segment_ids`.\
*   **sorted**: A boolean indicating whether `segment_ids` is sorted. Defaults to `False`.\
\
**Returns**\
\
A tensor containing the min of segments, where each element represents the min of the corresponding segment in `data`.\
\
**Example**\
\
Copied!\
\
`>>> data = keras.ops.convert_to_tensor([1, 2, 10, 20, 100, 200]) >>> segment_ids = keras.ops.convert_to_tensor([0, 0, 1, 1, 2, 2]) >>> num_segments = 3 >>> keras.ops.segment_min(data, segment_ids, num_segments) array([1, 10, 100], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L194)\
\
### `segment_prod` function\
\
Copied!\
\
`keras.ops.segment_prod(data, segment_ids, num_segments=None, sorted=False)`\
\
Computes the product of segments in a tensor.\
\
**Arguments**\
\
*   **data**: Input tensor.\
*   **segment\_ids**: A 1-D tensor containing segment indices for each element in `data`. `data.shape[0]` should match `segment_ids.shape[0]`.\
*   **num\_segments**: An integer representing the total number of segments. If not specified, it is inferred from the maximum value in `segment_ids`.\
*   **sorted**: A boolean indicating whether `segment_ids` is sorted. Defaults to `False`.\
\
**Returns**\
\
A tensor containing the product of segments, where each element represents the product of the corresponding segment in `data`.\
\
**Example**\
\
Copied!\
\
`>>> data = keras.ops.convert_to_tensor([1, 2, 10, 20, 100, 200]) >>> segment_ids = keras.ops.convert_to_tensor([0, 0, 1, 1, 2, 2]) >>> num_segments = 3 >>> keras.ops.segment_prod(data, segment_ids, num_segments) array([2, 200, 20000], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L58)\
\
### `segment_sum` function\
\
Copied!\
\
`keras.ops.segment_sum(data, segment_ids, num_segments=None, sorted=False)`\
\
Computes the sum of segments in a tensor.\
\
**Arguments**\
\
*   **data**: Input tensor.\
*   **segment\_ids**: A N-D tensor containing segment indices for each element in `data`. Num dims for segment ids should be strictly smaller or equal to number of dims in data.\
*   **num\_segments**: An integer representing the total number of segments. If not specified, it is inferred from the maximum value in `segment_ids`.\
*   **sorted**: A boolean indicating whether `segment_ids` is sorted. Defaults to `False`.\
\
**Returns**\
\
A tensor containing the sum of segments, where each element represents the sum of the corresponding segment in `data`.\
\
**Example**\
\
Copied!\
\
`>>> data = keras.ops.convert_to_tensor([1, 2, 10, 20, 100, 200]) >>> segment_ids = keras.ops.convert_to_tensor([0, 0, 1, 1, 2, 2]) >>> num_segments = 3 >>> keras.ops.segment_sum(data, segment_ids,num_segments) array([3, 30, 300], dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L800)\
\
### `shape` function\
\
Copied!\
\
`keras.ops.shape(x)`\
\
Gets the shape of the tensor input.\
\
Note: On the TensorFlow backend, when `x` is a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
 with dynamic shape, dimensions which are dynamic in the context of a compiled function will have a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
 value instead of a static integer value.\
\
**Arguments**\
\
*   **x**: A tensor. This function will try to access the `shape` attribute of the input tensor.\
\
**Returns**\
\
A tuple of integers or None values, indicating the shape of the input tensor.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.zeros((8, 12)) >>> keras.ops.shape(x) (8, 12)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L467)\
\
### `slice` function\
\
Copied!\
\
`keras.ops.slice(inputs, start_indices, shape)`\
\
Return a slice of an input tensor.\
\
At a high level, this operation is an explicit replacement for array slicing e.g. `inputs[start_indices: start_indices + shape]`. Unlike slicing via brackets, this operation will accept tensor start indices on all backends, which is useful when indices dynamically computed via other tensor operations.\
\
Copied!\
\
`inputs = np.zeros((5, 5)) start_indices = np.array([3, 3]) shape = np.array([2, 2]) inputs = keras.ops.slice(inputs, start_indices, shape)`\
\
**Arguments**\
\
*   **inputs**: A tensor, the tensor to be updated.\
*   **start\_indices**: A list/tuple of shape `(inputs.ndim,)`, specifying the starting indices for updating.\
*   **shape**: The full shape of the returned slice.\
\
**Returns**\
\
A tensor, has the same shape and dtype as `inputs`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L506)\
\
### `slice_update` function\
\
Copied!\
\
`keras.ops.slice_update(inputs, start_indices, updates)`\
\
Update an input by slicing in a tensor of updated values.\
\
At a high level, this operation does `inputs[start_indices: start_indices + updates.shape] = updates`. Assume inputs is a tensor of shape `(D0, D1, ..., Dn)`, `start_indices` must be a list/tuple of n integers, specifying the starting indices. `updates` must have the same rank as `inputs`, and the size of each dim must not exceed `Di - start_indices[i]`. For example, if we have 2D inputs `inputs = np.zeros((5, 5))`, and we want to update the intersection of last 2 rows and last 2 columns as 1, i.e., `inputs[3:, 3:] = np.ones((2, 2))`, then we can use the code below:\
\
Copied!\
\
`inputs = np.zeros((5, 5)) start_indices = [3, 3] updates = np.ones((2, 2)) inputs = keras.ops.slice_update(inputs, start_indices, updates)`\
\
**Arguments**\
\
*   **inputs**: A tensor, the tensor to be updated.\
*   **start\_indices**: A list/tuple of shape `(inputs.ndim,)`, specifying the starting indices for updating.\
*   **updates**: A tensor, the new values to be put to `inputs` at `indices`. `updates` must have the same rank as `inputs`.\
\
**Returns**\
\
A tensor, has the same shape and dtype as `inputs`.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L676)\
\
### `stop_gradient` function\
\
Copied!\
\
`keras.ops.stop_gradient(variable)`\
\
Stops gradient computation.\
\
**Arguments**\
\
*   **variable**: A tensor variable for which the gradient computation is to be disabled.\
\
**Returns**\
\
The variable with gradient computation disabled.\
\
**Examples**\
\
Copied!\
\
`>>> var = keras.backend.convert_to_tensor( ...     [1., 2., 3.], ...     dtype="float32" ... ) >>> var = keras.ops.stop_gradient(var)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L552)\
\
### `switch` function\
\
Copied!\
\
`keras.ops.switch(index, branches, *operands)`\
\
Apply exactly one of the `branches` given by `index`.\
\
If `index` is out of bounds, it is clamped to within bounds.\
\
The semantics of `switch` are given roughly by this Python implementation:\
\
Copied!\
\
`def switch(index, branches, *operands):     index = clamp(0, index, len(branches) - 1)     return branches[index](*operands)`\
\
**Arguments**\
\
*   **index**: An integer scalar indicating which branch function to apply.\
*   **branches**: A sequence of functions to be applied based on `index`.\
*   **operands**: Inputs to whichever branch is applied.\
\
**Returns**\
\
The outputs of `branch(*operands)` for the branch that was selected based on `index`.\
\
**Examples**\
\
Copied!\
\
`>>> add_fn = lambda x, y: x + y >>> subtract_fn = lambda x, y: x - y >>> x = keras.ops.array(2.0) >>> y = keras.ops.array(0.5) >>> branches = [add_fn, subtract_fn] >>> keras.ops.switch(0, branches, x, y) 2.5`\
\
Copied!\
\
`>>> keras.ops.switch(1, branches, x, y) 1.5`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L251)\
\
### `top_k` function\
\
Copied!\
\
`keras.ops.top_k(x, k, sorted=True)`\
\
Finds the top-k values and their indices in a tensor.\
\
**Arguments**\
\
*   **x**: Input tensor.\
*   **k**: An integer representing the number of top elements to retrieve.\
*   **sorted**: A boolean indicating whether to sort the output in descending order. Defaults to `True`.\
\
**Returns**\
\
A tuple containing two tensors. The first tensor contains the top-k values, and the second tensor contains the indices of the top-k values in the input tensor.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.convert_to_tensor([5, 2, 7, 1, 9, 3]) >>> values, indices = top_k(x, k=3) >>> print(values) array([9 7 5], shape=(3,), dtype=int32) >>> print(indices) array([4 2 0], shape=(3,), dtype=int32)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L776)\
\
### `unstack` function\
\
Copied!\
\
`keras.ops.unstack(x, num=None, axis=0)`\
\
Unpacks the given dimension of a rank-R tensor into rank-(R-1) tensors.\
\
**Arguments**\
\
*   **x**: The input tensor.\
*   **num**: The length of the dimension axis. Automatically inferred if `None`.\
*   **axis**: The axis along which to unpack.\
\
**Returns**\
\
A list of tensors unpacked along the given axis.\
\
**Example**\
\
Copied!\
\
`>>> x = keras.ops.array([[1, 2], [3, 4]]) >>> keras.ops.unstack(x, axis=0) [array([1, 2]), array([3, 4])]`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1171)\
\
### `vectorized_map` function\
\
Copied!\
\
`keras.ops.vectorized_map(function, elements)`\
\
Parallel map of `function` on axis 0 of tensor(s) `elements`.\
\
Schematically, `vectorized_map` implements the following, in the case of a single tensor input `elements`:\
\
Copied!\
\
`def vectorized_map(function, elements):     outputs = []     for e in elements:         outputs.append(function(e))     return np.stack(outputs)`\
\
In the case of an iterable of tensors `elements`, it implements the following:\
\
Copied!\
\
`def vectorized_map(function, elements):     batch_size = elements[0].shape[0]     outputs = []     for index in range(batch_size):         outputs.append(function([e[index] for e in elements]))     return np.stack(outputs)`\
\
In this case, `function` is expected to take as input a single list of tensor arguments.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L614)\
\
### `while_loop` function\
\
Copied!\
\
`keras.ops.while_loop(cond, body, loop_vars, maximum_iterations=None)`\
\
While loop implementation.\
\
**Arguments**\
\
*   **cond**: A callable that represents the termination condition of the loop. Must accept a `loop_vars` like structure as an argument. If `loop_vars` is a tuple or list, each element of `loop_vars` will be passed positionally to the callable.\
*   **body**: A callable that represents the loop body. Must accept a `loop_vars` like structure as an argument, and return update value with the same structure. If `loop_vars` is a tuple or list, each element of `loop_vars` will be passed positionally to the callable.\
*   **loop\_vars**: An arbitrary nested structure of tensor state to persist across loop iterations.\
*   **maximum\_iterations**: Optional maximum number of iterations of the while loop to run. If provided, the `cond` output is AND-ed with an additional condition ensuring the number of iterations executed is no greater than `maximum_iterations`.\
\
**Returns**\
\
A list/tuple of tensors, has the same shape and dtype as `inputs`.\
\
**Examples**\
\
Copied!\
\
`>>> i = 0 >>> cond = lambda i: i < 10 >>> body = lambda i: i + 1 >>> keras.ops.while_loop(cond, body, i) 10`\
\
Copied!\
\
`>>> x, y = 0, 1 >>> cond = lambda x, y: x < 10 >>> body = lambda x, y: (x + 1, y + 1) >>> keras.ops.while_loop(cond, body, (x, y)) 10, 11`\
\
* * *\
\
[Core ops](https://keras.io/api/ops/core/#core-ops)\
\
[`associative_scan` function](https://keras.io/api/ops/core/#associativescan-function)\
\
[`cast` function](https://keras.io/api/ops/core/#cast-function)\
\
[`cond` function](https://keras.io/api/ops/core/#cond-function)\
\
[`convert_to_numpy` function](https://keras.io/api/ops/core/#converttonumpy-function)\
\
[`convert_to_tensor` function](https://keras.io/api/ops/core/#converttotensor-function)\
\
[`custom_gradient` function](https://keras.io/api/ops/core/#customgradient-function)\
\
[`dtype` function](https://keras.io/api/ops/core/#dtype-function)\
\
[`erf` function](https://keras.io/api/ops/core/#erf-function)\
\
[`erfc` function](https://keras.io/api/ops/core/#erfc-function)\
\
[`erfinv` function](https://keras.io/api/ops/core/#erfinv-function)\
\
[`extract_sequences` function](https://keras.io/api/ops/core/#extractsequences-function)\
\
[`fori_loop` function](https://keras.io/api/ops/core/#foriloop-function)\
\
[`in_top_k` function](https://keras.io/api/ops/core/#intopk-function)\
\
[`is_tensor` function](https://keras.io/api/ops/core/#istensor-function)\
\
[`logsumexp` function](https://keras.io/api/ops/core/#logsumexp-function)\
\
[`map` function](https://keras.io/api/ops/core/#map-function)\
\
[`rsqrt` function](https://keras.io/api/ops/core/#rsqrt-function)\
\
[`saturate_cast` function](https://keras.io/api/ops/core/#saturatecast-function)\
\
[`scan` function](https://keras.io/api/ops/core/#scan-function)\
\
[`scatter` function](https://keras.io/api/ops/core/#scatter-function)\
\
[`scatter_update` function](https://keras.io/api/ops/core/#scatterupdate-function)\
\
[`segment_max` function](https://keras.io/api/ops/core/#segmentmax-function)\
\
[`segment_min` function](https://keras.io/api/ops/core/#segmentmin-function)\
\
[`segment_prod` function](https://keras.io/api/ops/core/#segmentprod-function)\
\
[`segment_sum` function](https://keras.io/api/ops/core/#segmentsum-function)\
\
[`shape` function](https://keras.io/api/ops/core/#shape-function)\
\
[`slice` function](https://keras.io/api/ops/core/#slice-function)\
\
[`slice_update` function](https://keras.io/api/ops/core/#sliceupdate-function)\
\
[`stop_gradient` function](https://keras.io/api/ops/core/#stopgradient-function)\
\
[`switch` function](https://keras.io/api/ops/core/#switch-function)\
\
[`top_k` function](https://keras.io/api/ops/core/#topk-function)\
\
[`unstack` function](https://keras.io/api/ops/core/#unstack-function)\
\
[`vectorized_map` function](https://keras.io/api/ops/core/#vectorizedmap-function)\
\
[`while_loop` function](https://keras.io/api/ops/core/#whileloop-function)