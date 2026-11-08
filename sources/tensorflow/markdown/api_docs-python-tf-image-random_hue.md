[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/random_hue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/random_hue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.random\_hue Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/random_hue#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2643-L2689)

Adjust the hue of RGB images by a random factor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.random_hue`](https://www.tensorflow.org/api_docs/python/tf/image/random_hue)

tf.image.random_hue(
        image, max_delta, seed=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fine tuning models for plant disease detection](https://www.tensorflow.org/hub/tutorials/cropnet_on_device) |

Equivalent to `adjust_hue()` but uses a `delta` randomly picked in the interval `[-max_delta, max_delta)`.\
\
`max_delta` must be in the interval `[0, 0.5]`.\
\
#### Usage Example:\
\
    x = [[[1.0, 2.0, 3.0],\
\
For producing deterministic results given a `seed` value, use [`tf.image.stateless_random_hue`](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_hue)\
. Unlike using the `seed` param with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same results given the same seed independent of how many times the function is called, and independent of global seed settings (e.g. tf.random.set\_seed).\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `image` | RGB image or images. The size of the last dimension must be 3. |\
| `max_delta` | float. The maximum value for the random delta. |\
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
| `ValueError` | if `max_delta` is invalid. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.