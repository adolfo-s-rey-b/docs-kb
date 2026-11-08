[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.unpack\_int2 Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_int2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/packing.py#L295-L331)

Unpack a packed int2 tensor back to an int8 tensor.

tf.keras.quantizers.unpack_int2(
        packed, orig_len, axis=0, dtype='int8'
    )

This reverses `pack_int2`, restoring the original tensor whose values lie in `[-2, 1]` (signed) or `[0, 3]` (unsigned) from a packed tensor where each byte stores four int2 values. It restores the original axis order and removes any padding that was added during packing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `packed` | An `int8` or `uint8` tensor with four int2 values per element along the specified axis. |
| `orig_len` | The original (unpadded) length of the packed axis. Used to trim the padding inserted during packing. |
| `axis` | The axis along which the tensor was packed. Defaults to 0. |
| `dtype` | The data type of the input and unpacked tensor. Can be `"int8"` or `"uint8"`. Defaults to `"int8"`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `unpacked` | A tensor with the same shape as the original (unpacked) tensor. |

#### Example:

> > > import numpy as np from keras.quantizers import pack\_int2, unpack\_int2 codes = np.array(\[\[-2, 1, 0, -1, 1\]\], dtype="int8") packed, \_, orig\_len = pack\_int2(codes, axis=1) np.asarray(unpack\_int2(packed, orig\_len, axis=1)) array(\[\[-2, 1, 0, -1, 1\]\], dtype=int8)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.