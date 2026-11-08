[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/relu6)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/relu6?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.relu6 Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/relu6#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3630-L3664)

Computes Rectified Linear 6: `min(max(features, 0), 6)`.

tf.nn.relu6(
        features, name=None
    )

In comparison with [`tf.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
, relu6 activation functions have shown to empirically perform better under low-precision conditions (e.g. fixed point inference) by encouraging the model to learn sparse features earlier. Source: [Convolutional Deep Belief Networks on CIFAR-10: Krizhevsky et al., 2010](http://www.cs.utoronto.ca/%7Ekriz/conv-cifar10-aug2010.pdf)
.

#### For example:

    x = tf.constant([-3.0, -1.0, 0.0, 6.0, 10.0], dtype=tf.float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`, `int16`, or `int8`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `features`. |     |

|     |
| --- |
| References<br>---------- |     |
| Convolutional Deep Belief Networks on CIFAR-10: Krizhevsky et al., 2010 ([pdf](http://www.cs.utoronto.ca/%7Ekriz/conv-cifar10-aug2010.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.