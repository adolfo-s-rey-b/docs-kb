[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/audio/decode_wav#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.audio.decode\_wav Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

Decode a 16-bit PCM WAV file to a float tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.audio.decode_wav`](https://www.tensorflow.org/api_docs/python/tf/audio/decode_wav)

tf.audio.decode_wav(
        contents: Annotated[Any, _atypes.String],
        desired_channels: int = -1,
        desired_samples: int = -1,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio) |

The -32768 to 32767 signed 16-bit values will be scaled to -1.0 to 1.0 in float.

When desired\_channels is set, if the input contains fewer channels than this then the last channel will be duplicated to give the requested number, else if the input has more channels than requested then the additional channels will be ignored.

If desired\_samples is set, then the audio will be cropped or padded with zeroes to the requested length.

The first output contains a Tensor with the content of the audio samples. The lowest dimension will be the number of channels, and the second will be the number of samples. For example, a ten-sample-long stereo WAV file should give an output shape of \[10, 2\].

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. The WAV-encoded audio, usually from a file. |
| `desired_channels` | An optional `int`. Defaults to `-1`. Number of sample channels wanted. |
| `desired_samples` | An optional `int`. Defaults to `-1`. Length of audio requested. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (audio, sample\_rate). |     |
| `audio` | A `Tensor` of type `float32`. |
| `sample_rate` | A `Tensor` of type `int32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.