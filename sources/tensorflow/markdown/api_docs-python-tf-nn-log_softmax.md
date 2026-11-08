[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.log\_softmax Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3960-L3985)

Computes log softmax activations.

#### View aliases

**Main aliases**

[`tf.math.log_softmax`](https://www.tensorflow.org/api_docs/python/tf/nn/log_softmax)

tf.nn.log_softmax(
        logits, axis=None, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index) |

For each batch `i` and class `j` we have

logsoftmax = logits - log(reduce_sum(exp(logits), axis))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logits` | A non-empty `Tensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `axis` | The dimension softmax would be performed on. The default is -1 which indicates the last dimension. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `logits`. Same shape as `logits`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if `logits` is empty or `axis` is beyond the last dimension of `logits`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.