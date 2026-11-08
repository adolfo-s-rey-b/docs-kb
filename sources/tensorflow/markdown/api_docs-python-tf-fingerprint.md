[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/fingerprint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/fingerprint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/fingerprint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/fingerprint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/fingerprint#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.fingerprint Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/fingerprint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/fingerprint#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6415-L6462)

Generates fingerprint values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.fingerprint`](https://www.tensorflow.org/api_docs/python/tf/fingerprint)

tf.fingerprint(
        data, method='farmhash64', name=None
    )

Generates fingerprint values of `data`.

Fingerprint op considers the first dimension of `data` as the batch dimension, and `output[i]` contains the fingerprint value generated from contents in `data[i, ...]` for all `i`.

Fingerprint op writes fingerprint values as byte arrays. For example, the default method `farmhash64` generates a 64-bit fingerprint value at a time. This 8-byte value is written out as an [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)
 array of size 8, in little-endian order.

For example, suppose that `data` has data type [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)
 and shape (2, 3, 4), and that the fingerprint method is `farmhash64`. In this case, the output shape is (2, 8), where 2 is the batch dimension size of `data`, and 8 is the size of each fingerprint value in bytes. `output[0, :]` is generated from 12 integers in `data[0, :, :]` and similarly `output[1, :]` is generated from other 12 integers in `data[1, :, :]`.

Note that this op fingerprints the raw underlying buffer, and it does not fingerprint Tensor's metadata such as data type and/or shape. For example, the fingerprint values are invariant under reshapes and bitcasts as long as the batch dimension remain the same:

tf.fingerprint(data) == tf.fingerprint(tf.reshape(data, ...))
    tf.fingerprint(data) == tf.fingerprint(tf.bitcast(data, ...))

For string data, one should expect `tf.fingerprint(data) != tf.fingerprint(tf.string.reduce_join(data))` in general.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor`. Must have rank 1 or higher. |
| `method` | A `Tensor` of type [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br>. Fingerprint method used by this op. Currently, available method is `farmhash64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A two-dimensional `Tensor` of type [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)<br>. The first dimension equals to `data`'s first dimension, and the second dimension size depends on the fingerprint algorithm. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.