[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.sparse\_softmax\_cross\_entropy\_with\_logits Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4284-L4404)

Computes sparse softmax cross entropy between `logits` and `labels`.

tf.compat.v1.nn.sparse_softmax_cross_entropy_with_logits(
        labels=None, logits=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers) | *   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings) |

Measures the probability error in discrete classification tasks in which the classes are mutually exclusive (each entry is in exactly one class). For example, each CIFAR-10 image is labeled with one and only one label: an image can be a dog or a truck, but not both.

A common use case is to have logits of shape `[batch_size, num_classes]` and have labels of shape `[batch_size]`, but higher dimensions are supported, in which case the `dim`\-th dimension is assumed to be of size `num_classes`. `logits` must have the dtype of `float16`, `float32`, or `float64`, and `labels` must have the dtype of `int32` or `int64`.

**Note that to avoid confusion, it is required to pass only named arguments to this function.**

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of `labels` and result) and dtype `int32` or `int64`. Each entry in `labels` must be an index in `[0, num_classes)`. Other values will raise an exception when this op is run on CPU, and return `NaN` for corresponding loss and gradient rows on GPU. |\
| `logits` | Per-label activations (typically a linear output) of shape `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32`, or `float64`. These activation energies are interpreted as unnormalized log probabilities. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` of the same shape as `labels` and of the same type as `logits` with the softmax cross entropy loss. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If logits are scalars (need to have rank >= 1) or if the rank of the labels is not equal to the rank of the logits minus one. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.