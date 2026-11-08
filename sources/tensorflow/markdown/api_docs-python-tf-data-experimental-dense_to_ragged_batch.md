[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.dense\_to\_ragged\_batch Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/batching.py#L30-L91)

A transformation that batches ragged elements into [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.dense_to_ragged_batch`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_ragged_batch)

tf.data.experimental.dense_to_ragged_batch(
        batch_size,
        drop_remainder=False,
        row_splits_dtype=tf.dtypes.int64
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Recommend movies for users with TensorFlow Ranking](https://www.tensorflow.org/ranking/tutorials/quickstart) |

This transformation combines multiple consecutive elements of the input dataset into a single element.

Like [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)
, the components of the resulting element will have an additional outer dimension, which will be `batch_size` (or `N % batch_size` for the last element if `batch_size` does not divide the number of input elements `N` evenly and `drop_remainder` is `False`). If your program depends on the batches having the same outer dimension, you should set the `drop_remainder` argument to `True` to prevent the smaller batch from being produced.

Unlike [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)
, the input elements to be batched may have different shapes:

*   If an input element is a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     whose static [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)
     is fully defined, then it is batched as normal.
*   If an input element is a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     whose static [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)
     contains one or more axes with unknown size (i.e., `shape[i]=None`), then the output will contain a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
     that is ragged up to any of such dimensions.
*   If an input element is a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
     or any other type, then it is batched as normal.

#### Example:

    dataset = tf.data.Dataset.from_tensor_slices(np.arange(6))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |
| `row_splits_dtype` | The dtype that should be used for the `row_splits` of any new ragged tensors. Existing [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> elements do not have their row\_splits dtype changed. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Dataset` | A `Dataset`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.