[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/lower#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/lower)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/lower?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/lower#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/lower#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/lower#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.lower Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/lower#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/lower#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/lower#returns)
    

Converts all uppercase characters into their respective lowercase replacements.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.lower`](https://www.tensorflow.org/api_docs/python/tf/strings/lower)

tf.strings.lower(
        input: Annotated[Any, _atypes.String],
        encoding: str = '',
        name=None
    ) -> Annotated[Any, _atypes.String]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)<br>    <br>*   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Warm-start embedding layer matrix](https://www.tensorflow.org/text/tutorials/warmstart_embedding_matrix)<br>    <br>*   [word2vec](https://www.tensorflow.org/text/tutorials/word2vec) |

#### Example:

    tf.strings.lower("CamelCase string and ALL CAPS")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The input to be lower-cased. |
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