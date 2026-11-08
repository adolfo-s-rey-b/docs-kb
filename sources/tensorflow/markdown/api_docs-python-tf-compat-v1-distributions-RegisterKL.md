[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.distributions.RegisterKL Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/kullback_leibler.py#L161-L210)

Decorator to register a KL divergence implementation function.

tf.compat.v1.distributions.RegisterKL(
        dist_cls_a, dist_cls_b
    )

#### Usage:

@distributions.RegisterKL(distributions.Normal, distributions.Normal) def \_kl\_normal\_mvn(norm\_a, norm\_b): # Return KL(norm\_a || norm\_b)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dist_cls_a` | the class of the first argument of the KL divergence. |
| `dist_cls_b` | the class of the second argument of the KL divergence. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/kullback_leibler.py#L189-L210)

__call__(
        kl_fn
    )

Perform the KL registration.

|     |     |
| --- | --- |
| Args |     |
| `kl_fn` | The function to use for the KL divergence. |

|     |
| --- |
| Returns |     |
| kl\_fn |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if kl\_fn is not a callable. |
| `ValueError` | if a KL divergence function has already been registered for the given argument classes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.