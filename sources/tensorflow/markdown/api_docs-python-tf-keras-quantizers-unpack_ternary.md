[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.unpack\_ternary Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/unpack_ternary#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/packing.py#L382-L418)

Unpack a base-3 packed `uint8` tensor back to ternary `{-1, 0, +1}`.

tf.keras.quantizers.unpack_ternary(
        packed, orig_len, axis=0
    )

This reverses `pack_ternary`, restoring an `int8` tensor whose values are in `{-1, 0, +1}`. The original axis order is preserved and any padding added during packing is removed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `packed` | A `uint8` tensor produced by `pack_ternary`, with five trits encoded in each byte along `axis`. |
| `orig_len` | The original (unpadded) length of the packed axis, used to strip padding. |
| `axis` | The axis along which the tensor was packed. Defaults to 0. |

|     |
| --- |
| Returns<br>------- |     |
| An `int8` tensor with values in `{-1, 0, +1}` and the original (unpacked) shape along `axis`. |     |

#### Example:

> > > import numpy as np from keras.quantizers import pack\_ternary, unpack\_ternary trits = np.array(\[\[1, -1, 0, 1, 1, -1\]\], dtype="int8") packed, \_, orig\_len = pack\_ternary(trits, axis=1) np.asarray(unpack\_ternary(packed, orig\_len, axis=1)) array(\[\[ 1, -1, 0, 1, 1, -1\]\], dtype=int8)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.