[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.pack\_int2 Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_int2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/packing.py#L247-L292)

Pack an int2 tensor into an int8 tensor with 4 values per byte.

tf.keras.quantizers.pack_int2(
        arr, axis=0, dtype='int8'
    )

The input values must already be int8/uint8 representing the desired int2 values (signed range `[-2, 1]`, or unsigned range `[0, 3]`). Packing is performed along the specified axis (default is 0). Four consecutive values along the packing axis are stored in a single output byte, from the least significant 2-bit field to the most significant one.

This mirrors the design of `pack_int4` (padding + original-length trim), but achieves a 4x rather than 2x storage reduction, which is what makes 2-bit storage worthwhile relative to a plain uint8 tensor.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `arr` | An `int8` or `uint8` tensor containing int2 values in the range `[-2, 1]` (signed) or `[0, 3]` (unsigned). |
| `axis` | The axis along which to pack the tensor. Defaults to 0. |
| `dtype` | The data type of the input and packed tensor. Can be `"int8"` or `"uint8"`. Defaults to `"int8"`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `tuple` | A tuple `(packed, packed_shape, orig_len)` where `packed` is the packed tensor with four int2 values per byte, `packed_shape` is the shape of the packed tensor, and `orig_len` is the original (unpacked) length along `axis` prior to any padding that was inserted to reach a multiple of four. |

#### Example:

> > > import numpy as np from keras.quantizers import pack\_int2 codes = np.array(\[\[-2, 1, 0, -1, 1\]\], dtype="int8") packed, packed\_shape, orig\_len = pack\_int2(codes, axis=1) np.asarray(packed) # four 2-bit fields per byte; axis 1 padded to 8 array(\[\[-58, 1\]\], dtype=int8) packed\_shape, orig\_len ((1, 2), 5)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.