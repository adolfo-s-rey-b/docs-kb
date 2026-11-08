[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Frelu_layer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.relu\_layer Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/relu_layer#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L407-L428)

Computes Relu(x \* weight + biases).

tf.compat.v1.nn.relu_layer(
        x, weights, biases, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | a 2D tensor. Dimensions typically: batch, in\_units |
| `weights` | a 2D tensor. Dimensions typically: in\_units, out\_units |
| `biases` | a 1D tensor. Dimensions: out\_units |
| `name` | A name for the operation (optional). If not specified "nn\_relu\_layer" is used. |

|     |
| --- |
| Returns<br>------- |     |
| A 2-D Tensor computing relu(matmul(x, weights) + biases). Dimensions typically: batch, out\_units. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.