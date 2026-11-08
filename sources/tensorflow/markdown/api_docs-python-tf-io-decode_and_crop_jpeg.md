[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_and\_crop\_jpeg Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg#returns)
    

Decode and Crop a JPEG-encoded image to a uint8 tensor.

#### View aliases

**Main aliases**

[`tf.image.decode_and_crop_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_and_crop_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)
, [`tf.compat.v1.io.decode_and_crop_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)

tf.io.decode_and_crop_jpeg(
        contents: Annotated[Any, _atypes.String],
        crop_window: Annotated[Any, _atypes.Int32],
        channels: int = 0,
        ratio: int = 1,
        fancy_upscaling: bool = True,
        try_recover_truncated: bool = False,
        acceptable_fraction: float = 1,
        dct_method: str = '',
        name=None
    ) -> Annotated[Any, _atypes.UInt8]

The attr `channels` indicates the desired number of color channels for the decoded image.

#### Accepted values are:

*   0: Use the number of channels in the JPEG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.

If needed, the JPEG-encoded image is transformed to match the requested number of color channels.

The attr `ratio` allows downscaling the image by an integer factor during decoding. Allowed values are: 1, 2, 4, and 8. This is much faster than downscaling the image later.

It is equivalent to a combination of decode and crop, but much faster by only decoding partial jpeg image.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The JPEG-encoded image. |
| `crop_window` | A `Tensor` of type `int32`. 1-D. The crop window: \[crop\_y, crop\_x, crop\_height, crop\_width\]. |
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