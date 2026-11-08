None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
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
 [Quantizer classes](https://keras.io/api/quantizers/quantizer_classes/)
 [Quantizer utilities](https://keras.io/api/quantizers/quantizer_utils/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Quantizers](https://keras.io/api/quantizers/)
 / Quantizer utilities

Quantizer utilities
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L69)

### `abs_max_quantize` function

Copied!

`keras.quantizers.abs_max_quantize(     inputs, axis, value_range=(-127, 127), dtype="int8", epsilon=1e-07, to_numpy=False )`

Quantizes the input tensor using the absolute maximum quantization scheme.

**Arguments**

*   **inputs**: Input tensor to quantize.
*   **axis**: Axis along which to compute the quantization range.
*   **value\_range**: Tuple of the minimum and maximum values of the quantization range.
*   **dtype**: Data type of the quantized output.
*   **epsilon**: Small value to avoid division by zero.
*   **to\_numpy**: Whether to perform the quantization in numpy. This performs the computation on the host CPU and can be useful for saving memory on the device. If False, the computation is performed on the device.

**Returns**

A tuple of the quantized tensor and the scale.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L597)

### `compute_float8_amax_history` function

Copied!

`keras.quantizers.compute_float8_amax_history(x, amax_history)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L584)

### `compute_float8_scale` function

Copied!

`keras.quantizers.compute_float8_scale(amax, scale, dtype_max, margin=0)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L430)

### `fake_quant_with_min_max_vars` function

Copied!

`keras.quantizers.fake_quant_with_min_max_vars(     inputs, min_vals, max_vals, num_bits=8, narrow_range=False, axis=None )`

Perform per-tensor or per-channel fake quantization.

`[min_vals, max_vals]` define the clamping range for the `inputs`.

The `inputs` are quantized into the quantization range: - `[0, 2^num_bits - 1]` when `narrow_range=False` - `[1, 2^num_bits - 1]` when `narrow_range=True`

After quantization, the values are dequantized and output as floats within the `[min_vals, max_vals]` interval.

This operation supports gradient computation, allowing `min_vals` and `max_vals` to be trained.

**Arguments**

*   **inputs**: Input Keras tensor of float dtype.
*   **min\_vals**: A global minimum scalar or a per-channel minimum tensor.
*   **max\_vals**: A global maximum scalar or a per-channel maximum tensor.
*   **num\_bits**: Quantization bit width (e.g., `8` for int8). Defaults to `8`.
*   **narrow\_range**: Whether to use narrow quantization range. Defaults to `False`.
*   **axis**: Axis along which to perform per-channel quantization. If `None`, per-tensor quantization is performed. Defaults to `None`.

**Returns**

*   **Tensor**: A Keras tensor with fake quantization applied.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L623)

### `pack_int4` function

Copied!

`keras.quantizers.pack_int4(arr, axis=0, dtype="int8")`

Pack an int4 tensor into an int8 tensor with packed nibbles.

Copied!

``The input values must already be int8 in the signed range `[-8, 7]` and represent the desired int4 values. Packing is performed along the specified axis (default is 0).  For every two consecutive rows, the **low nibble** of the output byte stores the value from the first row, and the **high nibble** stores the value from the second row.  # Arguments     arr: An `int8` or `uint8` tensor containing int4 values in the range         `[-8, 7]`.     axis: The axis along which to pack the tensor. Defaults to 0.     dtype: The data type of the input and packed tensor. Can be         `"int8"` or `"uint8"`. Defaults to `"int8"`.  # Returns     tuple: A tuple `(packed, packed_shape, orig_rows)` where `packed` is         the packed int8 tensor with int4 values stored in nibbles,         `packed_shape` is the shape of the packed tensor, and `orig_rows`         is the original (unpacked) row count prior to any padding that may         have been inserted when an odd number of rows is supplied.  # Example   ```python >>> import numpy as np >>> from keras.quantizers import pack_int4, unpack_int4  # Example with axis=0 # Original array has shape (3, 2) >>> original_array = np.array([[-3, 7], [2, -8], [1, 0]], dtype=np.int8)  # Pack the array along axis 0. Since the length of axis 0 (3) is # odd, it will be padded to a length of 4. The packed array will # have a shape of (ceil(3/2), 2) = (2, 2). >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=0) >>> print("Packed array:``

", packed) Packed array: \[\[ 45 -121\] \[ 1 0\]\]

Copied!

`# Now, unpack the array back to its original form >>> unpacked = unpack_int4(packed, orig_len, axis=0) >>> print("Unpacked array:`

", unpacked) Unpacked array: \[\[-3 7\] \[ 2 -8\] \[ 1 0\]\] >>> np.allclose(original\_array, unpacked) True

