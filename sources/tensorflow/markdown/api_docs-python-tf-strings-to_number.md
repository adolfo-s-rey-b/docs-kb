[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/to_number)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/to_number?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.to\_number Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_number#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L462-L488)

Converts each string in the input Tensor to the specified numeric type.

tf.strings.to_number(
        input,
        out_type=tf.dtypes.float32,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Migrating Keras 2 code to multi-backend Keras 3](https://www.tensorflow.org/guide/keras/migrating_to_keras_3)<br>    <br>*   [Signatures in TensorFlow Lite](https://www.tensorflow.org/lite/guide/signatures) | *   [Robust machine learning on streaming data using Kafka and Tensorflow-IO](https://www.tensorflow.org/io/tutorials/kafka)<br>    <br>*   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select) |

(Note that int32 overflow results in an error while float overflow results in a rounded value.)

#### Examples:

    tf.strings.to_number("1.55")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. |
| `out_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.float32, tf.float64, tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to `tf.float32`. The numeric type to interpret each string in `string_tensor` as. |
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

Last updated 2026-10-31 UTC.