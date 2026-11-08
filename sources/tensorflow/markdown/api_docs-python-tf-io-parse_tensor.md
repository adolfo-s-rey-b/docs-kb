[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.parse\_tensor Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor#returns)
    

Transforms a serialized tensorflow.TensorProto proto into a Tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.parse_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor)
, [`tf.compat.v1.parse_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor)

tf.io.parse_tensor(
        serialized: Annotated[Any, _atypes.String],
        out_type: TV_ParseTensor_out_type,
        name=None
    ) -> Annotated[Any, TV_ParseTensor_out_type]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized` | A `Tensor` of type `string`. A scalar string containing a serialized TensorProto proto. |
| `out_type` | A [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. The type of the serialized tensor. The provided type must match the type of the serialized tensor and no implicit conversion will take place. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `out_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.