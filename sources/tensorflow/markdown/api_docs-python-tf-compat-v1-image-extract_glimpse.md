[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_glimpse#main-content)

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
    

tf.compat.v1.image.extract\_glimpse Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4989-L5072)

Extracts a glimpse from the input tensor.

tf.compat.v1.image.extract_glimpse(
        input,
        size,
        offsets,
        centered=True,
        normalized=True,
        uniform_noise=True,
        name=None
    )

Returns a set of windows called glimpses extracted at location `offsets` from the input tensor. If the windows only partially overlaps the inputs, the non-overlapping areas will be filled with random noise.

The result is a 4-D tensor of shape `[batch_size, glimpse_height, glimpse_width, channels]`. The channels and batch dimensions are the same as that of the input tensor. The height and width of the output windows are specified in the `size` parameter.

The argument `normalized` and `centered` controls how the windows are built:

*   If the coordinates are normalized but not centered, 0.0 and 1.0 correspond to the minimum and maximum of each height and width dimension.
*   If the coordinates are both normalized and centered, they range from -1.0 to 1.0. The coordinates (-1.0, -1.0) correspond to the upper left corner, the lower right corner is located at (1.0, 1.0) and the center is at (0, 0).
*   If the coordinates are not normalized they are interpreted as numbers of pixels.

#### Usage Example:

    x = [[[[0.0],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | A `Tensor` of type `float32`. A 4-D float tensor of shape `[batch_size, height, width, channels]`. |\
| `size` | A `Tensor` of type `int32`. A 1-D tensor of 2 elements containing the size of the glimpses to extract. The glimpse height must be specified first, following by the glimpse width. |\
| `offsets` | A `Tensor` of type `float32`. A 2-D integer tensor of shape `[batch_size, 2]` containing the y, x locations of the center of each window. |\
| `centered` | An optional `bool`. Defaults to `True`. indicates if the offset coordinates are centered relative to the image, in which case the (0, 0) offset is relative to the center of the input images. If false, the (0,0) offset corresponds to the upper left corner of the input images. |\
| `normalized` | An optional `bool`. Defaults to `True`. indicates if the offset coordinates are normalized. |\
| `uniform_noise` | An optional `bool`. Defaults to `True`. indicates if the noise should be generated using a uniform distribution or a Gaussian distribution. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` of type `float32`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.