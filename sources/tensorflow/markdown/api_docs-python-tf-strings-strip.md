[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/strip#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/strip)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/strip?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/strip#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/strip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/strip#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.strip Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/strip#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/strip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/strip#returns)
    

Strip leading and trailing whitespaces from the Tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.string_strip`](https://www.tensorflow.org/api_docs/python/tf/strings/strip)
, [`tf.compat.v1.strings.strip`](https://www.tensorflow.org/api_docs/python/tf/strings/strip)

tf.strings.strip(
        input: Annotated[Any, _atypes.String], name=None
    ) -> Annotated[Any, _atypes.String]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery)<br>    <br>*   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras)<br>    <br>*   [](https://www.tensorflow.org/tfx/transform/get_started) |

#### Examples:

    tf.strings.strip(["\nTensorFlow", "     The python library    "]).numpy()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. A string `Tensor` of any shape. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `string`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.