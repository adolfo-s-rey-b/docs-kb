[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.initializers.lecun\_normal Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L1682-L1707)

LeCun normal initializer.

tf.compat.v1.initializers.lecun_normal(
        seed=None
    )

It draws samples from a truncated normal distribution centered on 0 with standard deviation (after truncation) given by `stddev = sqrt(1 / fan_in)` where `fan_in` is the number of input units in the weight tensor.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | A Python integer. Used to seed the random generator. |

|     |
| --- |
| Returns<br>------- |     |
| An initializer. |     |

|     |
| --- |
| References<br>---------- |     |
| *   Self-Normalizing Neural Networks, [Klambauer et al., 2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)<br>    <br><br>([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf)<br>)<br><br>*   Efficient Backprop, [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.