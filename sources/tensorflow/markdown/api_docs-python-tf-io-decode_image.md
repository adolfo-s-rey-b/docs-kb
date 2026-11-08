[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_image Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_image#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3285-L3361)

Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

#### View aliases

**Main aliases**

[`tf.image.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
, [`tf.compat.v1.io.decode_image`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)

tf.io.decode_image(
        contents,
        channels=None,
        dtype=tf.dtypes.uint8,
        name=None,
        expand_animations=True
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Image Super Resolution using ESRGAN](https://www.tensorflow.org/hub/tutorials/image_enhancing)<br>    <br>*   [Fast Style Transfer for Arbitrary Styles](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization)<br>    <br>*   [Frame interpolation using the FILM model](https://www.tensorflow.org/hub/tutorials/tf_hub_film_example) |

Detects whether an image is a BMP, GIF, JPEG, JPEG XL, WebP or PNG, and performs the appropriate operation to convert the input bytes `string` into a `Tensor` of type `dtype`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `contents` | A `Tensor` of type `string`. 0-D. The encoded image bytes. |
| `channels` | An optional `int`. Defaults to `0`. Number of color channels for the decoded image. |
| `dtype` | The desired DType of the returned `Tensor`. |
| `name` | A name for the operation (optional) |
| `expand_animations` | An optional `bool`. Defaults to `True`. Controls the shape of the returned op's output. If `True`, the returned op will produce a 4-D tensor for all GIFs and WebP images, animated or not, and a 3-D tensor in all other cases. If, `False`, the returned op will produce a 3-D tensor for all file types and will truncate animations to the first frame. |

|     |
| --- |
| Returns<br>------- |     |
| `Tensor` with type `dtype` and a 3- or 4-dimensional shape, depending on the file type and the value of the `expand_animations` parameter. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | On incorrect number of channels. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.