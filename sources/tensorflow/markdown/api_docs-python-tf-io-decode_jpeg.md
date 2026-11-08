[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_jpeg Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg#returns)
    

Decode a JPEG-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)
, [`tf.compat.v1.io.decode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)

tf.io.decode_jpeg(
        contents: Annotated[Any, _atypes.String],
        channels: int = 0,
        ratio: int = 1,
        fancy_upscaling: bool = True,
        try_recover_truncated: bool = False,
        acceptable_fraction: float = 1,
        dct_method: str = '',
        name=None
    ) -> Annotated[Any, _atypes.UInt8]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) | *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Load and preprocess images](https://www.tensorflow.org/tutorials/load_data/images)<br>    <br>*   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification) |

The attr `channels` indicates the desired number of color channels for the decoded image.

#### Accepted values are:

*   0: Use the number of channels in the JPEG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.

If needed, the JPEG-encoded image is transformed to match the requested number of color channels.

The attr `ratio` allows downscaling the image by an integer factor during decoding. Allowed values are: 1, 2, 4, and 8. This is much faster than downscaling the image later.

This op also supports decoding PNGs and non-animated GIFs since the interface is the same, though it is cleaner to use [`tf.io.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The JPEG-encoded image. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `ratio` | An optional `int`. Defaults to `1`. Downscaling ratio. |
| `fancy_upscaling` | An optional `bool`. Defaults to `True`. If true use a slower but nicer upscaling of the chroma planes (yuv420/422 only). |
| `try_recover_truncated` | An optional `bool`. Defaults to `False`. If true try to recover an image from truncated input. |
| `acceptable_fraction` | An optional `float`. Defaults to `1`. The minimum required fraction of lines before a truncated input is accepted. |
| `dct_method` | An optional `string`. Defaults to `""`. string specifying a hint about the algorithm used for decompression. Defaults to "" which maps to a system-specific default. Currently valid values are \["INTEGER\_FAST", "INTEGER\_ACCURATE"\]. The hint may be ignored (e.g., the internal jpeg library changes to a version that does not have that specific option.) |
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