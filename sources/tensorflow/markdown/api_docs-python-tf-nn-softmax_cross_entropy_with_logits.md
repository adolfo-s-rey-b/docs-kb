[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.softmax\_cross\_entropy\_with\_logits Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3994-L4054)

Computes softmax cross entropy between `logits` and `labels`.

tf.nn.softmax_cross_entropy_with_logits(
        labels, logits, axis=-1, name=None
    )

Measures the probability error in discrete classification tasks in which the classes are mutually exclusive (each entry is in exactly one class). For example, each CIFAR-10 image is labeled with one and only one label: an image can be a dog or a truck, but not both.

If using exclusive `labels` (wherein one and only one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

#### Usage:

    logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]

A common use case is to have logits and labels of shape `[batch_size, num_classes]`, but higher dimensions are supported, with the `axis` argument specifying the class dimension.

`logits` and `labels` must have the same dtype (either `float16`, `float32`, or `float64`).

Backpropagation will happen into both `logits` and `labels`. To disallow backpropagation into `labels`, pass label tensors through [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)
 before feeding it to this function.

**Note that to avoid confusion, it is required to pass only named arguments to this function.**

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | Each vector along the class dimension should hold a valid probability distribution e.g. for the case in which labels are of shape `[batch_size, num_classes]`, each row of `labels[i]` must be a valid probability distribution. |
| `logits` | Per-label activations, typically a linear output. These activation energies are interpreted as unnormalized log probabilities. |
| `axis` | The class dimension. Defaulted to -1 which is the last dimension. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` that contains the softmax cross entropy loss. Its type is the same as `logits` and its shape is the same as `labels` except that it does not have the last dimension of `labels`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.