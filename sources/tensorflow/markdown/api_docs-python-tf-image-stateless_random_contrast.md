[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fstateless_random_contrast&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.stateless\_random\_contrast Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/stateless_random_contrast#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2160-L2204)

Adjust the contrast of images by a random factor deterministically.

tf.image.stateless_random_contrast(
        image, lower, upper, seed
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

Guarantees the same results given the same `seed` independent of how many times the function is called, and independent of global seed settings (e.g. [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | An image tensor with 3 or more dimensions. |
| `lower` | float. Lower bound for the random contrast factor. |
| `upper` | float. Upper bound for the random contrast factor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |

#### Usage Example:

    x = [[[1.0, 2.0, 3.0],\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The contrast-adjusted image(s). |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if `upper <= lower` or if `lower < 0`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.