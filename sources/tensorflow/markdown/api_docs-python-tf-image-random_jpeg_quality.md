[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.random\_jpeg\_quality Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2819-L2870)

Randomly changes jpeg encoding quality for inducing jpeg noise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.random_jpeg_quality`](https://www.tensorflow.org/api_docs/python/tf/image/random_jpeg_quality)

tf.image.random_jpeg_quality(
        image, min_jpeg_quality, max_jpeg_quality, seed=None
    )

`min_jpeg_quality` must be in the interval `[0, 100]` and less than `max_jpeg_quality`. `max_jpeg_quality` must be in the interval `[0, 100]`.

#### Usage Example:

    x = tf.constant([[[1, 2, 3],\
\
For producing deterministic results given a `seed` value, use [`tf.image.stateless_random_jpeg_quality`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_jpeg_quality)\
. Unlike using the `seed` param with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same results given the same seed independent of how many times the function is called, and independent of global seed settings (e.g. tf.random.set\_seed).\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | 3D image. Size of the last dimension must be 1 or 3. |\
| `min_jpeg_quality` | Minimum jpeg encoding quality to use. |\
| `max_jpeg_quality` | Maximum jpeg encoding quality to use. |\
| `seed` | An operation-specific seed. It will be used in conjunction with the graph-level seed to determine the real seeds that will be used in this operation. Please see the documentation of set\_random\_seed for its interaction with the graph-level random seed. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Adjusted image(s), same shape and DType as `image`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if `min_jpeg_quality` or `max_jpeg_quality` is invalid. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.