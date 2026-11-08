[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.flip\_left\_right Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L548-L580)

Flip an image horizontally (left to right).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.flip_left_right`](https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right)

tf.image.flip_left_right(
        image
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

Outputs the contents of `image` flipped along the width dimension.

See also [`tf.reverse`](https://www.tensorflow.org/api_docs/python/tf/reverse)
.

#### Usage Example:

    x = [[[1.0, 2.0, 3.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A tensor of the same type and shape as `image`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if the shape of `image` not supported. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.