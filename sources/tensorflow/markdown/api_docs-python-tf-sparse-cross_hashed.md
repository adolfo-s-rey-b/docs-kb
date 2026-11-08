[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Fcross_hashed&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.cross\_hashed Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L666-L710)

Generates hashed sparse cross from a list of sparse and dense tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.cross_hashed`](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed)

tf.sparse.cross_hashed(
        inputs, num_buckets=0, hash_key=None, name=None
    )

For example, if the inputs are

* inputs[0]: SparseTensor with shape = [2, 2]
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
    * inputs[1]: SparseTensor with shape = [2, 1]
      [0, 0]: "d"
      [1, 0]: "e"
    * inputs[2]: Tensor [["f"], ["g"]]

then the output will be:

shape = [2, 2]
    [0, 0]: FingerprintCat64(
                Fingerprint64("f"), FingerprintCat64(
                    Fingerprint64("d"), Fingerprint64("a")))
    [1, 0]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("b")))
    [1, 1]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("c")))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | An iterable of `Tensor` or `SparseTensor`. |
| `num_buckets` | An `int` that is `>= 0`. output = hashed\_value%num\_buckets if num\_buckets > 0 else hashed\_value. |
| `hash_key` | Integer hash\_key that will be used by the `FingerprintCat64` function. If not given, will use a default key. |
| `name` | Optional name for the op. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` of type `int64`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.