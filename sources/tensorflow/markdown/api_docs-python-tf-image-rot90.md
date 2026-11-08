[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/rot90#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.rot90 Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L660-L723)

Rotate image(s) by 90 degrees.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.rot90`](https://www.tensorflow.org/api_docs/python/tf/image/rot90)

tf.image.rot90(
        image, k=1, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

#### For example:

    a=tf.constant([[[1],[2]],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |\
| `k` | A scalar integer tensor. The number of times the image(s) are rotated by 90 degrees. |\
| `name` | A name for this operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A rotated tensor of the same type and shape as `image`. |     |\
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