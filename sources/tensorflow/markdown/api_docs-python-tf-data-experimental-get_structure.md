[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.get\_structure Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L4401-L4439)

Returns the type signature for elements of the input dataset / iterator.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.get_structure`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_structure)

tf.data.experimental.get_structure(
        dataset_or_iterator
    )

For example, to get the structure of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
:

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

    dataset = tf.data.experimental.from_list([(1, 'a'), (2, 'b'), (3, 'c')])

To get the structure of an [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)
:

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset_or_iterator` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> or an [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A (nested) structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects matching the structure of an element of `dataset_or_iterator` and specifying the type of individual components. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If input is not a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> or an [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> object. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.