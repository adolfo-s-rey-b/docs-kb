[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int4#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.unpack\_int4 Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L753-L900)

Unpack a packed int4 back to an int8 tensor in the range \[-8, 7\].

tf.keras.quantizers.unpack_int4(
        packed, orig_len, axis=0, dtype='int8'
    )

This function reverses the packing performed by `pack_int4`, restoring
    the original int8 tensor (values in the range [-8, 7]) from a packed int8
    tensor where each element contains two int4 values (one in the lower nibble,
    one in the upper nibble).
    
    The function restores the original axis order and removes any
    padding that was added during packing.
    
    Args:
        packed: An int8 tensor containing packed int4 values along the
            specified axis. Each int8 value encodes two int4 values.
        orig_len: The original (unpadded) length of the axis that was
            packed. This is used to remove any padding that may have
            been added during packing to ensure an even number of rows.
        axis: The axis along which the tensor was packed. Defaults to 0.
        dtype: The data type of the input and unpacked tensor. Can be
            `"int8"` or `"uint8"`. Defaults to `"int8"`.
    
    Returns:
        unpacked: An int8 tensor with the same shape as the original
            (unpacked) tensor, with values in the range [-8, 7].
    
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