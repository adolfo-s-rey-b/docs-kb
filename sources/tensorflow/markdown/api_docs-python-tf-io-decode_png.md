[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_png?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_png Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_png#returns)
    

Decode a PNG-encoded image to a uint8 or uint16 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_png`](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_png`](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)
, [`tf.compat.v1.io.decode_png`](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)

tf.io.decode_png(
        contents: Annotated[Any, _atypes.String],
        channels: int = 0,
        dtype: TV_DecodePng_dtype = tf.dtypes.uint8,
        name=None
    ) -> Annotated[Any, TV_DecodePng_dtype]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) | *   [Displaying image data in TensorBoard](https://www.tensorflow.org/tensorboard/image_summaries) |

The attr `channels` indicates the desired number of color channels for the decoded image.

#### Accepted values are:

*   0: Use the number of channels in the PNG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.
*   4: output an RGBA image.

If needed, the PNG-encoded image is transformed to match the requested number of color channels.

This op also supports decoding JPEGs and non-animated GIFs since the interface is the same, though it is cleaner to use [`tf.io.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The PNG-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `dtype` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.uint8, tf.uint16`. Defaults to [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)<br>. |
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

Last updated 2024-04-26 UTC.