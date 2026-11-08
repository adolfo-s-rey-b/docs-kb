[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.from\_variant Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L4566-L4578)

Constructs a dataset from the given variant and (nested) structure.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.from_variant`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_variant)

tf.data.experimental.from_variant(
        variant, structure
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `variant` | A scalar [`tf.variant`](https://www.tensorflow.org/api_docs/python/tf#variant)<br> tensor representing a dataset. |
| `structure` | A (nested) structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects representing the structure of each element in the dataset. |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.