[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int4?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int4?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int4?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.pack\_int4 Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L623-L750)

Pack an int4 tensor into an int8 tensor with packed nibbles.

tf.keras.quantizers.pack_int4(
        arr, axis=0, dtype='int8'
    )

The input values must already be int8 in the signed range `[-8, 7]` and
    represent the desired int4 values. Packing is performed along the specified
    axis (default is 0).
    
    For every two consecutive rows, the **low nibble** of the output byte
    stores the value from the first row, and the **high nibble** stores
    the value from the second row.
    
    Args:
        arr: An `int8` or `uint8` tensor containing int4 values in the range
            `[-8, 7]`.
        axis: The axis along which to pack the tensor. Defaults to 0.
        dtype: The data type of the input and packed tensor. Can be
            `"int8"` or `"uint8"`. Defaults to `"int8"`.
    
    Returns:
        tuple: A tuple `(packed, packed_shape, orig_rows)` where `packed` is
            the packed int8 tensor with int4 values stored in nibbles,
            `packed_shape` is the shape of the packed tensor, and `orig_rows`
            is the original (unpacked) row count prior to any padding that may
            have been inserted when an odd number of rows is supplied.
    
    Example:
    
    ```python
    ```
    >>> import numpy as np
    >>> from keras.quantizers import pack_int4, unpack_int4
    
    ```
    
    # Example with axis=0
    # Original array has shape (3, 2)
    ```
    >>> original_array = np.array([[-3, 7], [2, -8], [1, 0]], dtype=np.int8)
    
    ```
    
    # Pack the array along axis 0. Since the length of axis 0 (3) is
    # odd, it will be padded to a length of 4. The packed array will
    # have a shape of (ceil(3/2), 2) = (2, 2).
    ```
    >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=0)
    >>> print("Packed array:

", packed) Packed array: \[\[ 45 -121\] \[ 1 0\]\]

```
    
    # Now, unpack the array back to its original form
    ```
    >>> unpacked = unpack_int4(packed, orig_len, axis=0)
    >>> print("Unpacked array:

", unpacked) Unpacked array: \[\[-3 7\] \[ 2 -8\] \[ 1 0\]\] >>> np.allclose(original\_array, unpacked) True

```
    
    # Example with axis=1
    # Original array has shape (2, 3)
    ```
    >>> original_array = np.array([[-3, 7, 2], [-8, 1, 0]], dtype=np.int8)
    
    ```
    
    # Pack along axis 1. Length of axis 1 (3) is padded to 4.
    # The new shape is (2, ceil(3/2)) = (2, 2).
    ```
    >>> packed, packed_shape, orig_len = pack_int4(original_array, axis=1)
    >>> print("Packed array:

", packed) Packed array: \[\[ 125 2\] \[ 24 0\]\]

```
    
    # Unpack the array
    ```
    >>> unpacked = unpack_int4(packed, orig_len, axis=1)
    >>> print("Unpacked array:

", unpacked) Unpacked array: \[\[-3 7 2\] \[-8 1 0\]\] >>> np.allclose(original\_array, unpacked) True

    ```
    
    ```

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.