Copied!

`# Example with axis=1 # Original array has shape (2, 3) >>> original_array = np.array([[-3, 7, 2], [-8, 1, 0]], dtype=np.int8)  # Pack along axis 1. Length of axis 1 (3) is padded to 4. # The new shape is (2, ceil(3/2)) = (2, 2). >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=1) >>> print("Packed array:`

", packed) Packed array: \[\[ 125 2\] \[ 24 0\]\]

Copied!

`# Unpack the array >>> unpacked = unpack_int4(packed, orig_len, axis=1) >>> print("Unpacked array:`

", unpacked) Unpacked array: \[\[-3 7 2\] \[-8 1 0\]\] >>> np.allclose(original\_array, unpacked) True \`\`\`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L608)

### `quantize_and_dequantize` function

Copied!

`keras.quantizers.quantize_and_dequantize(     inputs, scale, quantized_dtype, compute_dtype )`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L753)

### `unpack_int4` function

Copied!

`keras.quantizers.unpack_int4(packed, orig_len, axis=0, dtype="int8")`

Unpack a packed int4 back to an int8 tensor in the range \[-8, 7\].

Copied!

``This function reverses the packing performed by `pack_int4`, restoring the original int8 tensor (values in the range [-8, 7]) from a packed int8 tensor where each element contains two int4 values (one in the lower nibble, one in the upper nibble).  The function restores the original axis order and removes any padding that was added during packing.  # Arguments     packed: An int8 tensor containing packed int4 values along the         specified axis. Each int8 value encodes two int4 values.     orig_len: The original (unpadded) length of the axis that was         packed. This is used to remove any padding that may have         been added during packing to ensure an even number of rows.     axis: The axis along which the tensor was packed. Defaults to 0.     dtype: The data type of the input and unpacked tensor. Can be         `"int8"` or `"uint8"`. Defaults to `"int8"`.  # Returns     unpacked: An int8 tensor with the same shape as the original         (unpacked) tensor, with values in the range [-8, 7].  # Example   ```python >>> import numpy as np >>> from keras.quantizers import pack_int4, unpack_int4  # Example with axis=0 # Original array has shape (3, 2) >>> original_array = np.array([[-3, 7], [2, -8], [1, 0]], dtype=np.int8)  # Pack the array along axis 0. Since the length of axis 0 (3) is # odd, it will be padded to a length of 4. The packed array will # have a shape of (ceil(3/2), 2) = (2, 2). >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=0) >>> print("Packed array:``

", packed) Packed array: \[\[ 45 -121\] \[ 1 0\]\]

Copied!

`# Now, unpack the array back to its original form >>> unpacked = unpack_int4(packed, orig_len, axis=0) >>> print("Unpacked array:`

", unpacked) Unpacked array: \[\[-3 7\] \[ 2 -8\] \[ 1 0\]\] >>> np.allclose(original\_array, unpacked) True

Copied!

`# Example with axis=1 # Original array has shape (2, 3) >>> original_array = np.array([[-3, 7, 2], [-8, 1, 0]], dtype=np.int8)  # Pack along axis 1. Length of axis 1 (3) is padded to 4. # The new shape is (2, ceil(3/2)) = (2, 2). >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=1) >>> print("Packed array:`

", packed) Packed array: \[\[ 125 2\] \[ 24 0\]\]

Copied!

`# Unpack the array >>> unpacked = unpack_int4(packed, orig_len, axis=1) >>> print("Unpacked array:`

", unpacked) Unpacked array: \[\[-3 7 2\] \[-8 1 0\]\] >>> np.allclose(original\_array, unpacked) True \`\`\`

* * *

[Quantizer utilities](https://keras.io/api/quantizers/quantizer_utils/#quantizer-utilities)

[`abs_max_quantize` function](https://keras.io/api/quantizers/quantizer_utils/#absmaxquantize-function)

[`compute_float8_amax_history` function](https://keras.io/api/quantizers/quantizer_utils/#computefloat8amaxhistory-function)

[`compute_float8_scale` function](https://keras.io/api/quantizers/quantizer_utils/#computefloat8scale-function)

[`fake_quant_with_min_max_vars` function](https://keras.io/api/quantizers/quantizer_utils/#fakequantwithminmaxvars-function)

[`pack_int4` function](https://keras.io/api/quantizers/quantizer_utils/#packint4-function)

[`quantize_and_dequantize` function](https://keras.io/api/quantizers/quantizer_utils/#quantizeanddequantize-function)

[`unpack_int4` function](https://keras.io/api/quantizers/quantizer_utils/#unpackint4-function)