[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fragged%2Fcross_hashed&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.cross\_hashed Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_array_ops.py#L768-L802)

Generates hashed feature cross from a list of tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.cross_hashed`](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed)

tf.ragged.cross_hashed(
        inputs, num_buckets=0, hash_key=None, name=None
    )

The input tensors must have `rank=2`, and must all have the same number of rows. The result is a `RaggedTensor` with the same number of rows as the inputs, where `result[row]` contains a list of all combinations of values formed by taking a single value from each input's corresponding row (`inputs[i][row]`). Values are combined by hashing together their fingerprints. E.g.:

    tf.ragged.cross_hashed([tf.ragged.constant([['a'], ['b', 'c']]),\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `inputs` | A list of `RaggedTensor` or `Tensor` or `SparseTensor`. |\
| `num_buckets` | A non-negative `int` that used to bucket the hashed values. If `num_buckets != 0`, then `output = hashed_value % num_buckets`. |\
| `hash_key` | Integer hash\_key that will be used by the `FingerprintCat64` function. If not given, a default key is used. |\
| `name` | Optional name for the op. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A 2D `RaggedTensor` of type `int64`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.