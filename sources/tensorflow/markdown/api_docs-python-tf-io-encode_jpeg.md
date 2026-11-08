[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.encode\_jpeg Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg#returns)
    

JPEG-encode an image.

#### View aliases

**Main aliases**

[`tf.image.encode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.encode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)
, [`tf.compat.v1.io.encode_jpeg`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)

tf.io.encode_jpeg(
        image: Annotated[Any, _atypes.UInt8],
        format: str = '',
        quality: int = 95,
        progressive: bool = False,
        optimize_size: bool = False,
        chroma_downsampling: bool = True,
        density_unit: str = 'in',
        x_density: int = 300,
        y_density: int = 300,
        xmp_metadata: str = '',
        name=None
    ) -> Annotated[Any, _atypes.String]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation) |

`image` is a 3-D uint8 Tensor of shape `[height, width, channels]`.

The attr `format` can be used to override the color format of the encoded output. Values can be:

*   `''`: Use a default format based on the number of channels in the image.
*   `grayscale`: Output a grayscale JPEG image. The `channels` dimension of `image` must be 1.
*   `rgb`: Output an RGB JPEG image. The `channels` dimension of `image` must be 3.

If `format` is not specified or is the empty string, a default format is picked in function of the number of channels in `image`:

*   1: Output a grayscale image.
*   3: Output an RGB image.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | A `Tensor` of type `uint8`. 3-D with shape `[height, width, channels]`. |
| `format` | An optional `string` from: `"", "grayscale", "rgb"`. Defaults to `""`. Per pixel image format. |
| `quality` | An optional `int`. Defaults to `95`. Quality of the compression from 0 to 100 (higher is better and slower). |
| `progressive` | An optional `bool`. Defaults to `False`. If True, create a JPEG that loads progressively (coarse to fine). |
| `optimize_size` | An optional `bool`. Defaults to `False`. If True, spend CPU/RAM to reduce size with no quality change. |
| `chroma_downsampling` | An optional `bool`. Defaults to `True`. See http://en.wikipedia.org/wiki/Chroma\_subsampling. |
| `density_unit` | An optional `string` from: `"in", "cm"`. Defaults to `"in"`. Unit used to specify `x_density` and `y_density`: pixels per inch (`'in'`) or centimeter (`'cm'`). |
| `x_density` | An optional `int`. Defaults to `300`. Horizontal pixels per density unit. |
| `y_density` | An optional `int`. Defaults to `300`. Vertical pixels per density unit. |
| `xmp_metadata` | An optional `string`. Defaults to `""`. If not empty, embed this XMP metadata in the image header. |
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