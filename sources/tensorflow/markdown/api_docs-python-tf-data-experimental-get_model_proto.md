[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.get\_model\_proto Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/iterator_model_ops.py#L25-L56)

Gets the analytical model inside of `iterator` as `model_pb2.ModelProto`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.get_model_proto`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_model_proto)

tf.data.experimental.get_model_proto(
        iterator
    ) -> model_pb2.ModelProto

|     |     |
| --- | --- |
| Args<br>---- |     |
| `iterator` | An `iterator_ops.OwnedIterator` or `dataset_ops.NumpyIterator` |

|     |
| --- |
| Returns<br>------- |     |
| The model inside of this iterator as a model proto. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `NotFoundError` | If this iterator's autotune is not enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.