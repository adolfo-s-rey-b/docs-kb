[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.at Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/at#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/random_access.py#L22-L73)

Returns the element at a specific index in a datasest.

tf.data.experimental.at(
        dataset, index
    )

Currently, random access is supported for the following tf.data operations:

*   [`tf.data.Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices)
    ,
*   [`tf.data.Dataset.from_tensors`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensors)
    ,
*   [`tf.data.Dataset.shuffle`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#shuffle)
    ,
*   [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)
    ,
*   [`tf.data.Dataset.shard`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#shard)
    ,
*   [`tf.data.Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
    ,
*   [`tf.data.Dataset.range`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#range)
    ,
*   [`tf.data.Dataset.zip`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#zip)
    ,
*   [`tf.data.Dataset.skip`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#skip)
    ,
*   [`tf.data.Dataset.repeat`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#repeat)
    ,
*   [`tf.data.Dataset.list_files`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#list_files)
    ,
*   `tf.data.Dataset.SSTableDataset`,
*   [`tf.data.Dataset.concatenate`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#concatenate)
    ,
*   [`tf.data.Dataset.enumerate`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#enumerate)
    ,
*   `tf.data.Dataset.parallel_map`,
*   [`tf.data.Dataset.prefetch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch)
    ,
*   [`tf.data.Dataset.take`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#take)
    ,
*   [`tf.data.Dataset.cache`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#cache)
     (in-memory only)
    
    Users can use the cache operation to enable random access for any dataset, even one comprised of transformations which are not on this list. E.g., to get the third element of a TFDS dataset:
    
     ds = tfds.load("mnist", split="train").cache()
         elem = tf.data.Dataset.experimental.at(ds, 3)
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> to determine whether it supports random access. |
| `index` | The index at which to fetch the element. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A (nested) structure of values matching [`tf.data.Dataset.element_spec`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#element_spec)<br>. |     |
| `Raises` | UnimplementedError: If random access is not yet supported for a dataset. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.