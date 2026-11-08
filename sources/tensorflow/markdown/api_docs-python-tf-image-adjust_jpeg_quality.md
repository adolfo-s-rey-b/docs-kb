[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.adjust\_jpeg\_quality Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2929-L3010)

Adjust jpeg encoding quality of an image.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.adjust_jpeg_quality`](https://www.tensorflow.org/api_docs/python/tf/image/adjust_jpeg_quality)

tf.image.adjust_jpeg_quality(
        image, jpeg_quality, dct_method='', name=None
    )

This is a convenience method that converts an image to uint8 representation, encodes it to jpeg with `jpeg_quality`, decodes it, and then converts back to the original data type.

`jpeg_quality` must be in the interval `[0, 100]`.

#### Usage Examples:

    x = [[[0.01, 0.02, 0.03],\
\
Note that floating point values are expected to have values in the range \[0,1) and values outside this range are clipped.\
\
    x = [[[1.0, 2.0, 3.0],\
\
Note that `jpeg_quality` 100 is still lossy compression.\
\
    x = tf.constant([[[1, 2, 3],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | 3D image. The size of the last dimension must be None, 1 or 3. |\
| `jpeg_quality` | Python int or Tensor of type int32. jpeg encoding quality. |\
| `dct_method` | An optional string. Specifies the DCT method to use for JPEG decompression. Currently available options are \["INTEGER\_FAST", "INTEGER\_ACCURATE"\]. Defaults to "" which maps to "INTEGER\_FAST", sacrificing image quality for speed. |\
| `name` | A name for this operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Adjusted image, same shape and DType as `image`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `InvalidArgumentError` | quality must be in \[0,100\] |\
| `InvalidArgumentError` | image must have 1 or 3 channels |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.