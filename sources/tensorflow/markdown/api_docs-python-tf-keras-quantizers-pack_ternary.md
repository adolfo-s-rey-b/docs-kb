[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/pack_ternary#main-content)

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
    

tf.keras.quantizers.pack\_ternary Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/quantizers/packing.py#L334-L379)

Pack a ternary tensor into a `uint8` tensor at ~1.6 bits per value.

tf.keras.quantizers.pack_ternary(
        arr, axis=0
    )

The input values must be in `{-1, 0, +1}`. Five ternary values (trits) are packed into a single `uint8` byte using base-3 encoding, which is exact because `3 ** 5 == 243 <= 256`. This is the information-theoretic floor for ternary weights (`log2(3) ~= 1.58` bits/value) and is strictly denser than any integer format: ~2.5x denser than int4 and ~5x denser than int8, with no loss (the stored values are exactly the original `{-1, 0, +1}`).

Each trit `t` is shifted to an unsigned digit `d = t + 1` in `{0, 1, 2}`. Five consecutive digits `d0..d4` along `axis` are then combined into one byte as `d0 + 3*d1 + 9*d2 + 27*d3 + 81*d4` (max value `242`). If the axis length is not a multiple of 5 it is padded with zero-trits, which are removed on unpacking.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `arr` | A tensor whose values are in `{-1, 0, +1}` (any numeric dtype; values are rounded to the nearest integer and clipped to `[-1, 1]` before packing). |
| `axis` | The axis along which to pack the tensor. Defaults to 0. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `tuple` | A tuple `(packed, packed_shape, orig_len)` where `packed` is the packed `uint8` tensor, `packed_shape` is its shape, and `orig_len` is the original (unpadded) length of `axis`, needed by `unpack_ternary` to strip padding. |

#### Example:

> > > import numpy as np from keras.quantizers import pack\_ternary trits = np.array(\[\[1, -1, 0, 1, 1, -1\]\], dtype="int8") packed, packed\_shape, orig\_len = pack\_ternary(trits, axis=1) np.asarray(packed) # five trits per byte in base 3; axis 1 padded to 10 array(\[\[227, 120\]\], dtype=uint8) packed\_shape, orig\_len ((1, 2), 6)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.