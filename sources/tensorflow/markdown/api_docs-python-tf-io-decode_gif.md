[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_gif Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif#returns)
    

Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_gif`](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_gif`](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)
, [`tf.compat.v1.io.decode_gif`](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)

tf.io.decode_gif(
        contents: Annotated[Any, _atypes.String], name=None
    ) -> Annotated[Any, _atypes.UInt8]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [MoveNet: Ultra fast and accurate pose detection model.](https://www.tensorflow.org/hub/tutorials/movenet)<br>    <br>*   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet) |

GIF images with frame or transparency compression are not supported. On Linux and MacOS systems, convert animated GIFs from compressed to uncompressed by running:

convert \\(src.gif -coalesce \\)dst.gif

This op also supports decoding JPEGs and PNGs, though it is cleaner to use [`tf.io.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The GIF-encoded image. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `uint8`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.