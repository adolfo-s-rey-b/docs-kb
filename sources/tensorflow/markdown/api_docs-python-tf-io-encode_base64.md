[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.encode\_base64 Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64#returns)
    

Encode strings into web-safe base64 format.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.encode_base64`](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64)
, [`tf.compat.v1.io.encode_base64`](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64)

tf.io.encode_base64(
        input: Annotated[Any, _atypes.String], pad: bool = False, name=None
    ) -> Annotated[Any, _atypes.String]

Refer to [this article](https://en.wikipedia.org/wiki/Base64)
 for more information on base64 format. Base64 strings may have padding with '=' at the end so that the encoded has length multiple of 4. See Padding section of the link above.

Web-safe means that the encoder uses - and \_ instead of + and /.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. Strings to be encoded. |
| `pad` | An optional `bool`. Defaults to `False`. Bool whether padding is applied at the ends. |
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