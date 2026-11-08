[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/as_string?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.as\_string Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/as_string#returns)
    

Converts each entry in the given tensor to strings.

#### View aliases

**Main aliases**

[`tf.as_string`](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.as_string`](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)
, [`tf.compat.v1.dtypes.as_string`](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)
, [`tf.compat.v1.strings.as_string`](https://www.tensorflow.org/api_docs/python/tf/strings/as_string)

tf.strings.as_string(
        input: Annotated[Any, TV_AsString_T],
        precision: int = -1,
        scientific: bool = False,
        shortest: bool = False,
        width: int = -1,
        fill: str = '',
        name=None
    ) -> Annotated[Any, _atypes.String]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating Keras 2 code to multi-backend Keras 3](https://www.tensorflow.org/guide/keras/migrating_to_keras_3)<br>    <br>*   [Signatures in TensorFlow Lite](https://www.tensorflow.org/lite/guide/signatures) | *   [Recommending movies: retrieval using a sequential model](https://www.tensorflow.org/recommenders/examples/sequential_retrieval)<br>    <br>*   [Using TensorFlow Recommenders with TFX](https://www.tensorflow.org/recommenders/examples/ranking_tfx)<br>    <br>*   [Unified Embedding Tables (UET)](https://www.tensorflow.org/recommenders/examples/uet)<br>    <br>*   [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras) |

Supports many numeric types and boolean.

For Unicode, see the [https://www.tensorflow.org/text/guide/unicode](https://www.tensorflow.org/api_docs/python/tf/strings/Working%20with%20Unicode%20text)
 tutorial.

#### Examples:

    tf.strings.as_string([3, 2])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `complex64`, `complex128`, `bool`, `variant`, `string`. |
| `precision` | An optional `int`. Defaults to `-1`. The post-decimal precision to use for floating point numbers. Only used if precision > -1. |
| `scientific` | An optional `bool`. Defaults to `False`. Use scientific notation for floating point numbers. Can't be specified to `True` when `shortest` is set to `True`. |
| `shortest` | An optional `bool`. Defaults to `False`. Use shortest representation (either scientific or standard) for floating point numbers. Can't be specified to `True` when `scientific` is set to `True`. |
| `width` | An optional `int`. Defaults to `-1`. Pad pre-decimal numbers to this width. Applies to both floating point and integer numbers. Only used if width > -1. |
| `fill` | An optional `string`. Defaults to `""`. The value to pad if width > -1. If empty, pads with spaces. Another typical value is '0'. String cannot be longer than 1 character. |
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

Last updated 2026-11-05 UTC.