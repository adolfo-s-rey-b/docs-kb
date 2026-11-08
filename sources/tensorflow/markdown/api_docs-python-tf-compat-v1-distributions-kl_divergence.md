[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.distributions.kl\_divergence Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/distributions/kullback_leibler.py#L51-L118)

Get the KL-divergence KL(distribution\_a || distribution\_b). (deprecated)

tf.compat.v1.distributions.kl_divergence(
        distribution_a, distribution_b, allow_nan_stats=True, name=None
    )

If there is no KL method registered specifically for `type(distribution_a)` and `type(distribution_b)`, then the class hierarchies of these types are searched.

If one KL method is registered between any pairs of classes in these two parent hierarchies, it is used.

If more than one such registered method exists, the method whose registered classes have the shortest sum MRO paths to the input types is used.

If more than one such shortest path exists, the first method identified in the search is used (favoring a shorter MRO distance to `type(distribution_a)`).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `distribution_a` | The first distribution. |
| `distribution_b` | The second distribution. |
| `allow_nan_stats` | Python `bool`, default `True`. When `True`, statistics (e.g., mean, mode, variance) use the value "`NaN`" to indicate the result is undefined. When `False`, an exception is raised if one or more of the statistic's batch members are undefined. |
| `name` | Python `str` name prefixed to Ops created by this class. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor with the batchwise KL-divergence between `distribution_a` and `distribution_b`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `NotImplementedError` | If no KL method is defined for distribution types of `distribution_a` and `distribution_b`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.