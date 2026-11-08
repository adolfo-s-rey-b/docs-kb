[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Faudio%2Fencode_wav&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.audio.encode\_wav Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav#returns)
    

Encode audio data using the WAV file format.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.audio.encode_wav`](https://www.tensorflow.org/api_docs/python/tf/audio/encode_wav)

tf.audio.encode_wav(
        audio: Annotated[Any, _atypes.Float32],
        sample_rate: Annotated[Any, _atypes.Int32],
        name=None
    ) -> Annotated[Any, _atypes.String]

This operation will generate a string suitable to be saved out to create a .wav audio file. It will be encoded in the 16-bit PCM format. It takes in float values in the range -1.0f to 1.0f, and any outside that value will be clamped to that range.

`audio` is a 2-D float Tensor of shape `[length, channels]`. `sample_rate` is a scalar Tensor holding the rate to use (e.g. 44100).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `audio` | A `Tensor` of type `float32`. 2-D with shape `[length, channels]`. |
| `sample_rate` | A `Tensor` of type `int32`. Scalar containing the sample frequency. |
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