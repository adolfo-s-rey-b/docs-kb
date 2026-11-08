[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.encode\_jxl Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/image_ops_impl.py#L3341-L3387)

JPEG XL-encode an image.

#### View aliases

**Main aliases**

[`tf.image.encode_jxl`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.encode_jxl`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl)
, [`tf.compat.v1.io.encode_jxl`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jxl)

tf.io.encode_jxl(
        image, quality=95.0, effort=7, name=None
    )

`image` is a rank-N Tensor of type uint8 or uint16 with shape `batch_dims + [height, width, channels]`, where `channels` is:

*   1: for grayscale.
*   3: for RGB.
*   4: for RGBA.

`quality` is a JPEG-style quality factor in `[0.0, 100.0]`. It is mapped internally to a JPEG XL Butteraugli distance using the same mapping as `cjxl -q`: `100.0` encodes losslessly, `95.0` (the default) is high-quality lossy encoding matching `encode_jpeg`, `90.0` is visually lossless, and lower values compress more. Quality factors are not comparable across codecs, so a given `quality` will not produce the same file size or visual quality as the same value passed to [`tf.io.encode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)
.

The `effort` parameter (1 to 9) controls compression effort (default 7).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | A `Tensor`. Must be one of the following types: `uint8`, `uint16`. Rank N >= 3 with shape `batch_dims + [height, width, channels]`. |
| `quality` | An optional `float`. Defaults to `95.0`. Quality factor in `[0.0, 100.0]`; `100.0` encodes losslessly, `95.0` is high-quality lossy, and lower values compress more. |
| `effort` | An optional `int`. Defaults to `7`. Effort setting from 1 (fastest) to 9 (slowest, best compression). |
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