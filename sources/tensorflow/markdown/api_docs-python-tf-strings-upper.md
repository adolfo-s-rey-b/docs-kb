[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/upper#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/upper)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/upper?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/upper#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/upper#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.upper Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/upper#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/upper#returns)
    

Converts all lowercase characters into their respective uppercase replacements.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.upper`](https://www.tensorflow.org/api_docs/python/tf/strings/upper)

tf.strings.upper(
        input: Annotated[Any, _atypes.String],
        encoding: str = '',
        name=None
    ) -> Annotated[Any, _atypes.String]

#### Example:

    tf.strings.upper("CamelCase string and ALL CAPS")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The input to be upper-cased. |
| `encoding` | An optional `string`. Defaults to `""`. Character encoding of `input`. Allowed values are '' and 'utf-8'. Value '' is interpreted as ASCII. |
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