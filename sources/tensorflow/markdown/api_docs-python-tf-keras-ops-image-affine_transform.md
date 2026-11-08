[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.affine\_transform Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/affine_transform#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L475-L572)

Applies the given transform(s) to the image(s).

tf.keras.ops.image.affine_transform(
        images,
        transform,
        interpolation='bilinear',
        fill_mode='constant',
        fill_value=0,
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input image or batch of images. Must be 3D or 4D. |
| `transform` | Projective transform matrix/matrices. A vector of length 8 or tensor of size N x 8. If one row of transform is `[a0, a1, a2, b0, b1, b2, c0, c1]`, then it maps the output point `(x, y)` to a transformed input point `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`, where `k = c0 x + c1 y + 1`. The transform is inverted compared to the transform mapping input points to output points. Note that gradients are not backpropagated into transformation parameters. Note that `c0` and `c1` are only effective when using TensorFlow backend and will be considered as `0` when using other backends. |
| `interpolation` | Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`. |
| `fill_mode` | Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.<br><br>*   `"reflect"`: `(d c b a \| a b c d \| d c b a)` The input is extended by reflecting about the edge of the last pixel.<br>*   `"constant"`: `(k k k k \| a b c d \| k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.<br>*   `"wrap"`: `(a b c d \| a b c d \| a b c d)` The input is extended by wrapping around to the opposite edge.<br>*   `"nearest"`: `(a a a a \| a b c d \| d d d d)` The input is extended by the nearest pixel. |
| `fill_value` | Value used for points outside the boundaries of the input if `fill_mode="constant"`. Defaults to `0`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Applied affine transform image or batch of images. |     |

#### Examples:

    x = np.random.random((2, 64, 80, 3)) # batch of 2 RGB images

    x = np.random.random((64, 80, 3)) # single RGB image

    x = np.random.random((2, 3, 64, 80)) # batch of 2 RGB images

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.