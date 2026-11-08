[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.group\_by\_reducer Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/grouping.py#L28-L55)

A transformation that groups elements and performs a reduction.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.group_by_reducer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_reducer)

tf.data.experimental.group_by_reducer(
        key_func, reducer
    )

This transformation maps element of a dataset to a key using `key_func` and groups the elements by key. The `reducer` is used to process each group; its `init_func` is used to initialize state for each group when it is created, the `reduce_func` is used to update the state every time an element is mapped to the matching group, and the `finalize_func` is used to map the final state to an output value.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key_func` | A function mapping a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> tensor. |
| `reducer` | An instance of `Reducer`, which captures the reduction logic using the `init_func`, `reduce_func`, and `finalize_func` functions. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.