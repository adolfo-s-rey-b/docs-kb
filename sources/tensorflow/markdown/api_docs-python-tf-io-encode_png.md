[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/encode_png?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.encode\_png Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_png#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3255-L3282)

PNG-encode an image.

#### View aliases

**Main aliases**

[`tf.image.encode_png`](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.encode_png`](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)
, [`tf.compat.v1.io.encode_png`](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)

tf.io.encode_png(
        image, compression=-1, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation) |

`image` is a rank-N Tensor of type uint8 or uint16 with shape `batch_dims + [height, width, channels]`, where `channels` is:

*   1: for grayscale.
*   2: for grayscale + alpha.
*   3: for RGB.
*   4: for RGBA.

The ZLIB compression level, `compression`, can be -1 for the PNG-encoder default or a value from 0 to 9. 9 is the highest compression level, generating the smallest output, but is slower.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | A `Tensor`. Must be one of the following types: `uint8`, `uint16`. Rank N >= 3 with shape `batch_dims + [height, width, channels]`. |
| `compression` | An optional `int`. Defaults to `-1`. Compression level. |
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

Last updated 2026-10-31 UTC.