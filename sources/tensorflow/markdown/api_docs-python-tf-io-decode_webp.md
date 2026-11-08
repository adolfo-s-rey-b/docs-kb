[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_webp Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp#returns)
    

Decode a WebP-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_webp`](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_webp`](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)
, [`tf.compat.v1.io.decode_webp`](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)

tf.io.decode_webp(
        contents: Annotated[Any, _atypes.String],
        channels: int = 0,
        dtype: TV_DecodeWebP_dtype = tf.dtypes.uint8,
        name=None
    ) -> Annotated[Any, TV_DecodeWebP_dtype]

The attr `channels` indicates the desired number of color channels for the decoded image.

#### Accepted values are:

*   0: Use the number of channels in the WebP-encoded image.
*   3: output an RGB image.
*   4: output an RGBA image.

The number of channels must currently match that of the underlying file. For WebP animations, only 4-channel RGBA is supported.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The WebP-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `dtype` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)<br>. Defaults to [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)<br>. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `dtype`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.